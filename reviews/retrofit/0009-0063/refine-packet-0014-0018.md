# Retrospective Patch Plan — Chapters 14–18

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
  "summary": "11 findings in chapters 14-18",
  "findings": [
    {
      "chapter": 14,
      "confidence": 0.99,
      "current": "I faced Lee Seogeun on the Jin Family of Taiyuan’s main training ground.",
      "defect": "The named location 대연무장 is rendered generically instead of using the established term.",
      "id": "R0014-01",
      "rationale": "The glossary fixes 대연무장 as “Grand Training Ground.”",
      "replacement": "I faced Lee Seogeun on the Jin Family of Taiyuan’s Grand Training Ground.",
      "severity": "minor",
      "source": "이소군과 마주 선 이곳은 태원진가의 대연무장이다."
    },
    {
      "chapter": 16,
      "confidence": 1.0,
      "current": "“Did you think I spent three hours focusing on only one thing?”",
      "defect": "Three shichen has been reduced to three hours, halving the stated duration.",
      "id": "R0016-01",
      "rationale": "A shichen is approximately two hours, and the glossary requires the traditional unit to be preserved.",
      "replacement": "“Did you think I spent three shichen focusing on only one thing?”",
      "severity": "critical",
      "source": "내가 세 시진 동안 하나만 붙잡고 있었을까 봐?"
    },
    {
      "chapter": 16,
      "confidence": 1.0,
      "current": "“It’s a messenger hawk.”",
      "defect": "The established courier-bird term is rendered as a hawk.",
      "id": "R0016-02",
      "rationale": "The glossary fixes 전서응 as “messenger eagle.”",
      "replacement": "“It’s a messenger eagle.”",
      "severity": "minor",
      "source": "“전서응(傳書鷹)입니다.”"
    },
    {
      "chapter": 16,
      "confidence": 1.0,
      "current": "Or maybe the Elder Council, which had been constantly watching for an opportunity, had caused some kind of incident.",
      "defect": "The established name of the family body is not used.",
      "id": "R0016-03",
      "rationale": "The glossary fixes 장로원 as “Council of Elders.”",
      "replacement": "Or maybe the Council of Elders, which had been constantly watching for an opportunity, had caused some kind of incident.",
      "severity": "minor",
      "source": "호시탐탐 기회를 엿보고 있는 장로원에서 큰 사건을 터트렸을 수도 있다."
    },
    {
      "chapter": 17,
      "confidence": 1.0,
      "current": "- As a result of repeated training, **Sinews** and **Bones** have each increased by 1.",
      "defect": "Two distinct System attributes are truncated into generic body parts, omitting the meridian and muscle components of their names.",
      "id": "R0017-01",
      "rationale": "The glossary fixes 근맥 as “Sinews and Meridians” and 근골 as “Muscles and Bones”; these are System attributes rather than ordinary anatomical descriptions.",
      "replacement": "- As a result of repeated training, **Sinews and Meridians** and **Muscles and Bones** have each increased by 1.",
      "severity": "major",
      "source": "- 반복 수련의 결과로 근맥과 근골이 1씩 상승합니다."
    },
    {
      "chapter": 17,
      "confidence": 1.0,
      "current": "**Fame:** 73",
      "defect": "The displayed Fame value has been changed from 70 to 73.",
      "id": "R0017-02",
      "rationale": "The source Status Window explicitly displays 70; silently reconciling it with prior events alters a stated System quantity.",
      "replacement": "**Fame:** 70",
      "severity": "critical",
      "source": "명성 : 70"
    },
    {
      "chapter": 17,
      "confidence": 1.0,
      "current": "“Are you sure? You swear that on the name of the Medicine King Hall Leader?”",
      "defect": "The established office title is rendered as “Leader” rather than “Master.”",
      "id": "R0017-03",
      "rationale": "The glossary fixes 약왕당주 as “Medicine King Hall Master.”",
      "replacement": "“Are you sure? You swear that on the name of the Medicine King Hall Master?”",
      "severity": "minor",
      "source": "“확실해? 약왕당주의 이름을 걸고?”"
    },
    {
      "chapter": 17,
      "confidence": 1.0,
      "current": "“Listen to this young bastard. I ought to shove a large needle straight into his perineal acupoint!”",
      "defect": "The named acupoint is replaced with a generic anatomical description.",
      "id": "R0017-04",
      "rationale": "The glossary fixes 회음혈 as “Huiyin Acupoint,” preserving the specific acupoint being threatened.",
      "replacement": "“Listen to this young bastard. I ought to shove a large needle straight into his Huiyin Acupoint!”",
      "severity": "minor",
      "source": "“어린 노무 새끼가 말하는 본새 보소. 대침으로 회음혈을 쑤셔 버릴라.”"
    },
    {
      "chapter": 17,
      "confidence": 1.0,
      "current": "The Elder Council demanded your attendance.",
      "defect": "The established name of the family body is not used.",
      "id": "R0017-05",
      "rationale": "The glossary fixes 장로원 as “Council of Elders.”",
      "replacement": "The Council of Elders demanded your attendance.",
      "severity": "minor",
      "source": "장로원에서 네 출석을 요구했거든."
    },
    {
      "chapter": 18,
      "confidence": 1.0,
      "current": "“The man himself said he didn’t do it! And as the Medicine King Hall Leader said earlier, Lee Seogeun was perfectly fine—”",
      "defect": "The established office title is rendered as “Leader” rather than “Master.”",
      "id": "R0018-01",
      "rationale": "The glossary fixes 약왕당주 as “Medicine King Hall Master.”",
      "replacement": "“The man himself said he didn’t do it! And as the Medicine King Hall Master said earlier, Lee Seogeun was perfectly fine—”",
      "severity": "minor",
      "source": "“본인이 아니라고 하지 않소! 그리고 앞서 약왕당주가 말했듯이 이소군은 멀쩡했…….”"
    },
    {
      "chapter": 18,
      "confidence": 1.0,
      "current": "The family’s highest-ranking elder and the head of the Elder Council.",
      "defect": "The established name of the family body is not used.",
      "id": "R0018-02",
      "rationale": "The glossary fixes 장로원 as “Council of Elders.”",
      "replacement": "The family’s highest-ranking elder and the head of the Council of Elders.",
      "severity": "minor",
      "source": "가문의 최고 웃어른이자 장로원의 수장."
    }
  ]
}
```

## Chapter 14

### Korean source

```text
＃14화



“따라 나와라, 네놈이 저지른 짓의 대가를 치르게 해 주마!”

이소군이 분노에 가득 찬 고함을 내지른 그 순간이었다.

띠링.



퀘스트



[비무]

당신의 방탕함이 드디어 일을 냈습니다!

자신의 일은 스스로 해결해야 하는 법. 쥐꼬리만큼 남은 명예와 항산검문의 분노를 피하기 위해서 남은 방법은 하나뿐입니다.



종류 : 돌발 퀘스트

등급 : 일류

제한 : 진태경

임무 : 비무에서 승리 (미완료)

보상 : 칭호, [승부사]

 대량의 경험치

 명성 50

실패 : 칭호, [색마]

 부상



[비무] 퀘스트를 수락하시겠습니까?

수락    /    거절



“…….”

아니, 고등학교 이후로 연애도 해 본 적 없는 내가 색마 소리까지 들어야 하나?

하루 절반을 레이드 뛰고 고시원에서 쓰러져 자는 게 일상인데 이제는 게임에서 내가 싸지도 않은 똥을 치워야 한다.

‘퀘스트나 좀 잘 주든가.’

30레벨인 이소군을 무슨 수로 상대하란 말인가.

‘이런 미친, 레벨 차이가 두 배가 넘어가는데…….’

이건 절대 하면 안 되는 싸움이다.

나는 퀘스트를 거절했다. 아니, 거절하려고 했다. 하지만 이소군이 한발 빨랐다.

“만약 이 자리에서 도망친다면…… 태원진가는 합당한 대가를 치르게 될 것이다.”

띠링.



- 퀘스트 정보가 갱신되었습니다.

- 퀘스트 거부 시, [항산검문]이 [태원진가]에 선전포고합니다. 또한 [진태경]을 문파 공적으로 지목합니다.



……내 이럴 줄 알았다. 웬일로 선택권을 주나 했지.

내가 한숨을 푹 내쉴 때, 회의장은 숯불 위 가마솥처럼 끓어오르는 중이었다.

“무례하다!”

“어린놈이 가문의 위세를 업고 못 하는 말이 없구나!”

“아무리 삼공자가 개만도 못한 짓을 했어도 그렇지, 본가를 업신여기다니!”

“…….”

다 좋은데 마지막 누구냐.

분위기가 험악해지자 소가주인 진위경이 나섰다.

“모두 진정하시지요. 이 소협도 그만하게. 이번 한 번은 말실수로 생각하고 넘어가지.”

가장 상석에 앉아 낮은 목소리로 경고하는데, 포스가 장난이 아니다. 뿌리 있는 명문가의 차기 가주답다고나 할까.

이소군도 기세에 눌렸는지 확연히 줄어든 목소리로 대답했다.

“알겠습니다. 하지만…….”

“하지만?”

“말실수가 아닙니다. 제가 개인의 자격으로 오늘 이 자리에 왔다고 생각하십니까?”

그 말에 진위경은 물론이고 사람들의 안색이 굳어진다.

맞다. 이소군은 항산검문이 정식으로 보낸 사자(使者)다.

“아버님, 아니 문주께서 제게 모든 권한을 일임하셨습니다.”

“……그래서 원하는 게 뭔가?”

“이미 말씀드렸다시피 삼공자와의 비무를 원합니다.”

아니. 그건 내가 싫은데.

돌아가는 상황을 보아하니 항산검문 이 자식들, 작정하고 시비 털러 온 거다.

이 일로 얻을 수 있는 건 최대한 얻고, 그게 실패하더라도 나 하나 정도는 작살내 버리겠다는 것 같은데…… 이렇게 노골적으로 저격당하니 등골이 서늘하다.

“다른 길도 있겠지. 정말 원하는 걸 말해 보게.”

“태원을 제외한 모든 군현(郡縣)에서 철수. 이 정도면 제 누이의 혼삿길을 막은 대가로 적절하지요.”

말이 끝나기가 무섭게 회의장에 고함이 빗발쳤다.

드문드문 들리는 말로는, 한마디로 속옷 빼고 다 벗겨 먹겠다는 소리였다. 소가주인 진위경의 선택은 보나 마나다.

“불가.”

“하면 비무를…….”

“그 또한 거절하겠네.”

막냇동생에게는 껌뻑 죽는 진위경이다. 척 봐도 위험한 비무에 나를 밀어 넣을 리 없었다.

진위경의 대답에 이소군은 득의양양한 미소를 지어 보였다.

“그럼 남은 길은 하나뿐이군요.”

전쟁.

그 단어를 떠올린 것은 나뿐만이 아니었다. 전쟁이 주는 무게감에 회의장은 침묵에 휩싸였다.

그 침묵 사이에서, 나는 허공을 바라봤다.



퀘스트를 수락하시겠습니까?

수락    /    거절



- 퀘스트 거절 시, [항산검문]이 [태원진가]에 선전포고합니다. 또한 [진태경]을 문파 공적으로 지목합니다.



시스템 메시지 읽고, 땅 보고. 하늘 보고. 그리고 다시 읽고.

‘씨바…….’

어쩔 수 없다. 방법은 하나뿐이다.

“하겠습니다.”

이번만큼은 모든 이들의 반응이 일치했다. 부릅뜬 눈, 벌어진 입. 비무를 제안한 이소군, 거절한 진위경. 회의실 모두가 자신의 귀를 의심하고 있었다.

“자, 잠깐만. 태경아?”

황급히 만류하려는 진위경을 뒤로하고, 이소군에게 말했다.

“나와. 한판 붙자.”

이소군의 입꼬리가 잔인하게 올라갔다.



* * *



겨울바람이 차갑다. 구름 낀 하늘을 바라보며 심호흡했다.

“후우.”

이소군과 마주 선 이곳은 태원진가의 대연무장이다. 멀찍이 떨어진 오십여 명의 사람들은 자리에 앉아 우리를 바라보고 있었다.

태원진가 사람들은 저 새끼가 뭘 잘못 먹었나, 하는 얼굴이고, 항산검문 똘마니들은 손에 팝콘만 없지 아주 놀러 온 모양새다.

아. 전음을 보내는 사람도 있다.

- 막내야. 심호흡해. 심호흡. 후. 하. 후. 하…….

하고 있어. 이 양반아.

근엄한 얼굴을 하고선 똥 마려운 강아지처럼 엉덩이를 들썩거린다. 위팽이 어깨를 누르고 있지 않았다면 당장이라도 난입했을 기세다.

- 걱정 마라. 위험하다 싶으면 이 큰형님이. 막. 어? 저놈이 우리 막내한테 손만 댔다 하면 콱, 씨! 어? 알겠지? 흥분하지 말고 천천히, 안전하게. 할 수 있다. 진태경!

……알겠으니까 진정 좀.

아까 회의장에서는 포스가 철철 흘러넘치더니, 역시 기대를 저버리지 않는 진위경이다.

‘그래도 없는 것보다는 백배 낫지.’

최소한 반병신이 되기 전에는 구해 줄 사람이 있으니까.

진위경에 위팽까지 하면 생명 보험이 두 개다. 좋아.

그렇게 한결 가벼워진 마음으로 이소군을 바라봤을 때, 나는 곧바로 생각을 철회했다.

‘좋긴 뭐가 좋아. 시발.’

항산검문 놈들이 왜 그렇게 자신만만했는지 알겠다.

난데없이 상의를 훌렁훌렁 벗어 던지는데, 연체동물처럼 꿈틀거리는 근육에 숨이 턱 막히고…….



[Lv.30 이소군]



피처럼 붉은 레벨창에 손발이 저려 온다.

자그마치 16레벨 차이. 압도적이다. 그 사실을 알려 주듯이 시스템창이 울렸다.



- 상태 이상 [위축]에 걸렸습니다!



‘누가 구해 주기 전에 세 번은 죽겠다.’

이런 내 반응을 눈치챘는지 이소군이 잔인한 미소를 지어 보였다.

“이제 상황 파악이 되나? 숨이 턱 막히고 손발이 저려 오지?”

이제는 관심법까지 쓰네. 하지만 싸움은 기세가 반이다.

나는 짐짓 표정을 가다듬고 대답했다.

“헛소리.”

“목소리가 떨리는군. 당연히 겁먹었겠지. 좋아, 내가 하는 질문에 성실하게 답변한다면 살살 해 주마.”

……솔직히 살짝 흔들릴 뻔했다.

“헛소리는 집어치워.”

“오, 주제에 무가의 자제라 이건가?”

이소군이 가소롭다는 듯이 웃었다.

“하나만 묻자. 무슨 자신감으로 비무를 받아들였나? 무공도 보잘것없고 겁쟁이로 소문난 네놈이. 그 이유가 듣고 싶다.”

“이유?”

아무리 생각해도 방법은 이것 하나뿐이었다. 전쟁이 일어나면 나는 항산검문의 문파 공적이 된다.

사냥? 레벨 업? 꿈도 못 꾼다. 태원진가라는 울타리를 벗어난 순간 냄새를 맡은 암살자들이 득달같이 달려들 거다.

‘목숨이라도 붙어 있으면 다음 기회가 있다.’

내게는 마법이 있다. 레벨 업이라는 회복 마법이.

마음이 조금 편안해졌다.

“너 정도면 해 볼 만한 것 같아서.”

“푸핫! 하룻강아지 같은 놈.”

가벼운 도발인데 역시 먹히지 않는다. 본인의 실력에 자신이 있는지 여유가 제법이다.

“이제 내가 질문할 차롄가?”

“대답해 준다는 말은 없었는데…… 유언인 셈 치고 들어 주마.”

“이번 일. 너희들이 조작한 거지?”

예상치 못한 질문이었는지 이소군의 얼굴이 어색하게 굳어졌다.

그 표정이 내게는 충분한 대답이었다.

‘맞네.’

혹시나 했는데, 역시다. 어쩐지 처음부터 끝까지 구린내가 진동을 하더라.

“어이구, 이 치졸한 새끼들. 차라리 선전포고를 하지.”

“……그 아가리를 찢어 주마.”

이소군이 거대한 대검을 들어 보이며 음산하게 중얼거렸다.

나도 미리 꺼내 둔 [예리한 창]을 곧추세웠다.

‘그래, 해 보자.’

나도 무공을 익혔다. 7년간 실전으로 다져진 감각도 있다.

F급 헌터 겸 이류 무림인. 투잡으로 갈고닦은 실력을 무시하지 마라!

“크아아아압!”

이소군은 상상 이상으로 민첩했다. 순식간에 거리를 좁히고 수직으로 내리꽂히는 대검을 창대로 막아 냈다.

카가가각.

“큭.”

그대로 양단되면 어쩌나 했는데, 예리한 창은 통짜 강철답게 튼튼했다. 그러나 대검에 실린 힘에 의해 두 발이 땅을 파고들기 시작했다.

“죽어라, 이 벌레 같은 놈!”

“흡!”

가까이서 마주하니 더욱 숨 막히는 기세다. 몬스터의 피어(Fear)가 이럴까.

“지금이라도 무릎을 꿇고 용서를 빌어라! 그럼 팔 하나 정도로 끝내 주지!”

- 막내야!

이소군의 어깨 너머로 벌떡 일어난 진위경이 보인다. 항산검문 놈들은 킬킬거리며 지켜보고, 태원진가 사람들은 차마 못 보겠다는 듯 고개를 돌리고 있다.

‘버텨야 해.’

적어도 진위경이 올 때까지만이라도!

“크아압!”

종횡무진. 사방에서 이소군의 대검이 연달아 작렬했다. 분명 철끼리 부딪치는데, 내 귀에는 대포 소리가 들린다.

쾅! 쾅! 쾅! 막았다.

“크아아!”

“하압!”

쾅! 쾅! 다시 막았다.

“크아아아!”

“하아아압!”

쾅! 또 막았다.

“크아아압…….”

“하아앗…….”

“……?”

“……?”

다음 순간, 이소군과 시선이 부딪쳤다.

그 얼떨떨하고 당황해하는 눈빛을 보는 순간, 녀석이 나와 똑같은 생각을 하고 있음을 알 수 있었다.

‘뭐여, 이게.’

이소군은 강하다. 대형 몬스터를 연상시키는 괴력에, 근육에 맞지 않게 민첩하며, 무지막지한 대검을 성냥개비처럼 휘두른다.

그뿐인가, 방귀 좀 뀐다는 항산검문의 자제다. 펼치는 무공도 제법 높은 수준일 것이다.

그런데…….

‘할 만한데?’

나는 지금도 끊임없이 휘둘러지는 대검을 하나하나 막아 내고 있었다. 20회가 넘어가는 공격. 그리고 방어.

보인다. 보여서 막을 수 있는 거다. 어느새 발목까지 파묻힌 다리를 슬며시 들어 보였다. 쑥 뽑힌다.

‘이거 혹시…….’

에이, 설마. 아니겠지.

쐐액-!

그 순간, 허리를 노리고 날아든 대검을 창간으로 흘렸다. 그리고 나도 모르게 순간적으로 텅 빈 이소군의 가슴을 걷어찼다.

빠악!

“컥!”

……응?

주르륵, 복부를 부여잡고 대여섯 발자국을 밀려난 이소군이 아무 일도 없었다는 듯 콧잔등을 슥 문질렀다.

“제법이군. 쓰레기답지 않게 한 수 재간은 있어.”

“…….”

“후후. 양보도 여기까지다.”

“……야.”

“다음 일격에 네놈의 머리통을…… 왜?”

나는 떨떠름한 얼굴로 손을 들어 녀석의 입을 가리켰다.

“너, 피 나.”

주륵. 한 박자 늦게 피 한 줄기가 이소군의 입가를 타고 흐른다. 저거 아무래도 혀 깨물었나 본데. 아프겠다.

“앗! 잉! 엑! 훅!”

뭔 개 같은 추임새를 넣으며 피를 닦아 내는 이소군에게, 내가 말했다.

“닦지 마. 놔둬.”

“……?”

“이따 한 번에 닦는 게 편해.”

왜냐하면 지금부터 나한테 존나 맞아야 하거든.



- 상태 이상, [위축]이 해제됩니다!
```

### Current accepted English

```markdown
# Chapter 14

“Come out with me, you bastard! I’ll make you pay for what you’ve done!”

The instant Lee Seogeun shouted those words, filled with fury—

Ding.

> **System**
>
> **Quest**
>
> **Duel**
>
> Your debauchery has finally caught up with you!
>
> A man must deal with his own mess. To protect the tiny scrap of honor you have left and to avoid the anger of the Mount Heng Sword Sect, only one option remains.
>
> **Type:** Sudden Quest  
> **Grade:** First Rate  
> **Restriction:** Jin Taekyung  
> **Mission:** Win the duel (Incomplete)
>
> **Reward:** Title: **Gambler**
>
> - A large amount of EXP
> - Fame 50
>
> **Failure:** Title: **Sex Fiend**
>
> - Injury
>
> Would you like to accept the **Duel** Quest?
>
> **Accept** / **Decline**

“……”

Seriously? I hadn’t even dated anyone since high school, and I had to be called a sex fiend?

I spent half my day on raids and collapsed asleep in my goshiwon every night. Now I had to clean up a mess I hadn’t even made in a game.

*At least give me a decent Quest.*

How was I supposed to fight a Level 30 like Lee Seogeun?

*This is insane. The Level gap is more than twice mine…*

This was a fight I couldn’t possibly take.

I declined the Quest. Or I was going to. But Lee Seogeun beat me to it.

“If you run away from this place… the Jin Family of Taiyuan will pay the appropriate price.”

Ding.

> **System**
>
> - Quest information has been updated.
>
> - If the Quest is declined, the **Mount Heng Sword Sect** will declare war on the **Jin Family of Taiyuan**. In addition, **Jin Taekyung** will be designated a public enemy of the sect.

*…I knew it.*

I had wondered why the System was giving me a choice for once.

As I let out a deep sigh, the assembly hall was boiling like a cauldron over charcoal.

“How dare you!”

“That young punk thinks he can say anything because he has his family’s backing!”

“Even if the Third Young Master did something lower than a dog, how dare he look down on our family!”

“……”

The first two were fine, but who the hell was that last guy?

As the atmosphere turned hostile, Jin Wikyung, the Lesser Family Head, stepped forward.

“Everyone, calm yourselves. And you, Young Hero, enough. Let us consider this a verbal slip and let it go this once.”

Seated in the place of honor, he issued the warning in a low voice. His presence was no joke. He really did have the bearing of the next Family Head of a prestigious house with deep roots.

Perhaps cowed by that aura, Lee Seogeun answered in a noticeably quieter voice.

“Understood. However…”

“However?”

“It was not a verbal slip. Do you think I came here as a private individual?”

At those words, Jin Wikyung’s expression hardened, and so did everyone else’s.

Right. Lee Seogeun was an envoy officially sent by the Mount Heng Sword Sect.

“My father—no, the Sect Leader—has entrusted me with all authority.”

“……Then what is it you want?”

“As I already said, I want a duel with the Third Young Master.”

*No. I don’t want that.*

Judging by how things were unfolding, those bastards from the Mount Heng Sword Sect had come here looking for a fight.

They intended to get as much as possible out of this incident, and even if that failed, they were going to wreck me, at least. Being targeted so blatantly sent a chill down my spine.

“There must be another way. Tell me what you truly want.”

“Withdraw from every commandery and county except Taiyuan. That should be an appropriate price for ruining my sister’s chances of marriage.”

The instant he finished speaking, shouts erupted throughout the assembly hall.

From the bits and pieces I could make out, he was basically saying they intended to strip us of everything but our underwear. Jin Wikyung’s answer was obvious.

“Impossible.”

“Then accept the duel—”

“That too, I must refuse.”

Jin Wikyung was a complete pushover when it came to his youngest brother. There was no way he would push me into a duel that was obviously dangerous.

At Jin Wikyung’s answer, Lee Seogeun smiled triumphantly.

“Then there is only one path left.”

War.

I wasn’t the only one who thought of that word. The assembly hall fell silent beneath the weight of it.

Amid that silence, I looked up at the empty air.

> **System**
>
> Would you like to accept the Quest?
>
> **Accept** / **Decline**
>
> - If the Quest is declined, the **Mount Heng Sword Sect** will declare war on the **Jin Family of Taiyuan**. In addition, **Jin Taekyung** will be designated a public enemy of the sect.

I read the System message, looked at the floor, looked at the ceiling, and then read it again.

*Fuck…*

There was no choice. Only one way remained.

“I’ll do it.”

Everyone reacted the same way this time. Wide eyes. Open mouths. Lee Seogeun, who had proposed the duel. Jin Wikyung, who had refused it. Every person in the assembly hall looked as if they doubted their own ears.

“W-wait. Taekyung?”

I left Jin Wikyung’s frantic attempt to stop me behind me and spoke to Lee Seogeun.

“Come out. Let’s have a go.”

The corners of Lee Seogeun’s mouth rose cruelly.

* * *

The winter wind was cold. I took a deep breath while looking up at the cloudy sky.

“Whoo.”

I faced Lee Seogeun on the Jin Family of Taiyuan’s main training ground. About fifty people sat some distance away, watching us.

The Jin Family people wore expressions that seemed to ask what the hell I had eaten, while the Mount Heng Sword Sect’s goons looked like they had come out for a day of entertainment. The only thing missing was popcorn.

Ah. Someone was sending me Sound Transmission, too.

- Little brother. Deep breaths. Deep breaths. In. Out. In. Out…

*I’m doing it, man.*

Jin Wikyung had a solemn expression, but he kept shifting his hips like a puppy that needed to poop. If Wipeng hadn’t been holding him down by the shoulder, he looked ready to charge into the training ground at any moment.

- Don’t worry. If it looks dangerous, this eldest brother of yours will jump in. What? If that bastard so much as lays a hand on our youngest brother, I’ll—fuck! Got it? Don’t get worked up. Take it slow and stay safe. You can do it, Jin Taekyung!

*……I get it, so calm down.*

He had radiated such overwhelming force in the assembly hall, yet Jin Wikyung was once again living up to my expectations.

*Still, he’s a hundred times better than having no one.*

At least someone would save me before I became a half-crippled wreck.

With Jin Wikyung and Wipeng, I had two life insurance policies. Excellent.

But the moment I looked at Lee Seogeun with that slightly lighter feeling, I withdrew my thoughts.

*What’s so excellent about this? Fuck.*

Now I understood why the Mount Heng Sword Sect’s people had been so confident.

Lee Seogeun suddenly stripped off his upper garments, and my breath caught at the muscles writhing like some kind of mollusk.

> **System**
>
> **Lv. 30 Lee Seogeun**

My hands and feet began to tingle at the sight of the blood-red Level window.

The sixteen-Level gap was overwhelming. As if to drive that fact home, the System rang.

Ding.

> **System**
>
> - You have been afflicted with the Status Effect **Intimidation**!

*I’ll die three times before anyone gets here to save me.*

Perhaps he noticed my reaction, because Lee Seogeun gave me a cruel smile.

“Do you understand the situation now? Your breath is caught, and your hands and feet are tingling, aren’t they?”

He could read minds now, too?

But momentum was half the fight.

I deliberately composed my expression before answering.

“Bullshit.”

“Your voice is trembling. Of course you’re afraid. Fine. If you answer my questions honestly, I’ll go easy on you.”

……To be honest, I almost wavered.

“Cut the bullshit.”

“Oh? Putting on the airs of a martial family’s son, are you?”

Lee Seogeun laughed as if I were ridiculous.

“Let me ask you one thing. What made you accept the duel? You, whose martial arts are pathetic and who is infamous for being a coward. I want to hear the reason.”

“The reason?”

No matter how much I thought about it, this was the only way.

If war broke out, I would become a public enemy of the Mount Heng Sword Sect.

Hunting? Leveling up? I could forget about it. The moment I left the fence of the Jin Family of Taiyuan, assassins who caught my scent would come running.

*As long as I stay alive, there will be another chance.*

I had magic. The recovery magic of leveling up.

My mind eased slightly.

“I thought someone like you might be manageable.”

“Pfft! You’re just a wet-behind-the-ears pup.”

It was a mild provocation, but it didn’t work. He was confident in his own abilities, and it showed in his relaxed manner.

“Is it my turn to ask questions now?”

“I never said I’d answer them… but I’ll indulge you as if they were your last words.”

“This incident. You fabricated it, didn’t you?”

Perhaps the question was unexpected, because Lee Seogeun’s expression stiffened awkwardly.

That expression was answer enough.

*There it is.*

I had wondered if that was the case, but sure enough. No wonder the whole thing had smelled rotten from beginning to end.

“You petty bastards. You should have just declared war.”

“……I’ll tear that mouth apart.”

Lee Seogeun lifted a massive greatsword and muttered ominously.

I raised the Sharp Spear I had drawn earlier.

*All right. Let’s do this.*

I had learned martial arts. I also had instincts honed by seven years of real combat.

An F-rank Hunter and a second-rate Murim martial artist. Don’t underestimate the skills I had honed working two jobs!

“Graaah!”

Lee Seogeun was more agile than I had imagined. He closed the distance in an instant, and I blocked the greatsword crashing down vertically with the shaft of my spear.

Kra-kra-kraang.

“Urgh.”

I had wondered if I would be split in two, but the Sharp Spear was sturdy as a solid piece of steel. However, the force behind the greatsword began driving both my feet into the ground.

“Die, you insect!”

“Hup!”

Up close, his aura was even more suffocating. Was this what a monster’s Fear felt like?

“Kneel and beg for forgiveness now! Then I’ll let you off with one arm!”

- Little brother!

Over Lee Seogeun’s shoulder, I saw Jin Wikyung spring to his feet. The Mount Heng Sword Sect’s people watched while snickering, and the Jin Family people turned their heads away as if they couldn’t bear to watch.

*I have to hold out.*

At least until Jin Wikyung got here!

“Graaah!”

Lee Seogeun’s greatsword struck from every direction in a blurring barrage. The weapons were clearly clashing, iron against iron, but all I could hear was the sound of cannons.

Boom! Boom! Boom! I blocked them.

“Graaah!”

“Hup!”

Boom! Boom! I blocked them again.

“Graaah!”

“Haaah!”

Boom! I blocked another.

“Graaah…”

“Haaah…”

“……?”

“……?”

The next moment, Lee Seogeun and I met each other’s eyes.

The moment I saw the bewilderment and confusion in his gaze, I knew he was thinking exactly what I was.

*What the hell is this?*

Lee Seogeun was strong. He possessed the brute strength of a giant monster, moved with surprising agility for someone with that much muscle, and swung his massive greatsword like a matchstick.

And that wasn’t all. He was a Young Master of the Mount Heng Sword Sect—a sect that could actually throw its weight around. The martial arts he used had to be quite advanced.

And yet…

*This is… doable?*

Even now, I was blocking each and every strike of the continuously swinging greatsword. More than twenty attacks. And more than twenty blocks.

I could see them. That was why I could block them.

I slowly lifted one of my legs, which had been buried in the ground up to the ankle. It came free with ease.

*Could this be…*

No way. Surely not.

Ssshwip!

At that moment, I redirected the greatsword flying toward my waist along the shaft of my spear. Then, without thinking, I kicked Lee Seogeun in his unguarded chest.

Whack!

“Urgh!”

……Huh?

Lee Seogeun slid back five or six steps while clutching his chest. Then he casually rubbed the bridge of his nose as if nothing had happened.

“You’re not bad. You’ve got a trick or two, despite being trash.”

“……”

“Heh. I won’t hold back anymore.”

“……Hey.”

“With my next strike, I’ll smash your head—what?”

With a queasy look, I raised a hand and pointed at his mouth.

“You’re bleeding.”

A beat later, a thin line of blood ran down from the corner of Lee Seogeun’s mouth. He had probably bitten his tongue. That had to hurt.

“Ah! Eeng! Eek! Hup!”

Lee Seogeun wiped away the blood while letting out some ridiculous yelps.

“Don’t wipe it. Leave it.”

“……?”

“It’ll be easier to wipe it all off at once later.”

Because from now on, I was going to beat the absolute shit out of him.

> **System**
>
> - The Status Effect **Intimidation** has been removed!
```
## Chapter 16

### Korean source

```text
＃16화



“후우, 드디어 끝났군.”

진위경이 붓을 내려놓으며 한 말이었다. 언제나처럼 문가 옆 의자에 앉아 있던 위팽이 고개를 들었다.

“점점 일 처리가 빨라지시는군요. 오늘도 고생하셨…….”

위팽이 말꼬리를 흐렸다. 아직 탁자 위에 산더미처럼 쌓인 서류를 발견했기 때문이었다.

그러고 보니 아직 정오 무렵밖에 되지 않았다. 저 정도 양의 업무를 해치울 수 있는 시간이 아니었다.

‘잘못 들었나?’

“좋아. 이 정도면…….”

이번엔 환청이 아니었다. 서류 더미 위로 불쑥 솟은 진위경의 얼굴이 그 증거였다.

“위팽, 이리 와 보게. 아주 중요한 일이야.”

너무나도 진지한 음성에 위팽은 살짝 걱정되었다.

무슨 큰일이라도 났나?

서류에서 심각한 비리가 발견됐다거나, 호시탐탐 기회를 엿보고 있는 장로원에서 큰 사건을 터트렸을 수도 있다.

‘큰일이군. 아직 항산검문의 일도 마무리되지 않았는데.’

그리고 잠시 후, 진위경이 내민 문제의 서류를 받아 든 위팽의 표정이 괴상하게 일그러졌다.

“……뭡니까, 이게?”

“보면 모르나? 그림이지.”

진위경의 말대로였다. 위팽이 생각한 문제의 서류는 온데간데없고, 건네받은 것은 그림이 그려진 화선지 한 장이었다.

“아니, 그 말이 아니잖습니까. 난데없이 이게 무슨…….”

진위경이 비밀스러운 미소를 지으며 말을 잘랐다.

“자세히 보게. 평범한 그림이 아니야.”

평범한 그림이 아니다? 순간 위팽의 눈이 번쩍 뜨였다.

머릿속에는 무림에 떠도는 온갖 전설들이 휙휙 스쳐 지나갔다.

한 폭의 그림을 보고 우화등선한 도사. 오래된 동굴의 벽화를 보고 깨달음을 얻은 절대 고수!

한참 동안 화선지를 누비던 위팽의 시선이 어느 순간, 벼락 맞은 것처럼 파르르 떨렸다.

“이, 이것은 설마……!”

“알아차렸군. 맞네.”

진위경이 후후후, 웃으며 말을 이었다.

“어제의 비무를 그려 봤네.”

“…….”

“쓰러진 이소군과 당당히 서 있는 태경이! 훗날 천하제일인이 될 젊은 영웅의 머리 위로 펼쳐진 하늘!”

“…….”

“일부러 밑에서 올려다보는 구도로 그렸는데, 자네 소감은 어떤가. 잘 그렸지. 응? 잘 그렸지?”

화선지를 붙든 위팽의 손이 바들바들 떨렸다. 마음 같아서는 구기고, 찢고, 그 위에 일주일 치 대소변을 갈긴 다음 잘 말린 후 불태우고 싶었지만.

“……잘 그리셨군요.”

위팽은 이성적인 사내였다. 절정의 경지에 오른 무인의 위대한 정신력을 발휘해 냈다.

물론 그에겐 정신 상태가 의심되는 주군을 질책할 만한 용기도 있었다.

“지금 밀린 일이 얼마나 많은데, 아침부터 지금까지 겨우 이 그림 한 장 그렸다는 게 말이 됩니까!”

“당연히 말이 안 되지.”

“그걸 아시는 분이…….”

“내가 세 시진 동안 하나만 붙잡고 있었을까 봐?”

“예?”

“당연히 하나 더 그렸지. 나중에 보여 주려고 했는데 역시 눈치가 빠르구먼.”

위팽은 부들부들 떨리는 손으로 진위경이 건네는 화선지를 받아들었다. 진위경은 싱글벙글 웃으며 그림 설명을 시작했다.

“비무 직후 상황을 그려봤네. 현재에 만족하지 않고 수련동으로 돌아가겠다고 선언하는 젊은 영웅! 그리고 그 모습을 우러러보는 사람들!”

“뭐, 그 부분에 대해서는 저도 상당 부분 동의합니다. 삼공자, 정말 많이 변했더군요.”

“그렇지? 나도 깜짝 놀랐지 뭔가.”

이소군과의 비무에서 승리한 진태경은 모두의 예상을 깨고 수련동으로 돌아갔다. 전날의 기억을 떠올리는 진위경의 눈동자가 몽롱해졌다.

“언제고 이런 날이 올 줄 알았지. 막내는 천응(天鷹)이야. 위팽, 자네에게는 들리지 않나? 태경이의 힘찬 날갯짓 소리가…….”

“날갯짓 소리는 모르겠고, 헛소리는 들립니다.”

위팽이 모든 걸 포기한 한숨과 함께 화선지를 내려놓은 순간이었다.

푸드득.

“헉.”

“거봐! 들리잖아!”

황급히 고개를 돌린 위팽의 시선이 창문을 향했다. 막 내려앉은 매 한 마리가 깃털을 고르고 있었다. 발목에는 작은 통 하나가 매달려 있었다.

“전서응(傳書鷹)입니다.”

새끼 때부터 고도의 훈련을 거쳐 투입된 연락용 매.

태원진가에도 두 마리밖에 없는 전서응은 극히 긴급한 일에만 날리게 되어 있었다.

“문제가 생겼군.”

진위경이 가라앉은 목소리로 중얼거렸다.

그리고 그것은 곧 현실로 나타났다.



* * *



“한엽이라고 합니다.”

“예?”

“만나 뵙게 되어 영광입니다.”

뜬금없는 자기소개였다. 물론 아는 얼굴이긴 했다.

수련동에 들어온 이후 가장 자주 본 사람이었으니까.

‘수련동 경비원이라고 해야 하나?’

경비원. 경비무사. 용어가 어찌 됐건 눈앞의 NPC는 수련동을 담당하는 태원진가의 무사였다. 내게 식사와 탕약을 가져다주는 것도 그의 임무 중 하나고.

‘그런데 갑자기 웬 통성명?’

지금까지 말 한마디 섞어 본 적 없는 NPC다. 내게 악감정은 없어 보였지만 그렇다고 특별히 호의적이지도 않았다.

“아, 예. 저도 반가워요.”

떨떠름한 대답에도 경비원, 아니 한엽의 얼굴이 환하게 밝아졌다. 뭐야, 갑자기 왜 이래?

“저도 어제 그 자리에 있었습니다.”

“그 자리? 아.”

비무를 말하는 거구나. 워낙 많은 사람이 몰렸으니 그중 한엽이 있었다고 해도 놀랄 만한 일은 아니다.

“처음부터 끝까지 지켜봤지요. 그 악랄한 항산검문의 이소군에게 맞서 싸우던 공자님의 영웅적인 모습을!”

악랄해? 영웅적인 모습?

‘그게 그렇게 되나?’

솔직히 현대인의 시선에서 바라보자면 그놈이 그놈이다.

아니, 오히려 이소군의 손을 들어 주고 싶을 정도다. 나도 한 사람의 오빠로서, 내 여동생 성격이 아무리 지랄맞아도 진태경 같은 놈이랑 연애질한다고 하면 눈 뒤집힐 것 같거든.

물론 항산검문의 태도나 제안은 말도 안 되는 거였다. 그래서 어쩔 수 없이 싸운 거고.

“보는 내내 가슴이 떨렸습니다. 저뿐만 아니라 그 자리에 있던 모든 사람이 같은 마음이었을 겁니다.”

한엽은 상기된 얼굴로 말을 이어 갔다. 이거 단단히 착각하고 있는 것 같은데, 어느 타이밍에서 멈춰야 할지 모르겠다.

“저도 한때 공자님을 오해했던 적이 있습니다. 하지만 이제는 가문의 모두가 진실을 알고 있습니다.”

이번에는 반문하지 않을 수 없었다.

“진실? 무슨 진실?”

“그건…….”

한엽이 잔뜩 숨죽인 목소리로 속삭였다. 귀에 닿은 뜨거운 숨결은 둘째치고, 그 내용에 소름이 돋는다.

그러니까, 그 내용인즉슨.

“내가 태원진가의 비밀 병기다?”

“네, 네!”

한엽이 맹렬하게 고개를 끄덕였다.

“사실 지금까지의 모습은 모두 위장이고, 어릴 때부터 뼈를 깎는 수련을 거치며 문무겸전에 덕과 의를 갖춘, 잠. 잠……”

이 말만은 도저히 못 하겠다. 오그라드는 손발을 보호하려는 나를 대신해 한엽이 나섰다.

“산서잠룡! 지금 가문 내에 모르는 사람이 없습니다. 공자님께서 아직 하늘에 오르지 않고 물에 몸을 숨긴 산서성의 잠룡이라는 사실 말입니다!”

아, 제발. 살려 줘. 큰 소리로 외치지도 말아 줘.

잠룡이라니. 가문에 모르는 사람이 없다니!

‘만약 내가 죽는다면 사인은 수치사다, 수치사.’

극심한 심적 고통에 몸부림치는 내게, 한엽이 반짝거리는 눈빛으로 물었다.

“사실이지요? 실례인 줄은 알지만, 저한테만 살짝…….”

안 되겠다. 누가 뿌렸는지 모를 이 말도 안 되고 오그라드는 헛소문을 진압하기로 다짐하고 입을 열었다.

“도대체 누가 그런 소문을 퍼트렸는지 모르겠지만…….”

그때였다.

띠링.



- 태원진가에 [잠룡]에 대한 소문이 퍼지고 있습니다.

- 소문에 의한 영향으로 명성이 10 오릅니다.

- 소문을 믿는 사람이 많아질수록, 명성이 상승합니다.



나는 근엄한 얼굴로 말을 이었다.

“전부 틀림없는 사실입니다.”

“역시! 저는 철석같이 믿고 있었습니다!”

환희에 찬 얼굴로 떠나는 한엽의 등을 바라보며, 나는 한줄기 눈물을 흘렸다.

‘시발…….’

아, 엄마 보고 싶다.



* * *



이소군과의 비무를 통해 여러 가지 사실을 깨달았다.

첫째.

‘나는 강하다.’

게임 초기, 튜토리얼 NPC로 나온 천력부를 일격에 쓰러트린 일이 있었다. 당시의 짐작이 지금은 확신으로 바뀌었다.

나는 강하다. 30레벨인 이소군을 어렵지 않게 쓰러트릴 정도로. 전투 경험의 차이도 영향이 있겠지만 기본적으로 능력치가 월등하다.

‘힘, 체력, 민첩. 모두 비슷하거나 내가 약간 앞섰지.’

스탯(Stat). 즉 능력치의 차이다. 이 게임 속에서 나는 유저고, 시스템을 이용한 성장을 거듭해 왔다.

무공 습득, 수련과 여러 가지 퀘스트를 통해 빠른 속도로 스탯을 올렸고 그 결과는 비무에서 드러났다.

그리고 두 번째.

‘공력이 부족해.’

공력 하나만큼은 이소군이 나보다 앞섰다. 아니, 월등했다.

뭘 먹고 컸는지 창대로 수십 번을 후려쳐도, 마운트 자세에서 일방적으로 때려도 놈은 견뎌 냈다. 반격까지 하고 마지막 순간에도 공력을 끌어 올렸다.

‘현재 내 공력은 십 년.’

이소군은 내 두 배인 이십 년은 될 거다. 여기서 세 번째 사실을 깨달았다.

‘공력의 차이가 무공의 단계를 가른다.’

나는 일류인 이소군을 꺾었다. 하지만 시스템이 표시하는 내 경지는 여전히 이류다.

나는 그 이유가 공력에 있다고 생각했다. 내게 부족한 단 하나의 능력치를 올렸을 때, 그때 비로소 내 경지도 오르지 않을까?

거기까지 정리를 마치고 나니 문득 드는 생각이 있었다.

‘이거 완전히 헌터 등급 나누기네.’

최초 각성자는 반드시 지정된 센터에서 보유 능력과 적성 직업, 마나량을 체크받아야 하는데, 신체 능력이 아무리 높아도 마나량이 부족하면 등급 심사에서 찬바람을 맞는다.

마법사들이 최하 D등급부터 시작하는 이유이기도 하다. 마법사들은 직업 특성상 기본 마나부터가 빵빵하니까.

‘그래도 게임이 현실보단 낫네.’

여긴 그나마 성장이라도 하지. 현실은 그런 거 없다. 나만 해도 7년 동안 뭐 빠지게 굴러서 E급들 사이에 낀 거지, F급 헌터인 건 변함없었으니까.

아무튼 이제 대략적인 스케치는 그려졌다.

‘스탯은 충분. 공력은 시간 날 때마다 진가심법 돌리고, 경험치 위주로 퀘스트를 받자.’

이 빌어먹을 게임에 갇힌 지 일주일이 넘었다. 현실에서 무슨 헛짓거리를 하는지는 몰라도 구조받기는 글렀다.

확실하게 준비해서 끝내야지.

“퀘스트창 오픈.”

띠링.



퀘스트



[로그아웃]

이제 당신은 이 험난한 무림을 헤쳐 나가야 합니다.

더욱더 강해지고, 유명해지십시오.

언젠가 다가올 그 날을 위해…….



등급 : 메인 퀘스트

제한 : 진태경

임무 : [일류] 경지 달성 (미완료)

         Lv.30 달성 (17 / 30)

         명성 500 달성 (70 / 500)

보상 : [로그아웃]





“아, 빡세다.”

나는 가부좌를 틀었다. 폐관 완료까지 이틀. 최대한 공력을 끌어모을 생각이었다.



- [잠룡]에 대한 소문의 영향으로 명성이 3 상승합니다.



틈틈이 울리는 명성 상승 메시지가 한줄기 위로가 되었다.



* * *



늦은 밤. 대회의장에 불이 켜졌다. 소가주인 진위경의 요청에 의해 비밀리에 이루어진 가로회의였다.

워낙 늦은 시각이었고, 갑작스러운 소집이라 뚱한 표정을 짓고 있는 중진들도 있었다.

“갑자기 소집이라니. 이게 무슨 일이랍니까?”

“그러니까. 이유도 안 알려 주고 이 늦은 시각에.”

“소가주가 아직 젊어서 그래. 절차와 예의를 몰라.”

“어제 일로 상당히 기세등등해졌나 봅니다. 하긴, 유일한 약점이 사라진 셈이니까요. 삼공자가 그 정도일 줄은 아무도 예상 못 했습니다.”

“장로원에서 김 좀 샜겠군. 삼공자 건으로 크게 한번 터트리려고 준비 중이었을 텐데.”

“허어, 지금이라도 대장로께서 나서서 가문을 바로 잡으셔야 할 터인데.”

“어허. 말조심…….”

그때, 모든 소리가 뚝 끊겼다. 회의실의 문이 양옆으로 열리고 진위경이 들어왔기 때문이었다.

중진들 사이에서는 평가가 분분한 소가주였지만 진위경의 등장과 동시에 내려앉은 침묵은 그에게 우두머리의 자질이 있음을 알려 주는 증거였다.

“늦은 밤에 소집에 응해 주신 모든 분께 감사드립니다.”

상석에 앉은 진위경은 첫 마디를 꺼냈지만 쉽사리 말을 이어 가지 못했다.

무슨 말을, 어디서부터 어떻게 꺼내야 한단 말인가. 머리가 지끈거렸다. 하지만 알려야 하는 일이었다.

“제가 오늘 이 자리를 마련한 이유는…….”

그 순간이었다.

“항산검문 때문이겠지.”

그건 기이한 목소리였다. 처음에는 늙은이의 그것이었고, 한편으로는 젊었으며 거칠거나 부드러웠다. 그리고 알 수 없는 울림이 있었다.

‘설마.’

진위경의 얼굴이 일그러졌다. 다시는 열릴 것 같지 않았던 회의장의 문이 열리고 있었다.

저벅. 저벅. 저벅.

미끄러지듯이 걸어 들어오는 다섯 명의 노인. 그리고 가장 앞에 선 노인을 확인한 모두가 황급히 일어나 고개를 숙였다.

“노야(老爺)를 뵙습니다!”

노야. 수년간 두문불출하던 대장로의 등장이었다.
```

### Current accepted English

```markdown
# Chapter 16

“Whew. Finally done.”

Jin Wikyung set down his brush as he spoke. Wipeng, who was sitting in a chair beside the door as always, raised his head.

“You’re getting faster at handling your work. You must be exhausted toda—”

Wipeng let his words trail off. He had just noticed the mountain of documents still piled on the table.

Come to think of it, it was only around noon. There was no way anyone could finish that much work in so little time.

*Did I hear him wrong?*

“Good. This should be enough…”

This time, it wasn’t a hallucination. Jin Wikyung’s face suddenly popped up above the pile of documents, proof enough of that.

“Wipeng, come here. This is very important.”

His voice was so serious that Wipeng grew slightly concerned.

*Did something major happen?*

Perhaps they had discovered some serious embezzlement in the documents. Or maybe the Elder Council, which had been constantly watching for an opportunity, had caused some kind of incident.

*This is bad. We haven’t even finished dealing with the Mount Heng Sword Sect yet.*

A moment later, Wipeng accepted the document in question from Jin Wikyung. His expression twisted into something bizarre.

“…What is this?”

“You can’t tell? It’s a drawing.”

The document Wipeng had feared was nowhere to be found. Instead, Jin Wikyung had handed him a single sheet of rice paper covered in drawings.

“No, that’s not what I meant. Why are you suddenly—”

Jin Wikyung cut him off with a secretive smile.

“Look closely. It isn’t an ordinary drawing.”

*It isn’t an ordinary drawing?*

Wipeng’s eyes lit up.

All kinds of legends circulating through Murim flashed through his mind.

A Daoist who achieved ascension after looking at a single painting. An absolute master who attained enlightenment after seeing a mural in an ancient cave!

Wipeng’s gaze roamed over the rice paper for a long while. Then, at some point, it began to tremble as if struck by lightning.

“T-this is, perhaps…!”

“You noticed. That’s right.”

Jin Wikyung continued with a chuckle.

“I tried drawing yesterday’s duel.”

“……”

“Lee Seogeun lying defeated, and Taekyung standing proudly! The sky spread above the head of the young hero who would one day become the greatest under heaven!”

“……”

“I deliberately chose a composition looking up from below. What do you think? It’s good, right? Isn’t it?”

Wipeng’s hands trembled around the rice paper. If he had been acting on impulse, he would have crumpled it, torn it apart, covered it with a week’s worth of piss and shit, dried it thoroughly, and burned it.

But—

“…It’s very well drawn.”

Wipeng was a rational man. He summoned the magnificent mental fortitude of a martial artist at the Peak realm.

Of course, he also had enough courage to reprimand a lord whose sanity was in serious doubt.

“How can you say that when there’s so much work piled up? Are you telling me that you spent the entire morning drawing this one picture?”

“Of course not.”

“Then you know how ridiculous this is—”

“Did you think I spent three hours focusing on only one thing?”

“What?”

“Of course I drew another one. I was going to show it to you later, but you really are quick to catch on.”

Wipeng accepted the next sheet of rice paper from Jin Wikyung with trembling hands. Grinning from ear to ear, Jin Wikyung began explaining the drawing.

“I tried to depict the scene immediately after the duel. The young hero declares that he won’t rest on his laurels and will return to the training hall! And the people gazing up at him in admiration!”

“I agree with a considerable part of that. The Third Young Master really has changed a great deal.”

“Right? I was surprised myself.”

After defeating Lee Seogeun in the duel, Jin Taekyung had defied everyone’s expectations and returned to the training hall. Jin Wikyung’s eyes grew hazy as he recalled the events of the previous day.

“I always knew a day like this would come. The youngest is a heavenly eagle. Wipeng, can’t you hear it? The powerful sound of Taekyung’s wings beating…”

“I don’t know about wings, but I can hear you spouting nonsense.”

Wipeng lowered the rice paper with a sigh of complete resignation.

Flap.

“Gasp.”

“See? You can hear it!”

Wipeng hurriedly turned toward the window. A hawk that had just landed was preening its feathers. A small container hung from its ankle.

“It’s a messenger hawk.”

These hawks were trained intensively from the time they were fledglings before being put to use as messengers.

The Jin Family of Taiyuan had only two messenger hawks, and they were sent out only for matters of extreme urgency.

“We have a problem.”

Jin Wikyung muttered in a subdued voice.

And that problem soon made itself known.

* * *

“My name is Han Yeop.”

“Pardon?”

“It’s an honor to meet you.”

It was a sudden introduction. Of course, I knew his face.

He was the person I had seen most often since entering the training hall.

*Should I call him the training hall’s guard?*

Guard. Martial-artist guard. Whatever the proper term was, the NPC in front of me was a Jin Family of Taiyuan martial artist assigned to the training hall. Bringing me meals and herbal decoctions was one of his duties, too.

*But why is he introducing himself all of a sudden?*

This was an NPC I had never exchanged a single word with. He didn’t seem to bear me any ill will, but he wasn’t especially friendly, either.

“Ah, yes. Nice to meet you, too.”

Despite my lukewarm response, the guard’s—or rather, Han Yeop’s—face brightened.

*What the hell? Why is he suddenly acting like this?*

“I was there yesterday, too.”

“There? Oh.”

He meant the duel. So many people had gathered that it wasn’t surprising for Han Yeop to have been among them.

“I watched from beginning to end. I saw the heroic way you fought against that vicious Lee Seogeun of the Mount Heng Sword Sect!”

*Vicious? Heroic?*

*That’s how it looked?*

Honestly, from a modern man’s perspective, one was as bad as the other.

No, I almost wanted to take Lee Seogeun’s side. As an older brother myself, even if my little sister’s personality were fucking awful, I’d lose my mind if she said she was dating a guy like Jin Taekyung.

Of course, the Mount Heng Sword Sect’s attitude and proposal had been absurd. That was why I had no choice but to fight.

“My heart trembled the entire time I watched. I’m sure everyone there felt the same way.”

Han Yeop continued with an excited expression. He seemed to be under a serious misunderstanding, and I had no idea when I was supposed to stop him.

“I used to misunderstand you, too, Young Master. But now everyone in the family knows the truth.”

This time, I couldn’t help asking.

“The truth? What truth?”

“That is…”

Han Yeop whispered in a voice so hushed that it was practically a secret. Leaving aside the hot breath against my ear, what he was saying gave me goose bumps.

In other words—

“I’m the Jin Family of Taiyuan’s secret weapon?”

“Yes, yes!”

Han Yeop nodded furiously.

“Your behavior until now was all an act, and ever since you were young, you’ve undergone bone-shattering training, becoming a man accomplished in both civil and martial arts, with virtue and righteousness, a sl—sl—”

I couldn’t bring myself to say that word. Han Yeop came to my rescue before my hands and feet could curl up from embarrassment.

“The Sleeping Dragon of Shanxi! Everyone in the family knows now! You’re Shanxi’s Sleeping Dragon, still hiding in the water instead of ascending to the heavens!”

*Oh, please. Somebody save me. And don’t shout it out loud.*

The Sleeping Dragon? There wasn’t a single person in the family who didn’t know?

*If I die, the cause of death will be death by embarrassment.*

As I writhed in agony, Han Yeop asked with shining eyes,

“It’s true, isn’t it? I know it’s rude, but just between us…?”

This wouldn’t do. I decided to suppress this ridiculous, cringe-inducing rumor whose origin I couldn’t even guess, then opened my mouth.

“I have no idea who started such an absurd rumor, but…”

That was when it happened.

Ding.

> **System**
>
> A rumor about the **Sleeping Dragon of Shanxi** is spreading throughout the **Jin Family of Taiyuan**.
>
> Fame has risen by 10 due to the influence of the rumor.
>
> The more people believe the rumor, the more Fame will rise.

I continued with a solemn expression.

“Every word of it is true.”

“I knew it! I believed it with all my heart!”

I watched Han Yeop walk away with a face full of rapture and shed a single tear.

*Fuck…*

*Ah, I miss my mom.*

* * *

I realized several things through my duel with Lee Seogeun.

First.

*I’m strong.*

Early in the game, I had knocked down the Heavenly Axe, who had appeared as the tutorial NPC, in a single hit. What had only been a suspicion back then had now become a certainty.

I was strong. Strong enough to defeat a Level 30 like Lee Seogeun without much trouble. The difference in combat experience had certainly played a part, but my basic stats were overwhelmingly superior.

*Strength, Stamina, Agility. They were all similar, or I had a slight edge.*

Stats. In other words, the difference in abilities. In this game, I was a player, and I had continued growing by using the System.

I had raised my stats rapidly by learning martial arts, training, and completing various Quests. The result had shown itself in the duel.

And second.

*I don’t have enough internal energy.*

Lee Seogeun had surpassed me in internal energy. No, he had been overwhelmingly ahead.

What had he been eating growing up? Even after I smashed him dozens of times with the spear shaft, and even when I beat him one-sidedly from a mount, he endured it. He even counterattacked and drew on more internal energy at the final moment.

*I currently have ten years of internal energy.*

Lee Seogeun probably had twenty years—twice as much as I did. That led me to a third realization.

*The difference in internal energy determines the stage of one’s martial arts.*

I had defeated Lee Seogeun, who was First Rate. But the realm displayed by the System still said I was Second Rate.

I thought the reason lay in internal energy. Once I raised the one ability I lacked, wouldn’t my realm finally rise as well?

After organizing my thoughts that far, another idea suddenly occurred to me.

*This is basically just Hunter rank classification.*

A newly awakened Hunter had to be tested at a designated center for their abilities, suitable profession, and mana capacity. No matter how high their physical abilities were, if their mana capacity was lacking, they received a cold reception during the rank evaluation.

That was also why mages started at D-rank at the lowest. Because of their profession, mages had plenty of basic mana from the start.

*Still, the game is better than reality.*

At least you could grow here. Reality had no such thing. Even I had only managed to get lumped in with the E-ranks after working my ass off for seven years. I was still an F-rank Hunter.

Anyway, I had now drawn a rough outline.

*My stats are sufficient. I’ll keep cycling the Jin Family’s Cultivation Technique whenever I have time, and focus on taking Quests that reward EXP.*

It had been over a week since I was trapped in this godforsaken game. I didn’t know what kind of nonsense was happening in the real world, but I could forget about being rescued.

I needed to prepare properly and finish this.

“Open Quest window.”

Ding.

> **System**
>
> **Quest**
>
> **Logout**
>
> You must now make your way through this harsh Murim.
>
> Become stronger and more famous.
>
> For the day that will come someday…
>
> **Grade:** Main Quest  
> **Restriction:** Jin Taekyung  
> **Mission:** Achieve the **First Rate** realm (Incomplete)
>
> &nbsp;&nbsp;&nbsp;&nbsp;Reach Level 30 (17 / 30)
>
> &nbsp;&nbsp;&nbsp;&nbsp;Reach Fame 500 (70 / 500)
>
> **Reward:** **Logout**

“Ugh. This is brutal.”

I sat cross-legged. Two days remained before my seclusion ended. I intended to gather as much internal energy as possible.

> **System**
>
> Fame has risen by 3 due to the influence of the Sleeping Dragon of Shanxi rumor.

The Fame-increase messages that chimed from time to time were a small source of comfort.

* * *

Late at night, the lights came on in the main assembly hall. At the request of the Lesser Family Head, a secret meeting of the family council was taking place.

It was very late, and the summons had been so sudden that several of the senior members wore sour expressions.

“A sudden summons? What is this about?”

“Exactly. They didn’t even tell us why they were calling us here at this hour.”

“That’s what happens when the Lesser Family Head is still young. He doesn’t know procedure or etiquette.”

“He must have grown rather full of himself after yesterday’s events. Though I suppose his only weakness has disappeared. No one expected the Third Young Master to be that capable.”

“The Elder Council must have been deflated. They were probably preparing to make a major move over the Third Young Master.”

“Hmph. Even now, the Head Elder should step forward and set the family straight.”

“Careful. Watch your tongue…”

At that moment, every sound abruptly stopped. The doors to the meeting room opened from both sides, and Jin Wikyung entered.

The senior members had varying opinions of their Lesser Family Head, but the silence that settled over the room the instant he appeared proved that he possessed the qualities of a leader.

“Thank you all for answering my summons at this late hour.”

Jin Wikyung took the seat of honor and spoke his opening words, but he found it difficult to continue.

*What should he say? Where should he begin, and how?*

His head throbbed. But this was something he had to tell them.

“The reason I called everyone here today is…”

That was when a strange voice interrupted him.

“It must be because of the Mount Heng Sword Sect.”

The voice was bizarre. At first, it sounded like an old man’s. And yet it was young as well—rough one moment, smooth the next. There was also an inexplicable resonance to it.

*Could it be…?*

Jin Wikyung’s face twisted.

The doors to the meeting room, which had seemed permanently sealed, began to part.

Step. Step. Step.

Five old men walked in as if they were gliding across the floor. The instant everyone recognized the old man at the front, they hurriedly stood and bowed their heads.

“We pay our respects, Head Elder!”

The Head Elder. He had appeared after keeping himself shut away from the world for years.
```
## Chapter 17

### Korean source

```text
＃17화



운기조식.

숨을 고르게 하여 기운을 다스리는 방법이다. 외부의 기를 내부로 받아들여 순환, 축적하는 행위.

지금 나는 진가심법이 적용된 운기조식을 하고 있었다.

‘이건 매번 신기하단 말이야.’

몰랐다. 내 몸에 이렇게 많은 혈이 존재하는지.

일전에 주워듣기로 인체의 혈도는 360여 개에 달한다고 했는데, 직접 심법을 운용하며 느낀 바로는 그 이상이다.

게임 속 가상 캐릭터라 그런가?

‘뭐 어때.’

단전에서 끌어 올린 10년의 공력이 신체를 순환한다. 공력이 자동차라면 혈도는 고속도로다. 나는 운전대에 앉아 그저 액셀을 밟으면 된다.

직선과 곡선이 반복되는 신체의 혈도를 달린 공력은 다시 단전으로 돌아간다.

‘그리고 여기서부터가 진짜 문제지.’

나는 길게 심호흡했다. 그리고 느꼈다.

내 의지에도 꿈쩍하지 않는, 거대한 바위처럼 단전을 차지하고 있는 또 다른 공력을.

‘넌 도대체 뭐냐.’

처음 운기조식을 했을 때부터 의문이었다. 터줏대감처럼 자리 잡고 있는 정체불명의 기운.

어디서, 어떻게 생겼고 왜 사용할 수 없는지는 모르겠지만 한 가지는 확실하다. 이 정체불명의 기운은, 내가 가진 10년의 공력보다도 더 큰 힘을 품고 있다.

‘지금까지는 건드릴 엄두가 안 났었지.’

정확히 말하면 건드릴 생각도 없었다. 며칠 전까지는 적당히 목숨 부지하면서 내심 구조를 기다리는 입장이었으니까.

하지만 이제는 다르다.

‘공력이 필요해.’

상황이 바뀌었다. 자력으로 탈출하려면 로그아웃 퀘스트 조건을 충족시켜야 하고, 충족 조건은 [일류]의 경지에 오르는 것.

그리고 일류가 되기 위해서는 이소군 정도의 공력이 필요하다는 것도 알았다.

‘내 것으로 만든다.’

나는 신중하게 공력을 움직이기 시작했다.

불안 반, 기대 반의 마음으로 정체불명의 기운을 향해 공력을 흘려보낸 순간, 깨달았다.

‘턱도 없네.’

공력은 엄연히 말해서 형체가 없는 기(氣), 그 자체다. 그런데 단순히 접촉하는 것만으로도 강한 거부와 반발이 느껴진다.

아니, 오히려 끌어당기기까지 한다. 이러다간 오히려 잡아먹힐 기세다.

‘야, 야, 야. 잠깐만!’

나는 황급히 공력을 회수했다. 끝까지 물고 늘어지는 정체불명의 기운을 뿌리쳤다. 동시에 시스템 알림이 울렸다.

띠링.



- [진가심법]을 수련했습니다. 공력이 소량 상승합니다.

- 반복 수련의 결과로 근맥과 근골이 1씩 상승합니다.



“아니, 뭐 저딴 게 다 있어?”

식겁한 마음을 진정시키며 상태창을 열었다.



상태창



[Lv.17 진태경]

직업 : 이류 무인

명성 : 70

칭호 : 4개 (칭호 효과 적용 중)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 가문의 수치 (모든 능력치 –5, 명성 –50)

- 초보 수련자 (수련 속도 +10%)

- 승부사 (일대일 승부 시 전투 관련 능력치 10% 향상)

근력 : 65체력 : 65

민첩 : 75 지력 : 10

매력 : 10 공력 : 10년

잔여 포인트 : 0





이제는 제법 높은 수치를 기록하고 있는 상태창이다.

비무 퀘스트를 통해 한꺼번에 3레벨이 올랐고, 30포인트를 근력, 체력, 민첩에 균등 분배한 결과였다.

하지만 상태창을 보는 내 마음은 쓰라렸다.

‘에휴, 공력만 제자리걸음이네.’

이 빌어먹을 시스템은 말만 공력이 상승했다고 하지, 정작 상태창에 표시되는 공력은 그대로다.

‘영단, 영약. 뭐 이런 거라도 하나 먹어야 되나?’

나는 진위경을 떠올렸다. 눈 딱 감고 형, 나 영단 하나만 주라, 하면 단칼에 거절하진 않을 것 같은데.

다음에 만나면 물어봐야겠다. 내 단전에 존재하는 정체불명의 기운에 관해서도.

쿠구궁.

그때 수련동의 입구가 열리더니 두 사람이 들어왔다.

“저어, 진 공자님?”

한엽이다. 그 뒤에는 처음 보는 무사가 서 있었다. 생긴 것만큼이나 무뚝뚝한 말투로 무사가 말했다.

“가로회의에 참석하시라는 소가주님의 명입니다.”

“소가주님이요?”

마침 잘됐네. 물어볼 거 있었는데.



* * *



“틀림없소. 몇 군데 부러지고 약간의 내상이 있었지만 그 정도로는 절대…….”

“확실해? 약왕당주의 이름을 걸고?”

“아, 맞다고. 내가 직접 진찰했다고!”

“맞으면 됐지. 왜 반말이야. 어? 같은 당주라고 대접해 주니까 내가 우스워 보여!”

“백호당주 당신이 먼저 반말했잖아!”

나는 멍하니 회의실 천장을 바라봤다. 사방에서 난무하는 고함과 욕설에 귀가 따끔거린다.

‘뭐여, 이게.’

내가 생각한 가로회의는 이런 게 아니었는데. 조용하고 질서정연한 분위기에서 서로의 의견을 주고받고 합의점을 찾는, 뭐 그런 거였는데…….

“당주라고 다 같은 당주인 줄 알아! 어디 의원 나부랭이가.”

“어린 노무 새끼가 말하는 본새 보소. 대침으로 회음혈을 쑤셔 버릴라.”

M자 탈모가 진행 중인 4, 50대 아저씨 두 명이 서로의 멱살을 잡고 흔드는 모습을 보니 골이 다 아파 온다.

문제는 이런 상황이 곳곳에서 벌어지고 있다는 사실이다.

그 때문인지는 몰라도 대부분의 사람들은 내가 문을 열고 들어와 자리에 앉은 것도 모르는 눈치였다.

- 왔느냐?

귀가 아니라 머리를 통해 들리는 듯한 목소리. 전음이다.

고개를 돌리자 상석의 진위경과 시선이 마주쳤다. 그는 피곤한 웃음을 지어 보였다.

- 난장판이지?

그러게. 이 난장판에 날 왜 불러 이 양반아.

내가 비난의 시선을 보내자 진위경이 찔리는 듯한 표정으로 전음을 날렸다.

- 나도 어쩔 수 없었다. 장로원에서 네 출석을 요구했거든. 어찌 되었건…… 태경이 네가 이 일에 연관된 것은 사실이니까.

장로원? 내가 이 일에 연관되어 있다고?

‘내가 무슨 일에 연관…… 아. 항산검문?’

나는 사람들의 고성방가 속에서 빠르게 퍼즐을 조합했다.

우선 최근에 나와 연관된 일이라면 항산검문밖에 없고, 그 일로 장로원인가 뭔가 하는 곳에서 나를 불러오게 했다. 이건데.

‘그러고 보니 못 보던 할아버지들이 있네.’

숫자는 네 명. 하나같이 검버섯이 가득한 얼굴에 머리가 하얗게 셌다.

그들은 탈모인들의 멱살잡이를 차가운 눈으로 바라보고 있었다. 누가 봐도 양로원, 아니 장로원이다.

- 그리고…… 대장로께서 와 계신다.

무심코 진위경 쪽으로 고개를 돌린 나는 흠칫했다.

‘뭐야. 저 노인네.’

언제부터 저기 있었지? 이제야 알아차렸지만 오늘의 상석은 두 자리였다. 진위경의 오른편에 앉아 나를 응시하고 있는 노인의 시선에 얼굴이 따끔거렸다.

‘저 노인이 대장로?’

백발, 백염, 백미. 오래된 그림에서 튀어나온 신선 같은 모습이다. 꼿꼿한 허리와 딱 벌어진 어깨, 팽팽한 피부는 나이가 무색해 보였다.

‘그런데 왜 저렇게 빤히 쳐다봐?’

눈에 힘을 빡 주고 대장로를 노려……보려다가 슬그머니 시선을 돌렸다. 붙으면 질 것 같아서가 아니라, 노인 공경이다. 노인 공경. 정말이다.

‘……쭈그리고 있자.’

그사이에도 진위경의 전음은 꾸준히 들려왔다.

- 기억을 잃어서 모르겠지만 대장로께서는 네 작은할아버님이자 가문의 최고 어르신이다. 언행에 각별히 신경 쓰거라.

아버지라는 양반 얼굴도 못 봤는데 작은할아버지란다.

어쩌면 이 자리에 사돈에 팔촌, 오촌 당숙까지 있을지도 모르겠다. 나는 진위경에게 살짝 고개를 끄덕여 보였다.

- 그리고…… 지금부터 벌어지는 일에 결코 당황해서는 안 된다. 차분하게 진실만을 고해라. 알겠느냐?

정확히 무슨 상황인지는 모르겠지만 진위경이 내 편이라는 사실은 확실했다. 이번에도 작게 고개를 끄덕이자 진위경이 희미한 미소를 지으며 일어났다.

“모두 정숙하십시오.”

공력이 담긴 목소리가 회의장을 휩쓸었다.

“이 자리는 태원진가의 가로회의이며, 우리는 중대한 사안을 위해 모였습니다. 때마침 증인이 도착했으니 심문을 시작하고자 합니다.”

어느새 조용해진 회의장의 중심. 사람들의 이목이 집중된 가운데 진위경이 입을 열었다.

“소가주이자 현 가주 대행의 권한으로 심문을 시작한다. 삼공자 진태경은 앞으로 나서라.”

나는 사람들의 시선을 느끼며 걸어 나왔다. 여기까진 충분히 예상했다. 괜히 나를 부르진 않았을 테니까.

하지만…….

“묻겠다. 네가 항산검문의 이소군을 독살했느냐?”

이건 예상 못 했다.



* * *



“아닙니다.”

간신히 입을 뗐다. 갑작스러운 말에 머릿속이 뒤죽박죽이다.

이소군이 죽었다고? 그것도 독에 중독돼서?

“진실을 고하라. 만일 거짓으로 밝혀진다면…….”

“이소군의 독살은 저와 아무런 연관이 없습니다.”

칼 같은 내 대답에 진위경은 안도 섞인 한숨을 내쉬었다.

- 지금처럼만 하면 된다.

심문은 빠르게 진행되었다. 그들은 묻고, 나는 답한다.

진위경을 시작으로 차례차례 질문이 쏟아졌다.

이소군과의 독살에 연관되어 있느냐는 질문이 절반이었고, 나는 계속해서 부정했다.

‘사실이니까.’

혹시나 해서 몰래 시스템창을 띄워 확인해 봤지만 확실했다. 내가 가진 무공, 능력들은 독과는 아무 관련이 없다. 그런 아이템도 없고.

그래서 망설임 없이 대답할 수 있었다.

“아닙니다.”

문제는 어느 순간부터 회의장 분위기가 묘하게 흘러가고 있다는 사실이었다.

“혹시 입증할 수 있는 증거가 있소?”

“증거요?”

백호당주라고 했나? 이름도 모르는 그는 썩 달갑지 않은 눈초리로 나를 응시했다.

“그렇소. 증거. 삼공자의 무죄를 입증할 만한 증거 말이오.”

이 새끼가 지금 뭐라는 거야.

“그걸 왜 내가 입증해야 하는데요?”

“뭐?”

“뭐는 반말이고.”

“이보시오. 삼공자!”

“날 의심하는 건 좋은데, 증거는 그쪽에서 찾아야 하는 거 아닌가? 예? 안 그래요?”

이 새끼들이 보자 보자 하니까 누굴 보자기로 보나. 나는 씨근덕거리며 자리에 앉는 백호당주를 노려보다가 문득 이상한 점을 발견했다.

‘허. 이것 봐라.’

흘끗 장로원 노인네들에게 시선을 보내는 백호당주의 모습.

공교로운 사실은 나를 추궁하고 압박하는 질문을 하는 이들 모두가 비슷한 모습을 보이고 있다는 것이다.

그 숫자가 참석 인원의 절반 가까이 되니 모른 척하기가 미안할 지경이었다.

‘파벌이라 이거지.’

진위경과 장로원.

한 집안의 웃어른과 그 손자뻘 되는 소가주의 힘 싸움이 이 순간에도 벌어지고 있었다니.

‘집안 꼴 잘 돌아간다.’

이제 남은 이들은 몇 되지 않았다. 문제는 그들의 면면이었다. 검버섯 핀 얼굴. 노회한 눈빛. 바로 장로원의 노인네들이었다.

그중 가장 늙고 뚱뚱한 노인이 입을 열었다.

“실속 없는 문답은 집어치우지. 이 늙은이가 말하고 싶은 건 단 하나일세. 이 문제는 어디서부터 비롯되었는가?”

장로원에 동조하는 중진들이 기다렸다는 듯이 대답했다.

“삼공자입니다.”

“문란한 언행으로 본가의 명성에 먹칠을 하고 다닌 것은 누구인가?”

“그 또한 삼공자입니다.”

같은 대답이 여기저기서 튀어나왔다.

“하면, 항산검문의 장중보옥을 건드려 작금의 사태에 이르게 한 것은 누구인가?”

“…….”

그냥 죽여라, 이 새끼들아.
```

### Current accepted English

```markdown
# Chapter 17

Circulating qi.

It was a method of regulating one’s energy by evening one’s breathing: drawing qi from outside the body, circulating it within, and accumulating it.

Right now, I was circulating qi using the Jin Family’s Cultivation Technique.

*This still feels incredible every time.*

I had never realized there were so many acupoints in my body.

I had once heard that the human body contained more than three hundred and sixty acupoints, but based on what I could feel while circulating qi through the cultivation technique, there were even more than that.

*Is it because I’m a virtual game character?*

*Whatever.*

The ten years of internal energy I drew up from my dantian circulated through my body. If internal energy was a car, then the meridians were a highway. All I had to do was sit behind the wheel and press the accelerator.

The internal energy raced along the straight and curving meridians throughout my body before returning to my dantian.

*And this is where the real problem starts.*

I took a long, deep breath. Then I felt it.

A second internal energy occupied my dantian like an enormous boulder that would not budge, no matter how hard I willed it to.

*What the hell are you?*

It had been a mystery ever since I first circulated qi. An unidentified energy that had taken root like it owned the place.

I didn’t know where it had come from, how it had been formed, or why I couldn’t use it, but one thing was certain. This unidentified energy contained more power than the ten years of internal energy I possessed.

*Until now, I hadn’t even dared touch it.*

To be more precise, I hadn’t intended to. Until a few days ago, I had been waiting for rescue while doing just enough to stay alive.

But things were different now.

*I need more internal energy.*

If I wanted to escape on my own, I had to fulfill the Logout Quest’s condition: reaching the First Rate realm.

I also knew that I needed internal energy on the level of Lee Seogeun’s to become First Rate.

*I’ll make it mine.*

I cautiously began moving my internal energy.

The moment I sent it toward the unidentified energy, half anxious and half expectant, I realized something.

*Not even close.*

Internal energy was, strictly speaking, qi itself—something without a physical form. And yet the instant the two energies touched, I felt powerful rejection and resistance.

No. It was even pulling me in. At this rate, it was going to eat me alive.

*Hey, hey, hey! Wait a second!*

I hurriedly withdrew my internal energy and shook off the unidentified energy, which clung to me until the very end. At the same time, a System notification rang out.

Ding.

> **System**
>
> - You have trained the **Jin Family’s Cultivation Technique**. Internal energy has risen slightly.
>
> - As a result of repeated training, **Sinews** and **Bones** have each increased by 1.

“What the hell was that?”

I calmed my pounding heart and opened my Status Window.

> **Status Window**
>
> **Lv. 17 Jin Taekyung**
>
> **Class:** Second Rate martial artist  
> **Fame:** 73  
> **Titles:** 4 (Title effects active)
>
> - **Scion of a Prestigious Family** — All stats +5, Fame +50
> - **Family’s Shame** — All stats –5, Fame –50
> - **Novice Trainee** — Training speed +10%
> - **Gambler** — Combat-related stats +10% in one-on-one matches
>
> **Strength:** 65  **Stamina:** 65  
> **Agility:** 75  **Intelligence:** 10  
> **Charm:** 10  **Internal Energy:** 10 years
>
> **Remaining Points:** 0

The numbers in my Status Window were fairly impressive by now.

I had gained three levels all at once through the Duel Quest, then distributed the thirty points equally among Strength, Stamina, and Agility.

But looking at the Status Window still left a bitter taste in my mouth.

*My internal energy is the only thing that hasn’t changed.*

This damn System kept saying that my internal energy had risen, but the amount displayed in the Status Window remained exactly the same.

*Do I need to take a spirit pill, an elixir, something like that?*

I thought of Jin Wikyung. If I screwed up my courage and said, *Big brother, just give me one spirit pill,* I didn’t think he would refuse me outright.

I’d ask him the next time I saw him. I would also ask about the unidentified energy inside my dantian.

Krrrummble.

At that moment, the entrance to the training hall opened, and two people stepped inside.

“Um, Young Master Jin?”

It was Han Yeop. Behind him stood a martial artist I had never seen before. The man spoke in a blunt tone that matched his appearance.

“The Lesser Family Head commands you to attend the family council.”

“The Lesser Family Head?”

That worked out perfectly. There was something I wanted to ask him about.

* * *

“It is beyond doubt. A few bones were broken, and there was some minor internal damage, but that level of injury could never—”

“Are you sure? You swear that on the name of the Medicine King Hall Leader?”

“I said it’s true! I examined him myself!”

“Then why are you talking down to me? I treated you with respect because you’re another Hall Leader, and now you think I’m a joke!”

“You were the one who started talking down to me, White Tiger Hall Leader!”

I stared blankly at the ceiling of the meeting room. The shouts and curses flying from every direction made my ears ring.

*What the hell is this?*

This wasn’t what I had imagined a family council would be like. I had pictured a quiet, orderly atmosphere where everyone exchanged opinions and searched for common ground…

“You think every Hall Leader is your equal? You’re nothing but some quack doctor!”

“Listen to this young bastard. I ought to shove a large needle straight into his perineal acupoint!”

Two men in their forties or fifties, both with receding, M-shaped hairlines, were grabbing each other by the collars and shaking one another. Just watching them made my head hurt.

The problem was that scenes like this were unfolding all over the room.

Maybe that was why most of the people there didn’t seem to notice me opening the door and taking my seat.

—You came?

The voice sounded as if it had entered through my head rather than my ears. It was Sound Transmission.

I turned my head and met Jin Wikyung’s gaze from the seat of honor. He gave me a tired smile.

—It’s a madhouse, isn’t it?

*You said it. Why did you call me to this madhouse, you old man?*

When I shot him a reproachful look, Jin Wikyung sent another message through Sound Transmission, his expression turning sheepish.

—I couldn’t help it. The Elder Council demanded your attendance. In any case… you are involved in this matter.

*The Elder Council? I’m involved in this matter?*

*What matter am I involved in…? Oh. The Mount Heng Sword Sect?*

I quickly pieced things together amid the shouting and cursing.

If there was one recent incident connected to me, it was the Mount Heng Sword Sect. And because of that incident, this thing called the Elder Council had summoned me.

That had to be it.

*Come to think of it, there are some old men here I’ve never seen before.*

There were four of them. Every one had a face covered in age spots and hair that had gone completely white.

They watched the men with the M-shaped hairlines grab each other by the collars with cold eyes. Anyone could see it was a nursing home—or rather, the Elder Council.

—And… the Head Elder is here.

I turned toward Jin Wikyung without thinking, then flinched.

*What the hell? Where did that old man come from?*

I had only just noticed that there were two seats of honor today. An old man was sitting to Jin Wikyung’s right, staring at me. His gaze made my face prickle.

*Is that old man the Head Elder?*

White hair, a white beard, and white eyebrows. He looked like an immortal who had stepped out of an old painting. His back was straight, his shoulders broad, and his skin taut enough to make his age seem meaningless.

*But why is he staring at me so intently?*

I gathered strength in my eyes and tried to glare back at the Head Elder…

Then I quietly looked away.

Not because I thought I would lose if we locked eyes. It was respect for my elders. Respect for my elders. Really.

*I’ll just keep my head down.*

Jin Wikyung’s Sound Transmission continued in the meantime.

—You may not know this because you lost your memory, but the Head Elder is your great-uncle and the most senior elder in the family. Be especially careful with your words and actions.

I hadn’t even seen my father’s face, and now I had a great-uncle.

*Maybe this place has relatives by marriage, distant cousins, and every kind of obscure uncle, too.*

I gave Jin Wikyung a small nod.

—And… you must not be flustered by what happens from this point onward. Calmly tell them only the truth. Do you understand?

I didn’t know exactly what was going on, but one thing was certain: Jin Wikyung was on my side.

I nodded again, and Jin Wikyung rose with a faint smile.

“Silence, everyone.”

His voice, infused with internal energy, swept across the meeting hall.

“This is a family council of the Jin Family of Taiyuan, and we have gathered to discuss a grave matter. Since our witness has arrived, I intend to begin the interrogation.”

The meeting hall had gone quiet without me noticing. With everyone’s attention focused on him, Jin Wikyung spoke.

“By the authority of the Lesser Family Head and current acting Family Head, I begin this interrogation. Third Young Master Jin Taekyung, step forward.”

I felt everyone’s eyes on me as I walked forward. I had expected this much. They hadn’t summoned me for no reason.

But…

“I ask you this. Did you poison Lee Seogeun of the Mount Heng Sword Sect?”

That was something I hadn’t expected.

* * *

“No.”

I barely managed to force the word out. My thoughts were a mess from the sudden question.

*Lee Seogeun was dead? Poisoned, at that?*

“Tell us the truth. If it turns out to be a lie…”

“I have nothing to do with Lee Seogeun’s poisoning.”

My answer was as sharp as a blade. Jin Wikyung let out a sigh of relief.

—Keep doing exactly this.

The interrogation proceeded quickly. They asked questions, and I answered them.

Starting with Jin Wikyung, they fired one question after another at me.

About half of the questions concerned whether I had been involved in poisoning Lee Seogeun, and I continued to deny it.

*Because it was true.*

Just in case, I secretly opened my System Window to check. I was certain of it. None of my martial arts or abilities had anything to do with poison. I didn’t have any such Items, either.

That was why I could answer without hesitation.

“No.”

The problem was that, at some point, the atmosphere in the meeting hall began to grow strange.

“Do you have any evidence to prove it?”

“Evidence?”

White Tiger Hall Leader, was it? The man whose name I didn’t even know stared at me with obvious displeasure.

“That is correct. Evidence. I mean evidence that would prove the Third Young Master’s innocence.”

*What the hell is this bastard talking about?*

“Why do I have to prove it?”

“What?”

“Don’t talk down to me.”

“Listen here, Third Young Master!”

“You’re free to suspect me, but shouldn’t you be the ones looking for evidence? Am I wrong?”

I’d been letting it slide, and these bastards thought they could wrap me up like a cloth?[^1]

Fuming, I glared at the White Tiger Hall Leader as he sat down, then noticed something strange.

*Well, well. Look at this.*

The White Tiger Hall Leader kept stealing glances at the old men of the Elder Council.

The strange thing was that everyone who had been pressing and interrogating me was doing something similar.

Nearly half the people in attendance were acting this way. It was getting difficult to pretend I hadn’t noticed.

*So this is a factional struggle.*

The Elder Council and Jin Wikyung.

Even now, a power struggle was taking place between the senior members of the family and the Lesser Family Head who was young enough to be their grandson.

*What a family.*

Only a few people remained to question me. The problem was who those people were.

Faces covered in age spots. Canny, experienced eyes.

The old men of the Elder Council.

The oldest and fattest of them opened his mouth.

“Enough of this empty questioning. There is only one thing this old man wishes to ask. Where did this matter begin?”

The senior members allied with the Elder Council answered as if they had been waiting for the question.

“The Third Young Master.”

“Who was it that dragged our family’s reputation through the mud with disorderly words and conduct?”

“The Third Young Master.”

The same answer came from several places around the room.

“Then who was it that provoked the Mount Heng Sword Sect’s prized treasure and brought us to this crisis?”

“…”

*Just kill me already, you bastards.*

[^1]: In Korean, the line puns on *boja* (“let’s see / wait and see”) and *bojagi*, a wrapping cloth.
```
## Chapter 18

### Korean source

```text
＃18화



분위기는 점점 최악으로 치닫기 시작했다.

“중요한 사실은 비무가 정당했다는 것입니다!”

“정당? 요즘은 독을 쓰는 걸 정당하다고 하나? 여기가 무슨 사천당문이야?”

“본인이 아니라고 하지 않소! 그리고 앞서 약왕당주가 말했듯이 이소군은 멀쩡했…….”

“삼공자야 당연히 아니라고 하겠지. 그리고 저 돌팔이 말을 어떻게 믿어?”

“돌팔이? 이 새끼가 진짜!”

그때 잔뜩 흥분한 목소리 하나가 귓가를 파고들었다.

“필요하다면 삼공자의 목을 바쳐서라도 전쟁을 막아야지!”

……뭐?

“그 무슨 망발이오!”

“내 말이 틀렸소? 이제 그만 인정합시다. 항산검문은 본가보다 강하오. 전쟁이 시작되면 수백이 죽거나 다칠 테고, 최악의 경우에는 멸문이오. 모든 원인인 삼공자를 넘기면 끝나는 일 아닌가!”

저게 말이냐, 방구냐. 모처럼 대단한 개소리를 들었더니 뒷골이 당기고 가슴이 답답해져 온다. 하지만 나보다 먼저 나선 사람이 있었다.

“방금 뭐라 했소?”

나직한 목소리지만 힘이 실려 있었다. 오히려 나직하기에 더 선명하게 들린다.

진위경이다. 그가 무표정한 얼굴로 사람들을 둘러봤다.

“누구. 목을. 바치자고?”

한 음절씩 뚝뚝 끊어지는 음성에 서리가 꼈다. 나도 순간적으로 몸이 으슬으슬할 정도의 분위기인데, 백호당주가 냉큼 입을 열었다.

“그거야 당연히 이 일의 주범인 삼공자…… 아.”

저 새끼는 모발도 없는데 눈치까지 없네. 백호당주는 말꼬리를 흐렸지만 이미 늦었다.

“그래서, 확인되지도 않은 일로 삼공자의 목을 항산검문에 갖다 바치시겠다? 그게 가문 당주의 입에서 나올 말이오?”

“아니, 내 말은 그런 뜻이 아니라…….”

백호당주가 진위경의 기세에 눌려 그의 눈을 피한다. 진위경이 가만히 백호당주를 노려보았다. 안 그러던 사람이 화가 나니 더 무섭다.

하얗게 질린 백호당주의 얼굴을 보니 10년 묵은 체증이 내려가는 기분이다. 자리에서 일어난 진위경은 냉엄한 얼굴로 좌중을 내려다봤다.

“이미 다들 알고 있소.”

진위경이 모두를 둘러보며 단호히 말했다.

“비무는 공정했고 이소군의 독살은 음모라는 것을. 그 사실을 알면서도 두려움 때문에 저들에게 굴복하자는 거요?”

장로원 측 인사들이 시선을 회피했다. 진위경의 냉소가 더욱 짙어졌다.

“누가 쥐여 줬는지는 모르겠지만, 항산검문은 명분이라는 칼자루를 쥐고 있소. 오늘일지, 내일일지. 아니면 이미 뽑혔는지도 모르지만 우리가 되돌리기에는 늦었소. 방법은 단 하나. 맞서 싸우는 것뿐이오.”

“…….”

“살고 싶소? 가문을 지키고 싶소? 진정 그렇다면 무사들을 준비시키고 전쟁을 준비하시오. 아니면 나와 내 아우의 목을 베어 저들에게 바치시든가. 그저 부귀영화만을 바란다면 그것도 나쁘지 않은 방법이겠지.”

숨 막히는 정적이 대회의장을 점령했다.

다음 순간, 한 사람이 입을 열지 않았다면 몇 시간이고 그 정적에 짓눌려 있었을지도 몰랐다.

“훌륭하다.”

지금까지 말없이 사태를 관망하던 한 사람.

대장로였다.



* * *



대장로.

요주의 인물이다. 가문의 최고 웃어른이자 장로원의 수장.

나는 앞서 들었던 진위경의 전음을 떠올렸다.

‘조심하라고 했었지.’

진위경이라는 NPC는 내게 있어 가장 큰 아군이자 조언자다.

나는 그 말을 허투루 듣지 않았고, 틈틈이 대장로를 주시했다.

그리고 한 가지 결론을 내렸다.

‘시바, 도저히 모르겠다.’

이 거지 같은 게임을 시작한 뒤 한 번이라도 마주친 NPC들의 숫자를 세라고 하면 족히 백은 넘어간다.

그들에겐 각자의 표정과 성격이 있었다. 기루에서 만난 하인은 삶에 찌든 영업용 미소를 지었고, 나를 데려다준 마부는 허당끼가 있었으며 가문에서 만난 중진들은 의외로 단순하고 과격한 면모가 있다.

하지만 대장로는…….

‘표정을 못 읽겠어.’

그는 그저 묘한 웃음을 지으며 이 모든 것을 지켜볼 뿐이다.

심문이 시작되었을 때도, 중진들이 각자의 파벌에서 고함을 내지를 때도, 그리고 지금 이 순간에도.

짝. 짝. 짝.

대장로의 힘찬 박수 소리가 울려 퍼졌다.

“어리게만 생각했건만, 어느새 소가주가 이리 당당한 무인이 되었구려. 훌륭하오. 그래야 본가의 소가주라 할 수 있지.”

“못난 꼴을 보여 드려 죄송할 따름입니다.”

“과한 겸손은 오만으로 비치는 법. 소가주는 사과할 것 없소.”

대장로의 칭찬에도 진위경은 여전히 굳은 얼굴이었다.

“이 늙은이도 한마디 보탤까 하는데, 소가주의 생각은 어떠신가?”

“새겨듣겠습니다.”

천천히 자리에서 일어난 대장로에게 수십 쌍의 시선이 꽂혔다.

가문의 최고 웃어른이다. 가문 내 권위나 입지로 치자면 진위경을 뛰어넘을지도 모른다.

가장 큰 문제는 그가 반대 세력인 장로원의 수장이라는 거고.

‘시발, 좆 됐네.’

최악의 상황을 대비해 슬금슬금 문 쪽으로 몸을 돌리는 내 귓가에, 대장로의 첫 마디가 파고들었다.

“썩어 빠졌구나.”

응?

고개를 홱 돌렸다. 대장로는 여전히 특유의 묘한 웃음을 짓고 있었다. 내가 잘못 들었나?

하지만 아니었다.

“하물며 짐승들조차도, 제 굴에 적이 들어오면 함께 힘을 합쳐 싸우는 법이다. 그런데 가문의 중진씩이나 되는 것들이 직계의 목을 바치고 전쟁을 막겠다는 걸 대책이라고 내어놓고 있구나. 허허. 이런 놈들이 본가의 가로회의에 앉아 있단 말이지.”

“노, 노야. 오해십니다. 그것은 그저…….”

“백호당주.”

서늘한 대장로의 부름에 백호당주가 바짝 긴장했다.

“내 외유가 너무 길었던 것인가? 아니면 가주가 자리를 비웠기 때문인가?”

“노, 노야.”

표정만 보면 밥 먹었냐 물어보는 헬스장 몸짱 할아버진데, 말하는 내용은 살벌하기 그지없다.

‘뭐야, 이거.’

어떻게 돌아가는 거야? 왜 우리 편을 들어?

눈동자를 팽팽 돌려 봤지만, 사람들의 반응도 나와 다르지 않았다. 양측 모두 당황한 기색이 역력했다.

“어찌 생각하시오, 소가주?”

“무엇을 말씀하시는 것인지.”

“전쟁이 기정사실화되었다면 내부를 단속하는 것이 우선이겠지. 그러니 역도나 다름없는 저들의 목을 베는 게 우선일 텐데?”

얼어붙은 공기 속, 진위경은 한동안 물끄러미 대장로를 바라보다가 한숨처럼 대답을 토해 냈다.

“그럴 수는 없습니다.”

휴우. 백호당주가 안도의 한숨을 내쉬었다. 아까 내 목을 갖다 바치느니 마니 했던 걸 생각하면 살짝 아쉽다.

……저 자식만 죽이자고 말해 볼까.

“저들은 가문의 직계를 모함하는 것으로도 모자라 적들에게 넘기자고 주장했는데, 너무 무른 처사라고 생각하지 않나?”

“오랜 세월 본가에 충성한 이들입니다. 흥분해서 나온 실언이라고 생각하겠습니다.”

진위경의 대답에 대장로가 껄껄 웃었다.

“실언, 실언이라. 그래. 소가주의 그릇은 내 생각 이상으로 크구려. 과연 소가주요. 그렇다면 이들에 대한 책임은 묻지 않기로 하지. 늙은이들의 실언을 담대하게 용서해 준 소가주께 감사를 표하는 바요.”

이어 대장로가 고개를 숙이자 사람들이 다급하게 손사래를 치며 마주 허리를 굽혔다.

“아이고, 노야. 아닙니다. 저희의 생각이 짧았습니다.”

“제발 이러지 마십시오.”

“이러시면 저희가 더욱 부끄러워집니다. 부디…….”

“노야……!”

살려 준 건 진위경인데 난리가 났다. 아주 생쇼를 해라, 생쇼를.

내심 혀를 차며 그 모습을 지켜보던 순간이었다.

‘아니, 잠깐만. 쇼?’

정체 모를 위화감이 온몸을 감싼다. 나는 황급히 대장로 주위에 모여든 이들을 살폈다. 그리고 발견했다.

앞서 나를 몰아세웠던 장로원. 그들의 입가에 스치는 웃음을.

‘설마…….’

계획된 거라고? 이 모든 게 다?

도대체 무슨 의도로, 뭘 위해서? 수많은 물음이 떠올랐다 사라진다. 머릿속이 엉망진창이었다.

‘진위경은 뭔가 알고 있을까?’

고개를 돌려 찾을 필요도 없었다. 대장로가 진위경의 손을 번쩍 들고 외치고 있었으니까.

“가주가 자리를 비운 지금, 소가주가 가주나 다름없소. 이 일에 대해서 나는 소가주를 지지하겠소. 그를 중심으로 뭉친다면 저들이 아무리 대단하다 해도 감히 진가를 넘볼 수 없을 것이오!”

달아오른 분위기, 사람들의 연호와 함성.

이걸 어디서 봤더라, 왠지 모르게 익숙한 느낌이다.

그리고.

“감사합니다.”

파르르 떨리는 진위경의 입꼬리와 대장로의 묘한 웃음을 보는 순간, 나는 익숙한 느낌의 정체를 깨달았다.

‘선거 유세.’

대장로의 모습과 TV 속 정치인이 겹쳐 보였다.



* * *



상당히 찜찜하긴 했지만, 일단 대장로가 진위경의 손을 들어 주자 회의는 일사천리로 진행되었다.

장로원 측에서 끈질기게 물고 늘어졌던 비무 관련 이야기는 쏙 들어가고, 전쟁을 전제로 한 회의 내용이 주를 이뤘다.

“현재 가용 인원은 어떻게 되나?”

“외부 파견 중인 무사들까지 불러들인다면…… 이백 남짓입니다.”

이백 명이나 된다고? 나는 의외로 많은 숫자에 혀를 내둘렀지만 이어지는 대화에 입을 다물었다.

“일류 이상의 정예로 엄선한다면?”

“스물이 채 안 됩니다. 물론 이 자리에 계신 분들을 포함하면 다르겠지만 말입니다.”

중진들을 포함하면 일류 고수의 숫자는 3, 40명 남짓.

이곳 사정은 잘 모르지만, 이 정도면 양호한 수준인 것 같다.

역시 뿌리 깊은 명문세가. 200년을 이어 온 저력이 어디 가는 게 아니다.

“항산검문 측은?”

“우선 확인된 무사들만 최소 삼백입니다.”

삼백. 그것도 최소로 잡았으니 백 명 이상의 차이다.

하지만 괜찮다. 원래 싸움은 머릿수로 하는 게…….

“그리고 일류는 오십 이상입니다.”

이 전쟁, 어렵다. 그래도 진위경과 위팽 같은 고수들이 있다면 해 볼 만한 싸움이다. 그들은 기감으로도 읽지 못하는 고레벨의 NPC들이니까. 아마 대장로도 그 범주에 포함되는 존재일 것이다.

“본가의 절정 고수는 소가주와 노야, 위 대협까지 총 셋입니다. 그리고 항산검문의 절정 고수는 다섯이지요.”

……거지 같아서 못 해 먹겠네. 진짜.

‘뭐? 뿌리 깊은 명문세가? 200년 역사?’

이 새끼들은 200년 동안 뭘 한 거야. 듣자 하니 항산검문의 역사가 30년도 안 된다는데, 전력 면에서 밀리다 못해 압살이다. 압살.

‘작년에 흑사병이라도 돌았나.’

흑사병이 돌았건 말건 당장 내가 돌아 버릴 것 같다. 나는 어느새 노래진 회의실 천장을 바라보다 문득 다짐했다.

‘튀어야겠다.’

새벽 네 시 정도면 적당하겠지. 다들 잠들어 있을 때 몰래 담을 넘어서 멀리 도망가는 거다.

지금의 나라면 천력부 정도의 수준은 대여섯이 덤벼도 손쉽게 해치울 수 있다.

보이는 산마다 싹 뒤지면서 경험치와 명성을…….

“항산, 항산검문에서 전서구가 도착했습니다!”

황급히 들이닥친 무사의 외침이었다. 누군가 돌돌 말린 종이를 받아 펼치자 피로 쓴 듯 붉은 글자가 눈에 들어왔다.

굳이 시스템이 번역해 주지 않아도 알아볼 수 있는 글자였다.



不俱戴天



‘불구대천.’

하늘 아래 같이 살 수 없는 원수.

진위경이 무거운 얼굴로 입을 열었다.

“현 시간부로 본가는 전시 상황에 돌입한다. 내 인(印) 없이는 지위 고하를 막론하고 세가 외 출입을 금하며, 삼엄한 경계 태세를 유지해야 할 것이다. 개미 새끼 한 마리도 들이지 말라. 알겠는가!”

“옛!”

“…….”

넋이 반쯤 나간 내 귓가로, 시스템 알림이 울렸다.

띠링.



- [항산검문]이 [태원진가]에 선전포고했습니다.

- [전쟁] 관계가 양측 진영에 성립되었습니다.

- [항산검문]이 당신을 문파 공적으로 지목합니다.

- 도망칠 경우 심각한 불이익을 받게 될 것입니다.

- [메인 퀘스트 - 전쟁]이 생성되었습니다.



……허허. 허허허허.
```

### Current accepted English

```markdown
# Chapter 18

The atmosphere grew worse by the second.

“The important fact is that the duel was fair!”

“Fair? Since when is using poison considered fair? Is this the Sichuan Tang Clan or something?”

“The man himself said he didn’t do it! And as the Medicine King Hall Leader said earlier, Lee Seogeun was perfectly fine—”

“Of course the Third Young Master would say he didn’t. And how can you believe that quack?”

“A quack? You little bastard!”

Then one particularly agitated voice pierced my ears.

“If necessary, we should stop the war even if it means offering up the Third Young Master’s head!”

…What?

“What kind of outrageous nonsense is that?”

“Am I wrong? Let’s just admit it. The Mount Heng Sword Sect is stronger than our family. If war begins, hundreds will die or be injured, and in the worst case, our family could be destroyed. If we hand over the Third Young Master, who caused all this, won’t everything be over?”

What kind of bullshit was that? I hadn’t heard such spectacular nonsense in a long time. The back of my neck tightened, and my chest grew tight.

But someone else stepped forward before I could.

“What did you just say?”

His voice was quiet, but it carried power. In fact, its quietness made it sound even clearer.

It was Jin Wikyung. He looked around the room with an expressionless face.

“Whose. Head. Did you say we’d offer?”

Each syllable fell separately, frost coating his voice. The atmosphere was so chilling that even I shivered.

The White Tiger Hall Leader spoke up at once.

“Obviously, the Third Young Master, the main culprit behind this—ah.”

That bastard was bald, and he couldn’t read the room either. The White Tiger Hall Leader let his words trail off, but it was already too late.

“So you intend to hand the Third Young Master’s head over to the Mount Heng Sword Sect over something that has not even been confirmed? Is that something a hall leader of this family should be saying?”

“No, that’s not what I meant…”

The White Tiger Hall Leader was overwhelmed by Jin Wikyung’s aura and avoided his eyes. Jin Wikyung silently glared at him.

He wasn’t normally like this, which made him even scarier now that he was angry.

Looking at the White Tiger Hall Leader’s pale face made me feel as if ten years of indigestion had finally been cured. Jin Wikyung rose from his seat and looked down at everyone with a cold expression.

“You all already know.”

He looked around the room and spoke firmly.

“That the duel was fair, and Lee Seogeun’s poisoning was a conspiracy. Knowing that, are you suggesting we submit to them out of fear?”

The members of the Elder Council faction avoided his gaze. Jin Wikyung’s sneer grew deeper.

“I don’t know who placed it in their hands, but the Mount Heng Sword Sect holds the hilt of a sword called justification. Whether it happens today or tomorrow—or whether the sword has already been drawn—we are already too late to reverse it. There is only one way forward. We fight.”

“……”

“Do you want to live? Do you want to protect the family? If you truly do, prepare the martial artists and prepare for war. Or cut off my head and my younger brother’s, then offer them to the Mount Heng Sword Sect. If all you want is wealth and glory, I suppose that isn’t a bad option, either.”

A suffocating silence took over the main assembly hall.

If one person hadn’t opened his mouth the next moment, we might have been crushed beneath that silence for hours.

“Excellent.”

It was the man who had watched the situation without saying a word until now.

The Head Elder.

* * *

The Head Elder.

A person to watch out for. The family’s highest-ranking elder and the head of the Elder Council.

I remembered the Sound Transmission Jin Wikyung had sent me earlier.

*He told me to be careful.*

Jin Wikyung was the greatest ally and adviser I had among the NPCs.

I hadn’t taken his warning lightly. Whenever I had the chance, I kept an eye on the Head Elder.

And I reached one conclusion.

*Fuck, I can’t figure him out at all.*

If someone asked me to count the number of NPCs I had encountered even once since starting this godforsaken game, the number would easily be over a hundred.

Each of them had their own expressions and personalities. The servant I met at the pleasure house wore a business smile worn down by life. The coachman who brought me here had a goofy side. The senior members I met in the family were surprisingly simple-minded and aggressive.

But the Head Elder…

*I can’t read his expression.*

He merely watched everything with that strange smile of his.

When the interrogation began. When the senior members of each faction shouted at one another. And even now.

Clap. Clap. Clap.

The Head Elder’s vigorous applause rang through the hall.

“I thought of you as nothing more than a youngster, but before I knew it, the Lesser Family Head had become such a dignified martial artist. Excellent. That is how the Lesser Family Head of our family should be.”

“I can only apologize for showing you such an unseemly side.”

“Excessive humility can look like arrogance. You have nothing to apologize for.”

Despite the Head Elder’s praise, Jin Wikyung’s face remained stiff.

“May this old man add a word? What do you think, Lesser Family Head?”

“I will take it to heart.”

The Head Elder slowly rose from his seat, and dozens of pairs of eyes locked onto him.

He was the family’s highest-ranking elder. In terms of authority and standing within the family, he might even surpass Jin Wikyung.

The biggest problem was that he was the head of the opposing faction—the Elder Council.

*Fuck, I’m screwed.*

Preparing for the worst, I started edging toward the door when the Head Elder’s first words reached my ears.

“You’re rotten to the core.”

Huh?

I whipped my head around. The Head Elder still wore that same strange smile.

*Did I hear him wrong?*

But I hadn’t.

“Even beasts join forces and fight when an enemy enters their den. And yet men who are supposedly senior members of this family offer up the head of a direct-line member as a solution to stop a war. Heh. So men like this sit in our family council.”

“N-no, Head Elder. You’ve misunderstood. It was merely…”

“White Tiger Hall Leader.”

At the Head Elder’s chilly call, the White Tiger Hall Leader stiffened.

“Have I been away for too long? Or is it because the Family Head is absent?”

“N-no, Head Elder.”

Going by the Head Elder’s expression, he looked like a muscular old man at a gym asking whether you’d eaten. But the content of his words was vicious beyond belief.

*What is this?*

What was going on? Why was he taking our side?

I looked around frantically, but everyone else was just as confused as I was. Both factions were visibly flustered.

“What do you think, Lesser Family Head?”

“I’m not sure what you mean.”

“If war has become inevitable, then our first priority should be to discipline those within our ranks. Wouldn’t it be best to cut off the heads of those men who are little different from rebels?”

In the frozen air, Jin Wikyung stared at the Head Elder for a long moment before answering in something like a sigh.

“That cannot be done.”

Whew. The White Tiger Hall Leader let out a relieved sigh.

Considering how he had just been talking about offering up my head, I was a little disappointed.

*Should I suggest that we kill just him?*

“Those men not only framed a direct-line member of the family, but even argued we should hand him over to the enemy. Don’t you think that is too lenient a response?”

“They have served our family loyally for many years. I will consider it an ill-considered remark made in the heat of the moment.”

The Head Elder laughed heartily.

“An ill-considered remark. An ill-considered remark, indeed. Yes. The Lesser Family Head’s capacity is greater than I expected. Truly worthy of being the Lesser Family Head. In that case, I will not hold them responsible. I offer my thanks to the Lesser Family Head for magnanimously forgiving the thoughtless words of old men.”

When the Head Elder bowed, the others hurriedly waved their hands and bent at the waist in return.

“Oh, Head Elder, no. Our thoughts were shallow.”

“Please, don’t do this.”

“You’re only making us more ashamed. Please…”

“Head Elder!”

Jin Wikyung was the one who had spared them, yet they were making a huge scene.

Go on, put on a show. A real show.

I was watching the spectacle with a private click of my tongue when—

*Wait. A show?*

An indescribable sense of wrongness settled over me. I hurriedly examined the people gathered around the Head Elder.

And then I noticed it.

The smiles flickering around the lips of the Elder Council members who had pressured me earlier.

*No way…*

Was this all planned? Every bit of it?

Why? For what purpose? Countless questions rose and vanished. My thoughts were a complete mess.

*Does Jin Wikyung know something?*

I didn’t even need to turn around to look for him. The Head Elder was already holding Jin Wikyung’s hand high in the air and shouting.

“With the Family Head absent, the Lesser Family Head is effectively the Family Head. I support the Lesser Family Head in this matter. If we unite around him, then no matter how formidable they are, they will not dare challenge the Jin Family!”

The heated atmosphere. The people’s cheers and shouts.

*Where had I seen this before?*

It felt strangely familiar.

And then—

“Thank you.”

The moment I saw the corners of Jin Wikyung’s mouth quiver and the Head Elder’s strange smile, I realized where that familiar feeling came from.

*An election campaign.*

The Head Elder’s figure overlapped with the politicians I had seen on television.

* * *

It was deeply unsettling, but once the Head Elder raised Jin Wikyung’s hand, the meeting proceeded swiftly.

The discussion about the duel, which the Elder Council faction had stubbornly kept dragging out, disappeared entirely. Instead, the meeting focused on preparing for war.

“How many men are currently available?”

“If we call back the martial artists stationed outside, roughly two hundred.”

As many as two hundred?

I was astonished by the unexpectedly large number, but the next question made me shut my mouth.

“If we select only elites of First Rate or higher?”

“Fewer than twenty. Of course, that number would be different if we included everyone present.”

Including the senior members, there were around thirty or forty First Rate masters.

I didn’t know much about the circumstances here, but that seemed like a decent number.

As expected of a prestigious family with deep roots. Two hundred years of accumulated strength didn’t simply vanish.

“What about the Mount Heng Sword Sect?”

“At least three hundred martial artists have been confirmed so far.”

Three hundred. And that was the minimum, meaning there was a difference of more than a hundred men.

But it was fine. Fights came down to numbers anyway—

“And they have more than fifty First Rate martial artists.”

This war was going to be difficult.

Still, with masters like Jin Wikyung and Wipeng, it was a fight worth attempting. They were high-level NPCs beyond what my Qi Sense could read. The Head Elder probably belonged to that category, too.

“Our family has three Peak masters in total: the Lesser Family Head, the Head Elder, and Sir Wipeng. The Mount Heng Sword Sect has five.”

…This was so damn hopeless I couldn’t even deal with it.

*What? A prestigious family with deep roots? Two hundred years of history?*

What the hell had these bastards been doing for two hundred years? I heard the Mount Heng Sword Sect had existed for less than thirty, but in terms of military strength, we weren’t merely outmatched.

We were being steamrolled. Steamrolled.

*Did the Black Death sweep through last year or something?*

Whether there had been a plague or not, I felt like I was going insane. I was staring at the meeting-hall ceiling, which had yellowed before I knew it, when I suddenly made a decision.

*I need to run.*

Around four in the morning should do. Once everyone was asleep, I’d sneak over the wall and run as far away as possible.

At my current level, I could easily take down five or six martial artists around the Heavenly Axe’s level.

I could scour every mountain I came across and rack up EXP and Fame—

“Mount Heng—A messenger pigeon has arrived from the Mount Heng Sword Sect!”

A martial artist had rushed into the hall and shouted.

Someone accepted the tightly rolled sheet of paper and unrolled it. Red words, as if written in blood, appeared before my eyes.

Even without a System translation, I could understand them.

> **Enemies Who Cannot Live Beneath the Same Sky**

*Enemies who cannot coexist beneath heaven.*

Jin Wikyung spoke with a grim expression.

“From this moment onward, our family enters a state of war. Without my seal, no one may enter or leave the family grounds, regardless of rank. Maintain a strict state of vigilance. Do not let a single ant through. Understood?”

“Yes!”

“……”

With my mind half gone, I heard a System notification ring in my ears.

Ding.

> **System**
>
> - The **Mount Heng Sword Sect** has declared war on the **Jin Family of Taiyuan**.
>
> - A **War** relationship has been established between both factions.
>
> - The **Mount Heng Sword Sect** has designated you as a public enemy of the sect.
>
> - You will incur severe penalties if you flee.
>
> - The **Main Quest — War** has been created.

…Heh. Heh heh heh.
```
