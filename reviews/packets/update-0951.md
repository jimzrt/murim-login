<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0951.txt",
      "sha256": "44f3d1caae4e3ba75350cb63e046512a82e003ea0668ac1ed41edf920b4587b5",
      "bytes": 12922
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "860a243b4d75b4c63ad2f5ae5c6e9488e48ff8d1c71f236613079bdb383f9b37",
      "bytes": 2473
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bbb6bd1bdb9407382aeed622923c33e7d8077914c1c9edfd5dc0c45aea7b5f65",
      "bytes": 233797
    },
    {
      "path": "characters/Chinggen.md",
      "sha256": "e1814b721f26c04334f0648e26bb374e7a63c9ea91efd46c0288d0e8fb7e999c",
      "bytes": 577
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "84341a47fea4a0dae482268a43423a73955c01e4422f26c8f9c812d7b176ad54",
      "bytes": 759
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6102ae2e899d4e8d81d4fe546d75b643d03373237691ee2975a1296a52bf463a",
      "bytes": 1449
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "4cbe72c052d247b59af4ffb9a47287039ca99be1a5cde4809e6b8918db07c272",
      "bytes": 622
    },
    {
      "path": "characters/Temur.md",
      "sha256": "2dd2b3729e47afc3dcaba86e07c28f36d70c01ef42bb6e3b130e75812a1e61fe",
      "bytes": 616
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1efb275a0485bdab8f74bddeafc29157bc04997b8313766f8a1a4de940fca98a",
      "bytes": 267426
    }
  ],
  "estimated_tokens": 9583
}
-->

# Durable State Update — Chapter 951

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
1 and safe_through 951. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 951. Profile updates may replace only one
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
  "chapter": 951,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 951,
    "continuity_sources": [951],
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
    "The Emperor was poisoned with Blood Soul Gu, which reached his marrow; the Divine Physician said his vitality was at its limit and could not guarantee survival for another couple of months.",
    "The Divine Physician says the Emperor’s only path to survival requires him to die once; the method remains unexplained.",
    "Taekyung’s System Quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence remain unknown.",
    "War with Dark Heaven is imminent. The Jin Family of Taiyuan has rescinded its retreat and is preparing a stand at Eight Spring Gorge with Shanxi forces against an estimated thirty to forty thousand advancing enemies.",
    "The Hebei Peng Family, Murong Family, Huashan, and Zhongnan Sect are each sending two thousand reinforcements to Shanxi; two thousand martial artists have departed the Murim Alliance headquarters for the north.",
    "The improved Temporary Strength Pill may be spreading through Murim and may create a dangerous drive for strength; its effects and distribution network remain unknown.",
    "Jang Sam abruptly rose from Level 40 to Level 60, attacked Taekyung while apparently irrational, and is unconscious; his silk pouch from an unknown traveler in Hubei may have contained a modified Temporary Strength Pill.",
    "The Bow Saint wondered whether Pung Yang might have been the chosen one; the Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s hidden iron chest contained old bamboo slips, recent papers, and a small silk pouch of unknown significance."
  ],
  "continuity_sources": [
    950
  ],
  "open_questions": [
    "What will happen in the Shanxi campaign, and what role will Dark Heaven play in the fighting?",
    "Who gave Jang Sam the silk pouch, and what are the modified pill’s effects and side effects?",
    "How widely has the improved Temporary Strength Pill spread, and who is distributing it?",
    "What is the Martial God’s identity, and what is his connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain, and what is their significance?"
  ],
  "safe_through": 950,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살기     | **killing intent**                               |                                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 산서     | **Shanxi**             |
| 청해     | **Qinghai**            |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 평화 | **Peace Guild** | Guild name. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 게르 | **ger** | Traditional nomadic dwelling contrasted with Central Plains wooden buildings. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 전도 | **complete map of the realm** | Mae Jonghak's map marking terrain, place names, and sect locations. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |

## Listed compact profiles

### Chinggen.md

# Chinggen (칭겐)

- **Safe through:** Chapter 949
- **Aliases:** None
- **Role:** Chinggen is a Khan of the northern grasslands, ruling alongside Temur over tens of thousands of horses and warriors.
- **Personality:** Prudent, restrained, and attentive to the danger posed by the gathering's other powers
- **Voice:** Measured, familiar, and cautioning
- **Relationships:** Temur is his brother and fellow Khan; they shared life and death since childhood and brought peace and prosperity to the grasslands.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 950
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 950
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 950
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 949
- **Aliases:** None
- **Role:** Temur is a Khan of the northern grasslands, ruling alongside Chinggen over tens of thousands of horses and warriors.
- **Personality:** Hot-tempered, reckless, proud of his khan lineage, and inclined to dismiss distant threats while indulging in celebration.
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** Chinggen is his brother and fellow Khan; they shared life and death since childhood and brought peace and prosperity to the grasslands.

## Korean source

```text
＃951화



솨아아아.

갑작스럽게 쏟아지기 시작한 빗줄기에 모두가 바빠졌다.

날짐승들은 날개를 접고 종종걸음으로 풀숲에 숨었고, 먹이를 찾아 어슬렁거리던 들짐승들은 인적이 닿지 않는 동굴 안에 몸을 뉘었다.

지금 이 순간에도 쉼 없이 떨어지는 저 굵은 빗줄기로부터 체온을 지키기 위해.

그러나 이 광활한 초원의 한 축을 담당하고 있던 짐승들은 잠시 후 깨닫게 되었다.

항상 달갑지 않았던 저 자연의 산물이, 이번만큼은 자신들을 보이지 않는 위험으로부터 구했다는 것을.

드득. 드드득.

갑작스럽게 시작된 진동.

지면이 뒤흔들린다. 아니, 마치 초원 전체가 몸을 떨고 있다고 해도 과언이 아니었다.

곳곳에 숨어 있던 짐승들은 본능적으로 바짝 털을 곤두세웠다.

동시에 탄생과 함께 타고난 후각으로, 청각으로, 혹은 시력으로 보고 느꼈다.

한 치 앞도 보이지 않을 정도로 빽빽한 빗줄기 너머, 그들의 땅을 가로지르는 수많은 인마(人馬)의 무리를.

철퍽, 두두두두두!

흙탕물이 사방으로 튀었다. 흥건하게 고인 물웅덩이를 짓밟은 말발굽은 힘차게 전방을 향해 달려 나갔다.

그리고 끝없이 이어지는 거대한 무리의 선두에, 유독 눈에 띄는 두 사람이 있었다.

“도무지 그칠 기미가 안 보이는군.”

하늘을 바라보며 중얼거린 날렵한 체구의 사내가, 말머리를 나란히 한 채 달려가고 있던 거한을 향해 시선을 돌렸다.

“이보게, 테무르.”

갑작스러운 부름에 거한, 아니 테무르의 어깨가 움찔 떨렸다.

“으, 응?”

“속도를 좀 올려야겠네. 지체했다가는 사방이 온통 진창이 되고 말 거야.”

“그래, 그렇겠지.”

잔뜩 쉰 목소리로 고개를 끄덕이는 테무르의 모습에. 날렵한 체구의 사내가 미간을 좁혔다.

“그래서?”

“어?”

“그게 끝인가?”

“아.”

멍하니 눈을 깜빡이던 테무르가 이내 자신의 실수를 깨닫고 어딘가를 향해 손짓하자, 활과 돌격창으로 무장한 기병 수십이 바람처럼 달려와 고개를 숙였다.

“무슨 일이십니까, 테무르 칸.”

“휘하 모든 천인장들에게 전해라. 비가 그치기 전까지는 휴식 없이, 전력을 다해 이동할 것이라고.”

애써 준엄하게 명령을 내린 테무르가 날렵한 체구의 사내를 곁눈질하며 덧붙였다.

“만일 이 명을 소홀히 하는 자가 있다면, 나 테무르 칸과 여기 있는 칭겐 칸의 이름으로 엄벌할 것이다.”

“충!”

힘찬 군례와 함께 사방으로 흩어지는 기병들.

그제야 날렵한 체구의 사내, 칭겐의 미간이 펴졌다.

“그래, 응당 이래야지. 아주 잘했네.”

마른침을 꿀꺽 삼킨 테무르가 고개를 끄덕였다.

“칭찬 고맙군.”

“이제 자네도 칸으로서의 몫을 해내야 해. 언제까지 내가 옆에서 일일이 조언할 수는 없는 일 아닌가. 응? 내 자랑스러운 형제여.”

툭.

갑옷 위를 두드리는 칭겐의 손길에, 테무르의 신형이 흠칫 떨렸다.

“많이 추운가 보군. 괜찮나?”

“……물론. 아무 문제 없다.”

“아니야, 자네 마음은 누구보다 내가 잘 알고 있네. 형제여.”

나직이 한숨을 내쉰 칭겐이 문득 이를 악물었다.

“더럽고 비열한 족속들 같으니. 나는 놈들을 사로잡는 족족 갈기갈기 찢어 독수리 먹이로 던져 줄걸세.”

빗줄기 사이를 뚫고 울려 퍼진 칭겐의 목소리에, 두 사람의 주위에서 묵묵히 앞만 보고 내달리던 유목민들의 투구 사이로 살기 어린 눈빛을 번뜩였다.

그날의 참극(慘劇)은 이미 초원 전체에 모르는 이가 없었으니까.

테무르와 칭겐.

단숨에 동부 초원을 장악하여 평화와 번영을 가져다준 두 명의 젊은 칸은 각각 일백의 심복을 거느린 채 회동을 가졌다.

웃음소리로 가득하던 게르가 곧 피로 물 들것이라고는 꿈에도 생각지 못한 채.

“누가 알았겠나. 빌어먹을 한족 놈들이 그토록 끔찍한 흉계를 꾸미고 있을 줄은.”

물경 수백에 달하는 불청객들의 정체는 중원의 한족, 그중에서도 무림인이라 불리는 족속들이었다.

연회가 한창 무르익던 찰나 들이닥친 그들은 닥치는 대로 병장기를 휘둘렀다.

다행히 하늘의 도우심으로 두 칸은 살아남았으나, 치열한 혈투 끝에 그들이 거느렸던 심복 대부분은 피 웅덩이에 몸을 뉘어야 했다.

“친애하는 내 형제여. 텡그리께서 우리를 보살펴 주시지 않았다면, 동부 초원은 순식간에 갈기갈기 찢겨 저 한족 놈들의 손아귀에 떨어졌을 걸세.”

칭겐은 새하얗게 물든 손아귀로 말고삐를 힘껏 말아쥐었다.

“놈들이 무엇을 노렸는지는 뻔해. 각각 강력한 세력을 갖춘 우리가 위험이 될 거라 판단한 것이겠지. 마침내 감춰 두었던 야욕을 드러낸 거야.”

서늘하게 빛나는 칭겐의 눈빛에, 테무르가 쇳소리처럼 갈라진 목소리로 대꾸했다.

“나도, 나도 그렇게 생각해.”

“우리는, 아니 이 땅의 모두는 처음부터 놈들에게 이용당한 거였어. 저 비열하기 짝이 없는 족속들은 애초에 초원 전체를 손에 넣을 속셈이었겠지.”

끓어오르는 듯한 칭겐의 음성을 듣고 있던 유목민들은 약속이라도 한 것처럼 동시에 고개를 끄덕였다.

맞다. 한족들은 늘 그랬다.

아득한 과거부터 자신들을 오랑캐라 부르며 멸시하고, 짐승보다도 하찮게 여겼다.

위대한 선조들이 무수한 말발굽으로 중원을 짓밟고 거대한 제국을 세운 이후에도 그 사실은 변하지 않았다.

아니, 오히려 멸시를 넘어 증오마저 내비쳤다.

한낱 오랑캐 따위가 대륙의 역사에 오물을 흩뿌렸다는 이유로.

그러나 인간은 망각의 동물이다.

긴 세월이 흐르고, 선조들의 위업이 차츰 잊혀지자 그들은 새로운 것을 원하기 시작했다.

정복보다는 평화를.

말똥이 아닌 금은보화를.

아마도 그래서였을 것이다.

테무르와 칭겐. 황금 씨족의 혈통을 타고난 전도유망한 두 젊은이가 한족과 손을 잡았음에도 모두가 쌍수를 들고 환영했던 것은.

“내 실수였네.”

칭겐은 쏟아지는 빗줄기를 맞으며 탄식했다.

“놈들이 어떤 족속이었는지, 무엇을 위해 우리와 협력했는지 더 깊게 생각해 보지 못했어. 우두머리의 무지함과 어리석음으로 인해 고귀한 초원의 전사들이 희생당한 거야.”

슬픔과 후회로 가득한 그의 모습에 모두가 고개를 떨군 그 순간이었다.

“그 실수를 바로잡는다면, 초원의 전사들은 텡그리의 품에 안길 것이다.”

담담하면서도 힘 있는 목소리.

유목민 특유의 변발을 한 중년인의 모습을 발견한 칭겐이 눈을 크게 떴다.

“후미에 계셔야 할 자무카 칸께서 어찌 이곳까지…….”

“자무카 칸을 뵙습니다!”

칭겐을 시작으로 곳곳에서 터져 나오는 외침.

항거할 수 없는 힘이 실린 눈빛으로 모두를 쓸어보던 중년인, 자무카가 입을 열었다.

“후방에만 있으니 따분해서 말이야. 이 늙은이가 도움이 될 일이 없나 해서 와 봤지.”

귀밑머리는 밤처럼 까맣고, 당당한 풍채는 한창때의 젊은이보다도 강건하다.

그러나 그것은 단순히 보이는 모습일 뿐. 자무카는 이미 여든을 훌쩍 넘긴 노인이기도 했다.

초원 제일의 전사이자, 오랜 세월 동안 서부 초원을 통치해온 또 한 명의 칸.

자그마치 이 만여 명이 넘는 부족민들을 이끌고 합류한 그는, 이 거대한 군세를 이끄는 실질적인 수장이었다.

“늙은이라니요. 감히 누가 그런 생각을 하겠습니까. 안 그런가, 테무르?”

떨리는 눈빛으로 자무카를 바라보던 테무르가 황급히 고개를 끄덕였다.

“마, 맞습니다.”

“자무카 칸께서는 우리 황금 씨족의 웃어른이시자, 위대한 전사이며 칸이십니다. 저희에게 선봉을 맡겨 주신 것만으로도 감사할 따름이지요.”

칭겐은 주위의 모두가 들을 수 있도록 목소리를 높여 말을 이었다.

“멍청한 한족 놈들은 죽어 가는 그 순간까지도 몰랐을 겁니다. 자무카 칸께서 얼마나 강한 분인지.”

구태여 말하지 않더라도, 자무카를 바라보는 시선들은 이미 흠모와 경애로 가득했다.

초원 제일의 전사. 자무카.

알려진 바에 따르면 그는 테무르와 칭겐보다 앞서 수백에 달하는 한족들의 습격을 받았다고 했다.

고작 십여 기의 친위대만 거느린 상황에서.

하지만 그 결과는 엄청났다.

자무카는 자신의 무용을 똑똑히 증명했다.

적들에 비하면 한 줌밖에 되지 않는 친위대를 거느리고, 무수한 한족들을 상대로 학살극이나 다름없는 전투를 펼친 것이다.

결국 서부 초원마저 위협한 한족들의 흉계는 수포로 돌아갔고, 분노한 자무카는 휘하의 부족을 이끌고 중원으로 말머리를 향했다.

지금 이 순간처럼.

“별것 아닌 일이다. 수하들의 솜씨가 뛰어났을 뿐이지.”

담담하게 대꾸한 자무카가 등 뒤를 턱짓했다. 거무스름한 갑옷을 걸친 친위대가 무미건조한 표정으로 그의 뒤를 쫓아 달리고 있었다.

아득한 과거, 유목 제국의 기틀을 마련했던 위대한 정복자가 탄생시킨 최정예 전사들.

이른바 ‘케식’이라 불리는 그들은 여전히 황금 씨족의 잔재로서 자무카를 따르고 있었다.

한 사람, 한 사람이 각 부족을 대표하는 전사와 맞먹는 강자들.

그런 이들이 무려 일천에 달한다.

물경 수만을 아우르는 초원의 대군세가 승리를 확신하는 것은, 단순한 희망으로 말미암은 것이 아니었다.

“지금부터는 내 친위대 중 일부가 선봉에 설 것이다.”

“케식을…… 말씀이십니까?”

“그래. 무슨 문제라도 있느냐?”

생각지도 못한 자무카의 말에 잠시 침묵하던 칭겐이 이내 고개를 저었다.

“그럴 리 있겠습니까. 저희로서는 오히려 부탁드릴 일이지요. 안 그런가, 테무르?”

“……그렇지. 나 역시 동의한다.”

가장 강한 전사들이 선봉에 선다.

어찌 보면 당연한 결정에 모두가 납득했다.

단 한 사람만 빼고.

- 그래도 되겠습니까?

불현듯 귓가를 파고드는 누군가의 전음에, 자무카가 입술을 달싹였다.

- 조금 전에는 오히려 부탁드릴 일이라고 하지 않았나?

- 그건…….

- 번복은 없다. 저 아이들을 선봉에 세워 최단 시간 안에 국경을 넘을 것이다.

- 함정이 있을 수도 있습니다. 사방에 화살받이들이 널리고 널렸는데, 굳이 귀한 전력을 낭비할 이유가 있겠습니까?

- 함정이라면 무엇을 말하는 것이냐. 며칠 뒤에나 산서성에 도착할 화왕과 진태경? 아니면 보잘것없는 산서성 놈들?

무뚝뚝하게 대답한 자무카가 전음의 주인을 똑바로 응시했다.

- 네놈은 옆에 있는 그 얼간이나 제대로 단속하거라. 그때 죽이지 않았던 것이 슬슬 후회되려던 참이니.

- 제가 말씀드렸잖습니까. 차라리 머리가 잘 굴러가는 놈을 살리자고.

아무도 알아채지 못할 만큼 흐릿하게 실소를 흘린 칭겐, 아니 그의 모습을 한 누군가가 자신의 얼굴을 쓰다듬었다.

- 그놈 참, 어떤 의미로는 대단하긴 했습니다. 사방에서 수하들이 죽어 가는 와중에도 협상을 시도했으니.

그는 똑똑히 기억하고 있었다.

항거할 수 없는 무력의 차이에 굴복하여 오줌까지 지리던 테무르의 옆에서, 원하는 것을 말하라며 기개를 내보이던 칭겐의 모습을.

- 죽은 그놈에 비하면 이 멍청한 녀석은…….

- 멍청해서 살려 둔 것이다. 마음 깊이 굴복한 놈은 그만큼 다루기 쉬우니까.

- 그 부분은 인정합니다. 놈이 따라 준 덕분에 생각했던 것보다도 훨씬 많은 오랑캐들이 모였으니까요.

웃음기 어린 눈빛이 초원을 가득 메운 대군세를 훑었다.

이제 남은 거리는 불과 하루 남짓.

이 비가 그칠 때, 그들은 초원을 지나 성벽을 넘을 것이다.
```

## Final English reading copy

```markdown
# Chapter 951

*Whoosh…*

The sudden downpour sent everything into a flurry of activity.

Birds folded their wings and hurried into the grass. Beasts that had been prowling for food lay down inside caves, far from any human footsteps.

They were trying to preserve their body heat against the thick sheets of rain that kept falling without pause.

But the animals that inhabited this vast stretch of grassland would soon realize something.

For once, the ever-unwelcome gift of nature had saved them from an unseen danger.

*Rumble. Rrrumble.*

A sudden vibration.

The earth shook. No—it wouldn’t have been an exaggeration to say the entire grassland was trembling.

The animals hidden here and there instinctively bristled, every hair standing on end.

At the same time, with the senses they had been born with—their noses, their ears, their eyes—they saw and felt it.

Beyond the dense sheets of rain, so thick they couldn’t see an inch ahead: countless riders crossing their land.

*Splash! Thududududu!*

Mud sprayed in every direction. Hooves trampled through puddles of standing water as the horses charged forcefully onward.

At the head of the enormous, seemingly endless column, two men stood out.

“It doesn’t look like it’s going to let up.”

The lean man muttered as he gazed at the sky, then turned to the hulking man riding beside him.

“Temur.”

At the sudden call, the hulking man—Temur—flinched.

“Y-yes?”

“We should pick up the pace. If we delay, the whole area will turn into a quagmire.”

“Yes. I suppose so.”

Temur nodded in a hoarse voice. The lean man furrowed his brow.

“And?”

“Hm?”

“Is that all?”

“Oh.”

Temur blinked blankly, then realized his mistake. He gestured toward somewhere, and dozens of cavalrymen armed with bows and lances came galloping over like the wind. They bowed their heads.

“What is it, Khan Temur?”

“Tell every chiliarch under my command: no rest until the rain stops. We move at full speed.”

Temur forced himself to issue the order sternly, then added with a sidelong glance at the lean man beside him,

“Anyone who neglects this order will be severely punished in the name of me, Khan Temur, and Khan Chinggen here.”

“Understood!”

The cavalrymen scattered in every direction with a spirited salute.

Only then did the furrow between Chinggen’s brows ease.

“Good. That’s how it should be. Well done.”

Temur swallowed dryly and nodded.

“Thanks for the praise.”

“Now it’s time for you to do your part as a khan. I can’t stand beside you and give you every little piece of advice forever, can I? Right, my proud brother?”

*Tap.*

At Chinggen’s hand patting his armor, Temur’s body gave a start.

“You look terribly cold. Are you all right?”

“…Of course. Nothing’s wrong.”

“No. I know your heart better than anyone, brother.”

Chinggen let out a quiet sigh, then suddenly clenched his teeth.

“What filthy, despicable bastards. Every last one I capture, I’ll tear limb from limb and toss to the eagles.”

Chinggen’s voice rang through the rain. The nomads racing silently around them, their eyes fixed ahead, flashed killing intent in their eyes beneath their helmets.

Everyone across the grasslands already knew of the massacre that had taken place that day.

Temur and Chinggen.

The two young khans had seized the eastern grasslands in a single stroke, bringing peace and prosperity. Each had been accompanied by a hundred trusted retainers when they met.

Neither had dreamed that the ger, once filled with laughter, would soon be drenched in blood.

“Who could have known those damned Han Chinese would hatch such a horrifying plot?”

The uninvited guests—several hundred of them—were Han Chinese from the Central Plains. They were the sort known as Murim martial artists.

They had burst in at the height of the feast and swung their weapons at anyone in reach.

By the grace of heaven, the two khans had survived. But after a fierce battle, most of the retainers under their command had been left lying in pools of blood.

“My dear brother. If Tengri hadn’t watched over us, the eastern grasslands would have been torn apart in an instant and fallen into the hands of those Han Chinese.”

Chinggen gripped his reins tightly in his whitened hand.

“It’s obvious what they were after. They must have judged that we’d become a threat, with each of us commanding a powerful force. At last, they’ve shown the ambition they’d kept hidden.”

At the cold light in Chinggen’s eyes, Temur answered in a voice rough as iron.

“I—I think so too.”

“It wasn’t just us. Everyone on this land was being used by them from the very beginning. Those despicable bastards were planning to seize the entire grassland all along.”

The nomads listening to Chinggen’s seething voice nodded together, as if they’d agreed to do so.

That was right. The Han Chinese had always been like that.

Since time immemorial, they had called them barbarians, scorned them, and thought them worth less than beasts.

Even after their great ancestors had trampled the Central Plains beneath countless hooves and built a vast empire, nothing had changed.

No—instead of mere contempt, they had come to show hatred.

All because a mere band of barbarians had sullied the history of the continent.

But human beings were creatures of forgetfulness.

As the years stretched on and the achievements of their ancestors gradually faded from memory, they began to want something new.

Peace, instead of conquest.

Gold and silver, instead of horse manure.

Perhaps that was why everyone had welcomed the two promising young men of the Golden Clan with open arms when they joined forces with the Han Chinese.

Temur and Chinggen.

“It was my mistake.”

Chinggen lamented as the rain poured down on him.

“I should have thought more deeply about what kind of people they were, and why they’d agreed to work with us. Noble warriors of the grasslands died because their leader was ignorant and foolish.”

At the sight of his grief and regret, everyone lowered their heads.

Then came a calm, powerful voice.

“If you correct that mistake, the warriors of the grasslands will be welcomed into Tengri’s embrace.”

Chinggen’s eyes widened as he spotted a middle-aged man with the distinctive braided hairstyle of the nomads.

“Why is Khan Jamukha here? You should be in the rear…”

“Greetings, Khan Jamukha!”

Exclamations erupted in every direction, beginning with Chinggen.

The middle-aged man, Jamukha, swept his gaze over them, his eyes imbued with an irresistible force, then spoke.

“It was dull staying in the rear. I thought this old man might be of some help, so I came to see.”

His hair was as black as night at the temples, and his imposing build was more robust than that of a young man in his prime.

But that was only what he looked like. Jamukha was well over eighty years old.

The greatest warrior on the grasslands, and another khan who had ruled the western grasslands for many years.

He had joined the army with more than twenty thousand tribespeople. In practice, he was the one leading this immense force.

“Old man? Who would dare think that of you? Isn’t that right, Temur?”

Temur gazed at Jamukha with trembling eyes, then hurriedly nodded.

“Y-yes.”

“Khan Jamukha is our elder in the Golden Clan, a great warrior and a khan. We’re grateful just to have been entrusted with the vanguard.”

Chinggen raised his voice so everyone around them could hear.

“Those foolish Han Chinese probably never knew how strong Khan Jamukha was—not even as they were dying.”

Even without a word from Chinggen, the looks fixed on Jamukha were already full of admiration and reverence.

Jamukha, the greatest warrior on the grasslands.

According to what people knew, he had been attacked by several hundred Han Chinese before Temur and Chinggen were.

He had only a dozen or so personal guards with him.

But the outcome had been staggering.

Jamukha had proved his prowess beyond doubt.

With a mere handful of guards—barely a match for the enemy numbers—he had fought a battle against the Han Chinese that was little short of a massacre.

In the end, the Han Chinese plot that had threatened even the western grasslands came to nothing. Enraged, Jamukha had led his tribes south toward the Central Plains.

Just as he was now.

“It was nothing. My men were simply skilled.”

Jamukha answered calmly and jerked his chin over his shoulder. His personal guards, clad in dark armor, galloped after him with expressionless faces.

They were the elite warriors created by the great conqueror who had laid the foundations of the nomadic empire in the distant past.

Known as the *Keshik*, they still followed Jamukha as remnants of the Golden Clan.

Each one was as strong as the finest warrior in any tribe.

And there were a thousand of them.

The immense grassland army, numbering tens of thousands, wasn’t confident of victory on nothing but hope.

“From here on, some of my personal guards will take the vanguard.”

“The Keshik, you mean?”

“Yes. Is there a problem?”

Chinggen fell silent for a moment at Jamukha’s unexpected words, then shook his head.

“Of course not. We’d be the ones asking you. Isn’t that right, Temur?”

“…That’s right. I agree.”

The strongest warriors would lead the charge.

It was an obvious decision, and everyone accepted it.

Everyone but one person.

*Are you sure that’s wise?*

At the sudden Sound Transmission that pierced his ear, Jamukha’s lips moved.

*Didn’t you just say you’d be the one asking me?*

*Well…*

*I won’t change my mind. We’ll put those children in the vanguard and cross the border in the shortest time possible.*

*There could be a trap. The place is crawling with fodder to take arrows for us. Why waste precious forces?*

*What trap are you talking about? Fire King and Jin Taekyung, who won’t reach Shanxi Province for several days? Or those insignificant Shanxi fools?*

Jamukha answered bluntly and stared directly at the source of the Sound Transmission.

*You’d better keep that idiot beside you under control. I’m starting to regret not killing him back then.*

*I told you we should’ve spared the smarter one instead.*

Chinggen—or someone wearing his face—let out a faint, nearly imperceptible chuckle and ran a hand over his own features.

*That man was impressive, in a way. He tried to negotiate even as his men were dying all around him.*

He remembered it clearly.

Beside Temur, who had surrendered before an overwhelming difference in strength and even wet himself, Chinggen had shown his mettle, telling them to name what they wanted.

*Compared to that dead man, this idiot…*

*I kept him alive because he’s an idiot. Someone who’s surrendered deep in his heart is that much easier to handle.*

*I’ll grant you that. Thanks to his cooperation, far more barbarians gathered than I expected.*

His amused gaze swept across the vast army that filled the grasslands.

Only about a day remained.

When the rain stopped, they would cross the grasslands and pass over the fortress walls.
```
