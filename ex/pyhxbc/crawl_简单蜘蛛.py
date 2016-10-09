# 使用这些模块中不同的类来解析html
import cStringIO
import formatter
from htmllib import HTMLParser
# 使用httplib中定义的一个异常
import httplib
#该模块提供了许多文件系统方面的函数
import os
#使用其中提供的argv来处理命令行参数
import sys
#使用其中的urlretrive()函数来下载Web页面
import urllib
#使用其中的urlparse()和urljoin()函数来处理URL
import urlparse

# 从web下载页面
class Retriever(object):
    __slots__ = ('url','file')  # 用tuple定义允许绑定的属性名称，实例只允许绑定url和file两个属性
    def __init__(self,url):
        self.url,self.file = self.get_file(url)

    def get_file(self,url,default='index.html'):
        'Create usable local filename from URL'
        parsed = urlparse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0] # 将http://前辍移除,留下目录和文件名
        #如果没有扩展名后缀的添加一个默认的index.html
        filepath = '%s%s' % (host,parsed.path)
        if not os.path.splitext(parsed.path)[1]:
            filepath = os.path.join(filepath,default)
        #检测是否是目录，如果是目录就不管，如果不是目录就创建
        linkdir = os.path.dirname(filepath)
        if not os.path.isdir(linkdir):
            #如果进入了if，那么要么目录不存在，要么就是已经有文件了
            if os.path.exists(linkdir):
                os.unlink(linkdir)
            os.makedirs(linkdir)
        return url,filepath

    def download(self):
        'Download URL to specific named file'
        try:
            # 页面保存为文件
            retval = urllib.urlretrieve(self.url,self.file)
        except (IOError,httplib.InvalidURL) as e:
            retval = (('*** ERROR:bad URL "%s":%s' %(self.url,e)),)
        return retval
    # 解析下载下来的页面中的链接
    def parse_links(self):
        'Parse out the links found in downloaded HTML file'
        f = open(self.file,'r')
        data = f.read()
        # parser类不进行io，只处理一个formatter对象
        parser = HTMLParser(formatter.AbstractFormatter(formatter.DumbWriter(cStringIO.StringIO())))
        parser.feed(data)
        parser.close()
        return parser.anchorlist

class Crawler(object):
    count = 0  #计数器

    def __init__(self,url):
        self.q = [url]         # 待下载的链接队列
        self.seen = set()      # 已下载链接的一个集合
        parsed = urlparse.urlparse(url)
        host = parsed.netloc.split('@')[-1].split(':')[0]
        self.dom = '.'.join(host.split('.')[-2:])   # 存储主链接的域名
    #使用第一个链接实例化一个Retriever对象，然后开始处理
    def get_page(self,url,media=False):
        'Download page & parse links,add to queue if nec'
        r = Retriever(url)
        fname = r.download()[0]
        if fname[0] == '*':
            print fname,'... skipping parse'
            return
        Crawler.count += 1
        print '\n(',Crawler.count,')'
        print 'URL:',url
        print 'FILE:',fname
        self.seen.add(url)
        ftype = os.path.splitext(fname)[1]
        if ftype not in ('.htm','.html'):
            return

        for link in r.parse_links():
            # 过滤一些非web页面的链接
            if link.startswith('mailto:'):
                print '... discarded,mailto link'
                continue
            if not media:
                ftype = os.path.splitext(link)[1]
                if ftype in ('.mp3','.mp4','.m4v','.wav'):
                    print '... discarded,media file'
                    continue


            if not link.startswith('http://'):
                link = urlparse.urljoin(url,link)
            print '*',link
            if link not in self.seen:
                if self.dom not in link:
                    print '... new,added to Q'
                else:
                    if link not in self.q:
                        self.q.append(link)
                        print '... new,added to Q'
            else:
                print '... discarded,already processed'
    # 用于启动Crawler，用于将队列中所有待下载的新链接处理完毕
    def go(self,media=False):
        'Process next page in queue (if any)'
        while self.q:
            url = self.q.pop()
            self.get_page(url,media)

def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        try:
            url = raw_input('Enter starting URL:')
        except (KeyboardInterrupt,EOFError):
            url = ''
    if not url:
        return
    if not url.startswith('http://') and \
        not url.startswith('ftp://'):
        url = 'http://%s/' % url
    robot = Crawler(url)
    robot.go()

if __name__ == '__main__':
    main()