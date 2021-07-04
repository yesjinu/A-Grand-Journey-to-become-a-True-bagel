# 진정한 베이글이 되기 위한 위대한 여정
2021 Bagelcode Intern Game Jam 제출작

# Introduction
멀티태스킹 하드코어 리듬게임

![Play Demo](./images/play_demo.gif)


회사 생활 중 일어나는 여러 가지 상황을 동시에 처리해내야 한다. 
- 점심시간 붐비는 테이블, 빈자리를 찾아 앉아라!
- 빼곡히 차있는 구글 캘린더, 빈 칸을 찾아 낮잠 일정을 등록하라!
- 지루한 화상회의, 모두가 고개를 돌린 틈에 맥주를 마셔라!
- 오늘의 매출을 알리는 슬랙, 적절한 :pepe: 이모지를 남겨라!

이 모든 미션을 처리하며, 리듬을 놓치지 말 것!

자세한 방법은 [HOW TO PLAY](https://github.com/yesjinu/A-Grand-Journey-to-become-a-True-bagel/blob/master/HOW%20TO%20PLAY.pdf)를 참고하도록!



# Information
- 공정한 게임잼 경쟁을 위해, 아무도 사용해보지 않은 Pygame 라이브러리를 쓰기로 결정.
- 저작권 문제로 원 게임에서 배경 음악을 제거함. 원 음악은 [Billie Eilish - Bad guys](https://youtu.be/DyDfgMOUjCI)
- 위와 같은 이유로 게임 빌드 파일을 제공하지 못함. 게임 실행 방법은 pygame 설치 후 `main.py` run.
- 랭킹 서버가 닫혀, 랭킹 집계는 불가한 상태. 랭킹 관련 코드 주석처리 ;(
- 게임잼에 제출했던 코드 상태를 (디버깅용 출력까지) 최대한 그대로 유지


# Notable project structure
- `main.py::main()` 내부에서 `while True` 무한루프를 돌면서 키보드 인풋 이벤트 감지, 변경된 게임 화면 렌더링하는 구조
- 총 5가지의 미니 게임을 관리하기 위한 부모 클래스 `Game`을 선언하고, 미니 게임들이 이를 상속. 
- main에서는 `Game`만 조작하고, 게임 리스트는 `Game`에서 관리하도록 분리. 추후 새로운 게임이 추가되더라도 scalable하게 대응 가능하도록 구현
```
Game
├─ Table_Game
├─ Calendar_Game
├─ Meeting_Game
├─ Slack_Game
└─ Clicking_Game
```


# Tools I used
- Python3
- Pygame



