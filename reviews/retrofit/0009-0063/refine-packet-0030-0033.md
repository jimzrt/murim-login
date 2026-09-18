# Retrospective Patch Plan — Chapters 30–33

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
  "summary": "10 findings in chapters 30-33",
  "findings": [
    {
      "chapter": 30,
      "confidence": 0.99,
      "current": "“You can still stand after taking a seventh-stage Flame Divine Palm… What a high-maintenance junior.”",
      "defect": "칠 성 means seventy percent power, not the seventh stage of the technique. The current version invents a progression stage and obscures how much force Jopil used.",
      "id": "R0030-01",
      "rationale": "The source quantifies the technique's output as seven-tenths of full power.",
      "replacement": "“You can still stand after taking a Flame Divine Palm at seventy percent power… What a high-maintenance junior.”",
      "severity": "major",
      "source": "“칠 성의 화염신장(火焰神掌)을 맞고도 일어선단 말이지…… 손이 많이 가는 후배구먼.”"
    },
    {
      "chapter": 31,
      "confidence": 1.0,
      "current": "“You were unconscious for five days. Your condition was so critical that the Medicine King Hall Leader concluded you wouldn’t last the day.”\n\n“Really?”\n\n“Yes. When my lord heard that, he went berserk. If I hadn’t stopped him, he would have beaten the Medicine King Hall Leader to death.”",
      "defect": "The established title 약왕당주 is Medicine King Hall Master, not Medicine King Hall Leader.",
      "id": "R0031-01",
      "rationale": "The glossary fixes this office as Medicine King Hall Master.",
      "replacement": "“You were unconscious for five days. Your condition was so critical that the Medicine King Hall Master concluded you wouldn’t last the day.”\n\n“Really?”\n\n“Yes. When my lord heard that, he went berserk. If I hadn’t stopped him, he would have beaten the Medicine King Hall Master to death.”",
      "severity": "minor",
      "source": "“닷새 동안 혼절해 계셨습니다. 상태가 워낙 위중해서 하루를 못 넘길 거라는 게 약왕당주의 결론이었고요.”\n\n“그래요?”\n\n“예. 그 얘기를 들은 주군께서 길길이 날뛰셨죠. 제가 안 말렸으면 약왕당주를 때려죽였을 겁니다.”"
    },
    {
      "chapter": 31,
      "confidence": 1.0,
      "current": "“Number One Under Heaven.”",
      "defect": "The established rendering of 천하제일인 is not used.",
      "id": "R0031-02",
      "rationale": "The glossary distinguishes 천하제일인 as greatest under heaven from the stronger 고금제일인 superlative.",
      "replacement": "“The greatest under heaven.”",
      "severity": "minor",
      "source": "“천하제일인(天下第一人).”"
    },
    {
      "chapter": 31,
      "confidence": 1.0,
      "current": "“Number One of All Time.”",
      "defect": "The established rendering of 고금제일인 is not used.",
      "id": "R0031-03",
      "rationale": "The glossary fixes this distinct superlative as greatest of all time.",
      "replacement": "“The greatest of all time.”",
      "severity": "minor",
      "source": "“고금제일인(古今第一人).”"
    },
    {
      "chapter": 32,
      "confidence": 0.97,
      "current": "“The Mount Heng Twin D-Devils?”\n\n“The Mount Heng Twin Devils.",
      "defect": "Taekyung's profane mishearing of 쌍귀 as 썅귀 is reduced to an unexplained stutter, losing the joke and his coarse register.",
      "id": "R0032-01",
      "rationale": "썅 is a profanity-like distortion, while Wipeng immediately corrects it to the actual epithet 쌍귀, Twin Devils.",
      "replacement": "“The Mount Heng Fucking Devils?”\n\n“The Mount Heng Twin Devils.”",
      "severity": "major",
      "source": "“항산썅귀요?”\n\n“항산쌍귀 말입니다."
    },
    {
      "chapter": 32,
      "confidence": 0.99,
      "current": "“How many Peak masters do you think there are in a single city? Across all of Shanxi, where our family is located, there are fewer than twenty.”",
      "defect": "성 refers to a province in this administrative comparison, not a city. The current version materially understates the geographic scale of Peak-master scarcity.",
      "id": "R0032-02",
      "rationale": "The following clause explicitly uses all of Shanxi as the relevant province-wide frame.",
      "replacement": "“How many Peak masters do you think there are in a single province? Across all of Shanxi, where our family is located, there are fewer than twenty.”",
      "severity": "major",
      "source": "“한 성(城)에 절정 고수가 몇이나 있다고 생각하십니까? 본가가 위치한 산서를 통틀어도 채 스물이 되지 않습니다.”"
    },
    {
      "chapter": 33,
      "confidence": 0.98,
      "current": "That was how the debts and grudges of Murim worked. The chain of debts and grudges would not break until one of the two sides fell.",
      "defect": "The established Murim concept 은원 is rendered as debts and grudges rather than gratitude and grudges, muting its explicit positive-and-negative duality.",
      "id": "R0033-01",
      "rationale": "恩怨 encompasses both favors or gratitude owed and hostile grudges; the glossary fixes the phrase as gratitude and grudges.",
      "replacement": "That was how gratitude and grudges worked in Murim. The cycle of gratitude and grudges would not end until one of the two sides fell.",
      "severity": "minor",
      "source": "무림의 은원(恩怨)이란 그런 것이다. 둘 중 하나가 쓰러지기 전까지 은원의 고리는 끊어지지 않는다."
    },
    {
      "chapter": 33,
      "confidence": 1.0,
      "current": "“The Medicine King Hall Leader was absolutely furious.”",
      "defect": "The established title 약왕당주 is Medicine King Hall Master, not Medicine King Hall Leader.",
      "id": "R0033-02",
      "rationale": "The glossary fixes this office as Medicine King Hall Master.",
      "replacement": "“The Medicine King Hall Master was absolutely furious.”",
      "severity": "minor",
      "source": "“약왕당주께서 노발대발하셨죠.”"
    },
    {
      "chapter": 33,
      "confidence": 1.0,
      "current": "**One Flash**",
      "defect": "The newly acquired named Skill is given the wrong established English name.",
      "id": "R0033-03",
      "rationale": "The glossary explicitly establishes 일섬 as One Annihilation for the spear technique used to kill the Boss Zone monster.",
      "replacement": "**One Annihilation**",
      "severity": "major",
      "source": "[일섬]"
    },
    {
      "chapter": 33,
      "confidence": 1.0,
      "current": "“Hundred-year snow ginseng?”",
      "defect": "The established elixir name is not used.",
      "id": "R0033-04",
      "rationale": "The glossary fixes 백년설삼 as Hundred-Year-Old Snow Ginseng.",
      "replacement": "“Hundred-Year-Old Snow Ginseng?”",
      "severity": "minor",
      "source": "“백년설삼?”"
    }
  ]
}
```

## Chapter 30

### Korean source

```text
＃30화



화아악.

조필의 붉게 달아오른 손바닥이 내 가슴을 때린 순간, 용암처럼 뜨거운 기운이 내부를 휩쓸었다. 숨이 막히고 공력이 역류했다.

‘이건 뭐지?’

의문과 함께 나는 튕겨져 나갔다. 십여 장을 부딪치고 구른 후에야 멈출 수 있었다.

“쿨럭.”

턱을 타고 핏물이 주르륵 흘렀다. 간혹 섞여 나오는 정체불명의 덩어리는…… 시발. 내장 조각이다.

‘제대로 당했군.’

흐릿한 시야 너머로 걸어오는 조필이 보였다. 느긋한 걸음걸이에서 승자의 여유가 느껴졌다.

‘일어나야 해.’

손으로 옆을 더듬자 서늘한 창대가 잡혔다. 창을 지팡이 삼아 간신히 일어났을 때 조필의 찡그린 눈매가 보였다.

“칠 성의 화염신장(火焰神掌)을 맞고도 일어선단 말이지…… 손이 많이 가는 후배구먼.”

퍼벅!

또다시 그의 일장(一掌)이 작렬했다. 화염신장이라는 이름만큼이나 위력도 대단했다. 상의가 타들어 가고 살갗이 녹아 문드러졌다. 내부로 침투한 열기는 혈맥을 가닥가닥 끊었다.

“크헉.”

끔찍한 고통이 엄습한다. 그러나 고통에 몸부림치는 대신 조필의 급소를 향해 창을 찔러 넣었다.

턱.

“투견 같은 놈이군.”

창대를 잡아챈 조필이 혀를 찼다.

“자네 정도로는 날 어쩌지 못해.”

“좆…… 까!”

다음 순간, 나는 붙잡힌 창을 놓고 놈의 품속으로 뛰어들었다. 마지막 기회다. 모든 공력을 일점에 집중. 놈의 급소를 가격한다면 전세를 뒤집을 수 있다.

하지만…….

“헉.”

결과는 처참했다.

내상을 고려하지 않고 무리하게 공력을 끌어 올린 탓이다. 나는 그대로 쓰러져 번개에 맞은 것처럼 부들부들 떨었다.

입가에서 침이 줄줄 흐르는 것이 느껴졌다.

“푸핫. 푸하하! 이런 멍청한 놈을 봤나!”

조필이 광소를 터트리며 창날을 부러트렸다.

“자, 이제 어쩌지? 응? 태원진가의 막내 도련님?”

이제는 무기도 없다. 절망으로 눈앞이 캄캄해진다.

‘이렇게 죽는 건가?’

지난 7년간 지금만큼 죽음을 가깝게 느낀 적이 없었다. 천 번도 넘게 싸우고 살아남았던 내가. 고작 여기서 죽는다고?

이렇게 허무하게?

‘안 돼. 이렇게 죽을 수는…….’

손을 뻗었지만 거기까지였다.



- 조장!



노이즈 낀 외침을 마지막으로 모든 빛이 꺼졌다.



* * *



다시 눈을 떴을 때는 천국도, 지옥도 아니었다. 나는 땀에 흠뻑 젖은 상태로 헐떡이고 있었다. 온몸이 물먹은 솜처럼 무겁다.

‘꿈? 아니면 주마등?’

뭐든 간에 한 가지는 확실했다. 지금 이 상황이 과거, 그것도 7년 전의 기억이라는 사실이다. 낯익은 훈련 교관의 얼굴이 그 증거다.

“너, 너 이거…….”

교관은 말을 잇지 못했다. 그의 시선 끝에는 훈련용으로 제작된 강철 인형이 있었다. 몬스터의 형상을 본 따 제작된 그것은 이제 고철에 가까웠다. 온통 구부러지고 갈라진 고철.

“방금 그거 스킬이냐?”

과거의 내가 기진맥진한 목소리로 대답했다.

“있는 힘껏 찌르기요.”

“있는 힘껏 찌르기?”

“예. 그냥 있는 힘껏 찌르는 건데요.”

“어떻게 쓸 수 있는지는 잘 모르겠는데, 그냥 각성한 후부터는 자연스럽게 쓰게 됐고?”

“어, 네. 맞아요.”

“그게 스킬이야, 인마.”

황당한 표정의 교관이 손에 쥔 서류철로 시선을 돌렸다.

“진태경. 스무 살. 경기도 고양시 살고, F급 각성자. 이거 너 맞아?”

“네. 그런데요. 제 힘껏, 아니 스킬이요. 좋은 거 맞죠?”

“좋냐고?”

교관이 헛웃음을 지었다.

“훈련소에서만 15년짼데 이런 건 처음 본다. 이 정도면 최소 D급은 돼야 나올 만한 파괴력이니까.”

“시바, 이럴 줄 알았어. 저기 교관님. 저 퇴소할게요.”

“뭐?”

“그냥 심사 다시 보려고요. 솔직히 저 정도면 E급은 받아야 하잖아요.”

“아니, 그쪽에선 잘 판단한 것 같은데.”

“네?”

“스킬이 굉장한 건 맞아. F급에서 절대 나올 수 없는 수준이지. 그런데…….”

교관은 뒤통수를 긁적였다.

“너, 이거 못 쓴다.”

“왜, 왜요?”

“몸이 못 따라가. F급 수준의 마나와 신체 능력이 감당할 수 있는 스킬이 아냐. 네가 스킬 한 번 쓰고 퍼지는 이유도 거기 있지.”

“전 멀쩡한데요?”

“그래?”

고개를 끄덕이기도 전에 교관이 번개처럼 손을 뻗어 가슴을 툭 쳤다. 말 그대로 툭. 하지만 모든 힘을 소진한 나는 벌렁 자빠졌다.

온몸이 욱신거리는 통에 손 하나 까딱하기도 힘들다.

“이미 한계 이상의 힘을 내고 있어. 나중에 가면 단순히 쑤시는 정도로는 안 끝날 거다.”

“……다른 방법은요?”

“탄탄한 기본기와 훌륭한 테크닉. 그리고 너만의 전투 감각. 오래 살고 싶으면 스킬은 쓰지 마라. 아. 특별한 상황은 제외.”

“특별한 상황이요?”

교관이 씩 웃으며 덧붙였다.

“목숨이 위험한 상황. 그 스킬이 한 번쯤은 네 목숨을 살려 줄지도 모르지.”

다음 순간, 나는 차가운 눈밭 위에서 눈을 떴다.



* * *



“조장!”

마지막에 들었던 그 외침이 선명하게 들렸다. 엉망진창으로 망가진 몸 상태와 날카로운 고통도 느껴졌다.

‘아직 살아 있어.’

주마등은 아주 찰나의 순간에 불과했다. 조필은 손만 뻗으면 닿을 거리에서 뒤를 돌아보고 있었다.

“충성심이 제법이군. 실력은 형편없지만 말이야.”

놈의 시선 끝에는 한 무더기가 되어 달려오는 정찰조원들이 있었다.

“저놈들을 찢어 죽일까 하는데, 자네 생각은 어때?”

“……하게 싸웠어.”

“뭐?”

“멍청…… 싸웠어.”

나는 다시 한번 웅얼거렸다. 조필이 짜증난 얼굴로 허리를 숙였다.

“말도 똑바로 못하나?”

“그동안 멍청하게 싸웠다고.”

푸우웃!

기다리던 순간. 나는 놈의 얼굴을 향해 모아 둔 핏물을 뿜어냈다. 반 박자 빠르게 움직인 손은 놈의 발을 향해 내려 찍히고 있었다.

‘인벤토리 오픈.’

조필은 모르고 있다. 나는 헌터고 무림인이며, 시스템을 활용할 수 있는 유저라는 사실을!

‘비수 장착.’

텅 비었던 손아귀에 단단한 감촉이 느껴진다. 안면에 핏물을 뒤집어쓴 조필이 황급히 물러나려 했지만 이미 비수의 끝이 발등을 파고든 후였다.

푸푹!

“큭.”

절정 고수도 사람이다.

갑작스러운 고통에 놈의 몸이 덜컥 멈췄을 때 나는 비수를 놓고 발목을 향해 손을 뻗었다.

‘비수 장착.’

인벤토리에는 튜토리얼 때부터 해치운 적들의 무기가 쌓여 있다. 검, 창, 도끼, 비수…… 스무 자루가 넘는다.

조필의 부하들은 걸어 다니는 무기 창고였다.

서걱.

“크악!”

아킬레스건. 발목 힘줄을 끊자 비명이 터진다. 자세가 무너진 틈을 타 옆으로 구르며 비수를 휘두르고 쑤셨다. 남은 왼쪽 다리마저 피범벅이 되었다.

서걱. 푹. 푹. 푸푸푹!

분노와 고통으로 놈의 입이 쩍 벌어졌다.

“크아아악. 이 개새끼!”

두 다리를 못 쓰게 됐지만 조필은 절정 고수였다. 번개처럼 돌아서며 비수를 피한 그가 내 손목을 잡고 비틀었다.

우두둑.

“크악!”

공격은 거기서 끝나지 않았다. 붉게 달아오른 손바닥. 화염신장이다.

펑.

가슴이 움푹 꺼졌다. 눈앞이 새하얗게 물든다. 강력한 화기(火氣)가 몸속을 헤집었다.

펑.

몸에서 힘이 빠져나간다.

조필의 손아귀에 잡힌 목에서 뼈가 어긋나는 소리가 들렸다. 귓가로 스산한 목소리가 파고들었다.

“이제 깨달았겠지. 네가 누굴 건드렸는지.”

“……쿨럭.”

“염왕이 묻거든 내가 보냈다고 해라.”

말없이 시체처럼 축 늘어져 있는 내게, 조필이 환희에 찬 얼굴로 선언했다.

“죽어.”

그렇게 최후의 화염신장이 가슴을 향해 쏘아졌다. 붉게 타오르는 손바닥에는 내 생명을 송두리째 집어삼킬 용암이 깃들어 있었다.

그리고 마침내…….

턱.

세상이 정지했다. 용암도, 그 어떤 뜨거움도 없었다. 상처투성이에 못이 박힌 손바닥이 내 가슴을 짚었을 뿐이었다.

조필의 눈동자에 파문이 일었다.

“너…….”

목을 움켜쥔 손아귀에서 스르륵 힘이 빠진다. 주춤주춤 뒷걸음질 치는 조필의 배꼽 아래, 단전을 파고든 비수가 보였다.

“이게, 이게 도대체.”

다음 순간 조필의 턱을 타고 피가 흘렀다. 그건 시작에 불과했다. 두 눈, 코와 귀에서도 피가 흐르기 시작한 것이다. 칠공(七空)을 타고 흐르는 피의 폭포.

그 끔찍한 모습에 정찰조원들도 걸음을 멈췄다. 누군가 신음처럼 중얼거렸다.

“주화입마…….”

공력은 양날의 검이다. 나는 조필이 공력을 최고조로 끌어 올리는 순간을 기다렸고, 인벤토리에서 소환한 비수를 단전에 박아 넣었다.

그 결과는 공력의 역류. 주화입마다.

“분명히 넌 빈손이었는데.”

나는 피곤한 목소리로 대꾸했다.

“살다 보면 별일이 다 일어나는 법이지.”

“이렇게 죽을 수는 없어. 이건 말도 안 돼.”

조필은 넋 나간 사람처럼 중얼거리며 한 걸음씩 내디뎠다.

놈이 지나간 자리마다 피 웅덩이가 고였다.

“나는 조필이다. 일문일살 조필. 열화문의 십구 대 계승자. 너 같은 놈에게 죽어선 안 되는 몸이란 말이다!”

피를 뒤집어쓴 채 절규하는 조필의 모습에서 섬뜩한 귀기(鬼氣)가 느껴졌다. 결사의 각오로 뛰어왔던 정찰조원들도 두려움에 몸을 떨었다.

“그런데 왜, 네깟 놈에게 내가!”

그때. 꺼진 줄 알았던 불씨가 타올랐다.

변화는 조필의 몸에서 시작됐다. 흐르던 피가 멎고 전신의 핏줄이 푸르게 도드라진다. 그는 양발의 힘줄이 잘려 나간 고통도, 주화입마도 느끼지 못하는 사람 같았다.

내뱉는 숨에서 끔찍한 열기가 느껴졌다.

‘이게 뭐지?’

말 그대로의 부활? 아니다. 이건 조필의 마지막 발악이다.

모두가 공포에 사로잡혀 비명을 질렀지만 내게는 똑똑히 보였다. 시시각각 하얗게 세는 머리카락, 쪼그라드는 피부.

지금 놈은…… 생명을 태우고 있다.

‘나만큼은 죽이고 가겠다는 거겠지.’

가장 소중한 걸 버리면서 얻은 힘. 그 힘이 오롯이 나를 향하고 있다. 나는 본능적으로 피할 수 없다는 것을 깨달았다.

‘할 수 있을까, 내가?’

떨어져 있는 창을 주워들었다. 튜토리얼 때부터 지금까지 썼던 [예리한 창]이다. 창날이 부러진 그것은 이제 뾰족한 철봉에 불과했다.

‘나도 곧 이 꼴이 나겠군.’

남은 방법은 하나뿐.

성공하더라도 생명은 장담하지 못한다. 하지만 고민할 여유 따위는 없었다.

“진태경!”

“그래. 끝내자.”

나와 조필. 조필과 나.

우리는 서로를 향해 쏘아졌다. 놈에게서 뿜어져 나오는 열기에 쌓인 눈이 녹아내리고 입술이 바짝 말랐다. 나는 길게 호흡했다.

스읍. 후우.

주위의 소음이 멀어진다. 내 심장 박동과 호흡 소리가 천둥처럼 들렸다. 쿵. 쿵쿵. 쿵쿵쿵.

최고조에 다다른 심장 박동. 기계처럼 맞아떨어지는 호흡.

나는 확신했다.

‘지금.’

동시에 단전의 공력을 깨웠다. 기혈이 꼬이고 망가진 내부에 유일하게 남아 있는 건 바위처럼 굳은 제삼의 공력뿐이다.

유일한 선택지이자 내 스킬(Skill)을 채워 줄 마지막 한 조각.

‘네 멋대로 날뛰어라.’

깨어난 공력이 폭주했다. 망가진 기혈을 비집고 온몸으로 뻗쳐 나갔다. 아득한 고통이 느껴진다.

그러나 이내 공력이 주는 새로운 힘으로 잊혔다.

‘가라!’

전신의 근육이 팽팽하게 조여든다. 종아리와 허벅지, 허리를 지나 내질러지는 팔을 따라 전신의 모든 힘과 공력이 솟구쳤다. 부러진 창끝에서 응축된 공기가 터져 나간다.

그에 맞춰 조필이 화염신장을 내뻗었다.

“죽어어엇!”

콰아아아.

바람과 함께 눈 더미가 솟구쳤다. 나풀나풀 가라앉는 눈 사이로 조필의 모습이 드러났다.

화염신장을 펼쳤던 오른팔부터 어깨, 옆구리까지. 상반신의 절반이 증발해 버린 모습이었다.

“이게 무슨, 무공……?”

나는 창을 떨어트리며 대답했다.

“힘껏 찌르기.”

다음 순간 하늘과 땅이 뒤집혔다.

흐릿해지는 시야 너머로 이미 숨이 끊긴 조필의 목이 하늘 높이 솟구쳤다. 제 키만 한 검을 든 소천이 소리 내어 울고 있었다.
```

### Current accepted English

```markdown
# Chapter 30

*Whoosh.*

The instant Jopil’s red-hot palm struck my chest, energy as hot as lava swept through me. My breath caught, and my internal energy surged backward.

*What is this?*

The question came with me as I was sent flying. I slammed and rolled some ten zhang before I could stop.

“Cough.”

Blood trickled down my chin. The unidentified chunks mixed in with it now and then were… fuck. Pieces of organ.

*He got me good.*

Through my blurry vision, Jopil walked toward me. His unhurried stride had a victor’s ease.

*I have to get up.*

I groped beside me and found a cool spear shaft. Using the spear as a cane, I barely made it to my feet—and saw Jopil’s scowling eyes.

“You can still stand after taking a seventh-stage Flame Divine Palm… What a high-maintenance junior.”

*Wham!*

His palm detonated into me again.

The Flame Divine Palm was every bit as powerful as its name. My shirt burned away, and my flesh melted and sloughed off. The heat that sank inside me severed my blood channels strand by strand.

“Guh.”

Horrible pain crashed in. Instead of writhing in it, I drove the spear at Jopil’s vital point.

*Thunk.*

“You’re like a fighting dog.”

Jopil snatched the spear shaft and clicked his tongue.

“Someone at your level can’t do anything to me.”

“Go… fuck yourself!”

The next moment, I let go of the seized spear and threw myself into his chest.

Last chance. Focus every bit of internal energy on a single point. If I struck his vital point, I could turn the tide.

But…

“Gasp.”

The result was disastrous.

I had forced my internal energy up without accounting for my internal injuries. I collapsed on the spot and shook like I’d been struck by lightning.

I could feel drool running from the corner of my mouth.

“Pfft. Puhahaha! Have you ever seen such a stupid bastard!”

Jopil burst into mad laughter and snapped the spearhead.

“Well? What now? Huh? Youngest Young Master of the Jin Family of Taiyuan?”

I had no weapon left. Despair blacked out my vision.

*Am I going to die like this?*

In the last seven years, I had never felt death this close. Me—who had fought more than a thousand times and lived. Die here, of all places?

This pointlessly?

*No. I can’t die like this…*

I reached out, but that was as far as I got.

—Squad Leader!

A shout crackling with static was the last thing I heard before all the light went out.

* * *

When I opened my eyes again, it was neither heaven nor hell. I was drenched in sweat and panting. My whole body felt heavy, like waterlogged cotton.

*A dream? Or my life flashing before my eyes?*

Either way, one thing was certain. This was the past—a memory from seven years ago. The familiar face of the training instructor was proof enough.

“You—you, this…”

The instructor couldn’t finish. His eyes were on a steel dummy built for training. Modeled after a monster, it was little more than scrap metal now.

Bent and split scrap, head to toe.

“Was that a skill just now?”

My younger self answered in an exhausted voice.

“Thrust with All My Might.”

“Thrust with All My Might?”

“Yes. I just thrust as hard as I could.”

“You don’t really know how to use it, but after Awakening you just started using it naturally?”

“Uh, yes. That’s right.”

“That’s a skill, you idiot.”

Looking incredulous, the instructor turned to the file in his hand.

“Jin Taekyung. Twenty years old. Lives in Goyang, Gyeonggi Province. F-rank Awakened. Is this you?”

“Yes. So? My full-power thrust—no, my skill. It’s good, right?”

“You’re asking if it’s good?”

The instructor let out a hollow laugh.

“I’ve been at this training center for fifteen years, and I’ve never seen anything like this. Destructive power like that should be at least D-rank.”

“Fuck, I knew it. Uh, Instructor. I’m leaving.”

“What?”

“I’m going to get reevaluated. Honestly, with power like that, I should at least be E-rank.”

“No. They seem to have judged you correctly over there.”

“What?”

“The skill really is incredible. It’s a level that could never come out of an F-rank. But…”

The instructor scratched the back of his head.

“You can’t use it.”

“Why? Why not?”

“Your body can’t keep up. That skill is beyond what F-rank mana and physical ability can handle. That’s why you collapse after using it once.”

“But I’m fine.”

“Are you?”

Before I could even nod, the instructor’s hand shot out like lightning and tapped my chest.

Literally a tap. But I’d used up all my strength, so I flopped onto my back.

My whole body throbbed. I could barely twitch a finger.

“You’re already putting out more power than your limits can handle. Later on, it won’t end with a little soreness.”

“…Is there another way?”

“Solid fundamentals and excellent technique. And your own combat sense. If you want to live a long time, don’t use that skill. Ah. Except in special circumstances.”

“Special circumstances?”

The instructor grinned and added,

“When your life is in danger. That skill might save you once.”

The next moment, I opened my eyes on the cold snowfield.

* * *

“Squad Leader!”

The shout I’d heard at the end came through clearly. So did my wrecked body, and the sharp pain.

*I’m still alive.*

The flash of my life had lasted only an instant. Jopil was looking behind him, close enough to reach if I stretched out a hand.

“Not bad loyalty. Their skill’s pathetic, though.”

The reconnaissance squad was charging toward us in a cluster, right where he was looking.

“I’m thinking of tearing those guys apart and killing them. What do you say?”

“…dly. Fought.”

“What?”

“Stupid… fought.”

I mumbled it again. Jopil bent down, irritated.

“Can’t you even talk straight?”

“I said I’ve been fighting stupidly this whole time.”

*Ptoo!*

The moment I’d been waiting for.

I spat the blood I’d gathered at his face. Half a beat faster, my hand was already slamming down toward his foot.

*Inventory Open.*

Jopil didn’t know. I was a Hunter, a man of Murim, and a player who could use the System!

*Equip Dagger.*

A solid weight filled my empty grip. Jopil, his face covered in blood, tried to jerk back, but the dagger’s tip had already punched through the top of his foot.

*Shunk!*

“Guh.”

Even a Peak master was still human.

When his body jerked to a halt from the sudden pain, I dropped the dagger and reached for his ankle.

*Equip Dagger.*

My Inventory was piled with weapons from enemies I’d taken down since the Tutorial. Swords, spears, axes, daggers… more than twenty of them.

Jopil’s men had been a walking armory.

*Slice.*

“Gaaah!”

The Achilles tendon. The moment I cut the tendon at his ankle, a scream burst out of him. As his stance collapsed, I rolled aside, slashing and stabbing. His remaining left leg was soaked in blood too.

*Slice. Thrust. Thrust. Stab-stab-stab!*

Jopil’s mouth fell open with rage and pain.

“Gaaaaah! You son of a bitch!”

He couldn’t use either leg, but Jopil was a Peak master. He spun like lightning, slipped the dagger, caught my wrist, and twisted.

*Crack.*

“Gah!”

The attack didn’t end there.

A red-hot palm.

The Flame Divine Palm.

*Boom.*

My chest caved in. My vision went white. Powerful fire qi tore through my body.

*Boom.*

The strength drained out of me.

From the neck in Jopil’s grip came the sound of bone slipping out of place. A chilling voice slid into my ear.

“You understand now, don’t you. Who you picked a fight with.”

“…Cough.”

“If King Yama asks, tell him I sent you.”

To me, hanging limp as a corpse, Jopil declared it with a face full of rapture.

“Die.”

The final Flame Divine Palm shot toward my chest. Lava that would swallow my life whole was imbued in that blazing palm.

And at last…

*Tap.*

The world stopped.

No lava. No heat of any kind. Only a scarred, callused palm resting against my chest.

A ripple ran through Jopil’s eyes.

“You…”

The grip on my throat slipped away. As Jopil staggered backward, I saw the dagger driven in below his navel—buried in his dantian.

“This… what the hell is this?”

The next moment, blood ran down Jopil’s chin.

That was only the beginning.

Blood started pouring from his eyes, his nose, and his ears as well. A waterfall of blood streamed from his seven orifices.

The reconnaissance squad stopped in their tracks at the horrifying sight. Someone muttered, almost a groan.

“Qi deviation…”

Internal energy was a double-edged sword.

I had waited for the moment Jopil drew his internal energy to its peak, then driven a dagger summoned from my Inventory into his dantian.

The result was a reversal of internal energy. Qi deviation.

“You were definitely empty-handed.”

I answered in a tired voice.

“You live long enough, all sorts of things happen.”

“I can’t die like this. This makes no sense.”

Jopil muttered like a man whose soul had left him and took one step after another.

Wherever he passed, pools of blood collected.

“I am Jopil. Jopil, One Question, One Kill. The nineteenth-generation successor of the Fire Gate Clan. I’m not someone who should die at the hands of a nobody like you!”

A chilling, ghostly aura came off him as he screamed, covered in blood. Even the reconnaissance squad members who had charged in ready to die were shaking with fear.

“Then why? Why, at the likes of you, would I—!”

That was when the ember I’d thought extinguished burst into flame.

The change started in Jopil’s body. The flowing blood stopped, and the veins all over him stood out blue. He looked like a man who couldn’t feel the pain of both tendons being cut—or even the qi deviation.

A terrible heat poured from his breath.

*What is this?*

A literal resurrection?

No. This was Jopil’s last desperate struggle.

Everyone screamed, seized by terror, but I could see it clearly. His hair was turning white by the second. His skin was shriveling.

Right now, that man was…

*Burning his life.*

*He’ll kill me, at least, before he goes.*

Power gained by throwing away the most precious thing he had. Every bit of it was aimed at me. I knew on instinct that I couldn’t dodge.

*Can I do this? Me?*

I picked up the fallen spear.

The *Sharp Spear* I’d used from the Tutorial until now.

Its spearhead was broken. Nothing left but a pointed iron rod.

*I’ll end up looking like this soon enough.*

I had only one option left.

Even if I succeeded, I couldn’t guarantee I’d live. But there was no luxury of hesitation.

“Jin Taekyung!”

“Yeah. Let’s finish this.”

Me and Jopil.

Jopil and me.

We shot toward each other. The heat pouring off him melted the piled snow and dried my lips. I drew a long breath.

*Sss. Hoo.*

The noise around me receded. My heartbeat and breathing sounded like thunder.

*Thump. Thump-thump. Thump-thump-thump.*

My heartbeat hit its peak. My breathing locked in, precise as a machine.

I was certain.

*Now.*

At the same time, I woke the internal energy in my dantian. Inside me, where my qi and blood channels were twisted and wrecked, the only thing left was the third internal energy, hardened like rock.

My only option—and the last piece that would fill my Skill.

*Run wild as you please.*

The awakened energy went berserk. It forced its way through my ruined qi and blood channels and spread through my whole body. A dizzying pain hit me.

But it was soon forgotten in the new strength the energy gave me.

*Go!*

Every muscle in my body pulled taut. From my calves and thighs, through my waist and along my thrusting arm, every bit of strength and internal energy in me surged forward.

Condensed air burst from the broken spear tip.

Matching it, Jopil thrust out his Flame Divine Palm.

“Dieeeee!”

*Whoooosh.*

A mound of snow erupted with the wind. Through the flakes drifting gently back down, Jopil came into view.

From the right arm that had unleashed the Flame Divine Palm, through his shoulder and his side—half of his upper body had evaporated.

“What kind of martial art…?”

I dropped the spear and answered.

“Thrust with All My Might.”

The next moment, heaven and earth flipped.

Beyond my blurring vision, Jopil’s already lifeless head shot high into the sky.

Socheon was crying out loud, holding a sword as tall as he was.
```
## Chapter 31

### Korean source

```text
＃31화



“어쭈. 이 자식은 팔자도 좋네.”

슬며시 눈을 뜨자 익숙한 얼굴이 보인다.

“소풍 왔냐? 게이트에서 잠을 자?”

깜빡 졸았던 모양이다. 나는 뻔뻔한 얼굴로 대꾸했다.

“안 잤어요. 자긴 누가 잤다고 그래.”

“입가에 침 자국이나 닦고 구라를 쳐라.”

“씁.”

“어이고, 이걸 확.”

주먹을 흔들어 보였지만 입가에는 웃음이 맺혀 있다. 나는 뻐근한 목을 주물렀다.

“어우, 피곤해.”

“어제 여자라도 만났냐. 왜 레이드 뛰면서까지 병든 닭처럼 꾸벅꾸벅 졸아?”

“제가 여자 만날 시간이 어디 있어요. 사정 뻔히 아시면서.”

“그렇긴 하지.”

첫 전투 때부터 지금까지, 5년이나 동고동락한 처지다. 내가 그를 잘 아는 것처럼 그도 나를 잘 알았다.

“그럼 왜 그러는데?”

“왜 그러겠습니까. 돈 때문이지.”

“돈? 설마 너 투잡 뛰냐?”

한껏 낮아진 목소리다. 나는 그의 등 너머로 휴식을 취하고 있는 팀원들을 바라보며 고개를 끄덕였다.

“와, 이 자식 이거. 짬밥 좀 먹었다고 뒷주머니를 차네. 그것도 부팀장이라는 놈이.”

“요즘 레이드도 줄었고, 급해서 그래요. 급해서. 형님도 다 해 봤으면서 그러시네.”

프로 라이센스를 가진 헌터는 투잡이 법적으로 금지되어 있다. D급만 되어도 이렇게 살지는 않을 텐데, 우리 같은 F급들은 별수 없다. 그런 사정을 알기 때문에 길드에서 알아도 모른 척 넘어가는 거지.

“그렇긴 한데…… 조심해라. 관리청에 민원이라도 들어오면 골치 아파져.”

“믿을 만한 곳이에요. 페이도 당일 현찰로 받아서 문제없고. 제가 괜히 하겠습니까.”

“그래?”

표정을 보아하니 구미가 당기는 모양이다.

“형님도 돈 필요하세요?”

“애가 셋이다. 마당에 유전이라도 터져야 해.”

그는 슬픈 눈으로 말을 쏟아 냈다. 이미 수십 번 들었던 레퍼토리다. 육아의 괴로움과 분유값 상승, 장사치들의 파렴치함에 대해 울분을 토해 낸 뒤 내 어깨를 두드렸다.

“넌 결혼하지 마라.”

“안 해요.”

정확히는 못 하는 거지만.

여자도 없고, 돈도 없다. 5년 내로 안전 구역의 집을 한 채 사는 게 인생의 목표인 나로서는 내심 그가 부러웠다.

사랑하는 배우자와 아이들. 행복한 가정. 그런 걸 언제쯤 가질 수 있을지 모르겠다.

“결혼은 늪이야.”

말은 저렇게 해도 소문난 애처가에 좋은 아빠다. 가끔 가족사진을 꺼내 보면서 흐뭇하게 웃는 것을 나는 알고 있었다.

“인생이 빨려 들어가. 정신 차려 보면 가슴까지 파묻혀서 간신히 숨만 쉬고 있다니까.”

“…….”

잘못 알고 있었을 수도 있겠다.

“그러니까 너무 일만 하지 말고 쉬면서 해, 쉬면서. 연애, 취미 생활 이런 거 좋잖아.”

“글쎄요. 아직은 돈이 급해서.”

머리를 긁적이며 대답했다. 그가 안쓰러운 눈으로 바라본다.

“아까 보니까 식은땀까지 흘려 가면서 자던데. 그러다가 과로로 훅 간다.”

“제가요?”

그러고 보니 등허리가 식은땀으로 축축하다. 뭔가 안 좋은 꿈을 꾼 모양인데…….

‘기억이 안 나네.’

보나 마나 개꿈이겠지, 뭐.



* * *



게이트(Gate).

지금이야 나 같은 헌터들의 밥줄 역할을 하고 있지만 그 실체는 마계 군단의 침공 루트다.

마왕 아스모데우스가 쓰러지면서 그의 강대한 군대도 패퇴했지만 수십 년이 지난 지금도 게이트만은 남아 있었다.

“수비 대형!”

그의 지휘에 따라 거대한 타워 실드를 짊어진 헌터 셋이 전방을 막았다. 길이 좁은 동굴에서는 이 정도만으로 대부분의 공격을 해소할 수 있다.

캉. 카캉!

“끼이이익!”

이십여 마리의 고블린이 독침과 도끼, 창을 투척했지만 크고 아름다운 타워 실드에 모두 튕겨 나갔다.

“궁수!”

전방에서는 탱커가 모든 공격을 막아 내고, 후방에서는 궁수가 화살을 쏟아 낸다. 전진 압박을 가하며 절반가량을 쓰러트리자 고블린들이 당황한 울음을 토해 냈다.

“까아아악!”

“끼익!”

때에 맞춰 그가 명령했다.

“공격 대형!”

탱커들이 타워 실드를 떨어트리는 동시에 뛰쳐나간다. 하지만 그보다 내가 더 빨랐다.

“핫!”

철창을 크게 휘두르자 초록색 피가 터지며 선두가 흐트러진다. 그 사이로 뛰어들며 닥치는 대로 찌르고 베자 대열이 우르르 무너져 내렸다.

“돌격!”

이어 딜러와 탱커들이 가세하자 고블린 무리는 순식간에 시체가 되어 누웠다.

“오늘 되게 쉬운데?”

“솔직히 부팀장이 반은 했지. 아주 날아다니던데, 언제 저렇게 실력이 좋아졌…… 쉿. 팀장님 열받았다.”

잡담을 나누던 사람들은 그가 나타난 순간 입을 다물었다.

“야, 진태경!”

깜짝이야.

멍하니 생각에 빠져 있던 나는 화들짝 놀라 반문했다.

“왜요?”

“너 인마, 누가 단독 행동 하래? 네가 탱커야? 공격 순서 다 잊었어? 그러고도 네가 부팀장이야?”

“그게 아니라요…….”

“이따위로 할 거면 팀 옮겨. 다른 팀원들까지 위험해지니까.”

그의 험악한 얼굴을 보다가 한숨을 내쉬었다.

“죄송합니다. 제가 왜 그랬는지 모르겠어요. 그냥, 갑자기 별것 아닌 것 같더라고요. 잠깐 미쳤나 봐요.”

기분이 묘했다. 고블린 무리를 보는 순간, 혼자서 저놈들을 쓸어버릴 수 있다는 생각이 들었다. 아니, 그건 확신이었다.

“너…….”

그가 말을 삼켰다. 서로 등을 맡기고 싸워 온 지 어언 5년, 지금 같은 돌발 행동은 이번이 처음이었다.

“다음부턴 이러지 마라. 힘든 일 있으면 말하고.”

어깨를 두드리고 떠나는 그의 뒷모습을 바라봤다. 왠지 모르게 가슴 한구석이 욱신거렸다.

‘병원이라도 가 봐야 하나.’

하지만 통증 따위는 이내 신경도 쓰지 않게 되었다.



* * *



“마정석 나왔습니다!”

“나왔어요!”

“또!”

“떴다. 떴다. 떴다!”

“엄마! 하연아!”

아, 마지막 외침은 내가 한 거다. 그도 잔뜩 달아오른 얼굴로 중얼거린다.

“야, 이게 다 뭐냐…….”

바닥에는 크고 작은 스무 개의 마정석이 가지런히 놓여 있었다.

마정석. 겉보기에는 붉은 돌멩이지만 게이트의 꽃이라 불리는 물건이다. 몬스터가 지닌 이 마력 덩어리는 고차원 에너지인 동시에 몬스터의 부산물 중 가장 값진 거다.

“이 정도면 개당 백만 원은 넘겠는데.”

E급 헌터로 이 바닥에서 10년을 버틴 팀장의 말이다. 그 황홀한 광경에 사람들의 눈동자가 스르르 풀어졌다.

“원래 이런 건가요?”

신입의 질문에 모두가 맹렬히 고개를 흔들었다.

“절대 아니지.”

F급 게이트에서는 평균이 한두 개고 아무리 운이 좋아도 다섯 개를 못 채운다. 나는 돈 계산에 바빴다.

‘마정석만 최소 이천 잡고, 부산물에 장비까지 하면 오백. 거기에 각종 수당까지 더하면…….’

시발. 이게 다 얼마야. 헌터를 시작한 이래 최고의 대박이다.

심지어 아직 레이드가 끝난 것도 아니다.

“우리가 지금 얼마쯤 왔지?”

“거의 다 왔죠. 오른쪽 길로 꺾으면 바로 보스 존이에요.”

보스 존. 그 단어에 모두의 눈이 번쩍였다.

당연한 말이지만, 보스 존에는 보스가 있다. 보스 몬스터는 해당 게이트에서 가장 강력한 몬스터. 그리고 가장 비싼 부산물과 장비, 마정석을 갖고 있는 몬스터다.

‘보스 몬스터까지 잡으면?’

말 그대로 잭팟이다. F급 헌터로 살아가면서 다시없을 절호의 기회인 것이다. 모두가 그런 생각으로 환하게 웃고 있던 그때였다.

“잠깐. 생각 좀 해 보고.”

아니, 이 인간이 지금 뭐라는 거야?

“그게 무슨 말이에요?”

“그렇잖아. 마주치는 몬스터는 일반 고블린뿐인데. 마정석이 이렇게 많이? 아무래도 이상해.”

그가 한숨을 내쉬었다. 아직도 흥분이 채 가라앉지 않아 붉은 얼굴에는 갈등이 떠올라 있었다.

“너희 기분 알아. 아는데…… 이미 엄청나게 챙겼다. 이 정도에서 만족하고 돌아가자.”

만족? 지금 여기서, 여기까지 와서 돌아가자고?

나는 다른 팀원들을 바라봤다. 그중에는 2, 3년간 손발을 맞춘 이들도 있고, 신입도 있다. 하지만 다들 나와 같은 얼굴을 하고 있었다.

“저는 반대…….”

그 순간 숨이 턱 막혔다. 빌어먹을. 또 가슴 통증이다.

어떻게든 말을 이으려고 했지만 목소리가 나오지 않았다. 이제는 이명까지 들리기 시작한다.

‘이게 무슨.’

통증도, 이명도 점점 심해지고 있었다. 나는 무릎을 꿇고 숨을 헐떡였다.

‘누가 나 좀. 나 좀 도와줘.’

누군가의 바짓가랑이를 붙잡고 매달렸다. 바로 그다. 지난 5년간 형제처럼, 아버지처럼 나를 돌봐 준 그였다.

‘형. 제발 저 좀 살려 줘요.’

그가 덤덤한 시선으로 날 내려다봤다.

“내가? 모두를 두고 도망친 너를?”

뭐?

“나도 살고 싶었어.”

나는 통증도 잊고 멍하니 그를 바라봤다. 옷과 피부가 녹아내리고 뼈가 드러났다. 나를 제외한 모두가 해골이 되어 널브러졌다.

‘아. 그랬었지.’

모두 죽었다. 2년 전 그날. 내가 가자고 주장했던 그 보스 존에서 모두가 죽었다.

‘나 혼자 살아남았어.’

나는 기억에 파묻혀 허우적거렸다. 보스 존에 내려앉은 불길한 어둠. 불쾌한 냄새와 축축한 바닥을 떠올렸고 놈의 거대한 날개를 기억했다.

허공에서 갈기갈기 찢겨 나가는 시신. 공포에 질린 비명과 도망치는 사람들.



‘이런 개새끼가!’



하지만 내 모든 걸 쏟아부은 스킬로도 놈을 죽일 수 없었다. 죽음을 기다리고 있던 나를 그가 일으켜 세웠다.



‘태경아!’

‘형, 미안해요. 전부 제 잘못이에요.’



나만 아니었으면. 내가 욕심을 부리지 않았다면 모두가 살 수 있었을 텐데. 가족에게 돌아갈 수 있었을 텐데.

어린애처럼 엉엉 우는 내게 그는 애써 미소를 지어 보였다.



‘그게 왜 네 책임이야? 자식이 이제는 팀장 흉내까지 내고 있어.’



거대한 동체가 동굴을 부유했다. 종유석이 쏟아지고 마지막 팀원이 단말마를 내질렀다. 어둠 속, 놈의 붉은 눈동자가 우리를 향했다.



‘저 건방진 새끼. 태경아. 먼저 가라.’

‘형. 천수 형!’



가슴이 아팠다. 눈앞이 아득해질 정도의 고통이 밀려들어 왔다. 용암을 삼킨 것처럼, 내 안의 모든 것들이 타들어 가는 것 같았다. 간간이 들리던 이명은 괴물의 포효로 바뀌었다.

캬우우우!



* * *



“형-!”

비명과 함께 눈을 떴다. 하지만 그곳은 게이트가 아니었고 몬스터도, 팀원들도 없었다. 햇빛이 쏟아지는 창가에서 한 사람이 일어났다.

“주군에 관한 꿈을 꾸신 겁니까? 전해 드리면 좋아하시겠군요.”

차가움이 뚝뚝 묻어 나오는 얼굴. 진위경의 오른팔인 위팽이다. 그를 보자 아직 게임 속이라는 것이 실감이 났다.

“괜찮으십니까?”

“아뇨. 악몽이었어요.”

“그럼 그 부분은 빼고 전하겠습니다.”

“마음대로.”

땀으로 온몸이 흠뻑 젖어 있었다. 온몸에 칭칭 감긴 붕대 틈새로 피딱지가 돋은 살이 보인다.

“제가 얼마나 누워 있었죠?”

“닷새 동안 혼절해 계셨습니다. 상태가 워낙 위중해서 하루를 못 넘길 거라는 게 약왕당주의 결론이었고요.”

“그래요?”

“예. 그 얘기를 들은 주군께서 길길이 날뛰셨죠. 제가 안 말렸으면 약왕당주를 때려죽였을 겁니다.”

“아.”

며칠 전 회의 때 백호당주의 항문에 대침을 꽂아 넣겠다고 하던 늙은이가 생각났다. 아주 죽으라고 염불을 외웠구나.

“다른 일들은 없었나요?”

“많은 일이 있었죠. 그중에서도 좋은 소식과 더 좋은 소식이 있는데…… 어느 것부터 들으시겠습니까?”

“좋은 소식부터.”

“우선 정찰조와 삭주 지부의 생존자들은 무사히 복귀했습니다. 그중 두 명은 제법 큰 부상을 입긴 했지만 목숨에는 지장이 없을 겁니다.”

생존자. 그 세 글자에 가슴이 덜컥 내려앉는다.

‘칠 호.’

목과 미간에 비수가 박힌 채 마지막 숨을 토하던 그 얼굴이 떠올랐다. 기껏해야 스물이나 되었을까. 목숨을 잃기에는 너무 어린 나이였다.

“죽은 이를 생각하십니까?”

“시신은, 시신은 수습했나요?”

“잘 수습하여 장사 지냈습니다. 천애 고아인지라 유족이 없더군요.”

“…….”

“한 말씀 드려도 되겠습니까?”

위팽은 대답을 기다리지 않았다. 그가 나를 향해 한발 다가오며 입을 열었다.

“삼공자, 수하의 죽음을 개죽음으로 만들지 마십시오.”

“그게 무슨…….”

“무인은 보호받는 존재가 아니라 적과 싸워 스스로를 증명하는 자들입니다. 비록 손쓸 수 없을 만큼 강한 적을 만나 죽었지만, 사망(死亡)이 아닌 전사(戰事)라는 말입니다.”

전장에서 죽었으니 영예로운 죽음이라는 말은 희대의 개소리다. 영예로운 죽음은 없다. 지금도 2년 전 죽은 동료들의 비명과 숨이 끊긴 칠 호의 부릅뜬 눈이 생생하다.

“죽었다는 사실은 변하지 않아요.”

“결코 변하지 않는 사실에 집착하는 사람도 있더군요. 누구라고는 말하지 않겠습니다.”

“…….”

“후회됩니까?”

“당연히.”

“그럼 그의 몫까지 사십시오.”

위팽이 이제껏 들어 본 적 없는 부드러운 목소리로 말을 이었다.

“죽은 이들을 잊으라는 말이 아닙니다. 가슴에 묻고, 머리에 새기라는 뜻입니다. 그 후회를 발판 삼아 그들이 꿈꿨던 곳까지 비상하는 것이 공자가 가야 할 길입니다.”

내가 가야 할 길이라…….

듣는 것만으로도 가슴 한구석이 울렁거리는 그 한마디를 곰곰이 생각하다가 풀썩 웃어 버렸다.

“젠장. 가다가 다리 부러지겠네.”

“일평생이 걸리겠죠.”

“일평생을 바치면 도착할 수 있을까요?”

“모릅니다. 저도 제 길이 어디까지인지 모르는데 공자의 길을 어찌 알겠습니까.”

“위 대협이 가는 길 끝에는 뭐가 있는데요?”

“천하제일인(天下第一人).”

농담? 아니다. 지금의 위팽은 그 어느 때보다 진지하고, 단호했다.

“어렵네요.”

“꿈이니까요.”

맞다. 꿈이란 늘 이루기 어렵다. 떠나보낸 이들의 꿈까지 짊어진다면 더더욱.

“위 대협. 한 가지만 물어봐도 될까요?”

“얼마든지요.”

“그 녀석, 이름이 뭐였습니까?”

“그의 이름은…….”

위팽의 입술이 열린 순간, 겨울 찬바람이 창문을 흔들었다.

휘이잉. 서늘한 바람 소리 너머로 칠 호의 이름이 들려온다.

“멋진 이름이네요.”

“본인이 직접 지었다고 들었습니다. 그만큼 꿈도 컸죠.”

“뭔데요?”

“고금제일인(古今第一人).”

“…….”

“고생 좀 하실 겁니다.”

“그러게요. 어이가 없네.”

실소가 터져 나온다. 그제야 무거웠던 마음이 홀가분해진 것이 느껴졌다. 모두 위팽 덕분이다.

“이제야 좀 원래대로 돌아왔군요.”

“고맙습니다.”

“별말씀을.”

고개를 까딱인 위팽이 입을 열었다.

“이제 더 좋은 소식이 남았군요.”

아, 그랬지. 좋은 소식과 더 좋은 소식.

나는 한껏 기대하며 이어질 말을 기다렸다.
```

### Current accepted English

```markdown
# Chapter 31

“Well, look at this. This bastard’s got it made.”

I slowly opened my eyes to a familiar face.

“Did you come here for a picnic? Sleeping in a Gate?”

I must have dozed off. I answered, shameless.

“I wasn’t sleeping. Who says I was?”

“Wipe the drool off your mouth before you start lying.”

“Tsk.”

“Oh, you little—”

He shook a fist at me, but a smile sat at the corners of his mouth. I rubbed my stiff neck.

“Ugh, I’m tired.”

“Did you meet a woman yesterday? Why are you nodding off like a sick chicken even in the middle of a raid?”

“When would I have time to meet a woman? You know my situation.”

“True enough.”

We’d been through thick and thin for five years, from our first battle until now. He knew me as well as I knew him.

“Then what’s wrong?”

“What do you think? Money.”

“Money? Don’t tell me you’re moonlighting.”

His voice dropped low. I looked past his shoulder at the team members resting nearby and nodded.

“Well, well. This bastard gets a little time under his belt and now he’s stuffing his back pocket. And he’s the vice team leader, no less.”

“Raids have been scarce lately, and I’m strapped. Really strapped. You’ve done it yourself, hyung, so don’t give me that.”

Hunters with professional licenses were legally barred from second jobs. Even a D-rank probably wouldn’t have to live like this, but F-ranks like us had no choice. That was why the Guild looked the other way even when they knew.

“True, but… be careful. If someone files a complaint with the Management Agency, it’ll become a real headache.”

“It’s a trustworthy place. They pay cash the same day, so there’s no problem. You think I’d do this for nothing?”

“Really?”

Judging by his face, he was tempted.

“Do you need money too, hyung?”

“I’ve got three kids. I’d need an oil well to blow in the yard.”

He poured it out with a miserable look. I’d already heard this routine dozens of times. After venting about the misery of raising kids, the rising price of formula, and the shamelessness of merchants, he patted my shoulder.

“Don’t get married.”

“I won’t.”

More precisely, I couldn’t.

I had no woman and no money. My life’s goal was to buy a house in a safe zone within five years, so deep down I envied him.

A spouse I loved, and kids. A happy family. I had no idea when I’d ever get something like that.

“Marriage is a swamp.”

For all that talk, he had a reputation as a devoted husband and a good father. I knew how he sometimes took out his family photos and smiled fondly at them.

“Your whole life gets sucked in. You come to your senses and you’re buried up to your chest, barely breathing.”

“…”

Maybe I’d had the wrong idea about him.

“So don’t just work. Take breaks. Dating, hobbies—stuff like that’s good for you.”

“I don’t know. I still need the money.”

I scratched my head as I answered. He looked at me with pity.

“I saw you sleeping earlier, sweating cold the whole time. Keep that up and you’ll drop dead from overwork.”

“Was I?”

Now that he mentioned it, my back was damp with cold sweat. Must have been a bad dream…

*Can’t remember.*

Probably just some stupid dream anyway.

* * *

A Gate.

These days it was how Hunters like me made a living, but its true nature was an invasion route for the Demon Realm’s army.

When Demon King Asmodeus fell, his mighty army was routed with him. Decades later, the Gates were still there.

“Defensive formation!”

At his command, three Hunters bearing huge tower shields blocked the front. In a narrow cave, that alone was enough to soak most attacks.

*Clang! Clang-clang!*

“Giiiiik!”

About twenty goblins hurled poison needles, axes, and spears, but every one of them bounced off those big, beautiful tower shields.

“Archers!”

Up front, the tanks blocked every attack. From the rear, the archers poured arrows. We pushed forward and dropped about half of them, and the goblins let out panicked cries.

“Gyaaaah!”

“Kieek!”

He timed the next order perfectly.

“Attack formation!”

The tanks dropped their tower shields and burst forward at the same time. I was faster.

“Hah!”

I swung the iron spear in a wide arc. Green blood burst, and the front rank broke. I dove into the gap, stabbing and cutting at everything I could reach, and the line came crashing down.

“Charge!”

The damage dealers and tanks piled in, and in an instant the goblin pack was a pile of corpses.

“Pretty easy today, huh?”

“Honestly, the vice team leader did half of it. He was flying around. When did he get that good…? Shh. The Team Leader’s pissed.”

The people chatting shut their mouths the moment he appeared.

“Hey, Jin Taekyung!”

That made me jump.

I’d been staring off, lost in thought, and I startled as I answered.

“What?”

“Who told you to go solo? Are you a tank? Forget the attack order? And you still call yourself vice team leader?”

“That’s not—”

“If you’re going to act like this, transfer teams. You’re putting the rest of them in danger too.”

I looked at his grim face and sighed.

“I’m sorry. I don’t know why I did that. They just… suddenly didn’t seem like a big deal. I must have lost it for a second.”

The feeling was strange. The moment I saw the goblin pack, I’d thought I could wipe them out by myself.

No. That hadn’t been a thought.

It had been certainty.

“You…”

He swallowed the rest. We’d had each other’s backs for five years now, and this was the first time I’d ever pulled something like this.

“Don’t do it again. If you’re having a hard time, tell me.”

I watched him walk away after patting my shoulder. For some reason, a spot in my chest throbbed.

*Should I see a doctor?*

But before long I wasn’t even thinking about the pain.

* * *

“Magic Gems!”

“Got some!”

“Another!”

“Jackpot! Jackpot! Jackpot!”

“Mom! Hayeon!”

Ah, that last shout was mine. His face was flushed too as he muttered.

“Hey, what is all this…?”

Twenty Magic Gems, large and small, lay neatly on the floor.

Magic Gems. They looked like red pebbles, but they were called the flower of the Gate. These lumps of mana that monsters carried were high-dimensional energy, and the most valuable byproduct a monster had.

“At this rate, each one’s got to be worth over a million won.”

That from the Team Leader, an E-rank Hunter who’d lasted ten years in this business. People’s eyes went slack at the intoxicating sight.

“Is it normally like this?”

At the new recruit’s question, everyone shook their heads hard.

“Absolutely not.”

In an F-rank Gate the average was one or two, and even with incredible luck you wouldn’t hit five.

I was busy doing the math.

*Twenty million from the Magic Gems alone, another five million for the byproducts and Equipment. Add all the various allowances and…*

*Fuck. How much is this?*

The biggest jackpot I’d hit since becoming a Hunter.

And the raid wasn’t even over yet.

“How far have we come?”

“Almost there. Turn right and it’s the boss zone.”

The words *boss zone* made everyone’s eyes light up.

It went without saying, but a boss zone had a boss. A boss monster was the strongest monster in that Gate—and the one with the most expensive byproducts, Equipment, and Magic Gems.

*If we take down the boss monster too?*

A literal jackpot. A once-in-a-lifetime chance for an F-rank Hunter.

Everyone was smiling bright at the thought when he spoke.

“Wait. Let me think.”

What the hell was he talking about?

“What do you mean?”

“Think about it. Every monster we’ve run into has been an ordinary goblin. This many Magic Gems? Something’s off.”

He sighed. Excitement still hadn’t left his flushed face, but there was conflict on it too.

“I know how you feel. I do… but we’ve already grabbed a fortune. Let’s be satisfied with this much and go back.”

Satisfied?

Here? After coming this far, turn back?

I looked at the other team members. Some had been in sync for two or three years; some were new. They all had the same look I did.

“I’m against—”

My breath caught.

*Damn it. The chest pain again.*

I tried to keep talking, but no voice came out. Now there was ringing in my ears too.

*What is this?*

The pain and the ringing got worse and worse. I dropped to my knees, gasping.

*Someone. Please, help me.*

I grabbed someone’s pant leg and hung on.

It was him. The man who’d looked after me like a brother, like a father, for the past five years.

*Hyung. Please save me.*

He looked down at me, indifferent.

“Me? You, who ran and left everyone behind?”

What?

“I wanted to live too.”

I forgot the pain and stared at him. Clothes and skin melted away, and bone showed through. Everyone except me had become skeletons, sprawled across the ground.

*Ah. That’s right.*

They were all dead.

That day two years ago. In the boss zone I had insisted we enter, they had all died.

*I was the only one who survived.*

I floundered, buried in the memories. I remembered the ominous darkness that had settled over the boss zone, the foul smell, the damp floor, and that thing’s enormous wings.

Bodies ripped to shreds in midair. Screams of terror. People running.

*You fucking bastard!*

But even the Skill I had poured everything into hadn’t been enough to kill it. As I waited to die, he pulled me to my feet.

*Taekyung!*

*Hyung, I’m sorry. It was all my fault.*

If it hadn’t been for me. If I hadn’t gotten greedy, everyone could have lived. They could have gone home to their families.

I wailed like a child, and he forced a smile.

*How is that your fault? Look at this kid, now you’re even playing Team Leader.*

The massive body drifted through the cave. Stalactites rained down, and the last member of the team let out a death cry. In the darkness, its red eyes turned toward us.

*That arrogant bastard. Taekyung, you go first.*

*Hyung. Cheonsu hyung!*

My chest hurt. Pain rolled in hard enough to blank my vision. It felt like I had swallowed lava, like everything inside me was burning away. The ringing in my ears turned into a monster’s roar.

*Kyaaaaau!*

* * *

“Hyung—!”

I woke with the scream.

But it wasn’t a Gate. There were no monsters, and no team members.

Someone stood up at the window, where sunlight poured in.

“Did you dream about my lord? He’ll be pleased if I tell him.”

Coldness dripped from his face.

Wipeng, Jin Wikyung’s right-hand man.

Seeing him made it real that I was still inside the game.

“Are you all right?”

“No. It was a nightmare.”

“Then I’ll leave that part out of the report.”

“Suit yourself.”

I was soaked in sweat. Through the gaps in the bandages wound tight around my whole body, I could see flesh raised with blood scabs.

“How long was I out?”

“You were unconscious for five days. Your condition was so critical that the Medicine King Hall Leader concluded you wouldn’t last the day.”

“Really?”

“Yes. When my lord heard that, he went berserk. If I hadn’t stopped him, he would have beaten the Medicine King Hall Leader to death.”

“Ah.”

I remembered the old man from the meeting a few days ago, the one who had threatened to shove a giant needle into the White Tiger Hall Leader’s anus.

*So he really had been chanting for me to die.*

“Did anything else happen?”

“A great deal happened. Among it, there’s good news and even better news. Which would you like to hear first?”

“The good news.”

“First, the reconnaissance squad and the survivors of the Sakju Branch returned safely. Two of them suffered fairly serious injuries, but their lives are not in danger.”

*Survivors.*

The word made my heart drop.

*Number Seven.*

I remembered his face as he gasped out his last breath, a dagger in his throat and another between his brows. Twenty at most. Far too young to lose his life.

“Are you thinking of the dead?”

“The body—did they recover the body?”

“We recovered it properly and buried him. He was an orphan with no one in the world, so there were no surviving relatives.”

“…”

“May I say something?”

Wipeng didn’t wait for an answer. He took a step toward me and went on.

“Third Young Master, do not turn your subordinate’s death into a dog’s death.”

“What does that…”

“Martial artists are not beings meant to be protected. They are people who fight their enemies and prove themselves. He died facing an enemy too strong to do anything about, but that was not mere death—it was death in battle.”

The idea that dying on a battlefield made it an honorable death was the biggest load of bullshit ever.

There was no such thing as an honorable death. Even now, the screams of my comrades who died two years ago and Number Seven’s wide-open eyes as his breath left him were still vivid.

“The fact that he died hasn’t changed.”

“There are people who cling to facts that will never change. I won’t say who.”

“…”

“Do you regret it?”

“Of course.”

“Then live his share as well.”

Wipeng continued in a gentler voice than I had ever heard from him.

“I’m not telling you to forget the dead. Bury them in your heart and carve them into your mind. Use that regret as a foothold and soar to the place they dreamed of reaching. That is the path you must take, Young Master.”

*The path I must take…*

Just hearing those words made something in my chest lurch. I turned them over for a while, then let out a sudden laugh.

“Damn. I’ll break a leg before I get there.”

“It will take a lifetime.”

“If I give it my whole life, can I make it there?”

“I don’t know. I don’t even know how far my own path goes, so how could I know yours?”

“What’s at the end of the road Great Hero Wipeng is walking?”

“Number One Under Heaven.”

A joke?

No. Wipeng was more serious and resolute than ever.

“That’s a hard one.”

“Because it’s a dream.”

He was right. Dreams were always hard to reach.

Even more so if you were carrying the dreams of those you had lost.

“Great Hero Wipeng. May I ask you one thing?”

“Anything.”

“That guy. What was his name?”

“His name was…”

The moment Wipeng opened his lips, a cold winter wind shook the window.

*Whoooosh.*

Beyond the chill of the wind, I heard Number Seven’s name.

“That’s a cool name.”

“I heard he chose it himself. His dream was just as big.”

“What was it?”

“Number One of All Time.”

“…”

“You’re going to have a hard time.”

“Yeah. That’s unbelievable.”

A laugh slipped out. Only then did I feel the weight in my heart lift.

It was all thanks to Wipeng.

“You’re finally back to your old self.”

“Thank you.”

“Don’t mention it.”

Wipeng tipped his head and spoke.

“Now, there’s still the even better news.”

Ah. Right.

Good news and even better news.

I waited, as expectant as I could get, for what he would say next.
```
## Chapter 32

### Korean source

```text
＃32화



“이틀 전 큰 전투가 있었습니다. 혼주(昏住)에서 본가의 정예 일백과 항산검문의 선봉 이백이 맞붙었죠.”

“전투가 있었다고요?”

심지어 수백 명이 투입된 큰 전투란다. 순간 가슴이 덜컥했지만 앞서 위팽이 했던 말이 생각났다.

좋은 소식과 더 좋은 소식. 결과는 이미 들은 셈이다.

“우리가 이겼군요.”

“대승입니다. 살아서 도망친 놈들은 서른이 채 되지 않습니다. 본가의 사상자 숫자와 비슷하죠.”

위팽의 이마부터 턱까지 그어진 상처를 보건대 상당히 격렬한 전투였던 모양이다.

‘하긴. 병력 차이가 두 배나 났으니까.’

아무튼 이겨서 다행이다. 태원진가 입장에서는 가문의 전력을 절반 가까이 쏟아부은 전투. 만약 졌다면 타격이 막대했을 것이다.

“항산검문의 소가주를 놓친 건 아쉽지만 항산쌍귀(恒山雙鬼)를 잡은 건 큰 수확입니다.”

“항산썅귀요?”

“항산쌍귀 말입니다. 항산검문 휘하의 절정 고수들인데…… 충성심 하나는 대단하더군요. 목숨을 도외시하고 덤비는 통에 어쩔 수 없이 죽였죠.”

위팽이 새로 생긴 상처를 톡톡 건드렸다.

“붙잡았다면 중요한 정보를 캐낼 수 있었을 텐데.”

“그쪽이, 아니 위 대협이 죽였나요?”

“주군과 제가 한 놈씩 맡았습니다. 제법이더군요.”

“…….”

호로록, 차를 들이켜는 위팽의 모습에 할 말을 잃었다.

‘이런 씨바…… 절정 고수가 장난이야?’

내 27년 인생을 통틀어 가장 치열한 싸움이었다. 온갖 내상에 스테이크처럼 칼질도 당했다. 그러고도 닷새 동안 뻗어 있었으니 요단강에서 반신욕 정도는 한 거다.

그런데 그 정도의 절정 고수를 잡아 놓고. 뭐, 제법이라고?

‘이건 완전히 괴물이잖아.’

이번 기회에 확실히 알았다. 절정 고수에도 급이 있다는 사실을. 그 정도의 고수들이 내 편이라는 게 천만다행이다.

“그건 그렇고.”

달그락.

찻잔을 내려놓은 위팽이 미묘한 눈빛으로 나를 응시했다.

“대단하시더군요.”

“예?”

“일문일살 조필 말입니다. 그를 해치운 건 대단하다는 말로도 표현이 불가능한 일입니다.”

“…….”

난 당신들이 더 대단해 보이는데. 이건 마치 A급 헌터에게 고블린 잘 잡는다고 칭찬받은 기분이다.

“아, 예. 뭐 감사합니다.”

조필에 관한 이야기는 이쯤에서 마무리 짓고 싶었다. 몸 상태도, 기분도 별로인 데다 밀려 있는 시스템 보상을 확인하고 싶었기 때문이다.

‘이제 좀 쉬자. 나 아직 환자야, 인마.’

그런 의미를 담아 윙크를 날리자 위팽이 눈살을 찌푸렸다.

“눈이 아프십니까? 의원을 부를까요?”

“……아뇨. 괜찮아요.”

“방금 눈 쪽에 경련이 일어났는데요.”

“그건 경련이 아닌데요.”

“맞습니다, 경련. 제대로 봤습니다.”

“아니, 방금 그건…….”

그때 위팽이 눈깔을 허옇게 뒤집고 부르르 떨었다.

탁자가 흔들리고 잔에서 찻물이 흘러넘쳤다. 나는 깜짝 놀라 외쳤다.

“세상에, 위 대협!”

이 인간 간질 환자구나. 아니, 무슨 절정 고수씩이나 되는 양반이 간질에 걸렸대?

내가 황급히 일어나려 할 때 떨림이 멈췄다. 정상으로 돌아온 위팽이 평온한 얼굴로 말했다.

“이러셨습니다.”

“괜찮으시…… 아니, 예?”

“삼공자께서 방금 이러셨다고요. 눈에 경련이 일어났어요.”

“그러니까. 절 따라 하신 거라고요?”

“예.”

아니, 이건 무슨 종류의 또라이야…….

나는 윙크와 간질의 차이를 설명해 주려 했지만, 말문이 막혔다. 위팽이 열받은 독재자처럼 나를 노려보는 중이었다.

“……그냥 조필 얘기나 마저 할까요?”

“그러시죠.”

위팽이 만족스럽게 고개를 끄덕였다.

‘또라이 새끼.’

결국 나는 조필과의 싸움을 처음부터 끝까지 털어놔야 했다.

그가 어떻게 움직였고 무슨 무공을 썼는지. 위팽의 날카로운 질문 때문에 긴장되는 순간도 있었다.

“비수로 조필의 다리 근맥을 끊으셨다고요?”

“네. 미리 숨겨 둔 거였죠.”

“조필이 그걸 못 알아차렸을 리가 없는데…… 계속하십시오.”

마침내 긴 이야기가 끝났을 때, 위팽은 참았던 숨을 토해 냈다. 나를 바라보는 눈빛에 복잡한 심정이 그대로 전해진다.

“삼공자. 실로 큰 공을 세우셨습니다.”

“아, 감사합니…….”

“인정하긴 싫지만 진심입니다.”

“……아, 예.”

“지금껏 사고 치신 걸 생각하면 피가 거꾸로 솟지만 정말 감탄했습니다. 진심입니다.”

“…….”

“누가 생각이나 했겠습니까. 허구한 날 가문 공금 훔쳐서 주루에 갖다 바치고, 술에 떡이 돼서 거리를 활보하며 가문 명성에 똥칠을 하던 삼공자께서 이리 큰사람이 되실 줄이야. 이 위팽, 진심으로 탄복했습니다.”

차라리 욕을 해, 이 새끼야…….

나는 튀어나오려는 쌍욕을 간신히 참으며 말했다.

“운이 좋았죠. 조필이 방심한 것도 있고요.”

위팽이 고개를 저었다.

“아닙니다. 전부 실력입니다. 누가 방심했고 비수를 숨겨 뒀느냐는 핑계가 되지 못합니다. 고작 그 정도로 조필을 죽일 수 있었다면 그는 일문일살 조필이 아니었을 겁니다. 무림은 강한 자만이 살아남는 곳이니까요.”

“강한 자만이 살아남는다.”

그 말을 조용히 혀끝에서 굴렸다. 어딘지 모르게 쓰고 달콤하다.

무림은, 이 게임은 처음부터 그런 곳이었다. 나는 그런 곳에서 살아남았고, 강해진 것이다.

“조필은 전심무공을 모두 발휘했습니다. 마지막에는 선천지기까지 끌어올렸고요. 절정 고수가 스스로의 목숨을 버려 가며 공자를 죽이려 한 겁니다. 하지만 결과는 어떻습니까?”

“제가 이겼죠.”

“예. 바로 그겁니다.”

“그럼 저는 조필보다 강했던 거군요.”

아까부터 떨떠름하던 위팽이 정색을 하고 말했다.

“무슨 소립니까. 조필이 더 강하죠. 절정 고수가 장난처럼 보이세요?”

“…….”

“기습으로 조필을 죽일 정도로만 강하신 겁니다.”

적당히 해라, 진짜.

인벤토리에서 무기를 꺼낼까 말까 고민하고 있을 때 위팽이 피식 웃었다. 처음 보는 그의 웃음이다.

“잘하셨습니다.”

나는 의심 어린 눈길로 위팽을 바라봤다.

“이번엔 또 무슨 말을 덧붙이시려고?”

웃음이 더욱 짙어졌다.

“진심입니다. 제가 공자를 상당히 싫어했던 건 사실이지만…… 이번만큼은 인정하지 않을 도리가 없군요.”

이렇게 나오면 할 말이 없다. 나는 왠지 모르게 민망해져서 헛기침을 내뱉었다.

“크흠. 뭐 죽을 뻔하긴 했지만 겨우 조필이랑 낭인 몇 명 잡은 게 전부인데요. 크흠.”

“한 성(城)에 절정 고수가 몇이나 있다고 생각하십니까? 본가가 위치한 산서를 통틀어도 채 스물이 되지 않습니다.”

스물이라. 예상보다 훨씬 적은 숫자다.

“항산검문 쪽 피해가 상당하겠네요. 그런 절정 고수를 셋이나 잃었으니.”

“하지만 가장 큰 타격은 따로 있지요.”

“그게 뭔데요?”

“그건…….”

위팽이 입을 연 그 순간이었다.

“명분. 이 전쟁을 시작하게 된 명분이 사라진 거지. 태원진가의 삼공자는 독 따위를 쓰지 않아도 충분히 강하니까. 암, 그렇고말고.”

문가에서 들려온 떨리는 목소리. 거구의 진위경이 울먹거리며 두 팔을 벌렸다.

“막내야아아!”

“…….”

제발 나 좀 내버려 둬.



* * *



결국 나는 지난 며칠간의 추격전과 조필과의 일전을 다시 한번 반복 재생해야 했다.

“그때 생존자들을 추적해 온 낭인들이…….”

“이런 찢어 죽일 놈들!”

쾅!

“조필의 화염신장에 내상을…….”

“죽일 놈! 악랄한 낭인 새끼가 감히! 오장육부를 뜯어내고 잘근잘근 씹어 먹어도 시원찮을 놈!”

쾅쾅쾅!

“…….”

나는 멍한 얼굴로 초토화가 된 침실을 바라봤다. 진위경의 과한 몰입감이 불러온 결과였다.

위팽은 진작 멀찍이 떨어져서 입을 벙긋거리고 있었다.

- 그 얘기는 다시 안 하는 게 좋겠습니다.

처음으로 우리 둘의 의견이 일치된 순간이었다.

진위경은 한참을 씨근덕거리다가 안정을 되찾았…….

“놈이 살아 있었다면 곱게 죽진 못했을 것이다.”

콰드득. 나는 침대 모서리가 가루가 되어 흩날리는 광경을 슬픈 눈으로 지켜봤다. 위팽이 고개를 절레절레 흔들었다.

“주군. 그만 진정하시지요. 공자께서 불안해하시는 것 같은데요.”

이번 말은 확실히 효과가 있었다. 온몸에 붕대를 두른 채 슬픈 눈으로 앉아 있는 나를 본 진위경이 눈시울을 붉혔다.

“우리 막내 좀 보게. 이 어린 녀석이 얼마나 고초를 겪었으면 이리 넋이 나가 있단 말인가.”

덥석!

솥뚜껑만 한 손이 어깨를 잡고 끌어당긴다. 나도 한 덩치 하는데 이 인간은 거의 소형 오우거급이다. 나는 그의 넓은 가슴에 안겨 두려움에 몸을 떨었다.

“그래, 막내야. 이제 괜찮다. 괜찮아.”

혼자만 감동적인 포옹을 끝낸 진위경이 코를 훌쩍였다.

“언제까지 어린아이일 줄만 알았는데…… 이제 다 컸구나. 위팽, 그거 아는가?”

위팽이 숨도 쉬지 않고 대답했다.

“예. 말씀 안 해 주셔도 됩니다.”

물론 진위경은 들은 척도 하지 않았다.

“본가는 물론이고 저잣거리에까지 소문이 퍼지고 있네. 결사대를 이끌고 적진을 기습. 일문일살 조필과 일백의 낭인들을 쓰러트리고 삭주 지부의 식솔들을 구출해 낸 영웅의 이야기 말일세.”

“와. 그거 대단…… 예?”

나는 눈을 깜빡였다. 잠깐만. 저게 내 이야기였어?

“저기, 뭔가 오해가 있는 것 같은데요.”

“맞습니다. 주군. 뭔가 오해가…….”

진위경은 흐뭇하게 웃었다.

“우리 막내, 겸손하기도 하지. 위팽 자네는 입 닥치게.”

“아뇨, 겸손이 아니라 소문이 좀 왜곡된 것 같은데.”

“맞습니다. 주군이 공자를 아끼시는 건 알지만 이건 너무 나가셨습니다. 소문이 너무 허황되면 사람들이 믿지 않을…….”

“소문? 허황?”

콰광!

위팽의 목소리는 굉음에 파묻혀 사라졌다. 나는 뻥 뚫린 침실 벽면을 바라보며 입을 딱 벌렸다.

‘뭔 짓거리야. 미친놈아.’

진위경이 다시 한번 주먹을 뻗었다. 압축된 공기가 터져 나가는 소리와 함께 그나마 남아 있던 벽이 무너져 내렸다.

이 층짜리 전각에서 나무와 벽돌이 쏟아져 내리니 밖에 있던 사람들이 아우성을 쳤다.

“삼공자다! 삼공차 처소가 무너지고 있다!”

“사람들 불러와. 빨리!”

모두가 충격에서 벗어나지 못하고 있을 때, 진위경이 내 몸을 번쩍 들어 올렸다.

‘놔. 놔, 이 미친놈아!’

온 힘을 다해 몸부림쳤지만 진위경을 당해 낼 수는 없었다. 한 발. 한 발. 뻥 뚫린 벽을 향해 걸어갈 때마다 공포가 밀려왔다.

‘떨어트릴 속셈이구나!’

밑에는 50명도 넘는 사람이 운집해 있었다. 말이 좋아 이 층이지, 전각이 워낙 커서 10m는 되는 높이다. 불어오는 바람이 아찔했다.

‘떨어지면 최소 골절이다.’

등골이 서늘한 순간에도 사람들은 꾸역꾸역 모여들고 있었다. 50명이 넘어가는 인원이 고개를 꺾어 우리를 바라봤다.

“누구야? 사고 난 거 아니었어?”

“소가주님인데? 품에 안긴 건 누구지?”

“삼공자. 삼공자다!”

누군가의 외침에 술렁임이 번졌다.

“삼공자, 아니 삼공자님이라고?”

“일문일살 조필을 쓰러트린 삼공자께서 깨어나셨다!”

이게 뭔 상황이야. 눈과 귀가 홱홱 돌아갈 때 진중한 목소리가 또렷이 들렸다.

“보이느냐?”

“아, 예. 보이긴 하는데요. 좀 내려 주실…….”

“들리느냐?”

“들리기도 하는데요. 일단 좀.”

“무엇이 느껴지느냐?”

“부끄러움이요. 그리고 수치심.”

“저들은 널 믿고 있다. 네 이름을 부르고 있다!”

“아니, 이 시발 놈아.”

마지막 욕은 사람들의 외침에 파묻혀 사라졌다.

“삼공자! 삼공자!”

그 잠깐 사이에 수십 명이 더 늘었다. 무수히 많은 시선이 우수수 날아와 꽂힌다.

‘아니, 이게 무슨.’

그때 진위경이 비장한 얼굴로 내 겨드랑이로 손을 집어넣었다. 그리고 번쩍 들어 올렸다.

때맞춰 우레 같은 함성이 터져 나왔다.

“와아아아아!”

“삼공자! 진태경!”

“산서잠룡! 산서잠룡!”

그리고…….

‘시발. 이건 뭐 아기 사자도 아니고.’

내 귀에는 오래된 애니메이션의 BGM이 울려 퍼졌다.
```

### Current accepted English

```markdown
# Chapter 32

“There was a major battle two days ago. One hundred elite fighters from our family clashed with two hundred vanguard troops from the Mount Heng Sword Sect in Honju.”

“There was a battle?”

And a major one, no less—hundreds of people thrown in. My heart lurched for a moment, but then I remembered what Wipeng had said earlier.

Good news and even better news. I’d already heard the outcome.

“We won.”

“It was a great victory. Fewer than thirty of them escaped alive. That’s about the same as our family’s casualties.”

Judging by the scar running from Wipeng’s forehead to his chin, it must have been a fierce fight.

*Well, of course. They outnumbered us two to one.*

Still, it was a relief we’d won. From the Jin Family of Taiyuan’s perspective, we’d poured in nearly half our strength. If we’d lost, the damage would have been enormous.

“It’s unfortunate we let the Mount Heng Sword Sect’s Lesser Family Head escape, but taking the Mount Heng Twin Devils was a major haul.”

“The Mount Heng Twin D-Devils?”

“The Mount Heng Twin Devils. Peak masters under the Mount Heng Sword Sect, and their loyalty was something else… They kept throwing themselves at us without any regard for their lives, so we had no choice but to kill them.”

Wipeng tapped the fresh scar.

“If we’d captured them, we could have extracted some important information.”

“Did you—I mean, did Great Hero Wipeng kill them?”

“My lord and I took one each. They were pretty good.”

“…”

I was left speechless as Wipeng slurped his tea.

*For fuck’s sake… Are Peak masters a joke to him?*

It had been the fiercest fight of my twenty-seven years. All kinds of internal injuries, and I’d been sliced up like a steak. I’d been out for five days after that, so I’d practically taken a half-bath in the River Jordan.[^1]

And after taking down Peak masters of that caliber. What, *pretty good*?

*He’s a complete monster.*

I learned something for certain this time: even Peak masters came in different levels. It was a huge relief that people of that caliber were on my side.

“That aside…”

*Clink.*

Wipeng set down his teacup and looked at me with a peculiar expression.

“You were remarkable.”

“Pardon?”

“I’m talking about Jopil, One Question, One Kill. Defeating him isn’t something the word remarkable can even cover.”

“…”

*You people seem more remarkable to me.*

It felt like getting praised by an A-rank Hunter for being good at killing goblins.

“Ah. Yes. Thank you, I suppose.”

I wanted to wrap up the Jopil talk there. My body and my mood were both in bad shape, and I wanted to check the System Rewards still waiting for me.

*Let’s rest now. I’m still a patient, damn it.*

I put that meaning into a wink. Wipeng frowned.

“Does your eye hurt? Shall I call a physician?”

“…No. I’m fine.”

“Your eye just spasmed.”

“That wasn’t a spasm.”

“It was a spasm. I saw it clearly.”

“No, just now, that was…”

Then Wipeng rolled his eyes back until only the whites showed and started to tremble.

The table shook, and tea spilled over the rim of the cup. I cried out in alarm.

“My God, Great Hero Wipeng!”

*This guy’s epileptic. No—how does a Peak master even get epilepsy?*

Just as I hurriedly tried to stand, the trembling stopped. Back to normal, Wipeng spoke with a perfectly calm face.

“You did this.”

“Are you all ri—wait, what?”

“That’s what you did just now, Third Young Master. Your eye spasmed.”

“So you were imitating me?”

“Yes.”

*What kind of lunatic is this…*

I tried to explain the difference between a wink and an epileptic fit, but the words stuck. Wipeng was glaring at me like a pissed-off dictator.

“…Shall we just finish talking about Jopil?”

“By all means.”

Wipeng nodded, satisfied.

*You crazy bastard.*

In the end, I had to tell him everything about the fight with Jopil, from beginning to end.

How Jopil had moved, what martial arts he’d used. Wipeng’s sharp questions had me tensing up more than once.

“You severed the tendons in Jopil’s legs with daggers?”

“Yes. I had them hidden in advance.”

“There’s no way Jopil failed to notice them… Continue.”

When the long story finally ended, Wipeng let out the breath he’d been holding. The mixed feelings in the way he looked at me came through loud and clear.

“Third Young Master. You have accomplished a truly great deed.”

“Ah, thank you…”

“I hate to admit it, but I mean it.”

“…Ah. Yes.”

“When I think of all the trouble you’ve caused until now, my blood boils, but I was genuinely impressed. I mean that.”

“…”

“Who could have imagined that the Third Young Master who stole family funds day after day and poured them into pleasure houses, then paraded through the streets dead drunk and smeared shit all over the family’s reputation, would become such a great man? I, Wipeng, am genuinely in awe.”

*Just curse me out, you bastard…*

I barely held back the stream of swearing trying to burst out and said,

“I got lucky. Jopil let his guard down too.”

Wipeng shook his head.

“No. It was all skill. Who let their guard down and who hid a dagger beforehand are not excuses. If that had been enough to kill Jopil, he would not have been Jopil, One Question, One Kill. Murim is a place where only the strong survive.”

“Only the strong survive.”

I quietly rolled the words over my tongue. They tasted bitter and sweet at the same time.

Murim—this game—had been that kind of place from the beginning. I had survived there, and I had gotten stronger.

“Jopil used every martial art he possessed to its fullest. In the end, he even pulled up his innate qi. A Peak master threw away his own life trying to kill you. But what was the result?”

“I won.”

“Yes. Exactly.”

“Then I was stronger than Jopil.”

Wipeng, who’d been looking sour this whole time, turned serious.

“What are you talking about? Jopil was stronger. Do Peak masters look like a joke to you?”

“…”

“You were only strong enough to kill Jopil in a surprise attack.”

*Enough already. Seriously.*

While I was debating whether to pull a weapon from my Inventory, Wipeng let out a short chuckle. It was the first time I had ever seen him laugh.

“Well done.”

I looked at Wipeng suspiciously.

“What are you going to tack on this time?”

His smile deepened.

“I mean it. It’s true I disliked you quite a lot, but… this time, I have no choice but to acknowledge you.”

When he put it like that, I had nothing to say. I got embarrassed for some reason and cleared my throat.

“Ahem. Well, I almost died, but all I did was take down Jopil and a few wandering martial artists. Ahem.”

“How many Peak masters do you think there are in a single city? Across all of Shanxi, where our family is located, there are fewer than twenty.”

Twenty. Far fewer than I’d expected.

“The Mount Heng Sword Sect must have taken serious losses. They lost three Peak masters like that.”

“But the greatest blow is something else.”

“What is it?”

“That is…”

The instant Wipeng opened his mouth, a trembling voice came from the doorway.

“The pretext. The pretext for starting this war is gone. The Third Young Master of the Jin Family of Taiyuan is strong enough without using poison. Indeed, that’s exactly right.”

The enormous Jin Wikyung stood there, teary-eyed, both arms spread wide.

“My baby brother!”

“…”

*Please, just leave me alone.*

* * *

In the end, I had to replay the chase of the past several days and my fight with Jopil all over again.

“The wandering martial artists who chased the survivors…”

“Those bastards! I’ll tear them apart!”

*Boom!*

“Jopil’s Flame Divine Palm caused internal injuries…”

“I’ll kill him! How dare that vicious wandering martial artist bastard! Even if I ripped out his guts and chewed them to a pulp, it wouldn’t be enough!”

*Boom! Boom! Boom!*

“…”

I stared blankly at the wreckage of my bedroom. Jin Wikyung had gotten way too into the story.

Wipeng had already backed far away and was mouthing something.

—It would be best not to bring that story up again.

For the first time, the two of us were in complete agreement.

Jin Wikyung huffed and puffed for a long while before he finally calmed dow—

“If that bastard had still been alive, he wouldn’t have died peacefully.”

*Crunch.*

I watched with sad eyes as the corner of the bed crumbled into powder. Wipeng shook his head.

“My lord. Please calm down. The Young Master seems anxious.”

That one actually worked. Seeing me sitting there sadly, wrapped in bandages from head to toe, Jin Wikyung’s eyes reddened.

“Just look at my baby brother. How much has this child suffered, to be sitting there so out of it?”

*Grab!*

A hand the size of a cauldron lid seized my shoulder and yanked me in. I was a fairly big guy myself, but this man was practically a small ogre. Crushed against his broad chest, I trembled in fear.

“There, little brother. It’s all right now. It’s all right.”

After a heartfelt hug that only he found moving, Jin Wikyung sniffed.

“I thought you’d be a child forever… but you’ve grown up now. Wipeng, did you know?”

Wipeng answered without even taking a breath.

“Yes. You don’t need to tell me.”

Of course, Jin Wikyung pretended not to hear him.

“Rumors have spread throughout our family and even through the streets. The tale of the hero who led a death squad in a raid on the enemy camp, defeated Jopil, One Question, One Kill, and one hundred wandering martial artists, and rescued the Sakju Branch’s household.”

“Wow. That’s amaz—wait, what?”

I blinked.

*Hold on. That was my story?*

“Um, I think there’s been some misunderstanding.”

“That’s right, my lord. There seems to have been some misunder—”

Jin Wikyung smiled, pleased.

“Our little brother is modest, too. Wipeng, you shut your mouth.”

“No, it isn’t modesty. I think the rumor has been distorted a little.”

“That’s right. I know you care for the Young Master, my lord, but this is going too far. If the rumor gets too far-fetched, people won’t beli—”

“Rumor? Far-fetched?”

*BOOM!*

Wipeng’s voice vanished under the thunderous crash. I stared with my mouth hanging open at the hole blown through my bedroom wall.

*What the hell are you doing, you lunatic?*

Jin Wikyung threw another punch. With a sound like compressed air bursting, what was left of the wall came down.

Wood and bricks rained from the two-story pavilion, and the people outside started shouting.

“It’s the Third Young Master! The Third Young Mas—his residence is collapsing!”

“Get people over here! Hurry!”

While everyone was still stuck in shock, Jin Wikyung hoisted me into the air.

*Put me down. Put me down, you crazy bastard!*

I struggled with all my strength, but there was no fighting him off. One step. One step. Every step toward the gaping wall sent terror through me.

*He’s going to drop me!*

More than fifty people had gathered below. It was two stories in name, but the pavilion was so huge the drop was a good ten meters. The wind coming through made me dizzy.

*If I fall, that’s a fracture at the very least.*

Even with a chill running down my spine, people kept packing in. More than fifty of them had their heads cranked back, looking up at us.

“Who is that? Wasn’t there an accident?”

“That’s the Lesser Family Head, isn’t it? Who’s he holding?”

“The Third Young Master. It’s the Third Young Master!”

Someone’s shout sent a stir through the crowd.

“The Third Young Master—no, the Third Young Master, sir?”

“The Third Young Master who defeated Jopil, One Question, One Kill, has awakened!”

*What is this situation?*

While my eyes and ears were still whipping around, a solemn voice rang out clearly.

“Can you see?”

“Ah, yes, I can see. Could you put me down—”

“Can you hear?”

“I can hear too, but first, could you—”

“What do you feel?”

“Embarrassment. And shame.”

“They believe in you. They’re calling your name!”

“No, you fucking bastard.”

That last curse vanished, swallowed by the crowd’s shouts.

“Third Young Master! Third Young Master!”

Dozens more had shown up in that brief interval. Countless eyes came flying at me and stuck.

*No, what is this?*

Then, with a solemn face, Jin Wikyung shoved his hands into my armpits and lifted me high.

Right on cue, a thunderous cheer erupted.

“Woooooo!”

“Third Young Master! Jin Taekyung!”

“Sleeping Dragon of Shanxi! Sleeping Dragon of Shanxi!”

And then…

*Fuck. What is this, a baby lion?*

An old cartoon’s BGM rang in my ears.

[^1]: In Korean, “crossing the River Jordan” is a euphemism for dying; Taekyung twists it into taking a half-bath.
```
## Chapter 33

### Korean source

```text
＃33화



“죽여 주십시오.”

풀어헤친 머리카락, 피와 먼지를 뒤집어쓴 청년이 무릎을 꿇었다. 청년의 이름은 이소광. 죽은 이소군의 형이자 항산검문의 소문주였다.

“보고해라. 네 입으로 직접.”

서늘한 음성에 막사 내의 사람들이 얼어붙었다. 한 사람, 한 사람이 항산검문의 중진이며 오랜 세월 강호를 종횡한 고수들이다.

하지만 그들조차도 한 사람 앞에서는 고개를 숙여야 했다.

“아버님…….”

“내가 원하는 대답이 아니다.”

혈랑검 이천백은 돌아보지도 않았다. 이소광은 떨리는 목소리를 끄집어냈다.

“생존자는 저를 포함한 스물셋이 전부입니다. 나머지는 생사를 알 수 없습니다.”

좌중에 무거운 침묵이 내려앉았다.

이백여 명에 달하는 병력이 죽거나 사로잡혔고 세 명의 절정 고수도 잃었다. 이것만으로도 문책을 피하기 어려운데 더 큰 문제는 따로 있었다.

“네가 받은 명령이 무엇이냐?”

“……태원진가의 지부 섬멸과 정양까지의 진격입니다.”

“그다음은.”

“길을 봉쇄하고 본대의 합류를 기다리는 것입니다.”

“혼주까지 나아간 이유가 무어냐?”

“정보를, 정보를 입수했습니다.”

“정보?”

“예. 일문일살 조필이 진태경을 혼주까지 추격하여 사로잡았다고 했습니다. 한데…….”

“태원진가의 추격대에 쫓기고 있으니 도와 달라고 했겠지.”

이소광은 고개를 떨궜고, 이천백은 헛웃음을 흘렸다.

“그 정보를 누가 전했느냐?”

“조필 휘하의 낭인이었습니다.”

“지금도 그렇게 생각하느냐?”

“……아닙니다.”

철썩!

이소광의 얼굴이 홱 돌아갔다. 그 위로 불길 같은 이천백의 눈빛이 쏟아졌다.

“내 아들로 태어난 것에 감사해라.”

결국 항산검문으로 복귀하라는 처분을 받은 이소광이 물러나는 것으로 사태는 일단락되었다. 이제는 냉철하게 현실을 바라볼 때였다.

“현재 상황은?”

“이백의 병력을 잃었지만 그중 절반 이상이 급하게 끌어모은 낭인들이라 생각만큼 큰 피해는 아닙니다. 문제는…….”

“절정 고수를 셋이나 잃었다는 거지.”

이천백은 속이 쓰렸다. 이십 년 세월을 함께한 항산쌍귀. 그리고 거금을 들여 고용한 조필도 죽었다. 절정 고수는 전투의 흐름을 바꿀 수 있는 존재다. 빈자리를 어떻게든 메워야 한다.

“더 끌어모으게. 흑시(黑市)에서 낭인들을 사 오건, 마적 놈들을 고용하건 무슨 수를 써서라도.”

“지출이 너무 큽니다. 지금쯤 혼주에서의 일이 다 알려졌으니 몸값을 올리려 들 테고요.”

“믿을 만한 놈들도 아닙니다. 특히 마적들은 인간 백정 같은 자들 아닙니까. 그런 놈들을 고용했다가는 차후에도 본문의 평판이…….”

하지만 이천백은 눈 하나 깜빡하지 않았다.

“잘됐군. 전부 고용해.”

“문주!”

“이곳에 모인 머릿수만 물경 오백입니다. 두 배가 넘는 병력에 절정 고수의 숫자도 밀리지 않습니다.”

“내 아들놈도 그렇게 생각했지. 결국 혼주에서 개박살이 났고.”

“그건…….”

“인간 백정이건 뭐건 신경 쓰지 말고 총력을 기울여. 이 전쟁에서 지면 평판이 아니라 목숨을 잃게 될 테니까!”

이천백의 불호령에 중진들은 설득이 무의미하다는 사실을 깨달았다. 하지만 그렇다고 해서 모든 이야기가 끝난 것은 아니었다.

“무사들의 사기가 말이 아닙니다.”

“혼주에서의 패배도 패배지만, 진태경이 일문일살 조필을 죽였다는 소식에 동요하고 있습니다.”

진태경. 원수의 이름을 들은 이천백은 속이 뒤틀렸다.

‘그런 멍청한 소문을 믿는 놈들이 있단 말인가?’

진태경, 그 한심한 놈이 아들을 독살한 것으로도 모자라 이제는 절정 고수를 잡았다니. 속내가 뻔히 보이는 계략이다. 이천백은 태원진가의 비열함에 치가 떨렸다.

“그따위 헛소문을 퍼트리는 놈들을 색출해 내라. 한 놈도 빠짐없이!”

몇 놈을 본보기 삼아 목을 벤다면 사기는 떨어지겠지만 붕괴는 막을 수 있다. 지금은 억누르고 나아갈 때다.

“사흘이다. 사흘 후, 태원으로 진격한다!”

무림의 은원(恩怨)이란 그런 것이다. 둘 중 하나가 쓰러지기 전까지 은원의 고리는 끊어지지 않는다.

‘모두 빼앗아 주마. 너희가 그랬던 것처럼.’



* * *



“대단한 회복력이군요.”

의원이 혀를 내둘렀다. 정신을 차린 지 이틀째. 지난 밤 사이 딱지가 떨어지고 뽀얀 새살이 돋아나 있었다.

“의원 생활 십 년 만에 이런 건 처음 봅니다.”

내가 보기에도 경이로운 회복 속도다. 화염신장의 열기로 녹아내린 살갗, 골절된 뼈와 깊은 검상은 이제 찾아볼 수 없었다. 아, 거기에 더해 내상도.

‘아마 레벨 업의 효과겠지.’

현실에서도 비슷한 효력을 내는 방법이 딱 하나 있다.

소위 힐러(Healer)라 부르는 극소수의 헌터들이 사용하는 치유 마법이 바로 그것이다.

‘완전 치유까지는 무리인가?’

다소 아쉬웠지만 차라리 잘됐다. 레벨 업 한 번에 모든 상처가 회복됐다면 의심을 피하기가 어려웠을 것이다.

지금도 의원은 괴물 보듯이 나를 흘끗거리고 있었다.

“허어어. 괴이한 일이로다. 백년설삼의 효능이라 보기에는 너무 과한데…….”

“백년설삼?”

무협 소설에서 본 기억이 있다. 백 년 묵은 산삼. 뭐 그런 거 아닌가?

‘그게 갑자기 왜 나와?’

어리둥절한 내게 의원이 설명했다. 그는 내가 기억을 잃었다고 알고 있는 몇 안 되는 NPC중 하나였다.

“작년 이맘때쯤에 약왕당 창고가 털린 적이 있었습니다.”

아하. 듣자마자 감이 온다.

그때 도난당한 약재 중 백년설삼이 포함되어 있었을 것이고 범인은 보나 마나…….

“약왕당주께서 노발대발하셨죠.”

의원이 어색한 웃음을 지어 보였다.

“아무래도 백년설삼이 돈만 있다고 구할 수 있는 물건은 아니니까요. 한 번에 이십 년 공력을 얻을 수 있는 영약을 훔쳐 드셨으니.”

“이십 년 공력이요?”

문득 생각나는 게 있었다. 내 통제를 따르지 않았던 제삼의 공력.

‘그거였구나.’

동시에 아쉬움이 밀려왔다. 마지막 순간, 스킬을 쓰면서 백년설삼의 이십 년 공력 중 대부분이 사라졌기 때문이다.

순전히 내 통제에 따른 것이 아닌 폭주였기 때문에 일어난 대참사였다.

‘그걸 일회용으로 쓰다니.’

구겨지는 내 표정을 오해한 의원이 황급히 말했다.

“물론 공자님께서 큰 뜻이 있으셔서 그런 결정을 내리신 거겠지요.”

큰 뜻은 염병. 몸보신이나 하려고 먹었겠지.

백년설삼의 공력 덕분에 살긴 했지만 역시 아깝다. 아까워 죽겠다.

“거의 회복되셨으니 거동에는 문제가 없으실 겁니다. 그럼 전 이만.”

의원이 허둥지둥 자리를 뜨자마자 시스템창을 열었다.

‘상태창 오픈.’

띠링.



상태창



[Lv.30 진태경]

직업 : 이류 무인

명성 : 410

칭호 : 4개 (칭호 효과 적용 중)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 가문의 수치 (모든 능력치 –5, 명성 –50)

- 초보 수련자 (수련 속도 +10%)

- 승부사 (일대일 승부 시 전투 관련 능력치 10% 향상)

근력 : 115  체력 : 120

민첩 : 116 지력 : 15

매력 : 15공력 : 15년

잔여 포인트 : 0





보는 순간 뿌듯함이 밀려온다.

‘많이 컸다.’

산적 나부랭이한테 벌벌 떨던 때가 엊그제 같은데 이제는 나름대로 고수다. 조필을 잡으면서 레벨이 껑충 뛰었고 막대한 명성치도 얻었다.

그뿐만이 아니다. 남아 있는 백년설삼의 기운을 일부 흡수한 덕에 추가로 얻은 4년의 공력, 거기에 더해서…….



스킬창



[일섬]

등급 : 절정

경지 : 이 성

제한 : 진태경

효과 : 체력과 공력을 소모하여 강력한 일격을 날린다. 정도에 따라 일정 시간 무기력 상태에 빠진다.





새로운 무공, 아니 스킬도 생겼다. 하지만 현실에서의 스킬과는 큰 차이점이 있었다.

‘소모되는 양과 힘을 조절할 수 있다.’

힘껏 찌르기. 지금은 일섬이라는 이름이 붙은 이 스킬은 남발이 불가능했다. 순간적으로 몇 단계 위의 파괴력을 낼 수 있지만 그 한 방으로 모든 힘을 소진하기 때문이다.

‘아니, 원래 조절이 가능한 스킬이었을지도.’

현실에서의 나는 F급 헌터다. 신체 능력도, 몸에 지닌 마나도 보잘것없다. 하지만 이 게임, 무림에서만큼은 다르다.

15년의 공력과 2, 30레벨 차이의 NPC들보다 뛰어난 신체 능력을 지닌 무림인인 것이다. 힘을 담아내는 그릇이 달라지니 본래 있었던 활용도가 드러난 셈이다.

‘또 강해졌다.’

혁무진한테 탈탈 털리고 무공을 익히던 게 엊그제 같은데, 이제는 절정 고수를 잡았다.

창밖에서는 하루에도 몇 번씩 내 이름을 연호한다.

무슨 산서잠룡이니, 가문의 영웅이니 하면서.

‘영웅이라.’

살면서 저런 말을 들어 볼 줄이야. F급 헌터 나부랭이인데다 안전 제일이 삶의 모토인 나와는 인연이 없던 단어다.

나는 가만히 누운 채로 손을 꼼지락거렸다. 희고 부드럽던 도련님의 손바닥에는 어느새 굳은살이 빼곡하게 박여 있었다.

‘이 손으로 조필을 쓰러트렸단 말이지.’

내가 쓰러트린 자들을 모두 합하면 수십이 넘어간다. 산적부터 낭인, 일류라고 평가받는 이들도 있었지만 나는 살아남았다. 도저히 이길 수 없을 것 같았던 절정 고수, 일문일살 조필조차 쓰러트렸다.

문득 위팽이 했던 말이 떠올랐다.

‘살아남는 자가 강한 거라고 했지.’

그의 말대로라면 나는 분명히 강자다. 지금껏 상대한 적들로부터 살아남았고 영웅으로 불리고 있으니까.

그래. 솔직히 말해 보자면…….

‘나쁘지 않은 기분이야.’

현실의 나는 초라하다.

3평 남짓한 고시원 원룸에서 먹고 자며 가족들을 부양해야 하는 가장이다. 영웅이 될 수도 없고, 되고 싶지도 않다.

그저 매일 살아남기를 기도하며 싸우는 최하급 헌터 진태경.

그게 나였다.

‘하지만 이 게임에서는 달라.’

F급 헌터 진태경은 하지 못하는 많은 것들을 해냈다. 최소한…… 나를 믿고 따르는 이들을 적들의 손에서 지킬 수 있다. 사람들에게 인정받고, 영웅으로 불린다.

이곳의 모든 게 가상에 불과하고 눈에 보이는 사람들이 NPC라고 해도 그 사실은 변하지 않는다.

그런 생각을 하는데, 문득 웃음이 나왔다.

‘이래서 게임이 무섭다니까.’

게임 중독 현상인가?

어느새 무림인 진태경으로 사는 것에 재미를 느끼고 있는 나를 발견했다. 이곳은 게임이니까. 모든 불가능을 가능으로 바꿔 버릴 수 있으니까.

하지만 이제는 나가야 할 때다. 불가능이 가득한 그곳, 현실로. 그곳에 가족이 있고 진정한 내가 있다.

‘퀘스트창 확인.’

띠링.



퀘스트



[로그아웃]

이제 당신은 이 험난한 무림을 헤쳐 나가야 합니다.

더욱더 강해지고, 유명해지십시오.

언젠가 다가올 그 날을 위해…….



등급 : 메인 퀘스트

제한 : 진태경

임무 : [일류] 경지 달성 (미완료)

         Lv.30 달성 (완료)

         명성 500 달성 (410/500)

보상 : [로그아웃]





로그아웃. 반짝거리는 네 글자를 보는 순간 숨이 막힌다.

이제 로그아웃까지 남은 조건은 두 개. 명성은 시간이 해결해 줄 수 있다. 나에 관한 소문이 퍼져 나갈수록 계속해서 오를 테니까. 문제는 따로 있다.

“일류.”

일류가 되기 위해서는 대체 뭐가 필요한 거지?

레벨도, 능력치도, 명성도 아니라면…….

‘공력? 아니면 무공의 경지를 더 올려야 하나?’

그때 문밖에서 정중한 목소리가 들려왔다.

“공자님. 소가주님께서 찾으십니다.”

“아.”

맞다. 모를 땐 물어보는 게 최고다. 그런 의미에서 절정 고수인 진위경은 최고의 과외 선생이다.
```

### Current accepted English

```markdown
# Chapter 33

“Please kill me.”

A young man with disheveled hair, covered in blood and dust, dropped to his knees. His name was Lee Seogwang—the elder brother of the late Lee Seogeun and the Young Sect Leader of the Mount Heng Sword Sect.

“Report. From your own mouth.”

The cold voice froze everyone inside the tent. Every last one of them was a senior of the Mount Heng Sword Sect, a master who had spent long years roaming the martial world.

Yet even they had to bow their heads before one man.

“Father…”

“That isn’t the answer I want.”

The Blood Wolf Sword, Lee Cheonbaek, did not even turn around. Lee Seogwang forced the words out in a trembling voice.

“The only survivors are twenty-three of us, including me. We have no idea whether the rest are alive or dead.”

A heavy silence settled over those present.

Some two hundred troops had been killed or captured, and they had lost three Peak masters. That alone would have made it hard to avoid punishment, but there was a bigger problem still.

“What orders were you given?”

“…To wipe out the Jin Family of Taiyuan’s branches and advance as far as Jeongyang.”

“And after that?”

“To blockade the road and wait for the main force to join us.”

“Why did you push as far as Honju?”

“Intelligence—I obtained intelligence.”

“Intelligence?”

“Yes. They said Jopil, One Question, One Kill, had chased Jin Taekyung all the way to Honju and captured him. But…”

“He must have said the Jin Family of Taiyuan’s pursuit party was on his heels and asked you to help him.”

Lee Seogwang lowered his head, and Lee Cheonbaek let out a hollow laugh.

“Who delivered that information?”

“A wandering martial artist under Jopil.”

“Do you still think that?”

“…No.”

Smack!

Lee Seogwang’s head snapped to the side. Lee Cheonbaek’s gaze poured down on him like fire.

“Be grateful you were born my son.”

In the end, Lee Seogwang was ordered back to the Mount Heng Sword Sect, and with his withdrawal, the matter was settled for now. It was time to look at reality with a cool head.

“What is the situation?”

“We lost two hundred men, but more than half of them were wandering martial artists we scraped together in a hurry. The damage isn’t as bad as it sounds. The problem is…”

“We lost three Peak masters.”

It left a bitter taste in Lee Cheonbaek’s mouth. The Mount Heng Twin Devils, who had stood with him for twenty years. And Jopil, whom he had paid a fortune to hire, was dead as well.

A Peak master was someone who could change the course of a battle. Somehow, they had to fill the void.

“Gather more. Buy wandering martial artists from the black market, hire mounted bandits—use whatever means necessary.”

“The expense is already too high. By now, word of what happened in Honju will have spread, so they’ll try to drive their prices up.”

“They aren’t trustworthy men, either. Especially the mounted bandits. Aren’t they human butchers? If we hire people like that, our sect’s reputation will suffer afterward…”

Lee Cheonbaek did not even blink.

“All the better. Hire them all.”

“Sect Leader!”

“There are no fewer than five hundred men gathered here. We have more than twice their numbers, and we aren’t behind in Peak masters either.”

“My son thought the same thing. Then he got utterly wrecked in Honju.”

“That was…”

“Don’t worry about whether they’re human butchers or anything else. Throw everything we have into this. If we lose this war, it won’t be our reputation we lose—it’ll be our lives!”

At Lee Cheonbaek’s thunderous command, the seniors realized persuasion was pointless. That did not mean the discussion was over.

“The martial artists’ morale is in shambles.”

“The defeat at Honju is one thing, but they’re shaken by the news that Jin Taekyung killed Jopil, One Question, One Kill.”

Jin Taekyung.

Hearing the name of his enemy made Lee Cheonbaek’s stomach churn.

*Are there really people stupid enough to believe a rumor that dumb?*

As if it weren’t enough that that pathetic fool Jin Taekyung had poisoned his son, now he had supposedly killed a Peak master too. The scheme was obvious. Lee Cheonbaek’s teeth clenched at the Jin Family of Taiyuan’s despicable tactics.

“Find everyone spreading that kind of nonsense. Don’t miss a single one!”

If he took a few heads as examples, morale might drop, but he could keep the army from collapsing. Now was the time to clamp down and push forward.

“Three days. In three days, we march on Taiyuan!”

That was how the debts and grudges of Murim worked. The chain of debts and grudges would not break until one of the two sides fell.

*I’ll take everything from you. Just as you did.*

* * *

“What an incredible recovery.”

The physician was astounded. It was my second day since I’d come to. Overnight, the scabs had fallen away, and pale new skin had grown in.

“In ten years as a physician, this is the first time I’ve seen anything like this.”

Even to me, the speed of it was astonishing. The flesh melted by the heat of Flame Divine Palm, the fractured bones, the deep sword wounds—there was no trace of them left.

Oh, and the internal injuries too.

*Must be the effect of leveling up.*

There was only one method in the real world that produced a similar result.

Healing magic used by the tiny handful of Hunters known as healers.

*Is complete healing too much to ask?*

I was a little disappointed, but it was just as well. If a single level-up had healed every wound on my body, it would have been hard to dodge suspicion.

Even now, the physician kept stealing glances at me like I was a monster.

“Heavens. How bizarre. It’s far too much to pin on the effects of hundred-year snow ginseng…”

“Hundred-year snow ginseng?”

I remembered seeing something like it in martial arts novels. Ginseng that had grown for a hundred years, or whatever.

*Why is that suddenly coming up?*

Seeing how lost I looked, the physician explained. He was one of the few NPCs who knew I had lost my memory.

“Around this time last year, the Medicine King Hall’s storeroom was robbed.”

Ah. The moment he said it, I understood.

The stolen medicinals must have included hundred-year snow ginseng, and the culprit was obviously…

“The Medicine King Hall Leader was absolutely furious.”

The physician gave me an awkward smile.

“It isn’t something you can get just because you have money, after all. You stole an elixir that can grant twenty years of internal energy in a single dose and consumed it.”

“Twenty years of internal energy?”

Something clicked. The third internal energy that had refused to obey me.

*So that was it.*

At the same time, I felt a pang of regret. At the last moment, when I used the Skill, most of the twenty years of internal energy from the hundred-year snow ginseng had vanished.

It had been a complete disaster, because the energy had run wild instead of following my control.

*I used it as a one-time item.*

The physician misread the look on my face and hurriedly added,

“Of course, Young Master, you must have made that decision for some grand purpose.”

*Grand purpose, my ass. I probably ate it as a tonic.*

The snow ginseng’s internal energy had kept me alive, but it was still a waste.

A waste so bad it was killing me.

“You’ve almost completely recovered, so you shouldn’t have any trouble moving around. Then I’ll be on my way.”

The moment the physician hurried out, I opened the System window.

*Open Status Window.*

Ding.

> **System**
>
> **Status Window**
>
> **Lv. 30 Jin Taekyung**
>
> **Class:** Second Rate Martial Artist
>
> **Fame:** 410
>
> **Titles:** 4 (Title effects active)
>
> — **Scion of a Prestigious Family** (All stats +5, Fame +50)
>
> — **Family Shame** (All stats −5, Fame −50)
>
> — **Novice Trainee** (Training speed +10%)
>
> — **Gambler** (Combat-related stats increased by 10% in a one-on-one fight)
>
> **Strength:** 115 **Stamina:** 120
>
> **Agility:** 116 **Intelligence:** 15
>
> **Charm:** 15 **Internal Energy:** 15 years
>
> **Remaining Points:** 0

The moment I saw it, pride welled up.

*I’ve grown a lot.*

It felt like only yesterday I’d been shaking in front of some two-bit bandits. Now I was a master in my own right. My Level had jumped after I took down Jopil, and I’d gained a massive amount of Fame.

That wasn’t all. I’d absorbed some of the hundred-year snow ginseng’s leftover energy and gained another four years of internal energy. On top of that…

> **System**
>
> **Skill Window**
>
> **One Flash**
>
> **Grade:** Peak
>
> **Realm:** Second Stage
>
> **Restriction:** Jin Taekyung
>
> **Effect:** Consumes Stamina and internal energy to deliver a powerful strike. Depending on the amount used, the user enters a helpless state for a certain period of time.

I had a new martial art—or rather, a new Skill.

But it was very different from my Skills in the real world.

*I can adjust how much it consumes, and how much power it puts out.*

Thrust with All My Might. This Skill, now named One Flash, couldn’t be spammed. It could put out destructive power several stages above my usual level for an instant, but that single blow burned through all my strength.

*No. Maybe it was always a Skill you could adjust.*

In the real world, I was an F-rank Hunter. My physical abilities and the mana in my body were pathetic. But this game—Murim—was different.

Here I was a martial artist with fifteen years of internal energy and a body better than NPCs with a twenty- or thirty-Level gap. Change the vessel that holds the power, and the Skill’s original range of use comes out.

*I’ve gotten stronger again.*

It felt like only yesterday Hyuk Mujin had been wiping the floor with me while I learned martial arts. Now I’d taken down a Peak master.

Outside the window, they chanted my name several times a day.

Sleeping Dragon of Shanxi, hero of the family, that sort of thing.

*A hero.*

I never thought I’d hear a word like that in my life. For a two-bit F-rank Hunter whose motto was safety first, it was a word that had never had anything to do with me.

I lay still and fidgeted with my hands. Palms that had once been a young master’s—white and soft—were now packed tight with calluses.

*With these hands, I took down Jopil.*

All told, the people I’d taken down numbered more than a few dozen. Bandits, wandering martial artists, even people rated as First Rate—and I had survived. I’d even taken down a Peak master I thought I could never beat: Jopil, One Question, One Kill.

I suddenly remembered something Wipeng had said.

*The one who survives is strong.*

If he was right, I was definitely strong. I’d survived every enemy I’d faced so far, and they were calling me a hero.

Yes. If I’m being honest…

*It doesn’t feel bad.*

The real-world me was pitiful.

I ate and slept in a one-room goshiwon barely ten square meters across,[^1] the breadwinner who had to support my family. I couldn’t become a hero, and I didn’t want to.

I was just Jin Taekyung, a bottom-rung Hunter who fought every day praying he’d survive.

That was me.

*But in this game, I’m different.*

I’d done a lot of things F-rank Hunter Jin Taekyung could never do. At the very least… I could protect the people who trusted and followed me from the enemy. People acknowledged me. They called me a hero.

Even if everything here was nothing but virtual, even if the people in front of me were NPCs, that fact didn’t change.

Thinking that, I suddenly laughed.

*This is why games are scary.*

Was this game addiction?

Without realizing it, I’d found that I was enjoying living as Jin Taekyung, a martial artist of Murim. Because this was a game. Because it could turn every impossibility into a possibility.

But now it was time to leave.

Back to that place packed with impossibilities—the real world. My family was there. The real me was there.

*Check Quest Window.*

Ding.

> **System**
>
> **Quest**
>
> **Logout**
>
> Now you must make your way through this harsh Murim.
>
> Become stronger and more famous.
>
> For the day that will eventually come…
>
> **Grade:** Main Quest
>
> **Restriction:** Jin Taekyung
>
> **Objective:** Achieve the **First Rate** realm (Incomplete)  
>        Achieve **Lv. 30** (Complete)  
>        Achieve **Fame 500** (410/500)
>
> **Reward:** **Logout**

Logout.

The moment I saw those four glittering characters, my breath caught.

Only two conditions left before I could log out. Time could take care of Fame. The more rumors about me spread, the more it would keep climbing.

The problem was something else.

“First Rate.”

What did I even need to become First Rate?

If it wasn’t Level, stats, or Fame, then…

*Internal energy? Or do I need to raise the realm of my martial arts further?*

Just then, a polite voice came from outside the door.

“Young Master. The Lesser Family Head is looking for you.”

“Ah.”

Right. When you don’t know something, the best thing to do is ask.

And for that, Peak master Jin Wikyung was the best private tutor I could get.

[^1]: A goshiwon is a tiny, inexpensive room-for-rent housing arrangement.
```
