# Retrospective Patch Plan — Chapters 49–53

Create bounded exact-text patches; do not return complete chapters. Every `old`
string must occur exactly once in the identified current chapter. `new` must be
finished replacement prose. Combine adjacent findings when useful, never alter
unreported text, and disposition every finding.

Return exactly one JSON object with no Markdown fence:

{
  "summary": "brief patch summary",
  "patches": [
    {"chapter": 1, "finding_ids": ["R0000-01"], "old": "exact old text", "new": "exact replacement"}
  ],
  "dispositions": [
    {"finding_id": "R0000-01", "status": "applied|rejected|unresolved", "reason": "specific reason"}
  ]
}

Reject a finding only when its proposed change is not supported by the supplied
source. Leave genuinely uncertain findings unresolved. Do not intensify or
sanitize register.

## Audit rubric

# Retrospective Translation Audit Rubric

Audit accepted chapters for defects likely to survive an ordinary review. Do
not retranslate acceptable prose or optimize merely for difference.

Prioritize in this order:

1. Reversed or altered actions, negation, subjects, identities, kinship,
   quantities, causal relations, and physical direction.
2. Omitted source beats, explanatory mechanisms, pragmatic cues, ambiguity,
   jokes, and characterization.
3. Established terminology, Murim concepts, hierarchy, and address.
4. Register mismatch: intensified or sanitized profanity, euphemisms made more
   explicit, stiffness, or flattened comic timing.
5. Clear English defects that materially impede voice or meaning.

Semantic fidelity outranks polish. Preserve the source's degree of explicitness.
Do not report optional synonyms, generic praise, or whole-chapter rewrites.
Every finding must quote an exact current-English span and provide a finished,
bounded replacement. Mark a finding critical only when it changes a scene
fact, action, identity, negation, or consequence; major for meaningful lost
hierarchy, mechanism, characterization, ambiguity, or register; minor for clear
localized defects without changed meaning.

## Structured findings

```json
{
  "summary": "10 findings in chapters 49-53",
  "findings": [
    {
      "chapter": 49,
      "confidence": 1.0,
      "current": "〈 Luxury Nutjob\n\nLuxury Nutjob",
      "defect": "The established display name is replaced with an unapproved alternative.",
      "id": "R0049-01",
      "rationale": "명품충 is explicitly established for this text-message display name as “Designer-Brand Junkie.”",
      "replacement": "〈 Designer-Brand Junkie\n\nDesigner-Brand Junkie",
      "severity": "minor",
      "source": "〈 명품충\n\n\n\n명품충"
    },
    {
      "chapter": 49,
      "confidence": 1.0,
      "current": "“Because they trust me.”\n\n“What?”\n\n“They trust my instincts, and they trust my eye for people. That’s why I want to hold on to Jin Taekyung.”",
      "defect": "The translation changes the subject from Choi trusting himself to unspecified others trusting him, inventing external Guild approval for his decision.",
      "id": "R0049-02",
      "rationale": "저를 믿으니까요 and the following repeated 믿습니다 are first-person statements about Choi’s confidence in his own instincts and judgment.",
      "replacement": "“Because I trust myself.”\n\n“What?”\n\n“I trust my instincts and my eye for people. That’s why I want to sign you, Mr. Jin Taekyung.”",
      "severity": "critical",
      "source": "“저를 믿으니까요.”\n\n“네?”\n\n“제 촉을 믿고, 사람 보는 눈을 믿습니다. 그래서 진태경 씨를 꼭 잡고 싶어요.”"
    },
    {
      "chapter": 50,
      "confidence": 0.99,
      "current": "“Hey, HR. Process two resignations today. Kim Sangshik and Kim Sangho.”",
      "defect": "The English makes the dismissals sound like voluntary resignations even though the Guild Master has just fired Kim Sangshik and orders both father and son removed.",
      "id": "R0050-01",
      "rationale": "In context, 퇴사 처리 is an administrative order to terminate their employment, not a report that they chose to resign.",
      "replacement": "“Hey, HR. Process two terminations today. Kim Sangshik and Kim Sangho.”",
      "severity": "critical",
      "source": "“어, 인사팀장. 오늘 두 명 퇴사 처리 해. 김상식이랑 김상호.”"
    },
    {
      "chapter": 50,
      "confidence": 0.98,
      "current": "For the next few days, Sopung Guild was in an uproar over the rare event of a father and son resigning at the same time.",
      "defect": "The narration again characterizes the father and son as resigning voluntarily, obscuring the consequence of the Guild Master’s order.",
      "id": "R0050-02",
      "rationale": "The preceding scene establishes that the Guild Master dismisses both men; the neutral 퇴사 cannot override that explicit context.",
      "replacement": "For the next few days, Sopung Guild was in an uproar over the rare event of a father and son being forced out at the same time.",
      "severity": "major",
      "source": "그 후, 며칠간 소풍 길드는 부자(父子) 동시 퇴사라는 보기 드문 사건으로 시끄러웠다."
    },
    {
      "chapter": 51,
      "confidence": 1.0,
      "current": "“One Flash.”",
      "defect": "The named spear technique is rendered with a different name from the established terminology.",
      "id": "R0051-01",
      "rationale": "일섬 is established in this block as “One Annihilation,” specifically the technique used to kill the Boss Zone monster in one blow.",
      "replacement": "“One Annihilation.”",
      "severity": "major",
      "source": "“일섬(一晱).”"
    },
    {
      "chapter": 51,
      "confidence": 0.99,
      "current": "Dialect burst out of me before I knew it.",
      "defect": "방언 here means speaking in tongues, not a regional dialect; the mistranslation makes the punch line semantically incoherent.",
      "id": "R0051-02",
      "rationale": "Taekyung is blurting out an ecstatic, quasi-religious stream of facts about Shin Saimdang after recognizing the high-denomination bills.",
      "replacement": "I started speaking in tongues before I knew it.",
      "severity": "major",
      "source": "나도 모르게 방언이 터져 나온다."
    },
    {
      "chapter": 52,
      "confidence": 1.0,
      "current": "A roller coaster that dropped whenever the System disappeared…",
      "defect": "The conditional fear that the System might disappear is recast as a recurring event, falsely implying that it has disappeared before.",
      "id": "R0052-01",
      "rationale": "The conditional 사라지면 describes a feared future possibility, not something that repeatedly happens.",
      "replacement": "A roller coaster that would plummet if the System disappeared…",
      "severity": "critical",
      "source": "시스템이 사라지면 추락하는 롤러코스터……."
    },
    {
      "chapter": 52,
      "confidence": 0.99,
      "current": "“Mrs. Kim is really excited now that her son’s home after so long.”",
      "defect": "The established joking sobriquet 여사 is flattened into the ordinary marital title “Mrs.”",
      "id": "R0052-02",
      "rationale": "여사 is established as “Lady” when Taekyung jokingly refers to Kim Jeonghee.",
      "replacement": "“Look at Lady Kim, all excited because her son’s home after so long.”",
      "severity": "minor",
      "source": "“오랜만에 아들 왔다고 아주 신나셨네, 우리 김 여사.”"
    },
    {
      "chapter": 53,
      "confidence": 0.99,
      "current": "“Our Mrs. Kim is starting again. I know how to eat boiled pork too, you know?”",
      "defect": "The established joking sobriquet is again replaced with the ordinary title “Mrs.”",
      "id": "R0053-01",
      "rationale": "김 여사님 continues the established playful “Lady Kim” address.",
      "replacement": "“There goes Lady Kim again. I know how to eat boiled pork too, you know?”",
      "severity": "minor",
      "source": "“우리 김 여사님 또 시작이네. 나도 수육 먹을 줄 알거든?”"
    },
    {
      "chapter": 53,
      "confidence": 0.99,
      "current": "“From you. You kept calling it in your sleep.”",
      "defect": "The English incorrectly treats a person’s name as something Taekyung was “calling,” producing an unclear referent and unnatural meaning.",
      "id": "R0053-02",
      "rationale": "그 이름을 부르다 here means that Taekyung repeatedly called out or said Jin Wikyung’s name while asleep.",
      "replacement": "“From you. You kept saying that name in your sleep.”",
      "severity": "minor",
      "source": "‘오빠한테. 아까 자면서 계속 그 이름을 부르더라고.’"
    }
  ]
}
```

## Chapter 49

### Korean source

```text
＃49화



이른 아침.

나는 슬그머니 눈을 떴다.

띠링.



- [수면 모드]를 종료합니다.



시스템 알림과 동시에 안도의 한숨이 흘러나왔다.

“후우.”

다행이다. 모든 게 꿈이 아니어서.

고작 하루였지만 어제는 내 인생이 바뀐 날이었다. F급 헌터 진태경으로 눈을 떴다면 현실이 악몽처럼 느껴졌겠지.

부스럭거리며 일어난 그때였다.



- 상태 이상, [숙취]에 걸렸습니다.



“윽.”

어젯밤의 후폭풍이 장난이 아니다. 나는 어지러운 머리를 부여잡고 침대 매트리스 위에서 가부좌를 틀었다.

시스템이 알려 준 바에 의하면 운기조식의 기능 중에는 해독도 있었다.



- [운기조식]을 시작합니다.



진가심법의 구결에 따라 공력을 인도했다. 운기조식을 시작함과 동시에 두통이 옅어졌고, 10분 정도가 지나자 기다리던 메시지가 떴다.



- [숙취]가 사라집니다.



하지만 나는 멈추지 않았다. 도중에 갑자기 마무리 지으면 운기조식의 효율이 떨어진다는 사실을 알고 있었기 때문이다.

‘무림에서의 경험이지.’

마침내 가부좌를 푼 것은 한 시간이 지난 후였다. 머리는 맑았고 몸에는 활력이 넘친다.

문제는…….

‘왜 이렇게 들어오는 기운이 적지?’

외부의 기를 받아들여 내부에 저장, 순환시켜야 공력이 증가한다. 그런데 현실에서의 첫 운기조식은 이상할 정도로 그 기운이 적었다.

‘게다가 탁하기까지.’

비유하자면 양도 적고 맛도 없는 음식인데, 그마저도 한참을 기다려야 하는 셈이다. 저절로 눈살이 찌푸려졌다.

‘환경 오염 문제인가?’

자연의 순수한 기를 바탕으로 한 공력이다 보니 그럴 수도 있겠다. 무림과 비교하자면 현대 사회의 자연환경은 심각한 수준이니까.

‘아니면 장소가 문제일지도.’

지어진 지 수십 년이 넘은 고시원 원룸이 딱히 자연 친화적인 장소는 아니지. 냄새도 구리고, 시설도 낡았다.

진호 형은 고시원 총무인 주제에 항상 이곳의 정체를 의심했다.



‘고문실 아니었을까. 대격변 때 몬스터 잡아와서 나이프로 불알 툭툭 치면서 마왕 어딨냐, 하면 마왕 부모님 위치까지 불었을 것 같은데.’



……상상력 하나는 알아줘야 한다.

‘지금쯤이면 자고 있겠지?’

오전에 일어나는 걸 수치로 여기는 인간이니 굳이 확인할 필요도 없다. 아침이라도 먹으러 갈까, 고민하던 그때였다.

지이잉.

핸드폰으로 문자 한 통이 도착했다.



〈 명품충



명품충

시간 괜찮으십니까?



발신인은 명품충, 아니 최 팀장이었다.



* * *



번쩍이는 샹들리에. 맵시 있게 차려입은 사람들과 잔잔하게 흐르는 클래식 음악.

약속 장소는 카페인지, 고급 레스토랑인지 구분이 안 되는 곳이었다.

“주문하시겠습니까?”

시바, 여긴 웨이터도 연예인 수준이네. 모델 비율에 얼굴은 잘생긴 그리스 신 같다.

‘다들 이렇게 게이가 되는 건가.’

정체성 혼란을 느끼는 나와는 달리 최 팀장은 여유롭게 주문을 시작했다.

“블랙 아이보리 한 잔 주시고. 태경 씨는요?”

그리스 신이 내게 고개를 돌렸다.

왠지 카라멜 마끼아또 달라고 하면 안 될 것 같은 이 느낌.

“같은 걸로 주세요.”

잠시 후 나온 커피는 그럭저럭 괜찮았다.

“좋은데요. 이게 블랙…… 뭐라고요?”

“블랙 아이보리.”

사실 들어도 뭐가 뭔지 모른다. 그런가 보다, 하는 거지.

나는 솔직한 감상을 중얼거렸다.

“비싸 보이네요. 원두 좋은 거 쓰나?”

“코끼리 똥이에요.”

“아.”

나는 조용히 커피잔을 내려놨다. 최 팀장은 피식 웃더니 입을 열었다.

“축하드립니다.”

뜬금없는 축하 인사였지만 바로 알아들었다.

그는 전날의 등급 재측정 결과를 말하고 있었다.

“빠르시네요. 개인 정보라 협회에서도 전부 오픈하지는 않았을 텐데.”

“C급 재각성자는 드무니까요. 게다가 어제 그 모습을 직접 봤는데 모를 수가 없죠.”

그것도 그러네.

수긍하는 내게 최 팀장이 뭔가를 내밀었다. 테이블 위에 가지런히 놓인 봉투 한 장.

“이게 뭡니까?”

“보시면 압니다.”

설마, 돈?

나는 봉투 안의 내용물을 확인했다. 수표 대신 깨알처럼 박힌 글자들이 눈에 들어왔다.

“계약서군요.”

“저희 길드가 제시할 수 있는 최대한의 조건입니다. 한 번 읽어 보시죠.”

안 그래도 이미 읽고 있다. 첫 줄부터 마지막까지. 조항마다 놀라움의 연속이다.

“C급 계약서가 아닌 것 같은데요.”

이 바닥에서 7년쯤 굴렀더니 본 것도, 주워들은 것도 많다.

그런 나도 이 정도로 후한 계약서는 처음 본다.

“B급 중에서도 괜찮은 조건이니까요.”

“그런데 왜 저한테…….”

“저를 믿으니까요.”

“네?”

“제 촉을 믿고, 사람 보는 눈을 믿습니다. 그래서 진태경 씨를 꼭 잡고 싶어요.”

최 팀장이 빈 커피잔을 내려놨다.

“계약, 하시겠습니까?”

솔직히 흔들린다. 그것도 아주 많이.

계약 조건을 떠나 누군가가 나를 알아봤고, 이렇게 원하고 있다는 사실에 당장이라도 고개를 끄덕이고 싶다.

그래서 오늘의 망설임은 어제보다 길었다. 마침내 결정을 내렸을 때는 커피가 식은 후였다.

“죄송합니다.”

이유는 어제와 같았다.

계약서에 따르면 최소 1년간 소속 헌터로 활동해야 한다.

제의는 고맙지만…… 나로서는 성급하게 행동할 수 없었다.

“이미 계약하신 겁니까? 아니면 예정이라도?”

“아뇨. 단지 시간이 더 필요해서요.”

“시간이라.”

최 팀장은 한숨을 내쉬었다.

“어쩔 수 없군요.”

다시 한번 사과의 말을 건네려던 그때.

“두 번째 제안입니다.”

“예?”

최 팀장의 품속에서 또 다른 봉투가 나왔다. 어안이 벙벙한 상태로 받아 내용을 확인했다.

“가계약?”

“어떤 건지는 대충 아시죠?”

알지. 잘 알지.

인력 사무소가 일일 근로자라면 길드와의 가계약은 비정규직이다. 짧은 기간 동안 길드에 소속되어 활동하는 일종의 용병인 셈이다.

“이것까지 거절하시지는 않겠죠?”

앞서 받은 정식 계약서보다는 덜하지만, 역시 후하기는 마찬가지다. 거기에 내게 가장 중요한 계약 기간은 텅 빈 공란.

“원하는 기간을 적으세요.”

“아, 네.”

최 팀장이 내미는 펜을 얼떨결에 받아들었다.

그리고 고민 끝에 7일을 적어 넣었다. 일주일이면 시스템이 유지되는지 지켜보기에 충분한 시간이라고 생각했다.

사인까지 마치자 최 팀장이 손을 내밀었다.

“잘 부탁합니다.”

“제가 할 말이죠.”

굳게 손을 맞잡으니 C급 헌터로 첫발을 내디뎠다는 게 실감이 났다.

‘비록 가계약이지만.’

가슴이 벅찼다.

“내일부터 출근하면 되나요?”

“아뇨.”

최 팀장이 시계를 톡톡 두드렸다.

“지금부터.”



* * *



부우웅.

최 팀장의 차는 커다란 군용 차량이었다. 고가의 슈퍼카를 모을 것 같은 이미지라 의외다 싶었는데, 게이트에 도착한 후에야 그 이유를 알았다.

“고르세요.”

“뭘요?”

“장비.”

최 팀장이 작은 버튼을 누르자 성인 남성 다섯 명이 누워도 될 만한 트렁크가 나타났다.

“작업용으로 개조했어요. 집에 놔두기도 뭐해서.”

나는 입을 쩍 벌린 채 트렁크 안을 구경했다.

‘와, 미쳤다.’

적어도 수백만 원을 호가하는 장비들이 차곡차곡 분류되어 있었다. 방어구에 무기는 기본이요. 각종 포션과 비싸서 못 쓴다는 일회용 마법 스크롤까지 없는 게 없다.

“……이게 다 팀장님 거예요?”

“일단은요. 선물 받은 것도 있고, 예뻐서 산 것도 있고.”

그렇구나. 장비가 예뻐서 사는구나.

‘돈이 얼마나 많아야 저런 마인드가 되는 거냐.’

C급 헌터가 잘 벌긴 하지만 최 팀장의 씀씀이는 이미 그 이상이다. 원래 돈 걱정 안 하고 살 만큼 부자인 거겠지.

꿀꺽.

“그냥 대여소에서 빌리는 게 나을 것 같은데요. 괜히 빌렸다가 망가지기라도 하면 좀.”

“유행 지난 거라 상관없어요.”

그렇구나. 장비 디자인 유행도 따지는구나.

나는 그쯤에서 생각하는 걸 포기하고 장비를 골랐다.

시스템이 있으니 장비 고르는 것도 쉬웠다.

‘아이템 확인.’

띠링.



아이템창



[리자드맨 사냥꾼의 가죽 세트]

종류 : 방어구

등급 : 일류

제한 : 無

설명 : 리자드맨의 가죽을 통으로 벗겨 제작했다.

 전 세트 장착 시 [비늘 갑옷] 발동.





‘이거 괜찮네.’

무게도 가볍고, 가죽은 질기면서 단단했다.

모두 장착하자 [비늘 갑옷]의 세트 효과가 발동되었다.

“오.”

가죽 위로 솟아난 녹색 비늘이 온몸을 촘촘하게 뒤덮는다. 그런 내 모습에 최 팀장이 고개를 끄덕였다.

“괜찮은 거 고르셨네요. 안목이 좋으신데요.”

시스템이 좋은 거다.

나는 어색하게 웃으며 무기를 뒤적거렸다. 생각해 보면 최 팀장 이 인간, 검 쓰는 것밖에 못 봤는데 트렁크 안의 무기만 해도 다섯 종류가 넘어간다.

‘손때도 묻어 있고.’

스스로에게 맞는 걸 찾기 위해 노력한 흔적이 보인다.

잠시 후, 내 손에는 창 한 자루가 들려 있었다.



아이템창



[리자드맨 학살자의 작살]

종류 : 무기

등급 : 일류

제한 : 無

설명 : 공격 성공 시 높은 확률로 [출혈] 발동





누가 보면 리자드 성애자인 줄 알겠다. 창을 마지막으로 장비 선택이 끝나자 최 팀장이 피식 웃었다.

“왜 그러세요?”

“일이 잘 풀린다 싶어서요.”

“예?”

“곧 알게 될 겁니다.”

뭔 소린가 싶었지만 일단 최 팀장을 따라 게이트 앞으로 갔다. 관리청 직원 대신 웬 남자가 그곳에 있었다.

“오셨습니까.”

깍듯한 90도 인사. 더 놀라운 건 그 모습을 자연스럽게 받아들이는 최 팀장의 태도다.

“게이트 상황은요?”

“예. 어제 연락받고 출입 통제했습니다.”

“고생하셨어요.”

“아닙니다. 도련님.”

도련님이란 결혼하지 않은 시동생을 높여 이르거나 부르는 말인데, 일단 저 남자가 최 팀장의 형수일 리는 없고…….

‘최 팀장. 부잣집 도련님이었구나.’

어쩐지.

위아래로 명품 장비 쫙 빼입었을 때부터 알아봤어야 했다.

거기에 장비 디자인까지 따지는 패션피플, 어지간한 금수저가 아니고서야 불가능하지.

‘저 인간은 다 가졌네.’

그 다 가진 인간이 내게 고개를 돌렸다.

“자, 이제 들어갑시다.”

“지금 당장이요?”

“장비도 해결됐고, 무슨 문제라도 있습니까?”

너무 당연하다는 말투에 주위를 둘러보았다.

나와 최 팀장. 그리고 낯선 아저씨까지. 셋이 전부다.

“다른 팀원은요?”

“여기 있잖습니까. 팀원.”

“아, 그렇구나. 저분도 들어가시는 거죠?”

아저씨가 묵직한 음성으로 끼어들었다.

“전 아닙니다.”

“그럼……?”

“우리 둘이 전붑니다. 추가 인원은 없어요.”

최 팀장의 말에 나는 어안이 벙벙해졌다.

“없어요?”

“네.”

“한 사람도?”

“개 한 마리 안 데려갑니다.”

단호한 거 보소. 포청천인 줄.

“그럼 단둘이서 게이트를 돈다고요?”

“못 할 거 있습니까? 고작 D급 게이트인데.”

“저 D급 게이트 처음인데요.”

“전 많이 다녀 봤습니다.”

아니, 시발…….

D급 게이트가 무슨 동네 할인 마트도 아니고.

“단둘뿐이라면 빠지겠습니다.”

D급 게이트라면 동일 등급의 헌터 열 명이 팀을 짜야 안전한 레이드를 할 수 있다. 내가 아무리 시스템을 사용할 수 있고, 무공을 익혔다지만 그걸로 모든 위험이 사라지는 건 아니다.

“진태경 씨가 어떤 생각을 하고 있는지 압니다. 하지만 한 가지만 말씀드리죠.”

최 팀장이 느긋한 목소리로 말을 이었다.

“저도 재각성 헌터입니다.”

“재각성이요? 팀장님은 C급으로 알고 있는데…….”

“C급은 처음 측정 당시 나온 등급이죠. 재각성은 그 후의 일이었고.”

말인즉슨 최소 B급 이상의 실력자라는 뜻이다.

가능성은 희박하지만 그 이상일 수도 있고.

‘B급 헌터라.’

그렇다면 말이 달라진다. 단둘뿐이니 그만큼 내게 떨어지는 액수도 늘어날 테고.

“돌아가신다면 말리지는 않겠습니다. 저야 혼자 들어가도 되니까요. 그런 적이 한두 번도 아니고.”

혼자 D급 게이트를 수시로 드나들어?

“그럼 조심히 들어가세요. 내일부터는 E급으로 알아보죠.”

그 말이 결정타였다.

나는 돌아서는 그의 어깨를 덥석 붙잡았다.

“최 팀장님.”

“네.”

“레이드가…… 하고 싶어요.”

최 팀장이 따스하게 웃었다.

“잘해 봅시다.”
```

### Current accepted English

```markdown
# Chapter 49

Early morning.

I eased my eyes open.

Ding.

> **System**
>
> Exiting Sleep Mode.

The System notification came with a sigh of relief.

“Phew.”

Thank goodness. It hadn’t all been a dream.

It had only been one day, but yesterday was the day my life changed. If I’d opened my eyes as Jin Taekyung, F-rank Hunter, reality would have felt like a nightmare.

I rustled my way up—and that was when it hit.

> **System**
>
> Afflicted with the status ailment Hangover.

“Urgh.”

Last night’s aftermath was no joke. I clutched my spinning head and sat cross-legged on the mattress.

The System had told me circulating qi could detoxify, too.

> **System**
>
> Beginning Qi Circulation.

Following the formula of the Jin Family’s Cultivation Technique, I guided my internal energy. The moment I started circulating qi, the headache began to fade. After about ten minutes, the message I’d been waiting for appeared.

> **System**
>
> Hangover disappears.

But I didn’t stop. I knew that wrapping it up halfway through would tank the efficiency.

*Experience from Murim.*

I didn’t uncross my legs until a full hour had passed. My head was clear, and my body was bursting with energy.

The problem was…

*Why is so little energy coming in?*

Internal energy only increased if you took in qi from outside, stored it, and circulated it. But my first circulation in reality brought in strangely little.

*And it’s murky, too.*

It was like a tiny serving of bland food—and even that took forever to arrive. I frowned.

*Environmental pollution, maybe?*

Internal energy was based on pure natural qi, so it was possible. Compared to Murim, the natural environment of modern society was in pretty dire shape.

*Or maybe the location is the problem.*

A one-room in a goshiwon built decades ago was hardly a nature-friendly place. It stank, and the facilities were old.

Jinho hyung was always suspicious of what this place really was, and he was the goshiwon manager.

*Maybe it used to be a torture chamber. During the Great Cataclysm they probably dragged monsters in, tapped their balls with a knife, and asked where the Demon King was. The monsters would’ve given up his parents’ location, too.*

…You had to give him credit for his imagination.

*He should be sleeping by now, right?*

He treated getting up in the morning as a disgrace, so there was no need to check. I was wondering whether to go grab breakfast when—

Bzzzt.

A text arrived on my phone.

〈 Luxury Nutjob

Luxury Nutjob

Do you have some time?

The sender was Luxury Nutjob—or rather, Team Leader Choi.

* * *

A glittering chandelier. Stylishly dressed people, and soft classical music in the background.

I couldn’t tell if the meeting place was a café or a high-end restaurant.

“May I take your order?”

*Shit. Even the waiter here looks like a celebrity.*

Model proportions, and a face like a handsome Greek god.

*Is this how everyone turns gay?*

While I was having an identity crisis, Team Leader Choi calmly started ordering.

“One Black Ivory, please. What about you, Mr. Taekyung?”

The Greek god turned toward me.

Something about the vibe said I shouldn’t order a caramel macchiato.

“I’ll have the same.”

The coffee that came out a little later was pretty decent.

“It’s good. This is Black… what was it?”

“Black Ivory.”

Even after hearing it, I still had no idea what that meant. I just went, well, okay then.

I muttered my honest take.

“It looks expensive. Do they use good beans?”

“It’s elephant dung.”

“Oh.”

I quietly set down my cup. Team Leader Choi chuckled, then spoke.

“Congratulations.”

It came out of nowhere, but I knew what he meant right away.

He was talking about yesterday’s rank reassessment.

“You’re fast. It’s personal information—the Association wouldn’t have opened all of it.”

“C-rank reawakened Hunters are rare. Besides, I saw what happened yesterday with my own eyes. There was no way I wouldn’t know.”

That was true.

As I granted him that, Team Leader Choi held something out. A single envelope, laid neatly on the table.

“What is this?”

“You’ll know when you look.”

*Don’t tell me—money?*

I checked the contents. Instead of a check, tiny printed letters packed the page.

“It’s a contract.”

“The best terms our Guild can offer. Give it a read.”

I was already reading it. From the first line to the last. Every clause was another shock.

“This doesn’t look like a C-rank contract.”

After about seven years knocking around this business, I’d seen plenty, and overheard plenty more.

Even I had never seen a contract this generous.

“They’re good terms even among B-rank contracts.”

“Then why are you offering this to me…?”

“Because they trust me.”

“What?”

“They trust my instincts, and they trust my eye for people. That’s why I want to hold on to Jin Taekyung.”

Team Leader Choi set down his empty cup.

“Will you sign?”

Honestly, I was wavering. A lot.

It wasn’t only the terms. Someone had recognized me and wanted me this badly. I wanted to nod right then.

That was why today’s hesitation ran longer than yesterday’s. By the time I finally decided, the coffee had gone cold.

“I’m sorry.”

The reason was the same as yesterday.

According to the contract, I would have to work as an affiliated Hunter for at least one year.

I was grateful for the offer, but… I couldn’t rush this.

“Have you already signed with someone else? Or are you planning to?”

“No. I just need more time.”

“Time.”

Team Leader Choi sighed.

“I suppose it can’t be helped.”

I was about to apologize again when he said,

“This is my second offer.”

“Pardon?”

Another envelope came out of Team Leader Choi’s jacket. Still dazed, I took it and checked the contents.

“A provisional contract?”

“You have a rough idea of what that is, right?”

I did. I knew it well.

If the Manpower Office was day labor, a provisional contract with a Guild was temp work. You’d be attached to the Guild for a short stretch, basically a mercenary.

“You won’t turn this one down too, will you?”

It was less generous than the formal contract he’d given me, but it was still more than generous enough. And the part that mattered most to me—the contract period—was a blank.

“Write down whatever period you want.”

“Oh. Right.”

I took the pen he held out, half in a daze.

After thinking it over, I wrote seven days. A week should be enough time to see whether the System would last.

Once I’d signed, Team Leader Choi held out his hand.

“I look forward to working with you.”

“That’s my line.”

When we shook hands firmly, it sank in that I’d taken my first step as a C-rank-level Hunter.

*Even if it’s only a provisional contract.*

My chest swelled.

“Should I come in tomorrow?”

“No.”

Team Leader Choi tapped his watch.

“Starting now.”

* * *

Vroom.

Team Leader Choi’s car was a large military vehicle. He looked like the type to collect expensive supercars, so this was unexpected. I only understood why after we arrived at the Gate.

“Pick something.”

“Pick what?”

“Equipment.”

Team Leader Choi pressed a small button, and a trunk large enough for five grown men to lie down in appeared.

“I had it modified for work. Leaving all this at home felt kind of off.”

I stared into the trunk with my mouth hanging open.

*Holy crap.*

Gear worth at least several million won was stacked and sorted. Armor and weapons were a given. Potions of every kind, even disposable magic scrolls people said were too expensive to actually use. He had everything.

“…Is all this yours, Team Leader?”

“For now. Some of it was gifts, and some I bought because it looked nice.”

Ah. So he buys gear because it looks nice.

*How rich do you have to be to think like that?*

C-rank Hunters made good money, but Team Leader Choi’s spending was already beyond that. He must have been rich enough that money was never a concern.

Gulp.

“It might be better to rent from a rental shop. If I borrow something and it gets wrecked, it’d be kind of…”

“They’re out of fashion, so it doesn’t matter.”

Ah. So he even cares whether gear is in fashion.

I gave up thinking about it around there and picked my equipment.

Having the System made it easy.

*Item check.*

Ding.

> **System**
>
> Item Window
>
> Lizardman Hunter’s Leather Set
>
> Type: Armor
>
> **Grade:** First Rate
>
> Restriction: None
>
> Description: Made by stripping off a lizardman’s hide in one piece.
>
> Scale Armor activates when the full set is equipped.

*This is pretty good.*

It was light, and the leather was tough and hard.

Once I had everything on, the set effect Scale Armor activated.

“Oh.”

Green scales rose from the leather and covered my whole body in a tight layer. Team Leader Choi nodded at the sight of me.

“You picked a good one. You’ve got a good eye.”

*It’s the System that’s good.*

I smiled awkwardly and rummaged through the weapons. Come to think of it, I’d only ever seen this guy use a sword, but the trunk alone had more than five kinds of weapons.

*And they’ve got wear on them, too.*

You could see the traces of him trying to find what suited him.

A little later, I had a spear in my hand.

> **System**
>
> Item Window
>
> Lizardman Slayer’s Harpoon
>
> Type: Weapon
>
> **Grade:** First Rate
>
> Restriction: None
>
> Description: Upon a successful attack, Bleeding activates with a high probability.

Anyone watching would think I had a lizardman fetish.

With the spear as the last piece, I was done choosing. Team Leader Choi chuckled.

“What’s so funny?”

“I was thinking things are going well.”

“Pardon?”

“You’ll find out soon enough.”

I had no idea what he meant, but I followed him to the front of the Gate. Instead of an Administration staffer, some man was standing there.

“You’ve arrived.”

A perfectly proper ninety-degree bow. Even more surprising was the way Team Leader Choi took it as natural.

“How’s the Gate?”

“Yes. I received your call yesterday and restricted access.”

“Thanks for your hard work.”

“Not at all, young master.”

*Young master?*

The term was an honorific for an unmarried younger brother-in-law, but there was no way that man was Team Leader Choi’s sister-in-law…

*Team Leader Choi. So he was a rich family’s young master.*

No wonder.

I should have known from the moment I saw him dripping in luxury gear from head to toe.

Add being fashion-conscious enough to care about equipment design, and you couldn’t pull that off unless you were one hell of a gold spoon.

*That guy has everything.*

The guy who had everything turned to me.

“All right. Let’s go in.”

“Right now?”

“The equipment’s taken care of. Is there a problem?”

His tone made it sound so obvious that I looked around.

Me, Team Leader Choi, and some middle-aged guy I didn’t know. That was everyone.

“What about the other team members?”

“They’re right here. The team members.”

“Oh, I see. He’s going in too, right?”

The middle-aged man cut in, his voice heavy.

“I’m not.”

“Then…?”

“It’s just the two of us. There’s no one else.”

Team Leader Choi’s words left me slack-jawed.

“No one else?”

“No.”

“Not even one person?”

“We’re not bringing so much as a dog.”

Look at how decisive he was. Who was he, Pocheongcheon?[^2]

“So the two of us are running the Gate alone?”

“Why couldn’t we? It’s only a D-rank Gate.”

“This is my first D-rank Gate.”

“I’ve been to plenty.”

No, fuck…

A D-rank Gate wasn’t some neighborhood discount mart.

“If it’s just the two of us, I’m backing out.”

A safe raid on a D-rank Gate needed a team of ten Hunters of the same rank. I could use the System, and I’d learned martial arts, but that didn’t make the danger go away.

“I know what you’re thinking, Mr. Jin Taekyung. But let me tell you one thing.”

Team Leader Choi went on in a relaxed voice.

“I’m a reawakened Hunter, too.”

“Reawakened? I thought you were C-rank, Team Leader…”

“C-rank was the rank I received when I was first measured. The reawakening happened afterward.”

Meaning he was at least B-rank in ability.

The odds were slim, but he could be even higher than that.

*A B-rank Hunter.*

If that was true, the situation changed. Just the two of us also meant a bigger cut for me.

“If you want to go back, I won’t stop you. I can go in alone. It wouldn’t be the first time, or the second.”

He walked in and out of D-rank Gates alone on the regular?

“Then be careful in there. From tomorrow, we’ll look at E-rank.”

That was the deciding blow.

I grabbed his shoulder as he turned away.

“Team Leader Choi.”

“Yes?”

“I want to… raid.”

Team Leader Choi smiled warmly.

“Let’s do our best.”

[^2]: Pocheongcheon is a famously incorruptible judge in Chinese legend and popular storytelling.
```
## Chapter 50

### Korean source

```text
＃50화



나는 눈 앞에 펼쳐진 광경에 입을 딱 벌렸다.

뜨겁고 습한 열기 속, 빽빽한 숲을 따라 끝도 없이 펼쳐진 습지가 그곳에 있었다.

“이게 D급 게이트…….”

상위 게이트일수록 공간이 광활해진다는 사실은 알고 있었다. 하지만 이 정도로 차이가 날 줄이야.

“넓죠?”

나는 화내는 것도 잊은 채 대답했다.

“그러네요. 막막할 만큼.”

“이 정도면 그럭저럭 평균입니다. B급 게이트부터는 길잡이도 따로 고용해야 할 정도니까요.”

“……길잡이는 지금도 필요한 것 같은데요.”

“오늘은 괜찮습니다.”

최 팀장이 코팅된 종이를 꺼내어 보여 줬다.

“뭡니까, 그게?”

“지도. 권리 양도받을 때 같이 주더군요.”

지도라, 그럼 길 잃을 일은 없겠…….

“잠깐만요. 뭐라고요?”

“지도라고 말씀드렸습니다만.”

“아뇨, 그거 말고. 그 뒤에 뭐라고 하셨잖아요.”

“권리 양도 말하는 겁니까?”

그래, 인마. 그거.

“그게 무슨 말이에요?”

“말 그대로죠.”

최 팀장이 대수롭지 않다는 듯 말했다.

“이 게이트, 제 겁니다.”

“예?”

“정확히는 독점권을 가지고 있는 거지만요.”

습지대라 그런가. 손에 땀이 맺히고 목이 바짝바짝 탄다.

마른침을 꿀꺽 삼켰다.

‘게이트 독점권이라고?’

대한민국에서 게이트는 국가 재산이다.

대격변 이래 마정석은 핵심 에너지원으로 자리 잡았고, 게이트는 마르지 않는 다이아몬드 광산이나 다름없다. 그런데 그런 게이트의 독점권을 갖고 있다니.

‘도대체 정체가 뭐야?’

부잣집 도련님인 건 알았지만 이 정도일 줄이야.

“슬슬 출발하시죠.”

성큼성큼 앞서 나가는 최 팀장의 뒷모습이 눈부시다. 아아, 저 황금빛 광채, 범접할 수 없는 부의 향기.

‘당신의 길드에 뼈를 묻겠습니다.’

나는 굳게 다짐했다.



* * *



습지대는 미로 같았다.

최 팀장이라는 유능한 길잡이가 없었다면 한참을 헤맸을 것이다. 그렇게 얼마나 걸었을까.

- 키이잇.

공력을 끌어 올리자 더욱 선명히 들리는 울음소리. 몬스터의 등장이었다.

‘최소 스무 마리.’

오는 길에 들었던 최 팀장의 설명에 의하면 이번 게이트에 출현하는 몬스터는 습지대 리자드맨이다.

놈들은 하나의 부족 아래 여러 군락으로 나누어 생활하는데, 그중 하나인 모양이었다.

“입구에서 가장 가까운 소규모 군락입니다. 스무 마리 정도니까 빨리 해치우고 이동합시다.”

최 팀장은 넝쿨을 쳐내며 나아갔다. 평소에는 곱상한 도련님인데 막상 실전에 돌입하니 장난 아니다. 핸들이 고장 난 8톤 트럭처럼 밀고 나가는 뒷모습에서 마초의 냄새가 물씬 풍겼다.

‘존나 멋있어.’

리자드맨 서른 마리가 아니라 백 마리가 와도 최 팀장과 함께라면 쓸어버릴 수 있을 것 같은 이 기분.

왜 온라인 게임에서 고레벨 유저한테 쩔 받는지 알겠다.

“키이잇!”

그래서인지 리자드맨과의 첫 대면도 별 긴장감이 없었다.

다만 사진이나 영상으로만 봤던 몬스터에 대한 신기함만 있을 뿐.

“오, 크다.”

스무 마리 중 가장 작은 놈도 나보다 머리 하나가 더 크다.

최소 2m의 신장과 날렵한 근육, 두툼한 꼬리까지 있어서 그런지 더 커 보인다.

‘물론 어제 상대했던 홉 고블린 대전사만큼은 아니지만.’

이 흉측하게 생긴 농구 유망주들은 우리의 등장이 썩 반갑지 않은 듯했다.

- 키잇!

- 킷, 킷!

각기 손에 든 수십 개의 작살이 번쩍 빛난다. 나는 에워싸는 형태로 전방에서 접근해 오는 놈들을 보며 말했다.

“궁수는 없네요.”

“습지대 리자드맨은 대부분 작살을 씁니다. 혹시 모르니 투창 조심하세요.”

“넵.”

역시 리잘알. 여유롭게 팔짱까지 끼고 있다.

“키이잇!”

불과 이십여 미터 앞까지 접근해 왔다. 나는 최 팀장을 보며 씩 웃었다.

“이놈들이 겁이 없네요.”

“리자드맨 특성입니다. 저돌적이고, 정면 승부를 선호하죠.”

“아하.”

그사이 거리가 10m로 좁혀졌다. 나는 최 팀장의 팔짱이 신경 쓰이기 시작했다.

“슬슬 싸워야 할 것 같은데요.”

“싸워야겠네요.”

“……아, 네. 그래야죠.”

쐐애액-!

그때 작살 서너 개가 바람을 찢으며 쇄도했다. F급 헌터 시절이었다면 주마등이 스쳤겠지만 이제는 뭐, 가볍게 창을 휘둘러 튕겨 냈다.

터터텅!

뭔가 이상함을 느낀 건 그다음이었다.

- 끼이이잇!

- 킷! 키이잇!

저놈들 왜 저래?

눈을 허옇게 뒤집어 까고 괴성을 질러 대는데, 이건 적의를 넘어 거의 증오 수준이다.

어리둥절한 내게 최 팀장이 한마디를 툭 던졌다.

“장비 때문입니다.”

장비? 장비가 왜…… 아!

‘리자드맨 가죽 세트, 학살자의 창.’

시바, 이름 봐라.

내가 리자드맨이었어도 작살 날렸겠다.

‘그러고 보니 작살도 나한테만 날렸네.’

동족의 원수가 코앞에 있으니 최 팀장은 투명 인간 취급이다.

이렇게 되면 나만 줄창 공격당하게 생겼…… 아니, 잠깐만.

“이거 노린 겁니까?”

“뭘 말입니까?”

“저한테 이거 입혀서 어그로 끌고 본인이 쓱싹 하겠다, 딱 그 전략이잖아요, 이거!”

“맹세코 아닙니다.”

정색한 최 팀장이 덧붙였다.

“저는 가만히 있을 거거든요.”

“예?”

“태경 씨가 어그로 끌고, 레이드도 할 겁니다. 괜한 오해하지 마세요.”

이게 뭔 개소리야.

“그러니까…… 저 혼자 싸우라고요?”

“네.”

“최 팀장님은 거기서 팔짱 끼고 구경하시고?”

“팔짱은 풀겠습니다.”

“아니, 시벌…….”

“작살 날아옵니다.”

쐐애액-!

투창(投槍)과 동시에 사방에서 녹색 비늘이 번뜩이며 쇄도한다. 훌쩍 물러난 최 팀장이 비장하게 외쳤다.

“화이팅!”

저거 완전히 미친놈 아냐.

당장이라도 달려가 멱살을 붙잡고 싶었지만 사방에서 작살이 날아들었다.

캉!

- 키이잇!

“이 새끼들이.”

나는 이를 갈며 [기감]을 끌어올렸다. 곧 놈들의 머리 위로 스무 개의 창이 불쑥 솟아올랐다.



[Lv.40 리자드맨 부족민]



40레벨이라…….

나는 창을 꽉 움켜쥐었다.

“너넨 다 죽었어.”

띠링.



- [리자드맨 가죽 세트]의 효과로 해당 몬스터에게 입히는 피해가 10% 상승합니다.

- [리자드맨 학살자의 창]의 효과로 해당 몬스터에게 입히는 피해가 20% 상승합니다.

- 해당 게이트의 모든 [리자드맨]이 당신을 적대합니다. 그들은 이 원한을 갚기 전까지 결코 멈추지 않을 것입니다!



동시에 학살자의 창이 묵직한 궤적을 그려냈다. 칠 성에 이른 진가창법의 초식들이 놈들을 향해 쏟아졌다.

콰드득!



* * *



- 키이…….

노란 파충류의 눈이 스르륵 감긴다. 녹색 습지대는 앞서 죽은 놈들의 시체와 핏물로 잠겨 있었고, 더 이상 서 있는 리자드맨은 존재하지 않았다.

띠링.



- 레벨 업!

- 레벨 업!



경쾌한 시스템 알림을 뒤로하고 돌아섰다. 나무에 기대어 서 있던 최 팀장이 보였다. 팔짱 안 낀다고 하더니 끼고 있어서 두 배로 열받는다.

“뭐 하는 짓입니까?”

말없이 나를 바라보던 최 팀장이 뭔가를 던졌다. 조그만 드링크 병에 담긴 빨간 액체. 소진된 체력을 회복시켜 주는 포션이다.

“지금 병 주고 약 줍니까?”

“병든 것치고는 건강해 보이시는데요. 긁힌 상처 하나 없는 거 보면.”

……그럴듯한데. 순간 납득할 뻔했다.

내가 주춤하는 사이 최 팀장의 입이 열렸다.

“미안합니다.”

거기에 그치지 않고 허리를 굽힌다. 뭐라 할 말이 없을 정도로 정중한 사과였다. 순간 마음이 누그러졌지만 이유는 들어야겠다.

“왜 그랬어요?”

“실력을 봐야 하니까요.”

“겨우 그것 때문에?”

“저한테는 중요합니다. 태경 씨가 어떻게 움직이고, 얼마나 상대할 수 있는지. 또 어디까지 함께할 수 있는지를 알아야 하니까요.”

“그렇다고 몬스터 득실거리는데 혼자 빠져요?”

“태경 씨가 못 미더웠다면 그러지도 않았을 겁니다.”

잘난 놈이 띄워 주니까 솔직히 기분 좋다.

‘무엇보다 다치지도 않았고, 레벨 업도 두 번이나 했지.’

나는 은근히 기대하며 물었다.

“결과는요?”

“음.”

특유의 묘한 눈빛으로 나를 응시하던 최 팀장이 마침내 입을 열었다.

“아직 모르겠습니다.”

“예?”

“그래서 말인데.”

최 팀장이 뭔가를 꺼내 내게 던졌다. 안이 보이지 않는 길쭉한 원통이다. 흔들어 보니 액체가 찰랑거렸다.

“이게 뭡니까, 포션?”

“아래쪽에 버튼 있죠? 눌러 보세요.”

누르면 열리는 구조인가?

고개를 갸웃거리면서 버튼을 눌렀다. 달칵, 하는 소리와 함께 원통 앞부분이 활짝 열렸다.

문제는…….

피유우우우-

펑!

그 안에 있던 게 폭죽처럼 치솟더니 공중에서 터져 버렸다는 거다. 공중에서 터진 분홍색 액체는 넓게 퍼져 나갔다.

“어?”

저게 뭐지?

멍하니 그 광경을 바라보던 내 귓가로 최 팀장의 목소리가 파고들었다.

“페로몬입니다.”

“페로몬? 향수?”

“비슷합니다.”

“……?”

“암컷 리자드맨에게서 채취한 거거든요.”

그의 말이 끝나기가 무섭게 어디선가 진동이 느껴졌다.

땅이다. 땅이 울리고 있었다. 최 팀장이 친절히 덧붙였다.

“효과가 아주 강력합니다.”

너 이 새끼…….



* * *



“3팀장아.”

반백의 장년인이 한 시간 만에 내뱉은 첫 마디다. 그가 줄담배를 피우는 동안 하염없이 기다리던 김상식이 대답했다.

“예, 길드장님.”

“궁금하지? 이 인간이 또 뭔 지랄을 떨려고 아침부터 불렀나, 싶지?”

“아, 아닙니다.”

소풍 길드장이 사람 좋게 웃었다.

“맞아.”

“예?”

“지랄 떨려고 부른 거라고.”

“…….”

“내가 오늘 어디 다녀왔는지 알아?”

길드장이 담배 연기를 내뿜으며 말했다.

“길드 연합 조찬 모임.”

중소 길드도 기업체다. 지역마다 연합과 친목 도모를 위해 각 길드장끼리 모임을 갖는 일이 있는데, 그게 바로 오늘이었다.

“공복에 겨우 한술 뜨려는데, 상동 길드장 그 새끼가 재미있는 얘기를 하더라. 이번에 각성한 C급짜리가 며칠 전까지 우리 길드 식구였다고.”

“……길드장님, 그게.”

길드장이 손을 들어 김상식의 이어지는 말을 막았다.

“뭔 개소린가 싶었지. 근데 상동 길드장이 싸가지 없는 새끼인 건 맞는데, 없는 얘기까지 지어낼 놈은 아니거든. 그것도 연합 모임에서.”

“제가, 제가 다시 알아보겠습니다!”

“3팀장이? 아냐, 그럴 필요 없어.”

길드장이 구겨진 종이 뭉치를 휙 던졌다.

“내가 따로 알아봤으니까.”

김상식은 이 구겨진 종이 뭉치의 정체가 누군가의 신상 명세서라는 사실을 알 수 있었다. 그의 이름도.

“진태경, 3팀장도 아는 이름이지?”

‘씨발.’

눈을 질끈 감는 김상식을 보며 길드장이 담뱃재를 털었다.

“3팀장 마음 알아. 나름 길드 창립 멤버고, 마음에 안 드는 최하급 헌터 하나 자를 수도 있지. 빈자리에 사랑하는 아들도 꽂아 주고. 안 그래?”

“예, 예.”

“그런데 실컷 박대하고 내쫓았던 F급 미꾸라지가 용 돼서 돌아왔네? 길드장이 꼭 영입하라고 신신당부까지 했는데 사실대로 말하면 지랄 떨 게 뻔하고, 사람도 못 알아보는 개눈깔이라고 소문날 것 같고. 그래서 허위 보고 올린 거지? 그렇지?”

치지직.

길드장은 담배를 비벼 껐다. 불씨가 흩어지며 그의 마지막 인내심도 사라졌다.

“3팀장. 아니, 상식아. 우리가 20년쯤 됐나?”

김상식이 불안한 목소리로 대답했다.

“21년입니다, 길드장님.”

“그게 아니지.”

“……예, 형님.”

“그래, 듣기 좋네. 앞으로 쭉 그렇게 해.”

“예?”

“21년 끌고 와 줬으면 할 만큼 했다. 3팀 애들한테는 따로 말할 테니까 오늘부로 퇴사해.”

“혀, 형님!”

“조용히 입 닥치고 꺼지면 앞길은 안 막는다. 나가서 뭘 하든 네 마음대로 해.”

분노를 꾹꾹 눌러 담은 길드장의 목소리.

김상식은 더 이상 선택지가 없다는 사실을 깨달았다.

‘나가라고? 길드를?’

20년 넘게 몸담았던 직장이다. 그런데 고작 이런 일로 나가라니. 망설임 없이 내치다니.

‘이런 씨발…….’

이를 악물고 사무실을 나서는 그의 등 뒤로 마지막 한 방이 날아왔다.

“어, 인사팀장. 오늘 두 명 퇴사 처리 해. 김상식이랑 김상호.”

그 후, 며칠간 소풍 길드는 부자(父子) 동시 퇴사라는 보기 드문 사건으로 시끄러웠다.

그와 함께 길드 내 핫이슈로 떠오른 건 얼마 전 퇴사한 최하급 헌터의 근황이었다.

“C급이래. 재각성.”

“어머, 태경 씨가요? 내가 아는 그 태경 씨?”

“그렇다니까. 완전히 로또 맞은 거지. 김상식 그 인간이 누군지도 모르고 영입하러 갔다가 제대로 뺀찌 먹었다는데.”

“온갖 트집 잡아서 자르더니, 뿌린 대로 거뒀네요. 듣기로는 김 팀장님, 돌아다니면서 부당 해고라고 길드장님 욕하고 다닌다던데.”

“정신 못 차린 거지. 크, 아무튼 부럽다. 나도 언제쯤 그런 인생 살아 보나.”

“솔직히 태경 씨는 자격 있죠. 그렇게 열심히 살던 사람이니까 행운도 찾아온 거지.”

“자격은 무슨. 그럼 우리는 죄다 흥청망청 사는 사람들이야? 다 운빨이지, 운빨.”

부러움 반, 질투 반인 대화의 끝은 늘 한 가지 의문으로 끝맺었다.

“태경 씨, 지금 어디서 뭐 하고 있을까?”
```

### Current accepted English

```markdown
# Chapter 50

My mouth fell open at the sight in front of me.

In the hot, humid heat, wetlands stretched on without end along a dense forest.

“This is a D-rank Gate…”

I knew higher-ranked Gates had more space. I just hadn’t thought the difference would be this big.

“Pretty big, right?”

I forgot to be angry and answered.

“Yeah. Big enough to feel lost.”

“This is fairly average. From B-rank Gates on, you even have to hire a separate guide.”

“…Feels like we need one now.”

“We’ll be fine today.”

Team Leader Choi pulled out a laminated sheet and showed it to me.

“What’s that?”

“A map. They gave it to me along with the transfer of rights.”

A map. Then we wouldn’t get lost—

“Wait. What did you say?”

“I said it was a map.”

“No, not that. You said something after that.”

“You mean the transfer of rights?”

Yeah, you. That.

“What does that mean?”

“Exactly what it sounds like.”

Team Leader Choi spoke as if it were nothing.

“This Gate is mine.”

“What?”

“More precisely, I have the exclusive rights to it.”

Maybe it was the wetlands. Sweat beaded on my palms, and my throat went bone-dry.

I swallowed a dry gulp.

*Exclusive rights to a Gate?*

In South Korea, Gates were national property.

Since the Great Cataclysm, Magic Gems had become a core energy source, and Gates were no different from diamond mines that never ran dry. And this guy had exclusive rights to one of those Gates.

*What the hell is he?*

I knew he was a rich family’s young master, but I hadn’t thought it went this far.

“Let’s get moving.”

Team Leader Choi strode ahead. The sight of his back was dazzling.

Ah, that golden radiance. The scent of wealth I could never touch.

*I’ll bury my bones in your Guild.*

I swore it then and there.

* * *

The wetlands were a maze.

Without a capable guide like Team Leader Choi, I would have wandered for a long time. How long had we been walking when—

- Keeiik.

The cry grew even clearer as I drew up my internal energy.

A monster had appeared.

*At least twenty.*

According to Team Leader Choi’s explanation on the way here, the monsters in this Gate were swamp Lizardmen.

They lived in several colonies under a single tribe, and this seemed to be one of them.

“This is the small colony closest to the entrance. About twenty of them, so let’s take them out fast and move on.”

Team Leader Choi hacked through the vines as he advanced. He was usually a pretty-faced young master, but once real combat started, he was no joke. The back driving forward like an eight-ton truck with a broken steering wheel reeked of machismo.

*He’s fucking cool.*

Even if it weren’t thirty Lizardmen but a hundred, I felt like we could sweep them all as long as Team Leader Choi was with me.

Now I understood why people let high-level players carry them in online games.

“Keiik!”

Maybe that was why my first face-to-face with Lizardmen didn’t come with much tension.

All I had was the novelty of seeing monsters I’d only ever seen in photos and videos.

“Oh, they’re big.”

Even the smallest of the twenty was a head taller than me.

They were at least two meters tall, with sleek muscle and thick tails that made them look even bigger.

*Of course, still not as big as the Hobgoblin Great Warrior I fought yesterday.*

These hideous basketball prospects didn’t seem too happy to see us.

- Keiik!

- Keet, keet!

Dozens of harpoons flashed in their hands. Watching them close in from the front in an encircling formation, I spoke.

“No archers.”

“Swamp Lizardmen mostly use harpoons. Watch out for thrown spears, just in case.”

“Yep.”

As expected of a lizard expert. He even had his arms folded, nice and easy.

“Keiik!”

They’d come within twenty meters. I grinned at Team Leader Choi.

“These guys have no fear.”

“That’s a Lizardman trait. They’re reckless, and they prefer a head-on fight.”

“Aha.”

Meanwhile the distance closed to ten meters. Team Leader Choi’s folded arms were starting to get on my nerves.

“I think we should start fighting soon.”

“Guess we should.”

“…Ah. Right. We should.”

Whoosh!

Then three or four harpoons tore through the air. If I’d still been an F-rank Hunter, my life would have flashed before my eyes. Now I just swung my spear and batted them aside.

Clang, clang, clang!

It was only after that that I sensed something off.

- Kieeeik!

- Keet! Keiik!

*What’s wrong with them?*

Their eyes rolled back white as they shrieked. This had gone past hostility. It was practically hatred.

As I stood there bewildered, Team Leader Choi tossed out a line.

“It’s because of your equipment.”

Equipment? Why would equipment—

Ah.

*Lizardman Hunter’s Leather Set. Lizardman Slayer’s Harpoon.*

*Shit. Look at those names.*

If I were a Lizardman, I’d throw harpoons too.

*Come to think of it, they only threw them at me.*

With the enemy of their kind standing right in front of them, Team Leader Choi might as well have been invisible.

At this rate I was going to get attacked nonstop—

No, wait.

“Did you plan this?”

“Plan what?”

“You put this on me to pull aggro so you could mop them up. That’s the strategy, isn’t it!”

“I swear it isn’t.”

Team Leader Choi’s face turned serious as he added,

“Because I’m going to stay put.”

“What?”

“You’ll pull the aggro, and you’ll do the raid too. Don’t get the wrong idea.”

*What the hell is this bullshit.*

“So… I have to fight them alone?”

“Yes.”

“And you’ll stand there with your arms folded and watch?”

“I’ll uncross my arms.”

“No, for fuck’s sake…”

“Harpoons incoming.”

Whoosh!

As the spears were thrown, green scales flashed from every direction and they charged.

Team Leader Choi sprang back and shouted with heroic gravity,

“You got this!”

Was this guy completely insane?

I wanted to run over and grab him by the collar, but harpoons were already flying in from all sides.

Clang!

- Keiik!

“You bastards.”

Grinding my teeth, I drew up my Qi Sense. Soon, twenty spears sprang up over their heads.

> **System**
>
> **Lv. 40 Lizardman Tribesman**

Level 40, huh?

I tightened my grip on my spear.

“You’re all dead.”

Ding.

> **System**
>
> - Damage dealt to this monster increases by 10% due to the effect of **Lizardman Hunter’s Leather Set**.
>
> - Damage dealt to this monster increases by 20% due to the effect of **Lizardman Slayer’s Harpoon**.
>
> - All **Lizardmen** in this Gate are hostile toward you. They will never stop until they repay this grudge!

At the same time, the Lizardman Slayer’s Harpoon traced a heavy arc. The forms of the Jin Family’s Spear Technique, having reached Seven Stars, poured toward them.

Crunch!

* * *

- Keiik…

The yellow reptilian eyes slowly closed.

The green wetlands were soaked with the corpses and blood of the ones already dead. Not a single Lizardman was left standing.

Ding.

> **System**
>
> - Level Up!
>
> - Level Up!

Leaving the cheerful System notifications behind me, I turned around.

Team Leader Choi was leaning against a tree. He’d said he wouldn’t fold his arms, and there he was with them folded. That made me twice as pissed.

“What do you think you’re doing?”

Team Leader Choi looked at me in silence, then tossed something over.

A small drink bottle of red liquid. A potion that restored depleted Stamina.

“So you give me the disease and then the medicine?”

“You look pretty healthy for a sick man. Not a scratch on you.”

…That actually sounded plausible. I nearly bought it.

While I hesitated, Team Leader Choi spoke.

“I’m sorry.”

He didn’t stop there. He even bowed at the waist.

It was such a formal apology I had nothing to say. My anger eased a little, but I still needed the reason.

“Why did you do that?”

“I had to see your skill.”

“Just for that?”

“It’s important to me. I need to know how you move, how much you can take on, and how far we can go together.”

“So you just slipped out alone while it was crawling with monsters?”

“If I hadn’t trusted you, I wouldn’t have.”

When a capable guy hyped me up like that, I had to admit it felt good.

*More importantly, I didn’t even get hurt, and I leveled up twice.*

I asked, quietly hopeful.

“And the results?”

“Hmm.”

Team Leader Choi studied me with that peculiar look of his. At last he opened his mouth.

“I still don’t know.”

“What?”

“Which is why.”

Team Leader Choi pulled something out and tossed it to me.

A long, opaque cylinder. When I shook it, liquid sloshed inside.

“What is this, a potion?”

“There’s a button on the bottom, right? Press it.”

*Does it open when I press it?*

I tilted my head and pressed the button.

Click.

The front of the cylinder sprang wide open.

The problem was—

Fwoooosh—

Boom!

Whatever had been inside shot up like a firework and burst in midair. The pink liquid that exploded there spread out over a wide area.

“Huh?”

*What is that?*

As I stared blankly at the sight, Team Leader Choi’s voice dug into my ear.

“It’s pheromones.”

“Pheromones? Perfume?”

“Something like that.”

“…?”

“It was collected from female Lizardmen.”

The instant he finished speaking, I felt a tremor from somewhere.

The ground. The ground was rumbling.

Team Leader Choi kindly added,

“The effect is extremely powerful.”

*You bastard…*

* * *

“Team Leader Three.”

That was the first thing the middle-aged man with half-gray hair had said in an hour. Kim Sangshik, who had been waiting endlessly while the Guild Master chain-smoked, answered.

“Yes, Guild Master.”

“Curious, aren’t you? Figured I called you in first thing this morning to raise hell?”

“Ah, no, sir.”

The Sopung Guild Master smiled good-naturedly.

“That’s right.”

“What?”

“I called you to raise hell.”

“…”

“Do you know where I went today?”

The Guild Master exhaled a plume of cigarette smoke.

“The Guild Alliance breakfast meeting.”

Small and midsize Guilds were corporations too. In each region, Guild Masters held meetings to form alliances and socialize. That was where he’d been today.

“I was on an empty stomach, just about to take a bite, when that Sangdong Guild Master bastard told me something interesting. He said the C-rank who awakened recently had been one of our Guild people until a few days ago.”

“…Guild Master, that…”

The Guild Master raised a hand and stopped Kim Sangshik from continuing.

“I wondered what kind of bullshit that was. But rude as the Sangdong Guild Master is, he isn’t the type to make up a story. Not at an alliance meeting, either.”

“I’ll look into it again myself!”

“Team Leader Three? No. No need.”

The Guild Master threw a crumpled bundle of papers across the room.

“I already looked into it myself.”

Kim Sangshik recognized the crumpled papers for what they were: someone’s personal file.

And the name on it, too.

“Jin Taekyung. Team Leader Three knows that name too, right?”

*Fuck.*

Kim Sangshik squeezed his eyes shut. The Guild Master tapped the ash from his cigarette.

“I know how you feel, Team Leader Three. You’re a founding member of the Guild, after all. You’re allowed to fire one bottom-tier Hunter you don’t like. Stick your beloved son in the vacancy. Right?”

“Yes, yes.”

“But the F-rank loach you treated like dirt and kicked out turned into a dragon and came back, huh? I even made a point of telling you to recruit him, but if you told the truth I’d obviously raise hell. You’d get a reputation for having dog eyes that can’t even recognize someone. So you filed a false report, right?”

Sizzle.

The Guild Master crushed out his cigarette. As the embers scattered, the last of his patience went with them.

“Team Leader Three. No, Sangshik. Have we been together about twenty years?”

Kim Sangshik answered in an uneasy voice.

“Twenty-one years, Guild Master.”

“That’s not what I meant.”

“…Yes, hyung.”

“Good. That sounds nice. Keep calling me that from now on.”

“What?”

“Twenty-one years of dragging you along is enough. You’ve done your part. I’ll talk to the Team Three kids separately, so as of today, you’re out.”

“H-hyung!”

“Shut your mouth, leave quietly, and I won’t block your path. Once you’re out, do whatever you want.”

The Guild Master’s voice was packed with tightly suppressed fury.

Kim Sangshik realized he had no choices left.

*Leave? Leave the Guild?*

This was the workplace he’d spent more than twenty years in. And now he was being told to leave over something like this. Thrown out without a second thought.

*Fuck…*

He clenched his teeth and walked out of the office.

One last blow came after him.

“Hey, HR. Process two resignations today. Kim Sangshik and Kim Sangho.”

For the next few days, Sopung Guild was in an uproar over the rare event of a father and son resigning at the same time.

Along with that, the hottest topic in the Guild became the recent whereabouts of the bottom-tier Hunter who had quit not long before.

“They say he’s C-rank. A reawakening.”

“Oh my, Mr. Taekyung? The Taekyung I know?”

“That’s what I’m saying. He hit the lottery. Apparently Kim Sangshik went to recruit him without even knowing who he was and got shut down hard.”

“He found every excuse he could to fire him, and now he’s reaped what he sowed. I heard Team Leader Kim’s been going around calling it wrongful dismissal and badmouthing the Guild Master.”

“He still hasn’t come to his senses. Still, I’m jealous. When do I ever get to live a life like that?”

“Honestly, Taekyung deserves it. He worked so hard, so luck found him.”

“Deserves it, my ass. Then are the rest of us all just living it up? It’s luck. All luck.”

Half envy, half jealousy, the conversations always ended with the same question.

“Where is Mr. Taekyung now, and what’s he doing?”
```
## Chapter 51

### Korean source

```text
＃51화



쉬쉬쉭!

검, 도끼, 철퇴.

수십 개의 무기가 소나기처럼 쏟아졌다. 그러나 내게는 똑똑히 보인다. 공격 하나하나가 어디로, 어떻게 향하는지.

그 틈을 파고들었다.

서걱-

C급 몬스터, 리자드맨 전사의 목을 쳐 날리는 게 시작이었다. 창날이 반원을 그림과 동시에 사방에서 핏물이 솟구쳤다.

띠링. 띠링. 띠링.



- [Lv.40 리자드맨 전사]를 처치했습니다!

- [Lv.41 늪지대 리자드맨]을 처치했습니다!

- [Lv.40 늪지대 리자드맨]을…….



- 키이이…….

살아남은 놈들이 주춤거리며 물러선다. 동족의 원수를 만나 살기를 뿜어내던 녀석들이, 지금은 두려움에 떨고 있다.

하지만 그것도 잠시.

- 크워어어!



- 보스 몬스터, [Lv.52 리자드맨 대족장]이 출현했습니다!

- 스킬, [전장의 함성]을 사용합니다!



최소 두 배는 큰 덩치. 거대한 철퇴를 든 리자드맨 족장의 외침에 공기가 터져 나간다. 우두머리의 등장에 뒷걸음질 치던 리자드맨들이 정신을 차리고 대열을 갖췄다.

‘어쩐 일로 쉽게 끝나나 했다.’

등 뒤로 최 팀장의 느긋한 목소리가 들렸다.

“가능하겠어요?”

“그게 며칠 동안 손 하나 까딱 안 한 사람이 할 소립니까?”

“이야기가 다르죠. C급 게이트니까.”

“그럼 도와주시든가.”

곰곰이 생각하던 최 팀장이 대답했다.

“그건 안 되겠네요. 제가 오늘 한정판을 입고 와서. 피라도 튀면 마음 아프잖습니까.”

“……진짜 아프게 해 드려요?”

대화를 이어 갈수록 내상을 입은 것처럼 속이 쓰리고 뒷골이 당긴다. 차라리 몬스터와 싸우는 게 낫지.

성큼 앞으로 한 걸음 내딛는 내게 최 팀장이 한 마디를 툭 던졌다.

“후퇴도 또 하나의 방법입니다.”

한정판 장비에 피 튈까 봐 뒤에서 팔짱만 끼고 있는 인간이 제법 맞는 말을 한다. 처맞는 말.

그리고…….

“더 좋은 방법이 있는데 뭐 하러요?”

저 앞. 리자드맨 대족장을 필두로 몬스터들이 파도처럼 밀려오고 있다. C급과 D급 몬스터가 뒤섞인, 평범한 C급 헌터라면 맞설 엄두도 못 낼 전력이었다.

평범한 C급 헌터라면, 말이다.

‘상태창 오픈.’

띠링.

시스템이 즉각 응답했다.

헌터 일을 다시 시작하고 일주일이 지난 지금, 상태창에는 40레벨이라는 숫자와 맨 밑에 적힌 글씨가 반짝반짝 빛나고 있었다.



- 잔여 포인트 : 100



현실로 돌아온 이래 나는 한 번도 잔여 포인트를 쓰지 않았다. 순전히 호기심 때문이었다. 지금의 내가 어디까지 갈 수 있을까, 하는 의문.

하지만 이 이상 아끼는 건 만용이다.

‘근력, 체력에 각각 30. 민첩에 40 부여.’

다음 순간, 잔여 포인트가 바닥을 드러냈다.

하지만 그와는 반대로 내 몸속 깊숙한 곳에서는 새로운 힘이 솟구쳤다. 불과 몇 초전의 진태경과는 또 다른 내가 지금 이곳에 있었다.

‘그래, 이거지.’

희열감에 몸이 부르르 떨리던 그때.

- 크아아아!

리자드맨 대족장이 포효와 함께 돌진했다. 그림자를 드리운 거대한 철퇴를 향해, 나는 창을 뻗었다.

“일섬(一晱).”

창날의 끝에서, 바람의 길이 열렸다.



* * *



“허.”

최 팀장, 최민우는 헛웃음을 흘렸다.

늪지대를 감싸 안은 농밀한 피 안개, 그리고 그 아래 널브러진 몬스터들의 사체가 그의 눈에 비쳤다.

‘이게 무슨.’

보스 몬스터를 포함한 수십 마리의 몬스터가 한순간에 몰살당했다. 이 모든 게 고작 며칠 전 재각성한 C급 헌터의 창끝으로부터 벌어진 일이었다.

‘이런 게 가능한가?’

진태경을 처음 만난 날부터 품고 있던 의문이었다. 별생각 없이 E급 게이트에 갔던 그날, C급 헌터 두엇은 달라붙어야 하는 레어 몬스터를 압도적으로 밀어붙이던 그 모습.

거기에 더해 지난 며칠 동안 그가 보여 준 힘은…….

‘C급 헌터라니, 웃기지도 않지.’

진태경과 단둘이 레이드를 시작한 이유는 간단했다.

이 흥미로운 인물의 한계를 보기 위해서. 그리고 다른 이들에게 들키지 않기 위해서.

그러나 문득 그런 생각이 들었다.

‘혹시 나보다…….’

아니, 아니다. 그럴 리가 없다.

애써 이어지는 생각을 털어 내는 최민우의 눈에 진태경이 들어왔다. 그는 상반신이 날아간 보스 몬스터의 사체를 붙잡고 애통한 외침을 토해 내고 있었다.

“안 돼! 내 가죽! 이거 비싼 건데!”

……저런 인간이 그럴 리가 없지. 아니, 그러면 안 되지.

최민우는 문득 억울해졌다.



* * *



불타는 금요일. 줄여서 불금.

20대 청춘들은 무리지어 술 마시고, 클럽을 들락거리겠지만 나는 최 팀장과 게이트를 돌았다.

오전에 한 번. 오후에 두 번. 그렇게 C급 게이트 세 번을 돌고 나오자 밖은 이미 어두운 밤이었다.

“고생하셨습니다, 도련님.”

이제는 익숙한 얼굴이다. 선 굵은 외모의 이 40대 아저씨를 최 팀장은 이렇게 불렀다.

“김 집사님도 수고하셨어요.”

김 집사. 비서도 아니고 집사다.

워낙 현실성 없는 단어라 처음에는 잘못 들은 줄 알았다.

‘나는 교회 집사밖에 못 만나 봤는데.’

그는 일주일 용돈으로 천 원을 받던 나의 코흘리개 시절, 십일조로 백 원을 내라고 강요하던 불한당이었다.

물론 나를 도련님이라고 불러 주지도 않았고, 심지어는 내가 십일조를 내기 싫다고 버티자 사탄의 자식이라고 중얼거렸다.

그리고 일곱 살이었던 나는 궁금한 건 꼭 물어보는 성격이었다.



‘엄마. 엄마가 사탄이야?’

‘응? 사탄?’

‘어. 교회 집사님이 그랬는데, 내가 사탄의 자식이래. 난 엄마 자식이니까 엄마가 사탄이지? 그치?’



그 말이 엄마를 사탄으로 만들었다. 나는 두 번 다시 교회 떡볶이를 못 먹게 됐고 교회 집사는 주님 곁으로 갈 뻔했다.

다시 생각해 보니 인생 진짜 버라이어티 하네.

“하실 말씀이라도……?”

김 집사의 말에 정신을 차렸다.

“아무것도 아닙니다. 잠깐 다른 생각 좀 하느라.”

“이제 퇴근합시다.”

최 팀장은 어느새 사복 차림으로 갈아입었다. 얇은 맞춤 정장을 입은 모습이 꼭 연예인 같다.

‘인생 진짜. 더럽게 불공평하네.’

나는 내심 투덜거리며 장비를 벗기 시작했다. 물론 조심스러운 손길로. 첫날 검색해 봤는데 가격이…… 됐다, 말을 말자.

김 집사가 장비를 건네받아 차에 싣는 사이, 나는 최 팀장에게 물었다.

“내일은 몇 시에 나와야 합니까?”

“내일 말입니까?”

최 팀장이 의아한 듯한 목소리로 되묻는다.

“오늘 금요일입니다.”

“네.”

“내일은 토요일이고요.”

“금요일 다음이 토요일인 건 저도 알죠.”

이게 누굴 병신으로 보나.

“아니, 그러니까.”

최 팀장이 눈썹을 찡그렸다.

“설마, 주말도 일하시게요?”

“……당연한 거 아니에요?”

“…….”

“…….”

최 팀장이 충격받은 얼굴로 물었다.

“아니, 주말에 안 쉬면 언제 쉽니까?”

“음. 일 못 구할 때?”

“그게 얼마나 되는데요.”

“글쎄요. 많이 쉬면 한 달에 한 번?”

“길드 소속이었잖습니까. 주말에도 출근했어요?”

“했죠. 일 있으면.”

“그거 헌터 근로법 위반 아닙니까?”

완벽해 보이던 최 팀장도 모르는 게 딱 하나 있었다.

세상 물정.

나는 피식 웃었다.

“그거 꼬박꼬박 지키는 중소 길드가 어디 있어요. 다들 추가 수당 더 얹어 주고 레이드 시키지. 뭐, 저야 좋지만.”

“예? 좋다고요?”

“주말에는 인력 사무소 가거든요. 그거 갈 바에야 길드에서 추가 수당 받는 게 훨씬 나으니까. 기록 남을까 봐 현찰로 딱딱 주고.”

“…….”

“뭐, 다 그런 거죠.”

최 팀장이 고개를 절레절레 저었다.

“우리 길드는 근로법 준수합니다. 가계약도 마찬가지예요.”

그거 아쉽네. 이번 주말에는 인력 사무소에 가야 할 모양인가 보다.

입맛을 다시는 나를 최 팀장이 특유의 묘한 눈빛으로 바라본다.

“그렇게까지 하는 이유가 뭡니까?”

“이유?”

“이제 C급 헌터잖아요. 좀 쉬면서 해도 될 텐데요.”

“그건…….”

시스템이 언제 사라질지 몰라서요.

목구멍에서 불쑥 튀어나오려는 말을 붙잡았다. 그건 누구한테도 말할 수 없는 나만의 비밀이다.

“별 이유 없어요. 물 들어왔을 때 노 저어야죠.”

“그렇게 일하다가는 노 부러집니다. 같이 배 타고 있는 사람도 생각하세요.”

“같이 타고 있는 사람? 최 팀장님이요?”

“뭐, 이를테면…….”

최 팀장이 멈칫하더니 말을 이었다.

“가족이라든가.”

가족.

고작 한 단어일 뿐인데, 몸 구석구석 온기가 스며든다. 통화는 가끔 하지만 벌써 두 달이 넘도록 보지 못했다. 무림에서의 시간까지 포함한다면 석 달이다.

‘벌써 그렇게 됐나.’

아버지가 돌아가신 이후 내 인생은 줄곧 오르막길을 달리는 차 같았다.

그래서 엑셀만 밟을 수밖에 없었다. 발을 떼면 굴러떨어질 것 같아서. 금방이라도 시동이 꺼질 것 같아서.

“아무튼 주말은 쉽니다. 인력 사무소 갈 생각하지 말고 쉬세요. 그거 계약 위반이니까.”

“아, 네.”

이렇게까지 억지로 쉬라는 거 보면 최 팀장 이 인간, 은근히 인성이 괜찮은…….

아니지, 겨우 이 정도 감성 팔이에 넘어가면 안 되지. 그동안 나 혼자 어떤 개고생을 했는데.

‘최 팀장은 악덕 고용주다. 악덕 고용주.’

주말에 쉬라는 것도 당장 다음 주부터 대차게 부려 먹기 위함인 게 뻔했다. 엄한 데 체력 소모하지 말라는 노예 농장주의 마음가짐인 거지. 지독한 인간.

“준비 끝났습니다, 도련님.”

그때 장비를 실으러 갔던 김 집사가 돌아왔다.

저 양반도 악덕 고용주 밑에서 고생이다. 밤 열 시가 다 돼 가도록 퇴근을 못 하고 있네.

“아, 말씀드린 건요?”

“가져왔습니다.”

“드리세요.”

악덕 고용주의 말에 김 집사가 손에 든 작은 박스를 내밀었다.

“받으시죠, 헌터님.”

나한테.

“예? 저요?”

보기에는 드링크병 박스 같은데. 눈만 끔뻑거리다가 머릿속을 번뜩 스치는 생각이 있어 조심스레 물었다.

“설마 이거 돈이에요?”

“주급으로 계약했잖습니까. 잊으셨어요?”

깜빡했다. 당연히 일요일에 받을 줄 알았거든.

나는 얼떨떨한 얼굴로 박스를 받아 들었다. 묵직하다.

“보통 현금 지급인가요?”

“당연히 아니죠.”

“그럼…….”

“진태경 씨가 현금이 좋다면서요. 특히 빳빳한 신권.”

어제였나, 그저께 흘리듯이 얘기한 건데 이런 식으로 돌아올 줄이야. 악덕 고용주에서 평가가 조금 더 올라갔다.

‘물론 가장 중요한 게 남았지.’

화요일부터 금요일까지. 총 4일 치 급여다. C급 헌터로서 받는 첫 주급이고. 금액이 기대될 수밖에 없다.

꿀꺽. 침을 삼키고 입을 열었다.

“그럼 이게 다 얼마…….”

“계약서보다 좀 더 챙겨 넣었습니다. 안에 정산 내역 있으니까 확인해 보시고요. 이만 갑니다.”

“다음에 또 뵙겠습니다, 헌터님.”

최 팀장과 김 집사가 쌩하니 사라졌다.

그야말로 순식간에 벌어진 일.

황당한 얼굴로 멀어지는 자동차 불빛을 바라보던 나는 드링크 박스를 열었다. 흐릿한 달빛 아래 두툼한 지폐 묶음이 눈에 들어온다.

‘하나, 둘, 셋…….’

숫자는 여섯에서 더 이상 올라가지 않았다.

백 장 묶음 여섯 개. 그러니까 6백만 원이다.

“뭐야, 이게.”

사기.

순간 뇌리를 스친 단어에 다리 힘이 풀리려는 찰나.

“어?”

내가 잘못 봤나? 왜 지폐 색깔이 누렇지?

“잠깐, 잠깐만!”

공력을 눈에 집중시키자 눈앞이 밝아진다. 그리고 봤다.

지폐 속, 한복을 입고 인자하게 웃고 있는 아주머니를.

“으아어어어! 신사임당! 현모양처! 아들이 율곡 이이! 남편은 이원수!”

나도 모르게 방언이 터져 나온다. 미쳤다. 이건 미쳤어.

신사임당 백 장이 한 묶음. 그게 여섯 개니까…….

“사, 삼억!”

이번에는 풀리는 다리를 붙잡지 못했다. 쿵, 소리가 날 만큼 세게 무릎을 꿇은 나는 넋 나간 눈빛으로 드링크 박스 안을 바라봤다.

지폐 묶음 밑, 흰 종이가 박스 바닥에 깔려 있었다.

‘맞다. 정산서!’

허겁지겁 종이를 펼쳤다.

그곳에는 지난 4일간의 수익이 빠짐없이 기록되어 있었다.

내게 지급되는 최종 금액까지.

‘정산서에는 3천만 원으로 나와 있는데?’

뭐지? 착각했나?

혼란하다, 혼란해. 흔들리던 내 동공이 마지막 줄에 가서 딱 멈췄다.



보너스 : 270,000,000



그리고 최 팀장이 떠나며 남겼던 마지막 말까지.



‘계약서보다 좀 더 챙겨 넣었습니다.’



쿠르릉.

머릿속에서 천둥 번개가 휘몰아친다. 나는 후들거리는 다리로 일어났다. 저 멀리, 이미 희미해진 차의 불빛이 보인다.

그건 마치 한 줄기 빛 같았다.

“아아. 아아아…….”

최 팀장. 아니, 그는 ‘빛’이다.
```

### Current accepted English

```markdown
# Chapter 51

Swish, swish, swish!

Swords, axes, maces.

Dozens of weapons poured down like rain. But I could see every one of them clearly—where each attack was headed, and how.

I slipped through the gaps.

Slice—

It started with me taking the head off a C-rank monster, a Lizardman Warrior. The instant the spearhead drew a semicircle, blood spurted in every direction.

Ding. Ding. Ding.

> **System**
>
> - You defeated **Lv. 40 Lizardman Warrior**!
>
> - You defeated **Lv. 41 Swamp Lizardman**!
>
> - You defeated **Lv. 40 Swamp Lizardman**…

- Keeee…

The survivors hesitated and backed away. The same creatures that had been pouring out killing intent at the enemy of their kin were now trembling with fear.

But that lasted only a moment.

- Gwoooaar!

> **System**
>
> - Boss Monster, **Lv. 52 Lizardman Great Chieftain**, has appeared!
>
> - Uses Skill **Battle Cry**!

A frame at least twice as large as the others. The roar of the Lizardman Chieftain, gigantic mace in hand, exploded through the air. The Lizardmen that had been backing away came to their senses at their leader’s appearance and formed ranks.

*I was wondering why this was wrapping up so easily.*

Team Leader Choi’s unhurried voice came from behind me.

“Can you handle it?”

“Is that something someone who hasn’t lifted a finger for days should be asking?”

“This is a different story. It’s a C-rank Gate.”

“Then help, why don’t you.”

Team Leader Choi thought it over before answering.

“I don’t think I can. I wore a limited edition today. It’d break my heart if blood splattered on it.”

“……Should I make it hurt for real?”

The longer we talked, the more my gut burned and the back of my head throbbed, like I’d taken internal injuries. Fighting monsters would have been better.

As I took a long stride forward, Team Leader Choi tossed out a single line.

“Retreat is another option.”

The man standing behind me with his arms folded so blood wouldn’t splatter on his limited-edition Equipment had said something pretty sensible.

A punchable kind of sensible.

And then…

“Why bother, when there’s a better way?”

Ahead of us, the monsters were surging forward like a wave, led by the Lizardman Great Chieftain. C- and D-rank monsters mixed together—a force an ordinary C-rank Hunter wouldn’t even dream of facing.

An ordinary C-rank Hunter, that is.

*Status Window, open.*

Ding.

The System answered at once.

A week had passed since I’d started Hunter work again. On the Status Window, the number 40 and the line written at the very bottom were shining bright.

> **System**
>
> - Remaining Points: 100

Since returning to reality, I hadn’t spent a single Remaining Point. Purely out of curiosity.

*How far can I go as I am now?*

But hoarding them any further would be reckless.

*Assign 30 each to Strength and Stamina. Assign 40 to Agility.*

The next moment, my Remaining Points hit zero.

In exchange, new power surged up from deep inside me. A different me from the Jin Taekyung of only a few seconds ago was standing here now.

*Yeah. This is it.*

My body was still shivering with exhilaration when—

- Gwaaaar!

The Lizardman Great Chieftain charged with a roar. I thrust my spear toward the gigantic mace that cast a shadow over me.

“One Flash.”

At the spearhead, a path through the wind opened.

* * *

“Hah.”

Team Leader Choi—Choi Minwoo—let out a hollow laugh.

A dense fog of blood wrapped the wetlands, and beneath it the monsters’ corpses lay sprawled.

*What the hell…*

Dozens of monsters, the boss included, had been slaughtered in an instant. All of it had come from the spear-tip of a C-rank Hunter who had reawakened only a few days ago.

*Is something like this even possible?*

It was a question he had carried since the day he first met Jin Taekyung.

That day, they had gone to an E-rank Gate without much thought. There, Taekyung had overwhelmingly overpowered a Rare Monster that normally took a couple of C-rank Hunters to bring down.

And on top of that, the strength he had shown over the past few days was…

*Calling him a C-rank Hunter is a joke.*

The reason Choi had started raiding with Taekyung alone was simple.

To see this fascinating man’s limits.

And to keep anyone else from finding out.

But another thought suddenly occurred to him.

*Could he be stronger than me…?*

No. No.

That was impossible.

Choi Minwoo forced the thought aside. That was when Jin Taekyung entered his vision.

He was clutching the boss monster’s corpse—its upper body gone—and wailing in grief.

“No! My hide! This was expensive!”

……There was no way a guy like that could be.

No. He *mustn’t* be.

Choi Minwoo suddenly felt cheated.

* * *

Burning Friday. *Bulgeum*, for short.[^1]

People in their twenties would be drinking in packs and drifting in and out of clubs. I was running Gates with Team Leader Choi.

Once in the morning. Twice in the afternoon.

By the time we finished three C-rank Gates and came back out, it was already dark.

“Good work, young master.”

That face was familiar now. Team Leader Choi called this broad-featured man in his forties that.

“You worked hard too, Mr. Kim.”

Kim the Butler. Not secretary—*butler*.[^2]

The word was so absurdly unrealistic I thought I’d misheard it at first.

*I’ve only ever met church deacons.*

Back when I was a snot-nosed kid getting a thousand won a week in allowance, he had been the bastard who forced me to put in a hundred won as a tithe.

Of course, he hadn’t called me young master. When I dug in and refused to pay, he’d even muttered that I was the child of Satan.

And I had been seven—the kind of kid who always asked when he was curious.

*Mom. Are you Satan?*

*Huh? Satan?*

*Yeah. The church deacon said I was Satan’s child. I’m your kid, so that makes you Satan, right? Right?*

That turned my mother into Satan.

I never got to eat the church tteokbokki again,[^3] and the church deacon nearly went to be with the Lord.

Thinking about it again, my life really was one hell of a variety show.

“Did you have something to say…?”

Butler Kim’s voice pulled me back.

“Nothing. I was just thinking about something else.”

“Let’s call it a day.”

Team Leader Choi had already changed into street clothes. In a thin tailored suit, he looked just like a celebrity.

*Life is so damn unfair.*

I grumbled inwardly as I started taking off my Equipment. Carefully, of course. I’d looked up the price on the first day, and it was…

Never mind. Let’s not go there.

While Butler Kim took the Equipment and loaded it into the car, I asked Team Leader Choi,

“What time should I come in tomorrow?”

“Tomorrow?”

Team Leader Choi asked back, sounding puzzled.

“Today is Friday.”

“Yes.”

“And tomorrow is Saturday.”

“I know Saturday comes after Friday.”

*Does he take me for a fucking idiot?*

“No, I mean…”

Team Leader Choi furrowed his brow.

“Don’t tell me you’re planning to work on the weekend too?”

“……Isn’t that obvious?”

“……”

“……”

Team Leader Choi asked with a shocked look,

“If you don’t take weekends off, when do you rest?”

“Um. When I can’t find work?”

“How often is that?”

“I don’t know. If I take a lot of time off, maybe once a month?”

“You used to belong to a Guild. You worked weekends then too?”

“I did, if there was work.”

“Isn’t that a violation of the Hunter Labor Law?”

Even Team Leader Choi, who seemed perfect, didn’t know one thing.

How the world actually worked.

I chuckled.

“What small or midsize Guild follows that to the letter? They all throw on extra pay and send you out on raids. Worked out for me, anyway.”

“Excuse me? You *liked* it?”

“I go to the Manpower Office on weekends. Getting extra pay from the Guild beats going there. They paid cash on the spot so there wouldn’t be a record.”

“……”

“That’s just how it is.”

Team Leader Choi shook his head in disbelief.

“Our Guild follows the Labor Law. Provisional contracts are no different.”

*That’s a shame. Looks like I’ll have to go to the Manpower Office this weekend.*

Team Leader Choi looked at me with that peculiar expression of his as I smacked my lips over the missed chance.

“Why do you go that far?”

“Why?”

“You’re a C-rank Hunter now. You could take it a little easier.”

“That’s…”

*Because I don’t know when the System might disappear.*

I caught the words before they jumped out of my throat. That was my secret—something I couldn’t tell anyone.

“No particular reason. You have to row when the tide comes in.”

“If you keep working like that, you’ll snap the oars. Think about the people in the boat with you.”

“The people in the boat with me? You, Team Leader?”

“Well, for example…”

Team Leader Choi paused, then went on.

“Your family, perhaps.”

Family.

It was only one word, but warmth seeped into every corner of my body. We talked on the phone now and then, but I hadn’t seen them in more than two months. Counting the time in Murim, it had been three.

*Has it already been that long?*

Ever since my father died, my life had been a car running uphill.

So I’d had no choice but to keep my foot on the gas. Take it off, and it felt like I’d roll backward. Like the engine might die at any second.

“Anyway, weekends are off. Don’t even think about going to the Manpower Office. Rest. That would be a contract violation.”

“Ah. Right.”

*Forcing me to rest this hard… Maybe this guy Choi isn’t such a bad person after all…*

No.

I couldn’t let myself get taken in by a little emotional appeal. Not after all the hell I’d gone through on my own.

*Team Leader Choi is an exploitative employer. An exploitative employer.*

It was obvious he only wanted me resting on the weekend so he could work me to the bone starting next week. The mindset of a slave plantation owner who didn’t want stamina wasted in the wrong places.

What a vicious man.

“Preparations are finished, young master.”

Butler Kim was back from loading the Equipment.

*That man’s suffering under an exploitative employer too. It’s almost ten at night, and he still hasn’t gotten off work.*

“Ah. What about the thing I mentioned?”

“I brought it.”

“Give it to him.”

At the exploitative employer’s word, Butler Kim held out the small box in his hands.

“Please take this, Hunter.”

To me.

“Huh? Me?”

It looked like a box of tonic drinks. I just blinked at it, then a thought flashed through my head and I asked carefully,

“Don’t tell me this is money?”

“We contracted for weekly pay. Did you forget?”

I had. I’d naturally assumed I’d get it on Sunday.

I took the box with a dazed look. It was heavy.

“Is it usually paid in cash?”

“Of course not.”

“Then…”

“You said you liked cash, Mr. Jin Taekyung. Especially crisp new bills.”

I’d mentioned it in passing yesterday—or the day before. I hadn’t expected it to come back like this.

My opinion of the exploitative employer rose a little.

*Of course, the important part’s still left.*

Four days of pay, Tuesday through Friday. My first weekly paycheck as a C-rank Hunter.

Of course I couldn’t help looking forward to the amount.

I swallowed and opened my mouth.

“Then how much is all of this…”

“We put in a little more than the contract. The settlement details are inside, so check them. We’ll be going.”

“Until next time, Hunter.”

Team Leader Choi and Butler Kim took off in a flash.

It really did happen in an instant.

I stared after the receding car lights, bewildered, then opened the drink box. In the faint moonlight, thick bundles of bills caught my eye.

*One, two, three…*

The count stopped at six.

Six bundles of a hundred bills.

In other words, six million won.

“What is this?”

*Scam.*

The word flashed through my mind, and just as my legs were about to give out—

“Huh?”

Had I seen it wrong? Why were the bills yellowish?

“Wait. Wait a second!”

I focused internal energy into my eyes, and the world in front of me brightened.

Then I saw her.

A kindly smiling woman in a hanbok, right there on the bill.

“Shin Saimdang! Wise mother and virtuous wife! Her son is Yulgok Yi I! Her husband is Yi Wonsu!”

Dialect burst out of me before I knew it.

This was insane. Completely insane.

One bundle was a hundred Shin Saimdang bills. Six of those, so…

“Th-three hundred million!”

This time I couldn’t catch my legs as they gave out. I dropped to my knees hard enough to thud and stared blankly into the drink box.

Under the bundles, a white sheet of paper lined the bottom.

*Right. The settlement sheet!*

I unfolded the paper in a panic.

It had a complete record of the past four days’ earnings.

Down to the final amount being paid to me.

*The settlement says thirty million won?*

What? Had I imagined it?

I was confused. Completely confused.

My shaking gaze froze on the last line.

**Bonus: 270,000,000**

And then Team Leader Choi’s last words as he left.

*We put in a little more than the contract.*

Thunder and lightning tore through my head.

I stood on trembling legs. Far off, the car’s lights were already fading.

They looked like a single ray of light.

“Ahh. Aaaah…”

Team Leader Choi.

No—he was the Light.

[^1]: Korean slang for Friday night, from “burning Friday.”
[^2]: In Korean, the same word, *jipsa*, means both butler and church deacon.
[^3]: Tteokbokki is a Korean dish of chewy rice cakes in a spicy sauce. Korean churches often sell it as a snack.
```
## Chapter 52

### Korean source

```text
＃52화



오전 여섯 시.

택시 기사 김 씨는 오늘의 첫 손님을 태웠다. 그리고 10분 만에 후회했다.

‘재수 옴 붙었네.’

겉보기로는 멀쩡하게 생긴 청년이다. 근육질의 듬직한 덩치에 얼굴은 멀끔해서 많이 쳐 줘야 20대 중후반으로 보였다.

그런데…….

“킁카킁카.”

이상하다. 좀 많이.

“흐어어.”

웬 드링크 박스를 보물처럼 꼭 껴안고, 30초에 한 번씩 슬쩍 열어 냄새를 맡는다. 그리고 뭐에 홀린 것처럼 몸을 부르르 떤다.

‘시방 저게 뭐 하는 짓이여.’

김 씨는 뒷골이 싸했다. 10년 넘게 택시를 몰았지만 이런 종류의 진상은 처음이다.

그가 계속해서 옆자리 청년을 곁눈질하던 그 순간.

“아저씨.”

“예, 예?!”

심장 떨어질 뻔했다.

방금 전까지만 해도 퀭하던 청년의 눈동자가, 야수처럼 번뜩이고 있었다.

“뒤에 트럭이요.”

“트, 트럭이요? 파란색?”

“네. 아까 사거리에서부터 따라오는 것 같지 않아요?”

“예? 아니 뭐, 그렇긴 한 것 같은데.”

“미행일지도 모르잖아요.”

이건 또 무슨 참신한 개소린가.

김 씨는 눈동자를 뒤룩뒤룩 굴리다가 결국 그가 원하는 듯해 보이는 원하는 대답을 내놨다.

“여, 옆쪽으로 빠지겠습니다.”

청년은 파란 트럭이 시야에서 사라질 때까지 드링크 박스를 꼭 껴안고 있었다. 마치 누군가가 뺏어 가기라도 할 것처럼.

“습하. 습하.”

물론 틈틈이 냄새를 맡는 것도 빼놓지 않았다.

‘이건 제대로 미친놈이다.’

차 내부는 에어컨 바람이 쌩쌩 부는데, 김 씨의 등허리는 식은땀으로 축축했다. 첫 개시부터 이 모양이라니.

아주 재수 옴 붙은 날이다.



* * *



부아앙.

요금을 건네고 문을 닫자마자 택시가 총알처럼 튀어 나간다.

누가 보면 뒤에서 몬스터라도 쫓아오는 줄 알겠네. 사고라도 나면 어쩌려고. 나는 쯧쯧 혀를 차고 아파트 단지로 들어섰다.

품에는 어제 받은 드링크 박스를 소중히 껴안은 채였다.

‘3억.’

내가 F급 헌터 시절부터 꼬박 3년을 일해서 모은 돈이랑 비슷한 액수다. 물론 지금은 한 푼도 안 남았다.

‘빚 갚는 데 다 썼지.’

그렇게 빚에 허덕이던 때가 있었는데, 이 악물고 하다 보니 점점 나아졌다. 가족을 일산 근처의 안전지대 아파트로 이사 보내기도 했고. 근래 들어서는 뭐, 인생이 롤러코스터 같다.

시스템이 사라지면 추락하는 롤러코스터…….

아니다. 몇 달 만에 오는 집인데 이런 생각은 집어치우자.

‘그런데 몇 동 몇 호였지?’

두어 달에 한 번 꼴로 오는 집이다 보니 늘 이렇다.

나는 다닥다닥 붙어 있는 아파트 단지를 노려보다가 핸드폰을 꺼내 전화를 걸었다. 한참 신호음이 울린 뒤에야 연결됐다.

딸칵.

- 여보세요?

아직 이른 시각이라 자고 있을 줄 알았는데, 하연이의 목소리는 또렷했다.

“일어나 있었어?”

- 일어나 있어야지. 시간이 몇 신데.

“아직 일곱 시도 안 됐는데.”

- 일찍 일어나야 공부가 잘돼.

내 동생이지만 감탄스럽다. 오전 기상을 7대 죄악쯤으로 여기는 진호 형이 이걸 들었어야 했는데.

- 왜 전화했어?

“내가 지금 집 앞이거든.”

- 응? 집 앞이라고?

“어. 근데 우리 집이 어딘지 까먹었어.”

- ……또? 가지가지 한다, 진짜. 기다려.

끊긴 전화를 붙잡고 몇 분쯤 기다렸을까, 어느 동 입구에서 여자애 하나가 슬리퍼를 질질 끌며 나타났다.

멀리서도 느껴지는 날백수 포스. 세상 귀찮다는 그 표정을 보자 나도 모르게 웃음이 나왔다.

“진하연!”

“소리 지르지 마. 사람들 깨.”

……그래, 이래야 내 동생이지.

“웬일이야? 말도 없이.”

“내가 우리 집 오는데 말하고 와야 되냐?”

“하도 드문드문 오니까 그렇지. 부녀회장이 오빠보다 우리 집 더 자주 올걸?”

“그 정도냐?”

“그 정도지.”

그때 엘리베이터가 멈췄다. 현관문 앞에 선 하연이가 비밀번호를 입력하고 문고리를 돌린다.

그리고 그곳에…….

“아들!”

환하게 웃고 있는 한 사람이 있다. 주름진 손과 반쯤 풀린 파마머리. 깜짝 선물을 받은 어린아이처럼 좋아하는 그 모습.

순간 목이 막힌 나는 턱을 긁적이다가 풀썩 웃어 버렸다.

“저 왔어요, 엄마.”

드디어 돌아왔다.

가족이 기다리고 있는 그곳. 집으로.



* * *



지글지글.

엄마는 부엌에서 아침 준비로 한창이다. 기분 좋은 냄새가 코끝을 맴돌았다.

“오랜만에 아들 왔다고 아주 신나셨네, 우리 김 여사.”

하연이가 배를 벅벅 긁으며 옆자리에 주저앉았다.

낡은 소파가 푹 꺼진다. 돼지 같은 년.

“요리 많이 준비하고 계셔?”

“어. 완전 진수성찬. 덕분에 잘 먹겠네.”

대답은 하는데, 눈은 핸드폰 화면에 박혀 있다.

“넌 오랜만에 오빠 봤는데 반갑지도 않냐?”

“응?”

“아니, 뭐. 고생했다고 어깨라도 좀 주물러 줄 수도 있고.”

하연이가 한숨을 푹 내쉬었다.

“왜 이래, 태경 씨. 우리 그런 사이 아니잖아.”

“……말하는 싸가지 봐라.”

이렇게 티격태격 하는 게 하루 이틀은 아니지만 괜히 섭섭하다.

나는, 어? 그렇게 죽을 고비 넘겨 가면서 겨우 돌아왔는데!

“지금 울컥했다. 울컥했지?”

눈치 하나는 귀신이다.

“학교 갈 준비나 해. 급식충아.”

“응. 오늘 개교기념일.”

주먹이 파르르 떨린다. 당장이라도 저 얄미운 뒤통수를 후려치고 싶지만 그러면 진짜 지는 거다.

“때리고 싶죠? 주먹 부들부들 하죠?”

“넌 여자라서 살았다. 불알만 달려 있었어도…….”

“엄마! 오빠가 나 성추행해!”

“야, 야!”

“오빠가 나한테 불. 읍, 읍!”

입을 틀어 막힌 하연이가 발버둥 친다. 때리고, 꼬집고. 그래 봤자 열아홉 살 여자애라 아프지도 않다.

그러다가 우연히, 녀석이 내뻗은 발이 소파 한구석에 고이 모셔 둔 드링크 박스를 강타했다.

퍽.

촤르르륵.

활짝 열린 박스. 거실 바닥에 쏟아지는 누런 지폐 뭉치.

순간, 하연이의 몸이 굳었다.

“이제 그만들 싸우고 아침 먹……어.”

거기에 부엌에서 나온 엄마까지.

일시 정지 버튼을 누른 것처럼 모든 게 멈춘 거실에, 찌개 끓는 소리만 잔잔하게 깔렸다.

지글지글.

나는 어색하게 웃으며 입을 열었다.

“밥 먹고 말하면 안 될까요?”

“……아들?”

“읍읍읍.”

아무래도 아침 식사는 한참 뒤로 미뤄질 것 같다.



* * *



가족들에게 지금까지의 일들을 적당히 각색해서 들려 주었다.

C급으로의 재각성, 그리고 돈의 출처까지.

“그렇게 된 거예요.”

반응은 두 가지로 나뉘었다.

“그렇구나.”

멍하니 고개를 끄덕이는 엄마.

그리고.

“증거.”

“…….”

그래, 넌 기대도 안 했다. 나는 한숨과 함께 지갑을 던져 주었다.

“뭐야?”

“확인해 봐.”

하연이가 의구심 가득한 눈으로 나를 바라보다가 지갑을 뒤지기 시작한다. 워낙 든 게 없는 지갑이라 ‘그것’을 찾는 데에는 얼마 걸리지 않았다.

“헐.”

손에 들린 카드 한 장. 이틀 전 협회에서 발급받은 C급 헌터 자격증이다.

“위조된 거 아냐?”

“맞을래?”

“진짠가 보네.”

“그거 위조하면 중범죄야, 인마.”

“저 돈은? 오빠 말대로 그, 최 팀장인가 뭔가 하는 그 사람이 준 거야?”

“몇 번 말해야 믿을래.”

“350번 정도?”

말과는 달리 이제는 믿는 눈치다. 은색으로 반짝이는 C급 헌터 자격증, 차곡차곡 쌓은 3억 원의 돈다발.

전부 이 낡고 좁은 거실과는 동 떨어진 물건들이다.

멍한 눈으로 앉아 있던 엄마가 신음처럼 중얼거렸다.

“이게 다 무슨 일이라니…….”

하연이도 세상 다 산 노인네처럼 허허 웃는다.

“그러게. 살다 보니 별일이 다 있네.”

“너 아직 스무 살도 안 됐거든.”

“말이 그렇다는 거지. 근데 엄마.”

“으, 응?”

“탄내 나.”

“맞다, 찌개!”

반쯤 풀려 있던 엄마의 눈이 번쩍 뜨인다. 급한 대로 내가 몸을 일으켰지만, 부엌은 이미 초토화가 되어 있었다.

뒤이어 따라온 엄마가 발을 동동 굴렀다.

“아이고, 이걸 어째!”

잔뜩 졸아 버린 국물에 숯덩이가 된 생선. 오랜만에 집밥을 먹을 수 있을 것 같아 기대했는데…….

뭐, 이런 전개도 나쁘지 않지.

“오랜만에 외식이나 하러 가요.”

평소 같았으면 식당 가격의 부조리를 일장연설 했을 엄마도, 치킨이나 시켜 달라고 했을 하연이도 이번만큼은 조용했다.

“동생아.”

“네, 오라버니.”

“돈 챙겨라.”

“옛썰.”

하연이가 기다렸다는 듯이 돈다발을 쓸어 담았다.



* * *



“손님. 죄송하지만 저희 레스토랑은 복장 규정이…….”

코스 요리 먹는 데 1인당 수십만 원을 지불해야 한다는 고급 레스토랑의 지배인이 난처한 웃음을 지었다.

“복장 규정이요?”

“네. 보시면 아시겠지만 다른 손님들도 마찬가지거든요.”

진짜네. 남자고 여자고 할 것 없이 죄다 정장에 원피스, 심지어는 드레스도 있다.

‘시바, 누가 보면 무도회장에 춤추러 온 줄 알겠네.’

여기가 무슨 18세기 프랑스야?

국밥집만 드나들었던 내게는 엄청난 문화 충격이다.

“그냥 다른 데 가자.”

“그래, 하연이가 이 근처 맛집 많이 알더라.”

나보다도 식구들이 더 무안해하는 것 같아 그냥 나왔다.

레스토랑 유리에 우리 셋의 모습이 비친다. 오랜만의 외식이라고 신경 써서 입었을 게 분명한데, 가진 옷이라고는 죄다 시장 메이커에 오래 입은 티가 난다.

‘돈이 부족했나?’

나 먹는 거, 입는 거 아껴 가며 번 돈의 대부분을 집에 보냈다.

F급 헌터였을 때도 남들보다 배로 일하니 결코 적은 돈은 아니었을 텐데.

“아들, 삼겹살 먹으러 갈까? 아침부터 기름진 음식은 좀 그런가?”

“삼겹살 좋지. 엄마가 뭘 좀 아네. 친구가 저 앞 사거리 고기집 갔는데 엄청 맛있었대.”

겨우 삼겹살.

지갑에는 C급 헌터 자격증이 있고 가방에는 돈다발이 가득하다. 그걸 모를 리 없는데, 걱정 없이 사치 부려도 되는데.

‘내가 일하는 이유가 그건데.’

누가 그랬다.

행복은 돈으로 살 수가 없다고. 행복에는 가격표가 없다고.

개인적으로 그런 소리 하는 놈들한테 한마디만 하고 싶다.

‘좆 까.’

없어서 못 쓰는 게 돈이다. 그리고 이 돈을 어떻게 써야 할지 어젯밤 내내 고민한 끝에 마침내 결심했다.

적어도 오늘 하루만큼은 가족을 위해 아낌없이 쓰기로.

지금, 그 결심이 훨씬 크기를 부풀렸다.

“우리 밥 좀 늦게 먹자.”

대답을 기다리지 않고 지나가는 택시를 붙잡았다.

“어디로 모실까요?”

“미래 백화점이요.”

근방에서 가장 크고 비싸다는 백화점이다. 룸미러 속 엄마가 눈을 동그랗게 떴다.

“백화점?”

반면 하연이의 입꼬리는 음흉하게 솟구쳤다.

“좋네. 돈 많은 오빠가 옷도 사 주고.”

역시 눈치 빠른 녀석. 척하면 착이다. 나는 피식 웃었다.

“사고 싶은 거 다 사.”

“진짜?”

“엄마 것부터 골라 주고.”

“오케이.”

“효자 아드님 두셨네. 허허.”

기사의 너스레에 비로소 엄마가 웃었다.



* * *



“진짜 다 산다?”

“다 사.”

최종 확인이 끝나자 하연이는 고삐 풀린 망아지처럼 백화점을 누볐다. 옷을 스캔하는 눈썰미도 매섭고 동작은 또 어찌나 빠른지 각성자가 아닌지 의심될 정도다.

처음에는 옷보단 가격표를 보던 엄마도 어느 순간부터 적극적으로 움직이기 시작했다.

“엄마, 이거 어때?”

“너무 짧지 않니?”

“이거!”

“괜찮네.”

“이것도!”

“예쁘네. 저기 언니, 이 옷 한 사이즈 더 큰 거 없어요?”

그렇게 두 시간이 지나고…… 나는 신체의 변화를 느꼈다.

‘죽겠다.’

이유를 알 수 없는 극심한 호흡 곤란과 다리 통증.

무림에서 조필을 상대했을 때와 비슷한 수준의 무력감이 온몸을 감싼다.

“오빠, 나 어때?”

“못생겼어. 저리 꺼져.”

“아들, 이거 입어 봐.”

“안 입어 봐도 될 것 같아요. 그걸로 살게요.”

그날 우리가 몇 벌의 옷을 샀고, 얼마를 썼는지는 모르겠다.

다만 쇼핑을 모두 끝내고 돌아갈 때쯤에는 백화점 높은 분이 우리를 배웅했으며.

“어서 오십시오.”

복장 규정이 철저하다던 레스토랑의 지배인은 우리를 알아보지도 못했다.

“우와, 나 이런 거 처음 먹어 봐.”

“그러게. 어쩜 요리를 이렇게 예쁘게 하지?”

소곤거리는 엄마와 하연이의 뺨이 불그스름하다.

수십만 원짜리 코스 요리를 먹으려고 그 수십 배쯤 되는 돈을 썼지만 하나도 아깝지 않은 날이었다.

“근데 밥 먹고 싶다. 느끼해.”

“여기 왜 이렇게 양이 적니?”

……아깝지 않은 척했다.
```

### Current accepted English

```markdown
# Chapter 52

Six in the morning.

Taxi driver Mr. Kim picked up his first fare of the day.

And regretted it ten minutes later.

*I’ve been jinxed.*

The young man looked perfectly normal at first glance. Sturdy, muscular build, clean-cut face—even being generous, he only looked mid-to-late twenties.

But then…

“Sniff, sniff.”

Something was off. Very off.

“Huuugh.”

He was hugging a drink box like treasure, cracking it open every thirty seconds to smell it, then shuddering like he was possessed.

*What in the world is he doing?*

A chill crawled up the back of Mr. Kim’s neck. He had been driving a taxi for more than ten years, but he had never had a problem customer quite like this.

He kept stealing glances at the young man in the passenger seat, and in that moment—

“Mister.”

“Yes, yes?!”

He nearly had a heart attack.

The young man’s eyes, hollow only a moment ago, were gleaming like a beast’s.

“There’s a truck behind us.”

“A-a truck? A blue one?”

“Yes. Doesn’t it look like it’s been following us since that intersection?”

“Huh? Well, I suppose it does.”

“It might be tailing us.”

What fresh bullshit was this?

Mr. Kim’s eyes darted around, and in the end he gave the answer the young man seemed to want.

“I-I’ll peel off to the side.”

The young man hugged the drink box tight until the blue truck disappeared from view. As if someone might snatch it away.

“Sniff. Sniff.”

Of course, he didn’t skip smelling it whenever he got the chance.

*This guy’s completely insane.*

The AC was blasting inside the car, but Mr. Kim’s back was soaked with cold sweat.

And this was the first fare of the day.

A thoroughly jinxed day.

* * *

Vroom.

The moment I handed over the fare and shut the door, the taxi shot off like a bullet.

Anyone watching would’ve thought a monster was chasing it. What if he got in an accident?

I clicked my tongue and headed into the apartment complex.

I still had yesterday’s drink box hugged carefully to my chest.

*Three hundred million won.*

About as much as I’d saved over three full years as an F-rank Hunter. Of course, I didn’t have a single won of that left now.

*I spent it all paying off debts.*

There had been a time when I was drowning in debt, but I’d gritted my teeth and kept at it until things gradually got better. I’d even moved my family to a safe-zone apartment near Ilsan.

Lately, though, my life had been like a roller coaster.

A roller coaster that dropped whenever the System disappeared…

No. I was coming home for the first time in months. I should drop thoughts like that.

*Which building and unit was it again?*

I only came here once every couple of months, so it was always like this.

I glared at the apartment buildings packed in tight, then pulled out my phone and called. The ringtone went on for a long time before the line finally connected.

Click.

“Hello?”

I’d figured Hayeon would still be asleep this early, but her voice was clear.

“You were already up?”

“I have to be. Do you know what time it is?”

“It’s not even seven.”

“I study better when I get up early.”

My little sister never failed to impress me. Jinho hyung, who treated getting up in the morning like one of the seven deadly sins, should’ve heard that.

“Why’d you call?”

“I’m out front.”

“Huh? Out front?”

“Yeah. But I forgot which place is ours.”

“……Again? You really do the damnedest things. Wait there.”

I stood there holding the dead phone. After a few minutes, a girl appeared at the entrance of one of the buildings, dragging her slippers.

Even from a distance, she radiated total bum energy. That face said the whole world was too much trouble, and I couldn’t help smiling.

“Jin Hayeon!”

“Don’t yell. You’ll wake people up.”

……Yeah. That was my little sister.

“What brings you here? You didn’t even tell us you were coming.”

“Do I have to announce it every time I come to my own house?”

“You come so rarely. The residents’ association president probably visits more than you do.”

“That bad?”

“That bad.”

The elevator stopped. Hayeon punched in the password at the front door and turned the handle.

And there—

“Son!”

Someone stood there beaming.

Wrinkled hands. A perm half fallen out. She looked as happy as a kid getting a surprise gift.

My throat tightened. I scratched my chin, then burst out laughing.

“I’m home, Mom.”

I had finally come back.

To the place where my family was waiting.

Home.

* * *

Sizzle, sizzle.

Mom was busy with breakfast in the kitchen. A good smell hung in the air.

“Mrs. Kim is really excited now that her son’s home after so long.”

Hayeon scratched her stomach and plopped down beside me.

The old sofa sagged.

What a pig.

“Is she making a lot?”

“Yeah. A whole feast. Looks like we’re eating well today.”

She answered, but her eyes stayed glued to her phone.

“You haven’t seen your brother in ages. Aren’t you happy to see me?”

“Huh?”

“I mean, you could at least massage my shoulders after all the work I did.”

Hayeon let out a long sigh.

“What’s gotten into you, Mr. Taekyung? We’re not that kind of siblings.”

“……Listen to that attitude.”

It wasn’t like we’d only started bickering yesterday, but I still felt a pang.

I mean, I’d barely made it back after brushing past death!

“That got to you just now, didn’t it?”

Her radar was scary.

“Go get ready for school, you little cafeteria parasite.”

“Mm. Today’s the school founding anniversary.”

My fist trembled.

I wanted to smack the back of that irritating head right then and there, but doing it would mean I’d really lost.

“You want to hit me, don’t you? Your fist is shaking.”

“You’re lucky you’re a girl. If you had balls, I would’ve—”

“Mom! My brother’s sexually harassing me!”

“Hey, hey!”

“He said my b—mmph!”

I clamped a hand over Hayeon’s mouth. She thrashed, hitting and pinching, but she was still just a nineteen-year-old girl. It didn’t hurt.

Then, by pure coincidence, the foot she flung out slammed into the drink box I’d set so carefully in the corner of the sofa.

Thump.

Flutter.

The box flew wide open.

Yellow bundles of bills spilled across the living-room floor.

Hayeon froze.

“Come on, stop fighting and eat your breakf—”

Mom had come out of the kitchen too.

Everything in the living room stopped as if someone had hit pause. Only the quiet sound of stew simmering filled the space.

Sizzle, sizzle.

I smiled awkwardly and opened my mouth.

“Can’t we talk about this after breakfast?”

“……Son?”

“Mmph, mmph, mmph.”

Breakfast was probably going to be delayed for quite a while.

* * *

I told my family a suitably edited version of everything that had happened so far.

My reawakening as a C-rank Hunter, and where the money had come from.

“So that’s how it happened.”

Their reactions split in two.

“I see.”

Mom nodded blankly.

And then—

“Proof.”

“……”

Yeah. I hadn’t expected anything else from you.

I sighed and tossed her my wallet.

“What’s this?”

“Check it.”

Hayeon looked at me with suspicion, then started digging through the wallet. There was barely anything in it, so it didn’t take her long to find *it*.

“Whoa.”

A single card in her hand.

The C-rank Hunter license the Association had issued me two days ago.

“This isn’t fake, is it?”

“Want to get hit?”

“Guess it’s real.”

“Forging one is a serious crime, you idiot.”

“What about that money? Did that Team Leader Choi or whoever really give it to you, like you said?”

“How many times do I have to tell you before you believe me?”

“About three hundred and fifty?”

Despite her words, she seemed to believe me now.

The C-rank Hunter license gleaming silver. Neatly stacked bundles of three hundred million won.

Every bit of it looked completely out of place in this old, cramped living room.

Mom sat there staring blankly and muttered, almost a groan.

“What on earth is all this……?”

Hayeon let out a hollow laugh like an old woman who had seen everything life had to offer.

“I know. You live long enough, you see it all.”

“You’re not even twenty yet.”

“It’s just an expression. But, Mom.”

“Y-Yes?”

“I smell burning.”

“Oh, right! The stew!”

Mom’s half-lidded eyes flew open. I got up in a hurry, but the kitchen was already a wreck.

Mom followed me in, stomping her feet.

“Oh no, what do we do!”

The broth had boiled down to almost nothing, and the fish had turned to lumps of charcoal. I’d been looking forward to a home-cooked meal after so long, but……

Well, this kind of development wasn’t so bad either.

“Let’s go eat out. It’s been a while.”

On any other day, Mom would’ve launched into a whole speech about how ridiculous restaurant prices were, and Hayeon would’ve asked us to order chicken. This time, both of them stayed quiet.

“Little sister.”

“Yes, dear brother.”

“Grab the money.”

“Yessir.”

Hayeon swept up the bundles like she’d been waiting for the order.

* * *

“I’m sorry, but our restaurant has a dress code…….”

The manager of the upscale restaurant—where a course meal ran to several hundred thousand won a person—gave us an awkward smile.

“A dress code?”

“Yes. As you can see, the other guests are the same.”

He was right. Men and women alike, all in suits and dresses. Some were even in evening gowns.

*Shit. Anyone watching would think they’d come here to dance at a ball.*

What was this, eighteenth-century France?

For someone like me, who’d only ever gone to gukbap[^1] places, it was a massive culture shock.

“Let’s just go somewhere else.”

“Yeah. Hayeon knows a lot of good restaurants around here.”

The family looked even more embarrassed than I did, so I just walked out.

The three of us were reflected in the restaurant glass. We’d clearly dressed up for our first meal out in a long time, but every piece we owned was cheap market-brand stuff that already looked well-worn.

*Had they been that short on money?*

I’d sent most of what I earned home, cutting back on food and clothes for myself.

Even as an F-rank Hunter, I’d worked twice as hard as other people. It shouldn’t have been a small amount.

“Son, should we go get pork belly? Maybe greasy food is a bit much this early in the morning.”

“Pork belly’s good. Mom knows what’s what. A friend went to the meat place at the intersection up ahead and said it was amazing.”

Just pork belly.

I had a C-rank Hunter license in my wallet and a bag stuffed with cash. It wasn’t like they didn’t know that. They could splurge without worrying.

*That’s why I work.*

Someone once said you can’t buy happiness with money. That happiness doesn’t have a price tag.

Personally, I had one thing to say to people who talked like that.

*Fuck off.*

Money’s what you can’t spend because you don’t have it.

And after thinking all night about how to use this money, I’d finally made up my mind.

At least for today, I would spend it freely on my family.

Right now, that decision had swollen even bigger.

“Let’s eat a little later.”

Without waiting for an answer, I flagged down a passing taxi.

“Where can I take you?”

“Mirae Department Store.”

It was supposed to be the biggest, most expensive department store in the area. In the rearview mirror, Mom’s eyes went round.

“The department store?”

Meanwhile, the corners of Hayeon’s mouth curled up slyly.

“Nice. My rich oppa can buy me clothes too.”

Sharp as ever. I only had to say the word and she got it.

I snorted.

“Buy whatever you want.”

“Really?”

“Pick out Mom’s things first.”

“Okay.”

“You’ve got yourself a devoted son, ma’am. Ha ha.”

Only then did Mom smile at the driver’s banter.

* * *

“You’re really buying everything?”

“Everything.”

Once I confirmed it for the last time, Hayeon tore through the department store like a colt off its reins. The way she scanned clothes was viciously sharp, and she moved so fast I started to wonder if she was an Awakened.

At first, Mom looked at the price tags more than the clothes. Before long, she started moving with enthusiasm too.

“Mom, what do you think of this?”

“Isn’t it too short?”

“This one!”

“That’s nice.”

“This too!”

“That’s pretty. Excuse me, miss—do you have this in one size larger?”

Two hours passed, and I felt a change in my body.

*I’m dying.*

Crushing shortness of breath and pain in my legs, for no reason I could name.

Helplessness wrapped around my whole body at about the same level as when I’d faced Jopil in Murim.

“Oppa, how do I look?”

“You’re ugly. Get lost.”

“Son, try this on.”

“I don’t think I need to try it. I’ll take that.”

I don’t know how many clothes we bought that day, or how much we spent.

All I know is, by the time we finished shopping and headed out, someone high up at the department store had come to see us off.

“Welcome.”

The manager of the restaurant that had been so strict about its dress code didn’t even recognize us.

“Wow, I’ve never eaten anything like this before.”

“I know. How do they make the food look this pretty?”

Mom and Hayeon spoke in hushed voices, their cheeks flushed.

We’d spent dozens of times more than the several-hundred-thousand-won course meal just to eat it, but it was a day when not a single won felt wasted.

“But I want rice. This is too rich.”

“Why are the portions so small?”

……I pretended it didn’t.

[^1]: A cheap Korean rice-and-soup meal, typically eaten at modest diners.
```
## Chapter 53

### Korean source

```text
＃53화



띠링.



- 수면 모드가 종료되었습니다.



“……빠, 오빠!”

헉, 헛숨과 함께 눈을 떴다.

제일 먼저 눈에 들어온 건 고시원 천장이 아니라 하연이의 얼굴이었다.

아, 맞다. 어제 집에 왔었지.

“악몽이라도 꿨어?”

“응?”

“아까부터 소리 지르던데. 땀도 엄청 흘리고.”

내가?

되묻기도 전에 깨달았다. 전신이 땀에 흠뻑 젖어 있었고 모래라도 삼킨 것처럼 목이 따끔거렸다.

‘몸 상태가 왜 이래?’

내가 가진 시스템은 깨어 있을 때만 적용되는 것이 아니다. 수면 모드는 숙면을 취하게 해 줌과 동시에 컨디션 최고로 끌어 올리는 효과가 있었다.

지금 같은 상황은 무림에서도, 동기화가 된 이후에도 없었던 일이다. 게다가 악몽이라니.

‘무슨 꿈을 꾼 거지?’

하지만 머리만 지끈거릴 뿐, 꿈 내용은 기억나지 않았다.

그런 내게 하연이가 걱정스러운 목소리로 물었다.

“요즘 안 좋은 일이라도 있어?”

“없어, 그런 거.”

“있으면 말해. 혼자 끙끙 앓지 말고.”

“네, 누나.”

“장난 아니거든.”

조그만 주먹이 가슴을 퍽 친다. 하연이의 진지한 표정에 할 말이 없어진 나는 턱만 긁적였다.

“진짜 없어? 고민이나, 힘든 일.”

“없다니까.”

거짓말이다. 7년 전에도 있었고 7년 후에도 있을 것이다. 혼자 방에 틀어박혀 운 날도, 진호 형과 진탕 술을 퍼마시며 잊은 날도 있었다.

‘그걸로 충분해.’

어린 두 남매 키우느라 무릎 연골이 닳도록 일한 어머니, 이제 수능을 준비 중인 고3 여동생에게는 말할 수 없는 일들이 있다.

혼자 버티고 극복하는 것. 이제는 익숙해졌다.

나는 아무렇지 않은 척 씩 웃어 보였다.

“이제 인생 펼 일만 남았는데 무슨 고민이 있겠냐? 아, 하나 있긴 하네. 앞으로 돈 어떻게 써야 하나, 뭐 그런 거?”

“허세는.”

분위기가 살짝 가벼워졌다. 나는 짐짓 얼굴을 구겼다.

“허세? 어제 기억 안 나냐? 돈다발 다시 보여 줘?”

“그건 인정. 재수는 없는데 할 말이 없네.”

“지금 내 27년 인생 그래프 꼭대기 찍었다. 별일 없으니까 너는 공부나 열심히 해.”

“내 성적 전국 0.1%거든? 충분히 잘하고 있으니까 걱정 마셔.”

입을 삐죽 내민 하연이가 방을 나가려다 말고 멈칫, 다시 돌아선다.

“오빠, 그런데.”

“응?”

“진위경이 누구야?”

“……뭐?”

생각지도 못한 타이밍에 등장한 한 사람의 이름.

몸이 뻣뻣하게 굳었다.



* * *



아삭.

갓 담근 총각김치를 한 입 베어 물었다. 그토록 먹고 싶었던 엄마 음식이었지만 맛이 거의 느껴지지 않았다.

방금 전, 하연이와 나눴던 대화 때문이다.



‘너, 그 이름 어디서 들었어?’

‘오빠한테. 아까 자면서 계속 그 이름을 부르더라고.’



그리고 마지막 한마디.



‘아는 사람이야? 꿈에도 나올 정도면 친한가 보네.’



그 질문에는 대답하지 못했다. 무림에서도, 현실에서도 그 답을 찾지 못했기 때문이다. 아니, 더 이상 찾을 이유도 없었다. 나는 현실로 돌아왔고, 진위경은 무림에 있으니까.

‘그런데 왜 갑자기 진위경이 꿈에…….’

머리가 복잡했다. 무림에서의 후유증 때문일까? PTSD. 외상 후 스트레스성 장애라는 단어도 떠올랐다.

‘미치겠네.’

나도 모르게 표정이 굳은 모양이다. 엄마가 넌지시 물었다.

“입맛이 없니? 너 좋아하는 걸로 차렸는데.”

“아, 아니에요. 김치는 언제 담그셨어요? 된장찌개도 아주 제대로네.”

황급히 변명하며 수저를 들었다. 오랜만에 세 식구가 한 식탁에 모였다. 이 소중한 순간을 망칠 수는 없다.

‘별일 아니겠지. 별일 아닐 거야.’

후루룩.

그럼에도 불구하고 구수한 된장찌개에서는 약간의 쓴맛이 느껴졌다.



* * *



찜찜했던 마음 한구석은 금방 평소대로 돌아왔다.

가족들과 하루 종일 웃고, 떠들고. 낮잠까지 푹 자고 나니 저녁이었다. 이제는 돌아가야 할 때다.

“며칠 더 있다 가지. 내일 수육 하려고 했는데.”

“우리 김 여사님 또 시작이네. 나도 수육 먹을 줄 알거든?”

미련이 뚝뚝 떨어지는 엄마의 말에 하연이가 구시렁거렸다.

“반찬도 잔뜩 챙겨 보내는데 뭐가 그렇게 걱정이야? 저 정도면 반찬 가게를 열어도 되겠구만.”

“……그건 그래.”

현관문 앞, 엄마가 준비해 둔 쇼핑백들 안에는 반찬이 한가득했다. 이것도 겨우 설득한 끝에 얻어 낸 협의점이다.

‘넣을 곳도 없는데.’

3평짜리 고시원 방에 냉장고까지 들여놓으면 정말 발 디딜 곳이 없을 것이다. 아니, 들여놓을 자리도 없다.

이미 냉장고만 한 캡슐이 있으니까.

‘슬슬 이사라도 가야 하나.’

그런 생각을 하며 어젯밤 미리 싸 놨던 배낭을 어깨에 멘 순간이었다.

“……?”

뭐가 이렇게 묵직해? 넣은 거라곤 기껏해야 어제 샀던 옷 몇 벌이 전부인데.

의아함에 배낭을 내려놓자 다급해진 건 가족들이었다.

“아들, 내일부터 바쁘지? 빨리 가서 씻고 푹 자.”

“……아까는 며칠 더 있다가 가라면서요?”

“오빠, 차 시간 늦겠다.”

“택시 타고 갈 건데?”

“야간 할증. 야간 할증 붙잖아.”

이쯤에서 대충 감을 잡았다.

“언제 넣었어?”

“뭐, 뭘?”

“돈.”

표정이 곧 대답이다. 나는 한숨을 내쉬었다.

“말했잖아요. 두고 필요할 때 쓰시라니까.”

“…….”

“저 돈 많이 벌어요. 앞으로도 그럴 거고요.”

사실과 거짓을 반반 섞었다.

C급 헌터 평균 연봉이 5억이다. 최 팀장이라는 후한 고용주를 만나 상상치도 못한 거액을 보너스로 받았지만, 시스템이 사라진다면 모든 게 물거품으로 사라질 거다.

그래서 더 가족에게 주고 싶었던 건데…….

“네가 목숨 걸고 벌어 온 돈이잖아. 너 위해서 써. 응?

“엄마.”

“아들.”

다음 순간, 조용히 흘러나온 엄마의 한마디에 나는 말문이 턱 막혔다.

“무리하지 마. 다치지도 말고. 엄마는 그거면 돼.”

더 이상 무슨 말을 해야 할까.

잠시 후, 나는 여름밤의 습한 공기 속으로 발을 내딛었다.

반찬이 든 쇼핑백과 돈다발이 가득한 배낭을 메고서.

부우웅.

택시를 타고 고시원으로 돌아가는 길 내내 엄마의 마지막 말과 그 온기를 떠올렸다.



‘살아남아라, 뒤도 돌아보지 말고 도망치란 말이다. 그게 네 임무다.’



점점 흐릿해지는 기억 속 누군가의 목소리도.



* * *



촤아악-

핏물이 솟구쳤다. 몬스터의 녹색 피가 아닌, 인간의 붉은 피다. 타는 듯한 허벅지의 통증을 느끼며 리자드맨 족장의 가슴에 창을 쑤셔 박았다.

“키이…….”

띠링.



- [Lv.50 리자드맨 족장]을 처치했습니다!

- 경험치를 획득했습니다!



게이트 클리어. 숨이 끊긴 리자드맨 족장의 시체 위에 밖으로 통하는 마력장이 생성됐다.

최 팀장이 나무에서 등을 뗀 것도 그때였다.

“세 번.”

“예?”

“진태경 씨가 오늘 다친 횟수입니다.”

단단하고 길쭉한 손가락이 내 몸 곳곳을 가리켰다.

이미 포션으로 치료된 목덜미와 팔, 그리고 아직도 피가 흘러나오고 있는 허벅지.

“괜찮아요. 스친 정도라 하급 포션으로도 충분히…….”

“안 괜찮습니다.”

단호한 어조로 말을 잘라 낸다. 평소에도 속을 알 수 없는 표정의 최 팀장이지만 이번만큼은 뭔가 달랐다.

확실한 건 저 표정에서 묻어 나오는 감정이 단순한 걱정이 아니라는 거다.

“지난주에는 한 번도 부상을 입지 않았습니다. 같은 게이트, 같은 몬스터를 상대하는데 이렇다면 이유는 하나죠.”

그의 투명한 눈이 나를 향했다.

“진태경 씨. 무슨 문제라도 있습니까?”



* * *



하루, 이틀, 사흘.

시간이 지났지만 상황은 나아지지 않았다. 결국 나흘째 되는 날엔 다섯 군데에 부상을 입고 말았다.



‘지금 상태로는 안 됩니다. 퇴근하세요.’



최 팀장의 말을 뒤로하고 고시원으로 향하는 길, 머릿속이 복잡했다.

‘뭐가 문제지?’

모든 게 잘 풀리고 있었다. 시스템은 사라지지 않았고, 내 계좌에는 은행에 맡긴 3억 상당의 돈이 예치되어 있다. 이제는 C급 헌터로서 승승장구할 일만 남았는데…….

‘빌어먹을 꿈.’

그때부터였다. 본가에서 보낸 첫날 밤 이후부터 나는 악몽을 꾸기 시작했다.

악몽 속 장면은 점점 또렷해졌고 꿈이 끝나면 땀에 흠뻑 젖어 깨어났다. 운기조식으로 몸 상태를 끌어 올려 놔도 정신이 불안정하니 실수만 늘었다.

‘이대로라면 곤란한데.’

몸은 현실에 있지만 정신은 아직도 무림에 붙잡혀 있는 상황. 정신과라도 가 봐야 하나 고민하며 고시원 방에 도착했다.

달칵.

“어, 왔어?”

인사가 너무 자연스러워서 잘못 들어왔나 헷갈릴 정도다.

나는 기가 막힌 얼굴로 물었다.

“뭐 하냐?”

진호 형이 대답했다.

“분해 및 조립.”

드라이버를 들고 캡슐 앞에 앉아 있는 모습에 순간 눈앞이 노래진다. 이 인간이 지금 설마…….

“미쳤어? 비켜!”

“야, 야. 한국말은 끝까지 들어야지.”

진호 형이 황급히 손을 내저었다.

“아직 시작도 안 했어.”

“뭐?”

“나도 막 들어왔다고. 진짜야.”

표정을 보니 거짓말하는 것 같지는 않다. 멀쩡한 캡슐을 확인하고 나서야 안도의 한숨이 흘러나왔다.

“후우.”

내 반응에 진호 형이 당황한 얼굴로 물었다.

“작동도 안 되는 고물 캡슐 하나에 왜 이렇게 난리야? 짐짝처럼 내다 버릴 때는 언제고.”

“그때는 그때고.”

동기화에 관한 일을 진호 형이 알 리 없다. 그에게는 고물 캡슐로 보이는 저 정체불명의 물건이 내게 어떤 의미를 갖는지도.

“아무튼 절대 건드리지 마. 알았어?”

“아주 때려죽일 기세네.”

“찢어 죽일 거야.”

“…….”

황당한 얼굴의 진호 형을 무시하고 침대에 풀썩 드러누웠다.

잠깐의 해프닝에 몸 안의 기운이 쭉 빠져나간 기분이다.

“무슨 일 있냐?”

“일은 무슨.”

“요즘 너 때문에 민원 장난 아냐. 오늘도 옆방 아저씨가 난리 치는 거 겨우 달래서 보냈다.”

뭐 때문인지는 짐작이 간다.

진호 형이 바닥에 늘어놓은 공구를 주섬주섬 챙기며 말을 이었다.

“밤새 끙끙거리니까 미칠 것 같대. 아, 그리고 진위경이 누구냐는데?”

또 나왔다. 저 이름.

나는 베개에 얼굴을 파묻었다.

“그냥 여자 친구라고 해.”

순간, 멍키 스패너를 쥔 그의 손이 부르르 떨리는 게 보였다.

“여자 친구 생겼냐? 이런 배신자 새끼.”

“…….”

“예뻐? 몇 살? 사진 보여 주라.”

저 인간이 서른이라니. 통탄을 금치 못하겠다.

“근데 이름이 좀 이국적이네. 조선족이셔? 아니면 중국인?”

“……중국인.”

틀린 말은 아니지, 뭐.

“이 새끼 C급 헌터 됐다고 벌써 글로벌하게 노네. 아무튼 여자 소개 좀. 나 중국 좋아해. 니하오마. 워아이니. 또 뭐 있더라.”

“니씨팔롬아.”

“병신. 성조랑 발음 다 틀렸다. 그래서 100일이나 채우겠냐? 따라 해 봐. 니 취팔러마.”

“니씨팔롬아.”

“다시. 니 취팔러마.”

“니씨팔롬아.”

“……아니 이 새끼가?”

새삼스러운 깨달음에 분노하는 진호 형을 무시하고, 나는 문을 가리켰다.

“나가.”

제발 혼자만의 시간 좀 갖자.



* * *



조용해진 방, 침대에서 몸을 일으킨 나는 캡슐로 다가가 낡고 때에 찌든 캡슐 표면을 톡톡 두드리며 중얼거렸다.

“너, 뭐 하는 놈이야?”

당연하게도 대답은 돌아오지 않았다.

내심 기대했는데, 아쉽다.

‘시스템도 현실에 동기화된 마당인데 기계가 말할 수도 있지 뭘.’

사실 진짜 기계인지도 의문이다. 아무리 현실이 판타지가 된 지 오래라지만 이건 새로운 장르 아닌가.

만약 지금 내 상황을 소설로 쓴다면 장르를 어떻게 정해야 할까. 판타지? 게임 소설? 그것도 아니면.

‘차원 이동?’

푸흐흐. 바람 빠지는 소리가 흘러나왔다. 차원 이동이라니, 내가 점점 미쳐 가는구나. 그런 게 가능할 리가 없다.

가능할 리가…….

얼음물을 뒤집어쓴 것처럼 정신이 번쩍 들었다.

‘……가능하잖아.’

차원 이동은 과거에도 있었고, 현재에도 남아 있다.

마왕 아스모데우스의 침공, 그리고 게이트가 그 증거다.

우리는 게이트를 통해 현실을 오고 갈 뿐이지만, 수십 년 전 몬스터 군단은 거길 통해 또 다른 차원에서 지구로 넘어왔다.

‘마계(魔界).’

악의 땅. 몬스터들의 고향. 마왕의 영지.

인간 중 그 누구도 발을 디디지 못한, 엿볼 수도 없는 미지의 차원. 인류는 그렇게 정의 내렸다.

그런데 만약 눈앞의 이 캡슐이 또 다른 차원으로 향하는 일종의 게이트라면, 무림이 알려지지 않은 또 다른 차원이라면…….

‘무림은 또 하나의 현실이다.’

그곳에서 보고 겪은 모든 것들이.

물, 흙, 바람. 그리고 사람까지도.

‘NPC가 아니었어.’

나는 빛바랜 캡슐 표면 위에 비친 얼빠진 내 얼굴을 바라봤다.

그 후로도 한참 동안.
```

### Current accepted English

```markdown
# Chapter 53

Ding.

> **System**
>
> - Sleep Mode has ended.

“…O-oppa!”

I gasped and opened my eyes.

The first thing I saw wasn’t the ceiling of my goshiwon[^1] but Hayeon’s face.

*Oh, right. I came home yesterday.*

“Did you have a nightmare?”

“Huh?”

“You’d been screaming. And you were sweating like crazy.”

*I was?*

Before I could even ask, I understood. My whole body was soaked in sweat, and my throat stung as if I’d swallowed sand.

*Why do I feel like this?*

The System I had didn’t only work while I was awake. Sleep Mode let me sleep deeply and pulled my condition up to its peak at the same time.

Nothing like this had happened in Murim, or after Synchronization. And a nightmare, on top of that?

*What did I even dream?*

My head just throbbed. I couldn’t remember the dream at all.

Hayeon asked, worried,

“Has something bad happened lately?”

“No. Nothing like that.”

“If there is, tell me. Don’t suffer by yourself.”

“Yes, nuna.”

“I’m not joking.”

Her little fist thumped my chest. Hayeon’s serious face left me with nothing to say. I scratched my chin.

“Really? No worries? Nothing hard going on?”

“I told you, there’s nothing.”

It was a lie. There had been things seven years ago, and there would be things seven years from now. There’d been days I locked myself in my room and cried, and days I drank myself senseless with Jinho hyung just to forget.

*That’s enough.*

There were things I couldn’t tell my mother, who’d worked until the cartilage in her knees wore down raising two young kids, or my little sister, a high-school senior now preparing for her college entrance exam.

Enduring and getting through things alone. I was used to it by now.

I flashed a grin, like nothing was wrong.

“My life’s finally about to take off. What would I have to worry about? Ah, there is one thing. How I’m supposed to spend all this money. Something like that.”

“Show-off.”

The mood lightened a little. I made a face on purpose.

“Show-off? Don’t you remember yesterday? Want me to show you the bundles of cash again?”

“I’ll give you that. You’re obnoxious, but I can’t argue.”

“I’ve hit the peak of my twenty-seven-year life graph. Nothing’s going on, so you just study hard.”

“My grades are in the top 0.1 percent nationwide, okay? I’m doing more than well enough, so don’t worry.”

Hayeon pouted and started to leave, then stopped and turned back.

“Oppa. But…”

“Yeah?”

“Who’s Jin Wikyung?”

“…What?”

A name I never expected, at a moment like that.

My body went rigid.

* * *

Crunch.

I bit into a piece of freshly made young-radish kimchi. It was Mom’s cooking, the food I’d wanted so badly, but I could barely taste it.

Because of the conversation I’d just had with Hayeon.

“Where did you hear that name?”

“From you. You kept calling it in your sleep.”

And then her last question.

“Someone you know? If they show up in your dreams, you must be close.”

I couldn’t answer. I hadn’t found that answer in Murim or in reality.

No. I no longer had any reason to look for it. I had come back to reality, and Jin Wikyung was in Murim.

*Then why did Jin Wikyung suddenly show up in my dream…?*

My head was a mess. An aftereffect of Murim? The word PTSD surfaced—post-traumatic stress disorder.

*This is driving me crazy.*

I must have looked grim without realizing it. Mom asked carefully,

“Have you lost your appetite? I made all your favorites.”

“Oh, no. When did you make the kimchi? And this doenjang-jjigae is perfect.”

I scrambled for an excuse and picked up my spoon. For the first time in ages, the three of us were together at one table. I couldn’t ruin this.

*It’s nothing. It has to be nothing.*

Slurp.

Even so, the savory doenjang-jjigae tasted faintly bitter.

* * *

That uneasy corner of my mind soon went back to normal.

I laughed and talked with my family all day. I even took a long nap, and then it was evening.

Time to go back.

“Stay a few more days. I was going to make boiled pork tomorrow.”

“Our Mrs. Kim is starting again. I know how to eat boiled pork too, you know?”

Hayeon grumbled at the reluctance dripping from Mom’s words.

“She packed you a ton of side dishes already, so why are you so worried? At this rate she could open a side-dish shop.”

“…That’s true.”

The shopping bags Mom had ready by the front door were packed with side dishes. This, too, was the compromise I’d only gotten after talking her down.

*There’s nowhere to put them.*

If I put a fridge in my three-pyeong goshiwon room, there really wouldn’t be anywhere to stand. No—there wasn’t even room to put a fridge.

I already had a capsule the size of one.

*Should I start looking at moving?*

I was thinking that as I slung the backpack I’d packed last night over my shoulder.

“…?”

Why was it so heavy? All I’d put in were a few outfits I’d bought yesterday.

When I set the backpack down, my family was the ones who suddenly got frantic.

“Son, you’ll be busy starting tomorrow, right? Hurry back, wash up, and get a good night’s sleep.”

“…A minute ago you told me to stay a few more days.”

“Oppa, you’re going to miss your bus.”

“I’m taking a taxi, though?”

“Night surcharge. There’s a night surcharge.”

At that point, I had a pretty good idea.

“When did you put it in?”

“P-put what in?”

“The money.”

Their faces answered for them. I sighed.

“I told you to keep it and use it when you needed it.”

“….”

“I make plenty of money. And I will from now on, too.”

I mixed fact and fiction fifty-fifty.

The average annual salary of a C-rank Hunter was five hundred million won. I’d met a generous employer in Team Leader Choi and gotten a bonus I never imagined, but if the System disappeared, all of it would go up in smoke.

That was why I’d wanted to give even more to my family, but…

“That’s money you risked your life to earn. Spend it on yourself. All right?”

“Mom.”

“Son.”

The next moment, the quiet words that came from Mom left me speechless.

“Don’t push yourself. Don’t get hurt, either. That’s enough for Mom.”

What else was I supposed to say?

A little later, I stepped out into the humid air of a summer night.

With shopping bags full of side dishes and a backpack stuffed with bundles of cash.

Vroom.

The whole taxi ride back to the goshiwon, I thought of Mom’s last words, and the warmth in them.

And of a voice in a memory that was growing fainter and fainter.

“Survive. I’m telling you to run without looking back. That’s your mission.”

* * *

Shaaah—

Blood spurted. Not the green blood of a monster, but red human blood. Feeling the burning pain in my thigh, I rammed my spear into the Lizardman Chieftain’s chest.

“Keee…”

Ding.

> **System**
>
> - You defeated **Lv. 50 Lizardman Chieftain**!
>
> - You gained EXP!

Gate cleared. A mana field leading outside formed over the Lizardman Chieftain’s lifeless body.

That was when Team Leader Choi pushed away from the tree.

“Three.”

“Pardon?”

“The number of times you’ve been injured today, Mr. Jin Taekyung.”

His long, sturdy fingers pointed to spot after spot on my body.

The nape of my neck and my arm, already treated with potions, and my thigh, still bleeding.

“I’m fine. It only grazed me. A low-grade potion is more than enough…”

“You’re not fine.”

He cut me off, his tone firm. Team Leader Choi’s expression was always unreadable, but this time was different.

One thing was certain. The emotion in that look wasn’t simple concern.

“You weren’t injured even once last week. Same Gate, same monsters. If this is happening, there’s only one reason.”

His clear eyes turned on me.

“Mr. Jin Taekyung. Is something wrong?”

* * *

One day. Two days. Three days.

Time passed, but things didn’t improve. In the end, on the fourth day, I took injuries in five places.

“Not in your current condition. Go home.”

Leaving Team Leader Choi’s words behind, I headed for the goshiwon, my head a mess.

*What’s the problem?*

Everything had been going well. The System hadn’t disappeared, and my account had some three hundred million won sitting in the bank. All that was left was to keep riding high as a C-rank Hunter, but…

*Damn dreams.*

That was when it started. After the first night at my family’s house, I began having nightmares.

The scenes in them grew clearer and clearer, and when a dream ended I woke up soaked in sweat. Even if I circulated my qi and pulled my condition up, my mind was unstable, so the mistakes only multiplied.

*This is going to be a problem.*

My body was in reality, but my mind was still trapped in Murim. I was wondering whether I should see a psychiatrist when I reached my goshiwon room.

Click.

“Oh, you’re back?”

The greeting was so natural I almost wondered if I’d walked into the wrong room.

I asked, incredulous,

“What are you doing?”

Jinho hyung answered,

“Disassembly and assembly.”

He was sitting in front of the capsule with a screwdriver. For a second my vision went yellow.

*This bastard isn’t actually—*

“Are you crazy? Move!”

“Hey, hey. You have to hear Korean all the way through.”

Jinho hyung hurriedly waved his hands.

“I haven’t even started yet.”

“What?”

“I just got here too. Seriously.”

He didn’t look like he was lying. Only after I checked that the capsule was still intact did a sigh of relief slip out.

“Phew.”

Jinho hyung looked thrown by my reaction.

“Why are you making such a fuss over one junk capsule that doesn’t even work? What happened to tossing it out like a piece of luggage?”

“That was then.”

There was no way Jinho hyung could know about Synchronization. Or what that unidentified thing—just a junk capsule to him—meant to me.

“Anyway, don’t touch it. Got it?”

“You look ready to beat me to death.”

“I’ll tear you apart.”

“….”

I ignored Jinho hyung’s baffled face and flopped onto the bed.

After that little episode, it felt like all the energy had drained out of me.

“Something going on?”

“Going on, my ass.”

“Complaints about you have been no joke lately. Today I barely calmed the guy next door down and sent him off.”

I could guess why.

Jinho hyung scooped up the tools he’d spread on the floor and went on.

“He says he’s going crazy because you keep groaning all night. Oh, and he asked who Jin Wikyung is.”

That name again.

I buried my face in the pillow.

“Just tell him she’s my girlfriend.”

I saw his hand quiver around the monkey wrench.

“You got a girlfriend? You traitorous bastard.”

“….”

“She pretty? How old? Show me a picture.”

This guy was thirty. I couldn’t help but despair.

“The name’s a bit exotic, though. Is she an ethnic Korean from China? Or Chinese?”

“…Chinese.”

Not exactly wrong.

“This bastard hits C-rank and he’s already gone global. Anyway, introduce me to a girl. I like China. Nǐ hǎo ma? Wǒ ài nǐ. What else was there?”

“You fucking bastard.”

“Idiot. You got the tones and the pronunciation all wrong. With that, you think you’ll last a hundred days? Repeat after me. Nǐ chī fàn le ma?”[^2]

“You fucking bastard.”

“Again. Nǐ chī fàn le ma?”

“You fucking bastard.”

“…What the hell is this bastard doing?”

I ignored Jinho hyung, who was getting angry at this sudden realization, and pointed at the door.

“Get out.”

*Please. Just let me have some time to myself.*

* * *

Once the room was quiet, I sat up on the bed and went over to the capsule. I tapped its old, grime-caked surface and muttered,

“What the hell are you?”

As expected, no answer came back.

I’d been hoping, privately. Shame.

*The System’s already synchronized with reality. Why couldn’t a machine talk too?*

Honestly, I wasn’t even sure it was a real machine. Reality had been fantasy for a long time now, but wasn’t this a whole new genre?

If I wrote my current situation as a novel, what genre would I even pick? Fantasy? A game novel? Or—

*Dimensional travel?*

Pffhh. A deflating sound slipped out. Dimensional travel? I really was losing it. There was no way something like that was possible.

There was no way it could be…

It was like ice water over my head. My mind snapped clear.

*…It is possible.*

Dimensional travel had happened in the past, and it still existed now.

The invasion of the Demon King Asmodeus, and the Gates, were the proof.

We only used Gates to come and go from reality, but decades ago a monster army had crossed through one from another dimension to Earth.

*The Demon World.*

A land of evil. The home of monsters. The Demon King’s domain.

An unknown dimension no human had ever set foot in, or even glimpsed. That was how humanity defined it.

But what if this capsule in front of me was a kind of Gate to another dimension? What if Murim was another unknown dimension?

*Murim is another reality.*

Everything I had seen and been through there.

Water. Earth. Wind. And people, too.

*They weren’t NPCs.*

I stared at my vacant face reflected on the capsule’s faded surface.

For a long while after that.

[^1]: A *goshiwon* is a tiny, inexpensive room-for-rent housing arrangement; three pyeong is roughly ten square meters.

[^2]: *Nǐ chī fàn le ma?* means “Have you eaten?” In Korean, its pronunciation resembles a profanity, which is why Taekyung keeps answering with “You fucking bastard.”
```
