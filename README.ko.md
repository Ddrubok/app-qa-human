# app-qa-Human

[English](README.md) | [한국어](README.ko.md)

**사용자의 목표·실수·중단·복구 과정을 따라 앱을 점검하는 AI 에이전트 스킬입니다.**

[기존 app-qa](https://github.com/Ddrubok/app-qa)를 유지하면서 별도로 설치하고 비교할 수 있습니다. 기존의 증거·재현 기준에 탐색형 QA, 테스트 케이스 생성, 버그 리포트 표준화, 스토어 심사 위험 점검을 추가했습니다.

스킬은 에이전트가 읽는 지침입니다. 실제 사람을 대상으로 한 사용자 조사나 자동 QA 서버가 아니며, 설치만으로 앱·회사 지식·협업 툴이 연결되지 않습니다.

## 무엇이 추가되었나요?

| 기능 | 확인하거나 만드는 것 |
|---|---|
| 사용자 관점 탐색 | 다음 행동을 찾고, 결과를 예상하고, 피드백을 이해하고, 실수에서 회복할 수 있는지 |
| 작업 완료 확인 | 다운로드 파일 열기, 저장 후 재진입, 실제 키보드·마우스 조작 확인 |
| 스크린샷 근거 | 기본 촬영 ON, 요청에 따라 `screenshots=on` / `screenshots=off` 선택 |
| PRD·디자인 기반 TC | 요구사항에 연결된 사전 조건·실행 절차·예상 결과·실행 상태 |
| 버그 리포트 정리 | 불명확한 제보에서 사실과 추정을 구분한 보고서 |
| 스토어 심사 위험 | 현재 공식 정책의 적용 조건과 실제 구현 증거 |
| 회사 지식 검색 | 지침·과거 결함의 출처, 버전, 충돌 및 유효성 |
| 비교 평가 | 동일 조건 비교 절차와 가상 평가 사례 |

기본 7개 영역은 기능, 사용성·접근성, 인터럽트, 예외·복구, 데이터·권한·개인정보, 호환성·성능, 배포·운영입니다. 회사 기준이 제공되면 해당 분류를 우선합니다.

## Claude Code·Gemini CLI에서도 사용하기

핵심은 공통 `SKILL.md`와 상대경로 참조 문서입니다. `agents/openai.yaml`은 Codex 표시용 부가 정보이며 다른 도구에서 실행하는 데 필요하지 않습니다.

| 도구 | 개인 설치 위치 | 호출 |
|---|---|---|
| Codex | 아래 설명의 현재 인식 경로 | `$app-qa-human` |
| Claude Code | `~/.claude/skills/app-qa-human` | `/app-qa-human` |
| Gemini CLI | `~/.gemini/skills/app-qa-human` | “app-qa-human 스킬을 활성화해서 작업해줘” |

Claude Code 설치:

```sh
git clone https://github.com/Ddrubok/app-qa-human.git ~/.claude/skills/app-qa-human
```

Gemini CLI 설치:

```sh
gemini skills install https://github.com/Ddrubok/app-qa-human --scope user
gemini skills list
```

프로젝트 전용이면 Claude는 `.claude/skills/app-qa-human`, Gemini는 `--scope workspace`를 사용합니다. 설치·활성화 동의가 표시될 수 있습니다. 이후의 `$app-qa-human` 호출 예시는 Codex용이며 다른 도구에서는 위 호출 방식으로 바꾸세요.

확인 범위는 **CLI 환경**입니다. 일반 웹 채팅, Claude 웹 업로드, Antigravity/agy의 자동 로딩까지 검증한 것은 아닙니다. [호환성 확인 기록](COMPATIBILITY.md)을 참고하세요.

## 설치

에이전트가 인식하는 스킬 위치 한 곳에 설치하세요.

```sh
git clone https://github.com/Ddrubok/app-qa-human.git ~/.agents/skills/app-qa-human
```

프로젝트 전용은 `<프로젝트>/.agents/skills/app-qa-human`을 사용합니다. 이미 `~/.codex/skills`에서 정상 인식되는 환경이면 그 위치를 사용해도 됩니다. 중복 설치를 피하고, 목록에 보이지 않으면 세션을 다시 시작하세요.

표시 이름은 `app-qa-Human`, 호출 이름은 `$app-qa-human`입니다.

## 사용 예시

```text
$app-qa-human 이 앱을 처음 사용하는 사람 관점에서 QA해줘.
잘못 입력하거나 중단했다가 돌아오는 흐름도 확인하고,
직접 재현한 문제와 추정·추가 확인 항목을 구분해줘.
```

```text
$app-qa-human 이 기획서에서 Markdown 테스트 케이스를 만들어줘.
각 케이스에 요구사항 근거를 연결하고 아직 실행하지 않은 것은 미실행으로 표시해줘.
```

```text
$app-qa-human 이 오류 메모를 Jira 결함 리포트 초안으로 정리해줘.
모르는 내용은 만들어내지 말고, 외부에 게시하지 마.
```

### 스크린샷: 기본 ON

실제 앱·웹 QA에서는 검사한 화면·케이스의 시작 상태와 결과를 촬영합니다. 정상 결과와 발견한 문제 모두 포함하며, 저장한 이미지를 직접 확인한 뒤 보고서의 해당 항목에 연결하거나 삽입합니다.

```text
$app-qa-human screenshots=on 이 앱을 QA해주세요.
$app-qa-human screenshots=off 스크린샷을 찍지 않고 QA해주세요.
```

별도 옵션 없이 요청하면 ON입니다. “스크린샷 켜고”, “스크린샷 찍지 말고”라고 말해도 됩니다. 이 옵션은 에이전트에 전달하는 요청이며 셸 명령이 아닙니다.

OFF이면 자동으로 스크린샷을 찍는 도구도 사용하지 않고, 가능한 텍스트·DOM 기반 검사와 시각적 확인의 한계를 기록합니다. 같은 QA를 이어가는 동안에는 마지막 선택을 유지합니다. 별도 선호를 지정하지 않은 새 QA는 ON으로 시작합니다. 도중에 OFF로 바꿔도 이미 찍은 파일은 삭제하지 않습니다.

촬영 도구가 없거나 민감한 정보를 안전하게 제외할 수 없으면 누락 사유를 남깁니다. 촬영 계획만 세운 상태는 미실행으로 표시합니다. 기존 메모 정리·보고서 비교만 요청한 경우에는 새 앱 검사를 시작하거나 스크린샷을 만들지 않으며, 제공받은 이미지의 출처를 구분합니다.

JSON·엑셀 출력은 형식을 명시해서 요청하세요. 실제 XLSX 생성은 사용 가능한 도구가 필요하며 CSV를 엑셀 파일로 위장하지 않습니다.

## 범위와 검증 상태

- 생성한 TC는 실행 결과가 아닙니다. 스크린샷만으로 조작·접근성 동작을 확인했다고 주장하지 않습니다.
- 심사 위험은 최신 공식 정책과 플랫폼·지역별 조건을 확인합니다. 승인 보장이나 거절 확률을 제공하지 않습니다.
- HIG·Material의 디자인 권장 사항을 곧바로 심사 거절 기준으로 취급하지 않습니다.
- QA 요청 자체는 코드 수정·배포·실제 결제·외부 메시지 전송을 허용하지 않습니다.
- Vector DB, Slack 봇, Jira 자동 댓글은 설치되어 있지 않습니다. 사용 가능한 자료와 도구를 활용하는 절차를 제공합니다.
- 파일 형식·참조 경로와 일부 가상 사례의 판단을 검토했습니다. 실제 앱 성능 시험이나 사람 대비 정확도 측정, 평가 목록 전체의 실행을 뜻하지 않습니다.

## 주요 문서

- [스킬 본문](SKILL.md)
- [TC·리포트 형식과 예시](references/cases-and-reports.md)
- [작업 완료·파일·저장 결과 확인](references/task-completion.md)
- [스토어 정책 점검](references/store-review.md)
- [지식 검색 절차](references/knowledge.md)
- [비교 평가 사례](references/evaluation.md)
- [기존 app-qa 기준](references/baseline.md)
