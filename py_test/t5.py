import collections



#플랫폼별 처리를 위한 운영체계 체크
import platform

if platform.platform().find('Windows')>=0:
    print('윈도우')
else:
    print('기타운영체계')

print(platform.platform())
print(platform.release())
print(platform.version())