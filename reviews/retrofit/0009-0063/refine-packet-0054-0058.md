# Retrospective Patch Plan — Chapters 54–58

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
  "summary": "13 findings in chapters 54-58",
  "findings": [
    {
      "chapter": 54,
      "confidence": 0.99,
      "current": "To them, I had been a Benefactor, a trusted superior, and a comrade they could turn their backs to.",
      "defect": "The English reverses the trust idiom: 등을 맡길 수 있는 means entrusting one’s exposed back to a comrade, not turning one’s back on or away from them.",
      "id": "R0054-01",
      "rationale": "The source specifically characterizes Taekyung as someone they trusted to protect them in combat.",
      "replacement": "To them, I had been a Benefactor, a trusted superior, and a comrade they could trust to watch their backs.",
      "severity": "major",
      "source": "나는 그들에게 있어 은인이었고, 신뢰하는 상관이자 등을 맡길 수 있는 전우였다."
    },
    {
      "chapter": 54,
      "confidence": 0.96,
      "current": "I had been a blood brother, too.",
      "defect": "“Blood brother” commonly denotes sworn brotherhood and leaves the actual biological kinship unclear.",
      "id": "R0054-02",
      "rationale": "The preceding memories are of Taekyung’s biological brother, and 피를 나눈 형제 explicitly invokes shared blood.",
      "replacement": "I was also his brother by blood.",
      "severity": "major",
      "source": "피를 나눈 형제이기도 했다."
    },
    {
      "chapter": 54,
      "confidence": 1.0,
      "current": "Luxury Freak.",
      "defect": "The displayed contact name does not use the established translation.",
      "id": "R0054-03",
      "rationale": "명품충 is fixed in the supplied glossary as Designer-Brand Junkie.",
      "replacement": "Designer-Brand Junkie.",
      "severity": "minor",
      "source": "[명품충]"
    },
    {
      "chapter": 54,
      "confidence": 0.99,
      "current": "“I’ll make him one of my people. Even if I have to pay him three personal visits.[^1]”",
      "defect": "The established name of the historical allusion is paraphrased rather than preserved.",
      "id": "R0054-04",
      "rationale": "삼고초려 is fixed in the supplied glossary as Three Visits to the Thatched Cottage, and the following Zhuge Liang joke depends on that allusion.",
      "replacement": "“I’ll make him one of my people. Even if it takes Three Visits to the Thatched Cottage.[^1]”",
      "severity": "minor",
      "source": "“내 사람으로 만들 겁니다. 삼고초려를 해서라도.”"
    },
    {
      "chapter": 55,
      "confidence": 1.0,
      "current": "Squad Leader",
      "defect": "Taekyung’s established squad title and Hyuk Mujin’s form of address are rendered inconsistently.",
      "id": "R0055-01",
      "rationale": "The supplied glossary fixes 조장, specifically Hyuk Mujin’s address for Taekyung, as Captain.",
      "replacement": "Captain",
      "severity": "minor",
      "source": "조장"
    },
    {
      "chapter": 56,
      "confidence": 0.98,
      "current": "For many years he had carried two swords. One at his chest, the other at his waist.\n\nThere was no need for more words.",
      "defect": "The first sword is metaphorically harbored in the Head Elder’s heart, but the English places a second physical sword at his chest.",
      "id": "R0056-01",
      "rationale": "가슴에 품었다 contrasts the concealed purpose he has carried within himself with the actual sword at his waist.",
      "replacement": "For many years, he had carried two swords: one in his heart, and one at his waist.\n\nThere was no need for more words.",
      "severity": "major",
      "source": "오랜 세월 두 자루의 검을 품었다. 하나는 가슴에, 하나는 허리춤에. 이제 더는 말이 필요 없었다."
    },
    {
      "chapter": 56,
      "confidence": 1.0,
      "current": "sixty years of internal energy",
      "defect": "The established Murim unit is converted into an explanatory quantity instead of using its fixed term.",
      "id": "R0056-02",
      "rationale": "갑자 is fixed in the supplied glossary as jiazi.",
      "replacement": "one jiazi of internal energy",
      "severity": "minor",
      "source": "일 갑자에 달하는 공력"
    },
    {
      "chapter": 56,
      "confidence": 0.99,
      "current": "His aim was to lay the foundation for a prestigious house that would one day be recognized even in the Central Plains.",
      "defect": "The established Murim category 세가 is replaced with a generic description.",
      "id": "R0056-03",
      "rationale": "세가 is fixed in the supplied glossary as great family.",
      "replacement": "His aim was to lay the foundation for a great family that would one day be recognized even in the Central Plains.",
      "severity": "minor",
      "source": "장차 중원에서도 인정받는 세가(世家)의 초석을 다지고자 했다."
    },
    {
      "chapter": 56,
      "confidence": 0.94,
      "current": "Whether in one form or half a form, the old man in front of him was a master a league above Lee Cheonbaek.",
      "defect": "“Whether in one form or half a form” is incoherent English and loses the source’s measurement of the old man’s superiority by a full or half move.",
      "id": "R0056-04",
      "rationale": "The source says that regardless of whether the margin was one full form or half a form, the Head Elder was the superior master.",
      "replacement": "Whether by a full form or half a form, the old man before him stood above Lee Cheonbaek.",
      "severity": "major",
      "source": "일 초식이건, 반 초식이건 눈앞의 노인은 이천백보다 윗줄의 고수였다."
    },
    {
      "chapter": 57,
      "confidence": 1.0,
      "current": "Squad Leader",
      "defect": "Taekyung’s established squad title and form of address are rendered inconsistently.",
      "id": "R0057-01",
      "rationale": "The supplied glossary fixes 조장 as Captain.",
      "replacement": "Captain",
      "severity": "minor",
      "source": "조장"
    },
    {
      "chapter": 57,
      "confidence": 1.0,
      "current": "The martial artists of the small and mid-sized sects known as the Five Gates of Shanxi—the Three Paths Sect, a union of three sects; the Tao-centered Byeokdo Sect; and Gunggwimun, which had been pouring arrows from the cliffs without pause—turned in an instant.",
      "defect": "Two named sects are rendered under non-established names, obscuring their identities within the Five Gates of Shanxi.",
      "id": "R0057-02",
      "rationale": "삼도문 and 궁귀문 are fixed in the supplied glossary as Samdo Sect and Gunggui Sect.",
      "replacement": "The martial artists of the small and mid-sized sects known as the Five Gates of Shanxi—the Samdo Sect, a union of three sects; the Tao-centered Byeokdo Sect; and the Gunggui Sect, which had been pouring arrows from the cliffs without pause—turned in an instant.",
      "severity": "major",
      "source": "세 개의 문파 연합체인 삼도문, 도를 중심으로 수련하는 벽도문, 절벽에서 쉴 새 없이 화살을 쏘아 대던 궁귀문까지."
    },
    {
      "chapter": 57,
      "confidence": 0.99,
      "current": "They were no longer the clumsy third-rate martial artists they had seemed to be.",
      "defect": "The formal martial realm designation is rendered as an ordinary lowercase description.",
      "id": "R0057-03",
      "rationale": "삼류 is fixed in the supplied glossary as the realm label Third Rate.",
      "replacement": "They were no longer the clumsy Third Rate martial artists they had seemed to be.",
      "severity": "minor",
      "source": "그들은 더 이상 어설픈 삼류 무인들이 아니었다."
    },
    {
      "chapter": 58,
      "confidence": 1.0,
      "current": "Squad Leader",
      "defect": "Taekyung’s established squad title and form of address are rendered inconsistently.",
      "id": "R0058-01",
      "rationale": "The supplied glossary fixes 조장 as Captain.",
      "replacement": "Captain",
      "severity": "minor",
      "source": "조장"
    }
  ]
}
```

## Chapter 54

### Korean source

```text
＃54화



오래된 TV를 보는 기분이다.

빛바랜 화면 속 뚝뚝 끊기는 장면과 목소리들. 그럼에도 불구하고 생생하게 느껴지는 전장의 열기.

‘죽여!’

‘태원 진가를 멸(滅)하라!’

좁은 협곡을 빼곡하게 메운 이들이 함성과 함께 돌격한다. 그들의 등 뒤로 항산(恒山)이라 적힌 깃발이 흔들렸다.

시퍼렇게 날 선 병장기의 끝에, 또 다른 깃발이 있다.

진(振).

그리고 협곡을 틀어막은 수백의 무인들.

‘무(武)도, 협(俠)도 없는 놈들이다. 항산검문은 오늘 사라진다!’

‘쳐라!’

지지직.

노이즈와 함께 시야가 확대된다. 태원진가를 상징하는 깃발 아래, 확연히 눈에 띄는 두 사람을 향해.

흰 수염을 늘어트린 노인이 입을 열었다.

‘긴 싸움이 되겠군.’

거대한 덩치의 사내가 대답했다.

‘그리고 마지막 싸움이 되겠지요.’

노인이 활짝 웃었다.

‘그렇게 될 거요. 반드시.’

이윽고.

사람과 사람, 검과 창이 부딪친다. 셀 수 없이 많은 무인들이 격돌했고, 협곡에는 짙은 피안개가 깔렸다.

어디선가 전투의 시작을 알리는 북소리가 울려 퍼졌다.

둥. 둥. 둥.



* * *



“헉.”

땀에 젖은 몸을 일으켰다. 또 무림에 관한 꿈이다.

처음과는 달리 이제는 깨어난 후에도 꿈의 내용을 또렷하게 떠올릴 수 있었다.

‘전투가 시작됐어.’

현실로 돌아와도 무림의 시간은 흐른다.

내가 본 장면들은 지금 무림에서 벌어지고 있는 일인지도 모른다. 두 거대 세력의 명운을 건 대전투.

‘아니, 하나 더 있지.’

대장로가 이끄는 제삼의 세력.

전투가 절정으로 치닫고 양 세력이 큰 피해를 입었을 때, 그때 비로소 놈들이 움직일 것이다.

‘혁무진은? 정찰조원들은 어떻게 된 거지?’

그들이 늦지 않게 도착하여 배신을 알린다면 최악의 사태는 면할 수 있다. 어쩌면 그 반대로 이미 모든 게 끝나 있을 수도 있다.

‘대장로…….’

첫인상부터 꺼림칙했던 늙은이. 태원진가의 웃어른이라는 작자가 이런 일을 꾸미고 있을 줄이야.

만약 대장로가 최후의 승자가 된다면 모든 게 끝이다.

반역의 끝에는 피의 숙청이 뒤따르는 법이니까.

‘진위경, 위팽, 혁무진과 정찰조원들.’

거기에 더해 조필과의 싸움에서 중상을 입어 출진하지 못한 한엽, 회복 중인 공야청과 소천, 소율 남매까지.

낯익은 얼굴들이 떠올랐다 사라지기를 반복한다.

‘그들은 내게 뭐였지?’

무림에서의 한 달.

나는 그들에게 있어 은인이었고, 신뢰하는 상관이자 등을 맡길 수 있는 전우였다. 그리고 누군가에게는…….



‘네가 자랑스럽구나.’

‘다친 곳은 없느냐?’

‘살아남아라, 막내야.’



피를 나눈 형제이기도 했다.

하지만 그들은 내게 있어 뭐였을까. 뛰어난 인공지능을 탑재한 NPC? 아니면 사람?

‘뭐였을까.’

나만이 오갈 수 있는 또 하나의 차원, 그리고 그곳에 남아 있는 사람들. 이걸 어떻게 해야 하나.

눈이 저절로 캡슐을 향했다.

‘만약에 돌아가면…….’

문득 든 생각에 화들짝 놀랐다. 내가 미쳤구나.

돌아가면 뭐 어쩌려고? 자그마치 2천여 명의 무림인이 뒤섞인 대전투다. 그중에는 일문일살 조필만큼, 혹은 조필보다 강한 괴물들도 있다.

그런데 거기로 돌아가?

“이 미친놈. 미친 새끼. 제대로 미쳤어, 아주.”

한숨처럼 중얼거리던 그때, 핸드폰이 울렸다.

지이잉.



[명품충]



최 팀장이었다.



* * *



빌딩 숲 중심부에 위치한 대형 카페.

“말씀하신 자료입니다.”

김 집사가 두꺼운 서류철을 내밀었다. 대충 보기에도 백여 페이지에 달하는 방대한 분량이다.

“많군요.”

“그만큼 철저하게 조사했습니다.”

최민우는 고개를 끄덕이고 빠르게 페이지를 넘기기 시작했다. 그가 읽고 있는 것은 한 사람의 인생이었다.

진태경의 27년이 이 백여 페이지의 종이에 담겨 있다.

출생지, 출생 배경과 성장 과정, 심지어는 은행에서 제공한 계좌 조회 기록까지. 없는 게 없었다.

특이하거나 의심이 가는 부분은 굵게 칠해져 있었기 때문에 최민우는 불과 30분도 안 되어 준비된 서류를 전부 읽었다.

“집사님 생각은 어떠세요?”

“깨끗합니다.”

김 집사가 확정적인 어조로 대답했다.

“부정 각성자도 아니고, 도련님께 계획적으로 접근한 것도 아닙니다.”

최민우는 고개를 끄덕였다. 김 집사가 그렇다면 그런 거다.

그는 지난 2주 동안 온갖 수단을 동원해 진태경의 모든 걸 들여다본 사람이니까. 마찬가지로, 지금 테이블 위에 놓인 백여 페이지의 서류도 모두 김 집사의 손을 거쳤을 것이다.

“그럼 이게 모두 우연이다?”

“지금으로서는 그렇습니다.”

“집사님.”

“예, 말씀하십시오.”

“재각성 확률이 얼마나 되는지 알고 계십니까?”

“1% 정도로 알고 있습니다.”

백 명 중 하나.

일반인의 시선에는 그리 희박한 확률이 아닐지도 모른다. 그러나 저 백 명은 일반인이 아닌 헌터다.

이미 비슷한 확률을 거쳐 탄생한 헌터들. 그중에서도 선택받은 자들만이 재각성의 행운을 누리는 것이다.

“그럼 F급 헌터가 단번에 C급 헌터로 재각성할 확률은 얼마나 될까요?”

최민우는 대답을 기다리지 않았다.

“C급 헌터가 혼자 동급 게이트를 클리어할 가능성은요?”

“혼자라면 불가능합니다. B급 헌터는 되어야…….”

“그런데 가능한 사람이 있더군요.”

“혹시?”

“C급 게이트 10회. D급 게이트 10회. 총합 스무 번의 레이드 동안 제가 한 거라곤 팔짱 끼고 구경한 게 답니다. 나설 필요도 없었어요.”

길쭉한 손가락이 두꺼운 서류철을 톡톡 두드렸다.

그 안에는 진태경의 모든 게 적혀 있었지만, 한편으로는 아무것도 적혀 있지 않았다.

잠시 침묵하던 김 집사가 입을 열었다.

“다시 조사해 보겠습니다.”

“아닙니다.”

최민우가 고개를 저었다.

“자꾸 긁으면 부스럼만 생겨요. 계속 곁에 두고 지켜볼 생각입니다.”

“결국 길드로 영입할 생각이십니까?”

“해야죠. 구린내가 나면 뒤를 캐 보고, 그게 아니면…….”

최민우의 눈이 반짝 빛났다.

“내 사람으로 만들 겁니다. 삼고초려를 해서라도.”

그리고 다음 순간.

딸랑.

방울 소리와 함께 카페로 들어온 한 사람을 보며 최민우는 피식 웃었다.

제갈량, 아니 진태경이었다.



* * *



계약금 5억.

월 5천만 원의 고정 급여와 7할의 정산 비율.

40평 상당의 오피스텔과 승용차는 옵션이요, 4대 보험은 기본이다. 계약서를 다 읽고 드는 생각은 딱 하나였다.

‘미쳤다.’

이런 무지막지한 계약 조건이라니.

집도 주고, 차도 주고, 돈은 썩어나게 준다.

C급 헌터 평균 연봉이 2억이다. 고정 급여, 레이드 수당을 모두 합쳐서 그렇다.

그런데 나는?

‘순수 계약금만 5억.’

최소 B급 헌터나 받을 수 있는 계약서다.

이건 내 실력이 그만큼은 된다는 뜻이기도 하고, 단순하게 헌터를 등급으로만 판단하지 않는 안목 있는 고용주를 만났다는 증거이기도 하다.

‘거기에 더해 돈도 있고.’

나는 테이블 너머의 최 팀장을 물끄러미 바라봤다. 언제나처럼 속을 알 수 없는 표정에 깊은 눈빛이다.

최 팀장이 불쑥 입을 열었다.

“이번이 세 번째군요.”

그는 앞서 두 번의 계약 제의를 했다. 내가 두 번 다 거절했지만. 이번에는 거절하지 말라는 완곡한 표현이다.

“그 부분은 죄송하게 생각합니다. 사소한 문제가 있어서요.”

“해결하신 겁니까?”

“네. 일단은 그런 것 같네요.”

“그럼 이제 아무 문제 없군요.”

“……그럼요.”

대답하면서도 의문이다. 이제 정말 아무 문제도 없는 걸까. 이대로 괜찮은 걸까.

‘내가 도대체 무슨 생각을.’

딴생각이 들기 전에 해치워야 한다.

“사인하겠습니다.”

나는 최 팀장에게 건네받은 만년필로 사인을 시작했다.

한 장, 두 장, 세 장…….

계약서는 총 다섯 장이었다. 이제 남은 한 장에 이름 석 자를 써 넣으면 끝이다.

그 순간, 다시 한번 의문이 떠올랐다.

‘이대로 괜찮은 건가?’

지금껏 거침없이 움직이던 만년필이 속도를 늦췄다. 생각이 꼬리에 꼬리를 물고 이어졌다.

‘괜찮지 않으면? 이게 내가 바랐던 거 아닌가?’

맞다. 7년 동안 간절히 꿈꿨던 상황이다.

막대한 연봉과 높은 사회적 지위를 얻는 것.

자랑스러운 아들, 오빠가 되어 가족들을 호강시켜 주는 것.

무시와 경멸 대신 부러움과 선망의 대상이 되는 것.

‘이제 다 이룰 수 있어.’

저 모든 것들을 누리며 살 수 있다. 구질구질했던 인생도, 개 같은 무림도 안녕이다.

빠각.

그리고 만년필도 안녕.

나는 손아귀의 힘을 풀었다. 박살 난 만년필과 함께 흘러내린 잉크가 계약서를 적셨다.

“진태경 씨. 다시 물어보겠습니다.”

최 팀장이 흰 손수건을 꺼내 턱에 튄 잉크를 닦아 냈다.

갑작스러운 상황에도 그는 침착해 보였다.

“지난번 그 문제, 정말 해결됐습니까?”

“아뇨.”

대답을 하고 나니 속이 후련했다.

“혹시 제가 도와드릴 수 있는 문제라면…….”

“말씀은 감사합니다만, 저 혼자 해결해야 합니다.”

묘한 시선으로 나를 응시하던 최 팀장이 피식 웃었다.

“계약이 이렇게 힘든 줄은 몰랐네요. 세 번이나 퇴짜 맞는 것도 예상 못 했고.”

화났다기보다는 이 상황이 재미있다는 어투다.

“네 번째 제의는 언제쯤 하는 게 좋을까요?”

반 농담 삼아 한 말이었겠지만 내 대답은 진지했다.

“내일 이 시간, 이 장소에서요.”

“내일이요?”

“예. 내일.”

고작 하루.

그러나 내게는 한 달, 혹은 몇 달이 될 것이다.

그 사실을 알 리 없는 최 팀장은 눈살을 찌푸렸다.

“그런 농담은 별로 안 좋아하는데요.”

“저도 안 좋아합니다. 이런 농담.”

그는 모른다. 내 말에 어떤 뜻이 담겨 있는지를.

“꼭 뵙죠.”

이건 스스로에게 하는 다짐이다.

반드시 살아 돌아오겠다는 다짐.

그리고…….

“내일은 계약 조건을 더 올려야 할 겁니다.”

나는 눈이 커진 최 팀장을 뒤로하고 카페를 나왔다.



* * *



“후우.”

크게 심호흡하며 캡슐을 열었다.

푹 꺼진 의자와 VR 헬멧을 보자 가슴이 두방망이질 친다. 여기까지 왔음에도 불구하고, 자꾸만 유혹이 고개를 들고 속삭인다.

돌아가지 말라고.

그냥 싹 다 잊고, 네 현실에 만족하면서 살라고.

무림에서 만난 이들은 모두 NPC고, 무림은 단순한 게임일 뿐이라고.

맞다. 그렇게 생각하던 때가 있었다.

하지만 고민 끝에 깨달았다. 나는 어떻게든 다시 돌아갈 거라는 사실을.

‘이미 오래전부터 결론은 나와 있었어.’

폭설이 내리던 그 날 밤, 나는 공야청에게 돌아갔다.

짐짝밖에 안 되는 어린 남매를 합류시켰고, 정찰조원들을 방패막이로 쓰는 대신 조필에 맞서 싸우며 죽을 고비를 넘겼다.

‘아마 그때부터였겠지.’

뇌리에 박혀 있던 NPC라는 세 글자가 희미해진 것은.

살아남으라 하고 돌아서던 진위경의 뒷모습에서 가족이라는 두 글자를 떠올린 것은.

“시발, 인생 진짜 버라이어티하네.”

나는 푸념 섞인 헛웃음과 함께 캡슐로 들어갔다. VR 헬멧을 쓰자마자 눈앞으로 한 줄 메시지가 떠오른다.

띠링.



[무림]에 접속하시겠습니까?

수락   /   거절



“예스.”

희미해지는 의식, 어두워지는 시야.

나는 로그인(Login)했다.
```

### Current accepted English

```markdown
# Chapter 54

It felt like watching an old TV.

Scenes and voices stuttered across a faded screen, cutting in and out. Even so, the heat of the battlefield came through vividly.

“Kill!”

“Destroy the Jin Family of Taiyuan!”

The people packed into the narrow gorge charged forward with a roar. Behind them, a flag marked *Mount Heng* whipped in the air.

At the tips of those steel-blue weapons was another flag.

Jin (振).

And hundreds of martial artists sealing off the gorge.

“They’re bastards with neither martial honor nor chivalry. The Mount Heng Sword Sect disappears today!”

“Attack!”

Static crackled.

The view zoomed in through the noise, locking onto two people who stood out beneath the flag of the Jin Family of Taiyuan.

An old man with a long white beard spoke.

“This is going to be a long fight.”

A massive man answered.

“And the last one.”

The old man smiled wide.

“It will be. Without fail.”

And then.

People crashed into people, swords into spears. Countless martial artists collided, and a thick blood-mist settled over the gorge.

Somewhere, a drumbeat announcing the start of battle rolled out.

Boom. Boom. Boom.

* * *

“Hah.”

I sat up, soaked in sweat. Another Murim dream.

Unlike at first, I could remember it clearly even after waking.

*The battle has begun.*

Even after I came back to reality, time kept moving in Murim.

The scenes I had seen might be happening there right now. A great battle with the fate of two massive forces on the line.

*No. There’s one more.*

A third force led by the Head Elder.

Once the fighting hit its climax and both sides had taken heavy losses, that was when they would finally move.

*What about Hyuk Mujin? What happened to the reconnaissance squad?*

If they arrived in time and exposed the betrayal, the worst could still be avoided. Or the opposite had already happened, and everything was already over.

*The Head Elder….*

An old man who had given me the creeps from the first impression. Who would have thought that so-called elder of the Jin Family of Taiyuan would be plotting something like this?

If the Head Elder became the final victor, it would all be over.

The end of a rebellion always brought a bloody purge.

*Jin Wikyung, Wipeng, Hyuk Mujin, and the reconnaissance squad.*

Plus Han Yeop, too badly injured in his fight with Jopil to march out, and Gong Yacheong and the siblings Socheon and Soyul, still recovering.

Familiar faces appeared and vanished in my mind again and again.

*What were they to me?*

One month in Murim.

To them, I had been a Benefactor, a trusted superior, and a comrade they could turn their backs to. And to someone…

“I’m proud of you.”

“Are you hurt anywhere?”

“Survive, youngest.”

I had been a blood brother, too.

But what had they been to me? NPCs loaded with advanced AI? Or people?

*What were they?*

Another dimension only I could come and go from, and the people left behind there. What was I supposed to do about that?

My eyes drifted to the capsule on their own.

*If I went back….*

The thought startled me. I was out of my mind.

Go back and do what? It was a great battle with some two thousand martial artists mixed together. Among them were monsters as strong as Jopil, One Question, One Kill—or even stronger.

And I was thinking of going back there?

“You lunatic. You crazy bastard. You’ve completely lost it.”

I was muttering it like a sigh when my phone rang.

Bzzz.

Luxury Freak.

It was Team Leader Choi.

* * *

A large café in the heart of a downtown forest of high-rises.

“Here are the materials you requested.”

Butler Kim held out a thick binder. Even at a glance, it looked like a massive file of more than a hundred pages.

“That’s a lot.”

“I investigated just as thoroughly.”

Choi Minwoo nodded and started flipping through the pages. What he was reading was one person’s life.

Jin Taekyung’s twenty-seven years were packed into those hundred-plus pages.

Birthplace, background, how he had grown up—even account inquiry records provided by the bank. Nothing was missing.

Unusual or suspicious parts had been highlighted in bold, so Choi Minwoo finished the entire file in under thirty minutes.

“What do you think, Butler Kim?”

“He’s clean.”

Butler Kim answered in a definitive tone.

“He isn’t an illegal Awakener, and he didn’t approach you as part of some plan.”

Choi Minwoo nodded. If Butler Kim said so, that was how it was.

He was the one who had spent the past two weeks using every means available to look into everything about Jin Taekyung. Likewise, every page of the hundred-odd-page file on the table would have passed through his hands.

“So this was all a coincidence?”

“For now, yes.”

“Butler Kim.”

“Yes. Please go ahead.”

“Do you know the odds of reawakening?”

“I understand they’re around one percent.”

One in a hundred.

From an ordinary person’s perspective, that might not seem impossibly rare. But those hundred people were not ordinary people. They were Hunters who had already been born through similar odds.

And among them, only the chosen enjoyed the luck of reawakening.

“Then what are the odds that an F-rank Hunter reawakens in one jump as a C-rank Hunter?”

Choi Minwoo did not wait for an answer.

“What about the odds that a C-rank Hunter could clear a Gate of the same rank alone?”

“Alone, it would be impossible. He’d have to be at least B-rank…”

“And yet there’s someone who can.”

“Could it be…?”

“Ten C-rank Gates. Ten D-rank Gates. Across twenty raids in total, all I did was sit with my arms crossed and watch. I never even needed to step in.”

His long fingers tapped the thick binder.

Everything about Jin Taekyung was written inside it, and in another sense, nothing was.

After a moment of silence, Butler Kim spoke.

“I’ll investigate him again.”

“No.”

Choi Minwoo shook his head.

“Keep scratching and you’ll only raise a sore. I intend to keep him close and watch.”

“Do you intend to recruit him into the Guild after all?”

“I should. If something smells fishy, I’ll dig into his background. If it doesn’t…”

Choi Minwoo’s eyes gleamed.

“I’ll make him one of my people. Even if I have to pay him three personal visits.[^1]”

And in the next moment—

Jingle.

As someone came into the café with the doorbell, Choi Minwoo gave a quiet laugh.

Zhuge Liang—or rather, Jin Taekyung.

* * *

A signing bonus of 500 million won.

A fixed monthly salary of 50 million won and a seventy-percent settlement split.

A roughly 132-square-meter officetel[^2] and a sedan came as extras, and the four major social insurances were a given. After reading the contract through, I had exactly one thought.

*This is insane.*

What kind of outrageous terms were these?

They were giving me a home, a car, and more money than I knew what to do with.

The average annual salary of a C-rank Hunter was 200 million won, including fixed pay and raid pay.

And me?

*The signing bonus alone is 500 million.*

This was the kind of contract a B-rank Hunter could get, at minimum.

It also meant my skill was valued that highly. And it was proof I had found an employer with the insight not to judge a Hunter by rank alone.

*And he has the money, too.*

I stared across the table at Team Leader Choi. As always, his expression gave nothing away, and his eyes were deep.

Team Leader Choi spoke without warning.

“This is the third time.”

He had made two offers before. I had turned both down. This was a roundabout way of telling me not to refuse him again.

“I’m sorry about that. There was a minor issue.”

“Have you resolved it?”

“Yes. For now, it seems that way.”

“Then there shouldn’t be any problem now.”

“…Of course.”

Even as I answered, I still had doubts. Was there really no problem now? Was it okay to leave it like this?

*What the hell am I thinking?*

I had to knock this out before my mind wandered.

“I’ll sign.”

I started signing with the fountain pen Team Leader Choi had handed me.

One page, two pages, three…

The contract was five pages long. All I had to do was write the three characters of my name on the last page, and it would be done.

At that moment, the question came back.

*Is this really okay?*

The fountain pen that had been moving without hesitation slowed. One thought caught on the next.

*What if it isn’t? Isn’t this what I wanted?*

It was. This was exactly what I had dreamed of so desperately for seven years.

A massive salary and high social standing.

Becoming a son and older brother they could be proud of, and treating my family to an easy life.

Becoming someone to envy and admire instead of someone to ignore and look down on.

*I can have it all now.*

I could live enjoying every bit of it. Goodbye to my grimy life. Goodbye to that shitty Murim.

Crack.

And goodbye to the fountain pen, too.

I let the strength out of my grip. Ink spilled from the shattered pen and soaked the contract.

“Mr. Jin Taekyung. Let me ask you again.”

Team Leader Choi pulled out a white handkerchief and wiped the ink that had splashed onto his chin.

For all the sudden mess, he looked calm.

“That problem from last time. Have you really resolved it?”

“No.”

Once I said it, I felt a weight lift.

“If it’s something I can help you with…”

“I appreciate it, but I have to handle this myself.”

Team Leader Choi studied me with an odd look, then gave a small laugh.

“I didn’t know a contract could be this hard. I didn’t expect to get turned down three times, either.”

He sounded amused by the situation rather than angry.

“When would be a good time to make the fourth offer?”

He had probably meant it half as a joke, but my answer was serious.

“Tomorrow, at this time, in this place.”

“Tomorrow?”

“Yes. Tomorrow.”

Only one day.

But for me, it would be a month, or maybe several.

Team Leader Choi had no way of knowing that, and he furrowed his brow.

“I don’t much like jokes like that.”

“Neither do I. Not jokes like this.”

He didn’t know what my words meant.

“I’ll be sure to see you.”

That was a vow to myself.

A vow that I would come back alive.

And…

“Tomorrow, you’ll have to raise the contract terms even further.”

I left the café, leaving Team Leader Choi behind with his eyes wide.

* * *

“Phew.”

I drew a deep breath and opened the capsule.

The sunken seat and VR headset made my heart hammer. Even after coming this far, temptation kept lifting its head and whispering.

*Don’t go back.*

*Just forget everything and live content with your reality.*

*Everyone you met in Murim is an NPC, and Murim is nothing more than a game.*

Right. There had been a time I thought that way.

But after thinking it through, I realized I was going back, one way or another.

*I’d already reached my conclusion a long time ago.*

On the night of the blizzard, I had gone back for Gong Yacheong.

I had brought along two young siblings who were nothing but baggage, and instead of using the reconnaissance squad as a shield, I had fought Jopil and barely made it through.

*It probably started then.*

That was when the three letters NPC, lodged in my head, began to fade.

That was when I saw the two-character word for family in Jin Wikyung’s back as he told me to survive and turned away.[^3]

“Fuck, life really is a variety show.”

With a hollow, complaining laugh, I climbed into the capsule. The moment I put on the VR headset, a single line of text appeared in front of me.

Ding.

> **System**
>
> Would you like to connect to Murim?
>
> **Accept** / **Decline**

“Yes.”

My consciousness faded. My vision darkened.

I logged in.

[^1]: “Paying three personal visits” alludes to Liu Bei’s repeated visits to Zhuge Liang in *Romance of the Three Kingdoms* to recruit him as an adviser.
[^2]: An officetel is a Korean mixed-use unit designed for both office and residential use.
[^3]: In Korean writing, each syllable is written as a single character block; the word for “family” consists of two such blocks, contrasting with the three Roman letters in “NPC.”
```
## Chapter 55

### Korean source

```text
＃55화



‘환장하겠네.’

혁무진은 눈앞이 노래지는 것을 느꼈다.

중소 문파의 제자들로 위장하고 있던 암살자들. 그리고 대장로의 배신. 여기까지만 해도 머리가 터질 지경인데…….

‘이 인간은 왜 쓰러진 거냐고!’

난데없이 진태경이 정신을 잃었다. 정찰조원들이 돌아가며 뺨도 때리고, 멱살을 짤짤 흔들어도 깨어날 기미가 안 보인다.

‘분명히 숨은 붙어 있는데.’

귀신이 곡할 노릇이다. 일이 이렇게 되니 결국 부조장인 자신이 이 엄청난 일의 책임자가 되어 버렸다.

“너, 그리고 너.”

아직도 혼란에 빠져 있는 정찰조원들 중 두 사람을 지목한 혁무진이 말했다.

“너희 둘은 지금 당장 본가로 복귀해서 이 사실을 알려라.”

대장로.

가문의 웃어른이자 옛 정마대전의 영웅인 그가 어떤 이유로, 무엇을 위해 이런 암계를 꾸몄는지는 모른다.

그러나 최악의 사태만은 막아야 했다.

“나머지는 모두 본대로 이동한다. 서둘러!”

혁무진은 정신을 잃고 쓰러져 있는 진태경을 등에 업었다.

그렇게 한 시진 가량을 달리자 이번에는 다른 의미로 눈앞이 노래졌다.

‘죽겠네.’

조필의 무지막지한 일장(一掌)에 내상을 입었던 것이 불과 며칠 전이다. 진태경에게는 거의 다 나았다고 큰소리를 쳤지만 사실 보름은 꼼짝없이 요양해야 할 상태였다.

“헉, 허억.”

온몸이 흠뻑 젖고 다리가 후들거린다.

그냥 따라가도 뒤처질 판인데 건장한 체구의 진태경까지 업고 있으니 그야말로 죽을 지경이다.

‘아, 어머니. 아버지.’

이제는 멀쩡히 살아 계신 부모님이 손짓하는 환영까지 보인다. 두 분 옆에 선 아주머니는 법당에서 자주 본 얼굴이다.

‘관음보살님?’

- 중생아. 고생했다. 이제 쉬어도 좋다.

자애로운 미소에 혁무진의 마음이 스르륵 풀어졌다.

그래, 이 정도면 할 만큼 했지. 조장이라는 인간은 정작 중요할 때 픽 쓰러지고. 조원이라는 새끼들은 내가 죽든 말든 대신 업겠다는 소리도 안 하고.

‘시벌, 모르겠다.’

혁무진이 정신을 놓으려던 그때였다.

“후우, 하아아.”

귓구멍을 파고드는 따뜻한 숨결. 누구인지는 돌아보지 않아도 알 수 있었다. 혁무진은 반가움에 눈물이 핑 돌았다.

“조장!”

진태경이 씩 웃으며 속삭였다.

“네 귀에 캔디.”



* * *



챙! 채챙!

“죽여! 죽여!”

“크아악!”

곳곳에서 피와 비명이 터져 나온다. 피를 뒤집어쓴 무인이 시체 사이를 엉금엉금 기어간다.

아직 앳된 얼굴이 고통과 공포로 얼룩져 있었다.

“흐윽, 흐으윽.”

참으려 해도 터져 나오는 울음. 십 년을 절치부심하며 무공을 익혔지만 피 튀기는 전장에서는 무소용이었다.

든든하던 선배가, 형제 같던 동기가 죽었다. 사방에서 쏟아진 병장기가 배를 가르고 사지를 난도질했다.

“어머니, 어머니…….”

하염없이 어머니를 부르던 그의 얼굴이 딱딱하게 굳었다.

푹-!

어느새 가슴팍에 돋아난 창날. 순간 부릅떠진 눈동자에서 이내 빛이 사라진다. 산적처럼 수염이 난 낭인이 녹슨 창을 뽑아내며 씩 웃었다.

“애새끼가 어딜.”

하지만 수없이 죽을 고비를 넘긴 낭인도, 다음 순간 날아드는 칼날을 피할 수는 없었다.

서걱-

은빛 선과 함께 낭인의 목이 솟구쳤다. 무인을 죽인 낭인, 낭인을 죽인 또 다른 무인.

이름도 모르는 이들이 사방에서 죽고 죽이기를 반복했다.

전장(戰場)은 그런 곳이었다.

‘그래, 이런 곳이었지.’

대장로는 상념에 젖은 얼굴로 전장을 바라봤다.

팔천협(八天峽). 수십 년 전 정마대전의 한 줄을 장식했던 격전지. 저 비좁은 협곡에서 얼마나 많은 이들이 죽어 갔던가.

‘그때는 나도 젊었지.’

육체는 강인했고 가슴은 뜨거웠다. 협(俠)이라는 낯간지러운 글자가 크게 느껴지던 시절이었다.

그러나 정마대전을 겪으며 대장로는 변했다. 끝없이 이어지는 전쟁에 지쳤고 죽음이 두려워졌다.

‘협의지사가 무슨 소용인가. 죽으면 귀신에 불과한 것을.’

그건 한 줄기 깨달음이었다. 마침내 그는 살아남아 영웅이 되었고, 기나긴 인고의 시간 끝에 이 자리에 섰다.

이제 결실을 맺어야 할 때. 대장로는 노회한 눈으로 옆에 선 한 사람을 응시했다.

‘아깝구나. 아까워.’

진위경은 뛰어난 인재다. 젊고, 무공도 상당하며 무엇보다 지도자에게 필요한 위엄과 판단력을 지녔다. 간혹 정에 얽매이는 모습을 보이긴 했지만 그 덕인지 가문 내에서 인망도 두터웠다.

‘능히 본가를 일으킬 수 있는 재목이다.’

만약 진위경이 태원진가의 가주가 된다면. 그리고 각기 두각을 나타내고 있는 두 아우가 뒤를 든든히 받쳐 준다면…….

대장로는 문득 자신의 생각을 깨닫고 피식 웃었다.

여기까지 온 마당에 이 무슨 해괴한 짓거리란 말인가. 심지어 진태경은 이미 죽어 고혼이 되었을 텐데.

“나도 늙었군.”

작은 중얼거림에 진위경이 반응했다.

“뭐라 하셨습니까?”

“별것 아니오. 원래 늙으면 혼잣말이 늘거든. 그보다 소가주가 보기에는 어떻소?”

“전황은 유리하게 흘러가고 있습니다만…….”

진위경의 표정이 살짝 어두워졌다. 병력의 질과 지형에서 우위를 점하고 있다고는 하나 피해는 꾸준히 누적되고 있었다.

가솔들의 죽음을 바라보는 그의 마음이 편할 리 없다.

“소가주. 그 마음은 알지만 경거망동하지 마시오.”

대장로는 엄중한 어조로 충고했다.

“우두머리는 나설 때를 알아야 하는 법, 전투가 길어질수록 조급해지는 것은 놈들이니 그때를 노려야 하오.”

“곧 항산검문에서도 총력으로 부딪쳐 오겠군요.”

“절정 고수들을 앞세우겠지. 문주인 이천백이 직접 올 수도 있고.”

“그때 모든 게 결정 나겠군요.”

대장로가 고개를 끄덕였다.

“소가주와 나, 위팽이 적들의 수뇌부를 막고 절벽 위에서 화살비가 쏟아지면 사기가 바닥으로 떨어질 거요.”

“화공을 못 쓰는 것이 아쉽습니다. 하늘이 원망스럽군요.”

팔천협의 좁은 지형은 화공에 안성맞춤이지만 며칠 전 내린 폭설로 인해 사방이 눈 더미였다.

그러나 하늘이 그의 편을 들어 주었다 해도 진위경이 기대하는 일은 일어나지 않았을 것이다.

절벽 위에서 활시위를 당길 이들은 대장로의 명령을 따를 테니까.

“나도 하늘이 원망스럽소.”

대장로의 말은 진심이었다.

기다린 세월이 너무 길었다. 이제야 찾아온 천명이 원망스러웠다.



* * *



“네 귀에 캔디.”

“조장!”

“꿈처럼 달콤했니.”

“……미쳤어요?”

못생긴 혁무진의 얼굴을 보자 반가움이 솟구쳤다. 내가 깨어났다는 말에 몰려든 다른 정찰조원들도 마찬가지였다.

“조장님 깨어나셨다!”

“무슨 일입니까? 몸은 괜찮으세요?”

“죽은 거 아니었어?”

방금 말한 새끼는 나중에 손봐 줘야겠다. 나는 얼굴과 이름을 기억해 둔 다음 모두에게 씩 웃어 보였다.

“오랜만이네. 잘들 있었냐?”

“예?”

“그게 무슨 말이래?”

“혹시 머리 다치신 거 아냐?”

“머리, 머리를 보자!”

충분히 예상했던 반응이다. 하지만 진심으로 한 번쯤 하고 싶었던 인사이기도 했다.

……미친놈 취급 받았지만.

“뭐 인사는 여기까지 하고. 나 기절한 지 얼마나 됐어?”

혁무진이 털썩 주저앉으며 대답했다.

“반 시진은 확실히 넘었고, 한 시진은 좀 안 됐을 겁니다.”

현실에서 2주를 보냈으니 얼추 시간이 맞아떨어진다. 나는 고개를 끄덕이고 다음 질문으로 넘어갔다.

“나 숨은 쉬었냐?”

“갑자기 왜 그래요, 진짜?”

“시간 없다. 빨리 대답해.”

“숨 쉬고 있었으니까 일어나신 거죠. 아니면 죽었게요?”

그것도 그러네.

로그인, 혹은 로그아웃 시 다른 한쪽은 가사 상태에 빠지는 모양이다.

‘암살자들 처리하기 전에 로그아웃했으면 돌아올 몸도 없었겠군.’

이 부분은 나중에 생각하기로 하자.

당장 급한 문제는 따로 있다.

“본대는?”

“안 그래도 그쪽으로 이동 중이었습니다. 두 명은 따로 빼서 가문으로 돌려보냈고요.”

“잘했어. 거리는 얼마나 남았지?”

“적어도 한 시진은 더 걸릴 것 같습니다.”

“한 시진이라.”

“저, 조장. 이런 말씀 드려서 죄송하지만…… 최악의 경우도 생각해야 할 것 같습니다.”

혁무진은 물론이고 정찰조원들 모두가 입을 꾹 다물었다. 최악의 경우가 뭘 뜻하는지 모르는 사람은 아무도 없었다.

‘나도 생각해 봤고.’

곽준이 죽기 직전 했던 말에 따르면 이번 배신은 오래전부터 철두철미하게 계획된 것이다.

하지만 그 계획엔 딱 한 가지 오류가 있다.

‘바로 나.’

대장로는 나를 너무 과소평가했다. 아니, 한편으로는 과대평가일지도 모르겠다. 자그마치 일류 고수 수십 명을 붙여 나를 죽이려고 했으니까.

그러나 그것만으로는 역부족이었고, 나는 살아남았다.

‘실수한 거지.’

거기에 더해, 곽준은 처음 본색을 드러내며 그런 말도 했다. 슬슬 움직여야 시간에 맞출 수 있다고.

그러니까…….

“아직 안 늦었어.”

조원들 한 명, 한 명과 시선을 맞추며 단호하게 말했다.

“최악의 경우는 생각하지 마라. 무슨 수를 써서라도 내가 그 결과를 바꿀 테니까.”

“조장…….”

“그러니까 무진아.”

나는 울컥한 표정의 혁무진에게 사람 좋게 웃어 보였다.

“당장 일어나.”

“힘들어 죽겠습니다.”

“맞아 죽고 싶냐?”

“…….”

“이 시간에 한 걸음이라도 더 뛰렴. 마라톤 정신 몰라?”

“모르는데요.”

아. 여기 무림이지.

“아무튼 빨리 일어나. 반 시진만 더 가면 된다.”

후들거리는 다리를 부여잡고 일어나던 혁무진이 고개를 갸웃한다.

“반 시진이요?”

“응, 반 시진.”

“말씀드렸잖아요. 최대한 빨리 가도 한 시진이라니까요.”

“그러니까. 반 시진.”

“지금 무슨 말씀을 하시는…….”

“무진아.”

“예?”

소처럼 순박하게 눈을 끔뻑이는 혁무진에게, 나는 더더욱 환하게 웃어 보였다.

“근성이라는 말, 들어 봤냐?”

한 시진이든 두 시진이든 상관없다.

무조건 반 시진 안에 간다.

“존나 뛰어. 그럼 돼.”

“헉.”

정찰조 전원의 얼굴이 새파랗게 질렸다.



* * *



“가로막혔습니다.”

“피해가 상당합니다. 문주님, 부디 조치를.”

이어지는 보고에도 항산검문주, 혈랑검 이천백의 눈은 뜨이지 않았다.

‘성급했다.’

급박하게 시작된 전쟁, 그만큼 준비도 미흡했다. 군량이 빠르게 소진되고 사기가 떨어지자 탈영하는 자도 속출했다.

‘놈들에게 전부 읽혔어.’

아들을 잃은 분노와 상황에 대한 조급함에 판단력이 흐려졌다. 수하들의 조언도 무시하고 가장 빠른 길을 찾았다.

그래서 결국 팔천협이라는, 이름도 생소한 좁은 협곡에서 태원진가 놈들과 맞닥트렸다.

“문주!”

수하의 외침에 이천백은 천천히 눈을 떴다. 절정 고수의 가공할 안력(眼力)이 전장을 꿰뚫었다.

“끄아아악!”

“쓸어 버려라! 오합지졸들일 뿐이다!”

일천이 훌쩍 넘어가는 아군은 좁은 입구에 가로막혀 나아가지 못하고 있었다. 선두에 세운 낭인들과 마적들은 머릿수만 많았지, 개개인의 기량은 태원진가의 평무사보다도 떨어졌다.

‘고작해야 칼받이 정도인가.’

내심 혀를 차던 그때, 수십여 명의 낭인들이 갑자기 전선에서 이탈하기 시작했다. 그중 선두에 선 중년 낭인이 목이 터져라 외쳤다.

“이대로는 개죽음이다! 혈우단(血雨團)의 형제들은 모두 후퇴하라!”

그것이 중년 낭인의 유언이 되었다.

사아악-

가벼운 바람. 낭인은 그 외에는 아무것도 느끼지 못했다.

어느샌가 혈랑검 이천백이 그를 스쳐 지나갔다는 사실도, 수하 낭인들이 모두 공포에 질려 발걸음을 멈췄다는 사실도 몰랐다.

다만 문득, 목이 뜨겁다고 생각했다.

“어…….”

깨끗하게 잘려 나간 목이 툭 떨어진다. 머리를 잃은 몸뚱이는 몇 걸음을 비틀거리더니 썩은 고목처럼 무너졌다.

“혈우단이라고 했나?”

이천백이 굳어 버린 낭인들에게 검을 겨눴다. 그의 검신에는 피 한 방울 묻어 있지 않았다.

“돌아가.”

절정 고수의 살기가 칼날처럼 쏘아졌다. 낭인들은 왔던 것보다 더 빠르게 선두를 향해 돌격했다.

눈앞의 절정 고수에게 덤비느니 선두에서 싸우는 게 더 낫다고 판단한 것이다.

“쥐새끼 같은 놈들.”

이천백이 그 뒤를 쫓았다. 이글거리는 그의 눈빛은 태원진가의 수뇌부가 있을 저 어디를 향하고 있었다.

“문주께서 앞장서신다!”

“모두 돌격! 태원진가를 쓸어 버려라!”

이천백이 나서자 항산검문의 핵심 전력도 그 뒤를 따랐다.

세 명의 절정 고수와 수십 명의 일류 고수들이 선두를 향해 짓쳐 들었다.
```

### Current accepted English

```markdown
# Chapter 55

*This is driving me crazy.*

Hyuk Mujin felt the world go yellow before his eyes.

Assassins disguised as disciples from minor sects. The Head Elder’s betrayal. That alone was enough to make his head feel like it was about to explode, but…

*Why the hell did this guy collapse too?!*

Jin Taekyung had gone down out of nowhere. The reconnaissance squad had taken turns slapping his cheeks and shaking him by the collar, and he still showed no sign of waking.

*He’s definitely still breathing.*

It was enough to make a ghost weep. And with things as they were, Hyuk Mujin—the deputy squad leader—had ended up in charge of this enormous mess.

“You, and you.”

Hyuk picked out two of the reconnaissance squad members still standing there in a daze.

“Return to the main family at once and report this.”

The Head Elder.

He did not know why the family’s senior, a hero of the old Great Faction War, had devised such a dark scheme, or what he hoped to gain from it.

But they had to stop the worst from coming to pass.

“The rest of us move to the main force. Hurry!”

Hyuk hoisted the unconscious Jin Taekyung onto his back.

After running for roughly two hours, the world went yellow before his eyes again—this time for a different reason.

*I’m going to die.*

It had only been a few days since Jopil’s brutal palm strike had left him with internal injuries. He had loudly told Jin Taekyung he was almost fully recovered, but in truth he needed at least two weeks of rest, no arguments.

“Huff… huff.”

He was soaked through, and his legs were shaking.

He would have fallen behind even if he had only been trying to keep up. Carrying the solidly built Jin Taekyung on his back was literally killing him.

*Ah, Mother. Father.*

Now he was even hallucinating his parents—who were alive and well—waving him over. The woman standing beside them was a face he often saw at the temple hall.

*Guanyin Bodhisattva?*

“Child. You’ve suffered enough. You may rest now.”

Her benevolent smile slowly eased Hyuk’s heart.

*Yeah. I’ve done enough. The squad leader collapses at the critical moment, and these bastards won’t even offer to carry him for me, whether I drop dead or not.*

*Fuck it. Whatever.*

Hyuk was just about to let go when—

“Whew… haaah.”

Warm breath slipped into his ear. He knew who it was without turning around. Tears of relief stung Hyuk’s eyes.

“Squad Leader!”

Jin Taekyung grinned and whispered,

“Candy in your ear.”[^1]

* * *

Clang! Clang!

“Kill them! Kill them!”

“Graaah!”

Blood and screams burst out on every side. A blood-soaked martial artist crawled on all fours between the corpses.

His still-youthful face was stained with pain and terror.

“Hnnh… hhhk…”

He tried to hold it back, but the crying kept breaking free. He had spent ten years grinding through martial arts with grim determination, and it had all been useless on a battlefield spraying blood.

The senior he had counted on was dead. So was the comrade who had been like a brother. Weapons poured in from every direction, splitting open bellies and hacking limbs apart.

“Mother… Mother…”

He called for her without end, and then his face went stiff.

Shunk—!

A spearhead had already sprouted from his chest.

His eyes flew wide for an instant, then the light went out of them. A wandering martial artist with a bandit’s beard pulled his rusty spear free and grinned.

“What’s a brat doing here?”

But even a wandering martial artist who had survived countless brushes with death could not dodge the blade that came flying at him a moment later.

Slice—

A silver line flashed, and the wandering martial artist’s head shot into the air.

A wandering martial artist killed a martial artist. Another martial artist killed the wandering martial artist.

Nameless men killed and died on every side, over and over.

That was what a battlefield was.

*Yes. This was what it was like.*

The Head Elder looked out over the battlefield, his face steeped in memory.

Eight Spring Gorge. A battleground that had occupied a single line in the history of the Great Faction War, decades ago. How many had died in that narrow gorge?

*I was young then, too.*

His body had been strong, and his heart had burned hot. It had been a time when that embarrassing character—chivalry—had still felt enormous.

But the Great Faction War had changed the Head Elder. He had grown tired of the endless fighting, and afraid of death.

*What good is a chivalrous warrior? Die, and you’re nothing but a ghost.*

That had been a sliver of enlightenment. In the end he had survived and become a hero, and after a long stretch of endurance he had reached this place.

Now it was time to reap the fruit.

The Head Elder turned his cunning old eyes on the man standing beside him.

*What a waste. Such a waste.*

Jin Wikyung was a remarkable talent. He was young, his martial arts were considerable, and above all he had the dignity and judgment a leader needed. He sometimes let himself be bound by sentiment, but perhaps because of that, he was deeply respected within the family.

*He’s more than capable of raising the family.*

If Jin Wikyung became the Family Head, and if his two younger brothers—each already distinguishing himself—stood firmly behind him…

The Head Elder caught himself and let out a short laugh.

What a bizarre thing to be thinking, this far along. Jin Taekyung would already have died and become a lonely ghost, at that.

“I’ve grown old.”

Jin Wikyung reacted to the quiet mutter.

“Did you say something?”

“Nothing of importance. Old men talk to themselves more. More to the point, how does it look to you, Lesser Family Head?”

“The battle is going in our favor, but…”

Jin Wikyung’s expression darkened slightly. They held the advantage in troop quality and terrain, but the casualties kept mounting.

There was no way he could watch members of his family die and feel at ease.

“Lesser Family Head. I understand how you feel, but do not act rashly.”

The Head Elder’s warning was stern.

“A leader must know when to step forward. The longer the battle drags on, the more impatient they become. That is the moment we have to seize.”

“The Mount Heng Sword Sect will soon throw its full strength at us.”

“They’ll put their Peak masters at the front. Their Sect Leader, Lee Cheonbaek, may even come himself.”

“Then everything will be decided.”

The Head Elder nodded.

“If you, I, and Wipeng hold off the enemy command, and arrows rain down from the cliffs, their morale will hit rock bottom.”

“It’s a shame we can’t use a fire attack. I resent the heavens.”

The narrow terrain of Eight Spring Gorge was perfect for fire, but the heavy snowfall from several days ago had left snowdrifts everywhere.

Even if the heavens had taken Jin Wikyung’s side, though, what he was hoping for would never have happened.

The men drawing their bows on the cliffs would obey the Head Elder.

“I resent the heavens as well.”

The Head Elder meant it.

The years of waiting had been too long. He resented the destiny that had only now arrived.

* * *

“Candy in your ear.”

“Squad Leader!”

“Was it sweet as a dream?”

“…Are you insane?”

The sight of Hyuk Mujin’s ugly face sent a rush of relief through me. The other reconnaissance squad members crowding in at the news that I was awake were no different.

“Squad Leader’s awake!”

“What happened? Are you all right?”

“Wasn’t he dead?”

I’d have to deal with the bastard who had just said that later. I memorized his face and name, then grinned at everyone.

“Been a while. You guys been well?”

“Huh?”

“What’s that supposed to mean?”

“Did he hit his head?”

“His head—check his head!”

Exactly the reaction I’d expected.

But it was also a greeting I’d genuinely wanted to give them at least once.

…Not that they didn’t treat me like a lunatic afterward.

“Anyway, that’s enough greeting. How long was I out?”

Hyuk dropped onto the ground with a thud and answered.

“Definitely more than an hour, and a little under two.”

I’d spent two weeks in reality, so the timing roughly lined up. I nodded and moved on.

“Was I breathing?”

“Why are you asking that all of a sudden? Seriously.”

“No time. Answer.”

“You were breathing, that’s why you woke up. Otherwise you’d be dead.”

Fair enough.

Apparently, logging in or logging out put the other side into a deathlike sleep.

*If I’d logged out before dealing with the assassins, there wouldn’t have been a body to come back to.*

I’d think about that later.

There was a more urgent problem.

“The main force?”

“We were already heading that way. We split two men off and sent them back to the family.”

“Good. How much farther?”

“At least another two hours.”

“Two hours…”

“Uh, Squad Leader. I’m sorry to say this, but… I think we have to consider the worst case.”

Hyuk Mujin and every member of the reconnaissance squad clamped their mouths shut. Nobody had to ask what the worst case meant.

*I’ve thought about it too.*

From what Gwak Jun had said right before he died, this betrayal had been planned down to the last detail for a long time.

But the plan had exactly one error.

*Me.*

The Head Elder had underestimated me.

No—maybe, in another way, he’d overestimated me. He’d sent dozens of First Rate masters just to kill me.

Even that hadn’t been enough. I had survived.

*He made a mistake.*

On top of that, when Gwak Jun first showed his true colors, he’d said they had to start moving soon if they wanted to make it on time.

Which meant…

“It’s not too late.”

I met each squad member’s eyes and spoke firmly.

“Don’t think about the worst case. I’ll change that outcome, no matter what it takes.”

“Squad Leader…”

“So, Mujin.”

I gave Hyuk’s choked-up face a good-natured smile.

“Get up. Now.”

“I’m dying here.”

“Want to get beaten to death instead?”

“…”

“Run even one more step in the time we’ve got. Don’t you know marathon spirit?”

“I don’t.”

Ah. Right. This was Murim.

“Anyway, get up. Another hour will do it.”

Hyuk grabbed his shaking legs and pushed himself up, then cocked his head.

“An hour?”

“Yeah. An hour.”

“I already told you. Even at full speed, it’s two hours.”

“Exactly. An hour.”

“What are you even saying…”

“Mujin.”

“Yes?”

Hyuk blinked at me, as simple as an ox. I smiled even brighter.

“You ever heard of grit?”

Two hours or four, I didn’t care.

We were getting there in an hour. Period.

“Run like hell. That’ll do it.”

“Huk.”

Every face in the reconnaissance squad went deathly pale.

* * *

“We’ve been blocked.”

“Casualties are heavy. Sect Leader, please take action.”

Even as the reports kept coming, Blood Wolf Sword Lee Cheonbaek, Sect Leader of the Mount Heng Sword Sect, did not open his eyes.

*I was too hasty.*

The war had started in a rush, and the preparations had been just as thin. Provisions were burning down fast, morale was dropping, and deserters were popping up one after another.

*They read us completely.*

Rage at losing his son and impatience with the situation had clouded his judgment. He had ignored his subordinates’ advice and taken the fastest route he could find.

And that was how he had run into the Jin Family of Taiyuan in a narrow gorge whose very name was unfamiliar: Eight Spring Gorge.

“Sect Leader!”

At his subordinate’s shout, Lee Cheonbaek slowly opened his eyes.

The fearsome vision of a Peak master pierced the battlefield.

“Gaaah!”

“Wipe them out! They’re nothing but rabble!”

Well over a thousand of his own men were jammed at the narrow mouth and couldn’t advance. The wandering martial artists and mounted bandits he’d put at the front had numbers, but man for man they were worse than even the Jin Family’s rank-and-file.

*Sword fodder, at best.*

Just as he was clicking his tongue, several dozen wandering martial artists suddenly started peeling off the front line. The middle-aged wanderer at their head bellowed until his throat tore.

“This is a dog’s death! Brothers of the Blood Rain Group, fall back!”

Those became the middle-aged wandering martial artist’s last words.

Whoosh—

A light breeze. The wandering martial artist felt nothing else.

He did not know that Blood Wolf Sword Lee Cheonbaek had already brushed past him. He did not know that the wandering martial artists under him had frozen in terror.

He only thought, suddenly, that his neck was hot.

“Uh…”

His cleanly severed head dropped with a dull thunk. The headless body staggered a few more steps, then went down like a rotten old tree.

“Blood Rain Group, was it?”

Lee Cheonbaek pointed his sword at the frozen wanderers. Not a drop of blood stained the blade.

“Go back.”

A Peak master’s killing intent shot into them like a blade. The wandering martial artists charged toward the front even faster than they had come.

They had decided that fighting at the front beat throwing themselves at the Peak master in front of them.

“Rat bastards.”

Lee Cheonbaek went after them. His burning gaze was aimed somewhere ahead, where the Jin Family of Taiyuan’s command had to be.

“The Sect Leader is taking the lead!”

“Everyone, charge! Wipe out the Jin Family of Taiyuan!”

With Lee Cheonbaek stepping forward, the Mount Heng Sword Sect’s core forces followed.

Three Peak masters and dozens of First Rate masters crashed toward the front.

[^1]: A Korean joke-whisper: mock ASMR, promising something sweet right in your ear.
```
## Chapter 56

### Korean source

```text
＃56화



이천백의 등장을 가장 먼저 알아차린 사람은 대장로였다.

‘머리가 직접 나섰군.’

협곡을 가로지르며 뿜어내는 강맹한 기파와 넘실거리는 살기. 눈으로 보지 않아도 알 수 있었다.

아니나 다를까.

“이놈들!”

천둥 같은 고함과 함께 이천백이 나타났다. 반백의 머리는 갈기처럼 휘날렸고 눈은 붉게 달아올라 있었다.

잇따라 항산검문의 핵심 전력이 도착했다. 일류 무인들과 세 명의 절정 고수!

“태원진가 놈들을 쓸어 버려라!”

“문주님이다! 문주님께서 오셨다!”

“우와아아!”

함성과 함께 식어 가던 전의가 타올랐다. 순식간에 트인 길을 따라 이천백이 쇄도했다.

“간악한 태원진가 놈들을 죽여라!”

그 모습을 가만히 지켜보고 있을 진위경이 아니었다.

“때가 되었습니다.”

대장로가 대답했다.

“동의하오.”

사실 그는 이천백의 등장이 달갑지 않았다. 어느 정도 소모전이 진행되어야 뒤처리가 편해진다.

하지만 현재 태원진가와 항산검문. 양 세력의 피해는 그리 크다고 할 수 없었다.

‘상관없겠지. 어차피 그들이 나설 테니.’

산서성의 패자를 자처하는 양대 세력이지만 ‘그들’의 힘에 비하면 하찮다.

과거 강성했던 시절에도 변방의 무가(武家) 취급밖에 받지 못하던 태원진가가 어찌 그들을 당해 낼 수 있을까.

‘일개 무가라…….’

씁쓸한 웃음을 삼킨 대장로가 검을 뽑아 들었다.

스르릉.

오랜 세월 두 자루의 검을 품었다. 하나는 가슴에, 하나는 허리춤에. 이제 더는 말이 필요 없었다.

“이천백은 내가 맡겠소.”

“그리하시지요.”

혈랑검 이천백이 누군가, 오로지 검 한 자루로 항산검문을 세우고 이제는 일성(一城)의 패자를 노리는 자다. 비록 적이지만 인정할 수밖에 없는 절정의 무인.

‘그와 겨뤄 보고 싶다.’

그러나 진위경은 끓는 피를 억눌렀다. 가문의 명운이 걸린 전투. 호승심은 접어야 한다.

“위팽.”

“예.”

어느새 예리한 협봉검을 빼 든 위팽이 진위경의 곁에 섰다.

“너와 내가 나머지를 맡는다.”

“받들겠습니다.”

한 치의 망설임도 없는 대답이다. 희미하게 웃은 진위경이 검을 뽑았다. 태원진가 대대로 내려져 오는 가문의 보검.

어느 날 홀연히 사라진 아버지가 남긴 유일한 물건이다.



중원 유람 좀 하고 오마.

그동안 너 써.



검집에 대충 끼워 넣어져 있던 서신의 내용을 떠올린 진위경은 새삼 피가 거꾸로 솟구쳤다.

‘중원 유람 같은 소리하네. 평생 실컷 놀아 놓고.’

가주라는 인간은 지금 어디서 뭘 하는지도 모르겠고, 수천 리 밖에 있는 둘째는 이제야 겨우 서신을 받았을 것이다.

‘내가 지켜야 한다.’

무인, 시비, 하인, 아이들.

지금은 다른 누구도 아닌 진위경이 태원진가의 가주다. 그들의 죽음도, 생존도 오롯이 그가 짊어져야만 했다.

‘반드시 승리한다.’

진위경이 눈을 부릅떴다. 검을 치켜든 그의 입에서 창룡후가 터져 나왔다.

“한 놈도 살려 보내지 마라!”

쉬쉬쉭!

태원진가의 고수들이 땅을 박차고 날아올랐다. 그것을 신호로 등 뒤에서 불화살 하나가 높게 솟구쳤다.

절벽 위에서 수십의 인영이 몸을 일으킨 것도 그때였다.

“쏴라!”

소낙비처럼 쏟아지는 화살 아래, 이 전투의 향방을 가를 고수들의 싸움이 시작되었다.



* * *



혈랑검 이천백은 타고난 무인이다.

무공에 대한 천부적인 재능과 야수 같은 감각으로 적들을 해치웠고, 자신의 야망을 차례차례 실현시켰다.

항산검문을 세우고, 인근 방파를 차례차례 흡수하며 힘을 길렀다. 장차 중원에서도 인정받는 세가(世家)의 초석을 다지고자 했다.



‘문주! 이 공자가…….’



그러던 어느 날, 둘째 아들이 주검으로 돌아왔다. 정당한 비무로 인한 것도 아니었다. 극독에 당해 칠공에서 피를 쏟아내며 죽었다.

이천백은 맹세했다. 태원진가와 연관된 것들은 모조리 죽이고 불태우기로.

그런 그의 눈앞에 진위경이 나타났다. 이천백의 눈에서 불길이 쏟아졌다.

“이노옴-!”

이천백이 야수처럼 뛰어들었다. 일 갑자에 달하는 공력을 머금은 검신이 우윳빛으로 빛났다.

이 힘이라면 어떤 갑옷도, 신병이기도 잘라 낼 수 있으리라.

‘놈은 반드시 죽는다!’

확신에 찬 이천백이 검을 휘두르려던 그 순간이었다.

“오호, 검기(劍氣)?”

뒤에서 들려온 나직한 목소리. 이천백의 가슴이 덜컥 내려앉았다.

‘어떻게?’

이토록 허무하게 뒤를 내주다니. 이천백의 반응은 섬전 같았다. 역수로 틀어쥔 검을 뒤로 찔러 넣었다.

쉭.

검신은 허공을 찔렀고, 이천백은 시간을 벌었다. 그제야 적의 얼굴을 확인할 수 있었다.

가슴께까지 늘어트린 수염, 입가에 맺힌 여유로운 미소.

백발의 노인이었다. 이천백은 단숨에 노인의 정체를 알아차렸다.

“화양검?”

대장로가 고개를 끄덕였다.

“오랜만에 듣는군. 그러는 자네는 이천백이겠지?”

“그렇소.”

이천백은 대답하는 지금도 등골이 서늘하다 느꼈다.

진위경이 어디 있는지, 전투가 어떻게 돌아가고 있는지 확인할 엄두도 나지 않았다. 눈을 떼면 금방이라도 목이 떨어질 것 같았다.

‘우연? 아니다.’

진위경을 보고 과하게 흥분한 건 맞다. 마음이 조급했던 것도 맞다. 하지만 이천백은 절정 고수였다.

그중에서도 검기상인의 경지에 오른 절정 고수.

이미 답은 나와 있었다.

‘고수!’

일 초식이건, 반 초식이건 눈앞의 노인은 이천백보다 윗줄의 고수였다. 이천백은 애검을 꽉 움켜잡았다.

“위명은 익히 들었소.”

“위명은 무슨. 뒷방 늙은이에 불과하네.”

“그럼 계속 뒷방에 있지, 뭣 하러 나온 거요?”

“아직 젊은 친구라 뭘 모르는군. 늙을수록 가끔 움직여 줘야 해.”

대장로의 능글맞은 태도에 이천백은 이를 갈았다.

‘망할 늙은이.’

그는 이미 오래전부터 태원진가의 동향을 살피고 있었다.

대장로를 중심으로 가주에게 맞서는 파벌이 있다는 것도 안다. 그래서 내심 태원진가의 내부 분열을 기대하기도 했다.

하지만 기대했던 상황은 정반대로 흘러갔다.

‘외적이 침입하면 한마음으로 뭉친다 이건가?’

무거운 눈으로 대장로를 응시하던 이천백의 입이 열렸다.

“당신은 얼마나 강하오?”

“자네가 믿는 만큼.”

“말장난이군.”

“화양검이라 불리던 시절 내 나이가 이립이었네.”

나이 서른에 대장로는 이미 절정의 무인이었다. 칠순의 노인이 된 지금, 그의 무공은 어떻게 변화했을까. 잠시 생각하던 이천백은 문득 실소를 머금었다.

‘나도 늙었군.’

혈랑검.

젊은 시절의 이천백은 거침없었다. 뛰어난 신공, 번듯한 스승 하나 없이 오로지 홀로 모든 것을 헤쳐 나갔다.

한 수 위의 상대를 만나도 그는 물러서지 않았다. 늑대처럼 달려들어 목을 물어뜯었다.

‘반평생을 그렇게 살았는데…….’

어느 순간부터 그는 혈랑검 대신 문주라고 불리기 시작했다.

혈육, 수하, 재물. 지켜야 할 것들이 산더미처럼 쌓여 갔다.

수련 대신 집무 시간이 늘었고, 행동해야 할 때 머리를 굴렸다. 지금처럼.

“왜 웃나?”

대장로의 물음에 이천백이 대답했다.

“나 자신이 한심해서 웃었소.”

“자네, 나를 무서워하는군.”

이천백이 묵묵히 고개를 끄덕였다.

“죽음이 두려웠나?”

“아주 잠깐은.”

“지금은 어떤가?”

“당신을 죽일 거요.”

“자네 정도로는 무리야.”

“길고 짧은 건 대봐야 하지 않겠소?”

“짧은 자들이 늘 하는 말이지. 막상 대봐도 결과는 변함없다는 사실을 몰라.”

“혀가 맵구려.”

“혀만 매울까.”

대장로는 검을 늘어트렸다. 별반 특별할 것 없어 보이는 청강검이었지만 그의 손에 들린 순간 지독한 예기를 뿜어내기 시작했다.

“먼저 오시게.”

이천백은 거절하지 않았다. 일 갑자의 공력을 빨아들인 검신이 빛의 아지랑이를 피워 올렸다.

수많은 무인들이 꿈꾸는 검기상인(劍氣霜刃)의 경지.

츠츠츠.

검기가 세 치(10cm)까지 솟구친 순간, 이천백의 신형이 쏘아졌다. 수많은 실전 끝에 완성한 독문 무공이 그의 손끝에서 펼쳐지고 있었다.

쉭, 쉬쉬쉬쉭!

콰아앙!

검기가 사방을 난도질했다. 순간적으로 솟아오른 흙더미 사이로 비명이 터져 나왔다.

“크아아악!”

간격에 휘말린 무인들이 내는 소리였다. 하나같이 젊은이의 목소리들. 이천백의 머릿속에 붉은 신호가 켜졌다.

‘뒤!’

이천백은 돌아섬과 동시에 검을 휘둘렀다. 바람에 나부끼는 흰 수염이 보였다. 그의 손에 들린 검도.

쾅!

‘큭.’

굉음과 함께 이천백이 정신없이 물러났다. 그에게는 손목의 통증을 느낄 틈도 주어지지 않았다.

쾅! 쾅! 쾅!

두 개의 검이 부딪칠 때마다 뇌성벽력이 울려 퍼진다.

줄줄이 뿜어져 나오는 검기가 땅을 부수고 바람을 찢었다.

쉬쉬슁!

“저게 도대체…….”

양 세력의 무인들은 싸우던 것도 잊었다. 그저 넋이 나간 얼굴로 이 엄청난 생사결을 바라봤다.

지금 이 순간만큼은 모두가 같은 생각을 하고 있었다.

‘저들이 우리와 같은 사람이란 말인가?’

쉴 새 없이 터지는 굉음과 보는 것만으로도 황홀해지는 검기의 향연. 그 중심에 선 두 사람의 움직임은 이제껏 본 그 누구보다 빠르고, 강했다.

누군가가 신음처럼 중얼거렸다.

“이게 절정 고수…….”

그들의 눈에는 누가 이겨도 이상하지 않은 싸움.

그러나 힘의 우위는 명백했다. 삼백여 합을 주고받았을 때, 대장로의 검이 변화를 보였다.

쉭, 서걱!

“크윽.”

이천백은 입술을 깨물었다. 대장로의 검이 훑고 지나간 팔뚝에서 피가 철철 흐르고 있었다.

검을 쥔 손에 힘이 스르륵 풀렸다.

‘하필이면.’

재빨리 검을 바꿔 잡았지만 그는 본래 우수검(右手劍)이다.

십 할의 전력을 쏟아부어도 모자랄 판에 검을 쓰는 팔을 다쳤으니 승부는 정해진 것이나 다름없었다.

쾅!

우드득.

단 일격에 손목이 꺾였다. 심각한 공력 소모로 약해진 검기로는 대장로를 당해 낼 수 없었다.

하지만 이천백은 포기하지 않았다.

‘아직, 아직 끝나지 않았다.’

이보다 더한 부상도 숱하게 겪었다. 이천백은 팔과 허리, 다리 힘을 이용해 검을 휘둘렀다.

아니, 휘두르려고 했다.

촤아악.

이번에는 무릎이다. 힘줄이 잘려 나간 무릎이 이천백의 의지와는 상관없이 스르륵 무너졌다.

그의 검이 허망하게 허공을 갈랐다.

푹. 푹푹푹.

옆구리, 어깨, 가슴.

번갯불이 전신을 쑤시고 베어 냈다. 강맹한 검기는 살과 뼈를 자르는 걸로도 모자라 내부를 진탕시켰다.

“우웨엑!”

내장 조각이 섞인 핏물을 토해 낸 이천백이 흐린 눈빛으로 대장로를 올려다봤다.

노인의 안색은 무덤덤했다. 상대를 쓰러트렸다는 희열도, 전쟁이 끝났다는 기쁨도 엿볼 수 없었다.

그에게는 이 모든 것들이 당연한 결과였다.

“쿨럭, 산서제일인이 눈앞에 있었구려.”

“천하제일이 아니라면 변방의 무부(武夫)에 불과하지. 나도, 자네도 그 정도 그릇은 아니야.”

“원하는 걸 말하시오. 내 목을 주겠소. 수하들을 항복시키고, 십 년이고 백 년이고 봉문 하겠소. 그러니…….”

“불가. 내가 원하는 건 멸문일세. 풀 한 포기 남겨 두지 않는 완전한 멸문.”

“어째서……!”

“그렇게 묻지 말게. 자네가 승리했다면 멸문하는 것은 본가가 되었을 테니.”

이천백은 핏발 선 눈동자로 대장로를 노려봤다.

당장이라도 저 주름진 목을 꺾어 버리고 싶다. 그러나 중상을 입은 그가 할 수 있는 일이라고는 목소리를 쥐어짜 내는 게 전부였다.

“태원진가. 네놈들이 시작하지 않았나. 그 어린 녀석을, 내 아들을 죽였어!”

“아, 이소군. 그렇지. 그 아이가 시작이었지.”

대장로는 고소를 머금었다.

산서성을 양분하는 항산검문의 주인조차 ‘그들’의 개입을 알아채지 못했다. 죽음이 목전에 다다른 지금까지도.

- 염라대왕을 만나면 물어보게. 이소군을 죽인 자가 누구인지.

귓가를 파고드는 전음(傳音)에 이천백이 눈을 부릅떴다.

“그게 무슨……!”

그건 다분히 충동적인 행동이었다. 아무것도 모른 채 죽게 될 이천백에 대한 연민일 수도 있고, 늙은이의 단순한 변덕일 수도 있다.

- 저승길 노잣돈일세. 먼 길 가는 동안 생각해 보게.

대장로는 검을 치켜세웠다. 겨울 산등성이 너머로 비춘 노을이 검신을 따라 산산이 부서졌다.

‘이것으로…….’

이천백이라는 거인의 죽음으로 항산검문은 무너진다.

저항하는 자는 죽고 항복하는 자는 사로잡힌다. 그렇게 하나의 전쟁이 끝나고…… 새로운 전쟁이 시작될 것이다.

모두가 승리에 취해 있는 그 순간에.

‘끝이다.’

마침내 대장로의 검이 움직였다.

쐐애애액-!

날카로운 파공성.

최후를 직감한 이천백은 눈을 감았다. 푸른 검기에 휩싸인 검신이 아름다운 선을 그었다.

서걱.

그러나 앞서 들린 파공성도, 검의 방향도 이천백의 예상을 벗어났다.

난데없이 등을 향해 날아온 창 한 자루를 검기로 갈라 낸 대장로의 입에서 창노한 음성이 터졌다.

“웬 놈이냐!”

다음 순간, 대답이 들려왔다.

“나다, 이 십새끼야!”

야트막한 언덕 위, 우뚝 서 있는 한 청년의 얼굴을 확인한 대장로가 신음했다.

“진태경?”
```

### Current accepted English

```markdown
# Chapter 56

The Head Elder was the first to notice Lee Cheonbaek’s arrival.

*The head himself has entered the fray.*

The fierce wave of qi blasting across the gorge, and the killing intent rolling with it, made that obvious even without seeing him.

Sure enough—

“You bastards!”

Lee Cheonbaek appeared with a thunderous roar. His half-gray hair whipped around like a mane, and his eyes burned red.

The Mount Heng Sword Sect’s core forces arrived on his heels. First Rate martial artists, and three Peak masters!

“Wipe out those Jin Family of Taiyuan bastards!”

“The Sect Leader is here! The Sect Leader has come!”

“Waaaah!”

The cheers rekindled the fighting spirit that had begun to fade. Lee Cheonbaek surged forward along the path that had opened in an instant.

“Kill those treacherous Jin Family of Taiyuan bastards!”

Jin Wikyung was not the kind of man to stand by and watch.

“The time has come.”

The Head Elder answered.

“I agree.”

In truth, he had not welcomed Lee Cheonbaek’s arrival. A certain amount of attrition would have made the cleanup easier.

But the losses on both sides—the Jin Family of Taiyuan and the Mount Heng Sword Sect—were still nothing to speak of.

*It doesn’t matter. They’ll be making their move anyway.*

The two great powers claimed to be the rulers of Shanxi, but compared to *them*, they were insignificant.

Even in its former heyday, the Jin Family of Taiyuan had been treated as nothing more than a martial family from the frontier. How could it possibly stand against them?

*A mere martial family…*

The Head Elder swallowed a bitter smile and drew his sword.

Shing.

For many years he had carried two swords. One at his chest, the other at his waist.

There was no need for more words.

“I’ll handle Lee Cheonbaek.”

“Please do.”

Who was Blood Wolf Sword Lee Cheonbaek? The man who had founded the Mount Heng Sword Sect with nothing but a single sword, and who now meant to become the ruler of an entire city. Enemy or not, there was no denying he was a Peak martial artist of the highest caliber.

*I want to fight him.*

But Jin Wikyung forced down the heat in his blood.

This was a battle with the family’s fate at stake. Competitive spirit had no place here.

“Wipeng.”

“Yes.”

Wipeng had already drawn his sharp, narrow blade and taken his place at Jin Wikyung’s side.

“You and I will handle the rest.”

“As you command.”

There was not a trace of hesitation in the answer. Jin Wikyung smiled faintly and drew his own sword—the family’s treasured blade, passed down through generations of the Jin Family of Taiyuan.

It was the only thing left behind by the father who had vanished one day without a trace.

*I’m going to travel around the Central Plains for a while.*

*Use this in the meantime.*

Remembering the letter that had been stuffed carelessly into the scabbard, Jin Wikyung felt his blood boil all over again.

*Travel around the Central Plains, my ass. You spent your whole life having fun.*

He didn’t even know where that so-called Family Head was, or what he was doing. And his second brother, thousands of li away, had probably only just received the letter.

*I have to protect them.*

Martial artists, maids, servants, children.

Jin Wikyung was the Family Head of the Jin Family of Taiyuan now. No one else.

Their deaths and their survival were his to carry, and his alone.

*We will win.*

Jin Wikyung’s eyes flared wide. Sword raised, an Azure Dragon’s Roar burst from his mouth.

“Don’t let a single one of them live!”

Whoosh, whoosh, whoosh!

The Jin Family’s masters kicked off the ground and leaped into the air. Taking that as the signal, a single fire arrow rose high behind them.

That was when dozens of figures stood up along the cliffs.

“Fire!”

Beneath arrows pouring down like a sudden rain, the fight between the masters who would decide the course of the battle began.

* * *

Blood Wolf Sword Lee Cheonbaek was a born martial artist.

With innate talent for martial arts and beastlike instincts, he had cut down his enemies and realized his ambitions one after another.

He had founded the Mount Heng Sword Sect and grown its strength by absorbing the surrounding factions one by one. His aim was to lay the foundation for a prestigious house that would one day be recognized even in the Central Plains.

*Sect Leader! The Young Master…*

Then, one day, his second son came home a corpse.

It had not been a fair duel. Deadly poison had taken him, and he had died with blood pouring from all seven orifices.

Lee Cheonbaek swore an oath.

He would kill and burn everything connected to the Jin Family of Taiyuan.

And then Jin Wikyung appeared before his eyes.

Lee Cheonbaek’s eyes blazed.

“You bastard—!”

He charged like a beast. The blade, holding sixty years of internal energy, shone milky white.

With this much power, it could cut through any armor, any divine weapon.

*That bastard dies here!*

Just as Lee Cheonbaek, sure of it, was about to swing—

“Oho. Sword Energy?”

A low voice, from behind him.

Lee Cheonbaek’s heart sank.

*How?*

To give up his back so cheaply. His reaction was lightning-fast. He drove the sword backward in a reverse grip.

Whoosh.

The blade stabbed empty air, and that bought him time. Only then could he see his opponent’s face.

A beard hanging down to his chest. A relaxed smile at the corners of his mouth.

A white-haired old man.

Lee Cheonbaek knew him at once.

“Blade of Flowers?”

The Head Elder nodded.

“I haven’t heard that name in a long time. Then you must be Lee Cheonbaek.”

“That’s right.”

Even as he answered, a chill ran down Lee Cheonbaek’s spine.

He didn’t dare look for Jin Wikyung, or check how the battle was going. Take his eyes off the old man, and he felt his head would come off on the spot.

*Coincidence? No.*

It was true that seeing Jin Wikyung had agitated him past reason. It was true that he had been impatient.

But Lee Cheonbaek was a Peak master.

A Peak master who had reached the realm of Sword Energy Frost Blade.

The answer was already clear.

*A master!*

Whether in one form or half a form, the old man in front of him was a master a league above Lee Cheonbaek.

Lee Cheonbaek tightened his grip on his beloved sword.

“I’ve heard much of your reputation.”

“Reputation? I’m nothing more than an old man in the back room.”

“Then why leave the back room?”

“You’re still a young fellow, so there’s a lot you don’t know. The older you get, the more you have to get moving now and then.”

Lee Cheonbaek ground his teeth at the Head Elder’s sly manner.

*Damn old man.*

He had been watching the Jin Family of Taiyuan for a long time.

He knew there was a faction centered on the Head Elder that opposed the Family Head. He had even privately hoped the family would split from within.

But things had gone the opposite of what he had expected.

*So when an outside enemy invades, they unite as one?*

Lee Cheonbaek stared at the Head Elder with heavy eyes, then opened his mouth.

“How strong are you?”

“As strong as you believe me to be.”

“Word games.”

“When I was called Blade of Flowers, I was thirty.”

At thirty, the Head Elder had already been a Peak martial artist.

Now he was a man of seventy. How had his martial arts changed since then?

After a moment’s thought, Lee Cheonbaek let out a wry laugh.

*I’m getting old, too.*

Blood Wolf Sword.

In his youth, Lee Cheonbaek had been unstoppable. Without an exceptional martial art or a respectable master, he had carved his way through everything on his own.

Even against an opponent a level above him, he never backed down. He charged like a wolf and tore out their throats.

*I lived half my life that way…*

At some point, people had started calling him Sect Leader instead of Blood Wolf Sword.

Blood relatives, subordinates, wealth.

The things he had to protect had piled up like a mountain.

Time spent training shrank; time spent on affairs grew. When it was time to act, he started thinking instead.

Just as he was now.

“Why are you laughing?”

Lee Cheonbaek answered the Head Elder’s question.

“I’m laughing because I find myself pathetic.”

“You’re afraid of me.”

Lee Cheonbaek nodded in silence.

“Were you afraid of death?”

“For a very brief moment.”

“And now?”

“I’m going to kill you.”

“Someone of your level won’t manage it.”

“You have to measure them to know which is longer, don’t you?”

“That’s what the short ones always say. They never realize that even after you measure, the result doesn’t change.”

“Your tongue is sharp.”

“Is it only my tongue?”

The Head Elder lowered his sword.

It looked like an ordinary blue-steel sword, but the moment it entered his hand, it began to give off a vicious killing edge.

“Come at me first.”

Lee Cheonbaek did not refuse.

The blade, having drawn in sixty years of internal energy, raised a shimmering haze of light.

The realm of Sword Energy Frost Blade—a realm countless martial artists dreamed of reaching.

Tssss.

The moment the Sword Energy rose three inches—about ten centimeters—Lee Cheonbaek’s body shot forward.

A unique martial art, perfected through countless real battles, unfolded from his fingertips.

Whoosh! Whoosh-whoosh-whoosh!

Boom!

Sword Energy hacked wildly in every direction. Screams burst from between the mounds of earth that erupted in an instant.

“Graaagh!”

They were the cries of martial artists caught in the gap.

Every voice was a young man’s.

A red warning light went on in Lee Cheonbaek’s mind.

*Behind!*

He spun and swung at the same time.

He saw the white beard fluttering in the wind.

And the sword in the old man’s hand.

Boom!

*Kh.*

Lee Cheonbaek fell back in a daze amid the thunderous crash. He was not even given time to feel the pain in his wrist.

Boom! Boom! Boom!

Every time the two swords met, thunder and lightning rolled.

Sword Energy poured out in a continuous stream, smashing the ground and tearing the wind.

Whoosh!

“What in the world is that…?”

The martial artists of both sides forgot they were fighting. They could only stare, slack-faced, at this staggering life-and-death duel.

In that moment, every one of them was thinking the same thing.

*Are those two really human beings like us?*

The ceaseless thunder. A feast of Sword Energy so dazzling it left them spellbound just to watch.

The movements of the two men at its center were faster and stronger than anyone they had ever seen.

Someone muttered, almost a groan.

“So this is a Peak master…”

To their eyes, it was a fight where either outcome would have made sense.

But the superiority in strength was obvious.

After some three hundred exchanges, the Head Elder’s sword changed.

Whoosh—slice!

“Ghk.”

Lee Cheonbaek bit down on his lip.

Blood streamed from the forearm the Head Elder’s sword had raked.

The strength drained from the hand on his sword.

*Of all things.*

He shifted the sword to his other hand at once, but he was a right-handed swordsman by nature.

Even at full power he would have been hard-pressed. Now that the arm he used to wield a sword was injured, the outcome was all but decided.

Boom!

Crack.

A single blow snapped his wrist.

His Sword Energy, weakened by the severe drain on his internal energy, could no longer stand against the Head Elder.

But Lee Cheonbaek did not give up.

*Not yet. It isn’t over yet.*

He had taken worse injuries than this, plenty of times.

Using the strength in his arm, his waist, his legs, Lee Cheonbaek swung his sword.

No—he tried to.

Slash!

This time, it was the knee.

The tendons had been cut, and the knee buckled slowly, with no regard for Lee Cheonbaek’s will.

His sword carved uselessly through empty air.

Shhk. Shhk-shhk-shhk.

His side. His shoulder. His chest.

Lightning stabbed and sliced through his whole body. The fierce Sword Energy did more than cut flesh and bone—it churned his insides.

“Bleeegh!”

Lee Cheonbaek vomited blood mixed with pieces of organ and looked up at the Head Elder through clouded eyes.

The old man’s face was impassive.

No joy at having put his opponent down. No delight that the war was ending.

To him, all of this was simply the natural result.

“Cough… So Shanxi’s Number One was standing right in front of me.”

“If you’re not Number One Under Heaven, you’re nothing more than a martial brute from the frontier. Neither you nor I have that kind of capacity.”

“Tell me what you want. I’ll give you my neck. I’ll make my men surrender, and I’ll seal the sect for ten years—or a hundred. So…”

“Impossible. What I want is annihilation. Complete annihilation, without a single blade of grass left standing.”

“Why…!”

“Don’t ask me that. If you had won, it would have been this family facing annihilation.”

Lee Cheonbaek glared at the Head Elder with bloodshot eyes.

He wanted to snap that wrinkled neck then and there.

But in his condition, all a man with wounds like his could do was wring out a voice.

“Jin Family of Taiyuan. You started this, didn’t you? You killed that boy—my son!”

“Ah, Lee Seogeun. That’s right. That child was where it began.”

The Head Elder wore a sardonic smile.

Even the master of the Mount Heng Sword Sect, one of the two powers splitting Shanxi between them, had failed to notice *their* intervention.

Not even with death at his doorstep.

—When you meet King Yama, ask him. Ask who killed Lee Seogeun.

The Sound Transmission burrowing into his ear made Lee Cheonbaek’s eyes flare wide.

“What does that mean…?”

It had been a thoroughly impulsive act.

Perhaps pity for Lee Cheonbaek, who was about to die knowing nothing.

Or perhaps nothing more than an old man’s whim.

—Fare for the road to the afterlife. Think it over on the long journey.

The Head Elder raised his sword.

The sunset beyond the winter ridge shattered into fragments along the blade.

*With this…*

With the death of the giant called Lee Cheonbaek, the Mount Heng Sword Sect would collapse.

Those who resisted would die. Those who surrendered would be taken.

One war would end like that…

And a new war would begin, at the very moment everyone was drunk on victory.

*It’s over.*

At last, the Head Elder’s sword moved.

Screeeech—!

A sharp sound tore the air.

Sensing the end, Lee Cheonbaek closed his eyes.

The blade, wrapped in blue Sword Energy, traced a beautiful line.

Slice.

But the tearing sound that had come first, and the direction of the sword, were both beyond Lee Cheonbaek’s expectations.

The Head Elder split a spear that came flying at his back out of nowhere, cutting it apart with Sword Energy.

An enraged roar burst from his mouth.

“Who the hell are you!”

The answer came the next instant.

“It’s me, you fucking bastard!”

The Head Elder saw the face of a young man standing tall on a low hill, and groaned.

“Jin Taekyung?”
```
## Chapter 57

### Korean source

```text
＃57화



“빨리, 더 빨리!”

“헉, 허억!”

우리는 그야말로 미친 듯이 달렸다. 혁무진은 당장 죽을 것처럼 헐떡거렸지만 죽지는 않았다. 발걸음이 느려질 때마다 등에 창날을 가져다 댔더니 적토마가 따로 없더라.

그리고 어느 순간, 소리가 들리기 시작했다.

누군가의 비명 소리, 철과 철이 부딪치는 소리…….

다행이다. 전투는 아직 끝나지 않았다.

안도감과 동시에 심장이 쿵쿵 뛰었다. 전투는 계속되고 있지만 진위경의 생사는 아직 확인하지 못했다.

일 분, 일 초 차이로 그가 죽는다면?

‘만약 그렇다면.’

까드득.

나도 모르게 창을 쥔 손에 힘이 들어갔다. 단전에서 끌어올린 공력을 두 다리로 흘려보냈다.

“조, 조장!”

빠르게 멀어져 가는 정찰조원들의 목소리를 뒤로하고 계속해서 달렸다. 앞서 본대가 새겨 놓은 무수한 족적, 점점 가까워지는 전장의 소음이 이정표였다.

‘살아 있어라. 살아 있어라. 제발 살아…….’

아! 비로소 보인다.

야트막한 언덕 아래, 불과 200여 미터도 떨어지지 않은 그곳에서 수많은 무인들이 죽고 죽이는 혈전을 벌이고 있었다.

“죽엇!”

“으아악!”

시체와 피, 그리고 더 많은 시체, 피!

순간 할 말을 잃을 정도로 눈앞에 펼쳐진 광경은 잔혹했다.

헌터 생활을 통해 내성을 기르지 않았다면 아마 한참 동안이나 충격에서 헤어 나오지 못했을 것이다.

‘진위경! 진위경은 어디 있지?’

하지만 가장 먼저 눈에 들어온 사람은 따로 있었다.

멀리서도 한눈에 들어오는 백발.

‘대장로!’

그는 검을 들고 누군가의 앞에 서 있었다.

대장로의 등에 가려 잘 보이지는 않았지만 무릎을 꿇은 그는 거구의 소유자였고, 손에는 검을 쥔 채였다.

‘큰 덩치와 검?’

한 사람밖에 생각나지 않았다.

진위경이다. 그를 구하려면 당장 움직여야 한다.

‘인벤토리 오픈.’

무림에서 사용하는 인벤토리에는 온갖 물건으로 가득했다.

창대는 나무로, 창두는 강철로 만들어진 이 창도 그중 하나다.

‘무기 장착.’

새로 꺼낸 창을 들고 뒤로 몇 걸음 물러났다.

200여 미터. 까마득한 거리다. 투창으로 누군가를 맞추기에는 더더욱. 하지만 해내야 한다.

‘못 할 것도 없지.’

근력, 체력, 민첩.

무림과 현실을 오가며 키워 온 능력치를 한껏 끌어 올렸다.

공력이 깃든 팔은 창을 좀 더 멀리, 강하게 쏘아 보낼 수 있을 것이다.

“후웁.”

숨을 멈추고 발을 디뎠다. 첫발은 천천히, 마지막 한 걸음은 무겁게. 채찍처럼 휘두른 손끝에서 창대가 쏘아졌다.

쐐애애액-!

투창은 내 예상보다 빠르고 정확했다. 금방이라도 대장로의 등을 꿰뚫을 것 같았다.

그런데…….

서걱.

‘뭐야, 저거.’

푸른빛이 번쩍하더니 창이 두 쪽으로 갈라졌다. 가장 윗부분인 창두부터 끝까지, 깔끔하게.

내가 던진 게 창인지 생일 케이크인지 헷갈릴 정도다.

“웬 놈이냐!”

노인네가 목청도 좋다.

“나다, 이 십새끼야!”

아마 대장로 평생 들어 본 적 없는 욕일 것이다.

심지어 무림에서 그와 나는 한 집안 사람이고, 족보로 따지자면 시조새와 병아리 정도의 항렬 차이가 있다.

이것만 해도 당황할 이유는 충분한데, 내게는 결정적인 한 방이 남아 있었다.

“대장로는!”

공력이 담긴 목소리가 쩌렁쩌렁 울렸다. 목소리를 낸 나도 놀랄 정도인데 다른 이들이 듣기에는 어떨까.

저 멀리, 차가운 표정으로 굳은 그를 응시하며 있는 힘껏 외쳤다.

“배신자다!”



* * *



진위경이 그 목소리를 들은 것은 항산검문의 절정 고수 세 명을 모두 쓰러트린 직후였다.

아니, 진위경뿐만 아니라 전장의 모두가 그 외침을 들었다.

- 웬 놈이냐!

- 나다, 이 십새끼야!

욕?

전장에서는 흔한 일이다. 그러나 욕설의 대상이 대장로라면, 난데없이 나타나 쌍욕을 퍼부은 청년이 진태경이라면 이야기가 달라진다.

“저거, 저거 삼공자 아냐?”

“뭣? 저놈이 진태경? 그런데 왜?”

“이게 무슨 일이야?”

진위경도 같은 생각을 했다.

‘무슨 일이 벌어지고 있는 거지?’

후방에 있어야 할 막내가 전장에 나타났다. 그것만으로도 당황스러운데, 가문의 웃어른에게 입에 담지도 못할 폭언을 쓰기까지 했다. 옆에 있던 위팽이 중얼거렸다.

“단단히 미쳤군.”

진위경이 저도 모르게 고개를 끄덕이려던 순간.

- 대장로는!

더 거대한 폭탄이 떨어졌다.

- 배신자다!

전장이 싸늘한 침묵에 잠겼다. 간간이 들려오던 병장기 부딪치는 소리도 뚝 끊겼다.

모두가 멍한 표정으로 진태경을 바라봤다.

‘이게 무슨 개소리야?’

‘배신? 대장로님께서?’

‘취한 거 아냐? 삼공자 저거 옛날 버릇 또 튀어나오네.’

태원진가의 무사는 말할 것도 없었고, 항산검문의 무사들도 비슷한 생각을 품었다.

최근 들어 진태경을 좋게 보기 시작한 중진들도 입을 딱 벌렸다.

“저런 미친놈.”

“노야께서 어떤 분이신 줄 알고!”

이 전쟁의 일등 공신을 꼽으라면 단연 대장로다.

진위경을 도와 가문의 힘을 결집시켰고 오늘 전투에서는 이천백을 꺾었다.

이처럼 이번 전쟁의 단순한 공(公)을 떠나 생각해 봐도 진태경의 말은 헛소리로 들릴 수밖에 없었다.

대장로가 누군가?

화양검이라 불리며 중원에까지 이름을 떨친 전대의 고수요, 정마대전에서 수많은 마두를 쓰러트린 의기의 표상이다.

산서성의 무인이라면 누구나 그에게 크고 작은 존경심을 품고 있었다.

“그런 분을, 뭐? 십새끼? 배신자?”

“허어, 저놈이 태원진가 삼백 년 역사에 똥칠을 하는구나.”

태원진가, 항산검문. 이 자리의 모두가 같은 생각을 품은 듯했다. 그러나 적어도 한 사람은 예외였다.

‘대장로, 배신.’

막내의 말을 들은 순간, 진위경은 온몸의 피가 싸늘하게 식는 것을 느꼈다. 그건 실체를 드러낸 위화감이었다.

‘이소군의 죽음이 시작이었지.’

그는 극독에 중독되어 죽었다. 항산검문은 태원진가를 범인으로 지목했고, 그것이 전쟁의 시발점이다.

하지만 가장 중요한 의문은 빠져 있었다.

‘흉수는 누구인가?’

전쟁이 막바지에 이른 지금까지도 배후에 숨겨진 흉수에 대해서는 밝혀지지 않았다. 아니, 막바지에 다다랐기 때문에 아무도 흉수의 정체를 신경 쓰지 않았다.

적자생존. 강한 자가 살아남아 모든 것을 독식할 테니까.

‘이 전쟁은…… 처음부터 잘못된 거였어.’

이소군의 죽음. 비상식적으로 빠른 소문의 확산.

항산검문이 전쟁을 선언했고, 태원진가가 대응하면서 본격적인 싸움이 시작되었다.

‘그리고 대장로가 있었다.’

두문불출하던 대장로가 나타난 것은 이소군의 독살 소식이 전해진 직후다. 가문 내에서 그의 역할은 지대했다.

존경받는 무인, 가문의 웃어른.

대장로가 적극 협조하지 않았다면 태원진가는 둘로 갈라졌을지도 모른다.

‘그의 도움 덕분에 여기까지 올 수 있었다.’

진위경은 반대로 생각했다.

‘여기까지 올 수 있었던 것은, 대장로가 원했기 때문이다.’

촌각(寸刻)이라 부르지도 못할 만큼 짧은 순간. 모든 생각을 끝마친 진위경의 입이 열렸다.

“위팽.”

“하명하십시오.”

“일장로를 베어라.”

“뭐라?”

허리가 구부정하고 깡마른 노인, 일장로가 눈을 부릅떴다.

그뿐만 아니라 주위에 있던 중진들 모두가 깜짝 놀랐다.

“소, 소가주!”

“이 무슨……!”

그러나 위팽은 망설이지 않았다. 부지불식간에 휘두른 검이 일장로의 가슴을 향해 날아갔다.

카가가각.

그때 갑자기 끼어든 두 개의 검이 위팽의 검을 밀어 냈다.

뚱뚱하고 키가 훌쩍 큰 두 명의 노인.

일장로와 함께 대장로의 수족을 자처하는 이, 삼장로였다.

그들의 검에 맺힌 희미한 검기를 확인한 위팽의 눈썹이 꿈틀거렸다.

“무공을 숨겼군.”

대답 대신 일장로의 일권(一拳)이 날아왔다.

쾅!

살아온 세월만큼이나 심후한 공력으로 위팽을 날려 보낸 일장로가 허리를 곧게 폈다.

평생을 대장로의 그늘에 가려져 있었던 또 다른 절정 고수의 등장에 장내가 얼어붙었다.

“일장로님, 이, 이게 도대체.”

“그럼 혹시!”

배신. 그 두 글자가 모두의 뇌리에 선명하게 박혔다.

“말도 안 되는 소리!”

빽 소리친 사람은 백호당주였다. 대장로의 수족이 장로들이라면 그는 일장로의 손발 노릇을 톡톡히 해냈다.

“어르신, 그리고 소가주. 뭔가 오해가 있으신 모양인데…….”

그러나 그의 말은 끝까지 이어지지 못했다. 일장로의 턱짓과 동시에 이장로가 눈부신 속도로 백호당주의 목을 베었기 때문이었다.

서걱. 툭.

진위경과 일장로의 시선이 허공에서 부딪쳤다.

“백호당주도 포섭한 게 아니었나?”

“시끄러운 놈이었네. 그뿐이야. 다른 놈들도 마찬가지고.”

진위경의 예상은 반은 맞고 반은 틀렸다.

장로들이 배신한 것은 맞지만, 장로파에 속한 중진들은 배신하지 않았다.

“그럼 왜…… 아!”

“영민하군. 칭찬해 줌세.”

일장로가 품에서 거무튀튀한 죽통(竹筒)을 꺼내 들었다. 이미 타들어 가고 있는 심지가 얼마 남지 않았다.

“저런 놈들에게 중요한 비밀을 말해 줄 수야 있나. 내부만 혼란스럽게 만들어도 쓰임새는 다한 거지. 밖에서 무슨 일이 벌어지는지 몰라야 일이 편했으니까.”

진위경이 비명처럼 외쳤다.

“막아!”

“늦었네.”

일장로의 말이 맞았다. 심지가 끝까지 타들어 간 순간, 무언가 터지는 소리와 함께 붉은 불꽃이 하늘 높이 솟구쳤다.

쉬이익, 펑!

그것이 신호였다.

세 개의 문파 연합체인 삼도문, 도를 중심으로 수련하는 벽도문, 절벽에서 쉴 새 없이 화살을 쏘아 대던 궁귀문까지.

이른바 산서오문이라 불리는 중소 문파의 무인들이 한순간에 돌변했다.

“닥치는 대로 죽여라!”

“가릴 것 없다! 모두 쓸어 버려라!”

그들은 더 이상 어설픈 삼류 무인들이 아니었다. 눈에서는 살기가 흘렀고 검로는 날카로웠다.

‘하루아침에 준비한 일이 아니다.’

진위경의 얼굴이 딱딱하게 굳었다.



* * *



펑!

대장로는 고개를 들어 하늘을 바라보았다. 붉은 불꽃이 사그라지기도 전에 사방에서 거대한 함성이 터져 나왔다.

‘빠르군. 너무 빨라.’

신호를 터트리는 순간은 항산검문이 괴멸한 뒤가 되어야 했다. 산서오문은 수십 년 동안 준비한 칼이다. 단 한 번 휘둘러 전광석화처럼 끝내야 했다.

‘모든 일에는 흐름이 있는 법이거늘.’

막힘없이 흘러가던 계획이 어긋나기 시작했다. 씁쓸하게 웃는 대장로의 귓가로 한 줄기 음성이 파고들었다.

“네, 네놈이었구나.”

이천백이다. 희미한 목소리였지만 눈은 어느 때보다도 맹렬하게 타오르고 있었다.

“아직도 말할 기운이 남아 있나?”

“네놈을 산채로 갈기갈기 찢어 죽일 것이다.”

그러나 말을 마치기가 무섭게 이천백의 입에서 핏물이 쏟아졌다. 대장로가 그의 혈도를 짚으며 중얼거렸다.

“아직은 곤란하네. 자네가 해야 할 일이 있거든.”

이천백은 절망했다.

큰 손실이 있었다고는 하나 아직 항산검문에는 수백의 무인이 남아 있다. 수뇌부까지 괴멸한 이 시점에서 문주가 포로로 잡힌다면…….

‘차라리 죽여라!’

비통한 외침은 입 밖으로 새어 나오지 못했다. 아혈(啞穴)이 짚여 말을 할 수 없게 되었고, 이어 대장로의 손이 마혈(痲穴)을 스치자 몸이 딱딱하게 굳었다.

이천백이 눈 뜬 산송장이 된 순간이었다.

“이 새끼야! 거기 손 안 떼!”

동시에 파공성이 일었다.

쐐애애액-!

대장로는 당황하지 않고 검을 아래에서 위로 그어 올렸다. 검기를 따라 반으로 갈라지는 창 너머, 진태경이 무서운 속도로 달려오고 있었다.

“이야아아아!”

“조장! 제발 천천히 좀!”

어디서 나타났는지 모를 십여 명의 떨거지들과 함께.
```

### Current accepted English

```markdown
# Chapter 57

“Faster! Faster!”

“Huff… huff!”

We ran like mad. Hyuk Mujin was panting like he was about to drop dead, but he didn’t. Whenever his steps started to slow, I put the spearhead to his back, and he might as well have been Red Hare.[^1]

Then, at some point, the sounds started to reach us.

Someone’s screams. Steel ringing on steel…

Good. The battle wasn’t over yet.

Relief hit me, and my heart hammered at the same time. The fighting was still going on, but I still hadn’t confirmed whether Jin Wikyung was alive or dead.

What if he died because we were a minute—or even a second—too late?

*If that happens…*

Crack.

I tightened my grip on the spear without realizing it. I drew internal energy up from my dantian and sent it flowing through both legs.

“S-Squad Leader!”

I kept running, leaving the reconnaissance squad’s voices fading behind me. The countless tracks the main force had left, and the growing noise of the battlefield, were my landmarks.

*Stay alive. Stay alive. Please, stay—*

Ah. I could see it at last.

Below a low hill, not even two hundred meters away, countless martial artists were locked in a bloodbath, killing and being killed.

“Die!”

“Gaaah!”

Corpses and blood—and more corpses, more blood!

The sight in front of me was so brutal I was momentarily speechless.

If I hadn’t built up a tolerance from my life as a Hunter, I probably wouldn’t have been able to pull myself out of the shock for a long time.

*Jin Wikyung! Where is Jin Wikyung?*

But someone else caught my eye first.

White hair you could pick out at a glance even from far away.

*The Head Elder!*

He stood in front of someone, sword in hand.

Hidden behind the Head Elder’s back, the kneeling man was hard to see, but he was huge, and he had a sword in his hand.

*A big guy with a sword?*

Only one person came to mind.

Jin Wikyung. If I wanted to save him, I had to move now.

*Open Inventory.*

The Inventory I used in Murim was packed with all kinds of things.

This spear was one of them. Its shaft was wood, its head steel.

*Equip Weapon.*

I took the spear and stepped back a few paces.

Two hundred meters. Impossibly far. Even more so if I was trying to hit someone with a thrown spear.

But I had to do it.

*It’s not like I can’t.*

Strength, Stamina, Agility.

I pushed the stats I’d built up going back and forth between Murim and reality as far as they would go.

With internal energy in my arm, I could send the spear farther and harder.

“Hup.”

I held my breath and stepped in. The first step was slow. The last was heavy. I whipped my arm, and the spear shot from my fingertips.

Fwoooosh!

The throw was faster and more accurate than I’d expected. It looked like it would punch straight through the Head Elder’s back.

But then…

Shhk.

*What the hell was that?*

A flash of blue light, and the spear split in two. From the spearhead at the very top all the way to the end, a clean cut.

For a moment I couldn’t tell whether I’d thrown a spear or a birthday cake.

“Who the hell are you?”

The old man had quite a set of lungs.

“It’s me, you son of a bitch!”

It was probably a curse the Head Elder had never heard in his life.

On top of that, he and I were members of the same family in Murim. If you went by the genealogy, the generation gap between us was about an archaeopteryx and a chick.

That alone was plenty of reason to be stunned. But I still had one finishing blow left.

“The Head Elder is—!”

My voice, loaded with internal energy, thundered across the battlefield. Even I was surprised by how loud it was. I could only imagine what it sounded like to everyone else.

I stared at his frozen, cold face in the distance and shouted with everything I had.

“A traitor!”

* * *

Jin Wikyung heard the voice right after bringing down all three Peak masters of the Mount Heng Sword Sect.

No—not only him. Everyone on the battlefield heard that shout.

“Who the hell are you?”

“It’s me, you son of a bitch!”

Cursing?

That was common enough on a battlefield. But if the target of the abuse was the Head Elder, and the young man who had appeared out of nowhere to dump a double helping of it was Jin Taekyung, then it was a completely different matter.

“Isn’t that… isn’t that the Third Young Master?”

“What? That’s Jin Taekyung? But why?”

“What’s going on?”

Jin Wikyung was thinking the same thing.

*What in the world is happening?*

His youngest brother, who was supposed to be in the rear, had appeared on the battlefield. That alone was shocking enough, and on top of it he had hurled language unfit to repeat at one of the family’s elders.

Wipeng, standing beside him, muttered,

“He’s completely lost it.”

Jin Wikyung was just about to nod without realizing it when—

“The Head Elder is—!”

An even bigger bomb dropped.

“A traitor!”

The battlefield sank into an icy silence. Even the occasional clash of weapons cut off cold.

Everyone stared blankly at Jin Taekyung.

*What kind of bullshit is this?*

*Betrayal? The Head Elder?*

*Is he drunk? The Third Young Master’s old habits must be coming back.*

Needless to say, the martial artists of the Jin Family of Taiyuan thought so. The martial artists of the Mount Heng Sword Sect were much the same.

Even the senior members who had recently begun to look favorably on Jin Taekyung stood there with their mouths hanging open.

“What a madman.”

“Does he even know who the old master is?”

If they had to name the person who had contributed most to this war, it was, without question, the Head Elder.

He had helped Jin Wikyung gather the family’s strength, and in today’s battle he had defeated Lee Cheonbaek.

Even setting aside his merits in this war, Jin Taekyung’s words could only sound like nonsense.

Who was the Head Elder?

He was a master of the previous generation, famous even in the Central Plains as the Blade of Flowers, a symbol of righteousness who had struck down countless demonic masters during the Great Faction War.

Every martial artist in Shanxi held him in some degree of respect.

“That man? A son of a bitch? A traitor?”

“Good heavens. That boy is smearing shit on three hundred years of the Jin Family of Taiyuan’s history.”

The Jin Family of Taiyuan, the Mount Heng Sword Sect—everyone here seemed to share the same thought. But there was at least one exception.

*The Head Elder. Betrayal.*

The instant he heard his youngest brother’s words, Jin Wikyung felt the blood in his entire body run cold. It was a sense of wrongness, finally showing its true shape.

*Lee Seogeun’s death was where it began.*

He had died poisoned by a lethal toxin. The Mount Heng Sword Sect had named the Jin Family of Taiyuan as the culprit, and that had been the spark that started the war.

But the most important question had been left unanswered.

*Who was the murderer?*

Even now, with the war nearing its end, the killer hiding behind it all had never been identified. No—because the war was nearing its end, no one cared about the murderer’s identity anymore.

Survival of the fittest. The strong would live and take everything.

*This war… was wrong from the very beginning.*

Lee Seogeun’s death.

The unnaturally rapid spread of the rumors.

The Mount Heng Sword Sect had declared war, and the Jin Family of Taiyuan had answered. That was how the real fighting had begun.

*And the Head Elder had been there.*

The Head Elder, who had never left seclusion, had appeared immediately after news of Lee Seogeun’s poisoning reached the family. His role within the family had been enormous.

A respected martial artist. One of the family’s senior elders.

If the Head Elder had not cooperated so actively, the Jin Family of Taiyuan might have split in two.

*We were able to come this far because of his help.*

Jin Wikyung thought the opposite.

*We were able to come this far because this was what the Head Elder wanted.*

A span too short even to call an instant. When Jin Wikyung finished the thought, he opened his mouth.

“Wipeng.”

“Your orders.”

“Cut down the First Elder.”

“What?”

The stooped, emaciated old man—the First Elder—opened his eyes wide.

The senior members standing nearby were just as shocked.

“L-Lesser Family Head!”

“What in the world…!”

But Wipeng did not hesitate. Before anyone knew it, his sword was flying toward the First Elder’s chest.

Clang-clang-clang!

Two swords cut in out of nowhere and knocked Wipeng’s blade aside.

Two fat, exceptionally tall old men.

They were the Second and Third Elders, who, together with the First Elder, styled themselves the Head Elder’s hands and feet.

Wipeng’s brow twitched when he saw the faint Sword Energy gathered on their blades.

“You’ve been hiding your martial arts.”

The First Elder answered with a single punch.

Boom!

With internal energy as deep as the years he had lived, he sent Wipeng flying, then straightened his back.

The field froze at the appearance of yet another Peak master who had spent his entire life hidden in the Head Elder’s shadow.

“First Elder, what… what is this?”

“Then could it be…!”

*Betrayal.* The word stamped itself clearly into everyone’s minds.

“That’s impossible!”

The one who shouted was the White Tiger Hall Leader. If the Elders were the Head Elder’s hands and feet, he had thoroughly served as the First Elder’s.

“Elder, Lesser Family Head. It seems there has been some misunderstanding…”

But he could not finish. At a jerk of the First Elder’s chin, the Second Elder moved with blinding speed and cut the White Tiger Hall Leader’s throat.

Shhk. Thud.

Jin Wikyung’s gaze met the First Elder’s in the air between them.

“You recruited the White Tiger Hall Leader too?”

“He was a noisy man. That was all. The others were the same.”

Jin Wikyung’s guess had been half right and half wrong.

The Elders had betrayed them, but the senior members who belonged to the Elders’ faction had not.

“Then why… Ah!”

“Sharp. I’ll give you that.”

The First Elder pulled a dark, grimy bamboo tube from inside his robes. Only a little of the fuse was left, and it was already burning down.

“Could we tell important secrets to men like that? Even just throwing the inside into chaos had already served its purpose. Things were easier if they didn’t know what was happening outside.”

Jin Wikyung shouted like a scream.

“Stop him!”

“You’re too late.”

The First Elder was right. The instant the fuse burned to its end, something burst, and a red flame shot high into the sky.

Fwish—boom!

It was a signal.

The martial artists of the small and mid-sized sects known as the Five Gates of Shanxi—the Three Paths Sect, a union of three sects; the Tao-centered Byeokdo Sect; and Gunggwimun, which had been pouring arrows from the cliffs without pause—turned in an instant.

“Kill everyone in your path!”

“No exceptions! Sweep them all away!”

They were no longer the clumsy third-rate martial artists they had seemed to be. Killing intent flowed from their eyes, and their sword paths were sharp.

*This wasn’t something they prepared overnight.*

Jin Wikyung’s face hardened.

* * *

Boom!

The Head Elder looked up at the sky. Before the red flame had even faded, a massive roar erupted from every direction.

*Too fast. Far too fast.*

The signal was supposed to go up only after the Mount Heng Sword Sect had been annihilated. The Five Gates of Shanxi were a blade prepared over decades. It had to be swung once, and finish everything like a bolt of lightning.

*Everything has its flow.*

The plan, which had been running without a hitch, had begun to go off course. As the Head Elder smiled bitterly, a voice slipped into his ear.

“So… it was you.”

Lee Cheonbaek. His voice was faint, but his eyes burned more fiercely than ever.

“You still have the strength to talk?”

“I’ll tear you to pieces alive and kill you.”

But no sooner had he finished speaking than blood poured from his mouth. The Head Elder pressed one of his acupoints and murmured,

“That would be inconvenient just yet. You still have something to do.”

Lee Cheonbaek despaired.

They had taken heavy losses, but hundreds of Mount Heng Sword Sect martial artists still remained. At this point, with even the leadership annihilated, if their Sect Leader were taken prisoner…

*Kill me instead!*

The anguished cry never left his mouth. The Head Elder pressed the Mute Acupoint, taking his voice. Then his hand brushed the Paralysis Acupoint, and Lee Cheonbaek’s body went rigid.

He had become a living corpse with his eyes still open.

“You bastard! Get your hands off him!”

At the same time, the air split with a shriek.

Fwoooosh!

The Head Elder did not panic. He swept his sword up from below. Beyond the spear splitting in two along the Sword Energy, Jin Taekyung was charging at terrifying speed.

“Aaaaaah!”

“Squad Leader! Please slow down a little!”

Together with a dozen or so riffraff who had appeared from who knew where.

[^1]: Red Hare is the legendary warhorse of Lü Bu in *Romance of the Three Kingdoms*.
```
## Chapter 58

### Korean source

```text
＃58화



전장은 혼돈으로 치달았다. 신호와 동시에 돌변한 이백 명의 무인들이 이리 떼처럼 사방을 덮쳤다.

“모두 죽여라!”

“으아아악!”

앞서 상대했던 곽준과 암살자들만큼은 아니지만, 놈들에게서는 잘 벼린 칼날 같은 기세가 뿜어져 나왔다.

태원진가와 항산검문. 양 세력의 무인들이 힘을 합친다면 충분히 승산이 있겠지만 지금 당장으로써는 어려워 보인다.

‘좋지 않아.’

최악의 경우 진위경만 빼내서 도망쳐야 할 수도 있다.

내심 그런 생각을 하고 있을 때, 등 뒤로 거친 숨소리와 함께 정찰조원들이 도착했다.

“조장, 좀 같이…… 헉!”

눈앞에 벌어진 상황을 보더니 하나같이 눈이 툭 튀어나온다. 뒤이어 엉금엉금 기어 올라온 혁무진도 입을 딱 벌렸다.

“우웨에엑!”

“……그쪽이었냐.”

힘들긴 했던 모양이다. 빠르고 굵은 구토를 끝낸 혁무진이 다 죽어 가는 얼굴로 말했다.

“전 여기까지인 것 같습니다.”

누가 보면 용감하게 싸우다가 칼 맞은 부상병인 줄 알겠다.

나는 녀석의 어깨를 힘주어 잡았다.

“무진아. 넌 할 수 있어.”

“아니에요. 전 틀렸어요. 가 봤자 짐만 될 거예요.”

“짐이라니! 넌 훌륭한 고기 방패…….”

“예?”

“방패! 넌 태원진가의 방패다!”

“고기 방패라고 했던 것 같은데.”

혁무진의 불신 섞인 중얼거림을 무시하고 녀석을 일으켜 세웠다. 지금은 고기 방패, 아니 손 하나가 아쉬운 시점이다.

더군다나 혁무진은 나를 제외하면 정찰조 중 최고의 실력을 지닌 고기 방패, 아 말이 자꾸 헛나오네.

나는 짐짓 목소리를 내리깔았다.

“본가가 위기에 처했는데 도망치겠다는 말이냐?”

솔직히 나였으면 도망쳤다.

“아닙니다!”

21세기 직장인이었다면 산재 처리 해 주겠다고 해도 면상에 침 뱉고 돌아섰을 텐데, 정찰조원들은 생각 이상으로 충성스러웠다. 혁무진도 창백한 얼굴로 검을 뽑아 들었다.

“좋습니다. 무인이라면 죽더라도 싸우다 죽어야죠.”

“각오는 좋은데, 죽지는 마라.”

“방금은 고기 방패라면서요?”

“너, 나 못 믿어?”

“예.”

혁무진의 칼 같은 대답에 정찰조원들 사이로 가벼운 웃음이 번졌다. 난생처음 겪는 대규모 전투에 얼어붙어 있던 몸이 한결 풀어지는 기분이다.

나도 씩 웃으며 창을 움켜쥐었다.

“눈 크게 뜨고, 귀 활짝 열어. 내 명령대로만 움직이면 살아서 돌아간다.”

그건 스스로에게 하는 다짐이었다. 이 녀석들만큼은 어떻게든 살려 보겠다는.

‘부디 죽지 마라.’

이 전쟁이 어떻게 끝날지, 누가 죽고 살지는 나도 모른다.

다만 최선을 다할 뿐이다.

“가자.”

그 말과 함께 우리는 질풍처럼 달려 나갔다. 나를 꼭짓점으로 한 화살이었고, 명중시켜야 할 목표는 정해져 있었다.

‘대장로.’

또렷한 시야 너머로 백발의 노인이 보인다. 그의 발아래 쓰러진 한 사람과 가득 고인 피 웅덩이도.

뱃속에서부터 뜨거운 불덩어리가 치솟았다.

“우리 형한테…….”

누군가의 시체 위에 묘비처럼 박혀 있던 창 한 자루를 뽑아 들었다. 그리고 다음 순간.

“손 떼, 이 새끼야!”

일직선으로 쏘아진 창이 수십 장의 거리를 압축시켰다.

정찰조원 중 누군가의 입에서 억눌린 외침이 튀어나왔다.

“됐다!”

대장로의 검이 움직인 것도 그때였다.

슉.

한 줄기 빛. 반쪽으로 갈라진 창이 양옆으로 튕겨져 나간다.

앞서와 똑같은 결과다. 하지만 이번에는 대장로와의 거리가 상당히 좁혀진 덕분에 똑똑히 목격할 수 있었다.

순간적으로 검신을 타고 솟구친 푸른 섬광을.

‘오라(Aura)?’

아니, 저게 여기서 왜 나와.



* * *



오라.

최소 A급 헌터는 되어야 뽑아낼 수 있다는 마나의 결정체.

마나와 공력은 이름만 다를 뿐, 기(氣)라는 면에서는 동일하다. 이곳은 무림이니까, 바꿔 말하자면 검기다. 검기.

허허허.

‘시발, 장난하나.’

대장로가 고수인 건 진작 알고 있었다. 여차하면 한판 붙을 각오도 했다. 문제는 ‘검기를 쓰는’ 대장로가 내 계획에 없었다는 거지.

‘이건 좀 아닌데.’

슬쩍 고개를 돌려 보니 십여 쌍의 흔들리는 동공들이 보인다.

그중에서도 혁무진의 눈동자는 거의 지진 수준이다.

“저, 조장.”

“으, 응?”

“방금 저거, 검기 같은데요.”

“그러게…….”

“조장도 검기 쓸 줄 아세요?”

“그런 거 있었으면 진작 썼지. 조필도 저 정도는 아니었어.”

“그렇죠?”

“그렇지. 근데 너 안 힘들어?”

“토할 것 같아요.”

우리는 약속이라도 한 것처럼 속도를 늦췄다. 100m 달리기에서 경보로 종목이 바뀌었지만 사자 아가리로 들어가는 기분은 똑같다.

“저기, 조장.”

혁무진이 핏기 하나 없는 얼굴로 입을 열었다. 피부색 하나만큼은 백인이라고 해도 좋을 정도다.

“대장로님이 배신한 거 확실해요?”

“확실해.”

“혹시 오해일 수도…….”

말이 끝나기도 전에 흑의인 서너 명이 고함과 함께 달려들었다.

“주군을 지켜라!”

“대장로님을 위하여!”

대사 봐라, 태원진가 망년회 건배사로 써도 되겠다. 달려드는 흑의인들을 모조리 베어 버린 나는 혁무진을 바라봤다.

“어, 무슨 말 하려고 했었냐?”

“……별말 아니었어요.”

정신 승리에 실패한 혁무진은 침통한 얼굴로 고개를 떨궜다.

하지만 그것도 잠시. 한 발, 한 발. 대장로와 가까워질수록 녀석은 필사적으로 살아 나갈 구멍을 찾기 시작했다.

“사람들은 왜 싸워야 하는 걸까요?”

이 새끼 노벨 평화상 노리나.

“아까는 싸우다가 죽겠다며. 무인답게.”

“그거야 최악의 경우고요. 대화로 해결하면 좋잖아요.”

“대화 좋지. 근데 저쪽에서 먼저 암살자 보냈잖아.”

“아.”

“나도 창 던졌고.”

“아아.”

“던지면서 욕도 했어.”

“앗, 아아아.”

대장로와의 거리가 십여 장 안으로 좁혀졌을 때, 혁무진의 얼굴은 까맣게 죽어 있었다. 다른 정찰조원들도 말은 안 했지만 덜덜 떨고 있는 게 눈으로 보일 정도다.

물론 나도 비슷하다. 검기를 떠올리는 것만으로도 가슴이 벌렁벌렁한다.

‘된통 걸렸네.’

하지만 도망칠 생각은 없다. 그럴 거였다면 처음부터 돌아오지도 않았겠지. 현실에 만족하며 그냥 그렇게 살았을 거다.

이미 너무 멀리 왔다. 남은 길은 하나뿐이다.

“정지.”

내 말에 모두가 기다렸다는 듯이 멈춰 섰다. 혁무진은 극적인 평화 조약을 기대하는 얼굴이었지만 나는 창을 쥐고 앞으로 나섰다.

“어, 어디 가세요?”

“싸우러. 너희는 여기서 대기해.”

“미쳤습니까? 차라리 소가주님이 올 때까지 기다렸다가 합공을…….”

“저기 엎어져 있는 사람 보이지?”

“어, 네.”

“우리 형이야.”

하늘이 무너진 표정으로 나를 바라보던 혁무진이 한숨을 푹 내쉬었다.

“그럼 같이 가요.”

“뭐?”

“저 같은 고기 방패라도 있어야 승산이 쥐꼬리만큼이라도 생길 거 아닙니까.”

이 자식이 이렇게 기특한 생각도 하네.

나는 피식 웃고는 돌아섰다.

“죽으러 가냐? 간 좀 보고 돌아올 테니까 기다리고 있어.”

이제 대장로와의 거리는 삼 장에 불과했다.

그와 나, 누구든 한순간에 좁힐 수 있는 거리다.

공간 사이로 무거운 침묵이 짓눌렀다. 잠깐 사이에 손바닥이 축축하게 젖어 든다.

‘후우.’

하지만 나도 호락호락한 놈은 아니다. 고작 이류였던 30레벨 때 이미 절정 고수인 조필을 꺾었고, 현실로 돌아간 후에도 발전을 거듭해 왔다.

40레벨인 지금은 현실과 무림, 어느 곳에서도 제법 먹히는 고수라고 자부한다. 아니, 고수 맞다.

‘최대한 거리를 유지하면서 싸운다면…….’

불과 몇 센티 차이로 생사가 판가름 나는 싸움에서 창의 공격 범위는 엄청난 장점이다.

나는 대장로의 얼굴을 보며 호흡을 가다듬었다.

‘해볼 만하다.’

단숨에 공력을 끌어 올려 쇄도했다. 일 장. 대장로에게 창날이 닿을 수 있는 거리. 그리고 대장로의 검이 내게 닿을 수 없는 거리.

‘지금!’

대장로의 정수리를 향해 창날을 내리찍었다.

동시에 기다리던 시스템 알림이 울렸다.

띠링.



- 칭호, [승부사]의 효과가 적용됩니다.

- [근력]이 일시적으로 상승합니다.

- [민첩]이 일시적으로 상승합니다.

- [체력]이 일시적으로…….



승부사. 일대일 승부 시 전투 관련 능력치를 10% 상승시켜 주는 칭호 효과가 전신 곳곳에 스며들었다.

거기에 더해서.

슈왁!

능력치의 상승은 공격의 가속에도 영향을 끼쳤다. 순간 빛살 같은 속도로 떨어지는 창날이 대장로의 정수리를 노렸다.

‘이건…… 들어갔다.’

그건 확신이었다.

설령 그 괴물 같은 조필이었어도 피하지 못할 거라는 확신. 그러나 내가 상대하고 있는 사람은 조필이 아니었다.

대장로였다.

쾅!

굉음과 함께 창대가 진동했다. 제대로 보이지도 않을 만큼 빠른 속도로 창을 막아 낸 대장로가 싱긋 웃었다.

“제법이구나. 기대 이상이야.”

나는 대답할 틈도 없이 젖 먹던 힘까지 끌어 올렸다. 어지간한 고수도 견디기 힘들 만한 거력(巨力)이 실린 창이 그의 검을 짓눌렀다.

그그극.

기분 나쁜 마찰음과 함께 검이 점차 위로 들리기 시작…….

아니, 잠깐만.

‘아래로 가야지 왜 위로 와.’

그토록 힘을 줬는데 밀리는 건 오히려 나다. 내 황당한 표정에 대장로의 웃음이 진해졌다.

“애썼다만, 그 정도로 되겠느냐?”

다음 순간, 머리털이 쭈뼛 서는 감각이 전신을 급습했다.

츠츠츠.

검신 위로 피어오르는 푸른 아지랑이. 검기다.

미처 대응할 사이도 없이, 서서히 밀리고 있던 창두가 두부처럼 잘려 나갔다.

슁.

이제는 창이 아니라 봉(棒)이다. 장봉.

물러서는 나를 향해 다시 한번 검기가 번쩍였다.

슁.

장봉이 단봉이 되었다.

슁.

“…….”

시발, 쌍절곤도 이것보다 길겠다. 나는 창도, 봉도 아니게 되어 버린 철 막대기를 대장로를 향해 집어 던졌다.

슁.

“도망칠 셈이더냐?”

도망치다니, 섭섭한 소리를.

이미 투척과 동시에 옆으로 몸을 날린 후였다. 죽은 듯이 엎드려 있는 진위경의 옷깃을 꽉 붙잡았다.

‘됐다!’

내 목적은 처음부터 단 하나, 진위경의 구출이었다.

목적을 달성했으니 저 괴물 같은 노인네와 싸울 필요도 없다. 나는 진위경을 끌어안고 온 힘을 다해 몸을 날렸다.

쉬익- 쾅!

뒤늦게 날아든 검기가 지면을 갈랐다.

간발의 차로 대장로의 공격 범위를 빠져나온 우리를 혁무진과 정찰조원들이 에워쌌다.

“조장을 보호해라!”

“괜찮으십니까?”

나는 침묵했다. 당장 대장로를 피해 도망쳐야 한다는 사실도, 이곳이 전장이라는 사실도 잊었다.

머릿속에는 한 가지 의문만 가득했다.

‘뭐야, 이 사람.’

분명히 진위경을 구했는데, 그랬어야 했는데…….

지금 내 품에 안겨 있는 이 마초 아저씨는 누구란 말인가.

얼굴 가득한 칼자국과 핏발 선 눈동자. 나는 떨리는 목소리로 물었다.

“실례지만 누구……세요?”

그때 혁무진의 입에서 외마디 비명이 터졌다.

“억! 이천백!”

이천백? 어디서 들어 봤는데.

“이 사람 알아?”

“당연히 알죠!”

“친해?”

“무슨 개소립니까! 혈랑검 이천백이잖아요!”

“혈랑검이라고?”

“네! 바로 그 혈랑검……!”

“별호 멋있네. 고수 같고.”

혁무진이 머리를 쥐어뜯으며 외쳤다.

“항산검문 문주잖아요! 혈랑검 이천백!”

“……!”

나는 후다닥 물러났다. 이 아저씨가 이천백이라니. 식은땀이 주르륵 흐른다.

‘이소군 아버지잖아.’

내가 자기 아들을 독살했다고 생각해서 전쟁까지 일으킨 인간이다. 보복 차원에서 어른, 아이 가리지 않고 죽여 버린 냉혈한이기도 했다.

‘엉뚱한 인간 구한 것도 억울한데, 칼침까지 맞을 뻔했네.’

그러나 이천백에게는 그럴 만한 힘이 더 이상 남아 있지 않은 듯했다.

전신이 피투성이인 데다, 손 하나 까딱 못 하는 게 심각한 내상 혹은 점혈을 당한 것처럼 보였다.

‘그래도 다행이다. 진위경이 아니라서.’

내 마음을 읽은 것처럼 혁무진이 물었다.

“그럼 소가주님께선 어디 계신 겁니까?”

“모르지. 그리고…….”

황급히 녀석의 목덜미를 잡아당겼다. 방금까지만 해도 혁무진의 발이 있던 자리에 검 한 자루가 날아와 박혔다.

‘진짜로 된통 걸렸네.’

나는 한숨을 푹 내쉬고 말을 이었다.

“저 노인네가 보내 주겠냐?”

대장로가 너털웃음을 터트렸다.

“으하하, 이런 버르장머리 없는 놈을 보았나!”

“예의 바르게 행동하면 그냥 보내 줄 수 있나?”

“그러기에는 너무 멀리 왔다고 생각하지 않느냐?”

츠츠츠.

솟구치는 검기. 더 이상 말이 필요 없다.

시체들 사이에 박혀 있던 창을 뽑아 들었다. 그리고 모두의 시선 속에서 입을 뗐다.

“포위 대형, 펼쳐.”

오래된 헌터 명언 중 하나.

‘강한 몬스터는 있어도 잡지 못하는 몬스터는 없다.’

그걸 가능케 하는 것이 레이드(Raid)다.
```

### Current accepted English

```markdown
# Chapter 58

The battlefield descended into chaos. At the signal, two hundred martial artists suddenly turned and swarmed in every direction like a pack of wolves.

“Kill them all!”

“Aaaaargh!”

They weren’t quite on the level of Gwak Jun and the assassins we’d fought earlier, but a honed-blade aura still poured off them.

The Jin Family of Taiyuan and the Mount Heng Sword Sect. If both factions’ martial artists joined forces, we’d have a real shot—but right now, that looked difficult.

*This is bad.*

At worst, I might have to pull Jin Wikyung out and run.

I was thinking that when the reconnaissance squad arrived behind me, breathing hard.

“Squad Leader, maybe we can—huff!”

The moment they saw what was happening in front of them, their eyes all popped wide. Hyuk Mujin, who came crawling up behind them, gaped as well.

“Bweeegh!”

“…So that was it.”

It must have been rough. After a fast, heavy burst of vomiting, Hyuk looked half-dead as he spoke.

“I think this is as far as I go.”

Anyone looking at him might have taken him for a wounded soldier who’d been stabbed while fighting bravely.

I gripped his shoulder hard.

“Mujin. You can do this.”

“No. I’m finished. I’ll only be a burden if I go.”

“A burden? You’re an excellent meat shie—”

“Excuse me?”

“Shield! You’re the Jin Family of Taiyuan’s shield!”

“I could have sworn you said meat shield.”

Ignoring Hyuk’s suspicious muttering, I hauled him to his feet. Right now, even a meat shield—no, a single extra hand—was precious.

Besides, apart from me, Hyuk was the strongest meat shield in the reconnaissance squad. Ah, it kept slipping out.

I deliberately lowered my voice.

“Our family is in danger, and you’re saying you want to run?”

If it had been me, I would have run.

“No, sir!”

A twenty-first-century office worker would have spat in your face and walked away, even if you’d offered to file it as a workplace injury. But the reconnaissance squad was more loyal than I’d expected. Hyuk drew his sword with a pale face.

“Very well. If a martial artist has to die, he should die fighting.”

“That’s a fine resolve, but don’t die.”

“You just called me a meat shield.”

“You don’t trust me?”

“Yes.”

Hyuk’s answer was as sharp as a blade, and a light laugh spread through the reconnaissance squad. They’d been frozen stiff by the first large-scale battle of their lives, but they seemed to loosen up a little.

I grinned and gripped my spear.

“Eyes wide, ears open. Follow my orders, and you’ll make it back alive.”

That was a vow I was making to myself. I would get these guys out alive somehow.

*Please don’t die.*

I didn’t know how this war would end, or who would live and who would die.

All I could do was give it everything I had.

“Let’s go.”

At that, we charged forward like a gale. We were an arrow with me at the tip, and the target we had to hit was already set.

*The Head Elder.*

Clear in the distance, I could see a white-haired old man. At his feet lay a fallen man, and a pool of blood.

A hot lump of fire surged up from my gut.

“That’s my brother…”

I pulled a spear from where it had been driven into someone’s corpse like a gravestone. Then, in the next instant—

“Get your hands off him, you bastard!”

The spear shot in a straight line, compressing dozens of yards of distance.

Someone in the reconnaissance squad let out a muffled cry.

“We got him!”

That was when the Head Elder’s sword moved.

Shuk.

A streak of light. The spear split in half and bounced away to either side.

Same result as before. But this time we’d closed the distance considerably, so I could see it clearly.

The blue flash that had surged along the blade for an instant.

*Aura?*

No. Why was that showing up here?

* * *

Aura.

A crystallization of mana that only an A-rank Hunter or higher could draw out.

Mana and internal energy were different only in name. In terms of qi, they were the same. And this was Murim, so put another way, it was Sword Energy.

Sword Energy.

Heh heh heh.

*Fuck. Are you kidding me?*

I’d known for a long time that the Head Elder was a master. I’d even been ready to fight him if it came to that. The problem was that a Head Elder *using Sword Energy* hadn’t been part of the plan.

*This is a bit much.*

I glanced aside and saw ten-odd pairs of shaking eyes.

Hyuk Mujin’s were practically seismic.

“S-Squad Leader.”

“Y-Yeah?”

“That just now… that looked like Sword Energy.”

“Yeah…”

“Can you use Sword Energy too?”

“If I could, I would have used it already. Even Jopil wasn’t at that level.”

“Right?”

“Right. But aren’t you exhausted?”

“I feel like I’m going to throw up.”

As if we’d agreed on it, we slowed down. The event had switched from a hundred-meter dash to race walking, but it still felt like walking into a lion’s jaws.

“Uh, Squad Leader.”

Hyuk opened his mouth with a face drained of all color. As far as his skin went, he could have passed for a white man.

“Are you sure the Head Elder betrayed us?”

“I’m sure.”

“Could it possibly be a misunderstanding—”

Before he could finish, three or four black-clad men charged at us with a shout.

“Protect our lord!”

“For the Head Elder!”

Get a load of those lines. They’d work as a toast at a Jin Family of Taiyuan year-end party.

I cut down every last black-clad man charging us, then looked at Hyuk.

“Uh, what were you about to say?”

“…Nothing.”

Having failed to win the argument in his head, Hyuk hung his head, looking grim.

But only for a moment. Step by step. The closer we got to the Head Elder, the more desperately he started hunting for a way out.

“Why do people have to fight?”

*Is this bastard aiming for the Nobel Peace Prize?*

“You said earlier you’d fight and die. Like a martial artist.”

“That was the worst case. Wouldn’t it be better to settle this with talk?”

“Talk’s good. But they sent assassins after us first.”

“Oh.”

“And I threw a spear.”

“Ah.”

“And I cursed while throwing it.”

“Ah—ahhh.”

When we closed to within about a hundred feet of the Head Elder, Hyuk’s face looked like death. The other reconnaissance squad members didn’t say anything, but I could see them shaking.

Of course, I wasn’t much different. Just thinking about Sword Energy made my chest hammer.

*I’m well and truly screwed.*

But I had no intention of running. If I had, I never would have come back in the first place. I would have been content with reality and just lived that way.

I’d already come too far. There was only one path left.

“Stop.”

Everyone halted as if they’d been waiting for it. Hyuk’s face said he was hoping for a dramatic peace treaty, but I gripped my spear and stepped forward.

“W-Where are you going?”

“To fight. You wait here.”

“Are you insane? We’d be better off waiting for the Lesser Family Head and attacking together—”

“See the person lying over there?”

“Y-Yes.”

“That’s my brother.”

Hyuk looked at me like the sky had fallen, then let out a long sigh.

“Then I’m coming with you.”

“What?”

“Even a meat shield like me should bump our odds up by a hair, shouldn’t it?”

This guy actually came up with some admirable thoughts.

I snorted a laugh and turned away.

“You going there to die? I’m just going to test the waters and come back. Wait here.”

The distance to the Head Elder was now barely thirty feet.

A distance either of us could close in an instant.

A heavy silence crushed the space between us. In that brief interval, my palms went damp.

*Phew.*

But I wasn’t an easy mark either. At Level 30, when I was only Second Rate, I’d already beaten Jopil, a Peak master. And I’d kept improving after I went back to reality.

At Level 40, I could proudly call myself a master who held his own in both reality and Murim.

No. I was a master.

*If I fight while keeping as much distance as I can…*

In a fight where a few centimeters could decide life or death, a spear’s reach was a massive advantage.

I looked at the Head Elder’s face and steadied my breathing.

*This is doable.*

I drew up my internal energy in a single burst and charged. Ten feet—the range where my spearhead could reach the Head Elder, and his sword couldn’t reach me.

*Now!*

I brought the spearhead down toward the crown of his head.

At the same time, the System notification I’d been waiting for rang out.

Ding.

> **System**
>
> - The effect of the Title **Gambler** is applied.
> - **Strength** temporarily increases.
> - **Agility** temporarily increases.
> - **Stamina** temporarily…

The effect of the Gambler Title, which raised combat-related stats by ten percent in a one-on-one duel, seeped through my whole body.

And on top of that—

Whoosh!

The boost to my stats accelerated the attack as well. In an instant, the spearhead dropped like a bolt of light, aimed at the crown of the Head Elder’s head.

*This is going in.*

That was certainty.

The certainty that even a monster like Jopil wouldn’t have been able to dodge it. But the man I was facing wasn’t Jopil.

He was the Head Elder.

Boom!

The spear shaft shuddered with a thunderous crash. The Head Elder, having blocked the spear at a speed too fast to see properly, smiled faintly.

“Not bad. Better than I expected.”

Without even time to answer, I wrung out every last ounce of strength. The spear, loaded with tremendous force that even a decent master would have struggled to endure, crushed down on his sword.

Grrrkk.

With an ugly grinding sound, his sword began to lift…

No. Wait.

*It should be going down. Why is it coming up?*

I’d put that much force into it, and I was the one being pushed back. At my dumbfounded expression, the Head Elder’s smile deepened.

“You tried, but did you think that would be enough?”

The next instant, every hair on my body stood on end.

Tsssss.

A blue haze bloomed along the blade.

Sword Energy.

Before I could even react, the spearhead that had been slowly getting pushed back was sliced off like tofu.

Shing.

Now it wasn’t a spear but a staff. A long staff.

Sword Energy flashed again toward me as I backed away.

Shing.

The long staff became a short staff.

Shing.

“…”

Fuck. Even nunchaku would be longer than this.

I threw the iron rod—no longer a spear or a staff—at the Head Elder.

Shing.

“Do you intend to run?”

Run? That’s a hurtful thing to say.

I’d already thrown myself sideways at the same moment I threw it. I grabbed the collar of the man lying facedown as if he were dead.

*Got him!*

My only goal from the beginning had been to rescue Jin Wikyung.

Now that I’d done it, there was no reason to fight that monstrous old man. I scooped Jin Wikyung into my arms and hurled myself away with all my strength.

Whoosh—boom!

The Sword Energy that arrived a beat later split the ground.

Hyuk Mujin and the reconnaissance squad surrounded us as we slipped out of the Head Elder’s range by a hair.

“Protect the Squad Leader!”

“Are you all right?”

I said nothing. I forgot we had to run from the Head Elder right now. I even forgot this was a battlefield.

My head was full of a single question.

*Who is this man?*

I had definitely rescued Jin Wikyung. I was supposed to have rescued him…

Then who was this macho middle-aged man in my arms?

His face was covered in sword scars, and his eyes were bloodshot. In a trembling voice, I asked,

“Excuse me, but who are you…?”

At that moment, a single cry burst from Hyuk Mujin’s mouth.

“Gah! Lee Cheonbaek!”

Lee Cheonbaek? The name rang a bell.

“You know him?”

“Of course I do!”

“Are you close?”

“What kind of bullshit is that? That’s Blood Wolf Sword Lee Cheonbaek!”

“Blood Wolf Sword?”

“Yes! That Blood Wolf Sword…!”

“Cool alias. Sounds like a master.”

Hyuk tore at his hair and shouted,

“He’s the Sect Leader of the Mount Heng Sword Sect! Blood Wolf Sword Lee Cheonbaek!”

“…”

I scrambled backward.

This man was Lee Cheonbaek?

Cold sweat rolled down me.

*He’s Lee Seogeun’s father.*

He was the man who’d started a war because he thought I’d poisoned his son. He was also a cold-blooded killer who’d slaughtered adults and children alike in revenge.

*Rescuing the wrong guy was unfair enough, and I nearly got stabbed too.*

But Lee Cheonbaek no longer seemed to have the strength left for that.

His whole body was covered in blood, and he couldn’t so much as twitch a hand. It looked like severe internal injuries, or like his acupoints had been sealed.

*Still, at least it isn’t Jin Wikyung.*

As if he’d read my mind, Hyuk asked,

“Then where is the Lesser Family Head?”

“I don’t know. And…”

I yanked him back by the nape of his neck. A sword came flying in and buried itself where Hyuk’s foot had been a moment before.

*I’m really well and truly screwed.*

I let out a long sigh, then went on,

“You think that old man is going to let us go?”

The Head Elder burst into a hearty laugh.

“Ha ha ha! Have you ever seen such an insolent brat!”

“If I behave politely, will you let us go?”

“Don’t you think you’ve come too far for that?”

Tsssss.

Sword Energy surged up.

No more words were needed.

I pulled a spear stuck among the corpses. Then, with everyone’s eyes on me, I spoke.

“Encircling formation. Spread out.”

One of the oldest Hunter sayings was this:

*There are strong monsters, but no monster that can’t be taken down.*

What made that possible was a raid.
```
