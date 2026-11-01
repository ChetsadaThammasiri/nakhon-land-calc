# src/units.py
# แปลงหน่วยพื้นที่ดินแบบไทย: ไร่ งาน ตารางวา

SQWAH_PER_NGAN = 100
SQWAH_PER_RAI = 400
SQM_PER_SQWAH = 4


def _validate(rai, ngan, sqwah):
    if rai < 0 or ngan < 0 or sqwah < 0:
        raise ValueError("ค่าต้องไม่ติดลบ")
    if ngan > 3:
        raise ValueError("งานต้องไม่เกิน 3 (4 งาน = 1 ไร่)")
    if sqwah >= SQWAH_PER_NGAN:
        raise ValueError("ตารางวาต้องน้อยกว่า 100 (100 ตร.ว. = 1 งาน)")


def to_sqwah(rai, ngan=0, sqwah=0):
    """แปลง ไร่-งาน-ตร.ว. เป็นตารางวารวม"""
    _validate(rai, ngan, sqwah)
    return rai * SQWAH_PER_RAI + ngan * SQWAH_PER_NGAN + sqwah


def from_sqwah(total):
    """แปลงตารางวารวม เป็น (ไร่, งาน, ตร.ว.)"""
    if total < 0:
        raise ValueError("ค่าต้องไม่ติดลบ")
    rai, rest = divmod(total, SQWAH_PER_RAI)
    ngan, sqwah = divmod(rest, SQWAH_PER_NGAN)
    return int(rai), int(ngan), sqwah


def to_rai_decimal(rai, ngan=0, sqwah=0):
    """แปลง ไร่-งาน-ตร.ว. เป็นไร่ทศนิยม (ใช้คิดราคาต่อไร่)"""
    return to_sqwah(rai, ngan, sqwah) / SQWAH_PER_RAI
