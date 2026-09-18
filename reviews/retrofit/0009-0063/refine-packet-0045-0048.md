# Retrospective Patch Plan — Chapters 45–48

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
  "summary": "11 findings in chapters 45-48",
  "findings": [
    {
      "chapter": 45,
      "confidence": 0.99,
      "current": "Even without arms, it was more than dangerous enough bare-handed.",
      "defect": "Calling an armless creature “bare-handed” is contradictory. The source says its body alone remains dangerous.",
      "id": "R0045-01",
      "rationale": "맨몸으로 means relying on its bare body, not fighting with bare hands.",
      "replacement": "Even without arms, its body alone was still more than dangerous enough.",
      "severity": "major",
      "source": "양팔을 잃었지만 놈은 맨몸으로도 충분히 위협적인 존재니까."
    },
    {
      "chapter": 45,
      "confidence": 0.99,
      "current": "Every step it gave, a new wound opened and more blood spilled.",
      "defect": "“Every step it gave” is unidiomatic and obscures that the monster is retreating step by step.",
      "id": "R0045-02",
      "rationale": "물러날 때마다 explicitly means each time it stepped back.",
      "replacement": "With every step it retreated, a new wound opened and more blood spilled.",
      "severity": "minor",
      "source": "한 걸음씩 물러날 때마다, 새로운 상처가 생기고 더 많은 피가 쏟아졌다."
    },
    {
      "chapter": 45,
      "confidence": 0.99,
      "current": "An awl in a bag pokes through.",
      "defect": "The established rendering of the idiom is not used.",
      "id": "R0045-03",
      "rationale": "The block glossary establishes 낭중지추 as “needle in a bag,” describing exceptional talent that inevitably reveals itself.",
      "replacement": "A needle in a bag eventually pokes through.",
      "severity": "minor",
      "source": "낭중지추."
    },
    {
      "chapter": 45,
      "confidence": 0.99,
      "current": "Well, I’m not some prestigious family’s son here. And I’m sure as hell no Sleeping Dragon.",
      "defect": "The established rendering of 잠룡 is replaced with a different epithet.",
      "id": "R0045-04",
      "rationale": "The block glossary establishes 잠룡 as “Hidden Dragon.”",
      "replacement": "Well, I’m not some prestigious family’s son here. And I’m sure as hell no Hidden Dragon.",
      "severity": "minor",
      "source": "하긴, 나는 여기서 명문가 자제도 아니고, 잠룡 같은 건 더더욱 아니니까."
    },
    {
      "chapter": 46,
      "confidence": 1.0,
      "current": "Food in Murim was spicy, salty, and bland. And even then, more days than not, I couldn’t eat properly. For thirty days, my stomach had been abused with beef jerky, bigu pills,[^1] and rice balls.",
      "defect": "The established English term for 벽곡단 is replaced by a romanization requiring an unnecessary footnote.",
      "id": "R0046-01",
      "rationale": "The block glossary establishes 벽곡단 as “fasting pills.”",
      "replacement": "Food in Murim was spicy, salty, and bland. And even then, more days than not, I couldn’t eat properly. For thirty days, my stomach had been abused with beef jerky, fasting pills, and rice balls.",
      "severity": "minor",
      "source": "무림의 음식은 맵고 짜고 싱겁다. 그마저도 제대로 못 먹는 날이 더 많았다. 30일간 내 위장은 육포와 벽곡단, 주먹밥으로 혹사당했다."
    },
    {
      "chapter": 46,
      "confidence": 0.97,
      "current": "“—You bastard, you’re a ghost. I was just about to call you.”",
      "defect": "The literal “you’re a ghost” is unnatural in English and loses the caller’s remark about Choi’s uncannily perfect timing.",
      "id": "R0046-02",
      "rationale": "Here 귀신이네 is an idiomatic reaction to Choi calling at exactly the right moment, not a claim that he is literally a ghost.",
      "replacement": "“—You bastard, are you psychic or what? I was just about to call you.”",
      "severity": "minor",
      "source": "이 자식, 귀신이네. 안 그래도 연락하려고 했는데."
    },
    {
      "chapter": 47,
      "confidence": 0.99,
      "current": "My martial arts, my stats, and even my steel-like Sinews and Bones had come with it.",
      "defect": "The established System attribute terminology is not used.",
      "id": "R0047-01",
      "rationale": "The block glossary establishes 근골 as “Muscles and Bones.”",
      "replacement": "My martial arts, my stats, and even my steel-like Muscles and Bones had come with it.",
      "severity": "minor",
      "source": "무공과 능력치. 그리고 강철 같은 근골까지 포함이다."
    },
    {
      "chapter": 48,
      "confidence": 1.0,
      "current": "“Luxury Nutjob? Who’s that?”",
      "defect": "Team Leader Choi’s established contact display name is replaced with a different rendering.",
      "id": "R0048-01",
      "rationale": "The block glossary explicitly establishes 명품충 as the display name “Designer-Brand Junkie.”",
      "replacement": "“Designer-Brand Junkie? Who’s that?”",
      "severity": "minor",
      "source": "“명품충? 누구야 이건?”"
    },
    {
      "chapter": 48,
      "confidence": 0.99,
      "current": "Jinho hyung stared blankly, looking from me to the phone in my hand.",
      "defect": "The phone is assigned to Taekyung’s hand, but the source says Jinho is holding it.",
      "id": "R0048-02",
      "rationale": "손에 쥔 핸드폰 refers to the phone Jinho has just been given and is currently holding.",
      "replacement": "Jinho hyung stared blankly, looking from me to the phone in his hand.",
      "severity": "minor",
      "source": "진호 형이 멍한 얼굴로 나와 손에 쥔 핸드폰을 번갈아 봤다."
    },
    {
      "chapter": 48,
      "confidence": 1.0,
      "current": "“Squad leader, squad leader!”",
      "defect": "The established form of address is replaced with a different rank.",
      "id": "R0048-03",
      "rationale": "The block glossary establishes 조장, Hyuk Mujin’s address for Taekyung, as “Captain.”",
      "replacement": "“Captain, Captain!”",
      "severity": "major",
      "source": "조장, 조장!"
    },
    {
      "chapter": 48,
      "confidence": 1.0,
      "current": "“Why is the squad leader suddenly like this now of all times…”",
      "defect": "The repeated established form of address is again replaced with a different rank.",
      "id": "R0048-04",
      "rationale": "The block glossary establishes 조장 as “Captain,” and the dream voice is referring to Taekyung by that title.",
      "replacement": "“Why is Captain suddenly like this now of all times…”",
      "severity": "major",
      "source": "조장은 왜 갑자기 이럴 때……."
    }
  ]
}
```

## Chapter 45

### Korean source

```text
＃45화



서걱.

붉은 눈동자가 온순하게 깜빡인다. C급 레어 몬스터, 그 무시무시한 홉 고블린 대전사도 이런 표정을 지을 수 있구나.

‘지금껏 왜 몰랐을까.’

가벼운 의문과 함께 창날에 묻은 피를 털었다. 동시에.

쿵.

육중한 뭔가가 땅으로 떨어졌다. 물건의 정체를 확인한 대전사가 저도 모르게 주춤주춤 뒷걸음질 친다.

그래, 그럴 만도 하지. 팔꿈치 아래로 오른팔이 싹둑 잘려 나갔으니.

‘그래도 너는 좀 다를 줄 알았는데.’

진가보법. 그래, 나는 바로 그 진가보법을 펼치며 놈의 품속으로 파고들었다. 대전사가 반사적으로 오른팔을 휘둘렀지만 이미 잘려 나간 그곳은 텅 비어 있었다.

“벌써 잊었냐?”

나는 대전사의 옆구리에 창날을 붙이고 동시에 위로 쳐올렸다. 공력을 머금은 창날이 딱딱한 피부와 근육을 갈라낸다.

서걱-

초록색 핏물과 함께 놈의 왼팔이 떨어져 나왔다.

순식간에 양팔을 잃은 홉 고블린 대전사가 분노와 고통으로 뒤범벅된 고함을 내질렀다.

- 크아아아악!

하지만 방심은 금물이다. 양팔을 잃었지만 놈은 맨몸으로도 충분히 위협적인 존재니까.

“어. 들어와.”

말이 끝나기도 전에 거대한 신형이 달려들었다.

캉! 캉! 캉!

역시, 이 녀석은 육체 자체가 무기다. 괴물답게 인간을 뛰어넘은 원시적인 감각과 힘을 지니고 있다.

쉭. 촤악.

갈고리발톱이 팔뚝을 스쳤다. 살점이 한 움큼 뜯겨 나가고 피가 쏟아진다. 나는 동요하지 않고 정수리를 향해 내리 찍히는 발뒤꿈치를 막아 냈다.

쿵. 까드득.

내가 딛고 선 지면이 점점 꺼지기 시작한다.

엄청난 힘. 이대로는 선 채로 파묻힐지도 모른다.

‘공력이 없었다면, 말이지.’

나는 단전의 모든 공력을 끌어 올렸다. 사지백해로 흘러 들어간 힘. 서서히 올라오는 창대에 놈의 눈동자가 흔들렸다.

‘늦었어.’

처음부터 온전한 상태였다면 모를까, 이미 양팔을 잃은 홉 고블린 대전사는 더 이상 내 상대가 되지 못한다.

- 크르르.

결국 놈이 먼저 물러났다. 그리고 그 시점에서 이미 승부는 갈린 거나 마찬가지였다.

나는 멈추지 않고 창을 뻗어 냈다.

‘진가창법 일 초식.’

몸과 머릿속에 각인된 동작들이 빠르게 펼쳐졌다.

찌른다. 벤다. 창대로 막고 때린다. 따로 보면 단순한 동작이지만 순서와 위치에 따라 무수한 조합이 탄생한다.

그게 내가 정의 내린 무공(武功)이다.

캉! 캉!

쉭. 쉬쉬쉭!

이 초식. 삼 초식. 사 초식…….

강철만큼 단단하던 갈고리발톱이 잘려 나갔다. 한 걸음씩 물러날 때마다, 새로운 상처가 생기고 더 많은 피가 쏟아졌다.

어느 순간 홉 고블린 대전사의 등이 벽면에 닿았다.

“크르륵…….”

C급 레어 몬스터. 도저히 상대할 수 없을 것 같던 이 괴물의 붉은 눈동자는 이미 전의를 상실한 지 오래였다.

“가라, 이제.”

푹.

끄륵. 단말마와 함께 녹색 거체가 벽면을 타고 미끄러진다.

그리고.

띠링.



- [Lv.45 홉 고블린 대전사]를 처치했습니다!

- 레벨 업!



시스템 알림이 울렸다. 다시는 듣지도, 보지도 못할 거라고 생각했는데…….

‘난데없이 시스템이라니.’

하지만 혼란스러워하는 건 나만이 아니었다.

“……진태경 씨?”

어느새 제사장을 처리한 최 팀장의 동공이 지진 난 것처럼 흔들린다. 그가 나와 대전사의 시체를 번갈아 바라봤다.

“당신…… 정체가 뭡니까?”

그러게. 그거 나도 알고 싶다.

허허, 허허허.



* * *



“레어 몬스터요?”

공무원이 물고 있던 담배가 툭 떨어졌다.

천생 공무원 체질로 보이는 그로서는 영 좋은 소식은 아니다. 아니나 다를까, 우리를 살펴보는 눈빛이 불안하기 짝이 없다.

“며, 몇 급이요?”

최 팀장이 피곤한 얼굴로 제사장의 지팡이를 흔들었다.

쩔그럭.

“C급 레어, 홉 고블린 제사장.”

“C급?! 이런 씨…….”

어, 욕 아껴 둬. 하나 더 있으니까.

나는 지팡이처럼 짚고 있던 홉 고블린 대전사의 대검을 발로 찼다. 둔탁한 소리에 공무원이 고개를 돌린다.

“그건?”

“하나 받고 하나 더. C급 레어, 홉 고블린 대전사.”

“중급 레어 몬스터가 둘? 겨우 E급 게이트에?”

그의 반응을 이해한다. 이건 뭐, 말이 되는 수준이어야지.

공무원은 한동안 우리와 장비를 번갈아 바라보다가 결국 슬픈 얼굴로 고개를 끄덕였다.

“일단 상부에 연락하겠습니다.”

“어이, 아저씨. 잠깐만.”

어느새 정신을 차린 임꺽정이다. 내 부축을 받고 있는 그는 최소 뼈 다섯 군데가 부러지는 중상을 입었다.

“힐러 불러 줘. 예쁜 언니로.”

E급 트리오도 땅바닥에 털썩 주저앉았다.

“포션도 줘! 포션! 좋은 걸로다가!”

“에이 시발, 게이트 관리를 어떻게 한 거야!”

“장비도 다 박살 나고, 어! 이거 다 어떡할 거야!”

어떡하긴 뭘 어떡해. 정부 쪽에서 다 보상해 주겠지.

이 경우 게이트에서 소비된 모든 물품과 치료비 및 보상금까지 지급해 주는 법률이 버젓이 존재한다.

저건 그러니까, 조금이라도 더 뜯어내려는 쇼인 거다.

‘쯧쯧. 아무리 그래도 그렇지. 사람들 눈이 있는데.’

그때 옆에서 따가운 시선이 느껴졌다.

“……태경 씨.”

최 팀장이다.

“뭐 하십니까?”

그는 혼란스러운 눈빛으로 나를 바라보고 있었다. 정확히 말하면 단검을 쥔 내 손을.

그그극.

공력이 실린 단검에 죽죽 그어진 7년 차 가죽 갑옷은 더 이상 사용할 수 없을 만큼 망가져 있었다.

“…….”

“…….”

“최 팀장님.”

나는 땅이 꺼져라 한숨을 내쉬었다.

“홉 고블린 대전사. 정말 강한 놈이더군요. 목숨은 건졌지만 갖고 있는 모든 장비가 망가져 버렸어요.”

“…….”

“7년 동안 절 지켜 준 갑옷, 이제는 창까지.”

“창은 멀쩡해 보이는…….”

그 순간, 나는 한쪽 발로 창의 중앙을 지그시 눌렀다.

세 자릿수 근력 스탯의 위엄에 철창이 엿가락처럼 휘어진다.

“멀쩡하다고요? 이게요?”

“…….”

최 팀장은 입을 다물었다.



* * *



최 팀장은 책임자 자격으로 파견된 공무원들에게 불려 갔고, 나머지 넷은 치료를 받기 위해 앰뷸런스로 옮겨졌다.

나는 퀴퀴한 휴게실 대신 넓고 쾌적한 사무실에 홀로 남았다. 막상 그 순간이 다가오자 심장이 쿵쾅거리며 뛰었다.

‘사, 상태창?’

반신반의하는 그 부름에, 시스템이 응답했다.

띠링.



상태창



[Lv.33 진태경]

직업 : 일류 무인

명성 : 0

칭호 : 2개 (칭호 효과 적용 중)

- 초보 수련자 (수련 속도 +10%)

- 승부사 (일대일 승부 시 전투 관련 능력치 10% 향상)

근력 : 120  체력 : 125

민첩 : 121 지력 : 20

매력 : 20공력 : 15년

잔여 포인트 : 30



- 동기화가 완료된 상태입니다. 칭호와 명성에 변화가 생깁니다.



“시발. 진짜 뜨네.”

잠시 넋 놓고 상태창을 바라보던 나는 뭔가 이상한 점을 깨달았다.

‘상태창이…… 바뀌었다?’

일단 가장 먼저 눈에 띈 건 0으로 리셋된 명성과 사라진 칭호 두 가지다. 마지막 줄을 읽어 보니 대충 짐작 가는 부분이 있었다.

‘무림이 아니라서?’

내가 쌓은 500의 명성은 모두 무림인으로서 쌓은 것이다. 그리고 이번에 사라진 칭호, [명가의 자제]도 같은 맥락에서 이해할 수 있다.

‘하긴, 나는 여기서 명문가 자제도 아니고, 잠룡 같은 건 더더욱 아니니까.’

굳이 칭호를 받는다면 서민층 자제나 잠룡 대신 지렁이. 뭐 그런 수준일 게 뻔하다.

“다른 건 얼마나 바뀌었을라나?”

나는 십여 분간 시스템의 모든 기능을 한 번씩 켰다 끄며 시험해 봤지만 달라진 건 상태창뿐이었다.

아니, 하나 더 있긴 했다. 바로 퀘스트창이다.

띠링.



퀘스트



[배신자]

당신은 배신자의 정체를 알아냈습니다. 본대에 합류하여 배신자가 있음을 알리고 전투를 승리로 이끄십시오!



등급 : 절정

제한 : 진태경

임무 : 배신자 처단 (미완료)

 전투 승리 (미완료)

보상 : 막대한 경험치와 명성

 귀중한 철궤

실패 : 사망





곽준과 암살자들을 해치우고 받은 연계 퀘스트다. 나는 머릿속이 복잡해지는 것을 느꼈다.

‘다시 돌아가라는 건가? 무림으로?’

이제는 안다. 내가 겪은 무림은 환상도, 게임도 아니라는 것을. 매우 비현실적인 이야기지만 무림은 아마도…….

끼익.

갑작스러운 소리에 고개를 돌렸다. 최 팀장이 문 앞에 서 있었다.

“가시죠, 태경 씨.”

대충 이야기가 마무리된 모양이다. 나는 생각을 접고 일어났다.

“다른 분들은…….”

“지금쯤이면 병원으로 가고 있을 겁니다. 일주일 정도 입원해야 한다고 해서요. 걱정하실 필요 없습니다.”

딱히 걱정은 하지 않는다. 전투 계열 헌터의 튼튼한 신체에 포션, 치료 마법까지 받았으니 곧 자리를 털고 일어날 것이다.

그리고…….

“어떻게 됐나요?”

“며칠 내로 다시 연락이 올 겁니다. 아마 태경 씨한테도 조사관이 갈 거고요.”

조사관이라.

다시 마주치고 싶지 않은 부류다. 하지만 내가 원한 대답은 이게 아니었다. 그래서 다시 물었다.

“다른 건요?”

“흠.”

최 팀장이 묘한 표정으로 나를 바라봤다. 마치 신기한 동물을 쳐다보는 것 같은 눈초리였다.

‘사실대로 말했을까?’

내 힘을 드러내고 싶지 않다. 왜 현실에서 시스템이 보이는지, 무림과의 연관성도 잘 모르는 이 시점에서는 더더욱.

F급 헌터가 C급 레어 몬스터를 혼자서 잡았다는 것은 유례없는 일이다. 낭중지추. 튀어나온 송곳과는 반대되는 인생을 살아온 나로서는 조심스러울 수밖에.

그래서 그에게 부탁했다.



‘저에 관해서는 비밀로 해 주실 수 있을까요?’



최 팀장의 입장에서는 어려운 부탁이었을 것이다. 난생처음 보는 사람을 위해 허위 진술을 하라는 소리니까.

“진태경 씨.”

“네.”

무거운 목소리에 덩달아 마음이 무거워지던 그때였다.

“밥이나 먹읍시다.”

“예?”

“보세요.”

최 팀장이 손목을 내밀었다. 번쩍거리는 마정석 전자시계는 오후 두 시를 가리키고 있었다.

“C급 마정석을 통으로 깎아 만든 N사 제품이죠. 강화 마법이 걸려 있어서 위급 시 방패로도 쓸 수 있습…….”

그쪽이었냐.

“……갑시다.”

도무지 종잡을 수 없는 인간이다.

“고기나 좀 먹죠. 한우 좋아해요?”

“한우요?”

“네. 특등급.”

그리고 돈도 많은 인간이다.

“없어서 못 먹습니다.”

다른 것도 아니고 한우다. 그것도 특등급 한우.

시스템이고 나발이고 일단 허기진 배부터 채워야겠다.
```

### Current accepted English

```markdown
# Chapter 45

Slash.

The red eyes blinked, almost tame. So even a C-rank Rare Monster—the terrifying Hobgoblin Great Warrior—could make a face like that.

*Why didn’t I realize it until now?*

With that passing thought, I shook the blood off the spearhead. At the same time—

Thud.

Something heavy hit the ground. The Great Warrior saw what it was and, without meaning to, shuffled backward.

Well, fair enough. Its right arm had been snipped clean off below the elbow.

*I thought you’d be a little different.*

Jin Family’s Manoeuvre Technique. Yeah—I’d used that exact technique to drive in against its chest. The Great Warrior reflexively swung its right arm, but that space was already empty.

“Forgot already?”

I set the spearhead against the Great Warrior’s side and drove it upward in the same motion. Charged with internal energy, the blade split hard skin and muscle.

Slash—

Its left arm came off in a spray of green blood.

Both arms gone in an instant, the Hobgoblin Great Warrior bellowed, the sound smeared with rage and pain.

—Kuwaaaaaargh!

But I still couldn’t let my guard down. Even without arms, it was more than dangerous enough bare-handed.

“Yeah. Come on in.”

Before I’d even finished, that massive frame charged.

Clang! Clang! Clang!

As expected, this thing’s body was a weapon all by itself. True to being a monster, it had primitive senses and strength beyond any human.

Swish. Slash.

Hooked claws grazed my forearm. A handful of flesh tore away, and blood poured out. Without flinching, I blocked the heel stomping down at the crown of my head.

Thud. Crunch.

The ground under my feet started to sink.

Incredible strength. At this rate, I might get buried standing up.

*If I didn’t have internal energy, that is.*

I drew up every last bit of internal energy in my dantian. The force flooded into every limb. As the spear shaft slowly rose, the Great Warrior’s eyes wavered.

*Too late.*

If it had been whole from the start, maybe. After losing both arms, the Hobgoblin Great Warrior was no longer my match.

—Grrr.

In the end, it was the one that backed off first. And from that point, the fight was as good as decided.

I didn’t stop. I thrust the spear out.

*Jin Family’s Spear Technique. First form.*

The movements engraved in my body and head unfurled in a rush.

Thrust. Cut. Block and strike with the shaft. Simple on their own, but the order and the angles made countless combinations.

That was martial arts, as I defined it.

Clang! Clang!

Swish. Swish-swish-swish!

Second form. Third form. Fourth…

Those hooked claws, hard as steel, were cut away. Every step it gave, a new wound opened and more blood spilled.

Then the Hobgoblin Great Warrior’s back hit the wall.

“Grrrk…”

A C-rank Rare Monster. This thing had seemed impossible to face, but those red eyes had already lost their will to fight a long time ago.

“Go. Now.”

Shunk.

Ghk. With a death rattle, the hulking green body slid down the wall.

And then—

Ding.

> **System**
>
> You have defeated Lv. 45 Hobgoblin Great Warrior!
>
> Level Up!

The System notification rang. I’d thought I’d never hear it or see it again…

*A System, out of nowhere?*

I wasn’t the only one confused.

“…Mr. Jin Taekyung?”

Team Leader Choi had already taken care of the Priest. His pupils trembled like they’d been hit by an earthquake as he looked from me to the Great Warrior’s corpse and back.

“What… are you?”

Yeah. I’d like to know that myself.

Heh heh. Heh heh heh.

* * *

“A Rare Monster?”

The cigarette in the government official’s mouth dropped.

He looked born to be a civil servant, and this was anything but good news for him. Sure enough, the way he looked us over was nothing but unease.

“W-what rank?”

Team Leader Choi gave the Priest’s staff a weary shake.

Clank.

“C-rank Rare. Hobgoblin Priest.”

“C-rank?! For fuck’s—”

Hey, save the swearing. There’s one more.

I kicked the Hobgoblin Great Warrior’s greatsword I’d been using like a walking stick. At the dull sound, the official turned.

“And that?”

“Buy one, get one more. C-rank Rare. Hobgoblin Great Warrior.”

“Two mid-grade Rare Monsters? In an E-rank Gate?”

I got the reaction. This had to at least make some kind of sense.

The official looked back and forth between us and the gear for a while, then finally nodded with a sad face.

“I’ll contact my superiors first.”

“Hey, mister. Hold on.”

Im Kkeokjeong had come to at some point. I was holding him up. He’d taken serious injuries—at least five broken bones.

“Call a healer. A pretty unnie.”

The E-rank trio dropped onto the ground as well.

“And potions! Potions! The good stuff!”

“Ah, for fuck’s sake, how did you people even manage this Gate?!”

“Our gear’s all smashed too, huh? What are you going to do about this?!”

Do about it? The government would cover everything.

There was an actual law for this: every item used in the Gate, plus medical costs and compensation.

So it was a show. Squeeze out a little extra.

*Tsk. Even so. People are watching.*

That was when I felt a stinging look from beside me.

“…Mr. Taekyung.”

Team Leader Choi.

“What are you doing?”

He was looking at me, confused. More precisely, at the hand holding my dagger.

Grrrk.

The dagger, charged with internal energy, raked long lines through seven-year leather armor until it was too wrecked to use.

“...”

“...”

“Team Leader Choi.”

I sighed hard enough to cave in the ground.

“The Hobgoblin Great Warrior. It was really strong. I made it out alive, but every piece of gear I had is ruined.”

“...”

“The armor that protected me for seven years. And now even the spear.”

“The spear looks perfectly—”

Right then, I pressed down steadily on the middle of the spear with one foot.

Under the majesty of a three-digit Strength stat, the iron spear bent like a stick of taffy.

“Looks perfectly fine? This?”

“...”

Team Leader Choi shut his mouth.

* * *

Team Leader Choi was called away by the officials dispatched to take charge, and the other four were moved to an ambulance for treatment.

Instead of the musty break room, I was left alone in a wide, comfortable office. Now that the moment had actually come, my heart started pounding.

*St-Status Window?*

At that half-doubtful call, the System answered.

Ding.

> **System**
>
> **Status Window**
>
> **Lv. 33 Jin Taekyung**
>
> **Job:** First Rate Martial Artist
>
> **Fame:** 0
>
> **Titles:** 2 (Title effects active)
>
> - Novice Trainee (Training speed +10%)
> - Gambler (Combat-related stats +10% in one-on-one matches)
>
> **Strength:** 120  **Stamina:** 125
>
> **Agility:** 121  **Intelligence:** 20
>
> **Charm:** 20  **Internal Energy:** 15 years
>
> **Remaining Points:** 30
>
> Synchronization has been completed. Changes have occurred to Titles and Fame.

“Fuck. It really came up.”

I stared at the Status Window, blank, then noticed something off.

*The Status Window… changed?*

The first things that jumped out were Fame reset to zero and two missing Titles. The last line gave me a rough idea why.

*Because this isn’t Murim?*

All five hundred Fame I’d stacked had been earned as a martial artist in Murim. The Title that had vanished, *Scion of a Prestigious Family*, made sense the same way.

*Well, I’m not some prestigious family’s son here. And I’m sure as hell no Sleeping Dragon.*

If I were getting a Title here, it’d obviously be something like *Scion of the Common Folk*, or *Earthworm* instead of Sleeping Dragon.

“How much else changed?”

For about ten minutes I turned every System function on and off and tested them. The only thing that had changed was the Status Window.

No. There was one more. The Quest Window.

Ding.

> **System**
>
> **Quest**
>
> **Traitor**
>
> You have discovered the traitor’s identity. Rejoin the main force, inform them that there is a traitor, and lead the battle to victory!
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Mission:** Punish the traitor (Incomplete)
>
> Battle victory (Incomplete)
>
> **Reward:** Vast EXP and Fame
>
> Valuable iron chest
>
> **Failure:** Death

The Chain Quest I’d gotten after taking down Gwak Jun and the assassins. My thoughts tangled.

*Go back? To Murim?*

I knew it now. The Murim I’d been through wasn’t an illusion, and it wasn’t a game. A wildly unrealistic story, sure, but Murim was probably…

Creak.

I turned at the sudden sound. Team Leader Choi was standing in the doorway.

“Let’s go, Mr. Taekyung.”

Looked like the talk had wrapped up. I folded the thought away and stood.

“The others…?”

“They should be on their way to the hospital by now. They said about a week of admission. You don’t need to worry.”

I wasn’t particularly worried. Combat-type Hunter bodies, plus potions and healing magic—they’d be up soon enough.

And…

“How did it go?”

“They’ll contact us again in a few days. An investigator will probably come see you, too.”

An investigator.

Not a type I wanted to run into again. But that wasn’t the answer I’d wanted, so I asked again.

“And the rest?”

“Hmm.”

Team Leader Choi looked at me with an odd expression. Like he was studying some strange animal.

*Did he tell them the truth?*

I didn’t want my strength out in the open. Even less now, when I still barely knew why the System was showing up in reality, or what it had to do with Murim.

An F-rank Hunter killing a C-rank Rare Monster alone was unheard of. An awl in a bag pokes through. I’d lived the opposite kind of life, nothing sticking out, so I had to be careful.

So I asked him.

“Could you keep what concerns me a secret?”

From Team Leader Choi’s side, it had to be a hard ask. I was telling him to lie in his statement for someone he’d only just met.

“Mr. Jin Taekyung.”

“Yes.”

His heavy voice made my chest sink with it—and then:

“Let’s get some food.”

“What?”

“Look.”

Team Leader Choi held out his wrist. A glittering Magic Gem electronic watch pointed to two in the afternoon.

“It’s an N Company piece carved from a whole C-rank Magic Gem. It’s got enhancement magic, so in an emergency you can even use it as a shield—”

*So that’s where he was going.*

“…Let’s go.”

Impossible man to read.

“Let’s get some meat. You like Hanwoo?[^1]”

“Hanwoo?”

“Yes. Highest grade.”

And rich, too.

“I never get to eat it.”

Not just any beef. Hanwoo. Top-grade Hanwoo at that.

System or whatever—first I had to fill a hungry stomach.

[^1]: Hanwoo is beef from Korean native cattle, prized as premium meat.
```
## Chapter 46

### Korean source

```text
＃46화



치이이익.

불판 위에 고기가 올라갔다. 붉고 두툼한, 마블링이 흰 눈꽃처럼 올올이 박혀 있는 최고급 한우다.

형태, 소리, 냄새. 모두 황홀했다. 한 가지 마음에 안 드는 건 가격이었지만…….

“이걸로 되겠어요? 먹고 더 시키죠. 특수 부위로.”

돈 많은 C급 헌터님이 내는 거니까, 뭐.

‘이게 얼마 만의 한우냐.’

무림의 음식은 맵고 짜고 싱겁다. 그마저도 제대로 못 먹는 날이 더 많았다. 30일간 내 위장은 육포와 벽곡단, 주먹밥으로 혹사당했다.

우걱. 우걱우걱.

소고기의 좋은 점은 금방 먹을 수 있다는 거다. 대충 익었다 싶으면 그대로 입으로 직행.

한번 씹을 때마다 구름 위를 걷는 기분이다. 이것도, 요것도, 저것도, 하나같이 천국의 맛이다.

“흐어어.”

그런 나를, 최 팀장은 특유의 묘한 표정으로 바라봤다.

“더 드실래요?”

“아뇨. 과식은 자제해야죠.”

“지금 25인분짼데…….”

“각자 12인분이면 그렇게 많지도 않네요.”

“전 3인분밖에 안 먹었습니다.”

“아, 육회 시켜도 돼요?”

“……네.”

“공깃밥도.”

“…….”

그렇게 폭풍 같은 식사가 끝난 뒤. 드디어 최 팀장의 입이 열렸다.

“제가 잡았다고 했습니다. 제사장과 대전사, 둘 다.”

“아, 감사합니다.”

“천만에요. 정당한 거래라고 해 둡시다. 오히려 제가 감사한 부분도 있죠.”

정당한 거래라.

맞는 말이다. 나는 생각할 시간을 벌었고, 그는 명성을 얻게 될 것이다. 하급 헌터 다섯을 데리고 중급 레어 몬스터를 둘이나 잡았으니까.

그 과정에서 사망자 하나 나오지 않았다는 사실은 길드 홍보에도 큰 도움이 될 테고.

‘만약 내가 동기화로 힘을 찾지 못했다면?’

글쎄, 누군가는 죽지 않았을까 싶다. 어쩌면 아무도 살아 나오지 못했을 수도 있고.

“이미 그렇게 생각하고 계셨군요.”

마냥 괴짜는 아니다. 이렇게 눈치가 빠른 걸 보면.

나는 어색하게 웃었다.

“서로에게 좋은 일이니까요.”

“서로에게 좋다. 서로에게…….”

중얼거리던 최 팀장이 불쑥 물었다.

“길드 가입하실래요?”

“푸웁.”

식탁보를 들어 물을 막아 낸 최 팀장이 세련된 솜씨로 명함 한 장을 꺼냈다.



[평화 길드 1팀장 최민우]



뭐야, 이거. 순간 엄청 당황했다.

“스, 스카우트 제의하신 건가요. 지금?”

“그렇죠. 인재는 항상 필요하니까.”

명함을 받아 든 나는 왠지 감개무량해졌다.

새우처럼 허리 굽히고 다니면서 면접 보던 게 엊그제 같은데…….

‘오래 살다 보니 별일이 다 있네.’

무려 인재 취급받으면서 스카우트 제의라니. F급 헌터 진태경, 많이 컸다.

“우리 길드가 아직 신생이고 인원수도 적긴 합니다만, 실속이 매우 훌륭합니다. 음, 예를 들자면…….”

최 팀장이 우아하게 와인잔을 흔들었다. 세상에 저건 또 언제 시켰대.

“재정이 굉장히 탄탄하죠.”

“오오, 재정!”

“그렇다 보니 직원 복지도 좋고요.”

“오오, 탄탄한 재정을 바탕으로 한 복지!”

“길드장님은 B급 헌터시고.”

“오오, 탄탄한 재정의 원천인 상위 헌터!”

“구조 조정 걱정은 없습니다.”

“오오, 안정된 직장!”

최 팀장이 부유한 미소를 머금고 물었다.

“오시겠습니까?”

나는 머리를 긁적였다.

“아뇨. 그건 좀.”

“……예?”

“제가, 당장은 곤란한 사정이 있어서요. 시간이 필요합니다.”

마음 같아서는 당장 계약서에 싸인, 도장, 지장, 키스 마크까지 남기고 싶다.

‘하지만 내일 당장 시스템이 사라져 버리면?’

바로 개털이다.

하루아침에 인재(人才)에서 인재(人災) 소리 듣게 되는 거지.

“혹시 돈 문제입니까?”

돈 문제야 항상 있지.

하지만 이건 더 중요한 문제다. 당장 눈앞의 돈뭉치에 홀려서 덥석 결정할 수 없다.

“말씀드리기가 어렵네요. 아쉽지만 지금 당장 결정할 문제가 아닌…….”

“일억.”

“억?”

“순수 계약금만. 나머지는 최소 C급 헌터 조건으로 맞춰 드리죠.”

위험했다. 이번엔 진짜 위험했어.

그러나 나는 초인적인 인내심으로 참았다. 세상살이가 그렇게 호락호락한 게 아니라는 건 진즉 깨닫지 않았나.

먹고 체하는 돈이 될 수도 있다.

“죄송합니다.”

나를 물끄러미 바라보던 최 팀장은 이내 고개를 끄덕였다.

“연락 기다리겠습니다.”



* * *



한 사람은 떠나고, 한 사람은 남았다.

최 팀장, 아니 최민우는 진태경이 떠난 자리를 말없이 바라보다가 핸드폰을 꺼냈다.

뚜, 뚜, 달칵.

- 이 자식, 귀신이네. 안 그래도 연락하려고 했는데.

“아까 말한 거, 어떻게 됐어?”

- 일단 네 부탁이니까 알아보긴 했는데…… 이 진태경이라는 사람, 뭐 있냐?

“그게 궁금해서 너한테 연락한 거지. 그래서 결과는?”

- 널리고 널린 케이스지 뭐. 7년 전 스무 살에 각성, 측정 결과 F급. 헌터 훈련소에서 수석으로 수료한 기록이 있고…….

수화기 너머로 진태경의 지난 7년이 흘러나왔다. 그러던 어느 순간, 최민우의 눈썹이 꿈틀했다.

“뭐? 상동역 변이 게이트?”

- 어. 너도 그 사건 알지?

모를 리가 있나. 불과 2년 전의 일이라 최민우도 똑똑히 기억하고 있었다.

- 그 사건 유일한 생존자더라고. 그 부분은 나도 확인하고 좀 놀랐다.

최민우는 물잔을 기울였다. 중급 레어 몬스터를 단신으로 잡은 F급 헌터, 그 실마리를 잡았다고 생각하니 목이 탔다.

“그리고?

- 반년 동안 휴직. 관리청 쪽에서 조사관들 수시로 보내고, 뭐 이래저래 마음도 추스르고 했나 보더라고. 너도 알다시피 사안이 좀 컸으니까.

“그래서?”

- 그게 끝. 다시 길드 복직해서 일 년 반 동안 좆 빠지게 게이트 돌다가 잘렸어. 그게 딱 사흘 전이고.

“잘린 이유는?”

- 일단 구조 조정이긴 한데…… 코딱지만 한 중소 길드가 무슨. 아마 그 사건 영향이 클 거야. 관리청 눈치 슬금슬금 보다가 내보낸 거지. 그쪽 입장에서는 껄끄러울 테니까.

“그게 끝이야?”

- 내가 보기에는. 따로 파일 보내 줘?

“바로 보내. 그럼 끊는다.”

- 야, 야!

뚝.

최민우는 긴 손가락으로 탁자를 두드렸다.

진태경. F급 헌터. 상동역 변이 게이트의 유일한 생존자.

그리고…….

‘최소 C급 헌터.’

말 그대로 최소로 잡았을 때의 이야기다. C급 레어 몬스터를 혼자, 그것도 압도적인 힘과 기술로 몰아붙이던 그 모습이 눈앞에 아른거렸다.

‘그런데 F급이란 말이지.’

둘 중 하나다. 힘을 숨겼거나, 최근 재각성을 했거나.

최민우는 후자라고 짐작했지만, 그것 역시 상식을 벗어난 일임에는 변함이 없었다.

평생 승급 한 번 못 해 보고 은퇴하는 헌터가 한둘인가.

F급에서 C급으로의 재각성은, 단언컨대 극히 드문 일이다.

‘이게 무슨 게임도 아니고. 도대체 정체가 뭐야?’

최민우는 고개를 저었다. 귀신에 홀린 기분이다.

‘좀 더 알아봐야겠군.’

자리에서 일어나는 그에게 사장이 다가와 계산서를 내밀었다.

“193만 7천 원입니다.”

“…….”

정말 귀신에 홀린 기분이다.



* * *



“시바, 좆 됐다.”

나는 털썩 주저앉았다. 너저분한 분리수거장. 응당 있어야 할 물건이 보이지 않았다.

“없다, 없어. 내 캡슐이 없어.”

최 팀장과 헤어질 때부터 초조하긴 했다. 하지만 반나절도 안 돼서 누가 가져갈 줄이야. 나는 허공을 향해 부르짖었다.

“어떤 새끼야!”

그리고 대답이 들려왔다.

“나다, 이 십새끼야.”

고시원 건물 옥상. 아침에 봤던 그 자리에서 진호 형이 담배를 피우고 있었다. 뭔가 아련한 표정으로 담배 연기를 뿜어낸 그가 말을 이었다.

“내가 10년 동안 울면서 후회하고 다짐했는데…….”

“진짜 울면서 후회하게 해 줘?”

“재미없는 새끼. 너 이 영화 모르지?”

“장난치지 마. 지금 심각하니까.”

“왜, 오늘 허탕 쳤냐.”

“아니.”

나는 힘이 쭉 빠진 목소리로 말을 이었다.

“캡슐.”

“……엉?”

“어떤 새끼가 내 캡슐 가져갔어.”

“콜록, 콜록콜록!”

담배 연기를 잘못 빨아들였는지 미친 듯이 기침하던 진호 형이 겨우 말문을 열었다.

“그, 필요 없어서 버린 거 아니냐?”

“그랬지.”

시스템이 돌아오기 전까지는.

불과 몇 시간 만에 상황이 이렇게 변하리라곤 나도 생각하지 못했다.

‘하루만 더 갖고 있을걸.’

어디서부터 찾아야 하나. 나는 한숨을 푹 내쉬었다.

“형, 혹시 누가 가져갔는지 못 봤지?”

“어…… 그게.”

진호 형이 머리를 긁적였다.

“봤다면 본 거고. 못 봤다면 못 본 건데.”

이게 말이냐, 똥이냐.

내가 노려보자 그가 쑥스럽다는 듯 웃었다.

“그 뭐냐, 내가 사례금 같은 걸 바라는 건 절대 아니고…….”

사례금을 바라는 게 절대 맞는 것 같은데.

아무튼 그게 중요한 게 아니다. 나는 벌떡 일어나 물었다.

“봤어? 확실해?”

“굳이 따지자면 본 쪽이지.”

“누구? 어디로 갔어!”

“사례금을 바라는 건 아니지만, 예상 금액은 어느 정도?”

“……10만 원?”

“어이구, 나도 나이가 들었나. 기억이 가물가물하네.”

“이런 시팔.”

“그래, 날 더운데 수고해라.”

“사례금은 십팔만 원입니다.”

금액이 마음에 드는지 진호 형이 환하게 웃었다.

“네 캡슐. 내가 주웠다.”

“……?”

이해하는 데 딱 3초 걸렸다.

‘이런 날강도 같은 인간을 봤나.’

기가 막히고 코가 막힌다. 이런 식으로 사람 뒤통수를 쳐?

“근데 마땅히 놔둘 데가 없더라고. 내 방에 놓기에는 너무 좁잖아.”

“그래서?”

“네 방에 다시 놔뒀어. 잘했지?”

저 인간을 어떻게 때려야 야무지게 때렸다고 소문이 날까.

나는 주먹을 부르르 떨었다.



* * *



“진짜 있네.”

아무 일도 없던 것처럼 원룸 절반을 차지한 캡슐을 보니 헛웃음만 나왔다.

‘이걸 운이 좋다고 해야 하나.’

그 많은 사람 중에서 캡슐을 가져간 게 진호 형이라니.

나는 캡슐 뚜껑을 열었다. 낡은 좌석에 던지듯 넣어 놓은 사용 설명서를 집어 들어 마지막 페이지를 펼쳤다.



[주요 기능]

- 한 사람만을 위한 맞춤형 캡슐! 사용자 등록 시 캡슐이 영구 귀속되며, 이는 사망 전까지 유효합니다.



……에이, 설마.

‘단순한 우연이겠지.’

하지만 찜찜함이 가시지 않는다. 나는 이 모든 사건의 근원인 캡슐을 노려보았다.

‘이거 뭐 하는 물건이야?’

오늘 아침 캡슐을 분리수거장에 버렸던 이유는 다 잊기 위함이었다. 가뜩이나 퍽퍽한 인생, 악몽 한 번 꿨다 생각하고 지금처럼 내 인생을 살기 위해서.

하지만 이제는 상황이 달라졌다.

‘시스템이 생겼으니까.’

시스템이라…….

그때 문득 생각나는 게 있었다. 나는 캡슐 표면에 손을 올리고 중얼거렸다.

“아이템 확인.”

띠링.

그럼 그렇지. 입꼬리가 올라간 그 순간이었다.



- 해당 아이템을 읽을 수 없습니다.



“……읽을 수 없다고?”

이런 경우는 처음이다.

‘무림이 아니라서 그런가?’

나는 당황스러운 마음에 방 안의 물건들을 닥치는 대로 확인했다. TV부터 볼펜, 심지어는 베개까지. 그때마다 시스템은 정확한 정보를 표시해 줬다.

그런데 딱 하나. 캡슐만큼은 읽을 수 없다.

“와, 이거 골 때리네.”

혹시 싶어 사용 설명서를 집어 들었지만 역시나.

띠링.



- 해당 아이템을 읽을 수 없습니다.



나는 침대에 벌렁 드러누웠다. 낡고 누렇게 찌든 천장을 멍하니 바라보며 생각했다.

‘무슨 일이 벌어지고 있는 거야?’

현재로서는 이해할 수 없는 일들이다. 하지만 한 가지는 확실했다.

‘나는 강해졌다. 비교할 수 없을 정도로.’

전신에 올올이 스며든 힘. 단전에서 꿈틀거리는 공력.

동기화를 거침으로써 내게는 힘이 생겼다. F급 헌터를 아득히 뛰어넘는 힘. 혼자서 C급 레어 몬스터를 쓰러트릴 수 있는 힘이.



‘길드 가입하실래요?’



난생처음 받아 본 스카우트 제의. 하지만 거절했다. 누군가 나를 인정해 준다는 사실에 기쁨보다 두려움이 앞서서.

‘그럴 만도 하지.’

F급 헌터라는 이름으로 7년을 버텼다. 흙바닥만 기어 다니던 애벌레에게 어느 날 시스템이라는 날개가 생긴 것이다.

두려움은 당연한 감정이다.

‘하지만 이 힘을, 시스템을 계속해서 쓸 수 있다면?’

상상만으로도 심장이 쿵쿵 뛰었다.

동시에 지난 7년의 시간이 머릿속을 스쳤다. 미친 듯이 노력했음에도 낙인처럼 찍혀 있던 F급이라는 이름. 타인들의 무시와 죄책감과 무력감에 몸을 떨어야 했던 2년 전의 기억까지.

“시발…….”

더 이상은 못 참겠다. 나는 자리에서 벌떡 일어났다. 곧장 고시원을 뛰쳐나와 지나가던 택시를 붙잡았다.

“어디로 모실까요?”

목적지는 이미 정해져 있었다.

“헌터 협회 부천 지부로 가주세요.”

헌터 등급 재측정.

F급 헌터. 오랫동안 나를 괴롭혀 온 이 지긋지긋한 족쇄를 끊어 내는 것부터 시작이다.

‘어디 한번 해 보자고.’

주먹을 불끈 움켜쥔 내게 택시 기사가 말했다.

“이거 서울 택신데요.”

“아.”
```

### Current accepted English

```markdown
# Chapter 46

Sizzle.

The meat hit the grill. Thick, red, and marbled with white streaks like snowflakes—it was the finest Hanwoo beef.

The shape, the sound, the smell. All of it was intoxicating. The only thing I didn’t like was the price…

“Will this be enough? Let’s order more after we eat. Some special cuts, too.”

A rich C-rank Hunter was paying, so whatever.

*How long had it been since I’d last had Hanwoo?*

Food in Murim was spicy, salty, and bland. And even then, more days than not, I couldn’t eat properly. For thirty days, my stomach had been abused with beef jerky, bigu pills,[^1] and rice balls.

Chomp. Chomp-chomp.

The best thing about beef was how quickly you could eat it. The moment it looked more or less done, it went straight into my mouth.

Every chew felt like walking on clouds. This piece, that piece, that one too—every last one tasted like heaven.

“Hnnngh.”

Team Leader Choi watched me with that peculiar look of his.

“Would you like some more?”

“No. I should hold back on overeating.”

“We’re at twenty-five servings…”

“Twelve servings each isn’t all that much.”

“I’ve only eaten three servings.”

“Oh, can we order some yukhoe?[^2]”

“…Yes.”

“Rice, too.”

“…”

And so that storm of a meal came to an end. At last, Team Leader Choi opened his mouth.

“I said I was the one who killed them. The Priest and the Great Warrior, both.”

“Oh. Thank you.”

“Don’t mention it. Let’s call it a fair deal. If anything, there’s something I should thank you for, too.”

A fair deal.

He wasn’t wrong. I’d bought myself time to think, and he would gain a reputation. After all, he had led five low-rank Hunters and killed two mid-grade Rare Monsters.

The fact that nobody had died in the process would be a huge help for Guild publicity, too.

*What if I hadn’t found my strength through Synchronization?*

Who knew? Someone probably would have died. Maybe nobody would have made it out alive.

“You were already thinking along those lines.”

He wasn’t just some eccentric. Not with instincts that sharp.

I smiled awkwardly.

“It’s good for both of us.”

“Good for both of us. Both of us…”

Team Leader Choi muttered to himself, then asked out of nowhere,

“Would you like to join the Guild?”

“Pffft.”

Team Leader Choi lifted the tablecloth and blocked the water, then smoothly produced a business card with practiced elegance.

> **Peace Guild, Team 1 Leader Choi Minwoo**

What the hell was this? For a second I was completely thrown.

“Y-you’re making me a recruitment offer? Right now?”

“That’s right. We always need talent.”

I took the card, and for some reason I felt deeply moved.

It seemed like only yesterday that I’d been going to interviews with my back bent like a shrimp…

*Live long enough and you really do see everything.*

An actual recruitment offer, treating me like talent. F-rank Hunter Jin Taekyung, you’d come a long way.

“Our Guild is still new, and we don’t have many people, but we’re excellent where it counts. For example…”

Team Leader Choi elegantly swirled his wineglass. When had he even ordered that?

“Our finances are extremely solid.”

“Oh, finances!”

“And because of that, our employee benefits are excellent.”

“Oh, benefits based on solid finances!”

“Our Guild Master is a B-rank Hunter.”

“Oh, a high-ranking Hunter—the source of those solid finances!”

“There’s no need to worry about restructuring.”

“Oh, a stable workplace!”

Team Leader Choi asked with an affluent smile,

“Will you come?”

I scratched my head.

“No. That’s a little…”

“…Pardon?”

“I have some circumstances that make it difficult right now. I need time.”

If I followed my heart, I wanted to sign the contract right away—signature, stamp, thumbprint, even a kiss mark.

*But what if the System vanished tomorrow?*

I’d be dead broke.

Overnight, I’d go from being called talent to being called a human disaster.[^3]

“Is it a money problem?”

There was always a money problem.

But this was more important than that. I couldn’t get dazzled by the wad of cash right in front of me and snatch at it.

“It’s difficult to explain. I’m sorry, but this isn’t something I can decide right now…”

“100 million won.”

“100 million?”

“Just the signing bonus. The rest will match the minimum terms for a C-rank Hunter.”

That was dangerous. This time it was really dangerous.

But I held out with superhuman patience. Hadn’t I already learned that life wasn’t that easy?

It could be money I’d end up choking on.

“I’m sorry.”

Team Leader Choi looked at me quietly, then nodded.

“I’ll wait for your call.”

* * *

One person left, and one person stayed.

Team Leader Choi—no, Choi Minwoo—looked in silence at the seat Jin Taekyung had left, then took out his phone.

Beep. Beep. Click.

“—You bastard, you’re a ghost. I was just about to call you.”

“How did that thing I asked about turn out?”

“—I looked into it because you asked, but… is there something about this Jin Taekyung guy?”

“That’s why I called you. So? What did you find?”

“—It’s a dime-a-dozen case. Seven years ago he Awakened at twenty and was assessed as F-rank. There’s a record he finished first at the Hunter training center…”

Jin Taekyung’s past seven years spilled from the other end of the phone. Then, at one point, Choi Minwoo’s eyebrows twitched.

“What? The Sangdong Station Mutated Gate?”

“—Yeah. You know about that incident, right?”

How could he not? It had happened only two years ago, so Choi Minwoo remembered it clearly.

“—He was the only survivor. I checked that part myself, and it surprised me, too.”

Choi Minwoo tipped his glass of water. Thinking he’d grabbed a lead on how an F-rank Hunter had killed a mid-grade Rare Monster alone made his throat burn.

“And?”

“—He took six months off. The Hunter Administration kept sending investigators, and I guess he spent the time trying to get himself back together. You know how serious the incident was.”

“And then?”

“—That’s it. He went back to his Guild, ran Gates his ass off for a year and a half, then got fired. That was exactly three days ago.”

“Why was he fired?”

“—It was technically restructuring, but a booger-sized little Guild, restructuring? Please. The incident probably had a lot to do with it. They kept glancing nervously at the Administration, then pushed him out. From their perspective, he’d have been awkward to keep around.”

“That’s all?”

“—As far as I can tell. Want me to send you the file separately?”

“Send it now. I’m hanging up.”

“—Hey, hey!”

Click.

Choi Minwoo tapped the table with his long fingers.

Jin Taekyung. F-rank Hunter. The sole survivor of the Sangdong Station Mutated Gate.

And…

*At least a C-rank Hunter.*

That was the absolute minimum. The image of Taekyung driving a C-rank Rare Monster into a corner alone, with overwhelming strength and skill, kept flickering before his eyes.

*And yet he’s F-rank.*

There were only two possibilities. He had been hiding his strength, or he had recently reawakened.

Choi Minwoo suspected the latter, but that was still far beyond common sense.

It wasn’t as if only one or two Hunters retired without ever ranking up even once.

Reawakening from F-rank to C-rank was, without question, extraordinarily rare.

*This isn’t some kind of game. What the hell is he?*

Choi Minwoo shook his head. He felt as if a ghost had possessed him.

*I’ll have to look into this further.*

As he rose from his seat, the restaurant owner approached and held out the bill.

“1,937,000 won.”

“…”

He really did feel as if a ghost had possessed him.

* * *

“Shit. I’m fucked.”

I dropped heavily onto the ground. The recycling area was a mess. The thing that should have been there was nowhere to be seen.

“It’s gone. It’s gone. My capsule is gone.”

I’d been anxious ever since leaving Team Leader Choi. But I hadn’t expected someone to take it in less than half a day. I shouted into the empty air.

“Who the fuck was it?!”

And I got an answer.

“Me, you son of a bitch.”

On the roof of the goshiwon building,[^4] Jinho hyung was smoking in the same spot where I’d seen him that morning. He exhaled a plume of smoke with a wistful look, then went on.

“I spent ten years crying, regretting it, and making vows…”

“You want me to make you really cry and regret it?”

“You’re no fun. You haven’t seen this movie, have you?”

“Quit joking around. This is serious.”

“What, you come up empty today?”

“No.”

My voice drained of strength as I went on.

“The capsule.”

“…Huh?”

“Some bastard took my capsule.”

“Cough, cough-cough!”

Maybe he’d inhaled the cigarette smoke wrong. Jinho hyung coughed like a maniac before he finally managed to speak.

“D-didn’t you throw it away because you didn’t need it?”

“I did.”

Until the System came back.

I hadn’t expected the situation to change this much in just a few hours.

*I should’ve kept it for one more day.*

Where was I even supposed to start looking? I sighed heavily.

“Hyung, you didn’t happen to see who took it, did you?”

“Uh… well.”

Jinho hyung scratched his head.

“If I saw it, then I saw it. If I didn’t, then I didn’t.”

Was that even an answer, or just crap?

When I glared at him, he smiled sheepishly.

“Look, it’s not that I want a finder’s fee or anything…”

It definitely sounded like he wanted a finder’s fee.

Anyway, that wasn’t the point. I shot to my feet and asked,

“You saw them? You’re sure?”

“If I have to pick, I saw them.”

“Who? Where did they go?”

“I’m not asking for a finder’s fee, but what’s the expected amount, roughly?”

“…100,000 won?”

“Oh, dear. Maybe I’m getting old. My memory’s a little hazy.”

“For fuck’s sake.”

“Right. It’s hot out, so good luck with that.”

“The finder’s fee is 180,000 won.”[^5]

Apparently satisfied with the amount, Jinho hyung broke into a bright smile.

“Your capsule. I picked it up.”

“…?”

It took me exactly three seconds to understand.

*Have you ever seen a daylight robber like this?*

I was so dumbfounded I couldn’t even breathe. He’d hit me in the back of the head like this?

“But there wasn’t anywhere suitable to put it. My room’s too small, you know.”

“So?”

“I put it back in your room. I did good, right?”

How was I supposed to hit this guy so cleanly that people would say I’d really done it right?

I clenched my fists until they shook.

* * *

“It really is here.”

Seeing the capsule taking up half the studio as if nothing had happened, all I could do was let out a hollow laugh.

*Should I call this lucky?*

Of all the people in the world, Jinho hyung had taken the capsule.

I opened the capsule lid. Then I picked up the user manual, which had been tossed onto the worn seat, and flipped to the last page.

> **Main Features**
>
> - A customized capsule for one person! Once a user is registered, the capsule becomes permanently bound to that user and remains so until their death.

…Come on. No way.

*It has to be a simple coincidence.*

But I couldn’t shake the unease. I stared at the capsule, the source of all these events.

*What even is this thing?*

The reason I’d thrown the capsule into the recycling area that morning was so I could forget everything. My life was already dry enough; I wanted to write it off as one nightmare and keep living my life as I was.

But the situation had changed now.

*Because the System is here.*

The System…

Then something occurred to me. I placed my hand on the surface of the capsule and murmured,

“Item check.”

Ding.

Just as I thought. The corners of my mouth had just begun to rise when—

> **System**
>
> This Item cannot be read.

“…It can’t be read?”

This had never happened before.

*Is it because I’m not in Murim?*

Flustered, I checked every object in the room at random. The television, a ballpoint pen, even the pillow. Every time, the System displayed accurate information.

But there was one exception.

The capsule couldn’t be read.

“Wow. This is driving me nuts.”

Just in case, I picked up the user manual. Same result.

Ding.

> **System**
>
> This Item cannot be read.

I flopped onto the bed. I stared blankly at the old, yellow-stained ceiling and thought.

*What’s going on?*

For now, these were things I couldn’t understand. But one thing was certain.

*I’ve become stronger. Incomparably stronger.*

Power had soaked into every fiber of my body. Internal energy writhed in my dantian.

Synchronization had given me strength. Strength far beyond that of an F-rank Hunter. Strength enough to defeat a C-rank Rare Monster alone.

*Would you like to join the Guild?*

It was the first recruitment offer I’d ever received. But I refused. When someone recognized me, fear had come before joy.

*Can’t blame me.*

I’d endured seven years under the name of F-rank Hunter. A caterpillar that had only ever crawled through the dirt had, one day, grown wings called the System.

Fear was a natural feeling.

*But what if I can keep using this power—keep using the System?*

My heart pounded at the mere thought.

At the same time, the past seven years flashed through my mind. The name F-rank, stamped on me like a brand despite all the insane effort I’d put in. Even the memories from two years ago, when I’d trembled at other people’s contempt, at the guilt and the helplessness.

“Fuck…”

I couldn’t take it anymore. I shot to my feet, burst out of the goshiwon, and flagged down a passing taxi.

“Where would you like to go?”

I already knew the destination.

“Take me to the Bucheon Branch of the Hunter Association.”

A Hunter rank reassessment.

An F-rank Hunter. I’d start by breaking this loathsome shackle that had tormented me for so long.

*Let’s give it a shot.*

As I clenched my fist, the taxi driver said,

“This is a Seoul taxi.”

“Oh.”

[^1]: Bigu pills are traditional fasting pills said to sustain the body without ordinary food.

[^2]: Yukhoe is seasoned Korean raw beef.

[^3]: The Korean words for “talent” and “human disaster” share the same pronunciation, though they use different characters.

[^4]: A goshiwon is a very small, inexpensive room-for-rent housing arrangement.

[^5]: In Korean, *sip-pal* (“eighteen”) echoes the swear he just used, and he switches abruptly to stiff politeness.
```
## Chapter 47

### Korean source

```text
＃47화



헌터 협회.

삼십여 년 전, 대격변의 종전과 동시에 등장한 이름이다.

피로 얼룩진 대격변에서 살아남은 1세대 헌터들이 깃발을 세웠고, 헌터 협회는 세월의 흐름에 따라 엄청난 위상을 지닌 단체로 발돋움했다.

꿀꺽.

나는 침을 삼키며 우뚝 선 협회 건물을 바라봤다. 이 빽빽한 빌딩 숲에서도 눈에 띄는 크기와 높이. 특별한 것 없는 평일에도 수많은 사람이 그곳을 드나들고 있었다.

‘이게 몇 년 만이지?’

모든 각성자는 협회의 감독하에 등급 측정을 실시한다.

나도 마찬가지였다. 설레는 마음으로 이곳을 찾았던 스무 살의 진태경을 생각하니 피식 웃음이 나오……긴 개뿔.

‘막상 오니까 엄청 긴장되네.’

경직된 걸음으로 로비로 들어섰다. 운동장만 한 로비는 인파로 득실거렸다. 곳곳에 설치된 전광판을 따라 걸음을 옮기니 원하는 곳을 찾을 수 있었다.



[측정 대기실]



창구 직원의 안내에 따라 서류를 작성하고 들어갔다. 대기실에는 수십 명의 인원이 측정을 기다리고 있었다.

쿵. 문 닫히는 소리에 시선들이 화살처럼 날아와 꽂힌다.

‘숨 막힌다, 숨 막혀.’

이곳은 공기부터 다르다. 팽팽한 긴장감이 대기실 전체를 짓누르고 있었다.

‘측정 한 번에 헌터 인생이 결정 나는 거니까.’

나도 마찬가지였다. 너무 긴장한 탓에 감독관 앞에서 방귀를 뀐 적도 있으니 말 다 했지, 뭐.

이런저런 생각을 하며 순서를 기다리고 있을 때였다.

“진태경?”

등 뒤로 들려오는 익숙한 목소리. 천천히 고개를 돌리자 그곳에 그가 있었다.

“설마 했는데, 맞네.”

주먹코에 배불뚝이의 중년인. 잊으려야 잊을 수 없는 얼굴이었다.

‘……김 팀장?’

김상식. 내가 수년간 몸담았던 소풍 길드의 창립 멤버이자 팀장인 그는 한 단어로 설명할 수 있다.

전(前) 직장 상사.

“이야, 이런 데서 볼 줄은 몰랐네. 반가워.”

김 팀장이 너털웃음과 함께 손을 불쑥 내민다. 나는 잠깐 망설이다가 그의 손을 맞잡았다.

“그러게요. 오랜만이네요.”

“오랜만은 무슨. 며칠이나 됐다고.”

“그 며칠이, 저는 꽤 길게 느껴지더라고요.”

무림을 떠올리며 한 말이었지만 김 팀장에게는 다른 의미로 들릴 것이다. 그도 그럴 것이, 불과 며칠 전 내게 해고 통보를 한 장본인이니까.

“여름이라 그래. 나도 요즘 하루가 길어.”

“그래요?”

능구렁이처럼 넘어가는 그를 보자 실소가 흘러나왔다.

언제 봐도 재미있는 양반이다. 여러 가지 의미로.

“그런데 여긴 어쩐 일이야?”

“볼일이 좀 있어서요. 팀장님은요?”

“스카우트차 왔지. 이번에 괜찮은 놈이 있다는 얘길 들어서.”

해고 사유는 구조 조정으로 인한 인원 감축인데 스카우트라.

“그렇군요.”

내가 할 말은 그것밖에 없었다. 다들 아는 뻔한 스토리. 그것도 완결 난 이야기에 더 이상 미련은 없다.

“그러는 너는 왜 왔어? 설마 재측정이라도 해 보려고?”

“네.”

김 팀장이 웃는 얼굴로 말했다.

“거, 시도는 좋지만 너무 돈 낭비 아냐? 재측정 비용이 한두 푼도 아니고. F급 헌터 처지에 부담될 텐데.”

“그래도 해 보는 거죠. 혹시나 하는 마음에.”

“젊을 때 모아 놔야지. 안 되는 거 계속 붙잡고 있으면 뭐가 달라지나.”

“글쎄요. 이번엔 좀 다를 것 같아서요.”

“그게 그렇게 쉬운 일이 아닌…….”

“팀장님.”

“어, 왜?”

나는 부드럽게 웃었다.

“적당히 하시죠.”

순간 김 팀장의 웃음에 실금이 갔다.

“뭐?”

“적당히 하시라고요. 이제 길드도 나갔으니 저한테 신경 끄시고.”

“무슨 뜻이야?”

무슨 뜻이긴.

“아시잖아요. 제가 무슨 말을 하는 건지.”

“…….”

“어쩔 수 없었다. 너라도 살아서 다행이다. 다 잊고 새 시작 하자. 위로하는 척하면서 뒤에서 열심히 쪼아 대셨던데요.”

“너…….”

“길드장님한테 저 자르자고 처음 얘기 꺼낸 것도 팀장님 아닙니까. 제가 모를 줄 아셨어요?”

김 팀장은 한마디로 어중간한 소인배다.

인간성도, 능력도 부족한 인간.

게이트에서도 제 목숨 챙기기에 급급해 길드 내의 평가는 바닥을 기었다.

“저 자르고 그 자리에 누구 넣었습니까? 얼마 받고 꽂아 주기로 했어요?”

“야, 진태경이.”

김 팀장이 내 어깨를 짓누르며 으르렁거렸다. 저래 봬도 소풍 길드에서 셋밖에 없다는 D급 헌터다. 이 정도 힘이면 F급 헌터 따위는 한 손으로도 갖고 놀 수 있다.

하지만…….

“손 떼.”

나는 눈 하나 깜짝하지 않았다. 동기화된 것은 시스템뿐만이 아니다. 무공과 능력치. 그리고 강철 같은 근골까지 포함이다.

“셋 센다. 손 떼.”

“이 새끼가 보자 보자 하니까…….”

나는 망설이지 않고 입을 열었다.

“하나, 둘.”

셋. 동시에 김 팀장의 손목을 움켜쥔 그 순간이었다.

덜컹.

“다음 분들 들어오세요. 21번부터 30번!”

서류철을 든 협회 감독관의 등장에 우리는 누가 먼저랄 것도 없이 떨어졌다. 협회에 찍혀 봤자 서로에게 좋을 게 없다.

“운 좋은 줄 알아라.”

“누구. 내가? 아니면 당신?”

벌겋게 달아오른 김 팀장의 얼굴이 퍽 우습다. 기감으로 파악한 그의 레벨창까지도.



[Lv.24 김상식]



“만나서 기분 더러웠고, 다신 보지 맙시다.”

미련 없이 자리를 털고 일어났다. 내가 받은 대기 번호는 30번. 감독관을 향해 걸어가는 발걸음은 더 이상 경직되어 있지 않았다.



* * *



“21번. 앞으로 나와 주세요.”

긴장된 얼굴의 각성자가 측정기 앞에 섰다. A급 마정석을 재료로 만든 등급 측정기는 그의 전신을 스캔, 체내의 마나를 수치로 환산한다.

지이잉-

수치를 확인한 감독관이 입을 열었다.

“체내 마나 분포량, F급.”

각성자의 얼굴이 흙빛으로 변했다. 하지만 절망하기에는 이르다. 두 번째 기회가 있으니까.

“마나를 움직여 보세요. 최대한 집중해서 측정기로 쏘아 보낸다는 느낌으로.”

마나 컨트롤을 보는 거다. 아직 끝나지 않았다는 사실을 깨달은 각성자가 이를 악물고 힘을 끌어 올렸다.

젖 먹던 힘까지 빡!

뿌우웅.

“…….”

“…….”

감독관이 토할 것 같은 얼굴로 말했다.

“제어 능력, F급.”

“한 번만! 다시 한번만 해 볼게요!”

“안 됩니다. 다음.”

순서가 휙휙 넘어간다.

죄다 E급, F급에 심지어는 비각성자인 놈까지 나왔다.

“이거 사기야, 사기! 저 측정기 중국산이지! 어? 이 새끼들아!”

“처리하세요.”

감독관의 말에 대기하고 있던 경비 헌터들이 사기꾼을 질질 끌고 나갔다. 아마 저놈은 기적적으로 각성한다고 해도 협회 블랙리스트에 등록될 거다.

“다음, 30번.”

올 게 왔구나.

나는 크게 숨을 들이켜고 앞으로 나섰다. 감독관이 손에 든 서류철을 흘끗 보더니 말했다.

“재측정이시네요?”

“네.”

“진태경 씨, 7년 전 F급 취득하셨고…… 재측정은 따로 비용 청구되는 건 아시죠?”

대충 들어 보니 괜히 헛돈 쓰지 말고 기회 줄 때 집에나 가란 소리다. F급 헌터를 보는 흔한 시선들.

‘누굴 거지로 아나.’

익숙한 것과 기분이 더러운 건 별개다. 내가 노려보자 감독관이 피식 웃었다.

“혹시 싶어 말씀드리는 건데 비용은 2백만 원입니다.”

“……가격 올랐어요?”

“몇 년 됐죠.”

시벌, 그걸 몰랐네.

지금 내 통장 잔고가 얼마더라…….

“그럼 측정 시작하겠습니다.”

나는 떨리는 마음으로 눈을 감았다. 그리고 다음 순간.

지이잉.

측정기에서 흘러나온 마력의 파동이 전신을 훑고 지나갔다.

15년의 공력이 그에 감응해 부르르 떨었다.

‘몇 급일까?’

C급? 아니, D급만 되어도 좋다. 하지만 십여 초를 기다려도 감독관의 입은 열리지 않았다.

“어어, 이게 왜 이러지?”

“왜요?”

당황한 얼굴로 측정기와 나를 번갈아 보던 그가 헛기침했다.

“오류가 좀 생긴 것 같은데…… 일단 다음 순서로 넘어가겠습니다.”

뭐가 어떻게 돌아가는 건지는 모르겠지만 어쩐지 불길하게 느껴지진 않는다.

‘느낌이 좋아.’

나는 두근거리는 심장 박동을 느끼며 공력을 끌어 올렸다.

스아아.

진가심법의 부름에 따라 솟구친 15년의 공력이 측정기를 향해 쏘아졌다.



* * *



로비 입구.

“잘했다.”

김상식은 청년의 어깨를 두드렸다. 오늘부로 D급 각성자로 공인받은 전도유망한 젊은이다.

그는 곧 소풍 길드에 가입, 김상식의 팀에 배정될 것이다. 곧 다가올 그 날을 떠올린 김상식은 뿌듯하게 웃었다.

“부자(父子)가 한 팀을 이루겠구나. 역시 내 아들이야.”

“뭘요, 아직 정식 헌터가 된 것도 아닌데. 훈련소도 들어가야 하고.”

“걱정하지 마라. 이 아버지가 미리 손써 뒀으니까.”

“어, 진짜요? 길드에 자리 없다고 하지 않았나?”

“다 방법이 있지.”

그 과정에서 눈엣가시 같던 최하급 헌터를 잘랐다는 사실은 말하지 않았다.

“어쨌든 이번 주는 푹 쉬고, 다음 주부터 같이 출근…….”

문득 김상식의 표정이 일그러졌다.

“왜 그래요?”

“……아니다. 먼저 차에 가 있어.”

아들이 떠난 후 홀로 남은 그는 셔츠 소매를 걷어 올렸다.

어느새 검푸른색으로 부어오른 손목을 확인하자 이가 갈린다.

“진태경, 이 개새끼가.”

그 자식은 처음부터 마음에 안 들었다. F급 헌터인 주제에 부팀장인 것도, 지금은 죽고 없는 전 팀장과 형제처럼 지내던 모습도 그랬다.

‘저 새끼도 그때 같이 뒈졌어야 했는데.’

2년 전 벌어진 불의의 사고는 김상식에게 있어 천운이었다.

각종 성추문으로 일선에서 물러나 있던 그는 팀장으로 금의환향했고, 며칠 전 진태경까지 내보낼 수 있었으니까.

‘그런데 이놈, 정말 재각성인가?’

김상식은 욱신거리는 손목을 내려다봤다.

그야말로 찰나의 순간이었지만 그때 느낀 힘은 어마어마했다. E급, 어쩌면 D급으로 재각성 했을지도 모를 일이다.

“아니지, 재각성이 무슨 애들 장난도 아니고.”

요즘 운동을 안 해서 약해진 건가. 김상식이 복잡한 심정으로 중얼거리던 순간이었다.

“측정실에서 속보 왔습니다.”

“괜찮은 놈 있대?”

“월척 하나 떴답니다. C급.”

“C급? 나쁘진 않은데 월척 소리 들을 정도는 아니잖아?”

“그런데 마나 컨트롤이 A급이랍니다.”

“뭐? A급! 빨대 꽂아, 빨리!”

“예. 상동 길드 최민숩니다. 다름이 아니고…….”

로비 입구를 하이에나처럼 어슬렁거리던 스카우터들 사이로 술렁임이 번졌다.

대부분이 중소 길드에서 파견된 이들이었지만 대형 길드에서 나온 몇몇은 이미 발 빠르게 움직이고 있다.

‘C급만 해도 상당한데, 마나 컨트롤까지 타고났어?’

이건 대박이다.

김상식은 정신이 번쩍 들었다. 진태경에 관한 생각은 저 멀리 내팽개치고 핸드폰을 꺼내 들었다.

- 어, 김 팀장. 갔던 일은 잘됐고?

수화기 너머 굵은 목소리의 주인은 소풍 길드장이었다.

김상식이 다급하게 말했다.

“길드장님. 지금 여기 난리 났습니다. C급 떴어요. 거기에 마나 컨트롤은 상위 헌터 수준이랍니다.”

- 뭐? 그런 놈이 어디서 튀어나와?

“그러니까요. 대형 길드 놈들, 매번 중간에 가로채더니 이번에는 한발 늦은 모양입니다.”

- 좋아, 그렇단 말이지…….

후욱. 훅.

흥분했는지 거친 숨소리가 흘러나왔다. 김상식을 부르는 호칭도 바뀌었다.

- 상식아. 너 이거 꼭 붙잡아라. 무조건 원하는 조건에 맞춘다고 해.

“금액 어디까지 됩니까?”

- 신경 쓰지 말고 다른 놈들 부르는 금액에 듬뿍 얹어 줘. 대형 길드 놈들이야 수지 좀 안 맞는다 싶으면 떨어질 거야. 그것들은 아쉬울 것도 없잖아?

“예, 예.”

- 나 지금 간다. 꼭 붙잡고 있어. 이거 성공시키면…… 알지?

전화를 끊은 김상식은 주먹을 불끈 움켜쥐었다.

‘됐다!’

이 바닥에서 닳고 닳은 그다. 이제 막 각성한 신출내기 각성자 정도쯤이야 붙잡아 두는 건 일도 아니다.

돈이면 귀신도 부리는 세상 아닌가.

‘다른 놈들보다 무조건 두 배. 두 배 부른다.’

그때 웅성거림이 더 커졌다. 측정실이 있는 3층에서 멈춘 엘리베이터가 로비를 향해 내려오고 있었다.

“온다!”

“아 거, 밀치지 좀 맙시다.”

스카우터 이십여 명이 개미 떼처럼 입구에 달라붙었다. 우악스럽게 선두 자리를 차지한 김상식이 명함을 건넬 만반의 준비를 마쳤다.

띵.

그리고 마침내 열리는 엘리베이터 문.

김상식은 넙죽 고개를 숙이며 준비해 둔 말을 꺼냈다.

“안녕하십니까. 소풍 길드의 김상식 팀장입니다. 저희는 전통 있는 부천의 명문 길드로서…….”

“소풍 길드가 명문이라는 소리는 또 처음 들어 보네.”

“……네?”

익숙한 목소리. 김상식의 고개가 슬그머니 들렸다.

그리고 두 사람의 시선이 부딪쳤다. 단춧구멍 같던 김상식의 눈이 부릅떠진 것도 동시였다.

“너, 너…….”

진태경이 씩 웃었다.

“또 만났네요. 김상식 씨.”
```

### Current accepted English

```markdown
# Chapter 47

Hunter Association.

The name had appeared some thirty years ago, at the same time the Great Cataclysm ended.

The first-generation Hunters who survived that blood-soaked catastrophe raised their flag, and over the years the Hunter Association grew into an organization of tremendous stature.

Gulp.

I swallowed as I stared up at the Association building standing tall before me. Even in this dense forest of skyscrapers, its size and height stood out. Even on an ordinary weekday, people streamed in and out.

*How many years has it been?*

Every Awakened underwent rank measurement under the Association’s supervision.

I was no different. The thought of twenty-year-old Jin Taekyung walking in here all excited almost made me snort—like hell it did.

*Now that I’m actually here, I’m incredibly nervous.*

I went into the lobby on stiff legs. The place was the size of a sports field and packed with people. I followed the electronic signs posted throughout until I found what I wanted.

**Measurement Waiting Room**

On the clerk’s instructions, I filled out the paperwork and went inside. Dozens of people were waiting to be measured.

Thud.

The door shut, and everyone’s eyes shot into me like arrows.

*Suffocating. This is suffocating.*

Even the air was different here. A taut tension pressed down on the entire waiting room.

*One measurement decides your whole Hunter life.*

I was no different. I’d been so nervous I’d even farted in front of an examiner once. That pretty much said it all.

I was waiting my turn, thinking about this and that, when—

“Jin Taekyung?”

A familiar voice from behind me. I turned my head slowly.

There he was.

“I didn’t think it would be, but it is.”

A middle-aged man with a bulbous nose and a potbelly. A face I couldn’t forget no matter how hard I tried.

*…Team Leader Kim?*

Kim Sangshik. A founding member and team leader of Sopung Guild, where I’d spent years. He could be summed up in one word.

Former boss.

“Wow, I never expected to run into you somewhere like this. Good to see you.”

Team Leader Kim thrust out his hand with a hearty laugh. I hesitated a moment, then took it.

“Likewise. It’s been a while.”

“What do you mean, a while? It’s only been a few days.”

“Those few days felt pretty long to me.”

I’d said it thinking of Murim, but Team Leader Kim would hear something else. After all, he was the one who’d handed me my dismissal only a few days ago.

“It’s because it’s summer. My days have felt long lately too.”

“Really?”

Watching him slide past it like a sly old fox, I let out a hollow laugh.

He was a funny guy, no matter when you saw him.

In more ways than one.

“So what brings you here?”

“I had some business. What about you, Team Leader?”

“Came to scout. Heard there was a decent one this time.”

They’d fired me for staff cuts in a restructuring. And he was here to scout.

“I see.”

That was all I had to say. Everyone knew that tired story, and it was already over. I had no lingering attachment left.

“What about you? Why are you here? Don’t tell me you’re trying to get reassessed.”

“Yes.”

Team Leader Kim spoke with a smile.

“Nice try, but isn’t that a waste of money? A reassessment isn’t cheap. Must be a burden for an F-rank Hunter.”

“Still, I figured I’d try. Just in case.”

“You should save up while you’re young. What’s going to change if you keep clinging to something that isn’t going to work?”

“Who knows? I think this time might be different.”

“It’s not that easy—”

“Team Leader.”

“Huh? What?”

I smiled, gentle.

“That’s enough.”

A crack ran through Team Leader Kim’s smile.

“What?”

“I said that’s enough. I’ve left the Guild now, so stay out of my business.”

“What’s that supposed to mean?”

What did it mean?

“You know what I mean.”

“…”

“It couldn’t be helped. You’re lucky you survived. Forget it all and make a fresh start. You pecked away at me behind my back while pretending to console me.”

“You…”

“Weren’t you the one who first told the Guild Master to cut me? Did you think I wouldn’t know?”

Kim Sangshik was a half-baked, petty little man.

Short on humanity, short on ability.

Even in Gates, he was too busy saving his own skin. His reputation in the Guild was rock-bottom.

“Who did you put in my place after you fired me? How much did you take to slot someone in?”

“Hey. Jin Taekyung.”

Team Leader Kim clamped down on my shoulder and growled. He didn’t look it, but he was one of only three D-rank Hunters in Sopung Guild. With that kind of strength, he could have toyed with an F-rank Hunter like me with one hand.

But—

“Take your hand off.”

I didn’t even blink. It wasn’t only the System that had synchronized. My martial arts, my stats, and even my steel-like Sinews and Bones had come with it.

“I’ll count to three. Take your hand off.”

“You little bastard. I’ve been putting up with you, but—”

I didn’t hesitate.

“One. Two.”

Three.

The instant I grabbed Kim Sangshik’s wrist—

Clack.

“Would the next group please come in. Numbers twenty-one through thirty!”

An Association examiner walked in with a file, and we both let go before the other could. Getting marked by the Association wouldn’t do either of us any good.

“Consider yourself lucky.”

“Who. Me? Or you?”

Kim Sangshik’s flushed face looked downright ridiculous. Even the Level Window I’d picked up through Qi Sense.

> **System**
> Lv. 24 Kim Sangshik

“Meeting you was disgusting. Let’s never see each other again.”

I got up without a shred of regret. My waiting number was thirty. The steps I took toward the examiner weren’t stiff anymore.

* * *

“Number twenty-one. Please come forward.”

An Awakened with a tense face stood in front of the measuring device. Made from an A-rank Magic Gem, it scanned his whole body and converted the mana inside him into numbers.

Bzzzzzt—

The examiner checked the reading and spoke.

“Mana distribution in the body: F-rank.”

The Awakened’s face turned ashen. But it was too soon to despair. He had a second chance.

“Try moving your mana. Concentrate as hard as you can, and imagine firing it into the measuring device.”

They were checking his mana control. Realizing it wasn’t over yet, the Awakened gritted his teeth and drew up his strength.

Every last ounce of it—ngh!

Bwoooom.

“…”

“…”

The examiner spoke with a face that looked ready to vomit.

“Control ability: F-rank.”

“Just once! Let me try one more time!”

“No. Next.”

The line moved fast.

All E-rank or F-rank. One guy wasn’t even Awakened.

“This is a scam! A scam! That measuring device is made in China, isn’t it? Huh? You bastards!”

“Handle him.”

At the examiner’s word, the security Hunters waiting nearby dragged the fraud out. Even if that guy miraculously Awakened, he’d probably end up on the Association’s blacklist.

“Next. Number thirty.”

Here it came.

I took a deep breath and stepped forward. The examiner glanced at the file in his hand.

“This is a reassessment?”

“Yes.”

“Mr. Jin Taekyung, you received F-rank seven years ago… and you know there’s a separate fee for reassessments, right?”

From the way he said it, he might as well have been telling me not to waste my money and to go home while I still could. The usual look people gave an F-rank Hunter.

*Do they think I’m a beggar?*

Familiar was one thing. Still filthy was another. When I glared at him, the examiner gave a short puff of a laugh.

“I’m only mentioning it in case you weren’t aware, but the fee is two million won.”

“…The price went up?”

“It’s been a few years.”

*Fuck. I didn’t know that.*

How much was in my account right now…?

“Then we’ll begin the assessment.”

Nervous, I closed my eyes.

And the next moment—

Bzzzzzt.

A wave of mana rolled out of the measuring device and swept through my whole body.

Fifteen years of internal energy answered it and shuddered.

*What rank will it be?*

C-rank? No, I’d be happy with D-rank. But ten seconds or so passed, and the examiner still didn’t open his mouth.

“Uh… why is it doing this?”

“Why?”

He looked from the device to me, flustered, then cleared his throat.

“There seems to be some kind of error… We’ll move on to the next step for now.”

I had no idea what was going on, but strangely, it didn’t feel ominous.

*This feels good.*

Feeling my heart pound, I drew up my internal energy.

Ssshhh.

At the call of the Jin Family’s Cultivation Technique, fifteen years of internal energy surged up and shot toward the measuring device.

* * *

The lobby entrance.

“Well done.”

Kim Sangshik patted a young man on the shoulder. As of today, he was a promising young D-rank Awakened, officially recognized.

He would soon join Sopung Guild and be assigned to Kim Sangshik’s team. Thinking of that coming day, Kim Sangshik smiled, proud.

“Father and son on the same team. That’s my boy.”

“What are you talking about? I’m not even an official Hunter yet. I still have to go through the training center.”

“Don’t worry. Your father already took care of it.”

“Wait, really? Didn’t you say the Guild didn’t have a spot?”

“There’s always a way.”

He didn’t mention that, in the process, he’d cut the lowest-rank Hunter who’d been a thorn in his eye.

“Anyway, rest up this week, and starting next week we’ll commute together—”

Kim Sangshik’s face suddenly twisted.

“What’s wrong?”

“…Nothing. Go wait in the car.”

After his son left, he was alone. He rolled up his shirtsleeve.

His wrist had already swollen a dark blue-green. The sight made him grind his teeth.

“Jin Taekyung, you fucking bastard.”

He’d disliked that bastard from the start. An F-rank Hunter as deputy team leader, and the way he’d been like brothers with the old team leader, who was dead now.

*That bastard should’ve fucking died with him back then.*

The unfortunate accident two years ago had been a stroke of luck for Kim Sangshik.

After being sidelined by various sex scandals, he’d made a triumphant return as team leader. A few days ago, he’d even gotten Jin Taekyung thrown out.

*But was this bastard really a reawakening?*

Kim Sangshik stared down at his throbbing wrist.

It had only lasted an instant, but the strength he’d felt then had been tremendous. Taekyung might have reawakened as E-rank—or even D-rank.

“No. Reawakening isn’t child’s play.”

Maybe he’d gotten weaker from not exercising lately. Kim Sangshik was muttering, mixed up inside, when—

“We have breaking news from the measurement room.”

“Someone good?”

“They say a big fish surfaced. C-rank.”

“C-rank? Not bad, but that’s not enough to call a big fish, is it?”

“But they say his mana control is A-rank.”

“What? A-rank! Get a straw in him, now!”

“Yes. This is Choi Min-su from Sangdong Guild. The thing is—”

A stir spread through the scouts prowling the lobby entrance like hyenas.

Most of them had been sent by small and midsized Guilds, but a few from the major ones were already moving fast.

*C-rank alone is impressive, and he’s gifted with mana control on top of it?*

This was a jackpot.

Kim Sangshik’s mind snapped clear. He shoved every thought of Jin Taekyung far away and pulled out his phone.

—Hey, Team Leader Kim. Did that business go well?

The deep voice on the other end belonged to Sopung Guild’s Guild Master.

Kim Sangshik spoke in a rush.

“Guild Master, it’s chaos here. A C-rank just showed up. And they say his mana control is at the level of a high-ranking Hunter.”

—What? Where did a guy like that come from?

“Exactly. The major Guilds always snatch them up midway, but it looks like they were a step late this time.”

—Good. So that’s how it is…

Huff. Huff.

Rough breaths came through the phone, as if he was excited. Even the way he addressed Kim Sangshik changed.

—Sangshik. You hold on to this guy no matter what. Tell him we’ll meet whatever conditions he wants.

“How high can we go on the money?”

—Don’t worry about it. Pile plenty on top of whatever the others offer. The major Guilds will drop out if they decide it isn’t profitable enough. It’s not like they need him.

“Yes, yes.”

—I’m on my way. Keep hold of him until I get there. If we pull this off… you know what that means, right?

After hanging up, Kim Sangshik clenched his fist.

*We’ve got this!*

He’d been worn smooth by years in this business. Holding on to a newly Awakened rookie was nothing.

This was a world where money could put even ghosts to work.

*Twice what everyone else offers. I’ll quote double, no matter what.*

The commotion grew louder. The elevator that had stopped on the third floor, where the measurement room was, was coming down toward the lobby.

“He’s coming!”

“Hey, stop shoving.”

About twenty scouts clung to the entrance like a swarm of ants. Kim Sangshik had muscled his way into the lead and was ready to hand over his card.

Ding.

At last, the elevator doors opened.

Kim Sangshik bowed low and launched into the words he’d prepared.

“Hello. I’m Team Leader Kim Sangshik of Sopung Guild. We’re a prestigious Guild with a long tradition here in Bucheon—”

“This is the first time I’ve heard anyone call Sopung a prestigious Guild.”

“…What?”

The familiar voice made Kim Sangshik lift his head, gingerly.

Their eyes met.

At the same time, Kim Sangshik’s buttonhole-sized eyes went wide.

“You, you…”

Jin Taekyung grinned.

“We meet again, Mr. Kim Sangshik.”
```
## Chapter 48

### Korean source

```text
＃48화



“네, 네가 왜 거기 있어?”

“그러게요. 내가 왜 여기 있을까.”

“그럼 혹시……?”

“혹시는 무슨. 역시지.”

김상식의 안색이 똥독 오른 사람처럼 거무죽죽하게 변했다.

그 모습을 보니 10년 묵은 숙변이 내려가는 기분이다. 아아, 이것이 바로 똥르가즘.

“그건 그렇고, 뒤로 좀 갑시다. 여기 혼자만 있는 거 아니잖아요?”

내가 한 걸음 내딛자 김상식이 힘없이 뒷걸음질 친다.

다른 스카우터들이 명함을 들고 나를 둘러쌌다.

“상동 길드입니다. 최고 대우를 약속드립니다.”

“이럴 게 아니라 따로 자리를 옮겨서 말씀을…….”

사방에서 스카우트 제의가 빗발친다. 잠깐 사이에 내 손에는 수십 장의 명함이 들려 있었다.

‘이런 기분이었구나.’

신기하면서도 묘한 기분이다. 7년 동안 단 한 번도 경험하지 못한 일들이 눈앞에서 펼쳐지고 있다.

고작 반나절 만에 나를 둘러싼 세상이 변했다.

아니.

‘내가 변한 거겠지.’

이 바닥에서는 C급 헌터부터가 진짜라는 말이 있다. 뛰어난 능력에 고액 연봉, 사회가 인정하는 중급 헌터.

비로소 그 길에 들어섰다는 사실이 실감 났다.

‘그리고…….’

이건 시작에 불과하다.

시스템의 힘이라면 나는 계속해서 성장해 나갈 수 있다.

그렇게, 어떤 헌터보다 빠르게 새로운 길로 접어들 것이다.

“각성자님, 원하는 조건이 있으시면 무조건 맞춰 드리겠습니다.”

“아, 네. 나중에 연락드릴게요.”

“정말이죠? 기다리겠습니다!”

아냐. 기다리지 마. 연락 안 할 거니까.

“자자, 이제 다들 진정하세요.”

끈질기게 달라붙는 스카우터들을 협회 경비원들이 막아섰다.

사실 C급 헌터를 상대로 저렇게까지 하는 경우는 없는데, 내가 워낙 흔치 않은 케이스라 이목이 많이 쏠리는 모양이었다.

‘하긴, 재각성 한 번으로 껑충 뛰었으니.’

이런 기분도 나쁘진 않다. 아니, 오히려 좋다.

나는 자꾸만 올라가는 입꼬리를 억누르며 협회를 빠져나왔다. 하지만 이 와중에도 따라붙은 한 사람이 있었다.

“진태경! 아니, 태경 씨!”

“허.”

나는 김상식을 보며 헛웃음을 삼켰다.

불과 30분 전만 해도 새끼 소리를 들었는데, 이제는 무려 ‘태경 씨’다.

“왜요?”

“아까, 아까는 내가 미안했어요. 예전에 서운했던 일도 전부 다.”

김상식은 횡설수설하며 과거 자신이 내게 저지른 잘못들을 쏟아 냈다. 때아닌 고해성사를 끝낸 그가 본론을 꺼내 들었다.

“그러니까, 다 잊고 비즈니스로 생각합시다.”

“비즈니스.”

그 단어를 혀끝에서 굴려 본다.

어감 좋고, 느낌은 별로다. 비즈니스 상대가 김상식, 소풍 길드라서 더더욱 그랬다.

“솔직히 태경 씨도 알잖아요. 대형 길드 아닌 이상 거기서 거기인 거.”

“알죠. C급이면 대형 길드에서도 손 내미는 것도 알고.”

“잘 생각해 보란 거죠. 그쪽은 아쉬울 게 없어요. C급 헌터 정도는 어렵지 않게 찾아볼 수 있는 동네니까. 대우도 딱 그 정도일 거고.”

김상식이 침을 튀겨 가며 말을 이었다.

“어디서 얼마를 부르든, 무조건 더 얹어 드릴게. 이 부분은 길드장님 허락도 떨어진 거니까 확실해요.”

소풍 길드는 몇 년간 꾸준한 하락세를 보였다.

그런 상황이니 길드장도 어지간히 똥줄이 탄 모양이다.

‘이 인간도 마찬가지고.’

가뜩이나 길드 내 평가도 바닥인데 며칠 전 멋대로 잘라 버린 F급 헌터가 C급으로 재각성을 해 버렸다.

다혈질로 소문난 길드장이 그 사실을 알면 무슨 일이 벌어질지, 기대감에 입꼬리가 올라갔다.

“긍정적으로만 생각해 줘요. 아, 이럴 게 아니라 어디 괜찮은 가게라도 가서 허심탄회하게 이야기를 해 봅시다. 길드장님도 지금 오고 계시…….”

“김상식 씨.”

나직한 목소리에 상식 씨가 입을 다물었다.

“저 영입하고 싶으면, 길드장님한테 토씨 하나 안 빠트리고 전하세요.”

“무슨?”

“꼴도 보기 싫은 인간. 그 인간 하나만 치워 주면 생각해 본다고.”

누굴 가리키는 말인지는 명백했다.

와락 일그러진 얼굴의 김상식을 뒤로하고, 나는 택시에 올랐다.

‘그래, 이거면 된 거야.’

푹신한 시트에 한껏 몸을 기댔다.

등급 재측정과 옛 악연과의 만남. 뭐라 표현할 수 없는 고양감과 동시에 속이 후련했다.

“어디로 모실까요?”

“송내역 희망 고시원이요.”

택시 기사가 나를 보며 허허 웃었다.

“아까 그 손님이네.”

“아.”

염병할 서울 택시.



* * *



“웬일이냐? 네가 소고기를 다 사 오고.”

고시원 옥상에 돗자리와 불판을 깔았다. 진호 형은 익어 가는 고기들을 흐뭇하게 바라보며 말했다.

“좋아. 네 성의를 봐서 사례금은 없었던 일로 하지.”

“줄 생각도 없었어.”

“양아치냐?”

“그 말 그대로 돌려주지.”

우리는 마주 앉아 소주잔을 기울였다.

“그런데 돈은 어디서 났어? 당장 이번 달도 힘들다고 징징거리던 놈이.”

“오늘 일당.”

“그거 몇 푼이나 된다고. 길드 잘리더니 인생 포기했냐?”

“몇 푼?”

나도 모르게 피식 웃음이 나왔다.

“어쭈, 웃어?”

“웃어야지 그럼. 천만 원을 푼돈 취급 하는데.”

진호 형이 우뚝 멈췄다.

“얼마?”

“천만 원.”

“오늘 일당으로 천만 원을 벌었다고?”

“좀 더 들어오긴 했는데 일단은.”

“너 설마.”

진호 형이 침을 꿀꺽 삼켰다. 눈치가 꽤 빠르군. 그를 향해 의미심장한 미소를 지어 보였다.

“맞아, 나 오늘…….”

“장기 팔았냐?”

죽일까.

나는 한숨을 푹 내쉰 다음 술잔을 털어 넣었다.

“사실대로 말해. 이 형은 고시원 총무로서 알아야 할 의무가 있다.”

얼핏 들으면 고시원 총무가 아니라 국무총리인 줄 알겠다.

“게이트 가서 번 거야.”

“증거 가져와. 난 내 눈으로 본 것만 믿는다.”

“그러시든가, 여기.”

진호 형에게 핸드폰을 건네줬다. 협회에서 재측정을 마치고 돌아오던 길에 받은 문자였다.

발신인은…….

“명품충? 누구야 이건?”

“오늘 같이 레이드 뛴 팀장.”

“돈 많나 보네. 의형제 맺고 싶다.”

이 인간 나랑 생각하는 게 비슷하다.

잠시 후, 문자 내용을 확인한 진호 형이 눈을 부릅떴다.

“천삼십만 원? 이거 내가 제대로 본 거냐?”

“그럴걸.”

계약서대로라면 지급 금액은 30만 원. 최 팀장은 거기에 천만 원을 추가 지급했다.

‘심지어 잔금이 남았지.’

홉 고블린 주술사와 대전사는 C급의 레어 몬스터. 놈들의 장비와 가죽, 마정석은 판매처를 찾고 있다고 최 팀장은 덧붙였다.



‘판매되는 대로 추가 지급하겠습니다.’



정신을 차려 보니 근처 마트에서 소고기를 닥치는 대로 쓸어 담고 있는 나를 발견했다.

“너…….”

진호 형이 멍한 얼굴로 나와 손에 쥔 핸드폰을 번갈아 봤다.

“도대체 어디서 뭘 하고 온 거야?”

“말하자면 긴데.”

허허 웃은 진호 형이 가위를 움켜쥐었다.

“네 명줄은 짧고?”

이걸 어디서부터 얘기해야 하나.

캡슐에 관련해서는 더 이상 말하지 않기로 했다.

진호 형에게는 허무맹랑한 거짓말로 남는 게 좋을 것 같다는 판단이었다.

“오늘 게이트에서 레어 몬스터 두 마리가 나왔는데…….”

목숨이 위태로운 절체절명의 순간, 재각성의 행운이 찾아와 놈들을 무찌를 수 있었다는 것. 그리고 협회에서의 일까지.

급하게 이어 붙인 스토리였지만 진호 형에게는 먹혀들었다.

“그래서, 이제는 C급 헌터라고?”

“재조정 절차 끝나려면 며칠 걸려서 아직은 아닌데.”

“그게 그거지, 인마.”

넋 나간 얼굴, 잔뜩 쉰 목소리.

물끄러미 나를 바라보던 진호 형의 눈에 물기가 맺혔다.

이 양반 왜 이래, 이거.

“……설마 우냐?”

“울기는 시발. 뭔 개소리야.”

괜한 욕과 함께 고개를 돌려보지만 툭 떨어지는 한 방울 눈물까지 감출 수는 없었다. 나는 소매로 얼굴을 벅벅 문지르는 진호 형의 눈치를 살폈다.

“형?”

“고기나 뒤집어. 탄다.”

“딴소리는.”

“탄다고!”

“아, 알았어.”

치이익.

고기를 뒤집는데, 뭔가 당황스러우면서도 가슴 한구석이 간질거린다.

‘그러고 보니까 진호 형이랑 안 지도 오래됐네.’

6년? 7년째던가. 세어 보지 않아서 모르겠다. 힘든 하루를 마치고 고시원에 들어오면 그는 늘 그곳에 있었다.

내게 친형이 있다면 이런 느낌이 아니었을까, 가끔 그런 생각이 들 정도로 우리는 형제처럼, 친구처럼 지냈다.

“야.”

어색한 침묵을 깬 것은 진호 형이었다. 나는 괜히 고기를 한 번 더 뒤집었다.

“어, 왜.”

“잘됐어.”

“……그래.”

“그리고.”

작은 목소리가 뒤를 이었다.

“고생했다.”

고작 그 한마디에.

저 밑에서부터 울컥 솟구치는 뭔가가 있었다. 지난 7년간 켜켜이 쌓여 있던 감정과 기억들이 한꺼번에 밀려들었다.

“C급 헌터 된 거. 축하한다. 이젠 놀리지도 못하겠네.”

“형…….”

“태경아…….”

“형!”

“태경아!”

우리는 불판을 사이에 두고 뜨겁게 포옹했다. 진호 형이 떨리는 목소리로 귓가에 속삭였다.

“아까 내가 했던 말, 기억해?”

“형 마음 다 알아. 고마워, 형.”

“그거 말고. 사례금.”

“……응?”

“사례금 꼭 줘라. 형 요즘 힘들다.”

“…….”

“너 이제 돈 많이 벌잖아.”

진짜 죽일까.



* * *



비틀비틀 방으로 돌아온 나는 침대에 몸을 던졌다.

지금쯤 투덜거리며 옥상을 치우고 있을 한 사람을 생각하니 피식 웃음이 나왔다.

‘하여간 방심할 수가 없어요.’

진호 형답다. 축하하는 방식도, 마지막의 장난도.

전부 그 나름의 표현 방식이라는 사실을 나는 잘 알고 있다.

‘고생했다.’

그 한마디가 자꾸만 머릿속을 맴돈다. 인정하면 쪽팔리지만…… 그때만큼은 살짝 울 뻔했다.

‘그래, 고생했지.’

아버지가 돌아가신 뒤 나는 쉴 새 없이 달려왔다. 알바를 병행하며 고등학교를 졸업했고, 아픈 어머니와 어린 여동생을 위해 버티고 또 버텨야 했다.

어느 순간 그 모든 것들이 내게는 당연한 것이 되어 버렸다.

그리고.

띠링.



- 상태 이상, [만취]에 걸렸습니다.

- [운기조식]으로 해독할 수 있습니다.



‘당연하지 않은 것’이 내 인생에 끼어들었다.

정체불명의 고물 게임 캡슐에서부터 시작된 일이었다.

“게임 캡슐이라.”

이제는 저걸 뭐라고 불러야 할지조차 모르겠다. 나를 C급 헌터로 만들어 줬으니 신의 선물이라고 불러야 하나?

아니, 어쩌면 악마가 준 선물일지도 모르지.

‘이대로 괜찮은 건가?’

인생 최고의 날을 보냈음에도 이런 생각을 하는 이유는 간단하다.

‘공짜는 없으니까.’

내가 경험한 세상은 그랬다. 모든 것에는 가격표가 매겨져 있다. 보이든, 보이지 않든 언젠가는 그 값을 치르기 마련이다.

‘시스템은 얼마나 비쌀까.’

천억? 천조? 어쩌면 그 이상?

비실비실 웃던 나는 눈꺼풀이 무거워지는 걸 느꼈다.

‘아, 맞다. 나 만취 상태였지.’

찌륵. 찌르륵.

창밖에는 풀벌레 우는 소리가 요란했다. 시야가 어두워지며 잠이 쏟아져 내린다. 그리고 그날 밤, 나는 꿈을 꿨다.

깊은 산 속 어딘가에서 누군가 나를 흔들어 깨우는 꿈을.

- 조장, 조장!

이상하게 듣는 것만으로도 때려 주고 싶은 목소리. 한편으로는 낯익은 그 목소리의 주인을 확인하고 싶었지만 너무 졸려 눈을 뜰 수 없었다.

- 어떡하지?

- 당장 본대에 알려야…….

- 조장은 왜 갑자기 이럴 때…….

고장 난 라디오를 듣는 기분이다. 목소리에는 노이즈가 꼈고 뚝뚝 끊겼다.

‘졸려…….’

멀어지는 의식 속에서, 작지만 또렷한 목소리가 들린다.

- 막내야, 살아남아라.

그러나 다음 날 잠에서 깼을 때, 나는 그것들을 기억해 내지 못했다.
```

### Current accepted English

```markdown
# Chapter 48

“Y-you? What are you doing there?”

“Good question. What am I doing here?”

“Then, could it be…?”

“What do you mean, ‘could it be’? It is.”

Kim Sangshik’s face went dark and sallow, like a man with shit poisoning.

Seeing him like that felt like ten years of constipation finally letting go. Ah. So this was a shitgasm.

“Anyway, let’s take a step back. We’re not the only ones here, you know.”

I took a step forward, and Kim Sangshik backed away weakly.

The other scouts surrounded me with business cards in hand.

“Sangdong Guild. We promise the best possible treatment.”

“Instead of doing this here, why don’t we move somewhere private and talk…”

Recruitment offers poured in from every direction. In no time at all, dozens of business cards were in my hands.

*So this is what it feels like.*

It was a novel, peculiar feeling. Things I hadn’t experienced even once in seven years were unfolding right in front of me.

In a mere half day, the world around me had changed.

No.

*I’m the one who changed.*

People said that in this business, C-rank was where you started being a real Hunter. Exceptional ability, a high salary, and society’s recognition as a mid-level Hunter.

At last, it sank in that I had stepped onto that path.

*And…*

This was only the beginning.

With the System’s power, I could keep growing.

That was how I would step onto a new path faster than any other Hunter.

“Sir, if you have any conditions you want, we’ll meet them no matter what.”

“Ah, yes. I’ll get in touch later.”

“You really will, right? We’ll be waiting!”

No. Don’t wait. I’m not going to call.

“All right, everyone, calm down.”

Association security guards stepped in and blocked the scouts who kept clinging to me.

They didn’t usually go that far for a C-rank Hunter. I was just such a rare case that I seemed to be drawing a lot of attention.

*Well, I did jump that far from a single reawakening.*

It wasn’t a bad feeling. No—it felt good.

I fought down a smile that kept trying to break out and left the Association. Even then, one person still followed me.

“Jin Taekyung! No, Mr. Taekyung!”

“Heh.”

I looked at Kim Sangshik and swallowed a hollow laugh.

Only thirty minutes ago, he’d been calling me a bastard. Now I was suddenly *Mr. Taekyung*.

“What do you want?”

“I’m sorry about earlier. Really. And I’m sorry about everything from before, too.”

Kim Sangshik rambled, spilling out every wrong he’d done to me in the past. When that untimely confession was over, he finally got to the point.

“So let’s forget all of it and treat this as business.”

“Business.”

I rolled the word around on my tongue.

It sounded good. The feeling was terrible. Even more so because the business partner was Kim Sangshik and Sopung Guild.

“You already know this, Mr. Taekyung. Unless it’s a major Guild, they’re all more or less the same.”

“I know. I also know that once you’re C-rank, even the major Guilds will reach out.”

“I’m telling you to think it through. They won’t be hurting for you. That’s the kind of place where a C-rank Hunter isn’t hard to find. The treatment will be exactly that level, too.”

Kim Sangshik kept going, spraying spit as he talked.

“No matter what they offer, we’ll add more on top. The Guild Master already signed off on that, so you can count on it.”

Sopung Guild had been in steady decline for several years.

Given the situation, the Guild Master seemed scared shitless.

*This guy’s no different.*

The Guild’s opinion of him was already at rock bottom, and now the F-rank Hunter he’d fired on a whim a few days ago had reawakened as C-rank.

I found myself smiling at the thought of what would happen when the Guild Master, notorious for his temper, found out.

“Just look at it positively. Actually, forget standing around here. Why don’t we go somewhere decent and talk it out honestly? The Guild Master is on his way here right—”

“Mr. Kim Sangshik.”

At my quiet voice, Sangshik shut his mouth.

“If you want to recruit me, tell the Guild Master this. Don’t leave out a single word.”

“Tell him what?”

“I’ll think about it if he gets rid of one man I can’t stand the sight of.”

It was obvious who I meant.

Leaving Kim Sangshik behind with his face twisted in fury, I got into a taxi.

*Yeah. This should do it.*

I sank back into the soft seat.

The rank reassessment. Running into old bad blood. An indescribable rush, and at the same time a sense of relief.

“Where would you like to go?”

“Huimang Goshiwon at Songnae Station.”

The taxi driver looked at me and chuckled.

“Oh, you’re that passenger from earlier.”

“Ah.”

*Goddamn Seoul taxis.*

* * *

“What’s gotten into you? You actually bought beef.”

We laid out a mat and a grill on the goshiwon roof. Jinho hyung gazed happily at the meat as it cooked.

“All right. Seeing your sincerity, I’ll forget about the finder’s fee.”

“I wasn’t planning to give you one.”

“Are you a punk?”

“Right back at you.”

We sat across from each other and tilted our soju glasses.

“But where did you get the money? You were whining that even this month was going to be tough.”

“Today’s pay.”

“How much could that be? Did you give up on life after getting fired from the Guild?”

“How much?”

I couldn’t help letting out a little laugh.

“Oh, you’re laughing?”

“I should laugh. You’re treating ten million won like pocket change.”

Jinho hyung froze.

“How much?”

“Ten million won.”

“You made ten million won in one day’s pay?”

“A little more came in, but that’s for now.”

“You didn’t…”

Jinho hyung swallowed hard. He caught on fast. I gave him a meaningful smile.

“That’s right. Today I—”

“Did you sell an organ?”

Should I kill him?

I let out a long sigh, then downed my drink.

“Tell me the truth. As the goshiwon manager, I have a duty to know.”

If you only heard that, you’d think he was the prime minister, not a goshiwon manager.[^2]

“I made it at a Gate.”

“Bring me proof. I only believe what I see with my own eyes.”

“Suit yourself. Here.”

I handed him my phone. It was the message I’d gotten on the way back from the Association after the reassessment.

The sender was…

“Luxury Nutjob? Who’s that?”

“The Team Leader I ran the raid with today.”

“He must be rich. I want to become sworn brothers with him.”

This guy and I really did think alike.

A moment later, Jinho hyung finished the message and his eyes went wide.

“10.3 million won? Am I reading this right?”

“Probably.”

According to the contract, the payment was supposed to be 300,000 won. Team Leader Choi had added another ten million.

*And there’s still a balance left.*

The Hobgoblin Priest and Great Warrior had been C-rank Rare Monsters. Team Leader Choi had added that he was looking for buyers for their equipment, leather, and Magic Gems.

> “We’ll make an additional payment as soon as they’re sold.”

When I came to, I found myself in a nearby supermarket, grabbing every piece of beef I could get my hands on.

“You…”

Jinho hyung stared blankly, looking from me to the phone in my hand.

“Where the hell have you been, and what did you do?”

“It’s a long story.”

Jinho hyung chuckled and gripped the scissors.

“And your lifespan is short?”

Where was I even supposed to start?

I had decided not to say anything more about the capsule.

I figured it was better if, for Jinho hyung, it just stayed an absurd lie.

“Two Rare Monsters showed up at the Gate today, and…”

At a life-or-death moment, the luck of a reawakening had come, and I’d been able to take them down. Then I told him about the Association.

It was a story hastily stitched together, but Jinho hyung bought it.

“So now you’re a C-rank Hunter?”

“The reassessment procedure will take a few days, so technically, not yet.”

“Same thing, you idiot.”

His face was dazed, his voice hoarse.

Jinho hyung stared at me for a long moment. Moisture gathered in his eyes.

*What’s gotten into this guy?*

“…Don’t tell me you’re crying?”

“The fuck I am. What kind of bullshit is that?”

He turned away with an unnecessary curse, but he couldn’t hide the single tear that slipped down. I watched him out of the corner of my eye as he roughly rubbed his face with his sleeve.

“Hyung?”

“Turn the meat over. It’s burning.”

“Changing the subject?”

“I said it’s burning!”

“Ah, all right.”

Sizzle.

As I turned the meat, I felt flustered, and yet a corner of my chest tickled.

*Come to think of it, I’ve known Jinho hyung for a long time.*

Six years? Seven? I didn’t know. I’d never counted. Whenever I came back to the goshiwon after a hard day, he had always been there.

Sometimes I wondered if this was what it would have felt like to have a real older brother. We had lived like brothers, like friends.

“Hey.”

Jinho hyung broke the awkward silence. I turned the meat over one more time for no reason.

“Yeah? What?”

“Good for you.”

“…Yeah.”

“And…”

His quiet voice followed.

“You worked hard.”

At just those words, something surged up from deep inside me. The emotions and memories that had stacked up over the past seven years all came rushing in at once.

“Congratulations on becoming a C-rank Hunter. I guess I can’t tease you anymore.”

“Hyung…”

“Taekyung…”

“Hyung!”

“Taekyung!”

We hugged each other tightly across the grill. Jinho hyung whispered in my ear, his voice shaking.

“Do you remember what I said earlier?”

“I know how you feel, hyung. Thank you.”

“That’s not what I meant. The finder’s fee.”

“…What?”

“You have to pay the finder’s fee. Hyung’s having a hard time these days.”

“…”

“You make a lot of money now.”

Should I really kill him?

* * *

I staggered back to my room and threw myself onto the bed.

I let out a little laugh, thinking of the one person who was probably cleaning up the roof while grumbling.

*You really can’t let your guard down around him.*

That was Jinho hyung. The way he congratulated me, and that last prank.

I knew all of it was just his way of showing it.

*You worked hard.*

Those words kept circling in my head. It was embarrassing to admit, but for a moment there, I had almost cried.

*Yeah. I really did work hard.*

After my father died, I had run nonstop. I graduated high school while working part-time jobs, and I had to hold on and keep holding on for my sick mother and little sister.

At some point, all of it had become a given.

And then.

Ding.

> **System**
>
> - You have been afflicted with a Status Effect: Dead Drunk.
> - It can be detoxified by circulating your qi.

*Something that wasn’t a given had entered my life.*

It had all started with that unidentified junk game capsule.

“A game capsule, huh?”

I didn’t even know what to call the thing anymore. It had made me a C-rank Hunter, so should I call it a gift from God?

No. Maybe it was a gift from the devil.

*Is this really okay?*

The reason I was thinking this even after the best day of my life was simple.

*Nothing comes for free.*

That was the world I knew. Everything had a price tag. Visible or not, sooner or later you had to pay.

*How expensive is the System?*

A hundred billion? A quadrillion? Maybe even more?

I laughed weakly and felt my eyelids growing heavy.

*Oh, right. I was dead drunk.*

Chirp. Chirp-chirp.

Outside the window, the grass insects were crying loudly. My vision darkened, and sleep poured over me.

That night, I dreamed.

I dreamed that somewhere deep in the mountains, someone was shaking me awake.

“Squad leader, squad leader!”

Weirdly, just hearing it made me want to punch whoever it belonged to. Part of me wanted to see who that familiar voice belonged to, but I was too sleepy to open my eyes.

“What do we do?”

“We have to tell the main force right away…”

“Why is the squad leader suddenly like this now of all times…”

It felt like listening to a broken radio. The voices had static in them, and they kept cutting out.

*I’m sleepy…*

As my consciousness drifted farther away, I heard a small but clear voice.

“Youngest, survive.”

But when I woke the next day, I couldn’t remember any of it.

[^2]: A pun: the Korean word for a goshiwon manager sounds like “prime minister.”
```
