<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0955.txt",
      "sha256": "32f1f3d3d4f5e70e7bf913f8ad62a4a1d0b1c44fc61717b36a3ad1eb3d7ce2a1",
      "bytes": 12563
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "7da6e6e6f2778ed5381be6f3df888272937d3cd7fd2dd3649e19c6e195494ed2",
      "bytes": 1982
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ebfc840d67104c97d0585f79795365156f1920a828fd6a4c5ba3dd3ca29b358d",
      "bytes": 234431
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "85642c6448788c71d9769f79db425bd78808af58926151f14a1d1e0d5bbaeeed",
      "bytes": 759
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "0dd3e7b72024d690ba1be5536763ada309ccd7e435287c492aee08191e4c733f",
      "bytes": 667
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1e050a5f7fe4495083a420c058a54c8ad275c138c7f3ba4e2735c3880f4b074d",
      "bytes": 1204
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3f54867b59b521f5c32a13cb2887e20d9f7bd101cd2885898b05bbff1e46977a",
      "bytes": 1449
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2ad4ed643c302b50858073078fa78fa9ac97958801978d572971d4f2cee2a4b0",
      "bytes": 622
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a20f593116af26c44513a62978f9565dd0243e9d8b9b1d44d682a18b3511712e",
      "bytes": 267908
    }
  ],
  "estimated_tokens": 10073
}
-->

# Durable State Update — Chapter 955

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
1 and safe_through 955. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 955. Profile updates may replace only one
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
  "chapter": 955,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 955,
    "continuity_sources": [955],
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
    "The steppe army has begun its assault on Eight Spring Gorge after the Jin forces devastated northern Shanxi’s fields, water sources, and homes and laid traps; the defenders’ battle remains unresolved.",
    "Jin Wikyung has promised his defenders they will celebrate the next Double Ninth Festival together on Mount Heng.",
    "Temur regrets ignoring the real Chinggen’s warnings and knows the man beside him is Chinggen’s killer and impostor, but conceals his knowledge.",
    "Jamukha leads the steppe army and has long awaited a call from “that person”; that person’s identity and purpose remain unknown.",
    "The Emperor remains gravely ill from Blood Soul Gu; the Divine Physician says saving him requires him to die once, and Taekyung’s quest to remove the Gu and treat him remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "The real Chinggen was killed; an impostor wearing his face continues to accompany Jamukha."
  ],
  "continuity_sources": [
    953,
    954
  ],
  "open_questions": [
    "How will the battle at Eight Spring Gorge fare?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will the Chinggen impostor do, and what is their purpose?"
  ],
  "safe_through": 954,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 궁성     | **Bow Saint**                 | —              |
| 삼성     | **Three Saints**    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 도사      | **Daoist**                                                      |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 염라 | **Yama** | Buddhist lord of the underworld invoked as the one awaiting the dead. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 등평도수 | **Rising on Duckweed, Crossing Water** | Comparable movement feat for walking across water. |
| 염라대왕 | **Yama** | Expanded source form of the established underworld ruler term 염라. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 시비 | 진태경 | household_servant_to_visiting_young_hero | Young Hero Jin | formal-polite | The maid summons Taekyung to meet the Family Head. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 954
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 952
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 948
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 953
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 953
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
＃955화



툭.

갑작스럽게 느껴진 차가운 감촉에, 나는 불현듯 눈을 떴다.

본능에 따른 움직임도 함께.

쉭!

허공을 가르는 일권(一拳).

빠르게 돌아오는 시야 속, 맞은편 나무 위에서 그런 내 모습을 지켜보고 있던 궁성이 덤덤한 얼굴로 입을 열었다.

“악몽이라도 꾼 모양이구나.”

“아.”

그제야 깨달았다.

조금 전까지 내가 언제 잠들었는지도 모를 만큼 깊은 잠에 빠져 있었다는 것을.

그리고 궁성의 말처럼, 그 안에서 보고 겪은 모든 것들은 최악 중의 최악이었다.

“제가, 제가 얼마나 잠들어 있던 겁니까?”

거칠어진 호흡을 가다듬으며 묻자, 나뭇가지 위에서 사뿐히 뛰어내린 궁성이 대답했다.

“글쎄. 한 시진쯤 되었지.”

“한 시진…….”

“더 자 두거라. 동이 틀 때까지만이라도.”

어스름한 새벽이었다.

머리 위에서는 내 잠을 깨운 아침 이슬이 나뭇잎을 타고 천천히 굴러떨어지는 중이었고, 인적이 드문 산속에서는 간간이 풀벌레 우는 소리만 들려왔다.

“노, 아니 스승님께서는 어디 계시죠?”

“사냥. 칠 주야가 넘도록 육포와 물밖에 마시지 않았으니 그 정도는 해야겠지. 그리고…….”

꺼져 가는 모닥불에 삭정이를 던져 넣은 궁성이 말을 이었다.

“호칭 문제로 눈치 볼 것 없다. 이미 대강의 사정은 짐작하고 있으니. 시커먼 사내들치고는 제법 낯간지럽게 굴더구나.”

“그걸 어떻게…….”

“시시콜콜한 것까지 물어볼 기운이 있으면 가까이 와서 몸이나 녹이거라.”

잠시 망설이던 나는 자리에서 일어나 걸음을 옮겼다.

모닥불이 아닌, 아직 캄캄한 숲 쪽 어딘가로.

“어디 가느냐?”

“천천히 앞서가고 있겠습니다. 곧 노야께서 오시면 함께…….”

“어지간히 말을 안 듣는 녀석이로군.”

작게 혀를 찬 궁성이 손을 뻗었다.

슈확!

바람이 찢어지는 소리와 함께 날아든 지풍(指風)이 목덜미를 스친다. 그 소름 끼치는 파공성에 전신에 달라붙어 있던 잠기운이 순식간에 사라졌다.

“……지금 뭐 하시는 겁니까?”

“말 안 듣는 어린아이에게는 매가 약이지. 좋은 말 할 때 불이나 쬐거라. 아니면 자빠져서 잠이나 자든지.”

깜빡했다.

기껏해야 삼십 대쯤으로 보이는 저 여인도, 결국 말보다는 힘이 앞서는 무림인이라는 것을.

심지어 삼성(三星)은 그중에서도 한 손에 꼽히는 대기업……이 아니라 전국구 깡패.

말없이 궁성을 노려보던 내가 입을 열었다.

“가야 합니다.”

“당연히 그럴 것이다.”

“저는 지금 당장을 이야기하는 겁니다.”

“나는 잠시 나중을 말하고 있다.”

“이렇게 나오실 겁니까?”

“이렇게 나오면, 네가 어쩔 셈이냐?”

담담하게 받아친 궁성이 모닥불을 뒤적이며 말을 이었다.

“나 역시도 그럴 때가 있었다. 한 사람이라도 구하기 위해 있는 힘껏 발버둥 치고, 고작 촌각밖에 안 되는 짧은 시간을 줄이기 위해 목숨을 걸었지.”

“이제는 아닙니까?”

“글쎄.”

무언가 공허한 대답.

옛 기억을 떠올리는 듯, 조금씩 살아나기 시작하는 불길을 바라보며 잠시 생각에 잠겨 있던 궁성이 입을 열었다.

“나는 그저 한 가지 작은 깨달음을 얻었을 뿐이다.”

“작은 깨달음?”

“그 조급함이, 나 자신을 더욱 사지로 몰아넣고 있다는 생각.”

“……!”

“매 순간에 최선을 다할지라도 결과는 아니었지. 마음 편히 밥 한 끼, 차 한 잔 마실 시간의 여유조차 없이 누군가를 죽이고 누군가의 죽음을 지켜봐야 했다. 어느덧 마음 깊숙이 싹 튼 심마(心魔)를 발견한 후에도 그 사실은 변하지 않았어.”

모닥불을 바라보는 궁성의 눈동자는 불그스름하게 달아올라 있었다.

그녀가 오래전 수없이 보고 겪었던 전쟁의 불길처럼.

“운명이라는 단어를 좋아하지는 않는다. 아무리 발버둥 쳐도 결국 정해진 대로 흘러간다면, 그 노력의 의미조차 퇴색되어 버리니까. 하지만…….”

투둑. 화아악.

점차 살아나던 불길이 크게 몸집을 부풀린다.

아스라이 흩날리는 불씨 너머, 궁성은 깊게 가라앉은 눈빛으로 나를 응시했다.

“무려 칠 주야 동안이나 한시도 쉬지 않고 달려온 누군가가 있음에도 막을 수 없는 일이라면, 그래. 그것이야말로 운명이겠지.”

나는 이를 악물었다.

그리고 물먹은 솜처럼 피로에 흠뻑 젖은 몸뚱어리를 느꼈다.

나 스스로도 안다.

궁성의 말이 옳다는 것을.

내게 있어 운명이란 이 세상에 존재하는 모든 단어 중 가장 엿 같은 의미를 지녔지만, 그럼에도 때로는 그것의 존재를 인정할 수밖에 없다.

나 또한 한낱 인간에 불과하니까.

전지전능한 신이 아니니까.

“꿈을, 악몽을 꿨습니다.”

남의 것처럼 낯선, 갈라진 목소리가 입술 사이로 흘러나온다.

처음 눈을 떴을 때부터 등허리가 축축하게 젖어 있던 이유는, 새벽이슬이 아닌 식은땀 때문이었다.

“마침내 도착했을 때는…… 모두가 죽어 있었습니다. 한 사람도 예외 없이 모조리. 전부다.”

“그랬더냐.”

내 목소리는 떨렸고, 궁성은 담담했다.

“몹시 슬펐겠구나.”

나는 고개를 가로저었다.

그건 슬픔이 아니었다. 절망이었다.

땅을 뚫고 저 멀리 지하 깊숙이까지 내리꽂히는 듯한 절망.

꿈에서 깨어난 지금 이 순간에조차, 처참하게 죽음을 맞이한 그들의 모습이 눈앞을 어른거리는 듯했다.

“그래서 가야 합니다. 더 늦기 전에, 한시라도 빨리.”

처음에는 단순히 게임이라고 생각했다.

검은색 목폴라나 체크무늬 셔츠를 입은 안경잡이 개발자들이 만들어 낸, 그저 데이터의 산물이라고 여겼다.

하지만 머지않아 진실을 깨달았다.

이곳이 또 하나의 세상이며, 저들은 저마다의 감정과 의지로 이루어진 인격체라는 사실을.

나는 그렇게 마음을 열었다.

나를 자신의 혈육이라 철석같이 믿고 있는 태원진가의 소가주에게, 첫 만남부터 아니꼬운 눈빛으로 시비를 걸어오던 어느 젊은 수문 위사에게.

그리고 생애 마지막 후회이자 미련으로 남은 제자를 찾기 위해 천하를 떠돌던 어느 정신 나간 노인에게도.

그들이 전한 진심은 내 마음 안에 고였고, 어느새 넘쳐흐르고 있었다.

또 하나의 친구이자 동료. 스승이자 가족.

눈을 감으면 여태껏 만난 모두의 얼굴과 이름이 어둠 속에서 떠오른다.

그것이야말로, 지금의 이 조급한 마음과 피로에 젖은 육신을 쥐어 짜내서라도 달려가야 할 이유다.

‘지난 칠 주야 동안 그래 왔듯이.’

그야말로 온 힘을 다했다.

숙련된 사냥꾼조차 꺼리는 험준한 산맥을 가로질렀고, 배를 기다리는 시간조차 아까워 막대한 공력을 불살라 등평도수(登萍渡水)로 강을 건넜다.

그렇게 여기까지 왔다. 이곳에 왔다.

‘이제 태원까지 남은 거리는, 고작 이틀 남짓.’

어쩌면 이미 황실의 전령이나 전서응을 앞질렀을지도 모른다.

천자가 내어준 명마도 버린 채. 가장 신속한 길을 찾아 밤낮을 가리지 않고 쉼 없이 달려왔으니까.

하지만 고작 그 이틀 남짓한 짧은 시간은, 오늘 내가 꾼 악몽이 현실로 이루어지기에 충분한 시간이기도 했다.

‘그렇게 놔둘 수는 없다.’

꾸욱.

힘껏 주먹을 말아쥐었다. 살을 파고든 손톱과 함께 뜨거운 핏물이 느껴진다.

그런 내 모습을 물끄러미 응시하던 궁성이 문득 입을 연 것은 바로 그 순간이었다.

“희한한 일이로구나.”

“그게 무슨…….”

“너는 그들을 한없이 소중히 여기면서도, 한편으로는 조금도 믿지 않으니.”

“……!”

“가끔은 그저 믿어 주어라. 그들은 네 생각처럼 나약하지도, 쉽게 뿌리 뽑히지도 않는다.”

전신이 덜컥 굳었다. 순간 할 말을 잃어버린 내 귓가로 궁성의 음성이 이어졌다.

“물론 너는 많은 것을 할 수 있겠지. 한 손으로 만근거석을 부수고, 다른 한 손으로는 강물을 가를 수도 있을 것이다. 하지만…… 그것이 바위가 아니라 산이라면, 강이 아닌 바다라면 어찌하겠느냐. 먼 옛날의 우공(愚公)과 같이 그저 홀로 묵묵히 감내할 생각이더냐?”

우공.

어느 어리석은 노인의 이야기다.

돌을 캐고 흙을 파서 거대한 산을 허물고자 했었던.

결국 그 정성에 감동한 옥황상제의 도움으로 어리석은 노인은 목적을 이룰 수 있었으나, 결국 그 자신의 노력과 힘만으로 이루어진 것만은 아니었다.

“우공의 소문을 들은 수많은 이들이 그를 보며 어리석다 비웃지 않고, 모두가 힘을 합쳐 도왔다면 어찌 되었을까.”

대답하지 않았지만, 나는 마음속으로 생각했다.

어리석은 노인은 그들의 도움을 받아 끝끝내 목적을 이루었을 것이다.

옥황상제가 아닌, 자신을 믿고 따라 준 이들의 힘으로.

그들 모두의 힘으로.

‘아.’

문득 마음 한구석이 울렁거린다. 나는 군데군데 흙이 묻어 있는 두 손을 내려다보았다.

궁성의 말처럼 내게는 강대한 힘이 있다.

일권(一拳)에 거대한 바위를 으스러트릴 수도, 일장(一掌)으로 짧게나마 작은 강을 갈라 버릴 수도 있다.

그러나 산을, 바다를 움직이기 위해서는 그것으로도 턱없이 부족하다.

산서성에 드리워진 재앙 역시 마찬가지였다.

하늘을 가득 채운 먹구름을 걷어내기 위해서는, 모두의 도움이 필요하다.

“네게 묻겠다.”

담담하지만 어째서인지 따뜻하게 느껴지는 눈빛.

궁성이 나를 응시하며 천천히 말을 이었다. 마치 어린 손자의 투정을 타이르는 할머니처럼.

“네가 믿는 것은 하늘이냐, 아니면 사람이냐?”

나는 대답 대신 서서히 빛이 번져오는 동쪽을 바라보았다.

그리고 불현듯 입을 열었다.

“혹시, 옥황상제가 어떻게 생겼는지 아십니까?”

“뭐?”

“제가 의심병이 좀 있어서, 직접 확인하지 않고서는 영 믿음이 안 가서요.”

“……!”

뜬금없는 대답에 눈을 깜빡이던 궁성이, 이내 내 말에 담긴 뜻을 깨닫고 피식 실소를 흘렸다.

“도사들이 들었다면 대경 질색했을 것이다.”

“괜찮습니다. 제 뒤에 계신 분이 상제(上帝)까지는 아니어도, 염라(閻羅)쯤은 되시는 분이라.”

사박.

일부러 소리 낸 것이 분명한 발걸음.

고개를 돌리니 눈살을 찌푸린 염라대왕, 아니 적천강이 그곳에 있었다.

쿵.

어디서 잡아 왔는지 모를 커다란 노루를 내려놓은 적천강이 입을 열었다.

“이런 괘씸한 놈을 보았나. 잠시 자리를 비운 틈에 뭐, 염라?”

퉁명스러운 어조와 잔뜩 주름 잡힌 미간.

그러나 지금 이 순간에도 씰룩거리는 입꼬리는 웃음을 감추고 있다는 명백한 증거다.

이미 궁성과 나 사이에 오간 대화를 들었음이 분명한 그는, 짐짓 아무렇지 않다는 듯이 내게 물었다.

“되었으니 변명은 집어치우고, 어때. 간만에 고기 좀 뜯으랴?”

한시가 바쁜 이 상황에 고기라.

문득 수풀이 우거진 북쪽을 흘끗 바라본 나는, 이내 흐릿한 미소를 머금으며 대답했다.

“그거 좋죠.”

나는 우공이 아니다. 진태경이다.

그렇기에 이제는 믿는다.

그들 모두를.

‘죽지 마라. 단 한 명도.’

들리지 않을 목소리를 마음속으로 뇌까리며, 나는 모닥불 앞에 앉았다.

칠 주야만에 주어진 제대로 된 휴식.

남아 있는 이틀 남짓의 거리를 위해, 최선을 다해 힘을 비축해야 했다.
```

## Final English reading copy

```markdown
# Chapter 955

Tap.

At the sudden touch of something cold, I abruptly opened my eyes.

My body moved on instinct, too.

*Whoosh!*

A punch cut through the air.

As my vision snapped back into focus, the Bow Saint—watching me from the tree across from us—spoke with a calm expression.

“Looks like you had a nightmare.”

“Ah.”

Only then did I realize it.

I’d been in such a deep sleep that I hadn’t even known when I’d fallen asleep.

And, just as the Bow Saint had said, everything I’d seen and experienced in it had been the worst of the worst.

“How long was I asleep?”

I asked as I tried to steady my ragged breathing. The Bow Saint dropped lightly from the branch and answered.

“Let’s see. About two hours.”

“Two hours…”

“You should sleep some more. At least until daybreak.”

It was the dim light of early morning.

Above us, the morning dew that had woken me was slowly rolling down a leaf, and now and then the only sound in the deserted mountain woods was the chirping of insects.

“W-wait, no. Master—where is he?”

“Hunting. We’ve been eating nothing but jerky and drinking nothing but water for more than seven days. He ought to do at least that much. And…”

The Bow Saint tossed a dry twig onto the dying campfire and continued.

“You don’t need to worry about what to call him. I’ve already figured out the general situation. For men as rough-looking as you two, you’ve been surprisingly sentimental.”

“How did you—”

“If you have the energy to ask me about every little thing, come over here and warm yourself.”

I hesitated a moment, then stood and started walking.

Not toward the campfire, but toward somewhere in the still-dark woods.

“Where are you going?”

“I’ll go on ahead, slowly. Once Old Master comes back, we can go together…”

“You really are a stubborn brat.”

The Bow Saint clicked her tongue and reached out.

*Fwish!*

A blast of Finger Qi shot toward me with the sound of tearing wind, grazing the back of my neck. That chilling whistle made every trace of sleepiness vanish in an instant.

“…What are you doing?”

“For a disobedient child, a beating is the best medicine. While I’m still asking nicely, sit by the fire. Or lie down and go back to sleep.”

I’d forgotten.

That woman, who looked like she was barely in her thirties, was still a Murim martial artist who favored force over words.

And the Three Saints were, among other things, a top-tier corporation—no, a nationwide gang.

I stared at the Bow Saint in silence, then spoke.

“We have to go.”

“Of course we do.”

“I mean right now.”

“I’m talking about a little later.”

“So this is how you’re going to play it?”

“If I do, what are you going to do about it?”

The Bow Saint answered calmly, prodding the fire as she went on.

“There was a time when I was like that, too. I struggled with everything I had to save even one person. I risked my life to shave off moments—short as they were.”

“Not anymore?”

“Who knows.”

Her answer sounded hollow.

She gazed at the fire as it began to stir back to life, lost in thought as if recalling old memories. Then she spoke.

“I’ve only come to understand one small thing.”

“One small thing?”

“That my impatience was only driving me further into danger.”

“…”

“I gave every moment my best, but the results still fell short. There wasn’t even time to sit back and enjoy a meal or a cup of tea. I had to kill people and watch others die. Even after I discovered the inner demon that had taken root deep in my heart, that didn’t change.”

The Bow Saint’s eyes, fixed on the fire, glowed red.

Like the flames of war she must have witnessed countless times long ago.

“I don’t like the word ‘fate.’ If everything is going to happen as it’s already been decided, no matter how hard we struggle, then even the meaning of that struggle fades away. But…”

*Crack. Fwoosh.*

The flames, which had been gradually coming back to life, suddenly leapt higher.

Beyond the faintly drifting embers, the Bow Saint looked at me with a gaze sunk deep in thought.

“If something can’t be stopped even by someone who’s run without rest for seven whole days and nights… Then yes. That, surely, is fate.”

I gritted my teeth.

And felt my body, drenched in exhaustion like a waterlogged cotton rag.

I knew it myself.

The Bow Saint was right.

To me, fate had the most goddamn meaning of any word in the world. And yet there were times when I had no choice but to admit it existed.

Because I was only human.

Not an all-knowing, all-powerful god.

“I had a dream. A nightmare.”

A cracked voice, strange as if it belonged to someone else, slipped between my lips.

The reason my back had been damp since I first woke wasn’t the morning dew. It was cold sweat.

“When I finally got there… everyone was dead. Every last one of them. Not a single exception.”

“Is that so?”

My voice trembled. The Bow Saint remained calm.

“You must have been terribly sad.”

I shook my head.

It wasn’t sadness. It was despair.

Despair that felt like it had punched through the earth and plunged deep into the ground below.

Even now, after waking from the dream, the sight of them, all horribly dead, still seemed to hover before my eyes.

“That’s why I have to go. Before it’s too late. As soon as possible.”

At first, I’d thought this was just a game.

I’d figured it was nothing more than data created by bespectacled developers in black turtlenecks or plaid shirts.

But before long, I’d realized the truth.

This was another world, and the people here were individuals, each with their own feelings and will.

So I’d opened my heart.

To the Lesser Family Head of the Jin Family of Taiyuan, who firmly believed I was his own flesh and blood. To the young gate guard who’d picked a fight with me at our very first meeting, looking at me like he couldn’t stand the sight of me.

And even to that deranged old man who’d wandered the world searching for the Disciple who remained his last regret and lingering attachment.

The sincerity they’d shown me had settled in my heart—and before I knew it, it had overflowed.

Another friend and comrade. A Master and family.

When I closed my eyes, the faces and names of everyone I’d met came to me in the darkness.

That was why I had to run, even if it meant wringing every last bit of strength from this tired, impatient body.

*Just as I had over the past seven days and nights.*

I’d given it everything I had.

I’d crossed rugged mountains that even seasoned hunters avoided. I’d thought even waiting for a boat was a waste of time, so I’d burned through a tremendous amount of internal energy to cross the river using Rising on Duckweed, Crossing Water.

That was how I’d made it here. To this place.

*Now, Taiyuan is only about two days away.*

Maybe I’d already passed the imperial messengers—or the messenger eagles.

I’d abandoned even the fine horse the Son of Heaven had given me. I’d sought the fastest route and run without rest, day or night.

But those two short days were also enough time for the nightmare I’d had today to become reality.

*I can’t let that happen.*

*Clench.*

I curled my hand into a tight fist. My nails dug into my flesh, and I felt hot blood well up.

The Bow Saint had been watching me in silence. Just then, she spoke.

“Strange, isn’t it?”

“What do you mean…?”

“You treasure them beyond measure, and yet at the same time, you don’t trust them at all.”

“…”

“Sometimes, just trust them. They aren’t as weak as you think, and they aren’t so easily uprooted.”

My whole body stiffened. For a moment I was at a loss for words, and then the Bow Saint’s voice continued in my ear.

“Of course, you can do a great deal. You could shatter a boulder weighing ten thousand *geun* with one hand, and split a river with the other. But what if it were a mountain instead of a boulder? An ocean instead of a river? Would you just quietly bear it alone, like Yu Gong long ago?”

Yu Gong.

The story of an old man, considered foolish, who tried to tear down a great mountain by digging up earth and hauling away rocks.

In the end, the Jade Emperor had been moved by his devotion and helped him achieve his goal. But it hadn’t been done by Yu Gong’s own effort and strength alone.

“What if the countless people who heard Yu Gong’s story hadn’t laughed at him for being a fool, but had joined forces to help him?”

I didn’t answer, but I thought to myself:

With their help, the old man would have accomplished his goal in the end.

Not through the Jade Emperor, but through the people who believed in him and followed him.

Through all of them.

*Ah.*

Something stirred in a corner of my heart. I looked down at my hands, which were smudged with dirt here and there.

Just as the Bow Saint had said, I had tremendous power.

I could crush a huge boulder with a single punch, or split a small river for a short while with one palm.

But that still wasn’t nearly enough to move a mountain or an ocean.

The same was true of the disaster looming over Shanxi Province.

To sweep away the dark clouds filling the sky, I’d need everyone’s help.

“Let me ask you something.”

Her gaze was calm, but for some reason it felt warm.

The Bow Saint looked at me and spoke slowly, like a grandmother gently chiding her petulant young grandson.

“What do you believe in—the heavens, or people?”

Instead of answering, I looked toward the east, where the light was slowly spreading.

Then, quite suddenly, I spoke.

“Do you happen to know what the Jade Emperor looks like?”

“What?”

“I have a bit of a suspicion problem. I can’t really believe in something unless I see it with my own eyes.”

“…”

The Bow Saint blinked at my unexpected answer. Then she realized what I meant and gave a quiet laugh.

“If the Daoists heard you, they’d be horrified.”

“It’s all right. The person behind me may not be the Jade Emperor, but he’s at least Yama.”

*Shff.*

Footsteps, deliberately loud.

I turned my head and saw the King of the Underworld—no, Jeok Cheongang—standing there with a frown.

*Thump.*

Jeok Cheongang set down a large deer, who knew where he’d caught it, and spoke.

“You cheeky brat. I leave for a moment, and what’s this about Yama?”

His tone was gruff, and his brow was deeply furrowed.

But the corner of his mouth was twitching even now—a sure sign that he was trying to hide a smile.

He’d obviously heard the conversation between the Bow Saint and me. Still, he pretended nothing had happened and asked me as if it were all quite ordinary.

“Enough. Spare me the excuses. What do you say? Feel like tearing into some meat for a change?”

Meat, when every second mattered.

I glanced toward the overgrown woods to the north, then answered with a faint smile.

“Sounds good.”

I wasn’t Yu Gong. I was Jin Taekyung.

And so, now, I believed.

In all of them.

*Don’t die. Not a single one of you.*

I repeated the words silently, though they couldn’t hear me, and sat down in front of the campfire.

A proper rest, at last, after seven days and nights.

I had to save my strength as best I could for the two days or so still ahead.
```
