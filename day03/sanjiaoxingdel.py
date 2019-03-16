import day03.mydef as md
import day03.demo01 as pa
if __name__ == '__main__':
    md.dengbian(10)
    md.jiujiu(9)
    md.lingxing(6)
    md.youduiqi(100)

    pa.a()
print('\n'.join([''.join([('Love'[(x - y) % len('Love')] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
            x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))



