# Retrospective Patch Plan — Chapters 40–43

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
  "summary": "6 findings in chapters 40-43",
  "findings": [
    {
      "chapter": 40,
      "confidence": 0.99,
      "current": "“What, has it only been a day or two?”",
      "defect": "The Korean is an idiom meaning that Jinho habitually comes into Taekyung’s room, not a literal question about whether one or two days have passed.",
      "id": "R0040-01",
      "rationale": "The replacement restores Jinho’s breezy implication that his presence in the room is routine.",
      "replacement": "“Is this anything new?”",
      "severity": "minor",
      "source": "“하루 이틀이야?”"
    },
    {
      "chapter": 40,
      "confidence": 0.97,
      "current": "“You stuck this in a piece of junk more than twenty years old before throwing it away?”",
      "defect": "The translation assigns the act of putting the manual inside the capsule to Taekyung. Jinho is instead questioning why whoever discarded the old capsule would have left its manual inside.",
      "id": "R0040-02",
      "rationale": "The source has an omitted generic subject and expresses disbelief about the capsule and manual being discarded together; it does not accuse Taekyung of inserting the manual.",
      "replacement": "“Someone left this inside when they threw out a piece of junk more than twenty years old?”",
      "severity": "major",
      "source": "“20년도 더 지난 고물을 버리면서 이런 걸 넣어 둔다고?”"
    },
    {
      "chapter": 42,
      "confidence": 0.99,
      "current": "People with money fought easy with magic equipment; people without it had to carry torches.",
      "defect": "“Fought easy” is ungrammatical English and disrupts the narrator’s otherwise sharp, colloquial contrast.",
      "id": "R0042-01",
      "rationale": "편하게 싸우고 means fighting comfortably or easily, not “fought easy.”",
      "replacement": "People with money had it easy fighting with magic equipment; people without it had to carry torches.",
      "severity": "minor",
      "source": "돈 있는 놈은 마법 장비로 편하게 싸우고 없는 놈은 횃불 들어야 한다."
    },
    {
      "chapter": 42,
      "confidence": 1.0,
      "current": "At best, he was first-rate. In Murim, that was exactly where he would stand.",
      "defect": "The established Murim realm term 일류 is not rendered with the glossary form and capitalization.",
      "id": "R0042-02",
      "rationale": "일류 denotes the established classification First Rate here rather than a generic description of quality.",
      "replacement": "At best, he was First Rate. In Murim, that was exactly where he would stand.",
      "severity": "minor",
      "source": "고작해야 일류. 무림에서의 그는 딱 그 정도다."
    },
    {
      "chapter": 43,
      "confidence": 0.96,
      "current": "That old Hobgoblin, using magic like this, was a monster at least one or two stages above us.",
      "defect": "The translation adds “above us,” making the monster one or two stages above the entire party, including C-rank Team Leader Choi. This conflicts with the subsequent revelation that the Priest itself is C-rank.",
      "id": "R0043-01",
      "rationale": "The source states that the Hobgoblin is a monster one or two tiers higher without making the whole party—including its C-rank member—the comparison point.",
      "replacement": "That old Hobgoblin, capable of magic like this, was a monster at least one or two tiers higher.",
      "severity": "major",
      "source": "이 정도 마법을 구사하는 저 늙은 홉 고블린은 최소 한두 단계 위의 몬스터라는 것."
    },
    {
      "chapter": 43,
      "confidence": 0.99,
      "current": "Rare Monsters were rare monsters that appeared in a given Gate only at a low rate.",
      "defect": "The tautology “Rare Monsters were rare monsters” is conspicuously defective English and blunts the explanatory beat.",
      "id": "R0043-02",
      "rationale": "The source explains that this monster category has a low probability of appearing in its associated Gate.",
      "replacement": "Rare Monsters appeared only infrequently within a given Gate.",
      "severity": "minor",
      "source": "레어 몬스터는 해당 게이트에서 드문 확률로 출현하는 희귀 몬스터다."
    }
  ]
}
```

## Chapter 40

### Korean source

```text
＃40화



나는 하늘을 날고 있다. 거대한 날개를 펴고 바람을 갈랐다.

저 아래 보이는 높고 가파른 협곡. 호리병 형상을 띤 그곳에 인간들이 있었다. 그 수가 어림잡아 수백.

중심에 선 남자가 목청껏 외쳤다.

“태원진가를 위해 싸우지 마라!”

그때 땅이 진동했다. 나무가 흔들리고 산새가 날아오른다.

흘끗 뒤를 돌아보자 거대한 먼지구름이 협곡을 휩쓸며 다가오고 있었다.

“너희를 위해 싸워라! 적들에게 짓밟힐 혈육과 사랑하는 이를 위해 싸워라!”

검을 뽑아 든 그가 포효한다.

“무인답게 맞서라! 나도 그러할 것이다!”

수백 개의 병장기가 나란히 뽑혔다. 성큼성큼 걸어 나간 남자가 선두에 섰다. 협곡을 가로지르던 먼지구름이 흩어지고 무수한 인간들이 모습을 드러낸다.

- 와아아!

- 태원진가 놈들을 쓸어 버려라!

문득 남자가 고개를 들었다. 나를 발견한 그가 씩 웃었다.

“느낌이 좋군.”

남자의 얼굴을 본 순간, 날개에 힘이 스르륵 빠졌다. 나는 의식 깊은 곳으로 추락했다.



* * *



“어푸, 어푸어푸!”

필사적으로 날개를, 아니 팔을 퍼덕거리다가 깨달았다.

‘꿈이었구나.’

천만다행이다. 죽는 줄 알았네. 한숨 돌린 후에야 방 안의 상황이 눈에 들어왔다.



- 뉴스 속보입니다. 합정역 3번 출구에서 새로운 게이트가 출몰했습니다. 마력 측정 결과 C급 게이트로 판명 났으며…….



책상 위, 아나운서의 모습을 비추고 있는 소형 TV. 그리고.

“방금 뭐냐?”

진호 형이 있었다. 한 손에는 냄비 뚜껑. 다른 한 손에는 젓가락을 든 그가 어처구니가 없다는 표정으로 나를 바라본다.

“행위 예술 같은 건가.”

“닥쳐. 꿈꿨어.”

“헤엄치는 꿈?”

“떨어지는 꿈.”

“좋겠네. 키 크겠다.”

영혼 없는 말을 던지고 후루룩 면발을 빨아들이는 모습이 자연스럽다. 순간 여기가 내 방이 맞나, 헷갈릴 정도로.

“여기 내 방 맞지?”

“그럴걸.”

“근데 형이 왜 여기 있어?”

“하루 이틀이야?”

그럴듯한데? 순간 설득당할 뻔했다.

“TV나 좀 끄든가. 사람 자는데.”

“어떤 몰상식한 새끼는 목젖도 때리더라. 사람 자는데.”

“…….”

하여간 저 인간, 말빨 하나는 끝내준다.

“할 말 없으면 라면이나 먹어. 너 깰 것 같아서 다섯 개 끓였어.”

선견지명 보소. 젓가락을 받아 든 나는 감회에 젖었다.

이게 보통 라면인가. 한 달 만에 먹는 라면이다. 식욕을 당기는 냄새, 딱 알맞게 익은 면발과 따로 썰어 넣은 청양고추로 매콤하게 끓여진 국물.

‘미쳤다, 미쳤어.’

후루루룩.

정신이 들었을 때는 모든 게 끝난 후였다. 냄비 바닥까지 싹싹 핥아 먹고 있는 나를 진호 형이 멍하니 바라봤다.

“광고 찍는 줄 알았네. 태어나서 라면 처음 먹어 보냐?”

“돌아와서 처음 먹는 라면이니까.”

“또 그 소리냐?”

“한 달 동안 중국 음식만 먹다가 라면 먹어 봐. 미슐랭이 따로 없다.”

“그만해. 이제 재미없으니까.”

질렸다는 표정. 하지만 이번에는 나도 믿는 구석이 있다.

“이거나 보고 다시 얘기합시다.”

“뭔데 이게.”

“뭐긴. 제품 사용 설명서지.”

“……이거 설마.”

“어, 저 캡슐에 들어 있더라고. 읽어 봐.”

“20년도 더 지난 고물을 버리면서 이런 걸 넣어 둔다고?”

진호 형은 고개를 갸웃하더니 설명서를 읽기 시작했다. 그리고 몇 초 지나지 않아 고개를 들었다.

“이거 인쇄가 잘못됐네. 제조일이 2020년 1월 1일이야.”

나도 처음에는 그렇게 생각했다. 처음에는.

“그거, 인쇄 오류 아닐지도 몰라.”

“응?”

“아니, 이건 아직 짐작이니까 넘어가자. 다른 부분은 어때? 거기 적혀 있는 모델명이나 제조사, 형은 들어 봤어?”

전자 기기, 그중에서도 캡슐이라면 사족을 못 쓰는 그다.

관련 사이트에서도 이름만 대면 아는 네임드 유저에 IT 전문 블로그도 운영했었다고 했다.

하지만 즉각 튀어나온 대답은 기대를 와르르 무너트렸다.

“아니.”

하긴, 인터넷 검색으로도 나오지 않았으니 어떻게 보면 당연한 결과다. 하지만 약간의 실망감은 어쩔 수 없다.

“전혀 몰라? 형 이쪽 계통은 완전 빠삭하잖아.”

“그렇지. 근데 이건 모르겠다.”

진호 형이 머리를 긁적였다.

“불법 개조 캡슐? 아니면 커스텀인가? 솔직히 저런 디자인은 처음 보네.”

들을수록 암담하다.

“그래, 디자인은 뭐 그렇다 쳐. 근데, 내가 최초 모델부터 최신형까지 다 꿰고 있는 사람이거든? 국내에 한 번이라도 풀린 물건은 싹 다.”

“그런데?”

“여기 적힌 모델명. 제조사. 완전히 쌩 초면이야.”

“해외 쪽 제조사일 수도 있지 않나?”

“어이고. 이 화상아, 등신아, 머저리 같은 놈아.”

진호 형이 속 터진다는 얼굴로 설명서를 내밀었다.

“첫 줄 읽어 봐라.”

“제품 사용 설명서?”

“그래. 한글이라고, 한글!”

“아.”

“H 소프트가 국내 제조 업체건, 해외 제조 업체건 사용 설명서까지 한글로 만들 정도면 모를 수가 없지. 그 바닥에 캡슐 제조사가 수백, 수천 개도 아닌데.”

완전 바보가 된 기분이다. 내가 캡슐 관해서 뭐 아는 게 있어야지. 그때 진호 형이 말했다.

“잠깐 기다려 봐.”

스마트폰을 꺼내 화면을 두드리는 걸 보니 검색 중인 모양이다. 하지만 결과는 뻔했다.

“시발, 야동 사이트밖에 안 뜨네.”

어, 거기 괜찮더라.

“유령 회사도 아니고. 왜 아무것도 안 떠?”

“일단 뒷장도 읽어 봐.”

마지막 장까지 읽으면 정말 유령에 홀린 기분이 될걸. 진호 형은 심각한 얼굴로 설명서를 넘겼다.

한 번. 그리고 다시 한번.

“기가 막히지?”

“그러네. 기가 막히네.”

허탈한 음성이었다.

“백지를 보라고 하니까 기가 막히네.”

“어?”

“어쩐지 뭔 설명서가 이렇게 허술하나 했다. 캡슐 부품 설명도 없고, 실행 방법도 없고, 그나마 있는 모델명, 제조사, 제조일도 개판이고.”

“아니, 백지? 그게 무슨 소리야!”

“얼씨구. 문과충 자식 천연덕스러운 거 보소.”

황급히 설명서를 뺏어 읽었다. 잠들기 전 봤던 그 내용이 그대로 있다. 두 번째 페이지에는 주의 사항. 마지막 페이지에는 주요 기능.

“이게 안 보여?”

“그만해라. 무서워지려고 한다.”

저 표정. 말투. 진심이다. 내게 보이는 이 글씨가, 진호 형에게는 보이지 않는다.

아니, 어쩌면…….

‘이 내용은 나한테만 보인다.’

나는 한동안 그렇게 굳어 있었다.



* * *



푸쉭-

후들거리는 다리로 캡슐을 빠져나왔다. 반질거리는 외관, 흡사 거대한 달걀처럼 보이는 이 물건은 지난달에 출시된 최신형 캡슐이다.

“어, 금방 나오셨네. 제가 추천해 드린 게임 해 보셨어요?”

카운터에 앉아 있던 캡슐방 사장의 물음에 나는 반쯤 혼이 나간 채로 대답했다.

“네.”

사장이 권유한 가상현실 게임은 동시 접속자만 천만 명에 달한다는 메가 히트작. 엄청난 그래픽과 뛰어난 자유도로 시장 점유율 70%가 넘는다고 했다.

“그래픽 미쳤죠?”

게임에 접속. 그래픽을 보고 생각했다. 내가 미쳤나?

‘이게 가장 잘나가는 가상현실 게임이라고?’

그래픽 좋은 건 알겠다. 하지만 딱 거기까지였다.

NPC들의 외모와 움직임, 대화 패턴과 내 캐릭터로 느껴지는 오감(五感). 모두 부자연스럽다. ‘게임’이지만 결코 ‘현실’처럼 느껴지진 않는다.

“혹시 무협 배경 게임도 있나요?”

“아하, 무협 쪽 취향이시구나? 꽤 있긴 하죠. 찾으시는 게임 제목이 뭔데요?”

“무림이요.”

“무림 온라인?”

“아뇨. 오픈 월드 식 게임이에요. 혼자 플레이하는.”

“무협 게임 중에 그런 게 있어요?”

그럼 그렇지. 더 들어 볼 것도 없다. 비틀비틀 문을 나서는 내게 사장이 인사했다.

“또 오세요!”

안 올 거다. 두 번 다시.



* * *



희망 고시원.

낡고 녹슨 간판 아래에 앉아 스마트폰을 꺼냈다. 신호음이 가기 무섭게 상대방이 전화를 받았다.

딸깍.

- 어, 왜.

하나뿐인 웬수, 아니 여동생인 하연이다. 특유의 싸가지 없는 목소리를 듣는 순간 목이 꽉 막혔다.

- 여보세요?

“……어.”

- 왜 전화했어?

“그냥. 목소리 듣고 싶어서.”

순간, 죽음 같은 침묵이 흘렀다.

- 끊는다.

“아니, 잠깐만. 잠깐만!”

- 3초 준다. 용건.

망할 년…….

그래, 이래야 진하연이지. 덕분에 잠시나마 촉촉해졌던 눈물샘이 피라미드 인근 모래처럼 건조해졌다.

“엄마는 뭐 하셔?”

- 잠깐 볼일 있다고 외출. 궁금하면 전화해 봐.

일부러 하지 않았다. 이 녀석 목소리에도 울컥하는데 엄마 목소리를 들으면 어린아이처럼 엉엉 울 것 같아서.

나는 재빨리 말을 돌렸다.

“너는?”

- 수능 120일 남은 고삼이 뭐 하겠어. 공부하지.

평소보다 까칠한 말투. 수험생 스트레스가 상당한 모양이다.

“공부는 잘되고?”

- 이번에 7월 모의고사 망쳤어. 컨디션 조절 실패해서 쉬운 문제도 다 틀리고. 아, 생각할수록 짜증 나.

“괜찮아. 실전에서만 잘하면 되지. 몇 개나 틀렸는데?”

- 두 개.

“그 정도면 1등급이잖아. 다른 과목은?”

- 전 과목 두 개.

“응?”

- 한국사에서 하나. 수학에서 하나.

“……전 과목 통틀어서 두 개? 진심이냐?”

- 당연히 그거 말한 거지.

똑똑한 년…….

공부 잘하는 건 알고 있었는데 이 정도일 줄이야. 과거 내 학창 시절 성적을 생각해 보면 유전자 몰빵이라는 게 정말 존재하는 모양이다.

“공부 좀 한다?”

- 오빠 입장에서 보면 엄청 잘하는 거 아냐?

“무, 무슨 헛소리를! 나도 공부 꽤 했거든? 네가 초등학생 때라 기억을 못 하는 거…….”

- 지난주에 대청소하다가 오빠 성적표 나왔어. 7등급이 하도 많아서 무슨 잭팟 터진 슬롯머신인 줄.

“용돈 필요하지? 요즘 화장품은 얼마나 하냐?”

- 애잔하다. 진짜.

잔인한 년…….

통화는 10분이 넘도록 이어졌다. 나는 주로 듣는 쪽이었다. 공부, 학교, 관심 있는 남학생 이야기를 떠들어 대는 하연이의 목소리는 처음보다 한결 밝아져 있었다.

문득 묘한 감상에 젖어 들었다.

‘정말 돌아왔구나.’

나는 꿈을 꿨던 걸까, 아니면 망상에 빠져 있던 걸까.

현실에서는 고작 하루가 지났을 뿐인데 도저히 이해할 수 없는 불가사의한 일들이 일어났다.

하지만 이제는 이해하지 않기로 했다.

‘이제 현실로 돌아왔으니까.’

그리고 현실에서 살아야 하니까.

이곳에 가족이 있고 내가 있다. 그럼 그걸로 된 거다. 나는 아주 잠깐 이상한 꿈을 꾼 거다. 시간이 흐르면 자연스럽게 잊혀질, 그런 꿈.

- 그래서 내가…….

“응.”

조잘거리는 여동생의 목소리를 들으며, 나는 자리에서 일어났다. 낡고 녹슨 간판 아래를 벗어나 내 방으로 돌아가야 할 시간이었다.



* * *



지잉. 지이잉.

성진호는 부스스 눈을 떴다. 머리맡에 놓아둔 스마트폰이 울리고 있었다. 새벽 여섯 시. 오늘 하루를 시작하는 신호였다.

“어이고, 죽겠다.”

집을 나온 지 5년째. 아침마다 코끝을 파고드는 곰팡내가 퍽 익숙해졌다. 성진호는 반쯤 감긴 눈으로 담배와 라이터를 주머니에 쑤셔 넣고 방을 나섰다.

‘잠 깨는 데는 담배가 최고지.’

슬리퍼를 질질 끌며 옥상으로 올라간 그가 담배를 입에 물었을 때였다.

쿵.

“응?”

무슨 소리지? 의문과 함께 난간으로 고개를 내밀자 바로 앞 분리수거장에 놓인 쇳덩어리가 눈에 띄었다.

그리고 그걸 물끄러미 바라보는 덩치 좋은 청년도.

“야! 진태경!”

성진호의 외침에 진태경이 고개를 들었다.

“왜?”

“그거 버리게?”

쇳덩어리의 정체는 전날 주워 온 고물 캡슐이었다. 저걸로 되지 않는 장난이나 치더니 도로 갖다 버리려는 모양이었다.

‘그런 것치곤 너무 진지하긴 했는데…… 뭐, 헛소리지.’

성진호가 피식 웃었다.

“왜 버려. 무림 다시 안 가?”

“그걸 믿었어?”

진태경이 마주 웃었다. 하지만 오랫동안 그를 지켜봐 온 성진호가 보기에는 어쩐지 어색한 웃음이었다.

‘뭐지?’

묘한 느낌이다. 찝찝해하는 성진호에게 손을 흔들어 보인 진태경이 언덕을 내려가기 시작했다.

“어디 가, 인마! 이따 같이 아침 안 먹어?”

“일해야 돼!”

진태경은 뒤도 돌아보지 않고 떠났다. 성진호는 반쯤 타들어 간 담배를 한 모금 빨았다.

“새끼, 열심히 사네…….”

이윽고 진태경의 모습이 시야에서 사라졌다. 화분에 담배를 비벼 끄고 떠나려던 성진호의 눈에 고물 캡슐이 눈에 띈 것도 그때였다.

‘제조사가 H 소프트라고 했나?’

허접한 장난이겠지만, 알아봐서 나쁠 건 없겠지.
```

### Current accepted English

```markdown
# Chapter 40

I was flying through the sky. Enormous wings spread, I cut through the wind.

Far below, a high, steep gorge came into view. Shaped like a bottle gourd, it held people—hundreds of them, at a rough count.

A man standing at the center shouted at the top of his lungs.

“Don’t fight for the Jin Family of Taiyuan!”

Then the ground shook. Trees trembled, and mountain birds took flight.

I glanced over my shoulder. A huge cloud of dust was sweeping through the gorge toward us.

“Fight for yourselves! Fight for the flesh and blood and loved ones who will be trampled by the enemy!”

He drew his sword and roared.

“Stand and face them like martial artists! I will do the same!”

Hundreds of weapons were drawn in unison. The man strode forward and took the lead. The cloud of dust crossing the gorge scattered, revealing countless people.

— Waaaaah!

— Wipe out those Jin Family bastards!

The man suddenly looked up. When he spotted me, he grinned.

“I’ve got a good feeling about this.”

The moment I saw his face, the strength drained from my wings. I plunged into the depths of consciousness.

* * *

“Pwah, pwah-pwah!”

I flailed desperately with my wings—or rather, my arms—before it hit me.

*It was a dream.*

Thank god. I thought I was a goner. Only after catching my breath did the situation in the room come into focus.

— This is a breaking news report. A new Gate has appeared at Exit 3 of Hapjeong Station. Mana measurements have confirmed it as a C-rank Gate, and…

A small TV sat on the desk, showing an announcer. And then there was—

“What the hell was that?”

Jinho hyung. He held a pot lid in one hand and chopsticks in the other, staring at me like I was out of my mind.

“Some kind of performance art?”

“Shut up. I was dreaming.”

“About swimming?”

“About falling.”

“Good for you. You’ll grow taller.”

He tossed out the line with zero soul and slurped up his noodles, looking completely at home. For a moment I wondered if this was even my room.

“This is my room, right?”

“Probably.”

“Then why are you here?”

“What, has it only been a day or two?”

That actually sounded plausible. I almost bought it.

“Turn the TV off or something. People are sleeping.”

“Some inconsiderate bastard even hits people in the uvula while they’re sleeping.”

“…”

Anyway, that bastard had one hell of a mouth on him.

“If you’ve got nothing to say, eat some ramen. I boiled five packs because I thought you might wake up.”

Talk about foresight. I took the chopsticks from him, a wave of feeling hitting me.

Was this ordinary ramen? This was ramen I was eating for the first time in a month.

The smell that pulled at my appetite. Noodles cooked just right. Broth boiled spicy with separately sliced Cheongyang peppers.

*Insane. This is insane.*

Slurp.

By the time I came to, it was all over. Jinho hyung stared blankly at me as I licked the pot clean.

“I thought you were filming a commercial. Have you never eaten ramen in your life?”

“It’s my first ramen since I came back.”

“Are you still on that?”

“Try eating nothing but Chinese food for a month, then have some ramen. Michelin’s got nothing on this.”

“Stop. It’s not funny anymore.”

He looked thoroughly fed up. But this time, I had something to back me up.

“Look this over, then we’ll talk again.”

“What is this?”

“What do you think? A product user manual.”

“…”

“Don’t tell me…”

“Yeah. It was inside that capsule. Read it.”

“You stuck this in a piece of junk more than twenty years old before throwing it away?”

Jinho hyung tilted his head, then started reading. A few seconds later, he looked up.

“This is a misprint. The date of manufacture is January 1, 2020.”

I’d thought the same thing at first. At first.

“That might not be a printing error.”

“Huh?”

“No, never mind—that’s still just a guess. What about the rest? The model name and manufacturer listed there. Have you heard of them?”

Jinho hyung was crazy about electronics, especially capsules.

On the related sites, he was a named user people recognized on sight. He’d even run an IT blog.

But the answer that came out immediately sent my expectations crashing down.

“No.”

Well, that was only natural. Even an internet search hadn’t turned anything up. Still, I couldn’t help feeling a little disappointed.

“You really don’t know? You know this field inside out.”

“Yeah. But I don’t know this.”

Jinho hyung scratched his head.

“An illegally modded capsule? Or a custom job? Honestly, I’ve never seen a design like that.”

The more he talked, the bleaker it got.

“Fine, I’ll grant you the design. But I know every model from the earliest ones to the latest. Everything that’s ever been released in Korea.”

“And?”

“The model name written here. The manufacturer. Complete strangers.”

“Couldn’t it be an overseas manufacturer?”

“Oh, you hopeless idiot. You dumbass. You moron.”

Jinho hyung thrust the manual at me, looking thoroughly exasperated.

“Read the first line.”

“Product User Manual?”

“Exactly. It’s in Korean. Korean!”

“Oh.”

“Whether H Soft is a domestic manufacturer or an overseas one, if they went as far as making the user manual in Korean, there’s no way I wouldn’t know them. It’s not like there are hundreds or thousands of capsule manufacturers in this business.”

I felt like a complete idiot. Not that I knew anything about capsules. That was when Jinho hyung spoke up.

“Wait a second.”

He pulled out his smartphone and started tapping the screen. Searching, from the looks of it. But the result was obvious.

“Fuck. All that comes up is porn sites.”

*Yeah, that one was pretty good.*

“It’s not even a ghost company. Why isn’t anything coming up?”

“Read the rest of it, too.”

By the time he reached the last page, he’d really feel like he’d been haunted. Jinho hyung turned the pages with a serious expression.

Once.

Then once more.

“Isn’t it incredible?”

“Yeah. Incredible.”

His voice was hollow.

“You told me to look at blank pages. That’s incredible.”

“Huh?”

“No wonder I thought this manual was so slapdash. No explanation of the capsule’s parts, no operating instructions, and even the model name, manufacturer, and date of manufacture are a mess.”

“Blank pages? What are you talking about?”

“Well, well. Look at this humanities-major bastard, acting all innocent.”

I snatched the manual and read it in a hurry. The contents I’d seen before falling asleep were still there. Precautions on the second page. Key features on the last.

“You can’t see this?”

“Cut it out. This is starting to get scary.”

That look. That tone. He meant it. The writing I could see was invisible to Jinho hyung.

Or maybe…

*Only I can see this.*

I stayed frozen like that for a long while.

* * *

Pshhh—

I climbed out of the capsule on shaky legs. Glossy exterior, shaped like a giant egg—this was the latest model, released only last month.

“Oh, you’re out already. Did you try the game I recommended?”

Still half out of my mind, I answered the capsule café owner at the counter.

“Yes.”

The virtual-reality game he’d recommended was a megahit with ten million concurrent users. Incredible graphics, outstanding freedom, over seventy percent of the market, he’d said.

“The graphics are insane, right?”

I logged in. I looked at the graphics and thought:

*Am I the one who’s insane?*

*This is the most popular virtual-reality game there is?*

The graphics were good. I could give it that. But that was as far as it went.

The NPCs’ faces and movements, their dialogue patterns, the five senses I felt through my character—all of it was unnatural. It was a *game*, but it never felt like *reality*.

“Do you have any games set in wuxia?”

“Ah, so you’re into wuxia? There are quite a few. What’s the title you’re looking for?”

“Murim.”

“Murim Online?”

“No. It’s an open-world game. One you play alone.”

“Are there games like that in the wuxia genre?”

Figures. There was nothing more to hear. I staggered out the door, and the owner called after me.

“Come again!”

I wouldn’t.

Not ever again.

* * *

Hope Goshiwon.

I sat beneath the old, rusted sign and pulled out my smartphone. The other end picked up almost before it could ring.

Click.

“Yeah. Why?”

My one and only nemesis—no, my younger sister, Hayeon. The moment I heard that uniquely bratty voice of hers, my throat closed up.

“Hello?”

“…Yeah.”

“Why’d you call?”

“Just. I wanted to hear your voice.”

A deathly silence followed.

“I’m hanging up.”

“No, wait. Wait!”

“Three seconds. What’s your business.”

*That damn girl…*

Right. This was Jin Hayeon. Thanks to her, the tear ducts that had gotten a little moist dried out like sand around the pyramids.

“What’s Mom doing?”

“She went out. Said she had an errand. Call her if you’re curious.”

I didn’t. On purpose. Even this brat’s voice was enough to choke me up. If I heard Mom’s, I’d bawl like a little kid.

I quickly changed the subject.

“What about you?”

“What’s a high-school senior with a hundred and twenty days left until the college entrance exam supposed to do? Study.”

Her tone was sharper than usual. Exam stress must have been hitting her hard.

“How’s studying going?”

“I bombed the July mock exam. I didn’t manage my condition right and missed even the easy questions. God, the more I think about it, the more annoyed I get.”

“It’s fine. Just do well on the real thing. How many did you miss?”

“Two.”

“That’s still Grade 1.[^1] What about the other subjects?”

“Two across all subjects.”

“Huh?”

“One in Korean history and one in math.”

“…Two in total, across every subject? Are you serious?”

“Obviously that’s what I meant.”

*Smart little brat…*

I knew she was good at studying, but I hadn’t realized she was this good. Thinking back on my own school grades, it really seemed like there was such a thing as dumping all the genes into one kid.

“You study pretty well, huh?”

“From an older brother’s standpoint, isn’t it amazing?”

“W-what kind of nonsense is that? I studied pretty well too, you know? You just don’t remember because you were in elementary school…”

“Last week during a deep clean, I found your report card. There were so many Grade 7s I thought it was a slot machine that had hit the jackpot.”

“You need some allowance, right? How much do cosmetics cost these days?”

“That’s pathetic. Seriously.”

*Cruel girl…*

The call lasted more than ten minutes. I did most of the listening. Hayeon rattled on about studying, school, and a boy she was interested in, and her voice was much brighter than it had been at first.

I found myself getting oddly sentimental.

*I really did come back.*

Had I been dreaming? Or lost in a delusion?

Only a day had passed in reality, yet utterly incomprehensible, inexplicable things had happened.

But I decided not to try to understand them anymore.

*I’m back in reality now.*

And I had to live in reality.

My family was here. I was here. That was enough. I had simply dreamed a strange dream for a little while. The kind of dream that would fade on its own with time.

“So I…”

“Yeah.”

Listening to my little sister chatter, I stood up. It was time to leave the old, rusted sign behind and go back to my room.

* * *

Bzzzt. Bzzzt.

Seong Jinho cracked his bleary eyes open. The smartphone by his pillow was ringing.

Six in the morning. The signal that started the day.

“Oh, I’m dying.”

It had been five years since he left home. The moldy smell that crept into his nose every morning had gotten pretty familiar. Eyes half shut, Seong Jinho shoved his cigarettes and lighter into his pocket and left the room.

*Nothing wakes you up like a cigarette.*

He shuffled up to the rooftop in his slippers. He’d just put a cigarette between his lips when—

Thud.

“Huh?”

What was that? Wondering, he leaned over the railing, and a hunk of metal sitting in the recycling area right in front of him caught his eye.

So did the well-built young man gazing at it.

“Hey! Jin Taekyung!”

At Seong Jinho’s shout, Jin Taekyung looked up.

“What?”

“You throwing that away?”

The hunk of metal was the junk capsule Taekyung had picked up the day before. After pulling some failed prank with it, he seemed to be taking it back out to throw away.

*He’d been awfully serious for a prank like that… Ah, whatever. It was nonsense.*

Seong Jinho gave a short laugh.

“Why throw it away? Not going back to Murim?”

“You believed that?”

Jin Taekyung smiled back. But to Seong Jinho, who had watched him for a long time, the smile looked somehow awkward.

*What’s with him?*

Something felt off. As Seong Jinho stood there uneasily, Jin Taekyung waved and started down the hill.

“Where are you going, you punk? Aren’t we eating breakfast together later?”

“I have to work!”

Jin Taekyung left without looking back. Seong Jinho took a drag from his half-burned cigarette.

“That bastard’s really working hard…”

Soon, Jin Taekyung disappeared from sight. Seong Jinho stubbed out his cigarette in a flowerpot and was about to leave when the junk capsule caught his eye.

*He said the manufacturer was H Soft, right?*

It was probably just some half-assed prank, but there was no harm in looking into it.

[^1]: Korean mock exams use a 1–9 scale; Grade 1 is the highest.
```
## Chapter 42

### Korean source

```text
＃42화



게이트(Gate).

대격변이 남긴 가장 큰 흔적.

삼십여 년 전 마왕 아스모데우스가 침략 루트로 사용했던 그곳은, 헌터들의 생계 수단이자 마정석이라는 고차원 에너지 자원의 발굴 현장으로 전락한 지 오래였다.

“평화 길드 분들이시죠?”

입구에 나와 있던 작업복 차림의 중년인이 다가왔다.

게이트마다 배치된 게이트 관리청 소속의 공무원이다.

“네.”

최 팀장의 무뚝뚝한 대답에 공무원이 고개를 끄덕였다.

“딱 맞춰 오셨네요. 언제 진입하실 겁니까?”

“장비 갖추고 바로 들어가겠습니다.”

“2층에 대기실 있으니까 준비 마치고 내려오시면 됩니다. 그럼.”

우리는 최 팀장을 따라 이동했다. 관리청 공무원이 상주하는 2층짜리 건물은 낡을 대로 낡았는데, 대기실 역시 비슷한 상황이었다.

‘와 씨. 냄새 봐라.’

문을 열자마자 땀 냄새가 코를 찌른다. 녹슨 캐비닛과 꽉 찬 휴지통도 눈에 띄었다.

“여긴 좀 심하네. 환기도 안 시키나?”

“게이트 담당 공무원들이 그렇지 뭐. 괜히 꿀 보직이 아니여.”

나는 투덜거리는 소리를 뒤로하고 레이드 장비로 환복하기 시작했다. 가죽 갑옷에 가벼운 소재의 전투화. 마지막으로 길쭉한 케이스에서 창을 꺼내 쥐었다.

‘오랜만이네.’

손아귀에 딱 들어오는 이 감촉. 익숙하면서도 낯설다.

지난 한 달 동안 썼던 무기와는 확실히 차이가…… 아, 아니다. 더는 생각하지 말자.

‘이젠 다 잊어야지.’

괜히 멀쩡한 전투화 끈을 조이는 내게 임꺽정이 다가왔다.

그는 전신 갑옷과 거대한 타워 실드를 갖춘 메인 탱커의 모습이었다.

“준비 끝났어?”

“예. 뭐.”

나를 위아래로 훑어본 임꺽정이 혀를 내둘렀다.

“이 녀석 보게. 도대체 언제 적 장비야?”

“글쎄요. 처음 시작할 때 샀으니까 적어도 7년?”

초짜 시절, 동대문 지하 매장에서 큰맘 먹고 질렀더랬다. 가격도 정확히 기억한다. 198만 원.

‘지르고 나서 며칠 동안 잠도 제대로 못 잤지.’

헌터는 수입만큼 지출도 큰 직업이다. 그 지출의 대부분을 차지하는 게 장비 관련이고. 이게 다 게이트의 특수성 때문이다.

‘마나, 혹은 마력이 깃들지 않은 장비는 금방 망가지니까.’

그래서 가장 흔하게 쓰이는 방법이 게이트 몬스터에게 얻은 마정석을 재료로 장비를 제작하는 거다.

사용된 마정석의 등급이 높을수록 가격은 천정부지로 솟는다.

“7년? 세상에. 아무리 돈이 좋아도 쓸 때는 써야지. 목숨에 돈 아낄래?”

“음. 사정이 있었어요.”

굳이 말하고 싶지 않은 사정이다. 임꺽정은 걱정스러운 목소리로 말했다.

“오늘은 비전투 포지션이니 괜찮겠지만…… 조심해라.”

“네.”

대답하면서도 기분이 묘하다. 얼마 전까지 조심하라는 말을 입에 달고 살던 누군가가 떠올라서.

하지만 감상에 젖는 것도 잠시.

“다들 준비 끝나셨습니까?”

최 팀장의 등장에 나는 입을 딱 벌렸다.

저거 설마.

“붉은 드레이크 가죽 세트?”

“음.”

최 팀장의 얼굴이 굳었다. 명품관 카탈로그에서나 보던 거라 나도 모르게 그만 실수했다.

“아, 죄송합…….”

“별거 아닙니다. 다섯 종류의 마법과 B급 마정석을 재료로 만들었을 뿐이죠.”

“……?”

“강조하는 건 아니지만 다섯 종류의 마법과 B급 마정석이 재료입니다.”

“아, 네.”

“붉은 드레이크의 가죽이 인기가 좋은 건 특유의 윤기 때문인데, 보기에만 그럴듯하고 별 쓸모는 없습니다.”

최 팀장이 굳은 얼굴로 몸을 움직였다. 은은한 붉은 빛이 번뜩였다.

“하지만 매우 아름답죠.”

“…….”

“이만 내려갑시다.”

최 팀장이 먼저 대기실을 나가자 임꺽정이 다가와 말했다.

“저 친구 장비 알아봐 주는 거 엄청 좋아해.”

“아니 뭐, 이해는 가는데…… 왜 저래요?”

“몰라. 장비 덕후야. 전 재산 털어서 저거 사고 밤마다 입고 잔다는 소문도 있어.”

저 자식도 또라이구나.

나는 내심 한탄하며 오늘 레이드가 무사히 끝나길 빌었다.



* * *



“신청하신 인원이랑 다르군요.”

공무원은 불편한 표정이었다. 그럴 만도 하지. 이제 진입해야 하는데 인원이 전부 안 모였으니까.

‘도대체 얼마나 기다려야 하나.’

현재 게이트 앞에 집결한 인원은 여섯 명. 짐꾼으로 온 나를 제외하면 전투 인원은 다섯밖에 안 된다.

E급 게이트니까 최소한 동급의 헌터 다섯이 더 필요한데…… 평화 길드 놈들이 코빼기도 보이지 않으니 공무원 입장에서는 짜증이 날 수밖에.

“추가된 인원이 있으면 미리 말씀을 해 주셔야죠.”

응? 방금 뭐라고 한 거냐.

추가된 인원이라니?

“죄송합니다.”

최 팀장의 무뚝뚝한 사과에 공무원이 펜을 들어 서류에 좍좍 줄을 그었다.

“뭐 수정하면 되니까 큰 문제는 없는데…… 다음부턴 조심해 주십쇼.”

“예.”

큰 문제가 없기는 시발. 사람이 없잖아, 사람이!

나는 임꺽정의 옆구리를 쿡 찔렀다.

“형님. 다른 사람들은 언제 와요?”

“무슨 사람들?”

“평화 길드요.”

“최 팀장 있잖아.”

“네?”

“아, 말 안 했었나? 평화 길드, 신생이라 인원이 없어. 길드장 포함 세 명이 전부지. 으하하.”

……웃어?

“아니, 형님.”

“알아, 인마. 근데 걱정 안 해도 돼.”

내 어깨를 툭 친 임꺽정이 서류에 사인 중인 최 팀장을 가리켰다.

“저 양반, C급 헌터거든.”

“아. C급…….”

나는 입을 다물었다. 최 팀장이 C급 헌터라면 문제없다. 아니, E급 헌터 열 명보다 훨씬 낫다. 그는 나 같은 하급 헌터와 격이 다른 ‘중급 헌터’니까.

‘명품 장비 걸쳤을 때부터 알아차렸어야 했는데.’

고급 아파트를 몸에 두르고 다니는 인간이다. 어지간한 하급 헌터들은 전 재산을 열 번 털어도 못 사는 가격.

최 팀장의 뒷모습에서 은은한 후광이 비쳤다.

“서명 확인 바랍니다.”

공무원에게 펜을 넘겨주는 모습도 어쩜 저렇게 우아하냐.

작은 움직임조차 부티가 좔좔 흐르는 것 같다.

저게 바로 C급 헌터의 품격인가.

‘존나 멋있어.’

의형제 맺고 싶다. 게이트 아래에서 게이결의, 아니 게이트결의 맺고 싶다.

“자, 그럼 이제 들어갈…… 뭡니까?”

최 팀장이 흠칫한 얼굴로 나를 바라봤다.

“아뇨. 그냥 멋있어서요.”

“네?”

“장비. 멋있다고요.”

그 순간, 최 팀장의 입꼬리가 꿈틀거렸다.

“별거 아닙니다. 다섯 종류의 마법과 B급 마정석을 재료로…….”

친해지고 싶은 또라이다.



* * *



게이트를 향해 한 걸음을 내디뎠다.

쏴아악-

익숙한 느낌이 전신을 감싼다. 서늘하면서 끈적거리는 마력 특유의 기운. 그리고 뒤바뀐 풍경.

“동굴이군요.”

최 팀장의 말처럼 이번 레이드 장소는 동굴이었다. 습기를 머금은 벽면은 축축했고 사방은 옅은 어둠에 잠겨 있었다.

“태경 씨. 손전등 꺼내세요.”

“넵.”

나는 재빨리 배낭을 내려놨다. 게이트 진입 직전, 최 팀장에게 건네받은 짐꾼용 가방이다. 겉보기에는 평범하지만 무려 공간 확장에 경량화 마법까지 걸려 있는 고가의 물품.

“여기 있습니다. 손전등.”

달라니까 주긴 하는데, 내 경험상 그리 좋은 방법은 아니다. 간편한 대신 빛이 사라질 경우 갑작스러운 어둠에 적응하지 못하기 때문이다.

차라리 잠깐 대기하면서 눈에 어둠이 익기를 기다리는 게 훨씬…….

딸깍.

“빛이 있으라. 라이트(Light).”

슈웅. 손전등으로부터 축구공만 한 빛 덩어리가 튀어나와 동굴 천장에 철썩 달라붙는다.

“……마법?”

“주문만 영창하면 바로 발동되는 내장 마법입니다. 지속력이 꽤 길어서 앞으로 서너 시간은 문제없어요. M사에서 한정판으로 구매한 물건인데…….”

지켜보던 임꺽정이 한마디로 축약했다.

“엄청 비싸.”

최 팀장의 얼굴이 살짝 어두워지는 건 기분 탓인가, 아니면 그림자 때문인가. 어쨌건 덕분에 레이드가 한결 쉬워졌다.

‘역시 돈이 최고야.’

세상은 자본이 지배하고 게이트도 마찬가지다. 돈 있는 놈은 마법 장비로 편하게 싸우고 없는 놈은 횃불 들어야 한다.

“각자 위치로.”

최 팀장의 지시에 사람들은 즉각 반응했다. 탱커 포지션인 임꺽정, 그리고 다른 E급 헌터가 선두에 섰고 최 팀장이 그다음. 짐꾼인 나와 원거리 딜러 둘이 가장 뒤에 섰다.

“이동.”

우리는 천천히 앞을 향해 나아가기 시작했다.

환한 마법의 불빛이 길을 밝혀 주었다.

“…….”

하나 갖고 싶다.



* * *



“키이이잇!”

어둠 속에 웅크리고 있던 녀석들이 괴성과 함께 모습을 드러냈다. 녹색 피부에 짧은 몸통. 흉측해 보이는 팔다리.

일반 고블린의 상위종인 홉 고블린(Hob goblin)이다.

‘머릿수는 대략 서른.’

고작 다섯 명으로는 힘든 싸움이 될 것이다.

‘하지만 C급 헌터가 있으면 이야기가 달라지지.’

거기에 다른 네 명은 최소 십수 년 경력의 E급 베테랑.

나는 멀찍이 물러서서 전투를 구경했다.

“원거리!”

최 팀장의 말이 떨어짐과 동시에 화살이 쏘아졌다. 한 발에 한 놈씩. 급소를 파고드는 화살에 방패가 없는 홉 고블린들이 우수수 쓰러진다.

“키잇!”

“어이고, 방패병 나왔다. 어쩔까요?”

“대기.”

최 팀장이 이어 말했다.

“탱커 전진.”

두꺼운 전신 갑옷에 타워 실드를 든 탱커들이 움직였다. 임꺽정도 그렇고, 다른 한 사람도 190센티가 넘는 거구들이라 위압감이 장난이 아니다.

“키이이잇!”

하지만 몬스터는 괜히 몬스터가 아니다. 머릿수만 믿은 홉 고블린들이 벌 떼처럼 달려들었다.

하지만…….

“어쭈.”

뻐버벙!

크고 아름다운 타워 실드에 피떡이 되어 날아갔다. 기세를 탄 임꺽정이 철퇴를 파리채처럼 휘두를 때마다 팔다리가 아작 나고 머리통이 박살 난다.

“요놈! 요놈!”

……무슨 두더지 게임이야?

‘역시 고인물.’

네 명 모두 과하지 않은 선에서 자신의 포지션을 지키면서 적들의 숫자를 착실하게 줄이고 있다.

물러설 때와 나아갈 때를 아는 건 풍부한 경험에서 우러나온 전투 지능이다.

“전원 위치 고수.”

그리고 한 사람.

지금껏 전투의 흐름을 조율하던 그가 움직였다.

“나머진 제가 맡겠습니다.”

동시에 갑옷을 타고 번뜩이는 붉은 선이 스무 마리의 홉 고블린 사이로 파고들었다.

서걱-

깔끔한 궤적과 함께 목이 솟구친다. 순식간에 벌어진 일에 놈들은 제대로 반응하지 못했다.

“키이이?”

서걱. 서걱. 서걱.

칼날은 멈추지 않았다. 무자비하고 효율적으로 적들의 급소를 꿰뚫고 베어 냈다. 그것은 더 이상 전투가 아니었다.

학살. 단 한 명의 인간이 이십여 마리의 몬스터를 상대로 벌이는 학살이다.

‘이게 C급 헌터.’

그의 속도, 근력. 모두 보인다. 그리고 느꼈다.

‘역시 강해.’

F급에 불과한 나로서는 감히 넘볼 수 없다. 무려 세 단계 높은 중급 헌터니까. 그건 노력으로는 결코 메울 수 없는, 넓은 강이자 높은 벽이다.

하지만 동시에 어떤 의문이 고개를 들었다.

‘만약 무림이라면 어땠을까.’

최 팀장은 분명 강하다. C급 헌터에 어울리는 능력과 풍부한 경험을 갖췄다. 그러나 이곳이 무림이라면. 또 그가 무림인이라면…….

‘내가 더 강해.’

빠르고 힘 있는 동작이지만 그뿐이다. 그는 무공도 익히지 않았고, 마나를 효율적으로 사용하지도 못한다.

고작해야 일류. 무림에서의 그는 딱 그 정도다.

‘하지만 이게 현실이지.’

나도 모르게 입술을 깨물었다.

중급 헌터와 최하급 헌터. 중급 헌터가 값비싼 장비를 입고 몬스터들을 학살할 때 최하급 헌터는 멍하니 바라볼 뿐이다.

짐꾼이라는 역할로.

“끼이이잇…….”

마지막 홉 고블린이 쓰러졌다. 놈의 가슴에서 검을 빼낸 최 팀장과 시선이 부딪쳤다.

“태경 씨. 부산물 처리 부탁합니다.”

“…….”

“태경 씨?”

그에게 말하고 싶었다. 내가 당신보다 강하다고.

하지만 끝내 말하지 못한 것은 이게 내 현실이기 때문이다.

“……고생하셨습니다.”

나는 당신보다 강‘했었’다.
```

### Current accepted English

```markdown
# Chapter 42

A Gate.

The greatest scar left behind by the Great Cataclysm.

More than thirty years ago, Demon King Asmodeus had used them as an invasion route. These days, they had long since been reduced to a livelihood for Hunters and excavation sites for a higher-dimensional energy resource called Magic Gems.

“Are you with the Peace Guild?”

A middle-aged man in work clothes came over from the entrance.

He was a civil servant from the Gate Management Office, posted at every Gate.

“Yes.”

At Team Leader Choi’s curt reply, the civil servant nodded.

“You’re right on time. When will you be entering?”

“We’ll gear up and go in right away.”

“There’s a waiting room on the second floor. Come down when you’re ready. Right, then.”

We followed Team Leader Choi. The two-story building where the Management Office civil servant was stationed was as run-down as a building could get, and the waiting room wasn’t much better.

*Damn. Get a load of that smell.*

The moment we opened the door, the stench of sweat hit me. Rusty cabinets and an overflowing trash can jumped out at me too.

“This place is pretty bad. Don’t they even air it out?”

“That’s how Gate officials are. It’s not called a cushy post for nothing.”

I left the grumbling behind and started changing into my raid gear. Leather armor and lightweight combat boots. Last, I drew a spear from its long case and gripped it.

*It’s been a while.*

That snug fit in my hand felt familiar and strange at the same time.

It was definitely different from the weapon I’d used over the past month… Ah, no. I shouldn’t think about that anymore.

*I have to forget all of it now.*

I was tightening the perfectly fine laces on my combat boots for no reason when Im Kkeokjeong came over.

He looked every bit the main tank, in full-body armor with a massive tower shield.

“Are you ready?”

“Yes. Pretty much.”

Im Kkeokjeong looked me up and down, then clicked his tongue.

“Look at this guy. How old is that equipment, even?”

“Who knows? I bought it when I first started, so at least seven years?”

Back when I was a rookie, I’d splurged on it at an underground shop in Dongdaemun.[^1] I still remembered the exact price.

1.98 million won.

*I couldn’t sleep properly for days after buying it.*

Hunting was a job where the expenses ran about as high as the pay. Most of that spending went to equipment. All because of how Gates worked.

*Gear that isn’t imbued with mana falls apart in no time.*

So the most common method was to craft equipment from Magic Gems taken from Gate monsters.

The higher the Grade of Magic Gem used, the more the price shot through the roof.

“Seven years? Good grief. No matter how much you like money, you have to spend it when you need to. You going to pinch pennies with your life on the line?”

“Hmm. I had my reasons.”

Reasons I didn’t particularly want to talk about. Im Kkeokjeong’s voice was worried.

“You’ll be in a noncombat position today, so you should be fine… but be careful.”

“Yes.”

Even as I answered, I felt strange. Someone who’d had “be careful” on their lips constantly until just recently came to mind.

But the sentimentality didn’t last.

“Is everyone ready?”

When Team Leader Choi appeared, my jaw dropped.

*No way.*

“Is that a Red Drake leather set?”

“Hmm.”

Team Leader Choi’s face hardened. I’d only ever seen gear like that in luxury-store catalogs, so the words slipped out before I could stop them.

“Ah, sorry…”

“It’s nothing. It’s only made with five types of magic and B-grade Magic Gems.”

“…”

“I’m not emphasizing it, but the materials are five types of magic and B-grade Magic Gems.”

“Ah. Right.”

“Red Drake leather is popular because of its distinctive sheen, but that’s all for show. It isn’t actually that useful.”

Team Leader Choi moved, his face still stiff. A faint red glow flashed across him.

“But it is very beautiful.”

“…”

“Let’s head downstairs.”

Team Leader Choi left the waiting room first. Im Kkeokjeong came over.

“That guy really loves it when people recognize his equipment.”

“I mean, I get it, but… why is he like that?”

“No idea. He’s an equipment nut. There’s even a rumor he blew his entire fortune on that set and sleeps in it every night.”

*So this guy’s a nutjob too.*

I sighed inwardly and hoped today’s raid would end in one piece.

* * *

“This isn’t the number of people you registered.”

The civil servant looked uncomfortable. Fair enough. We were supposed to enter soon, and the party still wasn’t all there.

*How long are we going to have to wait?*

Six people had gathered in front of the Gate. Barring me, the porter, there were only five combatants.

It was an E-rank Gate, so you needed at least five more Hunters of the same rank… and with those Peace Guild bastards nowhere in sight, of course the civil servant was pissed.

“If additional personnel have been added, you need to inform us in advance.”

*Huh? What did he just say?*

Additional personnel?

“I’m sorry.”

At Team Leader Choi’s curt apology, the civil servant picked up his pen and struck several lines through the paperwork.

“We can just amend it, so it’s not a major problem… but please be careful next time.”

“Yes.”

*Not a major problem, my ass. There aren’t any people!*

I poked Im Kkeokjeong in the ribs.

“Hyung. When are the others getting here?”

“What others?”

“The Peace Guild.”

“Team Leader Choi is here.”

“What?”

“Oh, did I not tell you? The Peace Guild is new, so it’s short on people. There are only three of us, including the Guild Master. Hahaha.”

…You’re laughing?

“Come on, hyung.”

“I know, punk. But you don’t have to worry.”

Im Kkeokjeong patted my shoulder and pointed at Team Leader Choi, who was signing the paperwork.

“That man’s a C-rank Hunter.”

“Oh. C-rank…”

I shut my mouth.

If Team Leader Choi was a C-rank Hunter, there was no problem. No—he was far better than ten E-rank Hunters. He was a mid-rank Hunter, in a completely different league from a low-rank Hunter like me.

*I should’ve realized the moment I saw him in that luxury gear.*

This was a man walking around with a high-end apartment wrapped around his body. A price most low-rank Hunters couldn’t afford even if they drained their entire fortunes ten times over.

A faint halo seemed to shine from Team Leader Choi’s back.

“Please verify the signature.”

Even the way he handed the pen back to the civil servant was elegant.

Even his smallest movements seemed to drip with class.

*So this is the dignity of a C-rank Hunter.*

*That’s fucking cool.*

I wanted to become sworn brothers with him. To swear a gay oath beneath the Gate—no, a Gate oath.

“All right, then. Let’s go in… What is it?”

Team Leader Choi looked at me, startled.

“No. I just thought you looked cool.”

“Excuse me?”

“The equipment. I said it looks cool.”

At that moment, the corner of Team Leader Choi’s mouth twitched.

“It’s nothing. It’s only made with five types of magic and B-grade Magic Gems…”

*A nutjob I wanted to get along with.*

* * *

I took a step toward the Gate.

Whoosh—

A familiar sensation wrapped around me. The cool, sticky energy unique to mana. Then the scenery flipped.

“It’s a cave.”

As Team Leader Choi said, this raid’s location was a cave. The walls were damp with moisture, and faint darkness lay over everything around us.

“Mr. Taekyung. Take out a flashlight.”

“Yes.”

I quickly set down my backpack. It was a porter’s bag Team Leader Choi had handed me just before we entered the Gate. It looked ordinary on the outside, but it was an expensive item enchanted with both space expansion and weight-reduction magic.

“Here. A flashlight.”

I handed it over since he’d asked, but in my experience it wasn’t the best method. Convenient, sure, but if the light vanished, you couldn’t adapt to the sudden dark.

It was much better to wait a little and let your eyes get used to the darkness…

Click.

“Let there be light. Light.”

Whoosh. A ball of light the size of a soccer ball shot out of the flashlight and slapped itself against the cave ceiling.

“…Magic?”

“It’s built-in magic that activates as soon as you chant the spell. It lasts quite a long time, so three or four hours shouldn’t be a problem. It’s a limited edition I bought from Company M, but…”

Im Kkeokjeong, who had been watching, boiled it down to one line.

“It’s crazy expensive.”

Was Team Leader Choi’s face darkening a little just my imagination, or was it the shadows? Either way, the raid had gotten a lot easier thanks to it.

*Money really is the best.*

The world was ruled by capital, and Gates were no different. People with money fought easy with magic equipment; people without it had to carry torches.

“Take your positions.”

At Team Leader Choi’s command, everyone moved at once. Im Kkeokjeong and another E-rank Hunter took the lead as tanks, with Team Leader Choi behind them. I, the porter, and the two ranged dealers stood at the very back.

“Move.”

We started advancing slowly.

The bright magic light lit the path ahead.

“…”

*I want one.*

* * *

“Kiiiieet!”

The creatures that had been crouched in the darkness showed themselves with shrill cries. Green skin. Short torsos. Limbs that looked grotesque.

They were Hobgoblins, a higher species of ordinary goblin.

*About thirty of them.*

With only five people, this would be a hard fight.

*But a C-rank Hunter changes the story.*

On top of that, the other four were veteran E-rank Hunters with at least ten-odd years of experience each.

I hung back and watched the fight.

“Ranged!”

The moment Team Leader Choi gave the order, arrows flew. One shot, one kill. The arrows punched into vital points, and the unshielded Hobgoblins dropped in heaps.

“Kiit!”

“Oof, shield-bearers. What should we do?”

“Hold.”

Team Leader Choi went on.

“Tanks, advance.”

The tanks in thick full-body armor moved forward with their tower shields. Im Kkeokjeong and the other man were both huge, over 190 centimeters, so the intimidation factor was no joke.

“Kiiiieet!”

But monsters were monsters for a reason. Trusting in their numbers, the Hobgoblins charged like a swarm of bees.

But then—

“Well now.”

Bam!

They turned to bloody pulp against those big, beautiful tower shields and went flying. Riding that momentum, Im Kkeokjeong swung his mace like a flyswatter, wrecking limbs and smashing heads.

“You punk! You punk!”

…What was this, whack-a-mole?

*Old-timers, as expected.*

All four of them kept to their roles without overdoing it, steadily cutting the enemy numbers down.

Knowing when to fall back and when to push in was combat intelligence born of plenty of experience.

“Everyone, hold your positions.”

And then one man.

The man who had been directing the flow of battle until now moved.

“I’ll handle the rest.”

At the same time, a red line flashing along his armor plunged through the twenty Hobgoblins.

Slash—

A head sprang into the air along a clean arc. The monsters couldn’t react in time to something that happened so fast.

“Kiiie?”

Slash. Slash. Slash.

The blade did not stop. Merciless and efficient, it pierced and cut through vital points. This was no longer a battle.

It was a massacre. A massacre of some twenty monsters by a single human.

*This is a C-rank Hunter.*

I could see his speed, his strength. All of it. And I felt it.

*He really is strong.*

As a mere F-rank, I couldn’t even dream of matching him. He was a mid-rank Hunter three full stages above me. A wide river and a high wall that effort alone could never bridge.

But at the same time, a question surfaced.

*What if this were Murim?*

Team Leader Choi was definitely strong. He had the ability befitting a C-rank Hunter, and plenty of experience.

But if this were Murim… if he were a man of Murim…

*I’d be stronger.*

His movements were fast and powerful, but that was all. He hadn’t learned martial arts, and he didn’t use mana efficiently either.

At best, he was first-rate. In Murim, that was exactly where he would stand.

*But this is reality.*

I bit my lip without realizing it.

A mid-rank Hunter and the lowest-rank Hunter.

While the mid-rank Hunter wore expensive equipment and slaughtered monsters, the lowest-rank Hunter could only stare blankly.

In the role of a porter.

“Kiiieet…”

The last Hobgoblin fell. Team Leader Choi pulled his sword from its chest, and our eyes met.

“Mr. Taekyung. Please handle the byproducts.”

“…”

“Mr. Taekyung?”

I wanted to tell him I was stronger than he was.

But in the end I couldn’t. This was my reality.

“…Thank you for your hard work.”

I *used to be* stronger than you.

[^1]: Dongdaemun is Seoul’s major wholesale-market district.
```
## Chapter 43

### Korean source

```text
＃43화



스윽.

날카롭게 벼린 단검이 홉 고블린의 시체를 파고들었다.

체액이 튀고 고약한 냄새가 풍겼지만 손을 멈추지 않았다. 머리는 버리고, 등과 뱃가죽을 깔끔하게 도려낸 뒤 차곡차곡 쌓았다.

“솜씨가 좋으시군요.”

“……감사합니다.”

최 팀장이다. 그의 호의 어린 목소리에 나는 죄책감을 느꼈다. 이런 사람을 상대로 그런 유치한 질투를 하다니.

더군다나 이미 잊기로 마음먹은 허상까지 끄집어내서.

‘사춘기도 아니고.’

결국 얼굴이 벌겋게 달아오른 채로 작업을 끝마쳤다.

10분 남짓이니 사체 한 구당 20초쯤 걸렸나? 빠른 속도에 슬쩍 다가온 임꺽정도 입을 벌렸다.

“이야, 넌 밥 먹고 이것만 했냐?”

“이 정도 하는 사람 많아요.”

“많기는 무슨. 완전 전문가구만.”

음. 살짝 뿌듯한데.

앞에서 약간 겸손을 떨긴 했는데, 사실 임꺽정의 말대로 이 정도 속도를 내면서 깔끔하게 도축할 수 있는 헌터들은 많지 않다.

“제가 손이 빠른 편이라.”

학창 시절 공장 알바에, 인형 눈깔 붙이기까지 섭렵했던 나다. 어떻게 보면 헌터 일보다 먼저 시작한 게 이거란 말이지.

“레이드 뛰면서도 계속했고요.”

“아예 이쪽으로 방향을 튼 거야?”

“아뇨. 그냥 병행했는데요. 투잡.”

“투잡이요?”

가만히 대화를 듣고 있던 최 팀장이 불쑥 끼어들었다.

“어, 네.”

“정확히 어떤?”

“그냥 전투 끝나고 휴식 시간 쪼개서 작업하는 거죠.”

“수당을 더 받습니까?”

“그럼요. 그것도 일인데.”

“그렇게 얼마나 하셨습니까?”

“계속했는데요. 처음부터 지금까지 쭉.”

임꺽정이 혀를 내둘렀다.

“독한 놈. 난 그거 못 하겠던데.”

“하다 보면 괜찮아져요. 체력 기르는 데 도움도 되고.”

“목숨이 왔다 갔다 하는데 체력을 길러? 으하하. 최 팀장님, 내가 말했죠? 태경이 이 녀석처럼 악착같이 하는 놈 없을 거라고.”

그런 말을 했어?

“흠.”

최 팀장은 대답 대신 물끄러미 나를 바라보더니 이내 돌아섰다.

“작업도 끝났으니 다시 출발할까요?”

저 반응은 뭘까. 어리둥절한 내게 임꺽정은 알 수 없는 웃음을 흘렸다.

“열심히 해.”

아니, 뭔데?



* * *



레이드는 순조롭게 진행됐다. 오랫동안 손발을 맞춰서 이제는 한 몸처럼 움직이는 E급 헌터들이 몬스터의 머릿수를 줄이면 최 팀장이 바통을 넘겨받았다.

촤악-

한 번 검을 휘두를 때마다 어김없이 터져 나오는 피 분수.

나는 코앞에서 벌어지는 전투를 빠짐없이 눈에 담았다.

‘확실히 잘 싸우긴 하네.’

물론 자꾸 무림에 대한 생각이 드는 건 어쩔 수 없다.

새벽마다 시민 공원에서 연습하는 춤 같은 동작이 아닌, 진짜 무공(武功)을 내 눈으로 직접 보고 익히기까지 했으니까.

‘……어?’

설마, 에이. 그래도 혹시?

말도 안 되는 소리지만. 설마 그럴 리야 없겠지만 한 번 시도해 보는 거다.

‘안 되겠지, 안 되겠지…… 됐으면 좋겠다.’

조심스럽게 발을 떼려던 그 순간이었다.

“태경 씨. 정리 부탁드립니다.”

최 팀장의 목소리에 순간 정신이 확 든다. 내가 단단히 미쳤구나. 레이드 중에 한눈을 팔다니.

‘정신 차리자.’

나중에 뭘 하든 당장은 레이드가 최우선이다.

그게 같은 팀원들에게 보이는 예의고, 내 명줄을 튼튼하게 만들어 줄 신념이다.

“예. 갑니다!”

나는 바람처럼 달려가 사체를 분해하기 시작했다.

최 팀장과 임꺽정은 힘들지도 않은지 휴식 시간 내내 주변을 얼쩡거렸다.

‘드럽게 신경 쓰이네.’



* * *



임꺽정은 다음 휴식 때도 어김없이 찾아왔다.

“태경아. 너 창 잡은 지 얼마나 됐지?”

“7년이요.”

“이야, 그 정도면 아주 달인이네, 달인.”

“……?”

그다음 휴식 때도.

“태경아. 너 훈련소 수석이었다고 했나?”

“네. 근데 F급 중에서만 수석이라 큰 의미는 없어요.”

“인마. 그게 대단한 거지. 나는 꼴등으로 수료했어.”

“……형님도 대단하시네요. 그런데 저 작업 좀.”

“아, 그래.”

그리고 다음, 다음, 다음 휴식 시간에도.

“태경아. 태경아. 태경아.”

“형님. 달팽이관이 찢어진 것 같아요.”

“너 전에 있던 길드에서 몇 년 동안 일했다고 했지?”

“아.”

지금이라도 마법사로 갈아타고 싶다. 저 인간 입에 침묵 마법 걸어 버리게.

‘미치겠네.’

방법은 하나밖에 없다. 정말 귀에서 피가 흐르기 전에 이 작업을 끝내는 것. 나는 이를 악물고 손을 놀렸다.

서걱, 서걱, 서걱.

“태경아.”

살려 줘.

근처에 앉아 있던 최 팀장에게 구조 신호를 보냈지만 그는 슬쩍 자리를 뜨는 것으로 대답을 대신했다.



* * *



“작업 끝났습니다.”

나는 처음보다 묵직해진 가방을 메고 일어섰다. 홉 고블린은 아낌없이 주는 몬스터였다. 독 저항 성질을 띤 가죽과 쓸 만한 무기 몇 개. 그리고 E급 마정석도 두 개나 떨궜다.

‘가죽 상태도 좋고, 마정석도 두 개. 이거 돈 좀 되겠는데.’

아무래도 기여도가 가장 높은 최 팀장이 절반가량을 가져가겠지만 인원이 적으니 다른 팀원들에게도 남는 장사다.

아, 물론 나는 제외. 계약서에 따르면 기본급 30만 원이 내가 받는 전부니까.

‘기분 좋으면 좀 더 챙겨 주겠지. 뭐.’

최 팀장은 꽤 후한 고용주다. 까마득한 C급 헌터면서 꼬박꼬박 존대해 주고, 성격이 좀 특이해서 그렇지 이 바닥에서 저 정도면 인격자다.

‘그리고 믿을 수 있는 실력자고.’

덕분에 안정적이고 빠른 속도로 여기까지 올 수 있었다.

이제 남은 건 게이트의 마지막. 보스 존(Boss zone).

눈앞의 이 석문을 열면 이 게이트의 보스 몬스터와 우리를 밖으로 내보내 줄 마력장이 기다리고 있을 것이다.

“어이고, 열심히 움직였더니 배고프네.”

“후딱 끝내고 나가서 국밥이나 먹자고. 태경아, 너도 올 거지? 그리고 최 팀장님도.”

“전 괜찮습니다. 따로 초밥 시켜 먹게요.”

“…….”

보스 존을 앞에 두고 밥 얘기라니. 그 와중에 혼자 초밥 시켜 먹겠다는 인간까지 있다.

‘이렇게 여유로워도 되는 건가.’

물론 내가 할 소리는 아니다. 짐꾼에 중간중간 도축하는 것만으로도 하루 일당을 벌었으니까.

새 길드에 취직할 때까지 최 팀장이 자주 불러 줬으면 소원이 없겠다. 이런 꿀 알바라면 백 번도 더 할 수 있으니까.

“어떻게, 이제 슬슬 들어갈까요?”

“네.”

최 팀장의 대답에 임꺽정이 타워 실드로 석재 문을 후려쳤다.

콰앙-!

문이 터져 나가면서 돌가루와 먼지가 쏟아진다. 나는 팀원들을 따라 보스 존으로 진입했다.

그리고 그곳에…….

- 케룩.

놈이 있었다.

‘주술사?’

놈을 본 순간 처음으로 떠올린 단어다.

알 수 없는 문양이 그려진 로브. 한 손에는 말라비틀어진 지팡이를, 다른 한 손에는 예리한 단검을 든 늙은 홉 고블린.

- 카륵. 취. 악토.

석문이 부서지면서 큰 소리가 났음에도 아랑곳하지 않고 뭔가를 중얼거린다. 한 음절이 끝날 때마다 주변에 널브러진 시체들 위로 검은 기운이 피어올랐다.

‘잠깐. 시체라고?’

제대로 본 게 맞다. 제단 위에는 백 마리에 달하는 홉 고블린들이 죽어 있었다. 자세히 보니 원래대로라면 보스 존에서 우리가 상대해야 할 녀석들이다.

‘이게 도대체 무슨.’

처음 겪는 상황에 나를 포함한 모두가 굳어 있을 때, 최 팀장이 벼락처럼 외쳤다.

“밖으로 나가요. 당장!”

정체를 알 수 없는 늙은 홉 고블린이 고개를 돌린 것도 그때였다. 쩔그럭. 놈의 지팡이가 가볍게 흔들렸다.

- 미타. 알로.

공기가 부르르 떨렸다. 마법의 발현이다.

“방패 뒤로!”

탱커들이 황급히 타워 실드를 들어 올렸다. 하지만 그건 잘못된 판단이었다. 놈이 사용한 건 공격 마법이 아니었으니까.

쿵. 쿵. 쿵!

“뒤다! 통로가 막히고 있다!”

“뛰어, 빨리!”

젠장. 늦었다.

시계를 거꾸로 돌린 것처럼 박살 났던 석문이 멀쩡하게 복구되어 있었다. 변화는 거기에서 끝나지 않았다.

바닥에 널려 있던 돌무더기가 이중, 삼중의 벽을 쌓았고 동굴 벽면의 넝쿨이 그 위를 단단히 묶었다.

“모두 비켜!”

임꺽정이다. 근력 강화 스킬을 썼는지 전신의 근육이 터질 듯 부풀어 오른 그가 타워 실드를 들고 석문을 향해 돌진했다.

“흐아아압!”

쾅! 쩌저적!

“……염병할.”

임꺽정이 망연자실한 얼굴로 금이 잔뜩 간 타워 실드를 떨어트렸다. E급 헌터가 스킬까지 썼는데 뚫기는커녕 방패만 망가졌다.

‘강화 마법?’

그게 뭐건 간에 하나는 확실하다.

이 정도 마법을 구사하는 저 늙은 홉 고블린은 최소 한두 단계 위의 몬스터라는 것.

그리고…….

쉬쉭!

우리 중에 저놈을 상대할 사람이 존재한다는 것.

‘도대체 언제?’

최 팀장은 이미 놈을 향해 쇄도하고 있었다. 마치 통로가 뚫리지 않을 거라는 사실을 확신하고 있던 사람처럼.

“바람이 깃든다. 헤이스트.”

그의 신형이 쭉 미끄러진다. 백 미터가 넘는 거리가 순식간에 좁혀졌다. 다섯 걸음을 남겨 두고 최 팀장의 허리춤에서 검이 뽑혀 나왔다.

쐐애액!

C급 헌터가 전력을 다한 공격. 그러나 늙은 홉 고블린은 비릿하게 웃어 보였다.

- 카륵. 취. 악토.

변화는 순식간에 일어났다.

쏴아아아.

제단 위에 널브러져 있던 백여 구의 시체가 쪼그라들더니 모래처럼 흩어진다. 그렇게 완전히 뽑혀 나온 검은 기운이 한데 뭉쳐 최 팀장의 옆구리를 후려쳤다.

퍼억!

“큭.”

빠르게 튕겨 나온 최 팀장이 일그러진 얼굴로 말했다.

“막아야 합니다. 지금 당장.”

“……저걸요?”

이미 늦었다.

불과 몇 초 전만 하더라도 유형화된 기운에 불과하던 그것은 빠르게 제 형태를 갖추고 있었다.

3m에 달하는 거구. 터질 것 같은 근육과 어마 무시한 크기의 대검을 든 괴물로.

“저게 뭐야…….”

누군가 넋 나간 목소리로 중얼거렸다. 나와 마찬가지로 이들도 처음 보는 기현상이 틀림없다.

최 팀장만이 유일하게 놈들의 정체를 알고 있었다.

“홉 고블린 대전사. C급 레어 몬스터(Rare Monster)죠.”

저 덩치가 홉 고블린이라는 사실도 충격적이지만 뒤에 붙은 말에 비하면 아무것도 아니다.

‘C급 레어 몬스터라고?’

시발, 그게 여기서 왜 튀어나와?

레어 몬스터는 해당 게이트에서 드문 확률로 출현하는 희귀 몬스터다. 게다가 저 대전사라는 놈은 C급이니 나와 다른 팀원들은 평생 마주칠 일도 없는 존재였다.

……물론 이젠 아니지만.

“저놈이랑 싸우라고요?”

“저놈들, 이죠.”

최 팀장이 늙은 홉 고블린을 가리켰다.

“홉 고블린 제사장. 역시 C급 레어 몬스터입니다.”

“아, 씨바…….”

나도 모르게 욕이 튀어나온다. 임꺽정이 굳은 얼굴로 물었다.

“승산은? 냉정하게 판단해 주쇼.”

“제사장을 먼저 처리한다면 희망이 있습니다. 그 대신…….”

쿵. 쿵.

최 팀장의 말이 뚝 끊겼다. 대전사가 우리를 향해 다가오고 있었다. 한 걸음, 한 걸음. 동굴 바닥이 진동했다.

“잠시만 저놈을 묶어 놔야 합니다.”

누가?

“우리가요?”

“아뇨. 여러분들이.”

“쿠워어어어!”

대전사의 포효에 동굴 천장에 매달려 있던 종유석이 뚝 떨어졌다. 최 팀장은 지금껏 본 적 없는 결연한 얼굴로 돌아섰다.

“바람이 깃든다. 헤이스트.”

야, 이 새끼야.
```

### Current accepted English

```markdown
# Chapter 43

Swish.

A sharpened dagger dug into a Hobgoblin corpse.

Fluids splattered, and a foul stench filled the air, but I didn’t stop. I discarded the heads, neatly cut away the hides from their backs and bellies, and stacked them in a pile.

“You’re quite skilled.”

“…Thank you.”

It was Team Leader Choi. His kindly voice made me feel guilty. Getting jealous of someone like him—how childish was that?

Especially after dragging up an illusion I’d already decided to forget.

*It’s not like I’m going through puberty.*

I finished the job with my face burning red.

A little over ten minutes, so about twenty seconds per corpse? Even Im Kkeokjeong sidled over, drawn by the speed, and his mouth fell open.

“Damn, have you been doing nothing but this?”

“Plenty of people can do this much.”

“Plenty, my ass. You’re a total professional.”

Hmm. That made me a little proud.

I’d played modest a second ago, but Im Kkeokjeong was right. There weren’t many Hunters who could butcher this cleanly at this speed.

“I’m just fast with my hands.”

I’d done factory part-time jobs in school. I’d even stuck eyes on dolls. In a way, I’d started this before I ever worked as a Hunter.

“I kept doing it during raids, too.”

“You switched over to this completely?”

“No. I just did both. A side job.”

“A side job?”

Team Leader Choi, who’d been listening quietly, cut in.

“Oh, yes.”

“Exactly what kind?”

“I just split the rest time after combat to do the work.”

“Do you receive additional pay?”

“Of course. It’s work, too.”

“How long have you been doing it?”

“I’ve kept at it. From the beginning until now.”

Im Kkeokjeong was floored.

“You hardcore bastard. I couldn’t do that.”

“You get used to it. It helps build stamina, too.”

“Your life’s on the line, and you’re building stamina? Hahaha. Team Leader Choi, didn’t I tell you? There’s nobody who works as relentlessly as this kid.”

*Did you say that?*

“Hm.”

Instead of answering, Team Leader Choi studied me for a moment, then turned away.

“The work’s done, so shall we get moving again?”

What was that reaction supposed to mean? While I stood there bewildered, Im Kkeokjeong gave me an unreadable smile.

“Keep working hard.”

*No, what?*

* * *

The raid went smoothly. The E-rank Hunters had been in sync so long they moved as one. Once they cut the monsters’ numbers down, Team Leader Choi took over.

Slash—

Every swing of his sword sent up a fountain of blood.

I took in every second of the fight unfolding right in front of me.

*He really can fight.*

Of course, I couldn’t help thinking about Murim.

I’d seen real martial arts with my own eyes—and even learned them. Not the dance-like moves I practiced in the city park at dawn.

*…Huh?*

*No way. Still, maybe?*

It was ridiculous. There was no way it would work, but I was going to try once.

*It won’t work. It won’t… But it’d be nice if it did.*

That was the moment I was about to take a careful step.

“Mr. Taekyung. Please handle the cleanup.”

Team Leader Choi’s voice snapped me straight back.

*I’ve completely lost it.* Getting distracted in the middle of a raid.

*Get a grip.*

Whatever I wanted to do later, the raid came first.

That was courtesy to my teammates—and the conviction that would keep me alive.

“Yes. I’m coming!”

I ran over like the wind and started taking the corpses apart.

Team Leader Choi and Im Kkeokjeong loitered nearby the whole rest period, like they weren’t tired at all.

*It’s seriously getting on my nerves.*

* * *

Im Kkeokjeong came over again at the next break, without fail.

“Taekyung. How long have you been using a spear?”

“Seven years.”

“Wow. At that point, you’re pretty much a master. A real master.”

“…?”

The break after that, too.

“Taekyung. You said you were top of your training class, right?”

“Yes. But I was only first among the F-ranks, so it doesn’t mean much.”

“You punk. That’s what makes it impressive. I finished dead last.”

“You’re impressive too, hyung. But I have some work to do.”

“Oh, right.”

And then the next break. And the one after that. And the one after that.

“Taekyung. Taekyung. Taekyung.”

“Hyung. I think my cochlea’s been torn open.”

“You said you worked at your previous Guild for several years, right?”

“Ah.”

I wanted to switch to a mage right then and there, just so I could put a silence spell on that man’s mouth.

*This is driving me crazy.*

There was only one way out. Finish the work before blood really started pouring from my ears. I clenched my teeth and kept my hands moving.

Slice. Slice. Slice.

“Taekyung.”

*Save me.*

I sent a distress signal to Team Leader Choi, who was sitting nearby, but he answered by quietly slipping away.

* * *

“The work’s done.”

I stood up with the bag on my back, heavier than before. Hobgoblins were generous monsters. Poison-resistant hides, a few usable weapons—and they even dropped two E-grade Magic Gems.

*The hides are in good condition, and there are two Magic Gems. This could be worth a decent amount.*

Team Leader Choi had contributed the most, so he’d probably take about half. But with so few people, it was still a profitable deal for the other team members.

Not me, of course. According to the contract, the 300,000-won base pay was all I would get.

*If he’s in a good mood, maybe he’ll throw me a little extra.*

Team Leader Choi was a fairly generous employer. He was a C-rank Hunter way out of my league, yet he always treated me with respect. His personality was a little unusual, but in this line of work, that made him a decent human being.

*And a skilled Hunter I can trust.*

Thanks to him, we’d made it this far at a steady, rapid pace.

All that remained was the last stretch of the Gate.

The Boss Zone.

If we opened the stone gate in front of us, the Gate’s boss monster and the mana field that would send us outside should be waiting beyond it.

“Man, all that moving around made me hungry.”

“Let’s finish this quick and go out for some gukbap.[^1] Taekyung, you’re coming too, right? And you too, Team Leader Choi.”

“I’m fine. I’ll order sushi separately.”

“…”

Talking about food with the Boss Zone right in front of us. And on top of that, there was a guy planning to order sushi by himself.

*Is it really okay to be this relaxed?*

Of course, I had no right to say that. Just portering and butchering in between had already earned me a day’s pay.

Until I landed a job at a new Guild, if Team Leader Choi kept calling me, I wouldn’t have anything left to wish for. A sweet gig like this? I could do it a hundred times over.

“Well, shall we head in?”

“Yes.”

At Team Leader Choi’s answer, Im Kkeokjeong slammed his tower shield into the stone gate.

Boom!

The gate blew apart, and stone dust and dirt poured down. I followed the others into the Boss Zone.

And there…

—Keuruk.

It was there.

*A shaman?*

That was the first word that came to mind when I saw it.

An old Hobgoblin in robes marked with unreadable patterns. A withered staff in one hand, a sharp dagger in the other.

—Karruk. Chwi. Akto.

Despite the loud crash when the stone gate broke, it went on muttering, unfazed. Each time a syllable ended, black energy rose from the corpses scattered around it.

*Wait. Corpses?*

I’d seen it right. Nearly a hundred Hobgoblins lay dead on the altar. Looking closer, they were the ones we were supposed to fight in the Boss Zone.

*What the hell is this?*

While all of us froze at a situation none of us had ever seen, Team Leader Choi shouted like a thunderclap.

“Get outside. Now!”

That was when the unknown old Hobgoblin turned its head.

Clink.

Its staff shook lightly.

—Mita. Allo.

The air shuddered.

Magic was taking form.

“Behind the shields!”

The tanks hurriedly raised their tower shields. But that was the wrong call. What it had used wasn’t an attack spell.

Boom. Boom. Boom!

“It’s behind us! The passage is being blocked!”

“Run! Hurry!”

*Damn it. Too late.*

As if the clock had been turned back, the shattered stone gate stood intact again.

And the changes didn’t stop there.

The rubble on the floor had stacked into double and triple walls, and vines from the cave walls bound them tight.

“Everyone, out of the way!”

It was Im Kkeokjeong. His muscles had swollen like they were about to burst—probably a Strength Enhancement Skill. Tower shield in hand, he charged the stone gate.

“Haaah!”

Bang! Crack!

“…Goddamn it.”

Im Kkeokjeong dropped the tower shield, his face blank with disbelief. An E-rank Hunter had even used a Skill, and he hadn’t broken through. He’d only wrecked his shield.

*Enhancement magic?*

Whatever it was, one thing was certain.

That old Hobgoblin, using magic like this, was a monster at least one or two stages above us.

And…

Swish!

There was someone among us who could face it.

*When did he—?*

Team Leader Choi was already charging the thing, as if he’d been sure the passage wouldn’t break.

“The wind takes hold. Haste.”

His body slid forward. More than a hundred meters vanished in an instant. With five paces left, the sword came free from Team Leader Choi’s waist.

Whoosh!

A C-rank Hunter’s full-power attack.

The old Hobgoblin only smirked.

—Karruk. Chwi. Akto.

The change happened in an instant.

Whoosh—

The hundred-odd corpses scattered across the altar shriveled, then dispersed like sand. The black energy, fully pulled out of them, gathered into one mass and smashed into Team Leader Choi’s side.

Thud!

“Ghk.”

Team Leader Choi bounced back fast. With a twisted face, he said,

“We have to stop it. Right now.”

“…That?”

It was already too late.

Only a few seconds ago, it had been nothing more than energy given form. Now it was rapidly taking shape.

A hulking frame nearly three meters tall. A monster with muscles ready to burst, holding a greatsword of terrifying size.

“What the hell is that…?”

Someone muttered in a dazed voice. Just like me, this had to be the first time they were seeing anything like it.

Only Team Leader Choi knew what they were.

“Hobgoblin Great Warrior. A C-rank Rare Monster.”

The fact that something that size was a Hobgoblin was shocking enough. Next to what came after, it was nothing.

*C-rank Rare Monster?*

*Fuck, why is that thing showing up here?*

Rare Monsters were rare monsters that appeared in a given Gate only at a low rate. And that Great Warrior was C-rank—something the rest of us would never have run into in our lives.

…Of course, not anymore.

“You want us to fight that thing?”

“Those things.”

Team Leader Choi pointed at the old Hobgoblin.

“Hobgoblin Priest. Also a C-rank Rare Monster.”

“Ah, fuck…”

The curse slipped out before I could stop it. Im Kkeokjeong asked with a stiff face,

“What are our chances? Give it to me straight.”

“If we take out the Priest first, there’s hope. In exchange…”

Boom. Boom.

Team Leader Choi’s words cut off.

The Great Warrior was coming toward us.

One step. Then another.

The cave floor shook.

“We need to hold that thing down for a little while.”

*Who?*

“Us?”

“No. All of you.”

“Kuwooooh!”

The Great Warrior’s roar sent a stalactite dropping from the cave ceiling.

Team Leader Choi turned with a resolute look I’d never seen on him before.

“The wind takes hold. Haste.”

*Hey, you bastard.*

[^1]: Gukbap is a Korean dish of soup served with rice.
```
