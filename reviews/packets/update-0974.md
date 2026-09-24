<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0974.txt",
      "sha256": "6545764558e00cbda124f0d1016adf6d8f42d3b0abc397fd119e0abc968a7c96",
      "bytes": 12981
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c5f12d68ef6210a93d94b07bd159943a89e45ffd280b38b713774ed4fd5b77cc",
      "bytes": 1085
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "65892110351fce017f8020b13720d8c5e71418799da1db239060ea308ecc01e4",
      "bytes": 235501
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b920306551efb6be27199ddd53334649c9b6fab37155ccf0816bd960fa71b566",
      "bytes": 759
    },
    {
      "path": "characters/Jamukha.md",
      "sha256": "da6f4f738d6bae26899c5301b58a9e935d0005a9667f50f09f4a0c856b8ffb9f",
      "bytes": 574
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "c76226e37cf6fd4c47c0c9124b75a194d5f30ce97a51df8e044d4d98f66d16f2",
      "bytes": 1254
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "395c0b693964329e59e669576c63e8ae30e2817e1989efae308fa70e59ab2c6d",
      "bytes": 1481
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1aef821bd0dc4ccd7a1fe9f6ba83736ec4f8ebc6d1a14aadbb5bf7a6b450efc7",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4ab770334cae05e602b597ac621bf33ba47f4c3e433b466c45967edfdcdd594f",
      "bytes": 271188
    }
  ],
  "estimated_tokens": 10306
}
-->

# Durable State Update — Chapter 974

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
1 and safe_through 974. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 974. Profile updates may replace only one
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
  "chapter": 974,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 974,
    "continuity_sources": [974],
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
    "The Bow Saint has left the gorge to aid the Hebei Peng Family, where roughly two thousand fighters remain and pill-enhanced Keshiks have broken their formation.",
    "The North Heaven Demon Lord is Murong Baek, Jeok Cheongang’s former battlefield comrade; their confrontation has resumed, and Taekyung and Jeok have repelled the first attacks.",
    "The conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu remain unknown.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved."
  ],
  "continuity_sources": [
    972,
    973
  ],
  "open_questions": [
    "Can the Hebei Peng Family withstand the pill-enhanced Keshiks?",
    "How will the renewed confrontation with Murong Baek unfold?",
    "What are the conditions of Jin Mukyung, Cheol Mubaek, Wipeng, and Peng Cheolhu?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 973,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무림맹    | **Murim Alliance**               |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 산서     | **Shanxi**             |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 노부      | **this old man / I**                                            |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 백염 | **White Flame** | Name of Jin Taekyung's newly forged spear. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 계도 | **precept blades** | Blades carried by the Hundred and Eight Arhats. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 칠공 | **seven apertures** | The seven bodily openings through which Taekyung's overflowing heat escapes. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 북천마군 | hostile opponents | you | casual, taunting, and profane | Taekyung teases and insults him during their standoff. |
| 적천강 | 북천마군 | former battlefield adversaries | you; you pup | blunt, familiar, and taunting | Jeok addresses him informally while challenging his alliance with Dark Heaven. |
| 북천마군 | 자무카 | lord to subordinate | my lord | formal-deferential | Jamukha answers the Demon Lord’s command with 하명하십시오. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 973
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jamukha.md

# Jamukha (자무카)

- **Safe through:** Chapter 972
- **Aliases:** None
- **Role:** Jamukha is the ruler of the western steppe and a former eastern-steppe chieftain recruited into Dark Heaven by Murong Baek.
- **Personality:** Patient and driven by a long-standing desire to avenge his defeat by Peng Cheolhu.
- **Voice:** Not established
- **Relationships:** Peng Cheolhu defeated him more than fifty years ago; Murong Baek spared him, recruited him into Dark Heaven, and commands him as a subordinate.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 973
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 973
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and learning to trust his allies rather than carry every burden alone.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 973
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃974화



살다 보면 종종 내 진심이 상대방에게 닿지 않을 때가 있다.

생각지도 못한 오해를 불러일으켰다는 건 슬픈 일이지만, 한편으로는 어쩔 수 없는 일이다.

애초에 대화로 풀어낼 관계도 아니었으니.

“그 아가리를…….”

차마 끝맺지 못하고 흩어지는 숨소리.

분노로 인해 머리가 어질어질해진 듯한 교수님. 아니, 북천마군이 일그러진 얼굴로 호흡을 가다듬었다.

척 봐도 힘겨워 보이는 놈을 대신해, 내가 먼저 입을 열었다.

“찢어 주마.”

“뭐?”

“원래 하려던 말이 그거 아니야? 많이 들어봐서 잘 알아.”

순간 할 말을 잃은 표정으로 나를 바라보던 북천마군이 이를 악물었다.

“입 다물어.”

“아니, 그래도 사람이 할 말은 하고 살아야지. 아무리 양심 없는 약쟁이 새끼여도.”

“입 다물라고 했다.”

“그런데 지금까지 하도 많이 들었던 대사라 어쩐지 좀 심심하게 느껴지네. 두 번 다시 그 방정맞은 혓바닥을 놀릴 수 없도록 아가리를 찢어 주마. 이러면 좀 맛이 살지 않나.”

“도무지…… 말로 해서는 안 될 놈이로군.”

“힘으로 해도 안 될걸. 나한테 그 말 했다가 죽은 애들이 사열 종대 앉아 번호로 무림맹 연무장 두 바퀴야.”

옆에 있던 적천강이 덧붙였다.

“참고로 노부는 열 바퀴가 넘는다.”

“그거야 저보다 훨씬 오래 사셨으니까 그렇죠.”

“꼬우면 네놈도 무병장수하든지.”

“유병장수 하셨잖아요. 기억 안 나세요? 저랑 처음 만났을 때만 해도…….”

슈확!

이어지려던 목소리를 집어삼키는 파공성.

한 치의 망설임도 없이 본능에 따라 고개를 숙이자, 빛살과도 같은 속도로 날아든 한 자루의 비수가 머리 위를 스쳐 암벽을 강타했다.

콰앙!

마치 포탄과도 같은 위력.

그러나 아무리 강력한 힘이 실린 공격이라고 해도 맞지 않으면 그만이다.

충격파와 함께 튀어 오른 돌가루를 툭툭 털어 낸 나는, 비수를 쏘아 보낸 북천마군을 동그랗게 뜨인 눈으로 바라보았다.

“와, 하마터면 맞을 뻔.”

“……!”

“약 빨아서 그런지 확실히 세긴 엄청 세네. 노야, 이거 저 혼자서는 일대일로 붙어도 절대 안 되겠는데요?”

적천강이 눈살을 찌푸렸다.

“그걸 말이라고 하느냐? 당연히 안 되지. 지금까지 해 왔던 대로만 해도 최소…… 일이 년 뒤쯤이라면 어느 정도 가능성이 있겠지만.”

고작 일 이 년.

내 과거와 가장 깊은 비밀까지 알고 있는 적천강으로서는 상당히 합리적인 결론이었지만, 듣고 있던 누군가에게는 참을 수 없는 모욕이나 다름없다.

“자무카.”

북천마군의 얼굴에는 더 이상 분노가 보이지 않았다. 낮게 가라앉은 그의 목소리에, 늙은 유목민이 고개를 숙였다.

“하명하십시오.”

“오래전, 나와 했던 약속을 기억하느냐?”

“단 한 순간도 잊어 본 적 없습니다.”

“그렇다면 목숨을 걸어라.”

“……!”

“살아남기만 한다면 광활한 초원에 더하여 하북을 네게 줄 것이다. 팽가(彭家)가 가졌던 모든 것을, 놈들의 목숨마저 맡기겠다.”

늙은 유목민, 자무카의 눈꺼풀이 파르르 떨렸다.

“그것이야말로 속하가 지금껏 살아온 이유입니다.”

“하면 너는 내게 무엇을 주겠느냐.”

“오늘의 승리를, 열화신룡 진태경의 목을 바치겠습니다.”

“그래. 그것이 내가 원했던 대답이다.”

저벅. 스아아아아.

무겁게 내디딘 발걸음과 함께, 아지랑이처럼 피어오르던 검붉은 기운이 운무(雲霧)가 되어 자욱하게 맺혀간다.

마침내 모든 전력을 한 방울도 남김없이 끌어 올린 두 사람의 모습에, 적천강이 담담하게 입을 열었다.

“태경아.”

“말씀하세요.”

“오래전, 노부와 했던 약속을 기억하느냐?”

나는 망설임 없이 대답했다.

“아뇨.”

“…….”

“그리고 뭐가 오래전이에요. 처음 만났을 때라고 해봤자 꼴랑 이 년 전인데.”

잠시 침묵하던 적천강이 한숨을 내쉬었다.

“이럴 때 장단 좀 맞춰 주면 칠공에서 피를 뿜어내며 뒈지는 병이라도 걸렸느냐?”

“장단 맞춰 봤자 뭐합니까. 애초에 잘 맞지도 않는 거, 차라리 저 새끼들 한 대라도 더 때려 맞추는 게 훨씬 낫죠.”

“음. 그건 부정하기 힘들구먼.”

“그냥 하던 대로 하세요. 화왕(火王)답게.”

천천히, 그리고 신중하게 접근해 오는 북천마군과 자무카에게 고정되어 있던 적천강의 시선이 나를 향해 움직였다.

“왜요. 아직 하실 말씀 남았습니까?”

“아니, 별것 없다. 그저 네 녀석을 제자로 받아들인 것이 옳은 선택이라는 생각이 문득 들었을 뿐이다.”

순간 무슨 말을 해야 할지 몰라 입을 다문 내 귓가로, 적천강의 나직한 목소리가 닿았다.

“우리 사이에 낯간지럽게 뭔가를 약속한 적은 없지만, 언제나 그렇듯이 하나만 명심하거라.”

“명심이라면 어떤…….”

“노부는 항상 네 곁에 있다.”

“……!”

“그러니 목숨 걸고 싸우는 멍청한 짓거리 따위는 하지 마라. 설령 염라(閻邏)가 네게 찾아온다 해도 노부가 엉덩이를 걷어차 쫓아 버릴 것인즉.”

알면 알수록 참으로 희한한 일이다.

똑같이 피륙으로 이루어진 한 명의 인간일진대, 그 생각이 이다지도 다르다는 것은.

누군가는 상대가 원하는 것을 내어주는 대신 목숨을 바치라 하고, 다른 누군가는 아무것도 필요 없으니 그저 살아남으라 한다.

그리고 그것은 곧, 내가 적천강에게 하고 싶은 말이기도 했다.

“그 약속 지키면, 저한테 뭘 주시렵니까?”

한 걸음, 또 한 걸음.

두 적수의 발걸음과 함께 가까워질수록 짙어지는 검붉은 안개를 바라보며 던진 한마디에, 적천강이 헛웃음을 흘렸다.

“이런 천하의 양심 없는 놈 같으니. 그래, 무엇을 원하느냐?”

“별거 아닙니다. 이미 한 번 아프셨으니 무병장수는 글렀고, 앞으로라도 꼭 유병장수 하시라고요.”

“이 나이에 장수라. 앞으로 백 년은 족히 더 살아야 할 이유가 생겼군.”

적천강은 무척 기꺼워하며 너털웃음을 터트렸다.

활짝 펼쳐진 그의 양손에 맺힌 새하얀 광염(光焰)이, 백염의 창날 위로 넘실거리는 청백색 화염과 함께 깊은 밤의 냉기를 불태웠다.

화아아.

같지만 다른 두 개의 화염에 녹아내리는 어둠 너머.

나는. 아니, 우리는 불길하리만치 자욱한 검붉은 안개를 향해 약속이라도 한 듯 동시에 걸음을 내뻗었다.

쐐애애액!



* * *



핏물처럼 붉고, 소름 끼치도록 짙은 운무(雲霧)를 마주한 이들은 하나 같이 등골 깊숙이 스며드는 한기를 느끼고 걸음을 멈추었다.

아니, 멈출 수밖에 없었다.

이성보다 먼저 본능으로 알아 버렸으니까.

‘가까이 다가간다면, 죽는다.’

지켜보는 것만으로도 느껴지는 섬뜩함.

안개처럼 자욱하게 내리깔린 저것은 극도로 유형화된 기운이었고, 들어가는 즉시 전신을 갈기갈기 베고 찢어 낼 창칼의 숲이나 다름없었다.

그러나 수많은 산서인들의 발이 묶인 가장 큰 이유는, 저 위험한 공간 안에서 벌어지고 있을 무시무시한 전투였다.

콰광! 콰아아아!

경천동지(驚天動地)라는 단어보다 이 상황을 더욱 잘 표현할 수 있는 말이 있을까.

살아 있는 생물처럼 꿈틀거리는 안개 너머에서, 네 명의 초절정 고수는 섬광과도 같은 속도로 서로를 향해 뒤얽히고 있었다.

한 치의 쉴 틈 없이.

바로 지금 이 순간에도.

서걱!

단단한 지면을 두부처럼 베어 내는 강기.

아슬아슬하게 북천마군의 일격을 피한 적천강이 손을 그러쥐었다.

되찾은 젊음으로 주름살이 사라진 그의 주먹 위로 새하얀 광염이 넘실거렸다.

화아악!

멸염신권(滅炎神拳).

장장 일백 년이 넘는 수련을 거쳐 마침내 십 성에 도달한 거대한 화염이 터져 나온다.

허공을 물들이며 눈앞의 적을 향해, 북천마군을 향해 쏘아졌다.

콰아아앙!

압축된 공기가 겹겹이 터져 나갔다.

그러나 땅이 녹아내리고 암벽이 뒤흔들리는 그 엄청난 충격 속에서도, 마지막 순간 흐릿해진 북천마군의 신형은 어디에서도 찾아볼 수 없었다.

정확히는, 한계가 명백한 인간의 시력으로는 그랬다.

솨악.

나지막하게 귓가를 파고드는 아주 작고 미세한 파공성.

하지만 소리를 넘어선 움직임은 청각마저 속인다는 것을, 적천강은 이미 잘 알고 있었다.

‘위!’

느껴진다.

자신의 머리 위, 보이지 않는 허공에서 내리꽂히는 상대방의 인기척이.

그와 동시에 바람을 지우며 내뻗어진 창날에 실린 막대한 강기가.

퍼어엉!

적천강은 망설임 없이 쌍장(雙掌)을 떨쳤다.

일순간 사방을 휘감은 검붉은 안개가 흩어졌다.

전력을 다한 화염신장(火焰神掌)이 불기둥이 되어 솟아올랐다.

최대한 인기척을 지우려 했으나, 완전히 감추기에는 너무나도 거대한 기운을 지닌 적수를 향하여.

그리고 다음 순간, 적천강은 새삼 깨달았다.

잠력단의 힘까지 빌린 지금의 북천마군은, 몇 번의 깨달음 끝에 현재의 경지에 도달한 자신마저 반 수 아래로 내려다보는 대적(大敵)이라는 사실을.

슈확!

정확히 일점(一點)을 관통한 창날.

그 끝에 실린 거대한 강기에 온 천하를 불사를 것만 같던 화염이 갈라지고, 두 사람 사이에 존재했던 모든 거리마저 사라졌다.

“……!”

너무나도 압도적인 그 힘에, 적천강의 눈이 크게 뜨였다.

이건 무공의 깨달음에 관한 문제가 아니다.

선천지기(先天眞氣)를 모조리 끌어낸 것은 아닐까 의심이 될 정도로 강대한 공력이, 거기에 더하여 극도로 향상된 북천마군의 움직임이 모든 것을 가능케 만들고 있었다.

‘빌어먹을.’

튀어나오려는 욕설을 삼키며, 적천강은 온 힘을 다해 전신의 공력을 끌어 올렸다.

정확히 그의 가슴을 노리고 내리꽂히는 창날을 향해 양손을 부딪쳤다.

콰드드득!

합장(合掌)하듯 맞물린 손바닥 사이에서 창날이 파르르 몸을 떨었다.

호신강기로도 완전히 막아 내지 못한 검붉은 강기가 살과 뼈를 헤집자, 적천강은 고통을 참기 위해 이를 악물어야 했다.

으득.

어금니가 부서지는 고통 따위는 시시각각 엉망이 되어 가는 양손에서 전해지는 것에 비하면 아무것도 아니다.

울컥 솟구치는 핏물을 삼키며 창날을 붙잡은 적천강의 모습에 북천마군이 이빨을 드러내며 웃었다.

“이제 그만하고 편히 쉬지 그러나. 많이 힘들어 보이는데.”

적천강의 악문 잇새 사이로 비웃음 섞인 목소리가 흘러나왔다.

“지금 그 말, 그대로 돌려주지.”

북천마군의 눈동자가 깊게 가라앉았다.

적천강의 말이 단순한 허세가 아니라는 것쯤은, 그 또한 전신으로 느끼고 있었기 때문이었다.

‘뭐 이런 괴물 같은 늙은이가.’

콰득. 콰드드득.

분명 전력을 다하고 있음에도 더 이상 나아가지 못하는 창날.

강기에 의해 살갗이 뭉개지면서도 지면 깊숙이 틀어박힌 발끝은 미동조차 없다.

수십여 년이나 젊어져서 돌아온 구화산의 노괴(老怪)는, 북천마군이 기억하는 과거보다도 훨씬 강해져 있었다.

잠력단을 복용한 지금에도 쉽게 쓰러트리지 못할 정도로.

‘하지만…….’

그것도 여기까지다.

머릿속의 생각을 완성함과 동시에, 북천마군은 창 자루를 비틀었다.

자신이 발휘할 수 있는 온 힘을 다해서.

제아무리 적천강이라 하더라도 이번만큼은 고통을 참을 수 없을 정도로.

콰직.

섬뜩한 파육음과 함께 적천강의 신형이 잘게 떨린 그때, 자무카의 입술 사이로 천둥 같은 고함이 터져 나왔다.

“자무카!”

그 순간.

콰앙! 쉭!

굉음과 함께 예리하기 그지없는 한 줄기의 바람이, 적천강의 등 뒤를 향해 쏘아졌다.
```

## Final English reading copy

```markdown
# Chapter 974

Sometimes, no matter how you live, your true feelings just don’t reach the other person.

It was sad to cause a misunderstanding you’d never intended, but in a way, it couldn’t be helped.

It wasn’t the kind of relationship you could fix by talking in the first place.

“That mouth of yours…”

The words died before he could finish, leaving only a breath that scattered into the air.

The professor—or rather, the North Heaven Demon Lord—seemed dizzy with rage. His face twisted as he steadied his breathing.

I spoke first, taking the words right out of the mouth of a guy who looked like he was struggling.

“I’ll tear it open.”

“What?”

“That’s what you were going to say, right? I’ve heard it plenty of times. I know.”

The North Heaven Demon Lord stared at me, momentarily at a loss for words, then clenched his teeth.

“Shut up.”

“Come on. People should be able to say what they want. Even if they’re shameless pill-popping bastards.”

“I said shut up.”

“But I’ve heard that line so many times, it’s starting to feel a little stale. ‘I’ll tear your mouth open so you can never wag that unruly tongue again.’ Doesn’t that have a bit more flavor?”

“You’re truly impossible to deal with using words.”

“You won’t manage with force, either. The guys who said that to me and died could line up in a column, count off, and stretch twice around the Murim Alliance training ground.”

Jeok Cheongang, standing beside me, added, “For the record, mine would stretch more than ten times around.”

“That’s because you’ve lived a lot longer than me.”

“If you don’t like it, then live a long, healthy life yourself.”

“You lived a long, sickly life. Don’t you remember? When I first met you…”

*Fwoosh!*

A sharp whistle swallowed the words that were about to follow.

I ducked on instinct, without a moment’s hesitation. A dagger shot past overhead at the speed of a streak of light and slammed into the cliff face.

*KABOOM!*

It hit with the force of a cannonball.

But no matter how much power an attack carried, it didn’t matter if it missed.

I brushed off the grit that had jumped up with the shock wave and stared wide-eyed at the North Heaven Demon Lord, who had thrown the dagger.

“Wow. That almost hit me.”

“……!”

“Those pills really do make you strong. Old Master, I don’t think I could take him one-on-one by myself.”

Jeok Cheongang frowned. “Do you even need to ask? Of course you couldn’t. If you keep doing what you’ve been doing, you might have a chance in a year or two.”

Only a year or two.

Considering Jeok Cheongang knew my past and even my deepest secrets, that was a fairly reasonable assessment. But to someone listening, it was an intolerable insult.

“Jamukha.”

There was no anger left on the North Heaven Demon Lord’s face. At his low voice, the old nomad bowed his head.

“Give your command.”

“Do you remember the promise we made long ago?”

“I have never forgotten it for a single moment.”

“Then stake your life on it.”

“……!”

“If you survive, I’ll give you Hebei along with the vast grasslands. Everything the Peng Family possessed—even their lives—I’ll put in your hands.”

The old nomad, Jamukha, trembled.

“That is the very reason I have lived until now.”

“Then what will you give me?”

“Today’s victory. And the head of Jin Taekyung, the Blazing Flame Divine Dragon.”

“Yes. That is the answer I wanted.”

*Step. Shhhhh…*

As he took a heavy step, the dark crimson energy rising around him like heat haze gathered thickly, turning into mist.

The two men had finally drawn out every last drop of their strength. Watching them, Jeok Cheongang spoke calmly.

“Taekyung.”

“Yes?”

“Do you remember the promise we made long ago?”

I answered without hesitation. “No.”

“……”

“And what do you mean, ‘long ago’? It’s only been two years since we first met.”

Jeok Cheongang fell silent for a moment, then sighed.

“Do you have some kind of disease that makes blood gush from your seven apertures and kills you if you play along at a time like this?”

“What’s the point of playing along? We can’t even get our timing right. It’s much better to land one more hit on those bastards.”

“Hmm. Hard to argue with that.”

“Just do what you’ve always done. Be the Fire King.”

Jeok Cheongang’s gaze, fixed on the North Heaven Demon Lord and Jamukha as they approached slowly and cautiously, shifted to me.

“What? Is there something else you want to say?”

“No, nothing much. It just struck me that accepting you as my Disciple was the right choice.”

For a moment, I didn’t know what to say. Jeok Cheongang’s quiet voice reached my ear.

“We never made any embarrassing promises to each other, but keep one thing in mind, as always.”

“What should I keep in mind…?”

“This old man is always by your side.”

“……!”

“So don’t do anything stupid like risking your life in a fight. Even if Yama comes for you, this old man will kick him in the ass and send him packing.”

The more I learned, the stranger it seemed.

We were both human, made of flesh and blood, and yet our thoughts could be so completely different.

One person asked another to give up his life in return for everything he wanted. Another needed nothing at all—he only wanted the other person to survive.

And that was exactly what I wanted to say to Jeok Cheongang, too.

“If I keep that promise, what will you give me?”

Step by step, the two enemies drew closer. I watched the dark crimson mist grow thicker as I spoke, and Jeok Cheongang gave a dry laugh.

“You shameless bastard. Fine, what do you want?”

“Nothing much. You’ve already been sick once, so a long, healthy life is out of the question. At least make sure you live a long, sickly one from now on.”

“Living a long time at my age, huh? Seems I have a good reason to live at least another hundred years.”

Jeok Cheongang laughed heartily, clearly delighted.

Pale light-flames gathered in his outstretched hands. Alongside them, blue-white flames surged over the spearhead of White Flame, burning away the chill of the deep night.

*Fwoooosh.*

Beyond the darkness melting in the heat of two flames—alike, yet different—I stepped forward toward the ominously thick dark crimson mist.

No. We did, as if we’d made a promise to do so at the same time.

*Shwaa!*

* * *

Everyone who faced the mist—red as blood and frighteningly thick—felt a chill sink deep into their spines and stopped moving.

No. They had no choice but to stop.

Their instincts knew it before their reason could.

*If I get close, I’ll die.*

The sight alone was chilling.

That thick blanket of mist was energy made almost completely tangible. It was no different from a forest of blades and spears, ready to slice and tear anyone who entered to pieces.

But the biggest reason so many people from Shanxi were held back was the terrifying battle raging inside that dangerous space.

*KABOOM! KABOOOOM!*

Was there any phrase that could describe what was happening better than “heaven and earth overturned”?

Beyond the mist, writhing like a living creature, four Supreme Peak masters were entangled with one another at the speed of flashes of light.

Without a moment’s pause.

Even now.

*Shhk!*

Force sliced through the hard ground as if it were tofu.

Jeok Cheongang narrowly dodged the North Heaven Demon Lord’s strike and clenched his fist.

The wrinkles had vanished from his face with his regained youth. Pale light-flames surged over his knuckles.

*Fwoosh!*

Flame-Extinguishing Divine Fist.

A tremendous blaze, brought to the tenth level of mastery after more than a century of training, erupted.

It stained the air and shot toward the enemy before him—toward the North Heaven Demon Lord.

*KABOOOOOM!*

Compressed air exploded in layers.

But even amid the enormous impact, which melted the ground and shook the cliff walls, the North Heaven Demon Lord’s figure blurred in the final instant and disappeared.

Or, more accurately, it disappeared from the sight of a human with such obvious limits.

*Whoosh.*

A tiny, faint whistle slipped quietly into his ear.

But Jeok Cheongang knew well that movement beyond sound could fool even hearing.

*Above!*

He could feel it.

His opponent’s presence, descending from the invisible space above his head.

And, at the same time, the massive Force carried on the spearhead that thrust forward, erasing the wind in its wake.

*Poom!*

Jeok Cheongang struck out with both palms without hesitation.

The dark crimson mist that had wrapped around the area scattered in an instant.

The full force of Flame Divine Palm surged upward in a pillar of fire.

He aimed it at his opponent, who had tried to erase his presence as much as possible, but whose immense energy made it impossible to conceal him completely.

And in the next moment, Jeok Cheongang realized something anew.

The North Heaven Demon Lord, drawing on the power of the Temporary Strength Pill, was a great enemy who could look down on even him—who had reached his current realm through several breakthroughs in insight—as half a step beneath him.

*Shwaa!*

The spearhead pierced a single precise point.

The immense Force carried at its tip split the flames that seemed capable of burning the whole world. The distance between the two men vanished.

“……!”

Overwhelmed by that force, Jeok Cheongang’s eyes widened.

This wasn’t a question of martial enlightenment.

The North Heaven Demon Lord’s movements, enhanced to an extreme, made everything possible—along with internal energy so powerful it made Jeok Cheongang wonder if he had drawn out every last bit of his innate qi.

*Damn it.*

Jeok Cheongang swallowed the curse rising to his lips and pulled up every ounce of his internal energy.

He slammed both hands together against the spearhead plunging toward his chest.

*Krrrrk!*

The spearhead trembled between his palms, pressed together as if in prayer.

Dark crimson Force that his Body-Protecting Qi could not fully stop tore into his flesh and bones. Jeok Cheongang clenched his teeth to endure the pain.

*Crack.*

The pain of his molars breaking was nothing beside what he felt in his two hands, growing more mangled by the second.

As Jeok Cheongang swallowed the blood surging up his throat and held on to the spearhead, the North Heaven Demon Lord bared his teeth in a grin.

“Why not stop now and get some rest? You look exhausted.”

A mocking voice slipped between Jeok Cheongang’s clenched teeth.

“I’ll give you that advice right back.”

The North Heaven Demon Lord’s eyes sank.

He, too, could feel with his whole body that Jeok Cheongang’s words weren’t an empty boast.

*What kind of monster is this old man?*

*Crack. Krrrunch.*

The spearhead was clearly being driven forward with all his strength, yet it could go no farther.

Jeok Cheongang’s skin was crushed by the Force, but his toes were dug deep into the ground, perfectly still.

The old monster of Mount Jiuhua, returned decades younger, was far stronger than the North Heaven Demon Lord remembered.

Strong enough that even now, after taking the Temporary Strength Pill, he couldn’t knock him down easily.

*But…*

It ends here.

As that thought took shape, the North Heaven Demon Lord twisted the spear shaft.

With every ounce of strength he could bring to bear.

Enough to make even Jeok Cheongang unable to endure the pain this time.

*Crack.*

At the grisly sound of flesh splitting, Jeok Cheongang’s body trembled. Then a thunderous shout burst from between Jamukha’s lips.

“Jamukha!”

At that instant—

*KABOOM! Shhk!*

With a thunderous crash, a razor-sharp gust of wind shot toward Jeok Cheongang’s back.
```
