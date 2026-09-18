# Retrospective Patch Plan — Chapters 24–28

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
  "summary": "10 findings in chapters 24-28",
  "findings": [
    {
      "chapter": 24,
      "confidence": 1.0,
      "current": "“Squad Leader. There’s a kid over there.”",
      "defect": "The established form of address 조장 is rendered as “Squad Leader” instead of the fixed term “Captain.”",
      "id": "R0024-01",
      "rationale": "The glossary fixes 조장 as “Captain” when Hyuk Mujin and the squad address Taekyung.",
      "replacement": "“Captain. There’s a kid over there.”",
      "severity": "minor",
      "source": "조장님. 저기 웬 꼬마가 있는데요?"
    },
    {
      "chapter": 25,
      "confidence": 1.0,
      "current": "By the time the carrier pigeon bearing word of war arrived, the Sakju Branch had already been surrounded so tightly that not even a drop of water could get through.",
      "defect": "The established term 전서구 is rendered as “carrier pigeon” rather than the fixed “messenger pigeon.”",
      "id": "R0025-01",
      "rationale": "The glossary specifically identifies this report-bearing 전서구 as a messenger pigeon.",
      "replacement": "By the time the messenger pigeon bearing word of war arrived, the Sakju Branch had already been surrounded so tightly that not even a drop of water could get through.",
      "severity": "minor",
      "source": "전쟁을 알리는 전서구가 도착했을 때는 이미 삭주 지부가 물 샐 틈 없이 포위된 상태였다."
    },
    {
      "chapter": 25,
      "confidence": 0.99,
      "current": "What do you think is the reason he has survived until now, despite being tangled up in all kinds of grudges and vendettas?",
      "defect": "The translation reduces 은원 to two synonymous forms of hostility, omitting the debts of gratitude included in the source concept.",
      "id": "R0025-02",
      "rationale": "은원 encompasses both gratitude and grudges—the full range of moral debts and enmities surrounding Jopil—not merely hostile vendettas.",
      "replacement": "What do you think is the reason he has survived until now, despite being tangled up in all kinds of gratitude and grudges?",
      "severity": "major",
      "source": "놈이 온갖 은원에 얽혀 있으면서도 지금까지 살아남을 수 있었던 이유가 무엇이겠소?"
    },
    {
      "chapter": 25,
      "confidence": 1.0,
      "current": "The wandering martial artists thought it was fortunate that Black Mountain Blade was dead. If he had still been alive, they would have suffered something even more horrifying.",
      "defect": "The second sentence changes the prospective victim from Black Mountain Blade to the wandering martial artists.",
      "id": "R0025-03",
      "rationale": "The omitted Korean subject remains Black Mountain Blade: the others believe his death spared him from Jopil inflicting an even worse punishment on him.",
      "replacement": "The wandering martial artists thought it was fortunate that Black Mountain Blade was dead. If he had still been alive, he would have suffered something even more horrifying.",
      "severity": "critical",
      "source": "낭인들은 흑산도가 죽어서 다행이라고 생각했다. 살아 있었다면 한층 더 끔찍한 일을 겪었을 테니까."
    },
    {
      "chapter": 27,
      "confidence": 1.0,
      "current": "“I’ll carry him.”\n\n“Yes. I’ll carry him.”",
      "defect": "Taekyung’s challenge is turned into a declaration that he himself will carry Gong Yacheong, duplicating Han Yeop’s answer and changing the speaker’s intended action.",
      "id": "R0027-01",
      "rationale": "Taekyung asks whether Han Yeop will carry Gong Yacheong; Han Yeop then accepts.",
      "replacement": "“Will you carry him?”\n\n“Yes. I’ll carry him.”",
      "severity": "critical",
      "source": "“두고 갈 수 없으면. 네가 업고 갈래?”\n\n“예. 제가 업겠습니다.”"
    },
    {
      "chapter": 27,
      "confidence": 0.97,
      "current": "Every time I heard her shallow, wheezing breaths, a pang of unease tightened in my chest.",
      "defect": "“Shallow, wheezing breaths” falsely suggests that Soyul is having respiratory difficulty; the source simply describes the small sleeping child’s soft breathing.",
      "id": "R0027-02",
      "rationale": "쌕쌕거리는 here is the audible breathing of the half-asleep child, while Taekyung’s discomfort comes from his guilt over abandoning Gong Yacheong.",
      "replacement": "Every time I heard her soft breathing, a pang of unease tightened in my chest.",
      "severity": "minor",
      "source": "쌕쌕거리는 숨소리를 들을 때마다 가슴 한구석이 불편해진다."
    },
    {
      "chapter": 27,
      "confidence": 1.0,
      "current": "“I’ll follow your orders, Squad Leader.”",
      "defect": "Hyuk Mujin’s established address 조장 is rendered as “Squad Leader” instead of “Captain.”",
      "id": "R0027-03",
      "rationale": "The glossary fixes Hyuk Mujin’s address for Taekyung as “Captain.”",
      "replacement": "“I’ll follow your orders, Captain.”",
      "severity": "minor",
      "source": "“명령에 따르겠습니다, 조장님.”"
    },
    {
      "chapter": 28,
      "confidence": 1.0,
      "current": "I couldn’t afford to lose a clash of qi, so I glared hard and dropped my voice.",
      "defect": "The idiomatic 기 싸움 is mistranslated as a literal supernatural clash of qi, obscuring the joke that Taekyung is trying to win an intimidation contest with a wolf.",
      "id": "R0028-01",
      "rationale": "In this context 기 싸움 means a contest of nerve or intimidation, not an exchange of internal energy.",
      "replacement": "I couldn’t afford to lose the battle of wills, so I glared hard and lowered my voice.",
      "severity": "major",
      "source": "기 싸움에서 밀리면 안 된다는 생각에 눈에 힘을 빡 주고 목소리를 깔았다."
    },
    {
      "chapter": 28,
      "confidence": 0.99,
      "current": "I tore his eyes before I left. Punishment for failing to recognize a master.",
      "defect": "“Tore his eyes” is malformed and loses the specific action of ripping the dead man’s eyes open.",
      "id": "R0028-02",
      "rationale": "This refers back to Jopil forcibly opening Black Mountain Blade’s frozen eyes until the flesh tore.",
      "replacement": "I ripped his eyes open before I left. Punishment for failing to recognize a master.",
      "severity": "minor",
      "source": "고수를 못 알아본 죄로 녀석의 눈을 찢어 주고 왔지."
    },
    {
      "chapter": 28,
      "confidence": 1.0,
      "current": "“Not a wastrel. These days they call me the Sleeping Dragon.”",
      "defect": "The established epithet 잠룡 is mistranslated as “Sleeping Dragon.”",
      "id": "R0028-03",
      "rationale": "The glossary fixes 잠룡, Jin Taekyung’s epithet and metaphor, as “Hidden Dragon.”",
      "replacement": "“Not a wastrel. These days they call me the Hidden Dragon.”",
      "severity": "minor",
      "source": "요즘은 잠룡 소리 듣고 있지."
    }
  ]
}
```

## Chapter 24

### Korean source

```text
＃24화



뛰었다. 그저 뛰는 것밖에 할 수가 없었다.

아버지가, 가족처럼 지내던 삭주지부의 식솔들이 죽어 나가도 열네 살 소년이 할 수 있는 일은 단 하나, 도망치는 것뿐이었다.

“오빠, 추워.”

품에 안긴 여동생이 칭얼거렸다. 소년, 소천은 추위에 얼어붙은 동생의 손에 호호 입김을 불었다.

“거의 다 왔으니까 조금만 참아. 응?”

“집 언제 가? 소율이는 엄마 보고 싶은데…….”

“어제도 오셨는걸.”

“거짓말. 오빠도 봤어?”

“그럼, 봤지.”

꿈속에서. 소천은 이어지는 말을 꿀꺽 삼켰다.

지난 밤 꿈에 나타난 어머니는 사흘 전과 똑같았다. 지쳐 잠든 소율이를 한참 동안이나 쓰다듬고 바라보다가 말씀하셨다.



‘살아남아라. 반드시 살아남아야 한다.’



그 목소리가, 다른 사람들을 이끌고 떠나던 그 뒷모습이 아직도 눈앞에 아른거렸다.

‘어머니는 어떻게 되셨을까. 혹시…… 아니, 아니다. 그럴 리 없어.’

불길한 느낌을 애써 억누르던 그때였다.

부스럭.

“누구냐!”

어린 누이를 끌어안는 동시에 품고 있던 비수를 꺼내는 일련의 동작이 자연스럽다.

집이 불타고 수많은 죽음을 목격한 그날 밤 이후, 쾌활하던 소년은 짐승의 눈빛을 갖게 됐다.

“셋을 세겠다. 하나, 둘…….”

“나다.”

어둠 속에서 불쑥 나타난 얼굴에 비수가 스르르 내려갔다.

“공 숙부?”

“쉿. 목소리를 낮추어라.”

공 숙부라 불린 이는 지친 얼굴의 중년인이었다. 삭주 지부장인 소천의 아비와는 오랜 지기로, 현재는 어린 남매의 길잡이이자 보호자이기도 했다.

“반 시진이 넘도록 안 오시기에 걱정했습니다.”

“주의해야 했다. 꼬리가 붙었어.”

“벌써 말입니까?”

“그래. 한시가 급하다.”

소천은 망설이지 않고 일어났다. 영문을 몰라 하는 소율을 들쳐 업은 공 숙이 풀숲을 헤치며 앞장섰다.

“어디로 가는 것입니까?”

“혼주. 제아무리 잔악무도한 놈들이라고 해도 그곳까지 쫓아오지는 못할 것이다.”

과연 그럴까. 소천은 의구심이 들었다.

이미 삭주 지부가 무너졌다. 건물은 불탔고 모두가 죽었다. 놈들의 정체는 모르지만 목적은 확실했다.

‘몰살.’

떠오른 단어를 입김에 날려 보낸다. 소천은 다시 걷기 시작했다.

그렇게 얼마나 걸었을까, 진눈깨비처럼 흩날리던 흰 눈이 종아리까지 차오른 순간이었다.

“조용히.”

앞서 걷던 공 숙의 발걸음이 멈췄다. 소천도 덩달아 숨을 죽였다. 세찬 바람 소리. 앙상한 나뭇가지들이 서로 부딪치는 소리…… 단지 그뿐이었다.

그러나 소천은 직감했다.

“놈들입니까?”

공 숙이 딱딱하게 굳은 얼굴로 대답했다.

“최소 십여 명. 곧 따라잡힐 것이다.”

암담한 상황이다. 하지만 이상하게도 소천의 마음은 차분하게 가라앉았다.

“내 불찰이다. 눈이 내리기 전에 서둘렀어야 하는 것을…… 하늘이 원망스럽구나.”

“숙부께서는 최선을 다하셨습니다.”

소천은 품에서 비수를 꺼내 들었다. 일 년 전 아버지에게 물려받은 비수. 아버지가 남긴 유일한 흔적이다.

“저도 하찮게나마 무공을 배운 몸. 무인답게 싸우다 죽겠습니다.”

“……아직 포기하기에는 이르다.”

공 숙이 할 수 있는 말은 그것뿐이었다. 그들은 얼마 남지 않은 힘을 끌어 올려 이동을 시작했다.

하지만 며칠간 밤낮 없는 도주로 한계에 다다른 체력이 발목을 잡았다. 걸음이 점점 느려지고, 숨이 가빠진다.

“여기다!”

“거의 다 따라잡았어!”

이제는 소천도 들을 수 있었다. 추격자들의 목소리와 그들이 밝힌 횃불이 점점 가까워진다.

그때, 공 숙이 곤히 잠든 소율을 소천에게 건넸다.

“뒤따라가마.”

“숙부!”

“걱정마라. 이 공야청, 그리 호락호락한 놈이 아니다.”

“그래도 어찌…….”

“어서!”

소천은 공야청을 뒤로하고 다시 산을 올랐다. 한계에 다다른 체력, 하지만 멈추지 않았다.

그렇게 눈 덮인 산의 언덕에 다다랐을 때, 병장기 부딪치는 소리와 누군가의 비명이 울려 퍼졌다.

‘공 숙부.’

소천은 이를 악물었다. 당장이라도 비수를 뽑아 들고 저 아래로 뛰어들고 싶었다. 하지만…….

‘참자. 참아야 한다.’

지난 닷새 동안 수백, 수천 번을 다짐했다. 꼭 살아남겠다고, 품 안의 여동생을 지키고 흉수들에게 복수하겠노라고.

언덕 위, 소천은 불길이 쏟아지는 눈동자로 일렁이는 횃불들을 바라봤다.

‘나는 반드시 살아남는다.’

그리고 등을 돌려 언덕을 오른 다음 순간, 소천은 벼락 맞은 것처럼 몸을 떨었다.

“아, 아아…….”

언덕 위 너른 공터, 남색 무복을 입은 열 명의 사내가 소천을 바라보고 있었다.

가슴에 수실로 새겨 넣은 진(陳)이라는 한 글자가 크게 보였다.



* * *



이상한 낌새를 느낀 것은 훈련을 막 시작하려던 찰나였다.

세찬 바람 너머로 언뜻 들리는 소리. 공력을 끌어 올리자 더욱 선명해지는 그것의 정체는…….

‘사람 목소리?’

어림잡아도 열 명은 넘어가는 듯했다. 어떻게 이제야 눈치챘을까 싶을 정도로 가까운 거리다.

‘이 날씨에 저 정도 인원이라…….’

좋아, 결심했다.

“짐 싸라.”

“예?”

각자 무기를 들고 훈련을 준비하던 조원들이 어리둥절한 얼굴로 되묻는다.

“빨리 짐 싸. 한 명은 들어가서 혁무진…….”

“조장님. 저기 웬 꼬마가 있는데요?”

젠장. 진짜네. 조그만 아이를 업은 꼬마가 멍하니 우리를 바라보고 있었다.

“쟤 누구야.”

“모르겠는데요. 이 오두막 주인인가?”

제발 그랬으면 좋겠다. 하지만 뒤에 따라오는 놈들이 화목한 대가족 구성원이라는 생각이 들지 않는 건 왜일까.

“우는데요?”

누군가의 말처럼, 꼬마는 울고 있었다. 하염없이 펑펑 울면서 뛰고 있었다. 문제는 방향이다.

“어어, 이쪽으로 오는데…… 조장님 어디 가세요?”

의혹 어린 눈빛들이 나를 향했다. 나는 이미 멀찍이 뒤로 물러난 상태였다.

“말 타러. 슬슬 출발해야지.”

“이 날씨에요? 말도 못 움직일 텐데.”

“그래? 그럼 버리고 가자.”

“예?”

“원래 임무라는 게 그래. 눈이 오건 비가 오건 우리는 할 일을 해야지. 입 다물고 짐이나 챙겨.”

“그래도…….”

“짐 챙겨! 혁무진 깨워!”

불과 일 다경 전까지 우러러보던 시선은, 이제 정신병자를 보는 시선으로 바뀌어 있었다.

“갑자기 왜 이러세요?”

왜 이러긴. 느낌이 더럽게 안 좋으니까 그렇지.

이제 척하면 척이다. 꼬마가 가까워질수록 빅 엿의 냄새가 강하게 풍겨 오고 있다.

어떤 전개가 벌어질지 눈에 선했다. 방법은 하나뿐이다.

“그럼 나만 먼저 내려가 있을…….”

그 순간, 함성 소리와 함께 불청객들이 언덕 위로 모습을 드러냈다. 무려 이십여 명에 달하는 남자들이다.

‘아, 시발.’

띠링.



- [돌발 퀘스트]가 생성되었습니다!



퀘스트



[삭주 지부의 생존자]

당신은 태원진가 삭주지부의 생존자들과 마주쳤습니다.

항산검문의 잔인무도한 추격자들에 맞서 생존자들을 구해 내십시오!



등급 : 돌발 퀘스트

제한 : 진태경

임무 : 생존자 구출 (미완료)

보상 : 연계 퀘스트

???

실패 : ???





“…….”

“…….”

우리는 놈들을 봤다. 놈들도 우리를 봤다. 얼어붙은 공터에 죽음 같은 침묵이 흘렀다.

‘이럴 줄 알았어. 이렇게 될 줄 알았어.’

하지만 후회해도 늦었다. 내 팔자가 더러운 걸 어쩌겠나.

나는 한숨을 푹 내쉬고 외쳤다.

“공격 대형. 펼쳐!”

차차착. 갑작스러운 상황이었지만 조원들은 가르친 대로 움직였다. 순식간에 대형이 갖춰질 때쯤, 놈들도 우리의 정체를 깨닫고 고함을 내질렀다.

“태원진가의 애송이들이다!”

“머릿수도 얼마 안 돼. 쓸어 버려!”

애송이. 딸리는 머릿수.

족집게처럼 골라낸 팩트가 가슴을 헤집는다.

아직 다 가르치지도 못했는데, 이놈들 무공도 낮고 실전 경험도 없어서 완전 신병인데…….

‘안 되면 나 혼자라도 튀어야 하나.’

나는 암담함을 느끼며 [기감]을 사용했다. 내 눈에만 보이는 푸른 기의 물결이 괴성을 지르며 달려드는 적들을 훑는다.

띠링. 띠링. 띠링.



[Lv.12] [Lv.11] [Lv.12]



“……응?”

그때 정찰조원들이 새파랗게 질린 얼굴로 외쳤다.

“어떻게 합니까?”

“옵니다, 와요!”

“조자아아앙!”

30m, 20m…… 빠른 속도로 쇄도하는 적들을 바라보며 입을 뗐다.

“걱정하지 마라. 적들은 단순한 경험치…… 아니, 오합지졸에 지나지 않는다. 단!”

“단?”

“온 힘을 다해 막아라. 막기만 해.”

“예? 그게 무슨 말씀이십니까.”

무슨 말씀이긴. 막타 치지 말라는 소리다.

“수비 대형, 펼쳐!”

응. 경험치 다 내 거.



* * *



“조장!”

“안 됩니다. 조자아앙!”

“조장이 자살하러 갔다!”

그런 거 아니야, 미친놈들아. 나는 정찰조원들의 비명을 뒤로하고 적들을 향해 뛰어들었다.

단전에서 솟구친 공력이 사지백해로 뻗쳐 나간다.

“미친놈.”

선두의 적이 누런 이빨을 드러내며 웃는다.

나도 마주 웃어 주었다.

“예쁜 놈.”

“뭐?”

서걱.

목을 움켜쥐고 고꾸라지는 녀석을 스쳐 지나가는 순간. 기다리던 목소리가 들렸다.

띠링.



- 경험치를 획득했습니다.

- 50의 공적치를 얻었습니다!



“뭐, 뭐야!”

“이 개새끼가 감히…….”

적들의 면면은 실로 훌륭했다. 얼굴에 칼자국은 기본 옵션이요, 위생 상태도 심히 안 좋아 악취가 코를 찔렀다.

그런데…….

“어우, 좋다.”

꽃밭에 있는 기분이다. 경험치라는 꿀을 머금고 있는 스무 송이의 꽃들. 나는 행복한 얼굴로 꽃송이에 달려들어 꿀을 빨았다.

푹. 푹. 푹.

띠링. 띠링. 띠링.



- 경험치를 획득했습니다.

- 50의 공적치를……

- 경험치를 획득…….

- 50의 공적치…….



거침없이 그 사이를 헤집었다. 눈 깜짝할 사이에 선두가 무너지고 적들이 자신도 모르게 주춤거린다.

‘그러면 고맙지.’

진가보법과 진가창법은 전진에 기반을 둔 무공이다.

나는 보법을 밟아 나갔다. 중심으로 파고들며 창을 휘둘렀다.

“크악!”

“으아아악!”

예리한 창의 육중한 무게에 패도적인 창법까지. 더군다나 갈수록 적들이 물러서는 상황.

진가창법이 진가를 발휘할 시간이었다.

‘일 초식.’

보법과 함께 창을 휘두르기 시작했다. 한 번 휘두르고 내질러질 때마다 누군가의 비명과 피가 터져 나온다.

“컥.”

“꺼흐으윽.”

이 초식, 삼 초식. 사 초식.

어느 순간 나는 흐름에 몸을 맡겼다. 물결이 파도가 되고, 파도에 적들이 휩쓸린다. 전신의 감각이 오싹할 정도로 곤두섰다.

더, 더, 더…….

“이 개새끼가아!”

푹. 푸푹.

목, 가슴, 복부. 차례대로 찌르고 베어 낸다. 사망자 확인은 시스템 알림이 대신해 주었다.

그렇게 얼마나 지났을까. 땅에 발을 딛고 서 있는 자는 한 사람이 유일했다.

“대, 대형께서 반드시 널 찾아…….”

기다리지 않았다.

파도는 흐름이다. 그리고 마지막 파도가 내 창끝에서 터져 나왔다. 진가창법의 마지막 초식, 천관일(天貫軼).

푸화악!

마지막 한 사람, 뱁새눈은 조각조각 난 검을 바라보다가 그대로 무릎을 꿇었다. 놈의 가슴 한복판이 포탄에 맞은 것처럼 터져 나가 있었다.

띠링.



- [Lv.32 흑산도]를 처치하셨습니다!

- [생존자] 퀘스트를 완료했습니다!

- 연계 퀘스트가 생성되었습니다!

- 경험치를 대량 획득합니다!

- 공적치를 대량 획득합니다!

- 레벨이 올랐습니다!

- 레벨이 올랐습니다!

- 레벨이…….



쉼 없이 들리는 시스템 알림을 들으며 나는 배를 쓰다듬었다.

“꺼윽.”

어우, 배불러.
```

### Current accepted English

```markdown
# Chapter 24

He ran. It was the only thing he could do.

Even as his father and the people of the Sakju Branch who had been like family to him died one after another, there was only one thing a fourteen-year-old boy could do: run.

“Oppa, I’m cold.”

His little sister whimpered in his arms. The boy, Socheon, blew warm breath onto her hands, which had gone stiff with cold.

“We’re almost there, so just hold on a little longer. Okay?”

“When are we going home? Soyul wants to see Mom…”

“She visited yesterday, too.”

“You’re lying. Did you see her?”

“Of course I did.”

*In my dream.*

Socheon swallowed the words that followed.

His mother had appeared in his dream the night before, exactly as she had three days earlier. She had spent a long time stroking and gazing at Soyul, who had fallen asleep from exhaustion, before speaking.

*Survive. You must survive.*

Her voice still rang in his ears, and the sight of her back as she led the others away still shimmered before his eyes.

*What happened to Mother? Could she have…? No. That can’t be.*

It was then, as he struggled to suppress his ominous feelings, that he heard something.

Rustle.

“Who’s there?”

The sequence of movements came naturally: pulling his little sister close while drawing the dagger from inside his clothes.

After the night when his home had burned and he had witnessed countless deaths, the cheerful boy had gained the eyes of a wild beast.

“I’ll count to three. One, two…”

“It’s me.”

The dagger slowly lowered when a face suddenly appeared from the darkness.

“Uncle Gong?”

“Shh. Keep your voice down.”

The man called Uncle Gong was a middle-aged man with a weary face. He had been an old friend of Socheon’s father, the Branch Leader of the Sakju Branch, and was now the young siblings’ guide and protector.

“I was worried because you hadn’t returned for more than half a shichen.[^1]”

“I should have been more careful. We have a tail.”

“Already?”

“Yes. Every moment counts.”

Socheon stood without hesitation. Uncle Gong hoisted the bewildered Soyul onto his back and led the way through the brush.

“Where are we going?”

“Honju. No matter how cruel those bastards are, they won’t pursue us that far.”

*Will they really not chase us that far?*

Socheon had his doubts.

The Sakju Branch had already fallen. The building had burned, and everyone was dead. He did not know who the attackers were, but their purpose was clear.

*Massacre.*

He blew the word away with his breath and started walking again.

How long had they walked?

The white snow, which had been drifting down like sleet, had risen to their calves when—

“Quiet.”

Uncle Gong stopped walking. Socheon held his breath as well. The only sounds were the howling wind and the clatter of bare branches striking one another.

But Socheon knew instinctively.

“Is it them?”

Uncle Gong answered with a rigid expression.

“At least ten. They’ll catch up soon.”

The situation was bleak. Yet strangely, Socheon’s heart settled into a calm stillness.

“It was my fault. I should have hurried before the snow began… I curse the heavens.”

“You did everything you could, Uncle.”

Socheon drew the dagger from inside his clothes. It had been handed down to him by his father a year ago—the only trace his father had left behind.

“I’ve learned a little martial arts myself. I’ll fight and die like a martial artist.”

“…It’s too soon to give up.”

That was all Uncle Gong could say. They summoned what little strength they had left and started moving again.

But their stamina, pushed to its limit by days and nights of nonstop flight, dragged at their feet. Their steps grew slower, and their breathing became labored.

“There!”

“We’re almost on them!”

Now Socheon could hear them, too. The pursuers’ voices and their torchlight were drawing closer.

At that moment, Uncle Gong handed the soundly sleeping Soyul to Socheon.

“I’ll bring up the rear.”

“Uncle!”

“Don’t worry. This Gong Yacheong isn’t such an easy man to take down.”

“But how can you…”

“Go!”

Socheon left Gong Yacheong behind and started up the mountain again. His stamina was at its limit, but he did not stop.

When he reached a hill on the snow-covered mountain, the clash of weapons and someone’s scream rang out.

*Uncle Gong.*

Socheon gritted his teeth. He wanted to draw his dagger and leap down there immediately. But…

*Hold on. I have to hold on.*

He had repeated those words hundreds, thousands of times over the past five days. He had sworn that he would survive, protect the little sister in his arms, and take revenge on the murderers.

From the hilltop, Socheon stared at the flickering torches with eyes that seemed to pour fire.

*I will survive.*

Then he turned his back and climbed the hill. The next moment, his body shook as if struck by lightning.

“A-ah…”

Ten men in navy martial uniforms were looking at Socheon from the wide clearing atop the hill.

A single character, 陳—the character for Jin—was prominently embroidered in silk thread across their chests.

* * *

I sensed something strange just as we were about to begin training.

A sound carried faintly over the howling wind. When I raised my internal energy, the sound grew clearer.

*A human voice?*

There had to be more than ten people. They were close enough that I wondered how I had failed to notice them until now.

*That many people in this weather…*

All right. I’d made up my mind.

“Pack your things.”

“Huh?”

The squad members, who had been preparing for training with their weapons in hand, stared at me, baffled.

“Pack up, quickly. One of you, go inside and get Hyuk Mujin—”

“Squad Leader. There’s a kid over there.”

Damn it. There really was one.

A little boy carrying an even smaller child on his back was staring blankly at us.

“Who’s that?”

“I don’t know. Is he the owner of this cabin?”

*Please let that be the case.*

But why did I find it so hard to believe that the people following him were members of one happy, extended family?

“He’s crying.”

As someone pointed out, the boy was crying. He was running while sobbing his heart out.

The problem was where he was headed.

“Uh, he’s coming this way… Squad Leader, where are you going?”

Suspicious gazes turned toward me. I had already retreated a good distance.

“I’m going to ride a horse. We should be leaving soon.”

“In this weather? The horses won’t even be able to move.”

“Really? Then we’ll leave them behind.”

“What?”

“That’s how missions work. Snow or rain, we still have a job to do. Shut up and pack your things.”

“But still…”

“Pack your things! Wake Hyuk Mujin!”

The admiring looks I’d enjoyed barely fifteen minutes ago had now turned into the sort reserved for a lunatic.

“What’s gotten into you all of a sudden?”

*What’s gotten into me?*

I had a really bad feeling about this.

By now, I knew the signs. The closer the kid got, the stronger the stink of a huge shitshow grew.

I could see exactly how this would play out. There was only one way out.

“Then I’ll head down first by my—”

At that moment, the uninvited guests appeared over the hill amid a chorus of shouts.

There were more than twenty men.

*Oh, fuck.*

Ding.

> **System**
>
> - Sudden Quest has been created!
>
> **Quest**
>
> **Survivors of the Sakju Branch**
>
> You have encountered survivors from the Sakju Branch of the Jin Family of Taiyuan.
>
> Rescue the survivors from the Mount Heng Sword Sect’s merciless pursuers!
>
> **Grade:** Sudden Quest
> **Limit:** Jin Taekyung  
> **Task:** Rescue the survivors — Incomplete  
> **Reward:** Chain Quest  
> ???  
> **Failure:** ???

“…”

“…”

We looked at them. They looked at us.

A deathly silence settled over the frozen clearing.

*I knew it. I knew this was how it would turn out.*

But regret was useless now. What could I do about my cursed luck?

I let out a deep sigh and shouted.

“Attack formation. Form up!”

Clack-clack-clack. Caught off guard, the squad members nevertheless moved as they had been taught. By the time they had formed up, the enemy had realized who we were and started shouting.

“They’re brats from the Jin Family of Taiyuan!”

“There aren’t many of them. Wipe them out!”

*Brats. Outnumbered.*

Those two facts hit me right in the chest.

I hadn’t even finished teaching them. Their martial arts were weak, they had no real combat experience, and they were complete rookies.

*If things go bad, should I bolt by myself?*

Feeling utterly hopeless, I used Qi Sense. Blue waves of qi, visible only to me, swept over the enemies charging forward with shrieks.

Ding. Ding. Ding.

> **System**
>
> - Level 12
> - Level 11
> - Level 12

“…Huh?”

The reconnaissance squad members turned deathly pale.

“What do we do?”

“They’re coming! They’re coming!”

“Squad Leadeeeer!”

As I watched the enemies rush toward us at incredible speed—thirty meters, twenty meters—I opened my mouth.

“Don’t worry. The enemy is nothing but simple EXP… I mean, a rabble. But!”

“But?”

“Stop them with everything you have. Just hold them back.”

“What? What do you mean?”

*What do I mean?*

*Don’t get the last hit.*

“Defensive formation. Form up!”

Yes. All the EXP was mine.

* * *

“Squad Leader!”

“No! Squad Leadeeeer!”

“The squad leader went to commit suicide!”

That wasn’t what I was doing, you lunatics.

I ignored the reconnaissance squad members’ screams and charged toward the enemies.

Internal energy surged from my dantian and spread through my limbs and bones.

“You crazy bastard.”

The enemy at the front grinned, baring yellow teeth.

I grinned back.

“Pretty boy.”

“What?”

Slash.

The man clutched his throat and collapsed. As I passed him, the voice I had been waiting for rang out.

Ding.

> **System**
>
> - You gained EXP.
> - You gained 50 Merit!

“What the—!”

“How dare this fucking bastard…”

The enemies were a spectacle in their own way. Facial scars were standard equipment, and their poor hygiene produced a stench that stabbed at my nose.

And yet…

“Ah, this is great.”

I felt like I was in a flower garden.

Twenty flowers filled with the sweet honey of EXP.

I charged into them with a blissful expression and sucked out the honey.

Stab. Stab. Stab.

Ding. Ding. Ding.

> **System**
>
> - You gained EXP.
> - You gained 50 Merit!
> - You gained EXP…
> - You gained 50 Merit…
> - You gained EXP…
> - You gained 50 Merit…

I tore through their ranks.

The front line collapsed in an instant, and the enemies instinctively began to falter.

*That works for me.*

The Jin Family’s Manoeuvre Technique and Spear Technique were martial arts built around advancing.

I advanced with the Manoeuvre Technique, drove into their center, and swung my spear.

“Gaaah!”

“Aaaargh!”

The spear was razor-sharp and massively heavy, and the technique was domineering to boot. On top of that, the enemies were steadily backing away.

It was time for the Jin Family’s Spear Technique to show its true worth.

*First form.*

I began swinging the spear in step with my footwork. Every swing and thrust brought forth someone’s scream and a burst of blood.

“Ghk.”

“Grrrgh.”

Second form. Third form. Fourth form.

At some point, I surrendered myself to the flow.

The ripples became waves, and the enemies were swept away by them. Every nerve in my body stood on end.

More. More. More…

“You fucking bastard!”

Stab. Slash.

Throat, chest, abdomen.

I stabbed and cut them down one after another. The System alerts confirmed the fatalities for me.

How much time passed?

Only one person remained standing.

“Our boss will find you no matter what…”

I didn’t wait.

A wave is momentum. The final wave burst from the tip of my spear.

The final form of the Jin Family’s Spear Technique:

*Sky-Piercing Strike*.

Splurt!

The last man, the one with the narrow birdlike eyes, stared at his sword, which had been shattered into pieces, before dropping to his knees.

The center of his chest had burst open as if struck by a cannonball.

Ding.

> **System**
>
> - You defeated **Level 32 Black Mountain Blade**!
> - You completed the **Survivors of the Sakju Branch** Quest!
> - A Chain Quest has been created!
> - You gain a large amount of EXP!
> - You gain a large amount of Merit!
> - You have leveled up!
> - You have leveled up!
> - You have leveled…

As the System alerts continued without pause, I rubbed my stomach.

“Buuurp.”

Ah, I’m stuffed.

[^1]: A shichen is a traditional Chinese time period of roughly two hours.
```
## Chapter 25

### Korean source

```text
＃25화



“이곳은 저승인가?”

중년인이 깨어나자마자 한 말이었다.

내가 대답하기도 전에 조그마한 뭔가가 튀어나와 중년인의 품에 안겼다.

눈가에 눈물이 대롱대롱 매달린 꼬마가 외쳤다.

“공 숙부!”

“천아! 무사했구나. 그런데 이게 도대체……?”

혼란스러워하는 중년인에게 꼬마가 울음 섞인 목소리로 설명했다. 언덕 위에서 우리를 만났고, 내 손에 적들이 모두 죽었다는 말을 들은 중년인이 눈을 크게 떴다.

“본가의 인물이시오?”

“예. 맞습니다.”

“아, 하늘이 도왔구나!”

“…….”

내가 도운 거지, 이 양반아.

“난 분명히 산 밑으로 추락했는데…… 그걸로 끝이라고 생각했소.”

“거의 그럴 뻔했지요. 운이 좋았습니다.”

나는 손가락으로 능선 밑을 가리켰다. 적으로 추정되는 시체 두 구가 나무에 머리를 박고 누워 있었다.

그가 미끄러졌던 경로에 풀숲이 무성하지 않았다면, 그도 저 꼴이 났을 것이다.

‘나도 처음에는 몰랐지.’

중년인의 존재를 깨달은 건 퀘스트창 덕분이었다.

적들을 다 물리쳤는데도 [삭주 지부의 생존자] 퀘스트가 완료되지 않았던 것이다. 그건 생존자가 더 있다는 뜻이었다.

‘문제는 이 사람 말고도 생존자가 더 있냐는 건데…….’

일말의 불안감은 지친 중년인을 부축한 순간 간단히 해소됐다.

띠링.



- [생존자] 퀘스트를 완료했습니다!

- 연계 퀘스트가 생성되었습니다!

- 레벨이 올랐습니다!

- 레벨이 올랐습니다!

- 공적치와 명성이 상승합니다!



* * *



“후우.”

중년인이 호흡을 토해 냈다. 짧은 운기조식이었지만 최소한의 기력을 회복한 듯, 훨씬 나아진 모습이었다.

그는 자리에서 일어나 정중히 포권을 취했다.

“은인께서 모두를 살리셨습니다.”

“아닙니다. 마땅히 해야 할 일을 한 것뿐인데요.”

이제는 입만 열리면 거짓말이 술술 나온다. 한편으로는 틀린 말도 아니다. 어떻게든 퀘스트는 깨야 했으니까.

‘오히려 내가 고맙다고 절을 해야 할 판이지.’

하지만 이런 내 태도에 산타클로스, 아니 생존자들은 적잖이 감격한 모양이었다.

“뛰어난 무공에 의협심까지. 이 공야청, 진심으로 탄복했소.”

“소천과 소율이 대협께 큰 은혜를 입었습니다.”

덕분에 이름을 알았다. 중년인은 공야청, 어린 남매는 소천과 소율이다.

“실례가 안 된다면 은인의 성함을 여쭈어도 되겠소?”

“제 이름은…….”

그때, 문득 한 가지 생각이 뇌리를 스쳤다.

‘이거, 내 이름 들으면 칼 들고 달려드는 거 아냐?’

어떤 음모가 있었건 간에 이 전쟁의 도화선에 불을 붙인 건 다름 아닌 이 몸, 진태경이다. 터전과 가족을 잃은 두 사람이 내게 좋은 감정이 있을 것 같지 않았다.

그래, 선의의 거짓말이 필요한 시점이다.

“홍길동. 저는 홍길동이라고 합니다.”

“홍길동…… 처음 듣는 이름이오. 그러나 영웅의 풍모가 느껴지는구려.”

소천이 옆에서 거들었다.

“동에 번쩍 서에 번쩍. 신출귀몰할 것 같은 이름입니다.”

……저 녀석이 어떻게 알았지?

나는 호부호형 얘기가 나오기 전에 서둘러 화제를 돌렸다.

“그보다, 어떻게 된 일입니까?”

두 사람의 얼굴에 그림자가 짙게 내려앉았다.

말문을 연 것은 공야청이었다.

“불과 며칠 전의 일이었소.”

전쟁을 알리는 전서구가 도착했을 때는 이미 삭주 지부가 물 샐 틈 없이 포위된 상태였다. 항산검문이 고용한 낭인들이 사람들을 도륙하고, 건물을 불태웠다고 했다.

“그 숫자가 물경 일백에 달했소. 지부장과 휘하 무사들이 시간을 벌어 준 덕분에 비밀 통로로 빠져나올 수 있었지요. 탈출한 이들 대부분이 무공을 모르는 여인과 아이들이었소.”

다른 이들이 어떻게 되었는지는 물어보지 않아도 알 수 있었다.

내가 갖고 있는 시스템은 절대적이며 사실적이다. 퀘스트창이 알려 준 삭주 지부의 생존자는 세 사람이 전부였다.

“적들에 관해 알고 싶습니다.”

“낭인들이오.”

“낭인?”

“은인도 알다시피, 돈이라면 뭐든 하는 놈들이지. 그중에서도 특히 악질인 놈들이 항산검문의 의뢰를 받아 우리를 습격했소.”

“악질치고는 약하던데요.”

“악하고 선함에 강자와 약자가 따로 있겠소? 이번에 고용한 놈들은 널리고 널린 수준의 낭인이오. 다만 우두머리가 문제였지.”

공야청이 이를 악물었다.

“일문일살 조필. 그놈이었소. 지부장께서는 놈을 보자마자 패배를 직감하고 내게 식솔들을 부탁하셨지.”

소천의 작은 주먹이 부르르 떨렸다.

“제 손으로 직접 사지를 찢어 죽일 겁니다.”

꼬맹이치고는 남다른 어휘 선택이었지만, 뼈에 사무친 원한을 생각하면 당연하게 생각되었다.

나는 소천의 머리를 쓰다듬어 주었다.

“꼭 그렇게 될 것이다. 내 도와주마.”

“정말이십니까?”

“남아일언중천금. 내 한 입으로 두말할 것 같으냐? 내 반드시 그놈을 잡아 레벨 업을…….”

“예?”

“아니, 놈을 죽여 원한을 갚아 주마.”

“아아, 감사합니다. 정말 감사합니다. 홍 대협!”

“고맙소. 정말로 고맙소!”

두 사람은 연신 감사를 표했다. 아, 뭔가 되게 야비한 놈이 된 기분이라 가슴 한구석이 심하게 찔려 온다.

‘아니지. 저쪽은 원수가 죽어서 좋고, 나는 레벨 업 해서 좋고. 상부상조지. 상부상조.’

애써 자기합리화를 시키며 물었다.

“머릿수가 얼마나 됩니까?”

“적들의 위치를 파악하는 도중에 놈들이 하는 이야기를 들었소. 조필을 포함해 서른 남짓이라고 하더군.”

“서른? 삼십 명이요?”

“그렇소. 그러니 어서 피해야…….”

공야청의 목소리가 멀어진다. 그 대신 저 멀리서 희미한 소리가 가까워졌다. 띠링. 띠링. 띠링.

들린다. 레벨 업 하는 소리가. 로그아웃하는 소리가!

나는 자꾸만 치솟는 입꼬리를 억누르며 말했다.

“여기서 나머지 놈들을 기다립시다.”

“기다린다니. 그게 무슨 말이오?”

“일망타진! 그런 악독한 놈들을 살려 둘 수 없습니다!”

“아니, 홍 대협. 내 말을 좀…….”

“은인 같은 고수라면 할 수 있습니다! 감사합니다. 은인!”

소천이 눈물을 글썽이며 내 품에 달려들었다. 나는 두 팔 벌려 녀석을 끌어안았다.

“그래. 놈들을 다 죽이자!”

“죽이자!”

“조필 개새끼!”

“개새끼!”

그때 공야청이 입을 열었다.

“조필은 절정 고수요.”

“조필 씹새…… 예?”

“일문일살 조필. 산서성을 통틀어도 몇 안 되는 절정 고수란 말이오. 놈이 온갖 은원에 얽혀 있으면서도 지금까지 살아남을 수 있었던 이유가 무엇이겠소?”

“설마…….”

“그에게 덤비는 자는 다 죽었소. 조필은 그런 자요. 잔혹하고, 그만큼 강하지.”

“아.

뭔가 이상함을 감지한 어린 눈동자가 나를 올려다본다.

“소천아.”

“예. 대협.”

“생각해 보니 지금은 때가 아닌 것 같다.”

“예?”

“내가 어리석었다. 우선 너희 남매를 본가로 생환시키는 게 최우선인데. 그렇지?”

“…….”

“실은 아까 싸우다가 부상을 입기도 했고, 내 부하들도 많이 지쳐서 힘든 싸움이 될 듯싶다.”

소천의 눈동자가 내 위아래를 훑었다. 적들의 피로 흠뻑 젖어 있긴 했지만 찢어진 곳 하나 없이 멀쩡한 옷이다. 상처가 있을 리 만무했다.

“내상을 입었단다.”

“…….”

이번에는 고개를 돌려 정찰조원들을 바라봤다. 칼 한 번 안 휘두르고 전투가 끝난 바람에 쌩쌩하다 못해 펄펄 날아다닌다.

“보이는 게 다가 아니지.”

“……대협.”

슬그머니 소천을 떼어 내고 외쳤다.

“본가로 돌아간다. 모두 출발 준비해!”

잽싸게 조원들에게 돌아가려는데, 소천의 손이 옷깃을 꽉 붙잡고 놔주질 않는다. 동그란 눈에는 눈물이 글썽하다.

“대협.”

“야, 빨리빨리 안 움직여! 소천아, 내가 지금 좀 바빠서 그런데 이따 이야기하자. 알았지?”

“홍 대혀엽.”

“공야청 아저씨. 아니, 공 대협은 뭐 하세요. 한시가 급한데.”

“……소천아, 이리 오거라.”

공야청이 나를 병신 보듯이 바라보며 소천을 떼어 냈다. 저건 마치 범죄자의 접근을 차단하는 보호자의 손길.

소천이 거의 통곡했다.

“홍길동 대혀업!”

그리고 그 말이 신호탄이었다.

쾅! 굉음과 함께 오두막의 문이 박살 나며 한 사람이 나타났다.



[Lv.22 혁무진]



“진태경 이 씨발 새끼야아아!”

쒸익쒸익. 혁무진의 분노에 찬 눈동자가 정확히 나를 향하고 있었다. 공야청과 소천이 멍한 얼굴로 나를 바라봤다.

“홍 대협?”

“홍길동 대협?”

“아. 그게. 그러니까.”

……에이, 시발.



* * *



“흠.”

조필은 물끄러미 시체를 내려다보았다. 일그러진 표정에 부릅뜬 눈. 피와 눈으로 얼어붙은 그는 흑산도라는 별호로 불렸었다.

“쯧쯧. 이 친구, 어쩌다 이렇게 되었나.”

제법 충성심이 깊고 똘똘한 놈이었는데, 이렇게 허망하게 갈 줄은 몰랐다.

“그러게, 내가 누누이 말하지 않았나. 두 눈 크게 뜨고 다니라고.”

조필은 흑산도의 부릅뜬 눈을 잡고 벌렸다.

얼어붙은 살이 찢어지며 끔찍한 소리가 새어 나온다.

찌직. 찌지직.

다른 이들은 숨도 못 쉬고 그 모습을 지켜봤다.

평소와 다름없는 표정과 말투였지만 그들은 조필이 분노했다는 사실을 온몸으로 느끼고 있었다.

절정 고수가 뿜어내는 살기에 숨이 막히고 식은땀이 흘렀다.

‘그럴 만도 하지.’

이십여 명이 전멸했다. 그것도 고작 삭주 지부의 잔당이나 처리하는 임무에.

일문일살. 마음에 드는 적을 만나면 꼭 한 가지 질문을 하고 죽인다는 괴악한 성격의 조필이다.

낭인들은 흑산도가 죽어서 다행이라고 생각했다. 살아 있었다면 한층 더 끔찍한 일을 겪었을 테니까.

“이제 좀 낫구먼.”

조필이 바지춤에 피를 닦아 내며 일어났다.

“그래, 다들 어떻게 생각하나? 가감 없이 말해 보게.”

“당연히 명령대로 움직여야지.”

한 사람이 나섰다. 단정한 복장과 점잖은 태도의 중년인, 그리고 그 뒤로 시립한 십여 명의 무사들은 항산검문이 낭인들을 통제하기 위해 보낸 감시자이자 길잡이였다.

조필이 빙긋 웃었다.

“아, 그래. 우리 대항산검문의 당주님을 잊고 있었구려. 그런데 명령이라니?”

“삭주 지부를 지우고 본대와 합류하라. 소문주의 명령을 벌써 잊은 건가?”

“명령이라, 의뢰를 받은 기억은 있소만.”

“그게 그거 아닌가!”

중년인이 불쾌한 얼굴로 조필을 응시했다.

“애초에 여기까지 온 것부터가 그대의 독단이었지. 한데 그 결과가 어떤가? 일개 지부 잔당 따위한테 스물이 넘는 수하들을 잃지 않았나!”

“그러니까 쫓아야지. 반나절이면 놈들을 끝장낼 수 있소.”

“정양까지는 모르나, 혼주까지 쫓는다면 역공당할 우려가 있지. 이 이상의 독단은 내가 허락하지 않겠다.”

“허락이라, 허락…….”

곰곰이 생각에 잠겨 있던 조필이 입을 열었다.

“안 되겠어. 마음에 안 드는군.”

“그게 뭐……!”

퍼걱. 목뼈가 으스러진 그는 말을 끝마치지 못하고 절명했다. 빛살 같은 속도로 중년인의 목을 꺾은 조필이 입술을 핥았다.

“나는 전쟁이 좋아. 누가 죽어도 잊히거든.”

“이노옴!”

상황을 파악한 항산검문의 무사들이 병장기를 빼 들었지만, 조필은 이미 그들 사이로 파고든 뒤였다.

퍼걱, 촤악!

눈밭 위로 더운 피가 쏟아졌다. 조필이 맹수처럼 날뛸 때마다 누군가의 목이, 팔이, 다리가 뜯겨 훨훨 날았다.

“끄아아…….”

이름 모를 무사의 신음이 마지막이다.

시체 더미 위, 짓눌린 침묵 속에서 조필이 말했다.

“놈들을 추격한다.”

이번에는 아무도 입을 열지 않았다. 도망치듯 준비를 서두르는 수하들의 모습을 뒤로하고, 조필은 시신들을 바라봤다.

‘어떤 놈일까.’

그는 절정 고수다. 시신들의 몸에 남은 상흔과 족적을 통해 상대의 모습을 그려 낼 수 있었다.

단 한 사람. 뛰어난 실력의 창수(槍手)가 이 자리에 있었다. 다른 이십여 명을 도륙한 것도 바로 그자다.

‘흑산도를 일격에 죽인 놈이니 오죽할까.’

특히 가슴을 관통한 마지막 일격은…… 조필이 흥미를 갖기에 충분했다.

‘재미있는 싸움이 되겠어.’

누구일까. 태원진가의 고수? 아니면 알려지지 않은 누군가?

아무래도 상관없다. 조필은 기분 좋은 웃음을 터트렸다.

“조만간 만나자고. 친구.”



* * *



“들어온 소식은?”

“없습니다. 그저 최대한 빨리 이동하는 수밖에는…….”

“젠장, 젠장!”

위팽은 분통을 터트렸다. 하지만 방법이 없었다. 수하의 말처럼 최대한 빨리 삼공자를 찾아 보호하는 수밖에는.

‘일문일살 조필…….’

놈의 악명은 익히 들어서 알고 있다. 만일 삼공자가 놈의 손에 들어간다면 결과는 죽음뿐이다.

‘그렇게 되면 주군을 볼 면목이 없다.’

진위경은 초인적인 인내심으로 참아 냈다.

그는 현재 태원진가의 머리이자 중심에 있다. 누구보다 사랑하는 동생과 수백의 식솔을 저울에 올려놨고, 장고 끝에 가장 믿는 수하인 위팽을 동생에게 보냈다.

그런데 만약 실패한다면…….

‘주군을 볼 면목이 없어.’

고삐를 잡은 손에 힘이 들어간다. 위팽은 박차를 가했다. 그의 뒤로 이십여 기의 기마가 꼬리를 물고 달렸다.
```

### Current accepted English

```markdown
# Chapter 25

“Is this the afterlife?”

That was the first thing the middle-aged man said when he woke up.

Before I could answer, something small sprang forward and threw itself into his arms.

The child, tears dangling from the corners of his eyes, shouted.

“Uncle Gong!”

“Socheon! You’re safe. But what in the world…?”

The confused middle-aged man listened as the child explained through sobs. When he heard that we had met on the hill and that all the enemies had died by my hand, his eyes widened.

“Are you from the main family?”

“Yes. That’s right.”

“Ah, Heaven has helped us!”

“…”

*I helped you, you old man.*

“I was sure I’d fallen to the bottom of the mountain… I thought that was the end of me.”

“You nearly did. You were lucky.”

I pointed below the ridge. Two corpses presumed to belong to the enemy lay with their heads buried in trees.

If the grass along the path where he had slipped had not been so thick, he would have ended up just like them.

*I didn’t realize it at first, either.*

I only became aware of the middle-aged man’s presence thanks to the Quest window.

Even after I defeated all the enemies, the **Survivors of the Sakju Branch** Quest had not been completed. That meant there were more survivors.

*The question was whether there were any survivors besides this man…*

The last trace of unease vanished the moment I helped the exhausted middle-aged man to his feet.

Ding.

> **System**
>
- You completed the **Survivors of the Sakju Branch** Quest!
> - A Chain Quest has been created!
> - You leveled up!
> - You leveled up!
> - Merit and Fame increase!

* * *

“Whew.”

The middle-aged man exhaled. Though he had only circulated his qi briefly, his complexion had improved noticeably.

He rose and respectfully clasped his hands in a salute.

“Benefactor, you saved everyone.”

“Not at all. I only did what anyone should have done.”

Every time I opened my mouth, lies came spilling out. It wasn’t entirely wrong, either. I had to clear the Quest somehow.

*If anything, I’m the one who should be bowing to them and thanking them.*

Still, Santa Claus—or rather, the survivors—seemed deeply moved by my attitude.

“Outstanding martial arts and a sense of chivalry, too. I, Gong Yacheong, sincerely admire you.”

“Socheon and Soyul owe Great Hero an enormous debt of gratitude.”

Thanks to that, I learned their names. The middle-aged man was Gong Yacheong, and the young siblings were Socheon and Soyul.

“If it isn’t too impertinent, may I ask our Benefactor’s name?”

“My name is…”

Then I had a thought.

*Wait. If I tell them my name, won’t they come running at me with swords?*

Whatever conspiracy had been involved, the person who had lit the fuse on this war was none other than me, Jin Taekyung. It was hard to believe that two people who had lost their home and family would look kindly on me.

*Yes. This is the moment for a well-intentioned lie.*

“Hong Gil-dong. My name is Hong Gil-dong.”[^1]

“Hong Gil-dong… I’ve never heard that name before. But I can feel the bearing of a hero.”

Socheon chimed in from the side.

“Here one moment, there the next. It sounds like the name of someone who appears and disappears like a ghost.”

*…How did that kid know?*

Before he could bring up the tale’s business about calling one’s father Father and one’s elder brother Brother,[^2] I hurriedly changed the subject.

“More importantly, what happened?”

Dark shadows fell across both their faces.

Gong Yacheong spoke first.

“It happened only a few days ago.”

By the time the carrier pigeon bearing word of war arrived, the Sakju Branch had already been surrounded so tightly that not even a drop of water could get through. The wandering martial artists hired by the Mount Heng Sword Sect had slaughtered people and burned down the buildings.

“There must have been a full hundred of them. Thanks to the Branch Leader and the martial artists under him buying us time, we were able to escape through a secret passage. Most of those who escaped were women and children who knew no martial arts.”

I didn’t need to ask what had happened to the others.

The System was absolute and factual. Those three were all the survivors of the Sakju Branch identified by the Quest Window.

“I want to know about the enemy.”

“They’re wandering martial artists.”

“Wandering martial artists?”

“As you know, they’re bastards who’ll do anything for money. The especially vile ones among them were hired by the Mount Heng Sword Sect to attack us.”

“They seemed pretty weak for such vile bastards.”

“Do good and evil determine who is strong and who is weak? The ones they hired this time were ordinary wandering martial artists, common as dirt. The leader was the problem.”

Gong Yacheong gritted his teeth.

“Jopil, One Question, One Kill. That was the man. The Branch Leader sensed defeat the moment he saw him and entrusted his family members to me.”

Socheon’s small fists trembled.

“I’ll tear him limb from limb and kill him with my own hands.”

That was an unusual choice of words for a child, but considering the grudge carved into his bones, it was understandable.

I gently patted Socheon on the head.

“That is exactly what will happen. I’ll help you.”

“Really?”

“A man’s word is worth a thousand pieces of gold. Do you think I’d say one thing and do another? I’ll definitely catch that bastard and level u—”

“Huh?”

“No, I mean I’ll kill him and avenge your grudge.”

“Ah… Thank you. Thank you so much, Great Hero Hong!”

“Thank you. Truly, thank you!”

The two of them repeatedly expressed their gratitude. I felt like a real scumbag, and a sharp stab tore through one corner of my chest.

*No. They’ll be happy when their enemy dies, and I’ll be happy when I level up. It’s mutually beneficial. Mutually beneficial.*

I forced myself to accept that justification and asked,

“How many of them are there?”

“While we were trying to determine the enemies’ position, I overheard them talking. They said there were about thirty, including Jopil.”

“Thirty? Thirty men?”

“That’s right. So we need to flee at once…”

Gong Yacheong’s voice began to fade. In its place, a faint sound from far away drew closer.

Ding. Ding. Ding.

I could hear it. The sound of leveling up. The sound of logging out!

Suppressing the corners of my mouth as they kept creeping upward, I said,

“Let’s wait here for the rest of them.”

“Wait? What do you mean?”

“Wipe them all out! We can’t let such vile bastards live!”

“No, Great Hero Hong, listen to me…”

“A master like you can do it! Thank you, Benefactor!”

Socheon came running into my arms with tears in his eyes. I opened both arms and pulled him into a hug.

“That’s right. Let’s kill them all!”

“Let’s kill them!”

“Jopil, you son of a bitch!”

“Son of a bitch!”

That was when Gong Yacheong spoke.

“Jopil is a Peak master.”

“Jopil is a fucking bast—huh?”

“Jopil, One Question, One Kill. He’s one of the few Peak masters in all of Shanxi. What do you think is the reason he has survived until now, despite being tangled up in all kinds of grudges and vendettas?”

“Don’t tell me…”

“Everyone who challenged him died. That’s the kind of man Jopil is. Cruel—and every bit as strong.”

“Ah.”

Sensing that something was wrong, Socheon looked up at me.

“Socheon.”

“Yes, Great Hero.”

“Now that I think about it, this probably isn’t the right time.”

“Huh?”

“I was being foolish. The priority should be getting you and your sister safely back to our family. Right?”

“…”

“I was injured during the fight earlier, too, and my men are exhausted. It looks like it would be a difficult battle.”

Socheon looked me up and down. My clothes were soaked in the enemies’ blood, but they were perfectly intact, without a single tear. There was no way I could have been injured.

“I have an internal injury.”

“…”

He turned to the reconnaissance squad. They had not even swung their swords once, and they were bursting with energy.

“What you see isn’t everything.”

“…Great Hero.”

I slipped Socheon off me and shouted,

“We’re returning to the main family. Everyone, prepare to leave!”

I hurried back toward the squad, but Socheon’s hand clutched my collar tightly and refused to let go. Tears glimmered in his round eyes.

“Great Hero.”

“Hey, why aren’t you moving? Move, move! Socheon, I’m a little busy right now, so let’s talk later. Okay?”

“Great Heeero.”

“Mister Gong Yacheong. No, Great Hero Gong, what are you doing? Every second counts.”

“…Socheon, come here.”

Gong Yacheong looked at me as if I were an idiot and pulled Socheon away. His hand came between me and Socheon like a guardian blocking a criminal.

Socheon almost wailed.

“Great Hero Hong Gil-dooong!”

And that was the starting gun.

With a thunderous boom, the cabin door was smashed apart, and someone burst in.

> **System**
>
> - **Level 22 Hyuk Mujin**

“Jin Taekyung, you fucking bastard!”

Hyuk Mujin huffed and puffed, his furious eyes locked on me. Gong Yacheong and Socheon stared at me with blank expressions.

“Great Hero Hong?”

“Great Hero Hong Gil-dong?”

“Ah. Well, you see…”

*…Fuck.*

[^1]: Hong Gil-dong is a legendary Korean outlaw and folk hero.

[^2]: In the Hong Gil-dong tale, he demands the right to address his father as “Father” and his elder brother as “Brother.”

* * *

“Hmm.”

Jopil stared down at the corpse. The face was twisted, its eyes wide open. Frozen beneath blood and snow, the man had been known by the nickname Black Mountain Blade.

“Tsk, tsk. How did you end up like this, friend?”

He had been loyal and clever. Jopil had never imagined he would die so pointlessly.

“See? Haven’t I always told you to walk around with both eyes wide open?”

Jopil grabbed Black Mountain Blade’s bulging eyes and pried them farther open.

A horrible sound escaped as the frozen flesh tore.

Rip. Riiip.

The others watched without even daring to breathe.

His expression and tone were no different from usual, but they could feel to their bones that Jopil was furious.

The killing intent radiating from a Peak master made it hard to breathe, and cold sweat trickled down their backs.

*It was understandable.*

More than twenty men had been wiped out. And all on a mission to deal with the remnants of the Sakju Branch.

Jopil, One Question, One Kill, was a bizarre man. Whenever he encountered an enemy he liked, he asked exactly one question before killing them.

The wandering martial artists thought it was fortunate that Black Mountain Blade was dead. If he had still been alive, they would have suffered something even more horrifying.

“That’s better.”

Jopil wiped the blood on his trousers and rose.

“Well, what does everyone think? Tell me without holding back.”

“We should obviously follow the order.”

One man stepped forward. The neatly dressed, dignified middle-aged man and the ten-odd martial artists standing at attention behind him were the overseers and guides the Mount Heng Sword Sect had sent to keep the wandering martial artists under control.

Jopil smiled faintly.

“Ah, yes. I’d forgotten our Mount Heng Sword Sect Hall Master was here. But what’s this about an order?”

“Wipe out the Sakju Branch and join the main force. Have you already forgotten the Young Sect Leader’s order?”

“An order? I remember accepting a commission.”

“Isn’t that the same thing?”

The middle-aged man glared at Jopil, displeased.

“Coming here in the first place was your own arbitrary decision. And what came of it? You lost more than twenty subordinates to the remnants of a single branch!”

“Then we should pursue them. We can finish them off in half a day.”

“Jeongyang might be another matter, but if you pursue them as far as Honju, we risk a counterattack. I won’t permit any more unilateral decisions.”

“Permission. Permission…”

After mulling it over, Jopil spoke.

“No. That won’t do. I don’t like it.”

“What do you mea—”

Crunch.

The middle-aged man’s neck shattered, and he died before he could finish speaking. Jopil had twisted it at blinding speed. He licked his lips.

“I like war. No matter who dies, people forget.”

“You bastard!”

The Mount Heng Sword Sect’s martial artists realized what had happened and drew their weapons, but Jopil had already plunged into their midst.

Crunch. Slash!

Warm blood poured onto the snowfield. Every time Jopil rampaged like a wild beast, someone’s neck, arm, or leg was torn free and sent flying.

“Gaaah…”

The groan of an unnamed martial artist was the last sound.

Standing atop the heap of corpses, Jopil spoke into the crushing silence.

“We’re pursuing them.”

This time, no one said a word. As his subordinates hurried to prepare as though fleeing for their lives, Jopil continued to stare at the bodies.

*What kind of man was it?*

Jopil was a Peak master. From the scars on the corpses and the footprints, he could picture what his opponent looked like.

*Only one man.*

A highly skilled spearman had been here. He was the one who had slaughtered the other twenty-plus men.

*If he killed Black Mountain Blade in one strike, he must be something else.*

The final strike that pierced through Black Mountain Blade’s chest had been particularly interesting.

*This should be a fun fight.*

Who was he? A master from the Jin Family of Taiyuan? Or someone unknown?

It didn’t matter. Jopil let out a pleased laugh.

“Let’s meet soon, friend.”

* * *

“What news have we received?”

“None, sir. All we can do is move as quickly as possible…”

“Damn it! Damn it!”

Wipeng was furious. But there was nothing he could do. As his subordinate had said, the only thing they could do was find the Third Young Master and protect him.

*Jopil, One Question, One Kill…*

Wipeng knew the man’s reputation well. If the Third Young Master fell into his hands, death would be the only possible outcome.

*If that happens, I won’t be able to face my lord.*

Jin Wikyung endured with superhuman patience.

He was currently at the head of the Jin Family of Taiyuan, its central pillar. He had placed his beloved younger brother and hundreds of family members on the scales, and after much deliberation, he had sent his most trusted subordinate, Wipeng, to his brother.

*But if I fail…*

*I won’t be able to face my lord.*

Wipeng’s grip tightened on the reins. He spurred his horse onward. More than twenty mounted riders followed in a long line behind him.
```
## Chapter 27

### Korean source

```text
＃27화



“일각 휴식.”

바람 빠지는 소리를 내며 순찰조원들이 주저앉는다.

힘들어 보이긴 하지만 저놈들이야 뭐, 별다른 걱정은 안 한다. 지켜본 대로라면 기초 체력은 탄탄했고, 전투 때도 넋 놓고 구경만 한 녀석들이니까.

다른 두 명이 문젠데…….

“괜찮아?”

“후욱. 괜찮, 괜찮습니다.”

소천이 거칠게 숨을 몰아쉬며 대답했다. 내가 보기에도 당장은 쓰러질 것 같진 않다. 하지만 지금처럼 이동했다가는 조만간 한계에 부딪힐 것이다.

‘어린 녀석이 고집은 세 가지고.’

앞서 나는 소천에게 제안했었다. 동생과 함께 내게 업혀 가는 게 어떻겠냐고. 답은 단호한 거절이었다.

“힘들면 말해. 너희 둘 정도는 감당할 수 있으니까.”

“지금으로도, 후욱. 충분합니다.”

아닌 것 같은데.

“모두를 위해서 하는 말이다. 쉽게 대답하지 마.”

“알겠습니다.”

대답하는 소천의 눈에 힘이 들어갔다. 나는 곤히 잠들어 있는 소율을 녀석에게 안겨 주고 돌아섰다.

“공 대협.”

핏기 없는 얼굴이 고개를 들었다.

“……진 공자.”

금방이라도 꺼질 듯한 목소리다. 이거 상태가 생각보다 심각한데. 괜찮습니까, 라는 물음이 혀끝에 맴돌다 흩어진다.

“얼마나 버틸 수 있겠어요?”

“모르겠소.”

솔직한, 그리고 심각한 대답이었다.

“벽곡단은요?”

그에게 남은 벽곡단을 몇 개 챙겨 주었었다. 하지만 공야청은 고개를 내저어 보였다.

“별 효력이 없더군요. 어떤 돌팔이가 만들었는지 입맛만 버렸소. 하하.”

“……지금 저 웃으라고 하는 소립니까?”

“재미없었소?”

“네. 하나도.”

“그거 안타깝…… 쿨럭.”

갑작스러운 기침. 흰 눈 위로 핏방울이 떨어진다.

이런 제기랄. 나는 혹여 누가 볼까, 황급히 공야청의 앞을 가로막았다.

“뭡니까? 이 정도는 아니었잖아요.”

반나절 만에 급속도로 악화된 모습이다. 지금의 공야청은 피로가 쌓인 것이 아니라 병자의 기색이 완연했다.

“예견된 일이오.”

공야청의 담담한 눈빛. 그래서 더 불길하다. 만류하는 그의 손길을 뿌리치고 상의 앞부분을 걷어 올렸다.

“아.”

그의 몸은 온갖 상처로 뒤덮여 있었다. 그러나 나를 놀라게 한 것은, 아랫배를 중심으로 퍼렇게 돋아난 핏줄이었다.

“이게 무슨…… 설마?”

공야청이 힘없는 손길로 상의를 여몄다. 다른 누군가, 특히 소천 남매가 볼까 염려하는 듯했다.

“이리 같은 놈들이오. 병장기에 독을 발라 놨더군.”

공야청이 벽곡단을 먹어도 회복되지 않는 이유를 이제야 알겠다. 벽곡단은 허기와 기력만 보충해 줄 뿐, 해독 능력은 전혀 없으니까.

“진작 말했어야죠!”

“그놈들, 돈이 없었는지 싸구려 독을 썼더군. 독기가 미약해서 지난밤에야 알아차렸소. 너무 늦었지.”

독에 당했을 때 공야청의 체력은 이미 바닥이었다. 그런 상황에서 이 날씨에 강행군을 계속했으니…….

“방법이 없습니까?”

“있소.”

“알려 주십시오.”

“하지만 시간이 허락해 주지 않겠지. 나 하나 때문에 천금 같은 시간을 버릴 수는 없소.”

맞는 말이다. 하지만.

“시도는 해 봐야죠.”

“공자.”

“다들 많이 지쳤습니다. 한 시진, 아니 반 시진만 쉬면서 방법을 시도해 보면 될 겁니다.”

“하하.”

“웃지 마시고요. 어차피 이쯤에서 쉬어 갈 생각이었으니까…….”

모르겠다. 지금 내가 무슨 말을 하는지. 횡설수설하는 나를 보는 공야청의 입가에 희미한 미소가 떠올랐다.

“가시오.”

“…….”

“공자도 알고 있지 않소? 지금 시간을 지체한다면 발목이 잡힐 거라는 사실을.”

나는 침묵했다. 그의 말이 맞다. 위태위태한 안색과 각혈하는 모습을 봤을 때부터, 어쩌면 어젯밤부터 이런 상황을 염두에 두고 있었다.

‘결국 이렇게 되나?’

공야청을 버려야 한다. 데려간다면 당장은 살겠지만 그 대신 모두의 발걸음이 느려질 것이다.

만약 내가 그를 짊어진다면?

시스템의 힘을 빌린다지만, 나도 사람이다. 선두에서 길을 만들어 가며 이틀을 걸었고 그만큼의 피로가 누적되었다.

‘남은 벽곡단은 두 개.’

서른 개에 달하던 벽곡단도 다 떨어져 간다. 남은 두 개로 공야청을 짊어진 채 놈들의 손아귀를 벗어날 수 있을까?

그렇게 하고도 끝내 놈들과 맞닥뜨리게 된다면? 지친 상태에서 놈들을, 절정 고수인 일문일살 조필을 상대할 수 있을까?

답은 오래전에 나왔다. 나도, 그도 알고 있었다.

“아이들을 부탁하오.”

공야청의 말과 동시에 시스템 알림이 울린다.

띠링.



퀘스트



[공야청의 마지막 부탁]

이제 그가 바라는 것은 하나뿐입니다. 살아남은 아이들을 안전하게 생환시켜 주십시오.



등급 : 無

제한 : 진태경

임무 : 소천, 소율의 생환 (미완료)

보상 : 없음



- 퀘스트를 수락하시겠습니까?



보상이 없다니.

내가 받아 본 것 중 가장 양심 없는 퀘스트다.

‘나 살기도 바빠, 이 양반아.’

하지만 나는 고개를 끄덕였다. 이걸로 마음 한구석 찝찝함을 덜어 낼 수 있다면 얼마든지.

“그렇게 하죠.”

공야청이 만족스럽게 웃었다.



* * *



“공 대협을 두고 간다고요?”

한엽이 충격받은 얼굴로 중얼거렸다. 혁무진은 무슨 생각을 하는지 말이 없었고, 다른 정찰조원들은 서로 눈치를 살피느라 바빴다.

“그래.”

“말도 안 됩니다!”

“목소리 줄여.”

소천이 알아봤자 좋을 게 없다. 함께 남겠다고 버티고 설 놈이라 더더욱 그랬다.

“하, 하지만 이건…….”

“공 대협이 결정한 거다. 내 생각도 같고.”

그때, 혁무진이 불쑥 입을 열었다.

“이유가 뭡니까?”

이 자식이 덜 맞았나. 나는 눈에 힘을 줬지만 혁무진은 겁먹지도, 물러서지도 않았다. 불끈 쥔 주먹에 힘이 풀렸다.

“상태가 심각해. 이대로라면 우리까지 위험하다.”

“그게 전부입니까?”

“그래.”

한엽이 붉어진 얼굴로 끼어들었다.

“안 됩니다.”

“명령이다.”

“그럼 항명하겠습니다.”

단호한 말투에 모두가 놀란 눈빛으로 한엽을 바라본다.

첫 만남부터 내 열렬한 신봉자를 자처하던 녀석이, 항명을 입에 담을 줄은 나도 몰랐다.

“네가 그런다고 달라지는 건 없어.”

“이대로 두고 갈 수는 없습니다.”

“두고 갈 수 없으면?”

갑자기 피곤이 몰려왔다. 나는 뻑뻑해진 눈가를 문질렀다.

“두고 갈 수 없으면. 네가 업고 갈래?”

“예. 제가 업겠습니다.”

“그리고 금방 지치겠지.”

한엽이 지치면 누군가 나서서 돕겠지. 그렇게 하나씩 지쳐 가고, 발걸음은 느려지고, 적들이 들이닥칠 것이다.

“상대는 절정 고수가 이끄는 닳고 닳은 낭인들이다. 우리가 살아남을 수 있을까?”

한엽은 대답하지 못하고 고개를 떨궜다. 다른 정찰조원들도 시선을 회피했다. 내 눈을 피하지 않는 건 한 사람뿐이다.

“일 호. 아직 할 말이 남았나?”

한참이나 말이 없던 혁무진이 고개를 숙였다.

“명령에 따르겠습니다, 조장님.”



* * *



우리는 다시 이동을 시작했다. 출발 직전, 공야청은 편안한 얼굴로 소천, 소율 남매의 머리를 쓰다듬어 주었다.

“잠시 후에 보자꾸나.”

소천은 씩씩하게 고개를 끄덕였고, 잠이 덜 깬 소율은 칭얼거리며 내 품에 안겼다. 쌕쌕거리는 숨소리를 들을 때마다 가슴 한구석이 불편해진다.

‘지금쯤이면 떠났을까?’

공야청은 어린 남매에게 자신의 부재를 알리고 싶지 않아 했다. 그래서 도중에 조용히 이탈하겠다고 내게 말했다.

소천은 대열의 중간이니 정찰조원들에 가려져 떠나는 그의 모습을 확인할 수 없을 것이다.

‘출발한 지 얼마나 지났지?’

한 식경? 반 시진? 모르겠다. 사방이 어둠에 잠긴 깊은 밤 속에서는 시간의 흐름도 느껴지지 않았다.

한 걸음씩 옮길 때마다 한 가지 생각이 머릿속에서 떠나가지 않는다.

‘떠났겠지. 지금쯤이면.’

당연한 일이었다. 공야청도 나도 알았고 한엽을 제외한 정찰조원들도 수긍했다. 무엇보다…… 내게는 기다리고 있는 가족이 있다. 나가서 맞닥트릴 현실이 있다.

‘그런데 기분이 왜 이렇게 더럽지?’

발이 무겁다. 종아리까지 쌓인 눈 때문만은 아니다. 앞길을 가로막는 풀과 나뭇가지 때문이 아니다.

공야청이라는, 일개 NPC가 자꾸만 마음에 걸렸다.

마지막 웃음이, 보상 하나 없는 싸구려 퀘스트가 생각났다.

항명하던 한엽이 생각났고, 혁무진의 담담한 눈빛이 가시처럼 가슴 한구석을 찔렀다.

‘당연한 건데 왜.’

게임이니까. 게임이라서.

안 버리면 다 죽는다고. 내가 죽는다고! 이 개새끼들아.

“씨이발…….”

목구멍에 턱 걸려 있던 욕이 흘러나온다. 선잠에서 깬 소율이 뭐라 웅얼거리며 내 목을 끌어안았다.

앙증맞을 정도로 작은 손은 차가웠다. 피부 위로 소름이 돋을 정도로 생생했다. 게임이라고는 생각할 수 없을 정도로.

고작 NPC 하나 버린 걸로 양심의 가책을 느낄 정도로.

“……게임 진짜 좆같이 만들었네.”

나는 돌아섰다.

“어디 가십니까?”

성큼성큼 왔던 길을 돌아갔다. 소천도, 정찰조원들의 얼굴도 눈에 들어오지 않았다.

그래서 알 수 없었다. 앞서 어딜 가냐 묻는 혁무진의 얼굴에 얼핏 웃음이 스친 것도, 가장 후미에 있어야 할 한엽의 얼굴이 보이지 않았던 것도.

“훅. 후욱.”

눈밭 위를 바람처럼 내달렸다. 그리고 발견했다.

언덕 아래, 숨이 턱에 차 헐떡거리면서도 이를 악물고 발걸음을 내딛는 한엽의 모습을.

녀석의 등에는 혼절한 공야청이 업혀 있었다.

“너…….”

무슨 말을 해야 할지 모르겠다. 나는 한숨과 함께 한엽의 손을 잡고 끌어올렸다.

“가, 감사합니다.”

시바…….

‘이젠 나도 모르겠다.’



* * *



이곳은 한 사람만을 위한 비처(秘處)다.

그는 삼십 년 전부터 이곳의 주인이 된 후 그 누구의 출입도 금했다. 그것은 세월이 흐르며 굳어 버린 법칙이었고, 다른 이들도 그렇게 생각했다.

- 일은 어떻게 되어 가고 있습니까?

미세한 공기의 울림과 함께 두 그림자는 전음으로 대화를 나누었다.

- 순조롭네. 그쪽은?

- 말해야 입 아프지요.

- 어련할까.

- 혈랑검. 별호치고는 정이 많더군요.

- 이리라고 혈육의 정이 없겠나. 그래서?

- 선발대만 이백입니다. 조필이라고, 웬 정신 나간 놈이 제멋대로 날뛰고 있긴 한데…… 뭐, 괜찮겠지요.

- 일문일살 조필? 혈랑검이 제대로 골랐군.

- 망나니 공자가 정신없이 쫓기고 있더군요. 예상에 없던 일이긴 합니다만 이것도 나쁘지 않죠.

- 하하하.

- 혹시?

- 맞네. 내가 보냈네. 끔찍이 아끼는 막냇동생의 목을 보면, 소가주도 마음을 달리 먹겠지.

- 크으, 피도 눈물도 없는 독심. 존경스럽습니다.

- 자네가 할 말인가?

- 저야 답 없는 목숨 하나를 취했을 뿐인데요.

- 덕분에 산서성에 피바람이 불 테고?

- 바라던 바 아닙니까?

- 부정할 수 없군. 맞네. 너무 오래 기다렸어.

- 과실은 더욱 달콤할 겁니다.

- 그러길 바라네.

- 아, 참. 하오문이 끼어들었습니다.

- 하오문? 그놈들이 어떻게?

- 새로 온 지부장이 코가 좋더군요. 이번 일만 마무리되면 쳐 낼 생각입니다.

- 조심하게. 천(天)이 아무리 대단해도 방심은 금물…….

그 순간, 바람이 그쳤다. 공기가 파르르 떨렸다.

- ……내가 실언을 했군.

다시 전음이 들려온 것은 한참 뒤였다.

- 언행에 주의하시는 편이 좋겠습니다.

고양이 발바닥처럼 부드러운 목소리. 그러나 듣는 이는 느꼈다. 시퍼렇게 날이 선 칼날을.

- 내 다시 한번 사과하지.

- 오늘은 이쯤 하지요. 문제가 생기면 일간 다시 찾아뵙겠습니다.

대화는 그것으로 끝이었다. 어떤 기척도, 소리도 없이 상대는 사라졌다.

‘귀신 같은 자들.’

가끔은 궁금할 때가 있었다. 저들의 진정한 정체가 무엇인지. 힘은 어느 정도고 구성원은 누구인지.

하지만 이내 고개를 가로저었다.

‘명을 단축할 뿐.’

인고의 세월을 견딘 것은 과실을 취하기 위해서다. 단순한 호기심으로 대사를 그르칠 수야 있나.

‘참으로 길었다.’

그림자는 달을 향해 손을 뻗었다. 손가락 사이로 새어 나온 희미한 달빛이 은빛 수염을 비추었다.

‘곧…… 모든 것이 제자리를 찾는다.’

대장로는 기껍게 웃었다.
```

### Current accepted English

```markdown
# Chapter 27

“Fifteen-minute break.”

The reconnaissance squad members dropped to the ground with a sound like the air going out of them.

They looked exhausted, but I wasn’t particularly worried about those guys. As I’d observed, they had solid basic stamina, and during the battle they had done nothing but stand around and watch.

The other two were the problem…

“Are you all right?”

“Huff. I’m fine. I’m fine.”

Socheon answered while breathing heavily. He didn’t look like he was about to collapse just yet. But if he kept traveling like this, he would hit his limit before long.

*He’s a stubborn little brat.*

Earlier, I had offered to carry him and his sister. He had refused without hesitation.

“If you’re having trouble, tell me. I can handle carrying both of you.”

“Huff. I’m fine like this. It’s enough.”

*Doesn’t look like it.*

“I’m saying this for everyone’s sake. Don’t answer so quickly.”

“Understood.”

His eyes hardened as he answered. I placed the peacefully sleeping Soyul in his arms and turned around.

“Great Hero Gong.”

The pale-faced man raised his head.

“…Young Master Jin.”

His voice sounded like it might give out at any moment. His condition was worse than I’d expected. The question *Are you all right?* lingered on the tip of my tongue before fading away.

“How long can you hold out?”

“I don’t know.”

His answer was honest—and serious.

“What about the fasting pills?”

I had given him several of the fasting pills I had left. But Gong Yacheong shook his head.

“They’re not very effective. Some quack must have made them. They’ve done nothing but ruin my appetite. Hahaha.”

“…Are you telling me that to make me laugh?”

“Wasn’t it funny?”

“No. Not at all.”

“That’s a shame… Cough!”

A sudden cough.

Drops of blood fell onto the white snow.

*Damn it.*

Worried that someone might see, I hurriedly stepped in front of Gong Yacheong.

“What happened? You weren’t this bad before.”

His condition had deteriorated rapidly in half a day. Gong Yacheong no longer looked merely exhausted. He unmistakably looked like a sick man.

“It was inevitable.”

The calm look in his eyes made it even more ominous. I brushed aside the hand trying to stop me and pulled up the front of his robe.

“Ah.”

His body was covered in all kinds of wounds. But what shocked me were the blue veins spreading outward from his lower abdomen.

“What is this…? Don’t tell me…”

Gong Yacheong weakly fastened his robe again. He seemed worried that someone else—especially Socheon and Soyul—might see.

“Those wolf-like bastards coated their weapons with poison.”

Now I understood why Gong Yacheong hadn’t recovered even after taking the fasting pills. They could only stave off hunger and restore stamina. They had no detoxifying effect whatsoever.

“You should have told me sooner!”

“Those bastards must have been short on money. They used cheap poison. Its potency was weak, so I didn’t notice until last night. By then, it was too late.”

Gong Yacheong’s stamina had already been at rock bottom when he was poisoned. Then he had continued forcing himself through this weather…

“Isn’t there anything we can do?”

“There is.”

“Tell me.”

“But time won’t allow it. I can’t waste such precious time on one person.”

He was right.

But still…

“We have to try.”

“Young Master.”

“Everyone is exhausted. If we rest for one shichen[^1]—no, just half a shichen—and try the method, that should be enough.”

“Hahaha.”

“Please don’t laugh. I was planning to stop and rest around here anyway…”

I didn’t know what I was saying anymore. As Gong Yacheong watched me ramble, a faint smile appeared at the corner of his mouth.

“Go.”

“…”

“You know it too, don’t you? If we waste time here, we’ll be held back.”

I fell silent.

He was right. I had been considering this possibility since I saw his precarious complexion and the blood he coughed up. Perhaps I had been thinking about it since last night.

*So this is how it ends?*

I had to leave Gong Yacheong behind. If I took him with us, he might survive for now, but everyone’s pace would slow down.

What if I carried him myself?

Even with the System’s help, I was still human. I had spent two days walking at the front and clearing a path. Fatigue had piled up with it.

*Two fasting pills left.*

Even the thirty fasting pills I’d had were almost gone. Could I escape those bastards while carrying Gong Yacheong with only two pills remaining?

And if we still ended up running into them, would I be able to fight them while exhausted? Would I be able to face Jopil, One Question, One Kill, a Peak master?

The answer had been clear for a long time.

We both knew it.

“Please take care of the children.”

The moment Gong Yacheong spoke, the System notification rang.

Ding.

> **System**
>
> **Quest**
>
> **Gong Yacheong’s Last Request**
>
> He wants only one thing now. See that the surviving children make it back safely.
>
> **Grade:** None
>
> **Limit:** Jin Taekyung
>
> **Task:** Socheon and Soyul’s safe return (Incomplete)
>
> **Reward:** None
>
> - Would you like to accept the Quest?

There was no reward.

It was the most shameless Quest I had ever received.

*I’m busy trying to stay alive myself, old man.*

But I nodded.

If accepting it could ease even a little of the guilt sitting in the corner of my heart, I was willing to do it.

“Let’s do that.”

Gong Yacheong smiled with satisfaction.

* * *

“You’re saying we’re leaving Great Hero Gong behind?”

Han Yeop muttered with a shocked expression. Hyuk Mujin said nothing, as though he was lost in thought, while the other reconnaissance squad members were busy watching one another’s faces.

“Yes.”

“That makes no sense!”

“Lower your voice.”

There was nothing to gain from Socheon finding out. That was especially true because he would insist on staying behind with Gong Yacheong.

“B-but this…”

“It was Great Hero Gong’s decision. I agree with him.”

That was when Hyuk Mujin suddenly spoke.

“What’s the reason?”

*Has this bastard not been beaten enough?*

I glared at him, but Hyuk Mujin neither flinched nor backed down. My fist, which had tightened instinctively, slowly relaxed.

“His condition is serious. If we continue like this, he’ll put all of us in danger.”

“Is that all?”

“Yes.”

Han Yeop cut in, his face flushed.

“No.”

“It’s an order.”

“Then I’ll disobey.”

Everyone stared at Han Yeop in surprise.

I hadn’t expected the boy who had declared himself my ardent follower from the very first time we met to use the word *disobey*, either.

“Nothing will change just because you say that.”

“We can’t leave him like this.”

“If we can’t leave him behind, then what?”

Fatigue suddenly swept over me. I rubbed at the corners of my stiff eyes.

“I’ll carry him.”

“Yes. I’ll carry him.”

“And you’ll get tired soon.”

If Han Yeop got tired, someone else would step forward to help him. Then they would grow tired one by one, our pace would slow, and the enemy would catch up.

“Our opponents are a pack of battle-hardened wandering martial artists led by a Peak master. Do you think we can survive?”

Han Yeop lowered his head without answering. The other members of the reconnaissance squad avoided my gaze as well.

Only one person continued to meet my eyes.

“Number One. Do you still have something to say?”

Hyuk Mujin had been silent for a long time. He finally bowed his head.

“I’ll follow your orders, Squad Leader.”

* * *

We began moving again.

Just before we left, Gong Yacheong gently stroked Socheon and Soyul’s heads with a peaceful expression.

“I’ll see you soon.”

Socheon nodded bravely. Soyul, still half-asleep, whimpered and nestled into my arms.

Every time I heard her shallow, wheezing breaths, a pang of unease tightened in my chest.

*Has he left by now?*

Gong Yacheong hadn’t wanted the children to know he was gone. That was why he had told me he would quietly slip away along the way.

Socheon was in the middle of the formation, so the reconnaissance squad members would block his view. He wouldn’t be able to see Gong Yacheong leave.

*How long has it been since we left?*

A sikyeong? Half a shichen?

I didn’t know. In the dead of night, with darkness swallowing everything around us, I couldn’t even feel time passing.

With every step I took, one thought refused to leave my mind.

*He must have left by now.*

It was only natural. Gong Yacheong and I knew it, and everyone in the reconnaissance squad except Han Yeop had accepted it.

Most importantly…

I had a family waiting for me. The real world was waiting for me outside.

*Then why does this feel so damn awful?*

My feet felt heavy.

It wasn’t just because snow had piled up to my calves. It wasn’t because grass and branches blocked the path ahead.

It was because a mere NPC named Gong Yacheong kept weighing on my mind.

I thought about his final smile. I thought about the cheap Quest with no reward.

I thought about Han Yeop’s defiance. Hyuk Mujin’s calm gaze pricked my chest like a thorn.

*It’s only natural. So why?*

Because it was a game.

Because it was only a game.

*If I didn’t leave him behind, everyone would die. I’d die, too! You fucking bastards!*

“Fuuuck…”

The profanity that had been caught in my throat spilled out.

Soyul stirred from her light sleep and mumbled something as she wrapped her arms around my neck.

Her tiny hands were cold. They felt so real that goose bumps rose across my skin. Too real to believe this was a game.

Real enough that I felt guilty over abandoning a single NPC.

“…What a fucked-up game.”

I turned around.

“Where are you going?”

I strode back the way we had come. I couldn’t see Socheon’s face or the faces of the reconnaissance squad members.

That was why I didn’t notice the fleeting smile that crossed Hyuk Mujin’s face when he asked where I was going.

I also didn’t notice that Han Yeop, who should have been at the very rear, was no longer there.

“Huff. Huuuff.”

I sprinted across the snow like the wind.

And then I found him.

Below the hill, Han Yeop was gritting his teeth and forcing one foot in front of the other despite gasping for breath.

Gong Yacheong, unconscious, was on his back.

“You…”

I didn’t know what to say. With a sigh, I grabbed Han Yeop’s hand and pulled him up.

“Th-thank you.”

*Shit.*

*I don’t know anymore, either.*

* * *

This was a hidden retreat reserved for one person.

After becoming its owner thirty years ago, he had barred everyone else from entering. Over time, that had hardened into an unbreakable rule, and the others thought of it the same way.

“How are things going?”

As the air trembled faintly, the two shadows conversed through Sound Transmission.

“Smoothly. And you?”

“There’s no need to ask.”

“I wouldn’t expect otherwise.”

“The Blood Wolf Sword. He’s surprisingly fond of his family for someone with that epithet.”

“A wolf can still love its own blood. So?”

“The vanguard alone numbers two hundred. A madman named Jopil is running wild as he pleases, but… it should be fine.”

“Jopil, One Question, One Kill? The Blood Wolf Sword chose well.”

“The wastrel young master is being chased for his life. It wasn’t part of the plan, but it isn’t bad, either.”

“Hahahaha.”

“Could it be…?”

“That’s right. I sent him. When the Lesser Family Head sees the head of his beloved youngest brother, he’ll change his mind.”

“Whew. A heart as cold as poison, without blood or tears. Impressive.”

“Is that something you should be saying?”

“I only took one hopeless life.”

“And thanks to that, a bloody storm will sweep across Shanxi?”

“Isn’t that what you wanted?”

“I can’t deny it. Yes. I’ve waited too long.”

“The fruit will be all the sweeter.”

“I hope so.”

“Ah, yes. The Lower District Sect has gotten involved.”

“The Lower District Sect? How did they?”

“The new Branch Leader has a good nose. Once this matter is finished, I plan to drive them out.”

“Be careful. No matter how formidable Heaven may be, one must never let one’s guard down…”

At that moment, the wind stopped.

The air trembled.

“…I misspoke.”

It was a long while before another message came through Sound Transmission.

“It would be wise to watch your words and actions.”

The voice was soft as a cat’s paw.

But the listener could feel the razor-sharp blade hidden beneath it.

“Let me apologize once more.”

“Let’s end things here for today. If a problem arises, I’ll come see you again soon.”

The conversation ended there.

The other person vanished without a sound or trace.

*They were like ghosts.*

Sometimes, he wondered what their true identities were. How strong were they? Who were their members?

But he soon shook his head.

*That would only shorten my life.*

He had endured years of hardship to reap the fruit. He couldn’t let mere curiosity ruin his plans.

*It truly has been a long time.*

The shadow reached a hand toward the moon. Faint moonlight slipping between his fingers illuminated a silver beard.

*Soon… everything will fall into place.*

The Head Elder smiled with delight.

[^1]: A shichen is a traditional time period of roughly two hours; a sikyeong is a shorter traditional interval.
```
## Chapter 28

### Korean source

```text
＃28화



후우.

가부좌를 튼 채 호흡을 골랐다. 내뱉는 숨에는 미처 갈무리하지 못한 기(氣)가 섞여 있다.

‘아깝다.’

운기조식은 외부의 기를 받아들여 내부의 기와 함께 순환, 축적하는 행위다. 하지만 체내에 남는 기는 소량에 불과했다.

대부분의 기운은 다시 자연으로 돌아간다.

‘소설에서는 조금만 해도 쭉쭉 오르던데.’

천하제일의 무공? 천고의 영약?

여긴 그런 거 없다. 진가심법의 등급이 절정이긴 하지만 공력 축적에는 영 젬병이고 영약은 개뿔, 구경도 못 해 보고 고생만 죽도록 했지 뭐.

‘희망은 하나뿐인가?’

단전 한구석에 웅크린 또 다른 공력. 그걸 전부 내 것으로 만든다면 앞으로의 싸움에 큰 도움이 될 것이다.

문제는 아무리 시도해 봐도 요지부동이라는 사실이다.

‘움직여라. 움직여!’

지금껏 장군바위처럼 버티고 있던 놈이 움직일 리가 있나. 공력을 끌어 올려 봤지만 묵묵부답이다. 나는 한숨과 함께 자리에서 일어났다.

“출발입니까?”

주위를 경계 중이던 혁무진이 물었다.

“그래.”

“알겠습니다.”

그러더니 잽싸게 순찰조원들을 준비시키고 소율을 품에 안는다. 어안이 벙벙해지는 순간이다.

‘이 자식이 뭘 잘못 먹었나.’

갑자기 왜 이렇게 빠릿빠릿해졌지?

주먹을 들이밀어야 마지못해 움직이던 놈인데, 어째 인간이 좀 달라진 것 같다.

‘나야 좋지만.’

잡생각은 치워 버리고 공야청을 둘러업었다. 중독 증상이 심해지면서 그의 안색은 검푸르게 변색되어 있었다.

혁무진이 걱정스럽게 물었다.

“괜찮을까요?”

“괜찮아야지.”

이미 할 수 있는 최선을 다했다. 공야청이 버텨 주기를 바랄 뿐이다. 혼절해 있는 그를 향해 중얼거렸다.

“얼마 남지 않았습니다. 조금만 더 버티세요.”

어스름한 새벽 사이로 햇빛이 비집고 들어왔다. 나는 햇빛을 향해 성큼 발을 내디뎠다.

아니, 내딛으려고 했다.

- 아우우우!

처음에는 바람 소리라고 생각했다. 하지만 그건 살아 있는 짐승들의 울음소리였다. 혁무진이 중얼거렸다.

“늑대들이 배가 고픈 모양이군요.”

“늑대?”

“그럼요. 산에 산짐승이 있는 게 이상한 일은 아니죠.”

고대 중국이 배경인 게임이다. 늑대, 호랑이가 어디서 튀어나와도 이상하지 않다. 나도 지난 며칠간 산짐승들의 울음소리를 여러 번 들었다.

그런데…….

‘기분이 이상해.’

지금까지의 그것과는 다르다. 저 울음소리를 듣는 것만으로도 가슴이 답답해지고 손끝이 찌릿하다.

지난 7년간의 경험으로 벼려 낸 직감이 속삭이는 듯했다. 아직 햇빛이 비치지 않은 저 숲 너머에 뭔가가 있다고.

“전투 준비.”

“그럼 이제 출발…… 예?”

“수비 대형 펼쳐.”

혁무진은 이내 정신을 차리고 내 명령을 전달했다. 얇은 철을 씌운 방패를 든 정찰조원 셋이 눈 덮인 길을 틀어막는다.

비좁은 오솔길에 언덕 위의 고지대. 유리한 위치다.

- 아우우우!

두 번째 늑대 울음소리가 들렸다. 더 가깝고, 그래서 불길하다. 혁무진이 조심스럽게 입을 열었다.

“단순한 늑대 무리인 것 같습니다만…….”

“그럼 더 좋고.”

“너무 시간을 지체하는 건 아닐까요?”

나는 고개를 저었다. 꼬박 이틀을 도망쳤다. 이 잠깐의 시간 때문에 붙잡힌다면 그건 운명인 거다.

“대기해. 조금만 더 기다린다.”

내 말을 짐승들도 알아들은 모양이다. 일 다경 동안 울음소리는 끊이지 않고 가까워졌다. 눈 덮인 새벽 산중에 나뭇가지 부러지는 소리와 눈 위를 뛰어오는 소리가 요란했다.

“한두 마리가 아닌 모양입니다.”

혁무진이 슬쩍 내 얼굴을 바라봤다.

“들리는 소리로는 수십 마리는 될 듯한데…… 늑대가 무리를 짓는 짐승이라지만 이상하긴 하군요.”

그 말이 끝나기가 무섭게 늑대 무리가 모습을 드러냈다. 겨울이라 먹잇감을 구하지 못했는지 대부분 갈빗대가 앙상하다. 하지만 그 본질은 맹수. 방심할 수 없다.

‘그것도 굶주린 맹수지. 애들이 다칠 수도 있겠어.’

생각과는 반대로 묘한 안도감이 들었다. 무림인들이 널리고 널린 곳이지만 설마 짐승까지 무공을 익혔을까.

느낌 운운할 것도 없이 손쉬운 상대인 것이다.

‘레이드 좀 안 뛰었다고 감 다 죽었네.’

나는 혀를 차며 앞으로 나섰다. 맹렬히 뛰어오는 수십 마리의 늑대들이 벌써부터 경험치 덩어리로 보인다.

“빨리 끝내자. 응?”

저 멀리 선두에서 달려오는 늑대에게 손가락을 까딱였다. 덩치를 보아하니 저놈이 우두머리다.

- 크허엉!

아니 무슨 늑대가 사자처럼 울어. 설마 뭐 영물, 그런 건가? 설마 나 짐승한테 지는 거야?

‘그건 안 되지.’

침을 삼키며 창을 곧추세웠다. 기 싸움에서 밀리면 안 된다는 생각에 눈에 힘을 빡 주고 목소리를 깔았다.

“와라.”

효과는 굉장했다!

- 크르르르.

달려오던 놈이 갑자기 방향을 틀어 숲속으로 뛰어든다. 수십 마리의 부하 늑대들도 우두머리를 따라 우르르 사라졌다.

아니, 이건 도망친 거다. 눈 위에 무수히 찍힌 발자국들 위로 찬 바람이 불었다.

‘뭐야, 이거.’

산 채로 씹어 먹을 것처럼 달려오더니 왜 도망쳐?

그때 문득 모 유명 만화가 생각났다. 과잉 행동 장애를 앓고 있는 고무 인간이 해상 공권력을 박살 내는 스토리.

“서, 설마 거기에 나오는 그거?”

기운만으로도 적을 겁먹게 만들고 기절시키는 그 능력.

워낙 정신 나간 게임이니 충분히 가능한 얘기다. 그럼 이 시점에서 시스템 알림 한 번 울려 줘야 하는데…….

띠링.

그렇지! 나는 기대에 부풀어서 시스템 음성을 기다렸다.

해괴한 표정을 한 정찰조원들은 신경도 쓰지 않고 쉴 새 없이 중얼거렸다.

“떠라, 떠라, 떠라!”

떴다.

퀘스트창이.



- 퀘스트가 생성되었습니다.



퀘스트



[일문일살 조필]

끈질긴 추격전이 끝났습니다. 당신은 이 잔인하고 집요한 추격자들과 맞닥트렸고, 일문일살 조필을 상대해야 합니다.

부디 명복을…… 아니, 무운을 빕니다.



등급 : 절정

제한 : 진태경

임무 : 생존 (미완료)

보상 : ???

실패 : 사망



- 당신은 퀘스트를 선택할 권한이 없습니다.

- 퀘스트가 강제 수락되었습니다!



“……어?”

이게 무슨 일인가. 여긴 어디고 나는 누구인가.

순간 수많은 물음이 떠올랐고 사라졌다. 그리고 누군가의 목소리가 들려왔다.

“드디어 만났군.”

앙상한 나무 옆, 한 남자가 서 있었다. 이십여 장의 거리. 멀다면 멀고, 가깝다면 가깝다. 문제는 아무도 그의 존재를 몰랐다는 것이다. 나조차도.

‘도대체 언제?’

레벨과 무공의 경지가 오를수록 오감(五感)은 날카로워졌다. 그런데 저 남자는 감지해 내지 못했다. 발소리조차 들리지 않았다.

그가 먼저 말하지 않았다면, 퀘스트창이 뜨지 않았다면 아무것도 모른 채 뒤돌았을 것이다.

‘늑대들.’

그 짐승들은 도망친 것이다. 내가 아닌 저 남자를 피해서.

아까부터 떠나지 않던 불안감이 실체를 드러내는 순간이었고, [기감]은 쓸 필요도 없었다. 나는 이미 남자의 이름을 알고 있으니까.

“조필?”

남자, 일문일살 조필은 활짝 웃으며 고개를 끄덕였다.



* * *



지금까지 내가 만난 절정 고수는 셋이다.

진위경, 위팽, 그리고 대장로. 셋 모두 외관상 절정 고수다운 풍모를 지닌 자들이다. 하지만 일문일살 조필은 달랐다.

‘평범해.’

진위경 같은 거인도, 위팽처럼 날카로운 눈매의 소유자도 아니었고 대장로처럼 은빛 수염을 기르지도 않았다.

일문일살 조필은 적당한 키에 평범한 인상의 소유자였고, 그래서 더 위험해 보였다.

“반갑네.”

조필이 환하게 웃으며 발을 내딛는 순간, 나는 고민할 것도 없이 훌쩍 물러났다.

“민첩하군. 반응도 좋고. 마음에 들어.”

가슴이 쿵쾅거린다. 긴장한 탓인지 쉰 목소리가 새어 나왔다.

“다가오지 마.”

“미안하게 됐네. 너무 반가운 마음에 그만.”

난 하나도 안 반갑다.

“너무 긴장하지는 말게. 단지 이야기를 나누고 싶을 뿐이니까.”

“이야기?”

“그래. 자네를 만나고 싶었거든.”

조필 입장에서는 만나고 싶긴 했을 거다. 불과 며칠 전 수하 스무 명을 잃었으니까.

‘시발. 좆 됐네.’

저런 고수가 나를 찢어 죽일 생각에 이틀 밤낮을 쫓아왔다고 생각하자 속이 울렁거렸다.

“개수작 부리지 마라, 조필!”

크게 소리치자 등 뒤의 공기가 얼어붙는 것이 느껴진다. 조필이 다 안다는 듯 웃었다.

“내 정체를 저들에게 알린다고 뭐가 달라지겠나. 이류, 삼류. 전부 머저리에 쓰레기들이야.”

정찰조원들의 수준을 정확히 짚어 낸다. 이 자식도 시스템을 사용하는 건 아닌지 의심이 들 정도다.

“그러지 말고 잠깐 대화를 나누는 게 어떤가? 자네에게 궁금한 게 많거든.”

“대화? 시간을 벌려는 건 아니고?”

“시간을 번다니. 그게 무슨 말이지?”

“무슨 말이긴. 당신이 수하들을 기다린다는 말이지.”

정곡을 찔린 듯, 조필의 콧잔등이 실룩거렸다. 맞다. 이유는 모르지만 지금 놈은 혼자다. 약간의 희생을 감수한다면 충분히…….

“기다려? 내가? 그 약해 빠진 놈들을?”

“……뭐?”

“앞서 말하지 않았나. 전부 머저리에 쓰레기들이라고. 노력도, 재능도 없는 구제 불능의 인생들이지.”

“…….”

“흑산도 그놈은 그나마 괜찮았는데…… 사람 보는 눈이 없었으니 죽어도 싸. 고수를 못 알아본 죄로 녀석의 눈을 찢어 주고 왔지.”

정정한다. 일문일살 조필은 위험해 보이는 게 아니라 존나 위험한 새끼다.

‘이건 완전히 미친놈이잖아.’

현실에서도, 게임에서도 조필 같은 놈은 처음 봤다. 천연덕스러운 말투와 태도. 놈은 인간을 도구 취급하는 사이코패스다.

“아무튼 자네가 걱정하는 일은 일어나지 않을걸세. 느려 터진 놈들이라 쫓아오려면 반 시진은 걸릴 거야. 모든 게 끝난 후겠지.”

하나는 확실하다. 놈이 생각하는 결말에 자신의 죽음은 들어가 있지 않다는 것.

“어떤가?”

“만약 거부한다면?”

조필은 부드럽게 웃어 보였다.

“자네한테 실망하겠지. 아주 많이.”

실망하면 무슨 일이 벌어질지 대충 그림이 그려진다.

“후배. 나는 자네에게 어떤 원한도 없어. 아니, 오히려 호감이 있는 편이지. 몇 가지만 사실대로 대답해 주면 보내 줄 수도 있네.”

“잠깐. 보내 준다고?”

“그래. 어떤 위해도 가하지 않고 멀쩡히 돌려보내 주지.”

“……정말로?”

“내 목을 걸지. 이 정도면 됐나?”

조필의 얼굴에서 진심이 묻어 나온다. 사이코패스에 종잡을 수 없는 놈이지만 어쩌면 모두가 무사히 살아갈 수도 있다는 생각이 들었다.

“그렇게 하지.”

최악의 상황이 오더라도 싸우기밖에 더 하겠나. 잠깐 시간을 벌면서 놈의 약점을 읽어 낼 생각이었다.

“좋아. 말이 통하는 친구로군, 하하.”

조필이 손뼉을 치며 웃었다. 왼쪽 허리춤에 찬 검갑이 흔들거린다.

‘오른손잡이. 검수.’

그렇게 머릿속에 정보를 입력해 나갔다.

“먼저 자네 나이를 묻고 싶군.”

“스물.”

조필은 눈을 동그랗게 떴다.

“허, 약관에 그 정도 경지라니. 대단하군.”

헌터 생활 7년 동안 F급을 벗어나지 못했는데 게임에서는 무공의 천재 취급 받는다. 묘한 기분이다.

“복장을 보아하니 태원진가의 인물인 것 같은데.”

선선히 고개를 끄덕여 주었다.

“약관에 초일류의 경지라. 그 유명한 진천검은 아닐 테고…… 자네 이름이?”

“진태경.”

“진태경. 진태경. 어디서 들어 본 이름인데? 아!”

곰곰이 생각에 잠겨 있던 조필이 탄성을 내뱉었다.

“망나니 삼공자! 그게 자네라고?”

“망나니는 아니고. 요즘은 잠룡 소리 듣고 있지.”

“푸하하! 그럼 그렇지. 태원진가, 그 고지식한 작자들이 독살은 무슨. 누가 짜 놓은 판인지는 몰라도 일이 재밌게 돌아가는군.”

조필은 흡족한 얼굴로 나를 바라봤다.

“자네에 관한 소문은 익히 들어 알고 있었지. 그건 전부 위장이었나?”

“……뭐, 그렇지.”

“좋아. 숨겨진 칼이라 이거지. 마음에 들어. 무공은 언제부터 익혔나?”

“칠 년.”

아주 틀린 말은 아니다. 무림으로 따지자면 헌터들의 전투법도 일종의 무공이니까.

“칠 년이라. 스승은?”

“없어.”

“스승이 없다?”

한동안 나를 바라보던 조필이 말했다.

“거짓말은 아닌 것 같군.”

“솔직하게 대답하면 살려 준다. 당신이 했던 약속 아닌가?”

“그래, 그랬지. 황당하면서 재밌는 이야기야. 태원진가의 직계가 스승도 없이 약관의 나이에 그 정도 경지에 올랐다…… 허, 참.”

입이 바짝 타들어 간다. 창을 꽉 움켜쥐고 조필의 몸을 훑었다. 지금의 그는 믿을 수 없을 정도로 허점투성이다. 하지만 정말 내 눈에 보이는 게 전부일까?

‘내가 먼저 달려들기를 노리는 것일 수도 있다.’

생각은 더 이상 이어지지 못했다. 조필이 돌연 웃음을 터트렸기 때문이었다.

“으하하! 좋아. 마음에 들어. 약속은 지키지.”

약속을 지킨다고?

설마 했던 일이 사실이 될 줄이야. 나는 멍한 얼굴로 조필을 바라봤다.

“그렇게 볼 것 없네. 사실 처음에는 자네를 꼭 죽이고 싶었는데…… 막상 만나 보니 더 지켜보고 싶다는 마음이 생겼거든.”

조필이 호의가 듬뿍 담긴 목소리로 말을 이어 갔다.

“이런 걸출한 인재를 죽이기에는 아깝지. 이런 상황에서는 더더욱.”

“이런 상황이라니?”

“아, 자네는 모를 수도 있겠군. 복귀하면 알게 될 거야. 그럼 가 보게. 다음에 볼 때는 좀 더 성장해 있길 바라지.”

가도 된다고? 정말로? 나는 경계를 풀지 않은 채 뒷걸음질 쳤다. 조필은 웃으며 나를 바라볼 뿐이었다.

그 모습이 송사리를 놓아주는 낚시꾼의 그것 같았다.

‘호랑이 굴에 들어가도 정신만 차리면 산다더니.’

조필의 어디로 튈지 모르는 성격이 탈출구가 될 줄이야.

안전거리가 확보되자 참았던 숨이 토해졌다. 하지만 숨 돌릴 틈도 없다. 1초라도 빨리 이 자리를 떠야 한다.

“이동한다. 빨리!”

하지만 다음 순간이었다.

“이보게. 후배.”

조필이 어리둥절한 얼굴로 나를 바라봤다.

“지금 뭘 하는 건가?”

“뭘 하다니. 그야 당연히 약속대로 돌아가는…….”

“내가 허락한 건 자네 혼자야.”

“……뭐?”

“이래 봬도 고용된 처지거든. 맡은 임무는 완수해야지.”

임무라니. 설마?

“삭주 지부의 생존자 셋. 그리고 자네가 수하라고 부르는 저 쓰레기들은 두고 가게. 이틀간 수고한 값은 받아야 하지 않겠나?”

어린아이처럼 맑던 눈동자가 번뜩인다. 다음 순간 그의 눈은 포식자의 그것으로 바뀌어 있었다.

“미리 말해 두지. 거부한다면 내가 아주 실망하게 될 거야.”

나는 멍하니 조필과 정찰조원들, 그리고 어린 남매와 죽어 가는 공야청을 바라보았다. 시간은 짧았지만 수십 번의 고민과 갈등 끝에 한마디가 튀어나왔다.

“그럼 실망해, 이 시발 새끼야.”

조필이 광포하게 웃었다.
```

### Current accepted English

```markdown
# Chapter 28

*Hoo.*

I sat cross-legged and evened out my breathing. The breath I exhaled still carried qi I hadn’t managed to draw back in.

*What a waste.*

Circulating qi meant drawing in energy from outside, cycling it together with my internal energy, and accumulating it. But only a small amount stayed in my body.

Most of it returned to nature.

*In novels, you could shoot up just by doing a little of this.*

The greatest martial arts under heaven? An elixir of the ages?

Not here. The Jin Family’s Cultivation Technique was Peak-grade, but it was hopeless at accumulating internal energy. And elixirs? Bullshit. I hadn’t even gotten a look at one. All I’d done was suffer like hell.

*Is that my only hope?*

Another mass of internal energy crouched in a corner of my dantian. If I could make all of it mine, it would be a huge help in the fights ahead.

The problem was that no matter how many times I tried, it wouldn’t budge.

*Move. Move!*

As if the thing that had sat there like a boulder this whole time was going to start moving. I tried drawing up my internal energy, but it gave me nothing. I sighed and got to my feet.

“Are we departing?”

Hyuk Mujin had been watching our surroundings.

“Yeah.”

“Understood.”

Then he briskly got the reconnaissance squad ready and scooped Soyul into his arms. I was left staring.

*What the hell did this bastard eat?*

Why had he suddenly gotten so sharp?

This was the guy who used to move only when I shoved a fist in his face. Somehow he seemed like a different person.

*Not that I’m complaining.*

I shoved the stray thoughts aside and slung Gong Yacheong onto my back. As the poisoning worsened, his face had gone dark blue.

Hyuk Mujin asked, worried, “Will he be all right?”

“He has to be.”

I’d already done everything I could. All I could do was hope Gong Yacheong held on. I muttered toward the unconscious man.

“Not much farther. Just hold on a little longer.”

Sunlight squeezed through the dim dawn. I took a long stride toward it.

No—I started to.

- Awoooooo!

At first I thought it was the wind. But those were the cries of living beasts. Hyuk Mujin muttered,

“The wolves must be hungry.”

“Wolves?”

“Of course. It’s hardly strange for there to be wild animals in the mountains.”

This was a game set in ancient China. Wolves, tigers—nothing jumping out would be strange. I’d heard wild animals crying more than once over the past few days.

But…

*Something feels off.*

This wasn’t like the ones before. Just hearing those howls made my chest tight and my fingertips tingle.

The gut I’d honed over seven years seemed to whisper. Something was beyond that forest, where the sunlight hadn’t reached yet.

“Prepare for battle.”

“Then we’re leaving now… Huh?”

“Form a defensive formation.”

Hyuk Mujin snapped out of it and passed on the order. Three reconnaissance squad members with thin-iron-plated shields blocked the snow-covered path.

A narrow trail, high ground on a hill. Advantageous position.

- Awoooooo!

A second howl. Closer—and more ominous for it. Hyuk Mujin spoke carefully.

“They appear to be nothing more than a wolf pack…”

“Then that’s even better.”

“Won’t this delay us too long?”

I shook my head. We’d been running for two full days. If this brief pause was what got us caught, that was fate.

“Hold. We wait a little longer.”

The beasts seemed to take me at my word. For several minutes the howls never stopped, and they kept getting closer. In the snow-covered mountains at dawn, snapping branches and paws racing over snow made a racket.

“Doesn’t sound like one or two.”

Hyuk Mujin glanced at my face.

“From the sound, there must be dozens… Wolves are pack animals, but this is strange.”

No sooner had he finished than the pack showed itself. Maybe they hadn’t found prey in winter; most of them were nothing but ribs. But they were still predators. We couldn’t let our guard down.

*Hungry predators, at that. The kids could get hurt.*

And yet, oddly, I felt relieved. The place was crawling with martial artists, but it wasn’t as if the beasts had learned martial arts too.

Forget gut feelings—these were easy opponents.

*I skip a few raids and my touch is completely gone.*

I clicked my tongue and stepped forward. The dozens of wolves charging at us already looked like chunks of EXP.

“Let’s wrap this up. Yeah?”

I crooked a finger at the wolf running point in the distance. Judging by the size, that one was the leader.

- Grrrraaaah!

Since when did a wolf roar like a lion? Don’t tell me it was some kind of spirit beast? Was I seriously going to lose to an animal?

*Not happening.*

I swallowed and brought my spear up. I couldn’t afford to lose a clash of qi, so I glared hard and dropped my voice.

“Come.”

The effect was incredible!

- Grrrrr…

The charging wolf suddenly veered off and plunged into the forest. Its dozens of subordinate wolves poured after it.

No—that was a retreat. A cold wind swept over the countless pawprints stamped into the snow.

*What the hell.*

They came running like they were going to eat me alive. Why run?

Then a famous comic popped into my head. The one about a rubber man with hyperactivity disorder smashing the maritime authorities.

“D-don’t tell me it’s that?”

That ability that could scare enemies senseless—knock them out, even—with qi alone.

This game was insane enough that it was entirely possible. In which case the System ought to ping me right about now…

Ding.

There it was! I waited for the System voice, buzzing with anticipation.

I ignored the reconnaissance squad’s bizarre faces and muttered without stopping.

“Come on, come on, come on!”

It appeared.

The Quest Window.

> **System**
>
> A Quest has been created.
>
> **Quest**
>
> **Jopil, One Question, One Kill**
>
> The relentless chase has come to an end. You have come face-to-face with these cruel and tenacious pursuers, and you must confront Jopil, One Question, One Kill.
>
> May you rest in peace… No, fortune in battle.
>
> **Grade:** Peak
>
> **Limit:** Jin Taekyung
>
> **Task:** Survive — Incomplete
>
> **Reward:** ???
>
> **Failure:** Death
>
> - You do not have the authority to choose this Quest.
>
> - The Quest has been forcibly accepted!

“…Huh?”

What was this. Where was I, and who was I?

Countless questions rose and vanished. Then I heard someone’s voice.

“We finally meet.”

A man stood beside a gaunt tree, about twenty zhang away.[^1] Far if you called it far, close if you called it close. The problem was that nobody had known he was there.

Not even me.

*When the hell did he…?*

The higher my Level and martial realm, the sharper my five senses got. And I still hadn’t picked that man up. I hadn’t even heard footsteps.

If he hadn’t spoken first—if the Quest Window hadn’t appeared—I would have turned around without knowing a thing.

*The wolves.*

Those beasts had run. Not from me. From that man.

The unease that hadn’t left me since earlier took on a shape. I didn’t even need Qi Sense.

I already knew his name.

“Jopil?”

The man—Jopil, One Question, One Kill—smiled wide and nodded.

* * *

I had met three Peak masters so far.

Jin Wikyung, Wipeng, and the Head Elder. All three looked the part. Jopil, One Question, One Kill, did not.

*He looks ordinary.*

He wasn’t a giant like Jin Wikyung, didn’t have sharp eyes like Wipeng, and didn’t wear a silver beard like the Head Elder.

Jopil was average height, unremarkable face—and that made him look even more dangerous.

“Nice to meet you.”

The instant Jopil smiled brightly and stepped forward, I sprang back. No thought required.

“Nimble. Good reactions, too. I like you.”

My heart hammered. Maybe from the tension, a hoarse voice slipped out.

“Don’t come any closer.”

“Sorry about that. I got a little too happy to see you.”

I wasn’t happy at all.

“Don’t be so tense. I only want to talk.”

“Talk?”

“Yes. I’ve been wanting to meet you.”

From Jopil’s side, he probably had. He’d lost twenty men just a few days ago.

*Fuck. I’m fucked.*

The thought of a master like that chasing me day and night for two days, wanting to tear me apart, made my stomach turn.

“Don’t give me that bullshit, Jopil!”

When I shouted, I felt the air behind me freeze. Jopil smiled like he already knew.

“What difference does it make if you tell them who I am? Second Rate, Third Rate. All idiots and trash.”

He’d read the reconnaissance squad’s level exactly. I almost wondered if he was using the System too.

“Why not have a short conversation? There’s a lot I want to ask you.”

“A conversation? You’re not just buying time?”

“Buying time? What is that supposed to mean?”

“You know what it means. You’re waiting for your men.”

As if I’d hit the mark, the bridge of Jopil’s nose twitched. Right. I didn’t know why, but he was alone. If I was willing to take a few losses, it might be enough to…

“Waiting? Me? For those pathetic weaklings?”

“…What?”

“Didn’t I already say? They’re all idiots and trash. Hopeless lives. No effort, no talent.”

“…”

“Black Mountain Blade was decent enough, but he had no eye for people, so he deserved to die. I tore his eyes before I left. Punishment for failing to recognize a master.”

Correction. Jopil, One Question, One Kill, didn’t look dangerous.

He was a fucking dangerous bastard.

*This guy’s completely insane.*

I’d never seen anyone like Jopil, in real life or in a game. That unbothered tone and manner. He treated people like tools. A psychopath.

“Anyway, what you’re worried about won’t happen. They’re painfully slow. It’ll take them half a shichen to catch up.[^2] By then, everything will be over.”

One thing was certain. In the ending Jopil had in mind, his own death wasn’t part of it.

“Well?”

“And if I refuse?”

Jopil smiled softly.

“I’ll be disappointed in you. Very disappointed.”

I could more or less picture what happened if he got disappointed.

“Young friend, I have no grudge against you. No—if anything, I’m rather fond of you. Answer a few things truthfully, and I might even let you go.”

“Wait. Let me go?”

“Yes. I won’t lay a finger on you. I’ll send you back in one piece.”

“…Really?”

“I’ll stake my neck on it. Is that enough?”

The sincerity showed on Jopil’s face. Unpredictable psychopath or not, maybe everyone could walk out of this alive.

“All right.”

Even if the worst came, all I could do was fight. I’d buy a little time and try to read his openings.

“Good. A friend who can talk, haha.”

Jopil clapped and laughed. The sword case at his left hip swayed.

*Right-handed. Swordsman.*

I kept inputting the data in my head.

“First, I’d like to ask your age.”

“Twenty.”

Jopil’s eyes went round.

“My. That realm at twenty. Impressive.”

Seven years as a Hunter and I never got out of F-rank. In this game, they treated me like a martial arts genius. Strange feeling.

“Judging by your clothes, you seem to be from the Jin Family of Taiyuan.”

I nodded readily.

“Super First Rate at twenty. You wouldn’t be that famous Heaven Shaking Sword, so… your name?”

“Jin Taekyung.”

“Jin Taekyung. Jin Taekyung. I’ve heard that name somewhere. Ah!”

Jopil had been turning it over. Then he exclaimed.

“The wastrel third Young Master! That’s you?”

“Not a wastrel. These days they call me the Sleeping Dragon.”

“Puhahaha! I knew it. The Jin Family of Taiyuan, those rigid fools, poisoning someone? Please. I don’t know who set this board, but things are getting interesting.”

Jopil looked at me, satisfied.

“I’ve heard plenty of rumors about you. Was all of that a disguise?”

“…Something like that.”

“Good. A hidden blade, then. I like it. When did you start learning martial arts?”

“Seven years.”

Not entirely a lie. By Murim standards, Hunter combat methods were a kind of martial art too.

“Seven years. And your master?”

“Don’t have one.”

“No master?”

He studied me for a while, then said,

“Doesn’t seem like a lie.”

“You promised to spare me if I answered honestly. That was your promise, wasn’t it?”

“Yes, it was. An absurd, entertaining story. A direct descendant of the Jin Family of Taiyuan, no master, that realm at twenty… My, my.”

My mouth was bone-dry. I gripped the spear and scanned Jopil’s body. The openings on him right now were unbelievable. But was what I was seeing really all there was?

*He could be baiting me into attacking first.*

The thought didn’t go any further. Jopil suddenly burst out laughing.

“Hahaha! Good. I like it. I’ll keep my promise.”

He’d keep his promise?

The thing I’d thought was impossible was actually happening. I stared at him, blank.

“No need to look at me like that. Truth is, at first I really wanted to kill you… But now that we’ve met, I find I want to watch you a little longer.”

Jopil went on, his voice full of goodwill.

“It’d be a waste to kill talent like this. Especially in a situation like this.”

“A situation like this?”

“Ah. You might not know. You’ll find out when you return. Go on, then. I hope you’ll have grown a little by the next time we meet.”

I could go? He meant it?

I backed away without dropping my guard. Jopil just smiled at me.

He looked like a fisherman letting a minnow go.

*They say even if you walk into a tiger’s den, you live if you keep your head.*

Who’d have thought Jopil’s wild-card personality would turn into an exit.

Once I had a safe distance, the breath I’d been holding came out. But there was no time to catch it. I had to leave this place a second sooner, if I could.

“We’re moving. Hurry!”

Then—

“Hold on, young friend.”

Jopil looked at me, puzzled.

“What are you doing?”

“What do you mean? Going back, like you promised…”

“I only gave permission for you. Alone.”

“…What?”

“I may not look it, but I’m in someone’s employ. I have to finish the mission I took on.”

The mission. Don’t tell me.

“The three survivors of the Sakju Branch. And those pieces of trash you call your subordinates. Leave them. I should be paid for two days’ work, don’t you think?”

Eyes that had been clear as a child’s flashed. The next instant, they were a predator’s.

“I’ll say this now. If you refuse, I’ll be very disappointed.”

I stared blankly at Jopil, the reconnaissance squad, the young siblings, and the dying Gong Yacheong. Time was short, but after dozens of loops of doubt and conflict, one line came out.

“Then be disappointed, you fucking bastard.”

Jopil laughed savagely.

[^1]: A zhang is a traditional Chinese unit of distance, roughly 3.3 meters.
[^2]: A shichen is a traditional time period of roughly two hours.
```
