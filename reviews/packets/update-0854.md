<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0854.txt",
      "sha256": "2e67f14248ad1b92f223cfcd615545c5debc53296f5cfd0c9deefaa0dd04ab35",
      "bytes": 13624
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "56c147b4e208c3d6f5448d06a927ec1ee50dd2d81a7446ceec6959b01c2e0067",
      "bytes": 1861
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f23c0abede4cee966eb0ece366e3ed19d44f5a5fceaacc621537d29d293b3d1e",
      "bytes": 228367
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0fca0823a4fbf3bdbbfd500c298315fa9a02a6ffe6cce9c65d64a8291aa02645",
      "bytes": 759
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "cc5d369594aaa700470c4324ebb5e5eca4369f4e6e06ade6420e9961524dc80a",
      "bytes": 253241
    }
  ],
  "estimated_tokens": 8728
}
-->

# Durable State Update — Chapter 854

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 854. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 854. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 854,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 854,
    "continuity_sources": [854],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "The Divine Physician secured the Blood Soul Gu found in the deceased City Lord of Sichuan Province; it weakens hosts, causes episodes of madness, and eventually kills them.",
    "Jin suspects Dark Heaven’s covert killing of the City Lord is part of a scheme targeting the Great Nation, possibly its imperial family.",
    "Prince Shangshan Zhu Bao is traveling with fifty Embroidered Uniform Guard members; their expected route from Shanxi passes through Shandong and Jiangsu toward Zhejiang.",
    "Hong Jin joined Prince Shangshan in Shanxi after requesting support from the Lower District Sect.",
    "A Shanxi tracking team was wiped out while following the group, and its operation was suspended over concern about official intervention.",
    "The Hidden Shadow Pavilion issued an Alliance Leader-approved order for Jeok Cheongang, Jin Taekyung, and the entire Fire Dragon Pavilion to escort Prince Shangshan.",
    "Jin and his party have departed to intercept Prince Shangshan in Jiangsu before the first of next month."
  ],
  "continuity_sources": [
    852,
    853
  ],
  "open_questions": [
    "Why did Dark Heaven secretly kill the City Lord of Sichuan Province?",
    "Is Dark Heaven targeting the Great Nation’s Emperor or imperial family, and is it influencing the Son of Heaven?",
    "What is the Embroidered Uniform Guard’s purpose in traveling with Prince Shangshan, and can Jin’s party reach him in time?",
    "What prompted the imperial decree against Hong Jin, and what will happen to him and Prince Shangshan?"
  ],
  "safe_through": 853,
  "temporary_decisions": [
    "Render 혈혼고 as “Blood Soul Gu.”",
    "Render 독혈지 as “Poisonblood Grounds.”",
    "Render 대국 as “Great Nation.”",
    "Render 금의위 as “Embroidered Uniform Guard.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 사천     | **Sichuan**            |
| 화산     | **Huashan**            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 쟁자수 | **caravan porter** | Porters who lead the escort caravan's horses and carts. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 장일 | **Jang Il** | Twenty-five-year-old two-knot Beggars' Sect Disciple killed near Emei. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 중경 | **Chongqing** | Region crossed by the Yangtze route. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 광서 | **Guangxi** | Region bordering Nanman. |
| 만족 | **Man people** | An ethnic group mentioned by the Poison Flower Pavilion owner. |
| 서문 | **West Gate** | One of the Nanman Beast Palace's gates. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 852
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

## Korean source

```text
＃854화



호북성 하급 무관 장일(張一)은 자신의 삶에 만족할 줄 아는 사람이었다.

그를 아는 누군가는 사내로 태어나 야심이 없다며 혀를 찼지만, 정작 장본인인 장일은 스스로를 자랑스럽게 여겼다.

‘이 정도면 할 만큼 했지. 암, 그렇고말고.’

가진 것이라고는 쥐뿔도 없는 양민 집안에서 태어나 정식 무관의 자리까지 오른 그다.

비록 낮은 직급 탓에 나라에서 받는 녹봉은 쥐꼬리만 했지만, 중요한 것은 그가 호북성 서쪽에 위치한 주요 도시인 의창(宜昌)의 일곱 수문장 중 하나라는 사실이었다.

의창이 어떤 곳인가.

빼어난 자연 풍광을 보기 위한 시인 묵객(墨客)들의 발걸음이 끊이지 않는, 호북성 전역을 가로지르는 장강 연안의 항구 도시가 바로 의창이다.

그만큼 하루에도 수많은 물자와 인파가 드나들었고, 그 과정에서 각 관문이 막대한 통행료를 거둬들이는 것은 당연지사였다.

물론 상부에는 절대 보고되지 않는, 뇌물이라는 이름의 떡고물도 함께.

‘오늘은 어느 잘나신 놈들이 찾아오려나.’

새벽 일찍 일어난 장일은 설레는 마음으로 출근을 준비했다.

윤기가 자르르 흐르는 비단옷에, 멋지게 장식된 패검까지.

터무니없이 비싼 탓에 사지 못한 면경(面鏡)에 이런 자신의 모습을 비추어 보지 못한다는 것은 조금 속이 쓰렸으나, 늙은 하인의 말이 한 줄기 위안이 되어 주었다.

“실로 영웅의 풍모이십니다, 주인어른.”

“큼. 자네가 보기에도 그런가?”

“예에. 관문을 통과하는 이들이 누구건, 주인어른의 위엄 앞에는 감히 고개도 제대로 들지 못할 겁니다요.”

“어허, 사람이 실없기는.”

말은 그렇게 해도 입꼬리를 씰룩이는 장일의 모습에, 늙은 하인이 변죽 좋게 웃으며 손을 내저었다.

“어휴, 제가 언제 빈말하는 것 보셨습니까? 한데 오늘따라 아끼시던 비단옷이며 검까지 차시는 걸 보면 중요한 일이 있으신 모양입니다.”

“자네는 언제나 눈치가 빠르군. 맞네. 오늘은 꽤 거물들이 올지도 몰라. 두 달 전쯤에 중경(重慶)으로 떠났던 상행이 이맘때쯤 돌아온다고 했거든.”

“허어. 한데 근래 들어 중경 쪽 분위기가 요상하게 흐르고 있지 않습니까?”

“누가 그러던가?”

“아는 보부상에게 들었습니다. 중경뿐만 아니라 광서 쪽에서도 무림인들 사이에 한바탕 피바람이 불었다고…….”

“전부 헛소리니까 무시하게. 광서의 소식은 나도 얼추 들어서 알고 있지만, 중경은 오합지졸 같은 산적이나 수적 따위밖에 없어. 이번 상행도 분명 대박일세.”

장일이 옷매무새를 가다듬으며 흐뭇하게 웃었다.

사천성과 호북성 사이에 자리 잡은 중경은 성이라고 부르기에는 부족하나, 풍부한 자원과 특산품이 있어 수많은 상단들이 군침을 흘리는 곳.

이문이 많이 남는 만큼 경쟁도 치열했고, 그렇게 뽑힌 상단 역시 엄청난 규모를 자랑했다.

‘이번 상행은 특히나 그랬지.’

세 개의 상단이 힘을 합쳤다.

그렇게 동원한 무사며 쟁자수의 숫자만 물경 오백.

백 개가 넘는 수레를 상선(商船) 열 척에 실어 떠난 것이 두 달 전쯤이었으니, 장일로서는 곧 자신에게 돌아올 떡고물을 기대할 수밖에 없었다.

‘어떻게 얻은 자리인데, 그 정도는 해 줘야 보람이 있지.’

뿌린 만큼 거둔다는 옛 격언은 장일에게 있어서 전혀 다른 의미다.

그는 의창의 수문장이 되기 위해 엄청난 뇌물을 뿌렸고, 불과 이 년도 되지 않아 그 이상의 것을 거두었으나 이쯤에서 만족할 생각은 추호도 없었다.

‘지금처럼만 거둬들이면 충분하다. 크게 욕심부릴 필요 없어. 번듯한 장원 한 채 마련할 정도면 족해.’

탐욕은 또 다른 탐욕으로 잊히는 법.

장일은 적당히 부패하고, 적당히 게으른 자신이 퍽 양심적인 관리라고 자부하며 집을 나섰다.

그리고 근무지인 서문(西門)에 도착하자마자, 무언가 잘못되었다는 것을 깨달았다.

‘뭐지?’

팽팽하게 조여드는 공기.

여느 때처럼 팔짱을 낀 채 하품을 하고 있어야 할 병사들은 땀범벅이 된 채 사방팔방으로 뛰어다녔고, 피 묻은 들것이나 그을린 잡동사니 따위가 곳곳에 굴러다녔다.

두 달 전 중경으로 떠나며 위풍당당하게 펄럭이던 세 개의 깃발도 함께.

“도대체 이게 무슨…….”

“나으리! 장 무관 나으리!”

문득 귓가를 파고드는 누군가의 부름에, 멍하니 중얼거리던 장일이 퍼뜩 정신을 차렸다.

어느새 익숙한 얼굴의 수하가 사색이 된 얼굴로 그의 앞에 서 있었다.

“이게. 이게 무슨 일이냐!”

“그, 그것이 그러니까…….”

“어서 바른대로 고하지 못할까!”

서슬 퍼런 상관의 외침에 순간 움츠러들었던 수하가 더듬거리는 목소리로 말을 끄집어냈다.

횡설수설에 가까운 그의 이야기를 듣고 있던 장일이 입을 딱 벌렸다.

“스, 습격?”

“예, 예. 상행을 끝마치고 돌아오는 길에 산적들의 습격을 받았다고 합니다.”

“말도 안 되는 소리! 무사며 쟁자수의 머릿수만 물경 오백이었다! 산적 놈들이 미치지 않고서야 어찌 그럴 수 있단 말이냐!”

경악에 가득 찬 고함이 터져 나온 그 순간.

“세상이 미쳐 돌아가는데, 산적들이라고 별반 다르겠나.”

피곤에 찌든 목소리가 불쑥 끼어들었다. 고개를 돌려 상대를 확인한 장일이 눈을 깜빡였다.

“다, 단주 어른?”

틀림없다. 피범벅이 된 몸뚱어리에 넝마가 된 옷가지를 걸치고 있어도 똑똑히 알아볼 수 있었다.

그는 장일이 두 달 전부터 오매불망 기다렸던 거물이자, 이번 상행에 참여한 세 명의 상단주 중 한 사람이었으니까.

“이렇게 살아서 다시 보니 반갑군. 장 무관.”

“도, 도대체 이게 어떻게 된 겁니까? 다른 두 분은요?”

“함께 왔다네. 대화를 나눌 기회는 영영 사라져 버렸지만.”

상단주의 손끝을 따라 고개를 돌린 장일은 눈앞이 캄캄해지는 것을 느꼈다.

거적에 쌓인 수십여 구의 시체. 그중에서도 따로 분류하여 떨어트려 놓은 시신 두 구의 정체는 불 보듯 뻔했다.

“……설마.”

“자네가 예상하는 그대로일세. 마지막까지 용감하게 싸웠지만 어쩔 수 없었지. 우리로서는 중과부적(衆寡不敵)이었어.”

“중과부적이라니. 산적들의 숫자가 그렇게 많았단 말입니까?”

“엄연히 따지면 산적과 수적들이었네. 예상치 못한 기습에 정신이 없는 와중에도 바로 알아보겠더군. 작살을 든 놈들이 사방에 득실거렸으니까.”

“수, 수적이 어찌!”

“산에 있으나 장강에 있으나, 도적놈들은 도적질을 본분으로 삼는 법 아니겠나?”

힘없이 중얼거린 상단주는 반파된 수레에 몸을 기대며 말을 이었다.

“두 달 전, 의창을 떠날 때만 해도 모든 게 순조로웠네. 하지만 중경에 도착하자마자 뭔가 잘못되어가고 있다는 생각이 들었어. 아니나 다를까. 옥화산(玉化山)에 발을 들이기 무섭게 놈들이 나타나더군.”

옥화산은 아름다운 풍광과는 별개로 험하기로 이름난 중경의 험산(險山)이다.

사방이 좁고 가로막힌 풀숲에서 적들과 처음으로 조우했던 순간을 떠올린 상단주가 자신도 모르게 몸을 부르르 떨었다.

“우리는 거칠 것이 없었네. 각 상단에서 정예들만 뽑아 데려왔고, 만일의 상황을 대비하여 이름난 낭인 수십 명도 고용했으니까. 하지만 놈들이 모습을 드러내자마자 그 모든 것이 전부 소용없다는 걸 깨달았네.”

“대관절 놈들의 숫자가 얼마나 많았기에…….”

“일천.”

“예?”

“일천이라고 했네. 눈대중으로 살폈음에도 그 정도였으니, 실제로는 그 이상이었을 테지.”

“……!”

장일은 잠시 자신의 귀를 의심했다.

일천이 넘는 도적 떼라니. 북방에서는 초원을 근거지로 한 유목민이나 마적단이 힘을 합쳐 대병력으로 쳐들어오는 일이 있었지만, 중경은 아니었다.

실로 유례가 없는, 있어서는 안 되는 일이 벌어진 것이다.



‘허어. 한데 근래 들어 중경 쪽 분위기가 요상하게 흐르고 있지 않습니까?’

‘누가 그러던가?’

‘아는 보부상에게 들었습니다. 중경뿐만 아니라 광서 쪽에서도 무림인들 사이에 한바탕 피바람이 불었다고…….’



집을 나서기 전, 늙은 하인과 주고받은 대화를 떠올린 장일은 덜컥 가슴이 내려앉았다.

그가 아끼던 비단옷은 언제 흘렸는지 모를 식은땀으로 이미 축축하게 젖어 있었다.

‘말도 안 돼.’

중경은 호북과 지척이다. 그가 수문장으로 있는 의창에서도 뱃길을 타면 사흘이요, 육로로 이동한다면 닷새 안에 도착할 수 있는 거리.

‘이게, 이게 전부 사실이라면…….’

손발이 덜덜 떨리고 호흡이 가빠진다.

볼 것도 없이 당장 일어나 군사들을 지휘하고, 경종을 울려야 함에도 몸이 제대로 움직이지 않았다.

그리고 그런 장일의 상황을 아는지 모르는지, 상단주는 계속해서 말을 이어 나갔다.

“우리는 통행료를 내겠다고 했지만, 대답 대신 돌아온 것은 놈들이 쏘아 보낸 화살이었네.”

누군가의 죽음을 신호탄으로 치열한 전투가 벌어졌다.

상단에서 키워 낸 무사들과 고용된 낭인들, 심지어는 수레를 끌던 쟁자수까지 나서서 싸웠으나, 일평생을 약탈자로 살아온 수적과 산적들은 거침없이 그들을 베어 넘겼다.

“그건 전투라기보다는 도륙에 가까웠네. 아군의 숫자도 많았지만 그중 절반은 쟁자수였고, 남은 이들로는 한계가 있었지.”

“아니, 아무리 그래도 어떻게…… 그놈들도 결국 화전민이나 어부 출신이 대다수 아닙니까?”

“그래, 그랬겠지. 하지만 놈들은 뭔가 달랐네. 마치 신들린 것처럼 계속해서 달려들었어.”

최대한 담담한 어투로 말하고 있던 상단주의 목소리가 문득 파르르 떨렸다.

“다리가 베이고, 팔이 날아가도 달려들었지. 하나를 쓰러트리면 셋이, 셋을 쓰러트리면 다섯이. 솟구치는 두려움을 참으며 그마저도 쓰러트리면 열 명의 적이 기다리고 있었어. 계속해서, 또 계속해서…….”

상단주는 지금도 또렷하게 기억하고 있었다.

아니, 숨이 끊기는 그 순간까지 잊지 못할 것이다.

지옥도(地獄道)에서 뛰쳐나온 악귀들처럼 달려들던 그들의 모습을.

“전투는 불과 반 시진 만에 일방적으로 끝났고, 사기가 꺾인 아군은 너나 할 것 없이 도망치기 시작했네. 사방이 비명과 죽음으로 가득한 그곳에서 나 역시 수하들을 이끌고 몸을 피했지. 비록 상행은 실패했지만, 어떻게든 살아 나가야 했어.”

목숨보다 귀중한 것은 없다.

그는 다른 두 상단주와 함께 남아 있는 병력들을 이끌고 퇴각했고, 옥화산을 빠져나왔을 때는 오백에 달하던 숫자가 절반으로 줄어 있는 것을 발견했다.

“우리는 산자락을 타고 계속해서 도망쳤네. 자그마치 사흘 동안.”

“사, 사흘?”

“산 밑으로 내려가 관군이나 다른 무림 문파에 도움을 청하고 싶었지만, 놈들이 있는 한 불가능에 가까웠지. 그 방법만이 최선이었어.”

적들은 각 길목을 집중적으로 감시하고 있었고, 간신히 살아남은 생존자들은 호북성으로 돌아갈 최단 거리를 통해 도주를 감행하여 마침내 중경을 벗어났다.

아니, 벗어났다고 생각했다.

가까스로 옥화산을 빠져나와, 가장 가까운 나루터에 정박시켜 두었던 열 척의 상선이 불타오르는 광경을 보기 전까지는.

“모든 것이 끝났다고 확신했네. 더는 도망칠 엄두조차 들지 않을 만큼.”

장장 사흘간 이어진 추격전은 끔찍하고 치열했다.

오백에서 절반으로. 그 절반에서 불과 백여 명도 되지 않는 숫자로 줄어든 그들은 죽음을 떠올렸다.

검붉은 불길과 함께 가라앉아가는 상선을, 자신들의 마지막 희망이었던 그것을 지켜보며.

등 뒤에서 울려 퍼지는 적들의 고함을 들으며.

그리고 생애 마지막의 전투가 시작되려던 그때. 그 누구도 예상할 수 없었던 인물들이 등장했다.

“웬 중년인이었네. 열 명 남짓한 일행과 함께하고 있던.”

“중년인…… 말입니까?”

“그래. 마치 산보 하듯이 다가오더니, 타오르는 상선을 가리키며 대뜸 이렇게 묻더군.”

호흡을 가다듬은 상단주가 말을 이었다.

“어떤 호로 새끼가 불을 질렀냐?”
```

## Final English reading copy

```markdown
# Chapter 854

Jang Il, a junior military officer in Hubei Province, was a man who knew how to be satisfied with his life.

Some people who knew him would click their tongues and say he had no ambition, despite being born a man. But Jang Il himself was proud of who he was.

*I’ve done enough. Damn right I have.*

He’d been born into a commoner family that had next to nothing, yet he’d risen to the rank of an official military officer.

His low rank meant the government paid him a pittance, but the important thing was that he was one of the seven gate commanders in Yichang, a major city in western Hubei Province.

What kind of place was Yichang?

A port city on the banks of the Yangtze, which ran across Hubei Province, it drew a steady stream of poets and scholars eager to take in its splendid scenery.

That meant countless people and goods passed through every day, and naturally, each gate collected a hefty toll.

And, of course, there were the little extras called bribes that were never reported to the higher-ups.

*I wonder what big shots will come through today.*

Jang Il had risen early, eager to get ready for work.

He wore a silk robe that gleamed with a rich sheen and carried a finely decorated sword.

It stung a little that he couldn’t see how he looked in a mirror, since they were far too expensive for him to buy. But his elderly servant’s words offered some comfort.

“You truly have the bearing of a hero, my lord.”

“Ahem. You think so, too?”

“Yes, my lord. Whoever passes through the gate, none of them will dare raise their heads properly in the face of your authority.”

“Now, now. What a silly thing to say.”

Despite his words, Jang Il’s lips twitched upward. The elderly servant laughed easily and waved a hand.

“Oh, when have you ever known me to flatter you? But seeing you wear your finest silk robe and carry your sword today, you must have something important going on.”

“You’re always quick to catch on. You’re right. Some real big shots might be coming through today. A trading caravan that left for Chongqing about two months ago is supposed to return around now.”

“Goodness. But haven’t things been getting strange around Chongqing lately?”

“Who told you that?”

“I heard it from a traveling merchant I know. There’s been a bloodbath among martial artists not just around Chongqing, but in Guangxi as well…”

“It’s all nonsense, so ignore it. I’ve heard a little about Guangxi myself, but Chongqing only has a few disorganized bandits and river pirates. This caravan is bound to bring in a fortune.”

Jang Il straightened his clothes, smiling with satisfaction.

Chongqing lay between Sichuan Province and Hubei Province. It wasn’t quite a province, but it had abundant resources and local specialties that made countless trading companies eager to do business there.

The profits were huge, so competition was fierce, and the trading companies that won out were massive.

*This caravan especially so.*

Three trading companies had joined forces.

The number of guards and caravan porters they’d brought along was a staggering five hundred.

They’d loaded more than a hundred carts onto ten merchant ships and set out about two months ago. Jang Il couldn’t help looking forward to the little extras that would soon come his way.

*How could I not get something out of it, after everything it took to get this job?*

The old saying “you reap what you sow” meant something entirely different to Jang Il.

He’d scattered a fortune in bribes to become a gate commander in Yichang, and in less than two years, he’d collected far more than he’d spent. But he had no intention of being satisfied now.

*As long as I keep collecting like I am now, that’s plenty. No need to get greedy. Just enough to buy a decent estate.*

One greed was soon forgotten in pursuit of another.

Jang Il prided himself on being a conscientious official—corrupt just enough, and lazy just enough—and left home.

The moment he arrived at his post at the West Gate, he realized something was wrong.

*What is this?*

The air was taut.

The soldiers, who would usually be yawning with their arms folded, were drenched in sweat as they ran in every direction. Bloodied stretchers and charred scraps of debris lay scattered all around.

The three flags that had flown proudly when the caravan left for Chongqing two months ago were among them.

“What on earth is…”

“My lord! Officer Jang!”

At the sudden call that pierced his ears, Jang Il snapped out of his daze.

A familiar subordinate was standing in front of him, pale as a sheet.

“What—what happened here?”

“Th-that is…”

“Why don’t you tell me the truth at once!”

The subordinate flinched at his superior’s sharp shout, then stammered out an answer.

As Jang Il listened to his rambling story, his mouth fell open.

“A-an attack?”

“Yes, yes. They say the caravan was attacked by bandits on its way back.”

“That’s impossible! There were five hundred guards and caravan porters! What bandit would be crazy enough to try that?”

Just as he let out his horrified shout—

“The world’s gone mad. Why should bandits be any different?”

A weary voice cut in. Jang Il turned to look and blinked.

“M-Master of the Trading Company?”

There was no mistaking him. Even with his body drenched in blood and his clothes reduced to rags, Jang Il recognized him at once.

He was one of the three trading company masters on the caravan—the big shot Jang Il had been eagerly awaiting for the past two months.

“Glad I survived to see you again, Officer Jang.”

“W-what on earth happened? What about the other two?”

“They came with us. But we’ll never have the chance to speak again.”

Jang Il looked where the trading company master pointed and felt the world go dark.

Several dozen bodies lay wrapped in straw mats. The identities of the two corpses set apart from the rest were obvious.

“……Surely not.”

“Just what you think. They fought bravely to the very end, but there was nothing we could do. We were simply outnumbered.”

“Outnumbered? There were that many bandits?”

“Strictly speaking, they were bandits and river pirates. Even while reeling from the unexpected ambush, I could tell who they were. Harpoon-wielding men were swarming everywhere.”

“R-river pirates? How could they be here?”

“Whether they’re in the mountains or on the Yangtze, thieves make their living by thieving, don’t they?”

The trading company master muttered wearily and leaned against a shattered cart.

“Everything went smoothly when we left Yichang two months ago. But the moment we reached Chongqing, I had a feeling something was going wrong. Sure enough, no sooner had we set foot on Yuhua Mountain than they appeared.”

Despite its beautiful scenery, Yuhua Mountain was known as one of Chongqing’s rugged mountains.

The trading company master remembered the first moment they’d encountered their enemies, in a patch of brush hemmed in by narrow, blocked-off paths. He shuddered without realizing it.

“We had nothing to worry about. Each trading company had brought only its best men, and we’d hired dozens of famous wandering martial artists in case of trouble. But the moment they showed themselves, I realized none of that mattered.”

“How many of them were there?”

“A thousand.”

“Pardon?”

“I said a thousand. That’s how many I estimated at a glance, so there must have been even more.”

“……!”

For a moment, Jang Il thought he’d misheard.

A band of more than a thousand bandits? In the north, nomads or mounted bandits based on the grasslands sometimes joined forces and invaded with a large army. But not in Chongqing.

It was an unprecedented thing, something that should never have happened.



*“But haven’t things been getting strange around Chongqing lately?”*

*“Who told you that?”*

*“I heard it from a traveling merchant I know. There’s been a bloodbath among martial artists not just around Chongqing, but in Guangxi as well…”*



Remembering his conversation with the elderly servant before he left home, Jang Il felt his heart sink.

His cherished silk robe was already damp with cold sweat, though he couldn’t remember when he’d started sweating.

*No way.*

Chongqing was right next to Hubei. From Yichang, where he served as a gate commander, it was three days by boat or five days by land.

*If—if all of this is true…*

His hands and feet trembled, and his breathing grew shallow.

He should’ve been on his feet, directing the soldiers and sounding the alarm, but his body wouldn’t move.

Whether he knew what was happening to Jang Il or not, the trading company master continued.

“We said we’d pay the toll, but their answer was a volley of arrows.”

Someone’s death set off a fierce battle.

The fighters trained by the trading companies and the hired wandering martial artists fought back. Even the caravan porters who had been hauling the carts joined in. But the river pirates and bandits, who’d spent their whole lives as raiders, cut them down without hesitation.

“It was less a battle than a slaughter. We had plenty of men, but half of them were caravan porters. The rest could only do so much.”

“B-but how could that happen? Most of those men must’ve been farmers or fishermen, too, right?”

“Right, they probably were. But there was something different about them. They kept charging at us like they were possessed.”

The trading company master’s voice, which had been as calm as he could make it, suddenly quivered.

“Even with their legs slashed and their arms torn off, they kept coming. Knock one down, and three more came. Knock three down, and five more appeared. And if we held back our rising fear and took them down, ten more enemies were waiting. Over and over, again and again…”

The trading company master still remembered it clearly.

No—he would never forget it, not until his last breath.

The way they charged like fiends bursting out of a hellscape.

“The battle ended decisively in just half a shichen—roughly an hour—and our side broke. Men started running in every direction. Surrounded by screams and death, I led my subordinates away, too. The caravan had failed, but we had to get out alive somehow.”

There was nothing more precious than one’s life.

He’d fled with the other two trading company masters and the troops still standing. When they emerged from Yuhua Mountain, they found that their number had been cut in half from the five hundred they’d started with.

“We kept running along the mountain foothills. For three whole days.”

“Th-three days?”

“We wanted to go down to the foot of the mountain and ask the imperial troops or another Murim sect for help, but with those men around, that was nearly impossible. It was our only choice.”

The enemy had been watching the main routes closely. The survivors, barely clinging to life, had made a break for Hubei along the shortest route and finally escaped Chongqing.

Or so they’d thought.

That was before they saw the ten merchant ships they’d left at the nearest dock, all burning.

“I was sure it was over. I couldn’t even bring myself to consider running any farther.”

The chase had gone on for three whole days. It had been brutal and fierce.

From five hundred, their number had been cut in half. From that half, it had fallen to fewer than a hundred. They began to think of death.

They watched the merchant ships—their last hope—sink beneath the dark red flames.

They heard the enemies shouting behind them.

And just as their final battle was about to begin, people no one could have expected appeared.

“There was a middle-aged man. He was with a group of about ten.”

“A middle-aged man…?”

“Yes. He walked toward us as if out for a stroll, pointed at the burning ships, and asked us this out of the blue.”

The trading company master steadied his breathing and continued.

“Which son of a bitch set those on fire?”
```
