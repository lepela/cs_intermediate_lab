# Copilot Studio 중급 핸즈온 Lab

Power Automate + Copilot Studio로 **HR 채용 자동화 솔루션**을 직접 만드는 7시간 핸즈온 과정 교안입니다.

이력서 접수부터 면접 확정까지 — AI에게 일을 맡기되 결정은 사람이 내리는(HITL) 파이프라인을 처음부터 끝까지 빌드합니다.

## 📖 교안 사이트

👉 https://lepela.github.io/cs_intermediate_lab/

## 과정 구조

| 유닛 | 제목 | 성격 |
|---|---|---|
| Unit 0 | 환경 셋업 (SharePoint 사이트·리스트·문서함) | 핸즈온 |
| Unit 1 | 적재 흐름 — 메일 수신 → AI 추출 → SP 적재 | 핸즈온 (산출물①) |
| Unit 2 | 승인 흐름 — 비동기 HITL | 핸즈온 |
| Unit 3 | 면접관 에이전트 + Knowledge + 지침 | 핸즈온 + 시연 |
| Unit 4 | 모듈 1 — 조회·평가·질문 (커넥터+지침) | 테스트 중심 |
| Unit 5 | 모듈 2 — 면접 확정 트랜잭션 (흐름) | 핸즈온 (산출물②) |

핵심 학습 가치는 두 가지입니다: **사람은 어디에 개입하는가**(비동기 HITL vs 대화형 HITL), 그리고 **커넥터인가 흐름인가**(읽기 = 커넥터+지침 / 상태 변경 = 흐름)의 경계 판단.

## 로컬 실행

```bash
bundle install
bundle exec jekyll serve
# → http://127.0.0.1:4000/cs_intermediate_lab/
```

## 대상

Power Automate / Copilot Studio 초급 과정을 이수한 시티즌 개발자. 코딩 경험은 필요하지 않습니다.

---

이 교안은 [Claude](https://claude.ai)와 협업해 제작되었습니다. 사이트 테마는 [Just the Docs](https://just-the-docs.github.io/just-the-docs/)를 사용합니다.
