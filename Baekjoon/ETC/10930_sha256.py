# 해시 라이브러리 사용
import hashlib
n = input()
# 바이트 코드로 인코딩 해줌
encoded_data = n.encode()
# 바이트 객체를 해시 결과 문자열로 변환
result = hashlib.sha256(encoded_data).hexdigest()
print(result)