# Retrospective Patch Plan — Chapters 34–38

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
  "summary": "14 findings in chapters 34-38",
  "findings": [
    {
      "chapter": 34,
      "confidence": 1.0,
      "current": "— Your Sinews and Bones and your Meridians improve greatly!",
      "defect": "The translation conflates and misnames two distinct System attributes: 근골 is Muscles and Bones, while 근맥 is Sinews and Meridians.",
      "id": "R0034-01",
      "rationale": "The source explicitly raises two separate attributes, both of which have established glossary renderings.",
      "replacement": "— Your Muscles and Bones and your Sinews and Meridians improve greatly!",
      "severity": "major",
      "source": "- 근골과 근맥이 크게 향상됩니다!"
    },
    {
      "chapter": 34,
      "confidence": 1.0,
      "current": "“Guo of the Three Paths Sect presents his respects.”[^1]",
      "defect": "Both the surname and sect name conflict with established terminology. 곽 is Gwak, and 삼도문 is the Samdo Sect.",
      "id": "R0034-02",
      "rationale": "The speaker is Gwak Jun, and the supplied glossary mandates Samdo Sect. The current Chinese-style surname rendering also breaks continuity with his later introduction.",
      "replacement": "“Gwak of the Samdo Sect presents his respects.”[^1]",
      "severity": "major",
      "source": "“삼도문(三道問)의 곽 모가 인사 올립니다.”"
    },
    {
      "chapter": 35,
      "confidence": 1.0,
      "current": "**Fire Divine Elixir**",
      "defect": "The named item is rendered with a different, generic name instead of its established title.",
      "id": "R0035-01",
      "rationale": "열화신단 has the exact glossary rendering Blazing Flame Divine Pill.",
      "replacement": "**Blazing Flame Divine Pill**",
      "severity": "major",
      "source": "[열화신단]"
    },
    {
      "chapter": 36,
      "confidence": 0.99,
      "current": "I started counting again from the end, one person at a time. Not counting me, there were eight. Han Yeop had serious injuries, so he obviously couldn’t have come—but Hyuk Mujin had snuck out to join us.\n\n“…What are you doing here?”",
      "defect": "The translation replaces Taekyung’s calculation with the answer before he identifies Hyuk Mujin. It omits that the original squad had nine members besides Taekyung, that both Hyuk Mujin and Han Yeop should be absent, and that only seven should therefore be present.",
      "id": "R0036-01",
      "rationale": "The source builds the reveal through a numerical discrepancy. Naming Hyuk Mujin before Taekyung recognizes him removes that mechanism and prematurely resolves the surprise.",
      "replacement": "I started counting again from the end, one person at a time. There had originally been nine of them, excluding me. Hyuk Mujin and Han Yeop were both seriously injured, so neither should have been here. That meant there should have been seven, but…\n\n“…What are you doing here?”",
      "severity": "major",
      "source": "나는 끝에서부터 한 명씩 다시 세기 시작했다. 일단 나를 제외하고 아홉 명. 거기에 혁무진과 한엽은 중상이니까 당연히 오지 못했을 테니 일곱이 되어야 하는데…….\n\n“……너 여기서 뭐 하냐?”"
    },
    {
      "chapter": 36,
      "confidence": 1.0,
      "current": "More than five hundred martial artists stood in formation across the main training ground.",
      "defect": "The established location name is replaced by a generic description.",
      "id": "R0036-02",
      "rationale": "대연무장 has the exact glossary rendering Grand Training Ground.",
      "replacement": "More than five hundred martial artists stood in formation across the Grand Training Ground.",
      "severity": "minor",
      "source": "대연무장에 도열한 무사들의 숫자는 오백이 넘어갔다."
    },
    {
      "chapter": 36,
      "confidence": 1.0,
      "current": "“Squad Leader!”",
      "defect": "Hyuk Mujin’s established form of address is changed from Captain to Squad Leader.",
      "id": "R0036-03",
      "rationale": "The glossary explicitly establishes 조장 as Captain when Hyuk Mujin addresses Taekyung, making this a hierarchy and address inconsistency.",
      "replacement": "“Captain!”",
      "severity": "major",
      "source": "“조장님!”"
    },
    {
      "chapter": 37,
      "confidence": 1.0,
      "current": "“I’m Gwak Jun of the Three Paths Sect. We met once before… We even shook hands.”",
      "defect": "The established sect name is mistranslated.",
      "id": "R0037-01",
      "rationale": "삼도문 has the exact glossary rendering Samdo Sect, and the organization is central to the ensuing betrayal.",
      "replacement": "“I’m Gwak Jun of the Samdo Sect. We met once before… We even shook hands.”",
      "severity": "major",
      "source": "“삼도문의 곽준이라 합니다. 일전에 한 번 인사를 드렸었는데…… 손도 잡았었죠.”"
    },
    {
      "chapter": 37,
      "confidence": 0.99,
      "current": "“The manual’s a Supreme Peak martial art, and if you absorb the elixir right, it’s thirty years.”",
      "defect": "The source’s traditional unit 반 갑자 is converted to a modern year count despite the established glossary term.",
      "id": "R0037-02",
      "rationale": "The source says half a 갑자, and the glossary requires jiazi. Although equivalent to thirty years, replacing the unit erases the Murim register.",
      "replacement": "“The manual’s a Supreme Peak martial art, and if you absorb the elixir right, it’s half a jiazi.”",
      "severity": "minor",
      "source": "“비급은 초절정 무공이고, 영단은 잘만 흡수하면 반 갑자.”"
    },
    {
      "chapter": 37,
      "confidence": 1.0,
      "current": "“Of course. You’re the Sleeping Dragon.”",
      "defect": "Taekyung’s established epithet is changed.",
      "id": "R0037-03",
      "rationale": "잠룡 has the exact glossary rendering Hidden Dragon.",
      "replacement": "“Of course. You’re the Hidden Dragon.”",
      "severity": "major",
      "source": "“그럼요. 잠룡이신데.”"
    },
    {
      "chapter": 38,
      "confidence": 1.0,
      "current": "“Squad Leader, please move your foot. It hurts.”",
      "defect": "Hyuk Mujin’s established address for Taekyung is mistranslated.",
      "id": "R0038-01",
      "rationale": "The glossary explicitly establishes 조장 as Captain in Hyuk Mujin’s dialogue.",
      "replacement": "“Captain, please move your foot. It hurts.”",
      "severity": "major",
      "source": "“조장. 발 좀 치워 주세요. 아파요.”"
    },
    {
      "chapter": 38,
      "confidence": 1.0,
      "current": "The eight said to be Jin Taekyung’s subordinates advanced slowly with their backs together, whether their leader was doing anything up ahead or not.",
      "defect": "The translation changes the number of Taekyung’s subordinates from nine to eight.",
      "id": "R0038-02",
      "rationale": "아홉 명 explicitly means nine people. This changes a concrete scene quantity and contradicts the squad composition established in the source.",
      "replacement": "The nine said to be Jin Taekyung’s subordinates advanced slowly with their backs together, whether their leader was doing anything up ahead or not.",
      "severity": "critical",
      "source": "진태경의 부하라는 아홉 명은 대장이 앞에서 뭘 하건 말건 서로 등을 맞대고 느릿느릿 전진했다."
    },
    {
      "chapter": 38,
      "confidence": 1.0,
      "current": "Of the ten or so subordinates caught in One Flash, he was the only one who even left a sound.",
      "defect": "The named spear technique is rendered with the wrong established name.",
      "id": "R0038-03",
      "rationale": "일섬 is the named technique One Annihilation in the supplied glossary.",
      "replacement": "Of the ten or so subordinates caught in One Annihilation, he was the only one who even left a sound.",
      "severity": "major",
      "source": "일섬에 휘말린 십여 명의 부하 중 목소리라도 남긴 이는 그가 유일했다."
    },
    {
      "chapter": 38,
      "confidence": 1.0,
      "current": "“One Flash. This thing is awesome.”",
      "defect": "The dialogue uses the wrong name for Taekyung’s established spear technique.",
      "id": "R0038-04",
      "rationale": "일섬 must remain One Annihilation wherever the technique is named.",
      "replacement": "“One Annihilation. This thing is awesome.”",
      "severity": "major",
      "source": "“일섬, 이거 끝내주네.”"
    },
    {
      "chapter": 38,
      "confidence": 1.0,
      "current": "“If you add the Three Paths Sect and Gunggwimun together, well over a hundred.”[^2]",
      "defect": "Both sect names conflict with the established glossary.",
      "id": "R0038-05",
      "rationale": "삼도문 and 궁귀문 have the exact established renderings Samdo Sect and Gunggui Sect. These identities matter directly to Taekyung’s calculation of the infiltrators’ strength.",
      "replacement": "“If you add the Samdo Sect and the Gunggui Sect together, well over a hundred.”",
      "severity": "major",
      "source": "“삼도문, 궁귀문을 합치면 백 명이 훌쩍 넘을 겁니다.”"
    }
  ]
}
```

## Chapter 34

### Korean source

```text
＃34화



언젠가 진호 형과 TV를 보면서 그런 대화를 나눴었다.



‘쟤가 걔지? 한성진.’

‘형이 한성진을 알아?’

‘모르는 게 이상한 거 아니냐. TV만 틀면 나오는 얼굴인데. 하도 많이 봐서 이제 한 가족 같다.’

‘말조심해. 그거 명예훼손이야.’

‘개새끼.’



화면에는 길쭉한 체형의 미남이 환하게 웃고 있었다. 수십 대의 카메라와 수많은 군중이 그의 움직임 하나하나에 반응했다. 플래시와 비명이 쉴 새 없이 터져 나온다.



‘쟤는 다 가졌네. A급 헌터면 걸어 다니는 중소기업 아니냐. 모델 비율에 연예인 얼굴까지 가진 건 너무 반칙인데. 몇 살이랬지?’

‘나랑 동갑일걸.’

‘……힘내라.’



무슨 직업이든 간에 잘 버는 놈, 못 버는 놈은 있다. 그리고 헌터만큼 그 격차가 심한 직업도 없다.



‘괜찮아, 인마. 너도 좀 기다리면 해 뜰 날이 있겠지.’

‘얼마나 기다려야 되는데?’

‘한 100년만 더 기다려 봐라. 다음 생에는 가능할 테니까.’



그때, 낄낄거리며 놀리던 진호 형에게 지금 내 모습을 보여 주고 싶다.

‘이 광경을 보면 무슨 표정을 지을까.’

한 걸음, 한 걸음을 옮길 때마다 수십 명의 사람이 우르르 움직인다. 남녀노소가 두루 섞인 태원진가의 NPC들이 반짝거리는 눈동자로 나를 바라보고 있었다.

‘유명인들은 항상 이런 기분인가.’

사람들의 주목. 우러러보는 눈빛들이 부담스러우면서도 살짝 즐겁다.

‘새로운 영웅을 기다린다!’라는 흔한 게임 홍보 멘트가 이해가 되는 순간이었다.

‘그래. 슬슬 마지막인데 즐겨 줘야지.’

웃음과 함께 손을 흔들자 함성이 터져 나온다. 그렇게 갈수록 불어나는 사람들을 끌고 도착한 곳은 회의실로 사용되는 대전이었다.

“기다리고 계십니다.”

무사의 얼굴이 낯이 익다. 지난번 이소군이 찾아왔을 때 나를 경멸의 시선으로 바라보던 무사였다.

‘한 보름 정도 지났나.’

그때의 내가 지금과 다르듯이, 무사도 마찬가지였다. 지극히 공손한 태도로 포권을 취한 무사가 문을 열어젖혔다.



* * *



대전은 내가 기억하는 모습 그대로였다. 커다란 탁자를 중앙에 두고 양옆으로 흐트러진 의자는 회의가 막 끝났다는 사실을 알려 주었다.

“왔느냐?”

상석에 앉아 있던 진위경이 피곤한 웃음을 지어 보였다. 넓은 대전에는 오직 그 혼자뿐이었다.

“위팽은요?”

“잠시 후에 돌아올 게다.”

자리에 앉자 진위경이 본론을 꺼냈다.

“하오문에서 연락이 왔다. 항산검문에서 닥치는 대로 병력을 끌어모으고 있다는구나.”

저쪽에서도 똥줄이 탄 모양이군.

나는 전쟁은 모르지만 전투는 안다. 그리고 전쟁은 전투가 모여 만들어진다. 이미 한 번의 대패로 많은 무사와 사기를 잃은 적들은 다음 전투에 총력을 기울일 것이다.

“힘든 싸움이 되겠군요.”

“일문(一門)의 금력을 모두 쏟아부었으니까. 증원군까지 혈랑검이 이끄는 본대에 합류한다면 일천을 헤아리겠지.”

“일천…….”

무지막지한 숫자다. 그런 대규모 전투는 경험해 본 적도 없고, 경험하고 싶지도 않다.

진위경이 굳은 얼굴로 말을 이었다.

“전 병력을 이끌고 북상. 증원군과 합류하기 전에 적들의 본대를 칠 계획이다.”

“그게 언제죠?”

“이틀 후.”

염병. 더럽게 빠르네. 시간 싸움은 태원진가와 항산검문 사이에서만 벌어지는 게 아니었다. 내게도 그랬다.

‘그때까지 로그아웃할 수 있을까?’

이틀 안에 일류가 된다면 로그아웃할 수 있다. 하지만 아니라면? 다시 한번 박 터지게 싸워야 한다.

‘그렇게 되면 완전히 나가린데.’

그때 진위경이 말했다.

“네가 후위를 맡았으면 좋겠구나.”

못 해. 안 해. 반사적으로 튀어나오려는 말을 겨우 삼켰다.

진위경의 얼굴이 그 어느 때보다 진지했기 때문이다.

“본가의 전부를 건 싸움이다. 네가 있는 것만으로도 사기가 크게 오를 거야.”

“…….”

이걸 받아들여야 하나, 고민하던 그때였다.

“다행히 산서오문(山西五門)이 우리를 돕기로 했다. 후위에서 그들 중 일부와 함께 움직여다오.”

“산서오문이라면?”

“다섯 개 중소 문파의 연맹이다. 본가와는 평소에도 좋은 인연을 맺고 있었지.”

“……그렇군요.”

“그럼 후위를 맡아 주겠느냐?”

띠링.



퀘스트



[후위 방어]

진위경은 당신에게 후위를 맡을 것을 제안했습니다.

이 임무를 수락한다면 무인들은 당신의 의지와 용기에 찬사를 보낼 것입니다.



종류 : 단기 퀘스트

등급 : 이류

제한 : 진태경

임무 : 제안 수락 (미완료)

보상 : 명성 10 상승

실패 : 명성 10 하락





더 생각할 것 없이 대답했다.

“하겠습니다.”

퀘스트 성공과 함께 명성이 상승했다는 메시지가 떴다.

거절 시 명성 하락이라니. 거절 못 할 제안을 하는 퀘스트창이 어이없었지만, 한편으로는 묘한 안도감이 퍼졌다.

‘안도감이라니. 정말 미친 건가.’

게임 중독이라며 자책하는 내게 진위경이 활짝 웃었다.

“네가 있어서 다행이다.”

웃는 얼굴이었지만 보이지 않는 그늘이 드리워져 있었다.

온종일 서류 더미에 파묻혀 생활하는 것으로도 모자라 이제는 전쟁까지 일어났다. 태원진가라는 거대한 가문을 통솔하는 것은 그에게도 무거운 짐일 것이다.

‘이틀 뒤라고 했지.’

한 지방을 양분하는 두 세력의 일대격돌이다. 무사의 숫자가 부족한 태원진가로서는 전력을 다해도 열세인 싸움이다.

‘이길 수 있을까?’

문득 드는 생각을 애써 털어 냈다. 죽든 살든 알 게 뭐냐. 출정은 이틀 뒤고 전투가 벌어지기까지는 또 며칠이 소요된다. 누가 이기건 간에 승자가 결정될 때면 나는 이곳에 없을 것이다.

이제는 내가 필요한 이야기를 들을 차례였다.

“저, 궁금한 게 있는데요.”

“말해 보거라.”

“제가 아직도 이류 경지에 머물러 있는데…….”

내 이야기를 모두 들은 진위경이 고개를 갸웃거렸다.

“네가 이류라고?”

도무지 이해가 가지 않는다는 말투였다. 이소군을 말 그대로 발라 버리고 조필까지 쓰러트린 나다. 진위경은 진작부터 나를 일류라고 생각했고, 그건 조필도 마찬가지였다.

“예. 도무지 경지가 안 올라서 조언을 좀 구하려고요.”

“조언이라…….”

잠시 생각하던 진위경이 입을 열었다.

“너는 이미 일류다.”

“저 이류인데요.”

“일류라니까. 그것도 절정의 벽에 맞닥트린 초일류의 무인이지.”

“아뇨. 저 이류 맞는…….”

“누가 그러더냐?”

아오, 미치겠네. 마음 같아서는 시스템창을 보여 주고 싶다.

떡하니 이류라고 적혀 있는데, 나만 알고 있으니까 답답해 죽겠다. 나는 한숨과 함께 대답했다.

“누가 저한테 이류라고 한 건 아니고요.”

“그럼?”

“그냥, 그냥 제가 이류인 거라서 뭐라 설명하기가 좀.”

“스스로 이류라고 믿느냐?”

“예.”

“그럼 간단하구나.”

“뭐, 뭔데요?”

드디어 경지 상승의 비법이 나오나?

나는 잔뜩 기대에 찬 눈빛으로 진위경을 바라봤지만, 그의 입을 열리지 않았다. 대신 그는 식어 버린 찻물에 손가락을 담가 탁자로 가져갔다.

스스슥.

그리고 드러나는 한 글자.



信



‘믿을 신(信)?’

내 얼굴을 확인한 진위경이 피식 웃었다.

“뺨이라도 한 대 맞은 표정이구나.”

“……잘못 보셨네요.”

뺨이라도 한 대 때리고 싶어 하는 표정이겠지.

“이게 뭡니까?”

“말 그대로지. 너 자신을 믿으란 소리야.”

“이게 경지가 오르는 것에 무슨 상관이 있는데요?”

“무공은 믿는 것부터 시작이니까.”

믿는 것부터 시작이라니. 뜬구름 잡는 소리다. 하지만 그 말을 듣는 순간부터 가슴은 쿵쾅거리며 뛰고 있었다.

‘믿는 것부터 시작이다…….’

이상하게도 그 한마디가 뇌리를 맴돈다. 끊임없이 뱅글뱅글 돌아가며 나를 어지럽게 만들었다.

‘그동안 나는 뭘 믿고 있었지?’

가장 먼저, 그리고 유일하게 떠오른 단어가 있다.

시스템. 이 게임에서 내게 가장 큰 도움이 됐고 언제나 절대적인 사실만을 알려 준 그것.

스스로를 이류라고 생각했던 건 시스템이 내게 이류라고 했기 때문이다.

‘시스템을 믿었으니까.’

일찍이 일류 고수인 이소군을 압도했다. 단신으로 스물이 넘는 낭인들을 쓰러트렸고 절정 고수인 조필마저 꺾었다.

사람들은 하나같이 나를 일류 고수요, 영웅이라고 추켜세웠지만 나는 여전히 이류였다. 스스로보다 시스템을 믿었기 때문이다. 하지만 이제는 알겠다.

‘나는 이미 일류야.’

이미. 어쩌면 오래전부터 그랬다. 나는 일류였다.

“뺨이라도 한 대 맞은 표정이구나.”

이번에는 진위경의 말이 맞았다. 나는 얼이 빠진 얼굴로 의자 등받이에 축 늘어졌다.

‘이런 병신.’

스스로도 못 믿는 나는 이류다. 아니, 였었다.

띠링.



- [일류]의 경지에 올랐습니다!

- 모든 무공의 경지가 한 단계씩 상승합니다!

- 근골과 근맥이 크게 향상됩니다!

- 단전의 크기가 확장됩니다!

- 레벨 업!

- 레벨 업!



삼류에서 이류. 다시 이류에서 일류.

나는 몸속 깊숙한 곳에서 뿜어져 나오는 힘을 느꼈고, 진위경은 소리 내어 웃었다.

“무슨 일 났습니까?”

뒤늦게 등장한 위팽이 어리둥절한 얼굴로 물었다.



* * *



막혔던 콧구멍이 뻥 뚫린 것 같다. 경지가 일류로 오르면서 비약적인 상승이 있었다. 감각과 무공, 모든 면에서.

대전을 나와 걷기 시작했다. 바람이 시원하다.

“삼공자님이시다.”

“다 나으신 건가?”

아니나 다를까, 사람들의 시선이 모인다. 나는 더 많은 사람이 있는 곳으로 방향을 틀었다.

‘누가 보면 영락없이 관심종자네.’

하지만 모든 일에는 다 이유가 있는 법이다.

띠링.



- 누군가가 당신을 경외감 어린 눈빛으로 바라봅니다.

- 명성이 1 상승합니다.

- 누군가가 당신의 소문을 듣고 감탄합니다.

- 명성이 1 상승합니다.



그렇게 걷다 보니 인파가 구름처럼 몰렸다. 그중에는 처음 보는 복색의 NPC들도 다수 섞여 있었다.

‘누구지?’

그중 한 사람과 눈이 마주쳤다. 스물이 좀 넘어 보이는 청년은 화들짝 놀라더니 이내 다가와 포권을 취했다.

“삼도문(三道問)의 곽 모가 인사 올립니다.”

“아, 예.”

이제는 반사적으로 튀어나오는 포권이 제법 그럴싸하다. 그런데 삼도문이 어디야?

아, 혹시?

“산서오문 소속이신가요?”

곽 뭐시기는 열정적으로 고개를 끄덕였다.

“맞습니다. 저희 삼도문은 태원진가에 힘을 보태기로 했습니다. 작은 힘이나마 도움을 드릴 수 있어 이 곽 모, 기쁘기 그지없습니다.”

지금 같은 상황에서는 천금 같은 지원군이다. 나는 이 곽 뭐시기가 내 몫까지 열심히 싸워 주길 바라며 손을 붙잡았다.

“와 주셔서 감사합니다.”

“별말씀을. 공자의 무용담에 낄 수 있게 되어 영광일 따름입니다.”



- 누군가가 당신의 소문을 듣고 감탄합니다.

- 명성이 1 상승합니다.



생판 남인데 여기까지 찾아와서 싸워 주고, 명성도 쭉쭉 올려 준다. 나는 아낌없이 주는 곽 뭐시기에게 따뜻한 감사의 말을 전했다.

“갓 블레스 유.”

“예?”

“옥황상제의 가호가 함께하길 바란다는 뜻입니다.”

“아아. 감사합니다. 갑부래수유.”

“아. 예.”

나는 가식적인 미소를 지으며 걸음을 옮겼다. 이제 알 만한 사람은 다 알아서인지, 태원진가 사람들로는 명성치가 오르지 않았다.

‘그래도 꽤 모였다.’

상태창을 열어 보니 목표 수치보다 50 정도가 부족했다. 앞으로 이틀만 더 빡세게 돌면 로그아웃이 가능하지 않을까 싶다.

“저어, 진 소협.”

고개를 돌려 보니 삼도문의 그 친구다. 아마 지구 끝까지 따라올 작정인 듯싶었다.

“혹 바쁘지 않으시다면 같이 차라도…….”

“죄송합니다. 제가 볼일이 있어서요.”

거짓말 같지만 진짜다. 처음부터 목적지는 정해져 있었다.

실망하는 그에게 건물을 가리켜 보였다. 빛바랜 현판이 걸린 그곳에서는 탕약 냄새가 물씬 풍겼다.

약왕당(藥王黨).

그리고 그 밑에 걸린 자그마한 나무판자.



관계자 외 출입 금지.



나를 둘러싼 사람들이 안타까운 한숨을 내쉬었다.
```

### Current accepted English

```markdown
# Chapter 34

Once, while Jinho hyung and I were watching TV, we had a conversation like this.

“That’s him, right? Han Seongjin.”

“You know Han Seongjin?”

“Wouldn’t it be weird if I didn’t? Turn on the TV and his face is right there. I’ve seen him so much he feels like family now.”

“Watch your mouth. That’s defamation.”

“Son of a bitch.”

On the screen, a handsome man with a lanky build was smiling brightly. Dozens of cameras and a huge crowd reacted to his every move. Flashes and screams kept going off without a pause.

“He’s got it all. An A-rank Hunter is basically a walking mid-size company, isn’t he? Model proportions and a celebrity face on top of that? That’s just cheating. How old did you say he was?”

“I think he’s the same age as me.”

“…Hang in there.”

No matter the job, there were people who made good money and people who didn’t. And no profession had a wider gap than Hunters.

“Don’t worry, man. If you wait a little longer, your day will come.”

“How long do I have to wait?”

“Try waiting another hundred years. It’ll be possible in your next life.”

I wanted to show Jinho hyung—the one who’d snickered while he teased me back then—what I looked like now.

*I wonder what kind of face he’d make if he saw this.*

With every step I took, dozens of people swarmed after me. NPCs from the Jin Family of Taiyuan, men and women of all ages, were looking at me with shining eyes.

*Is this how famous people always feel?*

People’s attention. Those admiring looks were burdensome, and yet a little enjoyable.

It was the moment I finally understood that common game-promo line: *Awaiting a new hero!*

*Yeah. It’s almost over. Might as well enjoy it.*

I waved with a smile, and a roar went up. Trailing a crowd that only kept growing, I arrived at the main hall they used for meetings.

“They’re waiting for you.”

The martial artist’s face looked familiar. He was the same man who had looked at me with contempt when Lee Seogeun came to see me last time.

*Has it been about fifteen days?*

Just as I was different from the person I had been then, so was he. He made an extremely respectful fist-and-palm salute and threw the door open.

* * *

The main hall looked exactly as I remembered it. The large table in the center and the scattered chairs on either side showed that a meeting had just ended.

“You’ve come?”

Jin Wikyung, seated at the head of the table, gave me a tired smile. He was the only person in the spacious hall.

“Where’s Wipeng?”

“He’ll be back shortly.”

Once I sat down, Jin Wikyung got straight to the point.

“The Lower District Sect has contacted us. It seems the Mount Heng Sword Sect is rounding up troops however they can.”

*They must be shitting bricks over there.*

I didn’t know war, but I knew combat. And war was what you got when battles piled up. Having already lost so many martial artists and so much morale in one crushing defeat, the enemy would throw everything they had into the next battle.

“It’ll be a difficult fight.”

“They’ve poured the entire wealth of their sect into this. If the reinforcements join the main force led by the Blood Wolf Sword, they’ll number around a thousand.”

“A thousand…”

That was an insane number. I’d never been in a battle on that scale, and I had no desire to.

Jin Wikyung continued with a grim expression.

“We’ll march north with every force we have. The plan is to strike the enemy’s main force before it joins the reinforcements.”

“When is that?”

“In two days.”

*Goddammit. That’s filthy fast.*

The race against time wasn’t happening only between the Jin Family of Taiyuan and the Mount Heng Sword Sect. It was happening to me, too.

*Can I log out by then?*

If I became First Rate within two days, I could log out. But what if I didn’t? I’d have to fight my head off all over again.

*Then I’d be completely screwed.*

Jin Wikyung spoke again.

“I’d like you to take charge of the rear guard.”

*Can’t. Won’t.*

I barely swallowed the words that tried to leap out on reflex.

Jin Wikyung’s face was more serious than I’d ever seen it.

“This is a fight our family is staking everything on. Your presence alone will raise morale a great deal.”

“…”

I was still debating whether to accept when he continued.

“Fortunately, the Five Gates of Shanxi have agreed to help us. Move with some of them in the rear guard.”

“The Five Gates of Shanxi?”

“An alliance of five small and mid-sized sects. We’ve always been on good terms with them.”

“…I see.”

“Then will you take charge of the rear guard?”

Ding.

> **System**
>
> **Quest**
>
> **Rear Guard Defense**
>
> Jin Wikyung has proposed that you take charge of the rear guard.
>
> If you accept this mission, the martial artists will praise your will and courage.
>
> **Type:** Short-Term Quest
>
> **Grade:** Second Rate
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Accept the proposal (Incomplete)
>
> **Reward:** Fame +10
>
> **Failure:** Fame −10

I answered without giving it any more thought.

“I will.”

A message appeared saying the Quest had succeeded and my Fame had increased.

*Fame drops if I refuse?*

The Quest Window had made me an offer I couldn’t refuse. It was ridiculous, but a strange relief spread through me all the same.

*Relief? Have I actually lost my mind?*

While I was berating myself for being a game addict, Jin Wikyung smiled broadly.

“It’s a relief to have you here.”

He was smiling, but an invisible shadow hung over his face.

Being buried under stacks of paperwork all day hadn’t been enough. Now there was a war, too. Commanding the enormous Jin Family of Taiyuan had to be a heavy burden even for him.

*He said two days.*

Two powers that split a region between them were about to collide. The Jin Family of Taiyuan was short on martial artists, so even if we threw everything we had into it, we’d still be at a disadvantage.

*Can we win?*

I forced the thought aside.

*Live or die, what do I care?*

The march was in two days, and it would take several more days before the battle actually began. Whoever won, I wouldn’t be here by the time the victor was decided.

Now it was time to hear what I needed to know.

“Um, there’s something I’m curious about.”

“Ask.”

“I’m still stuck at the Second Rate realm…”

After hearing me out, Jin Wikyung tilted his head.

“You’re Second Rate?”

His tone made it clear that he couldn’t understand it at all. I had literally wiped the floor with Lee Seogeun and even brought down Jopil. Jin Wikyung had taken me for First Rate for a long time, and so had Jopil.

“Yes. My realm just won’t rise, so I wanted to ask your advice.”

“Advice…”

Jin Wikyung thought for a moment before speaking.

“You’re already First Rate.”

“But I’m Second Rate.”

“I’m telling you, you’re First Rate. Not just that—you’re a Super First Rate martial artist who’s run into the wall of Peak.”

“No, I really am Second Rate…”

“Who told you that?”

*Ugh, this is driving me crazy.*

I wanted to show him the System Window. It plainly said Second Rate, but I was the only one who knew that, and the frustration was killing me.

I answered with a sigh.

“No one told me I was Second Rate.”

“Then?”

“It’s just… I’m just Second Rate, so it’s a little hard to explain.”

“Do you believe you’re Second Rate?”

“Yes.”

“Then it’s simple.”

“Wh-what is?”

*Is he finally going to reveal the secret to advancing realms?*

I looked at Jin Wikyung, eyes full of anticipation, but he didn’t open his mouth. Instead, he dipped a finger into the tea that had gone cold and brought it to the table.

Ssssk.

A single character appeared.

信

*信? The character for ‘believe’?*

After checking my face, Jin Wikyung let out a short laugh.

“You look like you’ve just been slapped.”

“…You must be mistaken.”

*More like I look like I want to slap you.*

“What is this?”

“Exactly what it says. Believe in yourself.”

“What does that have to do with advancing realms?”

“Because martial arts begin with belief.”

*They begin with belief.*

It sounded like pie in the sky. But from the moment I heard those words, my heart was pounding.

*They begin with belief…*

Strangely, that one sentence kept circling through my mind, spinning round and round until I was dizzy.

*What had I been believing in all this time?*

The first word that came to mind—and the only one—was the System.

The thing that had helped me most in this game, and had always told me nothing but absolute fact.

I had thought of myself as Second Rate because the System had told me I was Second Rate.

*Because I believed in the System.*

I had already overwhelmed Lee Seogeun, a First Rate master. I had taken down more than twenty wandering martial artists by myself, and I had even brought down Jopil, a Peak master.

Everyone praised me as a First Rate master and a hero, but I was still Second Rate.

Because I had believed in the System instead of myself.

But now I understood.

*I’m already First Rate.*

Already. Maybe I had been for a long time.

I was First Rate.

“You look like you’ve just been slapped.”

This time, Jin Wikyung was right. I slumped against the back of my chair, looking completely out of it.

*What a dumbass.*

If I couldn’t even believe in myself, I was Second Rate. No. I *had been* Second Rate.

Ding.

> **System**
>
> — You have reached the **First Rate** realm!
>
> — The realm of all martial arts increases by one stage!
>
> — Your Sinews and Bones and your Meridians improve greatly!
>
> — The size of your dantian expands!
>
> — Level Up!
>
> — Level Up!

From Third Rate to Second Rate. Then from Second Rate to First Rate.

I felt power surge from deep within my body, and Jin Wikyung burst out laughing.

“What happened?”

Wipeng showed up late and asked, looking bewildered.

* * *

It felt like a blocked nose had blown clear. Reaching First Rate had brought a tremendous leap in every way—senses, martial arts, everything.

I left the main hall and started walking. The wind felt refreshing.

“It’s the Third Young Master.”

“Has he fully recovered?”

Sure enough, people’s eyes gathered. I changed direction toward a place with even more people.

*Anyone watching would take me for an attention hog.*

But everything happens for a reason.

Ding.

> **System**
>
> — Someone gazes at you with awe.
>
> — Fame increases by 1.
>
> — Someone is impressed after hearing your rumors.
>
> — Fame increases by 1.

As I walked, the crowd gathered like clouds. Plenty of NPCs in unfamiliar clothing were mixed in among them.

*Who are they?*

My eyes met one of them. The young man looked a little over twenty. He flinched in surprise, then quickly approached and made a fist-and-palm salute.

“Guo of the Three Paths Sect presents his respects.”[^1]

“Ah, yes.”

The fist-and-palm salute now came out on reflex and looked fairly convincing. But where was the Three Paths Sect?

*Oh. Could it be…?*

“Are you with the Five Gates of Shanxi?”

Guo Whatsisname nodded hard.

“That is correct. Our Three Paths Sect has agreed to lend its strength to the Jin Family of Taiyuan. I, Guo, could not be more delighted to offer even the smallest assistance.”

In a situation like this, he was reinforcements worth their weight in gold. I grabbed Guo Whatsisname’s hand, hoping he would fight hard enough for my share as well.

“Thank you for coming.”

“Don’t mention it. It is merely an honor to be included in the Young Master’s tales of martial prowess.”

> **System**
>
> — Someone is impressed after hearing your rumors.
>
> — Fame increases by 1.

A complete stranger had come all this way to fight for us, and he was even helping my Fame climb. I offered my warm thanks to the freely giving Guo Whatsisname.

“God bless you.”

“Pardon?”

“It means I hope the Jade Emperor’s blessing will be with you.”

“Ahh. Thank you. Gapburaesuyu.”

“Ah. Yes.”

I put on a fake smile and kept walking. Maybe because everyone who needed to know already did, the Jin Family of Taiyuan’s people no longer raised my Fame.

*Still, I’d piled up quite a bit.*

I opened the Status Window and saw that I was about fifty short of the target. If I grinded hard for just two more days, maybe I could log out.

“Um, Young Hero Jin.”

I turned around. It was the fellow from the Three Paths Sect. He looked ready to follow me to the ends of the earth.

“If you aren’t busy, perhaps we could have some tea together…”

“I’m sorry. I have somewhere to be.”

It sounded like a lie, but it was the truth. My destination had been decided from the start.

I pointed out a building to him as he looked disappointed. A faded signboard hung there, and the smell of medicinal decoctions rolled out thick.

Medicine King Hall.

And beneath it hung a small wooden plaque.

**No Entry Except for Authorized Personnel.**

The people surrounding me let out pitying sighs.

[^1]: The given characters are 三道問, with 問 (“question”), not the usual 門 (“gate”/“sect”).
```
## Chapter 35

### Korean source

```text
＃35화



약왕당의 한 병실.

온몸에 붕대를 칭칭 감은 혁무진이 끙, 신음을 흘렸다.

“죽겠네.”

옆자리에 비슷한 몰골로 누워 있던 한엽이 대꾸했다.

“안 죽은 게 기적이죠.”

“그치?”

“그렇죠.”

잠시 침묵이 흘렀다. 둘 다 그날의 기억을 떠올리고 있었다.

조필의 일장(一掌). 알아도 막을 수 없는 공격이었다. 눈만 감으면 붉게 달아오른 놈의 손바닥이 생각났다. 어쩌면 평생 따라다닐 악몽일지도 모르겠다.

“괴물 같은 놈. 어떻게 그런 게 가능하지?”

“절정 고수잖아요.”

허탈해하는 혁무진과 달리 한엽의 목소리는 담담했다.

“야, 인마. 넌 아무렇지도 않냐?”

“뭐가요?”

“그…….”

혁무진은 순간 말문이 막혔다. 그러게. 아무렇지 않을 수도 있지.

“아니, 내 말은 그게 아니고…….”

“알고 있어요.”

“응?”

“부조장이 어떤 생각을 하고 있는지. 무슨 말을 하고 싶은지.”

“…….”

“처음 정신을 차렸을 때 참 많은 생각이 들더라고요. 살았다는 안도감. 그때 느꼈던 무력감과 내 무공에 대한 절망감.”

혁무진은 입을 다물었다. 한엽의 말은 정확했다. 조필의 화염신장은 뼈를 부러트리고 심맥을 찢었지만 그가 입은 상처는 따로 있었다.

그날 이후 머릿속을 맴도는 한 가지 질문.

‘내가 저 경지에 도달할 수 있을까?’

압도적이라는 표현으로도 부족하다. 지금까지의 노력이, 스스로의 무공에 대한 자부심이 송두리째 뿌리 뽑혔다.

“넌 그걸 전부 털어 낸 거냐?”

한엽이 고개를 저었다.

“그럼?”

“제가 약하다는 사실을 인정한 겁니다. 별로 어렵지도 않았어요. 항상 알고 있었으니까. 다만…….”

“……?”

“강해질 겁니다. 조필만큼. 아니, 조필보다 훨씬.”

한엽은 힘 있는 목소리로 말을 이었다.

“그 생각을 하니까 기뻐지더라고요. 나도 절정 고수가 된다면 저렇게 강해질 수 있겠구나. 뭐 그런 생각이요.”

“절정 고수라…….”

절정의 경지는 극소수에게만 허락된 영역이다. 고작 이, 삼류에 불과한 한엽의 선언은 우습기까지 했다.

하지만 혁무진은 비웃지 않았다.

‘변했구나. 이 녀석도.’

그동안 많은 것이 변했다. 상황도, 사람도.

소심하던 이류 무사도 어느새 그 흐름에 동참했다. 혁무진은 문득 가슴이 울렁거렸다. 다음 순간 불쑥 튀어나오는 말이 있었다.

“내가 더 강해질 거다.”

그 말에 눈을 동그랗게 뜬 한엽이 이내 씩 웃어 보였다.

“꼭 그렇게 될 겁니다. 우선 한 사람부터 따라잡아야죠.”

그들은 동시에 한 사람을 떠올렸다. 진태경. 이미 저 앞에서 뛰고 있는 그는 지금 뭘 하고 있을까?

생각에 잠긴 두 사람의 등 뒤로 빠끔히 열려 있던 문이 스르륵 닫혔다.



* * *



문을 닫고 돌아서는데 온몸이 부르르 떨렸다.

“어후, 씨.”

이것들이 병실에서 청소년 성장 드라마 찍고 있네. 무슨 얘길 하나 가만히 듣고 있었는데 아주 가관이다, 가관.

들어갔으면 의형제 맺을 뻔.

‘그래도 좀 기특하긴 하네.’

나름 생사고락을 함께한 사이 아닌가. 게다가 저 두 사람은 날 돕기 위해 목숨까지 걸었었다. 정나미 한 톨 없다고 하면 거짓말이지.

‘이게 마지막이려나.’

이틀 뒤, 나는 조만간 본대 후위를 맡아 출정할 것이고 저 둘을 비롯한 정찰조원들은 부상자로 가문에 잔류할 테니까. 그리고 아마도…….

‘그때쯤에는 로그아웃하게 되겠지.’

로그아웃 퀘스트의 마지막 조건인 명성 500 달성이 머지않았다. 오늘 약왕당 방문은 나름의 작별 인사인 셈이다.

전역을 앞둔 말년 병장의 추억 보정이라 해도 좋고.

‘뭐, 굳이 알릴 필요 없이 얼굴만 보면 되지.’

이미 다른 정찰조원들도 쓱 훑어보고 왔다. 한엽과 혁무진도 봤으니 한 곳만 더 들르면…… 어?

“어!”

한 손에는 헝겊 인형. 다른 손에는 과자.

귀엽게 댕기를 묶은 꼬마가 땡그란 눈으로 외쳤다.

“관심법 아저씨다!”

“…….”

오빠라고 불러 주면 안 되겠니. 나는 슬픈 눈으로 소율에게 손을 흔들어 주었다.



* * *



“진 공자.”

“은인!”

병실에 들어서자마자 즉각적인 반응이 튀어나왔다. 아직 파리한 안색의 공야청이 일어나려는 것을 제지하고 넙죽 절하는 소천을 일으켜 세웠다.

“누워 계세요. 너도 일어나, 인마. 내가 절 받을 나이냐.”

“백번 절해도 부족한 은혜를 입었습니다.”

벌써부터 두 사람의 눈가에 물기가 고인다. 멋모르는 소율은 헝겊 인형을 꼭 끌어안고 제 오빠한테 쪼르르 달려가 안겼다.

“오라버니 은혜 입었어? 나도 은혜 보여 줘. 예뻐?”

어. 그거 옷 아냐.

조잘거리는 소율을 뒤로하고 공야청에게 말을 걸었다.

“몸은 좀 어떠세요?”

“더할 나위 없이 좋소. 한동안 요양해야겠지만.”

공야청의 입가로 희미한 미소가 번졌다.

“모두 공자 덕분이오.”

“공치사 들으려고 한 일이 아닙니다. 심지어 한 번은 그대로 놓고 간 적도 있고요.”

“내 선택이었소. 그리고 공자는 돌아왔지.”

조필에게 쫓기던 그 날 밤이 떠올랐다. 공야청은 심각한 중독 상태였고 스스로 남기를 원했다. 그가 그랬듯 나도 선택해야 했다.

수많은 갈등 끝에 내가 내린 결정은 그에게 되돌아가는 것이었다.

‘엄청나게 후회했지.’

미친 짓이었다. 고작 게임 속 NPC를 위해서 목숨을 건 도박을 하다니. 하지만 이제는 알 것 같다. 왜 그런 선택을 했는지.

부모를 잃은 어린 남매에게 무엇을 보았고 공야청과 정찰조원들에게서 누구를 떠올렸는지…….

“진 공자?”

공야청의 목소리에 정신을 차렸다.

“별거 아닙니다. 그냥, 그냥 생각할 게 좀 있어서요.”

“아, 나도 소식은 전해 들었소. 혹 그것 때문이오?”

“무슨 소식이요?”

“조만간 큰 전투가 있을 거라 하더이다.”

이거 군사기밀 아니었냐.

병실에만 머무르는 공야청이 알 정도면 태원진가에 눈 있고 귀 달린 놈들은 다 안다고 봐야 한다.

첩자라도 하나 있으면 대북 확성기가 따로 없겠군.

‘이 전쟁, 이대로 괜찮은가.’

문득 드는 생각을 휘휘 저어 흘려보냈다. 뭔 상관이냐, 어차피 곧 나와는 상관없는 일이 될 텐데.

이 순간에도 울리는 시스템 알림이 그 증거다.

띠링.



- 당신에 대한 소문이 계속해서 퍼지고 있습니다.

- 명성치가 1 상승합니다.



발 없는 말이 천 리 간다고, 조필을 쓰러트린 이후 내 이름이 본격적으로 퍼지기 시작한 모양이었다.

슬쩍 퀘스트창을 열어 확인해 보니 남은 명성치는 50 남짓.

로그아웃은 이미 기정사실이나 마찬가지다.

“본가의 명운이 걸린 전투가 되겠구려.”

물론 내 상황을 이들이 알 리가 없다. 공야청과 소천의 이야기를 가만히 듣다가 자리를 털고 일어났다.

“이만 가 봐야 할 것 같습니다.”

“은인.”

아쉬운 얼굴의 소천을 제지한 건 공야청이었다.

“가시게 두어라.”

“하지만…….”

“어허.”

소천이 시무룩하게 고개를 숙였다. 혼자 인형을 갖고 놀던 소율이 커다란 눈으로 나를 올려다본다.

“아저씨 벌써 가?”

“오빠라니까.”

“응. 아저씨.”

소율의 통통한 볼을 살짝 꼬집어 주고 돌아서려는 순간, 공야청이 나를 불렀다.

“진 공자. 갈 땐 가더라도 놓고 간 물건은 가져가야 하지 않겠소?”

“놓고 간 물건이요?”

잠깐 생각해 봤지만 그런 게 있을 턱이 있나. 인벤토리라는 사기 기능 덕분에 늘 손이 가벼운 나다.

“그런 거 없는…… 뭡니까, 이게?”

공야청의 손에는 긴 보퉁이가 들려 있었다.

“공자가 경황이 없어 챙기지 못한 물건이오. 주인이 왔으니 돌려주는 게 맞겠지.”

뭐지?

어리둥절한 상태로 보퉁이를 받아 들었다. 제법 묵직한 무게. 내용물을 확인하려 하는 내게 공야청이 말했다.

“처소에서 풀어 보시오. 남들 눈에 띄지 않도록.”

금송아지라도 들었나?



* * *



처소에 도착하자마자 보퉁이를 풀었다. 그리고 공야청이 했던 마지막 말의 의미를 알 수 있었다.

‘다른 사람이 보면 탐낼 만한 물건이긴 하네.’

낡은 책자와 조그만 상자. 그리고 낯익은 검 하나.

무림인에게 이 물건들의 가치는 금송아지에 비할 바가 아니다. 그 가치를 어느 누구보다 정확하게 파악할 수 있는 능력이 내게는 있었다.

‘아이템 확인.’

띠링.



아이템창



[화염신장]

종류 : 무공 비급

등급 : 초절정

제한 : 열양지기의 소유자

설명 : 열화문(熱火門)의 비전절기 중 하나. 강력한 화기를 바탕으로 한 무공이다.

효과 : [화염신장]의 습득





아이템창



[열화신단]

종류 : 영단

등급 : 절정

제한 : 無

설명 : 열화문(熱火門) 비전으로 제조된 영단.

효과 : 복용 시 30년의 공력을 얻는다. 단, 영단이 품은 강력한 화기를 다스리지 못한다면 끔찍한 최후를 맞이할 수 있다.





아이템창



[이름 없는 검]

종류 : 검

등급 : 無

제한 : 無

설명 : 만년한철로 제작되어 매우 날카롭고 단단하다. 오랜 시간, 수많은 피를 머금은 탓에 스스로 변화했다. 검의 힘을 끌어내기 위해서는 특수한 조건이 필요하다.

효과 : 알 수 없음





“미쳤네.”

진짜 미쳤다. 초절정의 비급에 30년 공력을 주는 영단, 거기에 정확히는 모르지만 엄청나게 좋아 보이는 검까지.

호랑이는 죽으면서 가죽을 남긴다는데 조필은 이런 물건을 셋이나 남겼다.

‘시바, 좋은 건 꼭 다 끝나고 주더라.’

빌어먹을 망겜. 챙겨 줄 거면 진작 좀 챙겨 주든가. 다 끝나고 나서 뒷북치는 꼴에 혈압이 오른다.

‘그래도 아이템은 진짜 좋네.’

설명을 읽으면서 나도 모르게 혹할 정도였다. 영단 흡수하고 화염신장까지 익히면 어떨까. 조필처럼 손에서 막 불도 나오고 그러면…….

‘존나 멋있을 것 같은데.’

하지만 그런 생각도 잠시였다. 말년에는 떨어지는 낙엽도 조심하라 했는데 영단 잘못 삼켰다가 셀프 화형식을 열고 싶지는 않다.

‘명심하자. 안전 제일. 안전 제일.’

이제 와서 안전 운운하는 것도 웃기지만 그렇다고 넙죽 집어삼킬 만큼 멍청한 놈도 아니다.

‘다 끝나 간다.’

삐끗하는 순간 훅 가는 거다. 나는 아이템들을 모두 인벤토리에 처넣었다. 깊은 밤, 어딘가에서 벌어지는 술자리에서 내 얘기라도 하는지 시스템 알림이 울렸다.

띠링.



- 명성치가 1 올랐습니다.



* * *



그 시각, 대장로는 정원을 거닐고 있었다. 약속된 날짜와 장소다. 어둠 속 ‘그’는 시간을 어기는 법이 없었다.



- 달이 참 밝군요.

- 그렇군.

그의 말처럼 오늘의 보름달은 유난히 밝았다.



- 어릴 때는 달이 참 좋았는데…… 머리 굵어질수록 그런 생각이 들더군요.

- 어떤 생각?

- 달이 없었으면 좋겠다. 뭐 그런 생각이죠.

- 운치 없는 세상이로군.

- 운치 좀 없으면 어떻습니까. 저야 밤 생활로 먹고사는 놈이니 달이 없어지면 기쁠 겁니다.

밤 생활이라. 그는 기둥서방처럼 경박하고 유쾌한 어조로 떠벌렸지만 대장로는 알고 있었다. 그가 고강한 무공의 소유자이며 뛰어난 살수라는 사실을.

바람 사이로 피비린내가 나는 것 같았다.



- 아, 참. 일은 어떻게 되어 가고 있습니까?

- 순조롭네. 병력 배치까지 끝났지.

- 너무 무리하지 마십시오. 영민한 소가주가 냄새를 맡으면 일이 틀어지니까요.

- 걱정 말게. 내가 나설 필요도 없었으니.

- 하늘이 돕는군요.

- 그쪽은 어떤가?

- 뻔한 걸 물어보시는군요.

가벼운 질책이 담긴 말에 대장로는 입을 다물었다.

‘어련할까.’

해무(海霧) 같은 자들이다. 그들의 정체는 안개에 덮여 보이지 않고 손을 뻗어 휘저어도 실체가 없었다. 축축한 손바닥과 불쾌한 감정만이 남을 뿐이다.

‘하지만 힘이 있지.’

자신을 태원진가의 가주로, 산서성의 유일한 패자로 만들 수 있는 힘. 반평생 간직한 야망이다. 대장로는 무엇이든 할 준비가 되어 있었다.

- 모든 준비는 끝났습니다.

- 나 역시.

산서성의 양분하는 두 거대 문파가 격돌하는 날…… 모든 것이 끝나고 새롭게 시작될 것이다.
```

### Current accepted English

```markdown
# Chapter 35

A hospital room in Medicine King Hall.

Hyuk Mujin, wound tight in bandages from head to toe, let out a groan.

“I’m dying.”

Han Yeop, lying beside him in much the same shape, answered,

“It’s a miracle we didn’t die.”

“Right?”

“It is.”

A brief silence followed. Both of them were remembering that day.

Jopil’s palm strike. An attack you couldn’t block even if you knew it was coming. The moment he closed his eyes, that bastard’s red-hot palm came back to him. It might become a nightmare that followed him for the rest of his life.

“That monster. How is something like that even possible?”

“He’s a Peak master.”

Unlike the dejected Hyuk Mujin, Han Yeop’s voice was calm.

“Hey, punk. Doesn’t it bother you at all?”

“What?”

“That…”

Hyuk Mujin found himself at a loss for words. Right. Maybe it didn’t have to bother him.

“No, that’s not what I meant…”

“I know.”

“Huh?”

“I know what the deputy squad leader is thinking. I know what you want to say.”

“…”

“When I first came to, a lot of things went through my mind. The relief of being alive. The helplessness I felt that day. The despair over my own martial arts.”

Hyuk Mujin shut his mouth. Han Yeop had it right. Jopil’s Flame Divine Palm had broken bones and torn heart meridians, but the wound he’d taken was somewhere else.

One question had been circling through his head ever since that day.

*Can I reach that realm?*

“Overwhelming” wasn’t enough. All his effort, all his pride in his own martial arts, had been ripped up by the roots.

“You’ve shaken all that off?”

Han Yeop shook his head.

“Then?”

“I admitted that I’m weak. It wasn’t even that hard. I’ve always known. But…”

“…”

“I’ll get stronger. As strong as Jopil. No—far stronger than Jopil.”

Han Yeop went on, his voice firm.

“Thinking about that made me happy. If I become a Peak master, I can get that strong too. Something like that.”

“A Peak master…”

The Peak realm was a domain granted to only a rare few. Coming from Han Yeop, who was barely second- or third-rate, the declaration was almost laughable.

But Hyuk Mujin didn’t sneer.

*You’ve changed. You too.*

So much had changed. The situation. The people.

Even the timid second-rate martial artist had, before anyone noticed, stepped into that current. Hyuk Mujin felt his heart lurch. The next words burst out before he could stop them.

“I’ll get even stronger.”

Han Yeop’s eyes went round, then he flashed a grin.

“You will. First, though, we have to catch up to one person.”

They thought of the same person at the same time. Jin Taekyung. He was already running far ahead of them. What was he doing now?

Behind the two men, lost in thought, the door that had been slightly ajar slid shut.

* * *

I closed the door and turned away, and a shudder ran through me.

“Ugh, shit.”

These idiots were filming a teen coming-of-age drama in a hospital room. I’d stood there quietly listening to hear what they were talking about, and it was quite a spectacle. A real spectacle.

If I’d gone in, I might’ve ended up swearing brotherhood with them.

*Still, I have to admit it’s kind of admirable.*

Hadn’t we shared life and death together, in our own way? Besides, those two had risked their lives to help me. Saying I didn’t feel so much as a shred of affection for them would have been a lie.

*Could this be the last time?*

In two days I would set out in charge of the main force’s rear guard, while those two and the rest of the reconnaissance squad would stay behind at the family as wounded men. And probably…

*By then, I’ll have logged out.*

I was close to the last condition of the Logout Quest: 500 Fame. Today’s visit to Medicine King Hall was a farewell of sorts.

You could call it the nostalgia filter of a sergeant in his last stretch before discharge.

*Well, no need to announce anything. Seeing their faces is enough.*

I’d already given the other reconnaissance-squad members a once-over. I’d seen Han Yeop and Hyuk Mujin too, so if I stopped by just one more place…

Huh?

“Oh!”

A rag doll in one hand. Snacks in the other.

A little girl with her hair tied in a cute ribbon shouted, her eyes round.

“It’s the mind-reading uncle!”

“…”

Couldn’t you call me Big Brother? I gave Soyul a sad little wave.

* * *

“Young Master Jin.”

“Benefactor!”

The moment I entered the room, the reactions came at once. Gong Yacheong, still pale, tried to rise, and I stopped him. Then I pulled Socheon, who had dropped into a full bow, back to his feet.

“Stay lying down. You too, punk. Get up. Do I look old enough to take a bow from you?”

“I’ve received a kindness a hundred bows couldn’t repay.”

Tears were already welling in both their eyes. Soyul, who didn’t understand any of it, hugged her rag doll tight and scampered over to cling to her brother.

“Big brother, did you put on the Benefactor’s kindness? Show me too. Is it pretty?”

*Uh. That’s clothes, isn’t it?*

Leaving the chattering Soyul behind, I spoke to Gong Yacheong.

“How are you feeling?”

“Couldn’t be better. I’ll need to recuperate for a while, though.”

A faint smile spread across Gong Yacheong’s lips.

“It’s all thanks to you, Young Master.”

“I didn’t do it to hear you flatter me. I even left you behind once.”

“That was my choice. And you came back.”

I remembered that night Jopil had been chasing us. Gong Yacheong had been badly poisoned and had wanted to stay behind. Just as he had, I’d had to make a choice.

After a great deal of inner conflict, the decision I reached was to go back for him.

*I regretted it like crazy.*

It had been insane. Gambling my life for a mere NPC in a game. But now I thought I understood why I’d made that choice.

What had I seen in those young siblings who’d lost their parents? Who had Gong Yacheong and the reconnaissance squad reminded me of…?

“Young Master Jin?”

Gong Yacheong’s voice pulled me back.

“It’s nothing. I just—just had something on my mind.”

“Ah, I heard the news as well. Is that what this is about?”

“What news?”

“They say there will be a major battle soon.”

*Wasn’t that military intelligence?*

If Gong Yacheong, who never left his hospital room, knew about it, then anyone in the Jin Family of Taiyuan with eyes and ears already knew.

If there was even one spy among us, we wouldn’t need a loudspeaker aimed at North Korea.

*Is this war really going to be all right like this?*

I waved the thought away. What did it matter to me? Soon enough, it wouldn’t have anything to do with me anyway.

The System alerts ringing even now were proof.

Ding.

> **System**
>
> — Rumors about you continue to spread.
>
> — Fame increases by 1.

They said a rumor traveled a thousand li without feet. After I’d taken Jopil down, my name seemed to have started spreading in earnest.

I cracked the Quest Window open for a look. About fifty Fame left to go.

Logout was as good as decided.

“It will be a battle with our family’s fate at stake.”

Of course they had no way of knowing my situation. I listened quietly to Gong Yacheong and Socheon, then rose from my seat.

“I think I should be going.”

“Benefactor.”

Gong Yacheong was the one who stopped Socheon when the boy looked disappointed.

“Let him go.”

“But…”

“That’s enough.”

Socheon lowered his head glumly. Soyul, who had been playing with the doll by herself, looked up at me with huge eyes.

“You’re leaving already, mister?”

“I said Big Brother.”

“Okay. Mister.”

I gave her chubby cheek a light pinch and was about to turn away when Gong Yacheong called out to me.

“Young Master Jin. You may be leaving, but shouldn’t you take the thing you left behind?”

“The thing I left behind?”

I thought about it for a moment, but there was no way I’d left anything. Thanks to the cheat known as Inventory, my hands were always empty.

“There’s nothing like tha—what is this?”

Gong Yacheong was holding a long bundle.

“You were in no state to collect it. Now that its owner has come, returning it is only right.”

*What is it?*

Still bewildered, I took the bundle. It was fairly heavy. Just as I was about to check what was inside, Gong Yacheong spoke.

“Unwrap it in your quarters. Don’t let anyone else see.”

*Did he put a golden calf in here?*

* * *

I unwrapped the bundle the moment I reached my quarters. Then I understood what Gong Yacheong’s last words had meant.

*These really are the kind of things people would covet if they saw them.*

An old booklet. A small box. And a familiar sword.

To someone in Murim, these were beyond comparison to any golden calf. And I had the ability to judge that value more accurately than anyone.

*Check Item.*

Ding.

> **System**
>
> **Item Window**
>
> **Flame Divine Palm**
>
> **Type:** Martial Arts Manual
>
> **Grade:** Supreme Peak
>
> **Restriction:** Holder of Scorching Yang Qi
>
> **Description:** One of the Fire Gate Clan’s secret techniques. A martial art based on powerful fire qi.
>
> **Effect:** Acquired Flame Divine Palm
>
> **Item Window**
>
> **Fire Divine Elixir**
>
> **Type:** Spiritual Elixir
>
> **Grade:** Peak
>
> **Restriction:** None
>
> **Description:** A spiritual elixir made according to the Fire Gate Clan’s secret formula.
>
> **Effect:** Grants thirty years of internal energy when consumed. However, if the user cannot control the powerful fire qi contained within the elixir, they may meet a horrific end.
>
> **Item Window**
>
> **Nameless Sword**
>
> **Type:** Sword
>
> **Grade:** None
>
> **Restriction:** None
>
> **Description:** Made of ten-thousand-year cold iron, this sword is exceptionally sharp and durable. After drinking countless amounts of blood over a long time, it changed on its own. Special conditions are required to draw out the sword’s power.
>
> **Effect:** Unknown

“This is insane.”

It really was insane. A Supreme Peak martial arts manual. A spiritual elixir that granted thirty years of internal energy. And a sword I didn’t fully understand, but that looked ridiculously good.

They said a tiger left its pelt behind when it died, but Jopil had left three things like these.

*Shit. It always hands over the good stuff after everything’s over.*

Damn shitty game. If it was going to give me something, it should have done it sooner. Playing catch-up after everything was finished just spiked my blood pressure.

*Still, these items are seriously good.*

Reading the descriptions, I caught myself getting tempted. What if I absorbed the elixir and learned Flame Divine Palm? Fire shooting from my hands like Jopil…

*That would be fucking cool.*

But the thought lasted only a moment. They said that in your last stretch before discharge, you had to watch out even for falling leaves. I didn’t want to swallow the elixir wrong and hold a self-immolation ceremony.

*Remember this. Safety first. Safety first.*

Talking about safety at this point was pretty funny, but I wasn’t stupid enough to just gulp it down.

*It’s almost over.*

One slip and I’d be gone. I stuffed all the items into my Inventory. Somewhere in the dead of night, someone must have been talking about me over drinks, because a System alert rang out.

Ding.

> **System**
>
> — Fame has increased by 1.

* * *

At that hour, the Head Elder was walking through the garden. The date and the place had been agreed upon. In the darkness, the man never failed to keep the time.

“The moon is very bright.”

“So it is.”

As he had said, tonight’s full moon was exceptionally bright.

“When I was young, I really loved the moon… but the older I got, the more I found myself thinking.”

“Thinking what?”

“That I’d rather there were no moon. Something like that.”

“A world without charm.”

“What’s wrong with a little less charm? I make my living at night, so I’d be delighted if the moon disappeared.”

*Night life, huh.*

He ran his mouth in a flippant, cheerful tone like a kept man, but the Head Elder knew the truth. He possessed formidable martial arts, and he was a superb assassin.

The wind seemed to carry the smell of blood.

“Ah, right. How is the work progressing?”

“Smoothly. Even the troop deployments are finished.”

“Don’t overdo it. If the clever Lesser Family Head catches a whiff of it, everything will go wrong.”

“Don’t worry. I didn’t even need to make a move.”

“Heaven is helping us.”

“And your side?”

“You’re asking the obvious.”

The light reproach in his words made the Head Elder fall silent.

*As if it would be otherwise.*

They were like sea fog. Their identities lay hidden under the mist, and even if you reached out and stirred it with your hand, there was no substance to grasp. All that remained was a damp palm and an unpleasant feeling.

*But they have power.*

The power to make him Family Head of the Jin Family of Taiyuan, the sole hegemon of Shanxi. An ambition he had held for half his life. The Head Elder was prepared to do anything.

“All preparations are complete.”

“Mine as well.”

The day the two great sects that divided Shanxi clashed…

Everything would end, and everything would begin anew.
```
## Chapter 36

### Korean source

```text
＃36화



퀘스트



[로그아웃]

이제 당신은 이 험난한 무림을 헤쳐 나가야 합니다.

더욱더 강해지고, 유명해지십시오.

언젠가 다가올 그 날을 위해…….



등급 : 메인 퀘스트

제한 : 진태경

임무 : [일류] 경지 달성 (완료)

         Lv.30 달성 (완료)

         명성 500 달성 (475/500)

보상 : [로그아웃]





퀘스트창을 껐다. 한겨울인데 식은땀이 날 것 같다.

‘이렇게 되면 완전 나가린데.’

조금씩 오르던 명성치가 어느 순간 뚝 멈췄다. 그게 반나절 전의 일이다. 처소를 뛰쳐나가 대선 후보처럼 손이 발이 되도록 악수를 하고 다녔지만 기다리던 알림은 울리지 않았다.

‘아니, 알림이 울리긴 했지.’

삐빅!



- [태원진가]에 당신의 명성을 모르는 사람은 없습니다.



이미 한계치까지 명성을 뽑아 먹었으니 적당히 하란 소리였다. 시스템이 보기에도 내 모습이 애잔했던 모양이다.

그렇게 하루가 속절없이 흘렀다. 그리고 오늘은 대망의 출정식이다.

“시파…….”

내가 작게 욕설을 내뱉을 때 진위경은 단상에 오르고 있었다.

수백 쌍의 눈동자가 그를 따라 움직인다. 태원진가의 무사와 새로 합류한 중소 문파의 무사들까지. 대연무장에 도열한 무사들의 숫자는 오백이 넘어갔다.

쿵. 쿵. 쿵.

어느 순간, 거대한 울림이 퍼져 나갔다. 누군가는 발을 구르고 누군가는 병장기를 두드린다. 공력을 지닌 무림인 오백 명이 한뜻으로 움직이자 땅이 흔들리고 굉음이 천지를 메웠다.

‘이게 무슨…….’

지금껏 본 적 없는 광경. 개인에서 하나의 군세(軍勢)가 된 그들은 이제 한 사람의 명령을 기다리고 있었다.

그리고 마침내 진위경의 입이 열렸다.

“부정하지 않겠다. 적들은 병력도, 절정 고수의 숫자도 우리보다 앞선다.”

순식간에 침묵이 내리깔렸다. 하지만 시작부터 사기를 깎아 먹을 정도로 진위경은 멍청한 사람이 아니다. 전신에서 뿜어져 나오는 기백이 바로 그 증거였다.

“그러나.”

평소의 사람 좋은 웃음은 온데간데없다. 지금의 진위경은 절정의 무인인 동시에 태원진가의 수장이었다.

“머릿수만 많은 승냥이에 불과하다. 저자의 무뢰배, 황금에 눈이 먼 낭인과 양민을 약탈하던 마적 떼!”

불길을 토해 내는 외침에 공기가 찌르르 울린다. 이 순간만큼은 나도 피가 끓어오르는 듯했다.

“놈들에게는 명분도, 정의도 없다.”

명분. 정의.

항산검문은 전쟁에 있어 가장 중요한 두 가지를 잃었다.

두 강자의 전쟁에 눈치만 살피던 산서성의 중소 문파들이 지원군을 보낸 이유이기도 했다.

“사흘 안에 이 전쟁은 끝난다.”

천오백의 무인들이 한날한시에 부딪힌다.

서로를 죽고 죽이는 지옥 같은 싸움이 될 것이다.

“이 중 어느 누구도 생사를 장담하지 못한다. 그러나…….”

진위경의 번뜩이는 눈동자가 모두를 담았다.

“우리는 반드시 승리할 것이다.”

다음 순간.

귀가 먹먹할 정도의 함성이 터져 나왔다. 최고조에 달한 분위기 속, 진위경은 거인처럼 우뚝 서 있었다.

“적자생존(適者生存)! 목숨을 걸고 싸워 살아남아라!”

함성은 그 후로도 오랫동안 이어졌다.



* * *



오백의 병력은 선두, 중앙, 후미로 나뉘었다. 핵심이 되는 전력은 대부분 선두와 중앙에 배치되었기 때문에 내가 맡은 후미에는 수십 명의 무사가 전부였다.

그중에는 제법 낯익은 얼굴들도 있었다.

“조장님!”

정찰조원들이다. 나는 반가움 반, 의아함 반으로 물었다.

“너희가 왜 여기 있냐? 약왕당에 있는 거 아니었어?”

“본가의 명운이 걸린 싸움 아닙니까. 조금 다쳤다고 빠질 수야 없죠.”

지난번에 몰래 들렀을 때는 팔다리에 금 간 놈도 있던데. 무림인들 터프한 거 보소.

“조장 밑에 넣어 달라고 요청했더니 상부에서도 흔쾌히 허락하더군요. 그날 이후로 저희도 어깨에 힘 좀 주고 다닙니다, 하하.”

“어쭈.”

피식 웃음이 나왔다. 정찰조 임무를 맡아 며칠을 함께했지만 이 중 몇몇은 이름도 모른다. 그럼에도 친근한 마음이 드는 것은 함께 생사를 함께했다는 동질감 때문이다.

‘하긴, 레이드 세 번이면 의형제도 맺는다는데.’

나는 오래된 헌터 격언을 떠올리며 여덟 명의 정찰조원들을 향해 웃어 보였다. 그리고 문득 생각했다.

‘아니, 잠깐만.’

여덟이라고? 내가 잘못 셌나?

나는 끝에서부터 한 명씩 다시 세기 시작했다. 일단 나를 제외하고 아홉 명. 거기에 혁무진과 한엽은 중상이니까 당연히 오지 못했을 테니 일곱이 되어야 하는데…….

“……너 여기서 뭐 하냐?”

보면서도 이놈이 그놈인가 싶다. 찐빵처럼 부푼 얼굴, 옷 밖으로 드러난 살은 울긋불긋하다.

“보면 모릅니까?”

맞다. 정찰조원 중 이런 싸가지 없는 놈은 하나밖에 없다.

“혁무진?”

“예. 왜요. 뭐요.”

“너 진짜 혁무진 맞아?”

“이젠 제 얼굴도 못 알아봅니까?”

지금 꼴이면 너희 부모님도 못 알아볼걸…….

아니, 그전에 이 자식이 왜 여기 있는 걸까.

“너도 자원했냐?”

“했죠.”

이어 덧붙인다.

“안 받아 줬지만.”

“응?”

“의원한테 말했는데 죽고 싶어서 환장했냐고 화를 내더군요. 그래서 그냥 몰래 빠져나왔습니다.”

나는 진지하게 말했다.

“죽고 싶어서 환장했냐?”

“살고 싶은데요.”

혁무진이 썩은 표정으로 대꾸했다.

“그럼 여길 왜 와?”

“제 몸 상태는 제가 압니다. 충분히 싸울 수 있어요.”

“얼굴은 터지기 직전인데.”

“부기 빠지는 과정입니다. 내상은 전부 나았으니 문제없습니다.”

“외상은?”

“가면서 낫겠죠.”

“…….”

“뼈 몇 군데에 금이 가긴 했는데 버틸 만합니, 컥!”

혁무진이 갑자기 허리를 숙였다. 나는 깜짝 놀라 외쳤다.

“야! 왜 이래?”

“가끔 숨 쉴 때마다 가슴이 아파서…… 아, 이제 괜찮아졌네요.”

“…….”

이거 완전히 미친놈 아냐.

말문이 막힌 내게 혁무진이 말했다.

“아, 한엽 그 녀석은 못 왔습니다. 내상도 안 나아서 짐만 되겠더라고요. 조장? 조장, 지금 제 말 듣고 있는 거 맞죠?”

머릿속에는 한 가지 생각밖에 없었다.

로그아웃, 로그아웃이 시급하다.



* * *



겨울의 밤은 빨리 찾아왔다. 그렇게 해가 저물고 얼마나 걸었을까, 너른 분지(盆地)에 진입한 후에야 야영 준비를 하라는 명령이 떨어졌다.

“어이구, 삭신이야.”

혁무진이 앓는 소리를 냈다. 아무래도 완쾌된 몸이 아니다 보니 힘에 부치는 모양이었다.

“아직 안 늦었는데, 지금이라도 돌아갈래?”

“또 그 소립니까?”

“힘들어 보여서 하는 소리지.”

“착각입니다. 사나이 혁무진이 고작 반나절 걸었다고 지칠 놈으로 보이십니까?”

나는 한 치의 망설임도 없이 고개를 끄덕였다.

“응.”

“절대 아닙니다!”

“음. 정말 안 힘들어? 멀쩡해?”

“예.”

“그럼 가서 애들 야영 준비하는 거나 도와.”

그 순간, 사나이 혁무진이 눈을 부릅뜨며 주저앉았다.

“큭, 조필에게 당한 내상이.”

“…….”

내상 다 나았다며, 이 새끼야.

이놈을 한 대 때려 줘야 하나 고민하던 찰나였다.

“부상자인가?”

달빛 아래 드리워진 거대한 그림자. 슬그머니 고개를 들어 상대를 확인한 혁무진이 눈을 부릅떴다.

“헉, 소가주님!”

진위경이 사단장이면 혁무진은 이등병이다.

다음 순간, 번개처럼 일어나 차렷 자세를 취하는 혁무진의 모습에 진위경이 껄껄 웃었다.

“아직 몸이 성치 않아 보이는데 누워 있게. 아, 내상은 확실히 나은 것 같군. 내가 보증하지.”

“아, 저, 그것이 아니옵고.”

진위경은 쩔쩔매는 혁무진의 어깨를 가볍게 두드려 준 후 나를 향해 돌아섰다.

“잠시 걸을까?”

나는 진위경을 따라 후미진 구석으로 이동했다. 그가 먼저 입을 뗐다.

“몸 상태는 어떠냐?”

“좋습니다.”

레벨 업의 효과를 톡톡히 누렸다. 무시무시한 속도로 완쾌된 육체는 포인트 분배를 통해 더욱 강해졌다.

문제는 따로 있다.

‘명성치가 안 올라.’

아니, 오르긴 오른다. 정말 쥐똥만큼. 조금씩, 아주 조금씩.

지금 속도라면 전투가 벌어지기 전에 로그아웃할 수 있을지 장담하기 어렵다.

‘이대로라면, 말이지.’

마침 진위경이 왔으니 잘됐다. 아까 전부터 생각해 두었던 말을 꺼냈다.

“임무를 맡고 싶습니다.”

다짜고짜 들어온 직진에 진위경의 눈이 동그랗게 떠진다.

“응? 임무?”

“몸도 나았으니 본가를 위해 공을 세우고 싶습니다.”

내 자신이 자랑스럽다. 이런 대사, 이런 거짓말을 당당하게 할 수 있다니.

“지, 진정 그게 네 생각이냐?”

“예.”

진위경의 눈초리가 파르르 떨렸다. 감동의 물결을 온몸으로 느끼고 있는 모양이었다.

‘이거 은근히 죄책감 드네.’

내가 되지도 않는 연기를 한 건 명성치를 위해서다. 정찰 임무라도 나가서 공을 세우면 들어오는 명성치.

항산검문의 정찰대와 맞닥트리면 더욱 좋다. 훌륭한 경험치일 뿐만 아니라 남은 명성치를 모두 채울 수 있을 테니까.

‘본격적인 전투가 일어나면 끝장이다.’

그전에 후딱 로그아웃을 해야 한다. 나는 결의 어린 목소리로 말했다.

“맡겨만 주십시오.”

“어찌 이런 기특한 생각을 했을꼬. 고맙구나, 막내야.”

진위경이 촉촉해진 눈가를 소매로 닦으며 말을 이었다.

“하지만 안 된다.”

“그럼 제게 정찰 임무를, 예?”

“마음만 받으마. 너는 지금처럼 후미를 지켜라.”

이게 뭔 소리야.

멱살이라도 잡고 흔들고 싶은 마음을 간신히 억눌렀다.

“그, 꼭 공을 세우고 싶습니다.”

“이미 차고 넘친다.”

“아뇨, 그게 아니라.”

“지금껏 세운 전공으로도 본가에 큰 힘이 됐다. 그러니 너무 마음 쓰지 말거라.”

“정찰 임무라도 하나 맡겨 주셨으면 좋겠는데요. 앞에 적들이 매복하고 있을 수도 있고…….”

진위경이 허허 웃었다.

“본가의 명운이 걸린 싸움이다. 내가 그런 것 하나 염두에 두지 않았을까.”

“만에 하나 놓치고 간 부분이 있지 않을까요.”

“말 그대로 만에 하나일 뿐이다.”

염병.

되는 일이 하나도 없다. 이러다가 정말 명성치를 못 채우게 되면? 그때는 천오백 명이 투입된 대규모 전투를 치러야 한다.

‘좆 됐다.’

낙담한 내 어깨 위에 크고 따뜻한 뭔가가 닿았다. 진위경의 손이다.

“막내야.”

무거우면서도 쓸쓸한 목소리다. 갑자기 바뀐 분위기에 나는 잠자코 귀를 기울였다.

“네 임무는 우리 중 누구보다 막중하다.”

“제 임무가 뭔데요?”

한참 뜸을 들인 끝에 한마디를 토해 낸다.

“살아남아라.”

“예?”

“어떻게든 살아남아. 본가가 패배한다면 뒤도 돌아보지 말고 도망치란 말이다.”

“…….”

“뿌리가 살아 있다면 나무는 다시 자란다. 둘째와 너는 나보다 훌륭한 뿌리가 될 수 있을 것이다.”

나는 말문이 막혀 한동안 가만히 그의 얼굴을 바라보고만 있었다.

살아남아라. 뿌리가 되어라. 그 어느 때보다 진지하게 와닿는 목소리와 눈빛이었다.

“그게 네 임무다.”

어깨에 얹혀 있던 손바닥이 스르륵 내려갔다. 나는 떠나는 진위경의 뒷모습을 하염없이 바라보았다.
```

### Current accepted English

```markdown
# Chapter 36

> **System**
>
> **Quest**
>
> **Logout**
>
> You must now make your way through this harsh Murim.
>
> Become even stronger, and become famous.
>
> For the day that will one day come…
>
> **Grade:** Main Quest
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Reach the **First Rate** realm (Complete)
>
> Reach Lv. 30 (Complete)
>
> Reach Fame 500 (475/500)
>
> **Reward:** Logout

I closed the Quest Window. It was midwinter, and I still felt like I was about to break into a cold sweat.

*If this keeps up, I’m completely screwed.*

The Fame that had been climbing little by little had suddenly stopped dead. That had been half a day ago. I’d bolted from my quarters and shaken hands like a presidential candidate until I was worn to the bone, but the notification I’d been waiting for never came.

*No, I did get a notification.*

> **System**
>
> — There is no one in the Jin Family of Taiyuan who does not know your Fame.

It was the System’s way of telling me I’d already milked Fame to the limit and should knock it off. Even the System seemed to find me pitiful.

And so the day slipped away, and there was nothing I could do about it. Today was the long-awaited departure ceremony.

“Fuck…”

As I muttered the curse under my breath, Jin Wikyung was climbing onto the platform.

Hundreds of pairs of eyes followed him. Martial artists of the Jin Family of Taiyuan, and martial artists from the small and mid-sized sects that had newly joined us. More than five hundred martial artists stood in formation across the main training ground.

Boom. Boom. Boom.

At some point, a tremendous rumble spread through the air. Some stamped their feet; others struck their weapons. When five hundred martial artists with internal energy moved as one, the earth shook and a roar filled heaven and earth.

*What is this…?*

I had never seen anything like it. They had gone from individuals to a single military force, and now they were waiting for one man’s command.

At last, Jin Wikyung spoke.

“I will not deny it. The enemy is ahead of us in troop numbers and in the number of Peak masters.”

Silence dropped over them in an instant. But Jin Wikyung wasn’t foolish enough to kill morale from the opening. The presence pouring off his entire body was proof of that.

“However.”

His usual good-natured smile was gone without a trace. The Jin Wikyung standing before us was both a Peak martial artist and the head of the Jin Family of Taiyuan.

“They are nothing but jackals with numbers on their side. That man’s rabble—wandering martial artists blinded by gold, and a pack of mounted bandits who have plundered the common people!”

The air crackled under a shout that spat fire. Even I felt my blood boil, if only for that moment.

“They have neither cause nor justice.”

Cause. Justice.

The Mount Heng Sword Sect had lost the two most important things in a war.

That was also why the small and mid-sized sects of Shanxi Province, which had only been watching which way the wind blew in the war between two powers, had sent reinforcements.

“This war will be over within three days.”

Fifteen hundred martial artists would clash at the same hour on the same day.

It would be a hellish fight in which they killed and were killed.

“No one here can guarantee whether they will live or die. However…”

Jin Wikyung’s flashing eyes took them all in.

“We will surely win.”

The next moment.

A roar burst out, loud enough to leave my ears ringing. With the mood at its height, Jin Wikyung stood towering like a giant.

“Survival of the fittest! Fight with your lives on the line, and survive!”

The cheering went on for a long time afterward.

* * *

The five hundred troops were divided into vanguard, center, and rear guard. Most of the core fighting strength had been placed in the vanguard and the center, so the rear I’d been given had only a few dozen martial artists.

Some of the faces were fairly familiar.

“Squad Leader!”

They were members of the reconnaissance squad. Half pleased and half puzzled, I asked,

“Why are you guys here? Weren’t you at Medicine King Hall?”

“This is a battle with the fate of our family at stake. We can’t sit it out just because we’re a little injured.”

Last time I’d snuck over to visit, some of them had still had cracked bones in their arms and legs. Murim people really were tough as hell.

“When we asked to be placed under your command, the higher-ups readily approved it. We’ve been walking around with our chests puffed out ever since that day, haha.”

“Well, look at you.”

I let out a short laugh.

I’d spent several days with them on the reconnaissance mission, but I didn’t even know some of their names. Even so, I felt close to them—we’d been through life and death together.

*They say three raids are enough to make sworn brothers.*

I smiled at the eight reconnaissance-squad members. Then a thought suddenly struck me.

*No, wait.*

Eight? Had I counted wrong?

I started counting again from the end, one person at a time. Not counting me, there were eight. Han Yeop had serious injuries, so he obviously couldn’t have come—but Hyuk Mujin had snuck out to join us.

“…What are you doing here?”

Even looking at him, I wasn’t sure it was the same guy. His face was puffed up like a steamed bun, and the skin showing past his clothes was red and blotchy.

“Can’t you tell by looking?”

He was right. There was only one rude bastard on the reconnaissance squad.

“Hyuk Mujin?”

“Yes. Why? What?”

“Are you really Hyuk Mujin?”

“Can’t you recognize my face anymore?”

*Looking like that, even your parents wouldn’t recognize you…*

No. Before that—why was this bastard here?

“Did you volunteer too?”

“I did.”

He added,

“They didn’t take me, though.”

“Huh?”

“I told the physician, and he got angry and asked if I’d gone insane, wanting to die. So I just snuck out.”

I spoke seriously.

“Have you gone insane, wanting to die?”

“I want to live.”

Hyuk Mujin answered with a look like something had gone sour.

“Then why did you come here?”

“I know my own condition. I can fight well enough.”

“Your face looks like it’s about to burst.”

“The swelling is going down. My internal injuries have all healed, so there’s no problem.”

“What about the external injuries?”

“They’ll heal on the way.”

“…”

“A few bones are cracked, but I can handle i—kh!”

Hyuk Mujin suddenly bent forward at the waist. Startled, I shouted,

“Hey! What’s wrong?”

“Sometimes my chest hurts whenever I breathe… Ah, it’s fine now.”

“…”

Was this guy completely insane?

As I stood there speechless, Hyuk Mujin said,

“Ah, Han Yeop couldn’t come. His internal injuries haven’t healed, so he’d only be a burden. Squad Leader? Squad Leader, you are listening to me, right?”

There was only one thought in my head.

*Logout. Logout is urgent.*

* * *

Winter night came early. After the sun went down, we walked for who knew how long, and only after we entered a wide basin did the order come to prepare camp.

“Ugh, every bone in my body hurts.”

Hyuk Mujin groaned. Since he clearly wasn’t fully recovered, the march seemed to be too much for him.

“It’s not too late. Want to turn back even now?”

“Are you saying that again?”

“I’m saying it because you look like you’re struggling.”

“You’re mistaken. Does Hyuk Mujin the man look like someone who’d get tired from walking a mere half day?”

I nodded without the slightest hesitation.

“Yep.”

“Absolutely not!”

“Hmm. You’re really not tired? You’re fine?”

“Yes.”

“Then go help the others prepare camp.”

At that moment, Hyuk Mujin the man snapped his eyes wide and sank to the ground.

“Ugh, the internal injuries I took from Jopil…”

“…”

*You said your internal injuries had healed, you bastard.*

I was wondering whether I ought to hit him when a voice cut in.

“Is he injured?”

A massive shadow stretched under the moonlight. Hyuk Mujin cautiously lifted his head to see who it was, then his eyes flew open.

“Gasp, Lesser Family Head!”

If Jin Wikyung was a division commander, Hyuk Mujin was a private.

The next moment, Hyuk Mujin sprang to his feet like lightning and stood at attention. Jin Wikyung burst out laughing.

“You still don’t look fully recovered. Lie back down. Ah, the internal injuries do seem fully healed. I’ll vouch for that.”

“Ah, I, that isn’t…”

Jin Wikyung gave the flustered Hyuk Mujin’s shoulder a light pat, then turned to me.

“Shall we walk for a bit?”

I followed Jin Wikyung to a secluded corner. He spoke first.

“How’s your condition?”

“It’s good.”

I’d gotten full use out of the level-up. My body had recovered at a terrifying speed, and distributing my points had made it even stronger.

The problem was something else.

*My Fame isn’t going up.*

No, it was going up. Really, by about a rat dropping. Little by little. Very, very little.

At this rate, I couldn’t guarantee I’d be able to log out before the fighting started.

*If it stayed like this, I mean.*

Jin Wikyung showing up now was convenient. I brought up what I’d been thinking for a while.

“I want to take on a mission.”

His eyes went round at how bluntly I’d come out with it.

“Hm? A mission?”

“Now that I’ve recovered, I want to distinguish myself for our family.”

I was proud of myself. To think I could deliver a line like that—a lie like that—with a straight face.

“I-is that truly what you think?”

“Yes.”

The corners of Jin Wikyung’s eyes trembled. He looked like a wave of emotion was running through his whole body.

*This is actually making me feel kind of guilty.*

The reason I was putting on this unconvincing act was Fame. If I went out on even a reconnaissance mission and distinguished myself, Fame would come in.

It would be even better if I ran into a reconnaissance unit from the Mount Heng Sword Sect. Not only would that be excellent EXP, I’d be able to fill all the Fame I had left.

*Once the real battle starts, it’s over.*

I had to log out, and fast, before then. I spoke in a voice full of resolve.

“Just leave it to me.”

“How could you have thought of something so admirable? Thank you, my youngest brother.”

Jin Wikyung wiped the damp corners of his eyes with his sleeve and went on.

“But no.”

“Then a reconnaissance mission for me, please?”

“I’ll take the sentiment. You guard the rear as you are now.”

*What is he talking about?*

I barely held down the urge to grab him by the collar and shake him.

“I-I really want to distinguish myself.”

“You’ve already done more than enough.”

“No, that’s not what I mean.”

“The merits you’ve earned so far have already been a great help to our family. So don’t trouble yourself over it.”

“I’d like you to give me even one reconnaissance mission. There could be enemies lying in ambush ahead…”

Jin Wikyung laughed softly.

“This is a battle with our family’s fate at stake. Do you think I wouldn’t have accounted for something like that?”

“Might there not be a one-in-ten-thousand chance we missed something?”

“That is, quite literally, one in ten thousand.”

*Damn it.*

Nothing was going my way. If I really failed to fill my Fame at this rate? Then I’d have to fight a large-scale battle with fifteen hundred people committed.

*I’m fucked.*

Something large and warm settled on my dejected shoulder. Jin Wikyung’s hand.

“Youngest.”

His voice was heavy and lonely. At the sudden change in mood, I kept quiet and listened.

“Your mission is graver than anyone else’s among us.”

“What’s my mission?”

After letting it hang for a long time, he forced out a single word.

“Survive.”

“Huh?”

“Survive however you can. If our family loses, run without looking back.”

“…”

“If the roots live, the tree will grow again. Second Brother and you could become better roots than I.”

I was speechless. For a long while, I could only stare at his face.

Survive. Become roots.

His voice and eyes hit home with more seriousness than ever before.

“That is your mission.”

The palm resting on my shoulder slid slowly down. I stared after Jin Wikyung’s departing back, unable to look away.
```
## Chapter 37

### Korean source

```text
＃37화



이동은 순조로웠다. 지난번 정찰 임무 때 내린 폭설은 녹아 없어진 지 오래였고 지휘부는 병력의 힘을 최대한 비축시키며 이동했다.

“지금 속도라면 늦어도 내일 정양(定壤)에 도착하겠군요.”

어쩐지 낯익은 남자의 말에 나는 눈을 껌뻑거렸다.

“누구신지?”

복색을 보아하니 태원진가 쪽 사람은 아니다. 내가 있는 후미에는 정찰조원들을 제외하면 새로 합류한 중소 문파의 무사들이 대다수였으니 당연했다.

“삼도문의 곽준이라 합니다. 일전에 한 번 인사를 드렸었는데…… 손도 잡았었죠.”

삼도문의 곽준? 기억이 날 듯 말 듯 한데.

명성치 올리려고 잡은 손이 한 둘이냐. 아마 그들 중 하나였겠지.

“죄송합니다. 제가 기억력이 좀 안 좋아서.”

“사실 기대도 안 했습니다. 하하.”

친근한 웃음을 지어 보인 곽준이 재차 입을 열었다

“사실 처음에는 후미에 배치되었다는 사실에 실망했습니다.”

“왜요?”

“공을 세울 기회가 적어지니까요. 저 같은 무명 소졸이 이름을 알릴 기회 아니겠습니까?”

“아, 예.”

이런 경우는 둘 중 하나다. 정말 많은 전투를 겪어서 강심장이 됐거나, 겁이 없는 놈이거나. 나는 [기감]을 끌어올렸다.

띠링.



[Lv.40 곽준]



오, 한가락 하는데?

40레벨이면 최소 일류다. 나 고수라고 큰소리 뻥뻥 치지는 못해도 후미에만 처박혀 있는 게 억울할 정도는 된다.

“적들의 병력 중 절반은 급하게 충원된 자들입니다. 별의별 쭉정이들까지 끌어들인 데다 본대에 합류하기 위해 강행군을 했을 테니 태원진가와 삼도문의 정예들에게는 상대도 안 되겠지요.”

말은 제법 그럴듯하다. 삼도문이 정예라는 걸 빼면.

나는 건성으로 고개를 끄덕였다.

“그렇군요.”

“적들보다 뛰어난 절정 고수들도 있지요. 소가주님과 위 대협도 계시지만 화양검(火魎檢)의 무명은 중원 전체에 퍼져 있지 않습니까.”

화양검. 처음 듣는 별호였지만 누군지 짐작할 수 있었다.

태원진가의 절정 고수는 셋이고 진위경과 위팽을 제외한다면 남는 건 한 사람뿐이니까.

‘대장로.’

그 노인네가 그 정도였나?

이어지는 곽준의 말은 찬양 일색이었다. 수십 년 전, 젊은 시절의 대장로가 베어 넘긴 고수들의 별호와 이름이 수도 없이 흘러나왔다.

“정마대전이 낳은 영웅이셨죠.”

과거의 전쟁 영웅이라. 곽준의 말만 들어 보면 정의를 사랑하고 불의를 보면 못 참는 협객 중의 협객인데…….

‘난 왜 볼 때마다 찝찝할까.’

첫인상 때문인지 몰라도 나는 대장로가 싫었다.

특유의 분위기와 상대방을 뚫어 보는 묘한 눈빛. 진위경에 맞서 정치적 파벌을 이루고 있다는 것까지.

하지만 그 후로 대장로는 진위경을 전폭적으로 지지해 주었고, 태원진가는 안팎으로 똘똘 뭉칠 수 있었다.

‘하긴, 외적이 침입하면 집안싸움도 멈춰야지.’

현재 대장로는 진위경과 함께 선두를 이끌고 있다. 그가 소문만큼의 고수라면 내일의 전투가 한층 수월해질 것이다.

“내일 화양검 대협께서 전장을 휩쓸 모습을 생각하니 벌써부터 가슴이 뛰는군요.”

곽준은 사흘 만에 소변본 사람처럼 몸을 부르르 떨었다.

이 자식은 긴장감이란 걸 모르나? 더군다나 우리가 이길 거라는 자신감은 어디서 나온 건지 모르겠다.

“승리를 확신하시는군요.”

“지면 큰일이죠.”

“예?”

큰일이 아니라 끝장나는 거 아니냐. 항산검문이 지금까지 해 왔던 짓을 보면 태원진가는 물론이고 우리 쪽에 가담한 중소 문파들까지 쑥대밭으로 만들 것 같은데.

“그게 무슨…….”

“농담입니다.”

이 자식도 또라이네. 어이없어하는 내게 곽준이 씩 웃어 보였다.

“이깁니다. 우리가.”

확신에 찬 한마디였다.

곽준이 그 말을 끝으로 멀어지자 혁무진이 다가와 물었다.

“누굽니까?”

“40레벨.”

“예?”

“있어. 자신감 넘치는 놈이.”

여러모로 마음에 안 드는 놈이다. 뭐, 이제 대화를 나눌 일도 없겠지만.



* * *



시간은 빠르게 흘렀다. 진군을 시작한 지 이틀째 되는 밤, 우리는 혼주에 도착했고 진위경은 지휘부를 모아 회의를 열었다. 그의 손에는 작은 종이가 쥐어져 있었다.

“하오문에서 보낸 전서요. 이틀 전 적들의 원군이 오태산을 넘었다는군.”

“그렇다면…….”

“지금쯤, 혹은 내일 중에 본대와 합류할 가능성이 높소.”

뭐지? 이해할 수가 없다. 원군이 합류하기 전에 본대를 쳤다면 훨씬 수월한 싸움이 됐을 텐데.

‘생각해 둔 게 있겠지.’

아니나 다를까, 이어지는 진위경의 말이 있었다.

“새로 합류한 적들의 원군은 지쳐 있고 식량은 바닥을 드러내고 있소. 내일 우리가 앞서 정양의 유리한 고지를 점하면 항산검문주는 고민할 거요. 물러서느냐. 부딪치느냐.”

다음 순간 진위경의 시선이 나를 향했다.

“그가 어떤 선택을 할까?”

순간 당황했지만 답은 나와 있다. 이제 와서 물러설 위인이었다면 이미 한참 전에 물러났겠지.

“부딪칠 것 같은데요.”

두 배에 달하는 병력, 절정 고수의 숫자도 밀리지 않는다. 적으로서는 속전속결로 이 싸움을 끝내려 할 것이다.

“바로 보았다.”

흐뭇하게 웃은 진위경이 탁자에 놓인 지형도를 짚어 나갔다.

“적들이 정양으로 진입할 수 있는 길은 네 곳. 허나 식량 사정이 여의찮은 그들은 가장 빠른 길을 선택하겠지.”

손가락이 멈춘 곳에는 팔천협(八天峽)이라는 지명이 적혀 있었다. 그때, 조용히 자리를 지키고 있던 대장로가 처음으로 말문을 열었다.

“팔천협이라. 항아리 모양에 입구가 좁고 가파른 곳이지. 마적 떼들은 애마를 버려야겠구려.”

“목숨도 버리고 가야지요.”

“적들도 목숨을 불사하고 싸울 터, 이 정도로는 부족하오.”

“협곡 위 절벽에 각궁 백여 자루를 숨겨 두었습니다.”

“허어.”

막사 안이 술렁였다. 나도 입을 벌리고 진위경을 바라봤다.

아니, 도대체 그건 언제 숨겨 뒀대?

“혼주에서의 승리 직후였습니다. 수완 좋은 조력자 덕분이지요.”

진위경이 나를 똑바로 바라보며 말했다.

‘하오문. 월화구나.’

보이지 않는 곳에서 끊임없이 도움을 주고 있다. 물론 이 정도까지 큰 그림을 그린 진위경도 대단하다.

‘존나 멋있어.’

저 인간 분쇄기 같은 덩치에 명석한 두뇌라니. 갑자기 형이라고 부르고 싶어진다.

“오오.”

“소가주……!”

시커먼 사내놈들의 뜨거운 시선에 막사가 후끈 달아오른다.

진위경이 묵직한 눈빛으로 좌중을 훑었다.

“이제 결착을 냅시다.”

이견은 없었다. 가장 먼저 자리에서 일어난 대장로가 진위경을 향해 포권을 취했다.

“존명.”

그렇게 회의가 끝났다. 막사를 나오는 내 귓가로 익숙한 목소리가 파고들었다.

- 어제 했던 말, 잊지 말거라.

순간 몸이 굳는다. 하지만 이내 작게 고개를 끄덕여 보였다.

그리고 그날 새벽, 태원진가의 무사 삼백과 중소 문파의 지원군 백오십. 도합 사백오십의 병력이 협곡을 향해 떠났다.

‘그래도 마지막인데, 인사도 제대로 못 했네.’

나는 언덕에 올라 굽이치는 횃불을 하염없이 바라보았다.



* * *



다음 날 아침, 나를 본 혁무진이 흠칫 놀라며 물러났다.

“깜짝이야. 무슨 일이에요?”

“뭐가?”

“뭐긴요. 얼굴이 산송장 같아요. 안 주무셨어요?”

“아냐. 조금 잤어.”

거짓말이다. 사실 한숨도 못 잤다. 바위에 틀어 앉아 밤이 새도록 시스템창만 들여다보고 있었다.

마침내 코앞으로 다가온 그 순간을 손꼽아 기다리며.



명성 500 달성 (497 / 500)



숫자 1이 이렇게 소중하게 느껴질 줄이야.

나는 부쩍 늙어 버린 목소리로 중얼거렸다.

“간다, 간다, 이제 집 간다…….”

“이제는 혼잣말까지 하네. 실성했어요?”

쯧쯧. 혀를 차던 혁무진이 눈을 동그랗게 떴다.

“그건 뭐예요? 못 보던 물건인데.”

“이거?”

나는 바위에 올려 둔 낡은 서책과 조그마한 함을 차례대로 가리켰다.

“하나는 비급. 하나는 영단.”

“헉. 진짜요?”

반쯤 눈이 튀어나온 녀석에게 힘없이 설명해 주었다.

“비급은 초절정 무공이고, 영단은 잘만 흡수하면 반 갑자.”

“예?”

“그런데 영단 잘못 먹으면 타 죽는다더라. 너 먹을래?”

“아, 예에…….”

시큰둥한 얼굴과 댓 발 튀어나온 주둥이를 보아하니 내 말을 쥐뿔도 안 믿는 것 같다.

하긴, 난데없이 초절정 무공에 반 갑자짜리 파이어볼 영단이라고 하니 장난으로 생각할 만도 하지.

“진짜 안 먹어? 좋은 건데.”

“어이구, 됐습니다. 초절정 무공 많이 익히시고 영단 꼭꼭 씹어 드십쇼.”

“난 이제 이런 거 필요 없어.”

“그럼요. 잠룡이신데.”

평소 같았으면 뒤통수라도 한 대 후려쳐 줬을 텐데. 지금은 별 느낌 없다.

‘이게 말년 병장의 기분인가?’

동시에 기분이 이상해졌다. 워낙 많은 일을 겪은 후유증인가? 한 달 남짓인데 일 년은 있었던 것처럼 아련하다.

나는 과거의 기억을 더듬어 나갔다.

‘처음 홍화루에서 눈을 떴지.’

그곳에서 월화를 처음 만났고 이 게임에 갇혔다는 사실을 깨달았다. 그때만 생각하면 지금도 소름이 끼친다.

‘진짜 미쳐 버리는 줄 알았는데.’

태원진가에 오기로 결심하는 데만 사흘이 걸렸다. 거기서 만난 게 이 녀석, 혁무진이다.

빡!

“억! 왜 때려요?”

“음. 그냥 옛날 생각이 나서.”

“옛날 언제요?”

“안 돼. 안 알려 줘. 빨리 돌아가.”

“무슨 뒷골목 파락호예요? 무공 좀 세다고 이렇게 사람을 핍박해도 되는 겁니까?”

혁무진이 길길이 날뛰자 사람들의 시선이 우리를 향해 쏠렸다. 강 건너 불구경하던 정찰조원들까지 끼어들었다.

“두 분이서 무슨 얘기 중이에요?”

“몰라. 부조장이 잘못했겠지.”

“야, 난 아무것도 안 했어!”

“무림이잖아. 약한 게 죄야.”

“그런데 우리 이러고 있어도 되는 겁니까?”

누군가의 말에 순간 침묵이 흘렀다.

“그러게. 여기서 대기하는 게 우리 임무긴 한데…….”

억지웃음으로 억누르고 있던 긴장과 두려움이 감돈다. 곧 현실로 돌아갈 나조차 진위경의 모습이 어른거려 찝찝한 마당에 이 녀석들이야 오죽하겠나. 내가 해 줄 말은 하나밖에 없다.

“난 형님을 믿는다.”

형님. 이번만큼은 그 단어에 진심을 실었다. 이곳에서 내게 가장 큰 힘이 되어 주었던 진위경이다. 이렇게라도 찝찝함을 털어 내고 싶었던 것일지도 모르겠다.

잠깐 굳어 있던 사람들의 얼굴이 풀렸다.

“저희도 마찬가집니다.”

혁무진도 슬쩍 끼어들었다.

“전 조장을 더 믿습니다.”

“와, 부조장 줄 갈아타는 솜씨가 아주.”

“이 자식들이. 여기 조장한테 목숨 빚지지 않은 놈 있어?”

“에이, 그렇게 말씀하시면 또 할 말이 없죠.”

“저도 조장 믿습니다. 사실 전 조장이 망나니 행세할 때도 다 알고 있었어요. 아, 저 사람은 잠룡이구나. 딱 감이 왔죠.”

기분이 묘했다. 마른오징어도 짜면 물이 나온다더니, 게임에서 NPC들을 상대로 이런 감정을 느낄 줄이야.

‘뭐, 솔직히…… 기분이 나쁘진 않네.’

문득 저 산 너머에 있을 진위경이 궁금했다. 전투가 시작됐는지, 시작됐다면 어느 쪽이 이기고 있는지.

그리고 그런 생각을 한 것은 나 혼자만이 아니었다.

“지금쯤이면 전투가 시작됐겠군요.”

삼도문의 곽준이다. 지금까지와는 달리 그는 흑색 무복을 걸치고 있었다.

‘저 녀석이 원래 저 옷이었던가?’

내 시선에 곽준이 어깨를 으쓱했다.

“전 이런 게 좋더라고요. 움직이기에도 편하고, 피 좀 튀어도 티도 안 나고. 자네들도 그렇지?”

마지막 질문은 우리를 향한 것이 아니었다. 곽준이 이끄는 삼도문의 무사들. 빠짐없이 흑의로 갈아입은 그들이 과묵하게 고개를 끄덕였다.

“그렇다는군요.”

만족스럽게 웃은 곽준이 내게 고개를 돌렸다.

“자, 이제 저희도 출발해 볼까요?”

이 새끼가 지금 뭐라는 거지?
```

### Current accepted English

```markdown
# Chapter 37

The march went smoothly. The heavy snow that had fallen during our last reconnaissance mission had melted away long ago, and command moved us while conserving as much of the troops’ strength as possible.

“At this rate, we’ll arrive in Jeongyang by tomorrow at the latest.”

I blinked at the oddly familiar man’s words.

“Who are you?”

Judging by his clothes, he wasn’t from the Jin Family of Taiyuan. Aside from the reconnaissance squad, most of the people in the rear guard were martial artists from the newly allied small and mid-sized sects, so that made sense.

“I’m Gwak Jun of the Three Paths Sect. We met once before… We even shook hands.”

Gwak Jun of the Three Paths Sect? It was on the tip of my tongue.

*It wasn’t as if I’d shaken only one or two hands trying to raise my Fame.*

He was probably one of them.

“Sorry. My memory isn’t very good.”

“I wasn’t expecting you to remember, honestly. Haha.”

Gwak Jun gave me a friendly smile and went on.

“To be honest, I was disappointed at first when I found out we’d been assigned to the rear guard.”

“Why?”

“Because there’d be fewer chances to distinguish ourselves. Isn’t this the chance for an unknown grunt like me to make a name for himself?”

“Ah. Right.”

There were two possibilities in cases like this. Either he’d been through so many battles that he’d grown nerves of steel, or he was simply fearless.

I raised my **Qi Sense**.

Ding.

> **System**
>
> **Lv.40 Gwak Jun**

*Oh. He’s got some skill.*

At Level 40, he was at least First Rate. He couldn’t exactly go around bragging he was a master, but it was more than enough to feel wronged about being stuck in the rear.

“Half of the enemy troops were recruited in a hurry. They’ve dragged in every kind of deadweight, and they must have force-marched to join the main force. They won’t stand a chance against the elites of the Jin Family of Taiyuan and the Three Paths Sect.”

His words sounded plausible enough.

*If you leave out the part about the Three Paths Sect being elite.*

I nodded half-heartedly.

“I see.”

“And we have Peak masters superior to the enemy’s as well. There’s the Lesser Family Head and Great Hero Wipeng, of course, but the reputation of the Blade of Flowers has spread throughout the Central Plains, hasn’t it?”

The Blade of Flowers. It was the first time I’d heard the title, but I could guess who he meant.

The Jin Family of Taiyuan had three Peak masters. Exclude Jin Wikyung and Wipeng, and only one person was left.

*The Head Elder.*

*Was that old man really that strong?*

Gwak Jun’s next words were nothing but praise. Title after title, name after name of masters the Head Elder had cut down in his youth, decades ago, came spilling out.

“He was a hero born of the Great Faction War.”

A war hero from the past. Listening to Gwak Jun, he sounded like a chivalrous hero among chivalrous heroes—a man who loved justice and couldn’t stand to see injustice go unpunished…

*Then why do I feel so uneasy every time I see him?*

Maybe it was the first impression, but I disliked the Head Elder.

That peculiar air of his. The strange gaze that bored straight through people. The fact that he had formed a political faction against Jin Wikyung.

And yet after that, the Head Elder had thrown his full support behind Jin Wikyung, and the Jin Family of Taiyuan had been able to pull tight together, inside and out.

*Well, when an outside enemy invades, even family feuds have to stop.*

The Head Elder was currently leading the vanguard alongside Jin Wikyung. If he really was as skilled as the rumors claimed, tomorrow’s battle would be that much easier.

“Just thinking of Great Hero Blade of Flowers sweeping the battlefield tomorrow already has my heart racing.”

Gwak Jun shuddered like a man taking a piss after three days.

*Does this bastard not know what tension is?*

And where was he getting the confidence that we were going to win?

“You’re certain of victory.”

“If we lose, we’re in big trouble.”

“Excuse me?”

*Not big trouble. We’d be finished.*

Judging by everything the Mount Heng Sword Sect had done so far, they would turn not only the Jin Family of Taiyuan but the small and mid-sized sects allied with us into a wasteland.

“What do you mean by—”

“I’m joking.”

*This bastard’s a lunatic too.*

As I stared at him, speechless, Gwak Jun flashed me a grin.

“We’ll win. We will.”

One sentence, packed with conviction.

When Gwak Jun left it at that and moved away, Hyuk Mujin came up and asked,

“Who was that?”

“Level 40.”

“What?”

“There’s this guy. Overflowing with confidence.”

I didn’t like him, in more ways than one.

*Well, it wasn’t as though I’d have to talk to him again.*

* * *

Time passed quickly. On the second night after we began the march, we reached Honju, and Jin Wikyung gathered the command staff for a meeting. He was holding a small slip of paper.

“A letter from the Lower District Sect. The enemy reinforcements crossed Mount Otae two days ago.”

“Then…”

“They’re likely to join the main force around now, or sometime tomorrow.”

*What?*

I couldn’t understand it. If we had attacked the main force before the reinforcements joined them, the fight would have been much easier.

*He must have something in mind.*

Sure enough, Jin Wikyung went on.

“The enemy reinforcements that just joined them are exhausted, and their food is running out. If we take Jeongyang’s high ground first tomorrow, the Mount Heng Sword Sect Leader will have a choice to make. Fall back, or clash.”

The next moment, Jin Wikyung’s gaze shifted to me.

“What choice do you think he’ll make?”

I was caught off guard, but the answer was already there. If he were the kind of man to fall back at this point, he would have done so long ago.

“I think he’ll clash.”

Twice our numbers, and they weren’t behind us in Peak masters either. From the enemy’s side, they would want to end this fight as fast as possible.

“Exactly.”

Jin Wikyung smiled, pleased, and traced a finger across the topographic map on the table.

“There are four routes the enemy can take into Jeongyang. But with their food situation as it is, they’ll choose the fastest one.”

His finger stopped on a place labeled Eight Spring Gorge. The Head Elder, who had been sitting quietly until then, spoke for the first time.

“Eight Spring Gorge. Jar-shaped, with a narrow, steep mouth. The mounted bandits will have to abandon their prized horses.”

“They’ll have to abandon their lives too.”

“The enemy will fight with their lives on the line as well. This much won’t be enough.”

“I’ve hidden some hundred horn bows on the cliffs above the gorge.”

“Hoh.”

A stir ran through the tent. I stared at Jin Wikyung with my mouth open.

*When the hell did he hide those?*

“Right after our victory at Honju. Thanks to a resourceful ally.”

Jin Wikyung looked straight at me as he said it.

*The Lower District Sect. Wolhwa.*

She had been helping us constantly from places we couldn’t see. Of course, Jin Wikyung was impressive too, for drawing a picture this big.

*That’s fucking cool.*

A build like a human meat grinder, and a sharp mind to go with it. Suddenly I wanted to call him big brother.

“Oh!”

“The Lesser Family Head…!”

The tent went hot under the burning gazes of those dark, burly men.

Jin Wikyung swept a heavy look over everyone assembled.

“Let’s settle this.”

No one objected. The Head Elder was the first to rise, then gave Jin Wikyung a fist-in-palm salute.

“By your command.”

That was the end of the meeting. As I left the tent, a familiar voice bored into my ear.

—Don’t forget what I told you yesterday.

I stiffened for a moment. Then I gave a small nod.

And at dawn that day, three hundred martial artists from the Jin Family of Taiyuan and one hundred fifty reinforcements from the small and mid-sized sects—four hundred fifty in all—set out for the gorge.

*Still, this was the end, and I hadn’t even said a proper goodbye.*

I climbed a hill and stared endlessly at the winding line of torches.

* * *

The next morning, Hyuk Mujin flinched when he saw me and stepped back.

“You startled me. What’s going on?”

“What?”

“What do you mean, what? You look like a living corpse. Did you not sleep?”

“Nah. I slept a little.”

That was a lie. I hadn’t slept a wink. I had planted myself on a rock and stared at the System Window all night.

Counting down to the moment that had finally come right up to my nose.

> **System**
>
> Achieve Fame 500 (497/500)

I never thought the number 1 could feel this precious.

In a voice that had aged all of a sudden, I muttered,

“I’m going, I’m going, going home now…”

“Now you’re even talking to yourself. Have you lost your mind?”

Hyuk Mujin clicked his tongue, then his eyes went round.

“What’s that? I’ve never seen those before.”

“This?”

I pointed in turn at the old book and the small case sitting on the rock.

“One’s a martial arts manual. The other’s an elixir.”

“Hah. Really?”

I explained it weakly to the guy whose eyes were halfway out of his head.

“The manual’s a Supreme Peak martial art, and if you absorb the elixir right, it’s thirty years.”

“What?”

“But they say if you take the elixir wrong, you’ll burn to death. You want it?”

“Ah. Sure…”

Judging by that unimpressed face and the snout sticking out a good few feet, he didn’t believe a damn word I was saying.

*Well, if someone suddenly came at me with a Supreme Peak martial art and a thirty-year Fireball elixir, I’d figure it was a joke too.*

“You really won’t eat it? It’s good stuff.”

“Oh, I’m fine. Learn plenty of that Supreme Peak martial art, and be sure to chew your elixir thoroughly.”

“I don’t need this kind of thing anymore.”

“Of course. You’re the Sleeping Dragon.”

Normally I would have smacked him in the back of the head. Right now I didn’t feel much of anything.

*Is this how a short-timer sergeant feels?[^1]*

At the same time, I felt strange. Was it the aftereffect of everything I’d been through? It had only been a little over a month, but it felt distant, as if I’d been here a year.

I started tracing back through old memories.

*I first opened my eyes at Honghwaru.*

That was where I met Wolhwa for the first time and realized I was trapped in this game. Even now, thinking about that moment gave me goose bumps.

*I really thought I was going to lose my mind.*

It had taken me three days just to decide to go to the Jin Family of Taiyuan. And the guy I met there was this one—Hyuk Mujin.

Smack!

“Argh! Why did you hit me?”

“Hmm. Just thought of the old days.”

“What old days?”

“Nope. Not telling. Get back already.”

“What am I, some back-alley punk? Just because your martial arts are a bit strong, you think you can oppress people like this?”

As Hyuk Mujin threw a fit, everyone’s eyes turned toward us. Even the reconnaissance-squad members who had been watching like it was none of their business jumped in.

“What are you two talking about?”

“Dunno. The deputy squad leader must have done something wrong.”

“Hey, I didn’t do anything!”

“This is Murim. Being weak is a crime.”

“But should we even be doing this?”

At someone’s words, silence fell for a moment.

“True. Waiting here is our mission, but…”

The tension and fear they had been holding down with forced smiles hung in the air. Even I, who would soon be going back to the real world, felt uneasy with Jin Wikyung’s face flickering through my mind. How much worse must it be for these guys?

There was only one thing I could say.

“I trust my big brother.”

*Big brother.* This time, I put my heart into the word.

Jin Wikyung had been the greatest source of strength I’d had in this place. Maybe I simply wanted to shake off that unease, even if only like this.

The faces that had stiffened for a moment eased.

“We feel the same.”

Hyuk Mujin slipped in as well.

“I trust the squad leader more.”

“Wow. Deputy squad leader, that side-switching of yours is really something.”

“You little bastards. Is there anyone here who doesn’t owe the squad leader their life?”

“Well, when you put it that way, what can we say?”

“I trust the squad leader too. Honestly, I knew all along, even when you were playing the thug. I thought, *Ah, that man is the Sleeping Dragon.* I could tell right away.”

I felt strange.

*They say even dried squid gives water if you squeeze it. Who knew I’d feel something like this toward NPCs in a game?*

*Well, honestly… it doesn’t feel bad.*

Suddenly I wondered about Jin Wikyung, somewhere beyond those mountains. Had the battle started? If it had, which side was winning?

And I wasn’t the only one thinking that.

“By now, the battle must have started.”

It was Gwak Jun of the Three Paths Sect. Unlike before, he was wearing black martial robes.

*Was that what this guy originally wore?*

At my look, Gwak Jun shrugged.

“I like this sort of thing. Easy to move in, and even if a little blood splatters, it doesn’t show. You all feel the same, right?”

That last question wasn’t aimed at us. It was for the martial artists of the Three Paths Sect whom he led. Every last one of them had changed into black, and they nodded without a word.

“Apparently so.”

Gwak Jun smiled, satisfied, then turned to me.

“Well, shall we set out too?”

*What the fuck is this bastard talking about right now?*

[^1]: A conscript sergeant in the last stretch of mandatory service, coasting toward discharge.
```
## Chapter 38

### Korean source

```text
＃38화



처음에 드는 감정은 의아함이었다.

“출발?”

곽준이 대답했다.

“예. 이쪽에서도 슬슬 움직여 줘야 시간에 맞출 수 있거든요.”

종잡을 수 없는 그의 말에 혁무진이 나섰다.

“거기, 삼도문 양반. 뭘 잘못 알고 있나 본데, 우리 임무는 여기 계신 공자님과 함께 후미에서 대기하는 거요.”

“아, 정말입니까?”

곽준이 눈을 동그랗게 떴다. 그 반응에 정찰조원들이 그럼 그렇지, 하는 얼굴로 고개를 끄덕였다.

“잘못 알고 있었나 보군.”

“그럴 수 있지. 암. 그럴 수 있어.”

하지만 내 생각은 달랐다.

‘그럴 수 있긴 뭘 그럴 수 있어.’

현재 후미에 남아 있는 삼도문의 무사는 스물. 그중 우두머리 격인 인물이 바로 곽준이다.

‘그런 놈이 명령을 헷갈려?’

분명 기분 나쁜 놈이지만 그 정도로 멍청해 보이진 않는다.

불길함이 스멀스멀 올라와 온몸을 휘감는다.

“곤란하군요. 제가 받은 임무는 좀 달라서요.”

“어떻게 다르지?”

말과 동시에 혁무진의 발을 지그시 밟았다. 하루에도 수십 번씩 까불거리는 녀석이지만 바보는 아니다. 내 신호를 알아들은 혁무진의 눈이 커졌다.

“조장. 발 좀 치워 주세요. 아파요.”

“…….”

이런 시벌.

어이없어하는 나를 보며 곽준이 입꼬리를 말아 올렸다.

“눈치가 빠르시군. 아니면 수하들이 멍청한 건가? 뭐, 아무튼. 그분께서 하신 말씀을 그대로 들려주지.”

다음 순간, 곽준의 얼굴에서 웃음기가 사라졌다. 냉정하고 무감각한 눈빛의 살인자가 말을 이었다.

“모두 제거하고 본대에 합류하라.”

차차창!

말이 떨어짐과 동시에 수십 개의 검광이 치솟았다. 곽준이 이끄는 삼도문의 무사 스무 명. 그리고 반 박자 늦게 검을 뽑아 든 정찰조원들 사이로 살기와 긴장감이 감돌았다.

“이 자식들이 미쳤나…….”

빠드득, 혁무진이 이를 갈며 놈들을 노려봤다.

“네놈들이 감히 본가를 배신해? 죽고 싶어 환장한 것이냐!”

“배신? 죽어? 단단히 착각하고 있군.”

곽준의 입가에 비웃음이 떠올랐다.

“배신한 적도, 죽을 일도 없다. 네놈들 따위한테는 더더욱.”

“이 새끼가!”

눈이 뒤집힌 혁무진이 곽준을 향해 몸을 날렸다. 아니, 날리려고 했다.

“가만히 있어.”

“조장?”

혁무진이 눈을 부릅떴다.

“삼도문입니다. 이류 문파 쭉정이들이라고요! 당장 저놈들을 아작 내고…….”

“아니야.”

“예?”

“쭉정이가 아니라고.”

예리한 기세와 살기등등한 눈빛. 지금까지 봐 왔던 일개 중소 문파의 무사들이 아니다. 시스템은 그 의심을 확신으로 바꿔 주었다.



[Lv.30]



기감을 통해 읽어 낸 놈들의 평균 레벨이다.

하나하나가 일류의 무인들. 젠장, 이런 놈들과 사흘을 함께 있었는데 까맣게 몰랐다.

‘로그아웃에만 너무 정신이 팔려 있었어.’

방심한 결과다. 나는 입술을 깨물며 놈들을 바라봤다. 정확히 말하면 놈들의 등 뒤로 우거진 풀숲을.

아주 미세한 움직임이었지만 내 눈을 피해 갈 수는 없다.

‘숨어 있군.’

[기감]의 범위 밖이라 확인할 수 없지만, 직감상 확실하다. 첩자에 매복까지. 철저한 놈들이다.

“너희, 정체가 뭐냐?”

“무슨 말이지?”

“진짜 삼도문은 어디 있어?”

삼도문은 일개 중소 문파. 앞서 혁무진의 말처럼 이류 문파 쭉정이다. 이런 놈들이 하루아침에 뚝딱 생겨났을 리 없다.

설마?

“항산검문에서 왔나?”

곽준이 피식 웃었다.

“항산검문? 뭐, 그렇게 생각할 수도 있겠군.”

빌어먹을, 제삼의 세력이다.

로그아웃이 코앞인데 이런 일이 생기다니…….

‘시바, 운도 더럽게 없지.’

똥줄이 활활 탄다. 내가 위축될수록 곽준은 기세등등해졌다.

“이제 와서 후회해 봤자 늦었다. 대계(大計)는 오래전부터 시작되었으니까.”

“크윽.”

곽준은 희열에 찬 목소리로 선언했다.

“오늘…… 산서 무림은 새로운 주인을 맞이한다.”

띠링.



- 퀘스트가 생성되었습니다.



퀘스트



[암살자 처단]

오랫동안 때를 기다려 온 누군가가 움직였습니다. 우선 배신자가 보낸 암살자들을 처치하십시오!



등급 : 절정

제한 : 진태경

임무 : 암살자 처단 (0/20)

보상 : 경험치와 명성

 연계 퀘스트

실패 : 사망





눈을 깜빡였다. 내가 퀘스트창을 잘못 봤나?

‘스무 명?’

왜 이십이야? 저기 매복한 놈들도 있는데?

의문이 떠오른 그때, 풀숲이 들썩이고 매복한 적들이 함성과 함께 우리를 향해 돌격했다.

- 꾸에에에엑!

함성치곤 독특한데. 아니, 저건 울음소리 아닌가.

멍하니 서 있는 내 귓가로 [기감]이 발동됐다는 알림이 울렸다.



[Lv.1 고라니]



뭐여, 시벌.

“고라니여?”

고라니 무리가 우리를 스쳐 저 언덕 너머로 사라졌다. 갑작스러운 등장. 빠른 퇴장.

곽준이 묘하게 힘 빠진 얼굴로 검을 뽑아 들었다.

“쳐라!”

스무 명의 적들이 천천히 접근해 왔다. 나는 고라니의 충격이 가시지 않은 얼굴로 혁무진을 불렀다.

“야.”

“왜요.”

“쟤들 다 일류거든?”

“헉, 진짜요?”

혁무진이 화들짝 놀랐다.

“어. 너 이소군 알지. 항산검문 둘째. 걔가 한 스무 명 있다고 생각하면 돼.”

“이소군이, 스무 명이요?”

이번 반응은 묘하다. 잠깐 곰곰이 생각에 잠겨 있던 혁무진이 한마디를 툭, 던졌다.

“쟤들, 다 죽겠는데요?”



* * *



곽준은 생각했다.

‘이게 아닌데.’

그의 시선은 한 사람에게 고정되어 있다. 진태경. 초일류라고 알려진 태원진가의 삼공자. 놈의 창이 움직일 때마다 피가 솟구치고 수하들이 쓰러진다.

일격을 버텨도 이 격, 삼 격에 반드시 숨통이 끊어졌다. 그 한 명, 한 명이 최소 십 년을 수련시킨 일류 무인들이다.

‘뭐 저런 놈이 다 있지?’

창을 쓰니 창수(槍手)인 건 분명해 보이는데, 간격이 좁혀지건 말건 신경도 안 쓴다. 창을 휘두를 거리조차 없다 싶으면 어디선가 비수며 도끼가 툭툭 튀어나와 닥치는 대로 찌르고 쑤신다. 곡예단(曲藝團)의 묘기보다 더하다.

‘저 많은 무기가 도대체 어디서 튀어나오는 거지?’

보지도 못했다. 무슨 수법인지도 모르겠다. 무공과 공력의 문제가 아니다. 진태경이라는 인간 자체가 강해 보였다.

‘정보가 잘못됐다.’

스물로는 턱도 없다. 두 배는 데려와야 했다. 그가 받은 정보에 의하면 진태경은 운 좋은 애송이 그 이상도, 이하도 아니었다.

‘게다가, 저놈들은 도대체 뭐야.’

진태경의 부하라는 아홉 명은 대장이 앞에서 뭘 하건 말건 서로 등을 맞대고 느릿느릿 전진했다. 분명 개개인으로 보면 한참 부족한 실력인데, 한데 뭉치니 철벽이 따로 없다.

퍽. 콰직!

“크아악!”

“찔러, 찔러!”

“들어와, 들어와!”

곽준의 입술이 파르르 떨렸다. 무인으로서의 명예도 없는 놈들이다. 이런 난전에 서너 명씩 달라붙어 칼질을 해 대니 일류 고수인 수하들도 꼬치구이 신세를 면치 못했다.

“이놈들……!”

진태경에 대한 두려움을, 분노가 밀어냈다. 분기탱천한 그가 전장을 향해 몸을 날리려던 그때였다.

콰아아아-

전장의 중심에서 광풍이 휘몰아쳤다.

진태경의 창은 바람을 찢고 검을 조각 냈다. 수백 개의 검편(劍片)이 바람을 타고 전방을 휩쓸었다. 검의 주인들, 그리고 미처 반응하지 못한 자들을 향해.

푸푸푸푸푹!

“……끄윽.”

털썩.

전신에 검편이 박힌 무사가 그대로 고꾸라졌다. 일섬에 휘말린 십여 명의 부하 중 목소리라도 남긴 이는 그가 유일했다.

“……!”

꿀꺽. 누군가의 목울대가 크게 일렁였다. 이 순간만큼은 적아를 떠나 모두가 침묵을 지켰다. 어느 누구도 감히 검을 들어 싸울 생각을 하지 못했다. 물론 한 사람은 예외였다.

“일섬, 이거 끝내주네.”

진태경의 중얼거림을 듣는 순간, 곽준은 모든 걸 포기했다.

‘다 끝났어.’

대계가 성공해도 그는 실패했다. 진태경에게 죽느냐, 그분께 죽느냐 하는 무의미한 선택만이 남아 있을 뿐.

‘도망쳐야 한다. 아무도 찾을 수 없는 곳으로 멀리.’

하지만 곽준은 두 번째 인생을 찾아 떠날 수 없었다. 막 돌아서려는 찰나 들려온 살벌한 목소리 때문이었다.

“거기 딱 서. 매우 아프게 죽기 싫으면.”

진태경은 조금 누그러진 목소리로 덧붙였다.

“대답만 잘하면 살살 죽여 줄게.”

곽준의 얼굴이 하얗게 질렸다.



* * *



우직-!

“헙.”

느낌이 왔다.

갈비뼈가 두세 대쯤 부러지고 숨이 턱 막혔을 거다.

그래도 40레벨이라고 제법 버텼지만, 딱 거기까지가 한계다.

“도망치지 말라니까.”

“저 같아도 튀었습니다.”

피와 먼지를 뒤집어쓴 혁무진이 나를 짐승 보듯 바라본다.

“살살 죽인다니, 차라리 창날에 금창약을 바르고 찌른다고 하십쇼.”

“찔러 줘?”

“생각해 보니까 맞는 말이네요. 칼도 살살 맞으면 덜 아프잖습니까. 살살 죽을 수도 있죠. 허허, 허허허.”

뒤통수를 한 대 갈겨 주고 곽준을 일으켜 세웠다.

“다시 물어보자. 너희, 누구야?”

퉤. 피가래를 가볍게 피했다. 민첩 스탯이 높으면 코앞에서 날아오는 침도 피할 수 있다. 이건 좋은 리빙 포인트다.

물론 곽준에게 적당한 리빙 포인트도 있지. 예를 들자면.

“갈비뼈가 나간 상태에서 명치를 맞으면 많이 아프다.”

뻑.

“크아아아악!”

“그래서 대답은?”

“사, 삼도문.”

다시 주먹을 치켜드는 내게 곽준이 외쳤다.

“삼도문, 삼도문이 맞소. 사실이란 말이오!”

혁무진이 눈살을 찌푸렸다.

“거짓말입니다. 삼도문은 삼십 년 전에 개파한 문파인데, 사실 문파보단 무관에 가깝습니다. 주로 떠돌이 고아들을 받아들여 가르쳐서 명망이 높죠.”

“그래서?”

“이놈들이 삼도문의 제자들을 모두 죽이고 가짜 행세를 한 게 아닐까요?”

“가짜? 푸흐흐.”

곽준의 입에서 바람 빠지는 소리가 흘러나왔다. 놈은 웃고 있었다.

“아직도 모르겠느냐? 삼도문은 그분의 뜻에 따라 세워진 것이다. 삼십 년 대계를 짐작이나 했겠냐마는. 크흐흐.”

“삼십 년?”

까마득한 시간이다. 그 긴 세월 동안 웅크린 채 산서성을 차지할 계획을 꾸밀 수 있는 사람은 몇 되지 않는다.

당장 생각나는 건 한 사람뿐.

‘대장로?’

그가 도대체, 무슨 이유로?

아이들의 시신 앞에서 자책하던 진위경을 일으킨 것도, 모든 정치적 행위를 중단한 채 적극적으로 협력한 것도 대장로다.

덕분에 태원진가는 하나로 뭉쳐 오늘날에 이를 수 있었…….

‘잠깐.’

머릿속이 어지럽다. 설마?

“혁무진. 새로 합류한 중소 문파의 무사들이 몇이나 되지?”

“삼도문, 궁귀문을 합치면 백 명이 훌쩍 넘을 겁니다.”

“대장로 휘하는?”

“대장로님 계파라면 아마 본대의 절반 가까이…… 아!”

사태를 파악한 혁무진과 정찰조원들이 입을 벌렸다. 만약 내 짐작대로 대장로가 배신자라면 아귀가 맞아떨어진다.

진위경을 도운 건 오늘을 위한 포석에 지나지 않는다.

‘한 번의 전투로, 모든 걸 얻기 위해서.’

바로 오늘을 위해 진위경을 돕고, 가문의 힘을 합친 거다.

문득 전투 전, 곽준이 했던 말이 생각났다.

산서성의 주인이 바뀐다던 그 한마디. 결코 헛소리로 들리지 않는다.

‘본대가 위험해.’

이 사실을 진위경에게 알려야 한다.

“출발한다. 당장!”

버럭 외치며 돌아서려던 순간이었다.

“이미 늦었어.”

곽준이 피에 젖은 이를 드러내며 웃었다.

“나도, 네놈들도. 그리고 태원진가와 항산검문도. 대계는 이미 시작됐거든.”

동시에 핏물이 쏟아졌다. 눈, 코, 입. 구멍이란 구멍에서 피를 쏟아 낸 곽준의 고개가 스르륵 내려갔다.

혁무진이 질린 얼굴로 말했다.

“스스로 심맥을 끊었습니다.”

곽준의 죽음. 그건 한 가지 사실을 의미했다.

띠링. 띠링. 띠링.



- [Lv.40 곽준]을 처치했습니다!

- 암살자 처단 (20 / 20)

- 퀘스트, [암살자 처단]을 완료했습니다!

- 레벨 업!

- 명성이 50 상승합니다!



퀘스트 완료, 레벨 업과 명성 상승. 그 수많은 알림 끝에 나타난 하나의 메시지.



- [로그아웃]에 대한 모든 조건을 충족했습니다.

- 3초 후 로그아웃합니다. 3, 2…….



전신에서 힘이 쭉 빠져나간다. 몸이 붕 뜨는 감각.

혁무진이 화들짝 놀란 얼굴로 나를 부축했다.

“조장!”

노이즈 낀 목소리, 흐려지는 시야와 통제를 벗어난 몸.

지금은 안 되는데, 이런 식으로는 아닌데…….

‘하필 이럴 때.’

그리고 다음 순간.



- 1.



암흑이 들이닥쳤다.
```

### Current accepted English

```markdown
# Chapter 38

The first thing I felt was puzzlement.

“Set out?”

Gwak Jun answered.

“Yes. Our side needs to get moving too, or we won’t make it in time.”

At those inscrutable words, Hyuk Mujin stepped forward.

“You there, Three Paths Sect man. You seem to have the wrong idea. Our mission is to wait here in the rear with the Young Master.”

“Oh, is that so?”

Gwak Jun’s eyes went round. At that reaction, the reconnaissance-squad members nodded with looks that said, *That figures.*

“Looks like I had it wrong.”

“It happens. Sure it does.”

But I thought differently.

*What do you mean, it happens?*

There were twenty Three Paths Sect martial artists left in the rear. The one who amounted to their leader was Gwak Jun.

*Would a guy like that mix up his orders?*

He was unpleasant, no question, but he didn’t look that stupid.

A creeping dread rose and wound around my whole body.

“That’s a problem. The mission I received is a little different.”

“How is it different?”

As I spoke, I pressed down firmly on Hyuk Mujin’s foot. He horsed around dozens of times a day, but he wasn’t an idiot. His eyes widened as he caught my signal.

“Squad Leader, please move your foot. It hurts.”

“…”

*For fuck’s sake.*

Gwak Jun’s mouth curled as he watched me stare in disbelief.

“You catch on fast. Or are your subordinates just idiots? Well, anyway. I’ll tell you exactly what that person said.”

The next moment, the smile vanished from Gwak Jun’s face. A killer with cold, vacant eyes went on.

“Eliminate everyone and join the main force.”

Clang-clang-clang!

The instant the words left his mouth, dozens of sword flashes shot into the air. Killing intent and tension hung between the twenty martial artists Gwak Jun led and the reconnaissance-squad members, who drew their swords half a beat later.

“Have you bastards lost your minds…?”

Hyuk Mujin ground his teeth and glared at them.

“You dare betray our family? Are you itching to die?”

“Betray? Die? You’re badly mistaken.”

A sneer tugged at Gwak Jun’s mouth.

“There has been no betrayal, and we aren’t going to die. Least of all to trash like you.”

“You son of a—!”

Hyuk Mujin’s eyes went wild as he threw himself at Gwak Jun.

Or tried to.

“Don’t move.”

“Squad Leader?”

Hyuk Mujin’s eyes flew wide.

“They’re the Three Paths Sect! They’re nothing but Second Rate sect husks! Let us smash them right now and—”

“No.”

“What?”

“They’re not husks.”

Their sharp aura and murderous eyes were nothing like the ordinary martial artists of a small or mid-sized sect I had seen until now. The System turned that suspicion into certainty.

> **System**
>
> **Lv.30**

That was the average Level I read through my **Qi Sense**.

Every last one of them was a First Rate martial artist. Damn it. I’d spent three days with these people and hadn’t noticed a thing.

*I’d been too fixated on Logout.*

That was what I got for letting my guard down. I bit my lip and looked at them—or, more precisely, at the thick grass behind them.

The movement had been extremely faint, but it couldn’t get past my eyes.

*Someone’s hiding.*

They were outside the range of my **Qi Sense**, so I couldn’t confirm it. My instincts were certain, though. Spies, and an ambush on top of it. Thorough bastards.

“You lot. What are you really?”

“What is that supposed to mean?”

“Where is the real Three Paths Sect?”

The Three Paths Sect was only a small or mid-sized sect. As Hyuk Mujin had said, they were Second Rate husks. People like these couldn’t have been whipped up overnight.

*Don’t tell me.*

“Did you come from the Mount Heng Sword Sect?”

Gwak Jun gave a short laugh.

“The Mount Heng Sword Sect? Well, you could think that.”

*Damn it. A third faction.*

Logout was right in front of me, and this had to happen now…

*Shit. My luck is rotten.*

I was scared shitless. The more I shrank back, the more triumphant Gwak Jun looked.

“It’s too late for regret now. The grand plan began long ago.”

“Kh.”

Gwak Jun declared it in a voice brimming with delight.

“Today… Shanxi Murim will welcome a new master.”

Ding.

> **System**
>
> — A Quest has been created.
>
> **Quest**
>
> **Slay the Assassins**
>
> Someone who has waited a long time for the right moment has made their move. First, defeat the assassins sent by the traitor!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Slay the Assassins (0/20)
>
> **Reward:** EXP and Fame
>
> **Chain Quest**
>
> **Failure:** Death

I blinked. Had I misread the Quest Window?

*Twenty?*

Why twenty? There were enemies lying in ambush back there too.

Just as the question formed, the grass shook. The ambushers charged us with a battle cry.

“Kweeeek!”

Strange, for a battle cry. No, wait. Wasn’t that an animal?

As I stood there blankly, an alert rang in my ears that **Qi Sense** had activated.

> **System**
>
> **Lv.1 Water Deer**

What the hell?

“A water deer?”

A herd of water deer brushed past us and vanished beyond the hill. A sudden appearance. A quick exit.

Gwak Jun drew his sword with an oddly deflated look on his face.

“Attack!”

The twenty enemies came on slowly. Still wearing the shock of the water deer, I called to Hyuk Mujin.

“Hey.”

“What.”

“They’re all First Rate, you know?”

“What? Really?”

Hyuk Mujin jumped.

“Yeah. You know Lee Seogeun, the second son of the Mount Heng Sword Sect? Imagine there are twenty of him.”

“Twenty Lee Seogeuns?”

This reaction was odd. Hyuk Mujin thought it over for a moment, then tossed out a single remark.

“They’re all going to die, aren’t they?”

* * *

Gwak Jun thought,

*This isn’t how it was supposed to go.*

His gaze was locked on one man. Jin Taekyung, the third Young Master of the Jin Family of Taiyuan, known as a Super First Rate.

Every time that spear moved, blood spurted and Gwak’s men went down.

Even if they weathered one blow, the second or third always finished them. Every one of them was a First Rate martial artist trained for at least ten years.

*How is there a man like that?*

He was clearly a spearman, but he didn’t care whether the gap closed or not. Whenever it looked like there wasn’t even room to swing the spear, daggers and axes popped out from somewhere and stabbed and jabbed at anything in reach.

It put an acrobat troupe’s stunts to shame.

*Where the hell are all those weapons coming from?*

He hadn’t even seen them appear. He had no idea what kind of technique it was. This wasn’t a matter of martial arts or internal energy. Jin Taekyung himself just looked strong.

*The information was wrong.*

Twenty men weren’t nearly enough. They should have brought twice that. According to what he had been told, Jin Taekyung was nothing more or less than a lucky greenhorn.

*And what the hell are those people?*

The eight said to be Jin Taekyung’s subordinates advanced slowly with their backs together, whether their leader was doing anything up ahead or not. Individually, their skill was far from enough, but once they bunched up, they were an iron wall.

Thud. Crack!

“Gaaah!”

“Stab them! Stab them!”

“Come in! Come in!”

Gwak Jun’s lips trembled.

They had no honor as martial artists. In the middle of this melee they piled on three or four at a time and hacked away, and even his First Rate subordinates couldn’t avoid ending up as meat on a skewer.

“You bastards…!”

Anger shoved aside the fear of Jin Taekyung. Just as Gwak Jun, livid, was about to hurl himself into the fight—

Whoooosh—

A violent gale whipped up at the center of the battle.

Jin Taekyung’s spear tore through the wind and shattered the swords. Hundreds of sword fragments rode the gale and swept forward, toward the owners of those swords and the men who hadn’t reacted in time.

Pupupupupup!

“…Urk.”

Thud.

A martial artist with sword fragments buried all over his body crumpled forward. Of the ten or so subordinates caught in One Flash, he was the only one who even left a sound.

“…!”

Someone swallowed hard. Their throat bobbed.

For that moment, friend and foe alike kept silent. No one even dared think of raising a sword to fight.

Of course, one person was the exception.

“One Flash. This thing is awesome.”

The instant Gwak Jun heard that mutter, he gave up on everything.

*It’s all over.*

Even if the grand plan succeeded, he had failed. All that remained was the meaningless choice of dying to Jin Taekyung or dying to that person.

*I have to run. Far away, somewhere no one can find me.*

But Gwak Jun couldn’t leave to find a second life. Just as he was turning, a savage voice cut in.

“Stop right there. If you don’t want to die very painfully.”

Jin Taekyung added, his voice a little milder,

“If you answer well, I’ll kill you gently.”

Gwak Jun’s face went white.

* * *

Crunch!

“Ghk.”

I knew that feeling.

Two or three ribs had to have broken, and the wind would have been knocked clean out of him.

He held up pretty well for a Level 40, but that was as far as he could go.

“I told you not to run.”

“If I were him, I would’ve run too.”

Hyuk Mujin, covered in blood and dust, stared at me like I was some kind of beast.

“If you’re going to kill him gently, you might as well say you’ll coat your spearhead with Golden Sore Medicine[^1] and stab him.”

“Want me to stab you?”

“Now that I think about it, that’s true. A blade hurts less if it hits you gently, doesn’t it? You could die gently. Heh heh, heh heh heh.”

I smacked him once on the back of the head, then hauled Gwak Jun to his feet.

“Let’s try this again. Who are you?”

Ptooey.

I easily dodged the bloody phlegm. With a high Agility stat, you could even avoid spit flying at you from point-blank range.

That was a useful life hack.

Of course, I had a fitting life hack for Gwak Jun, too. For example:

“If you get hit in the solar plexus while your ribs are broken, it hurts a lot.”

Thump.

“Gaaaaah!”

“So? Your answer?”

“T-Three Paths Sect.”

As I raised my fist again, Gwak Jun shouted,

“The Three Paths Sect! It really is the Three Paths Sect! I’m telling you the truth!”

Hyuk Mujin frowned.

“He’s lying. The Three Paths Sect was founded thirty years ago. In truth, it’s closer to a martial arts school than a sect. They’re highly respected for taking in wandering orphans and teaching them.”

“So?”

“Couldn’t these bastards have killed all the Three Paths Sect’s disciples and impersonated them?”

“Impersonated? Pfft.”

A deflating sound escaped Gwak Jun’s mouth. He was laughing.

“You still don’t understand? The Three Paths Sect was established according to that person’s will. As if you could have guessed at a thirty-year grand plan. Heh heh.”

“Thirty years?”

It was an unimaginably long time. There were only a handful of people who could lie low for that many years and plot to seize Shanxi Province.

Only one person came to mind.

*The Head Elder?*

What possible reason could he have?

The Head Elder was the one who had pulled Jin Wikyung to his feet while he blamed himself in front of the children’s bodies. He was also the one who had halted every political maneuver and actively cooperated.

Thanks to that, the Jin Family of Taiyuan had united and made it this far…

*Wait.*

My head spun.

*Could it be?*

“Hyuk Mujin. How many martial artists from the newly joined small and mid-sized sects are there?”

“If you add the Three Paths Sect and Gunggwimun together, well over a hundred.”[^2]

“And under the Head Elder?”

“If you mean the Head Elder’s faction, probably close to half the main force… Ah!”

Hyuk Mujin and the reconnaissance-squad members opened their mouths as they grasped the situation.

If my guess was right and the Head Elder was a traitor, everything fit.

Helping Jin Wikyung had been nothing more than a setup for today.

*To take everything in a single battle.*

He had helped Jin Wikyung and united the family’s strength for this very day.

Suddenly I remembered what Gwak Jun had said before the fight.

That one line about Shanxi’s master changing. It no longer sounded like nonsense.

*The main force is in danger.*

I had to tell Jin Wikyung.

“We’re moving out. Right now!”

I shouted and was about to turn.

“Already too late.”

Gwak Jun grinned, baring bloodstained teeth.

“Too late for me, too late for you bastards, and too late for the Jin Family of Taiyuan and the Mount Heng Sword Sect. The grand plan has already begun.”

At the same time, blood gushed out. From his eyes, nose, and mouth—from every opening.

Gwak Jun’s head slowly drooped.

Hyuk Mujin spoke with a sickened look on his face.

“He severed his own heart meridian.”

Gwak Jun’s death meant one thing.

Ding. Ding. Ding.

> **System**
>
> — Defeated **Lv.40 Gwak Jun**!
>
> — **Slay the Assassins** (20/20)
>
> — Quest **Slay the Assassins** complete!
>
> — Level up!
>
> — Fame increases by 50!

Quest complete, a level-up, and a Fame increase.

After all those notifications, a single message appeared.

> **System**
>
> — All conditions for **Logout** have been met.
>
> — Logging out in 3 seconds. 3, 2…

Strength drained from my whole body. It felt as if I were floating.

Hyuk Mujin, startled, caught me.

“Squad Leader!”

His voice came through full of static. My vision blurred, and my body slipped out of my control.

*Not now. Not like this…*

*Of all times.*

And then—

> **System**
>
> — 1.

Darkness crashed in.

[^1]: Golden Sore Medicine is a salve for blade wounds.
[^2]: Gunggwimun is the name of another small sect newly allied with the Jin Family.
```
