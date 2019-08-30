import pymysql

def main():
    conn = pymysql.connect(host='localhost', user='root', password="", db='nim')
    cur = conn.cursor()
    fo = open("res.txt", "r")
    line = fo.readline()
    while(line):
        bagi= line.split(",")
        if(len(bagi)==2):
            bagi2=bagi[1].split(None,1)
            sql = "INSERT INTO mahasiswa (nama,nimtpb,nimjurusan) VALUES (%s, %s,%s)"
            val = (bagi2[1], bagi[0],bagi2[0])
        else:
            bagi1=line.split()
            sql = "INSERT INTO mahasiswa (nama,nimtpb,nimjurusan) VALUES (%s, %s,%s)"
            val = (bagi1[1], bagi1[0],'NULL')
        cur.execute(sql, val)
        conn.commit()
        line = fo.readline()
if __name__ == "__main__":
    main()