# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
from caipiao.settings import MY_SQL


class CaipiaoPipeline:
    def open_spider(self,spider):
        # print(1)
        self.f = open("./双色球.csv",mode="a",encoding="utf-8")

    def close_spider(self,spider):
        # print(2)
        self.f.close()

    def process_item(self, item, spider):
        # print(item)
        # with open("./双色球.csv",mode="a",encoding="utf-8") as f:
        self.f.write(f"{item['qihao']},{'_'.join(item['red_ball'])},{item['blue_ball']}\n")
        return item

class CaipiaoMySQLPipeline:
    def open_spider(self,spider):
        self.conn = pymysql.connect(
            host=MY_SQL['host'],
            port=MY_SQL['port'],
            user=MY_SQL['user'],
            password=MY_SQL['password'],
            database=MY_SQL['database']
        )

    def close_spider(self,spider):
        if self.conn:
            self.conn.close()

    def process_item(self, item, spider):
        cursor = self.conn.cursor()
        try:
            sql = "insert into caipiao(qihao,red_ball,blue_ball) values(%s, %s, %s)"
            cursor.execute(sql, (item['qihao'], "_".join(item['red_ball']), item['blue_ball']))
            self.conn.commit()
        except:
            self.conn.rollback()
        finally:
            if cursor:
                cursor.close()

        return item