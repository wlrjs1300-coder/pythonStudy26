class Score:
    def __init__(self,member_id,kor,eng,math,id=None):
        self.member_id = member_id
        self.kor = kor
        self.eng = eng
        self.math = math

    @property
    def total(self):
        return self.kor+self.eng+self.math
    @property
    def avg(self):
        return round(self.total/3,2)
    @property
    def grade(self):
        if self.avg >= 90:
            return "A"
        elif self.avg >= 80:
            return "B"
        elif self.avg >= 70:
            return "C"
        else:
            return "F"
    @classmethod
    def from_db(cls,row:dict):
        if not row:
            return None
        return cls(
            id=row.get("id"),
            member_id=row.get("member_id"),
            kor=row.get("korean",0),
            eng=row.get("english",0),
            math=row.get("math",0)
        )