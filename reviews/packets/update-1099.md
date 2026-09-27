<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1099.txt",
      "sha256": "23e6f77961ebc31cdf45a1ee2e5ddfca361126e0853bc3c69cf777fd67076fb8",
      "bytes": 12875
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fe25e8d804029952bbe804c0bbc922f0a0b70dc7c6be6a462c8ed86be48746a8",
      "bytes": 2312
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "e58ae46a1bac772cc7720c130c81de8fb5906bb3ba1496eb8e7943cb290731fa",
      "bytes": 244132
    },
    {
      "path": "characters/Cheongheoja.md",
      "sha256": "6f57e2e7b99fa7b19efbf1bb88f9fcdf85cf8fa98cba00e8f1e7b14056b70538",
      "bytes": 544
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "96576141909be6322c7a1325884e775d71eb30254141d4cd97cade6e1c72e8dd",
      "bytes": 760
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "3350dbe7efd821de4e663672c1b25ed67c25c939f8cf93bd61f9b4c49c06eddf",
      "bytes": 1001
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "de627e01d78364e5d95cf0ed3d354fa916d55585b77cfa751c96802f51013aab",
      "bytes": 668
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "ecf952754f6b6f51d31d6a6c89c89beb2759cec353d30ff7a1b16a244d9fdf05",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2922285fbec2b184f8560b887c555cf240a54f1258ac1e8af1c1349d45a8427e",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "9358ed28bd911c9ec69c28186d8d7c067c2dd3045be8dcc00f1d77191616947b",
      "bytes": 623
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "608f66a88d45af645acdba8ccbbea44aa6c54857645454e62a25cc00bb2284f9",
      "bytes": 779
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4ecfcc0b69b1a06902a45f9fda0db56c875d4c4700a51505402e9140a523e68e",
      "bytes": 287765
    }
  ],
  "estimated_tokens": 11244
}
-->

# Durable State Update — Chapter 1099

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
1 and safe_through 1099. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1099. Profile updates may replace only one
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
  "chapter": 1099,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1099,
    "continuity_sources": [1099],
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
    "Dark Heaven’s army surrounds Xining under the Blood Lord; the Potala Palace has joined its forces with elephants and the Twelve Secret Monks.",
    "A major enemy force was expected to reach Qinghai within one or two days; Taekyung senses a final wave approaching Xining.",
    "The Blood Lord offered to spare everyone else if Taekyung leaves Xining alone within a day, severs the sinews and meridians in all four limbs, and surrenders; Jeok Cheongang believes the Blood Lord will break his promise.",
    "Taekyung believes the Lord of Heaven wants him more than anything, possibly more than the world; the reason remains unknown.",
    "A hidden Dark Heaven agent remains inside the defenders’ ranks, awaiting a signal.",
    "The Potala Palace and Dark Heaven are allies, but the Palace has a deep, longstanding hatred of the Fire Gate Clan; the Dalai Lama accepts the alliance’s unequal terms.",
    "Namho fears Sichuan may be exposed to enemies from Tibet after the Nanman Beast Palace’s departure.",
    "The Fire Gate Clan’s leaders are unlikely to abandon Xining while their allies and civilians remain there.",
    "Mu Song disobeyed Pa Ryun’s order to kill captured imperial troops; Pa Ryun says the Eldest Senior Brother and Elders obeyed him without deviation.",
    "Mu Song claims the Eldest Senior Brother and Elders serve someone other than Pa Ryun, but loses consciousness before explaining.",
    "A Yangtze River Channel League fleet is preparing to meet thousands of new allies gathered near the river; their identity is unknown."
  ],
  "continuity_sources": [
    1097,
    1098
  ],
  "open_questions": [
    "Will the approaching force reach Xining in time to decide the battle?",
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?",
    "Who is the hidden Dark Heaven agent inside the defenders’ ranks, and when will they signal?",
    "Who are the new allies gathering near the river?",
    "Whom do the Eldest Senior Brother and Elders serve, and what was Mu Song about to reveal?"
  ],
  "safe_through": 1098,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 굉도     | **Hong Dao**       |
| 무신     | **Martial God**               | —              |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 시스템              | **System**                     |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 대사      | **Master** for a senior Buddhist monk                           |
| 청허자 | **Cheongheoja** | Kunlun Sect Leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 삼매진화 | **Samadhi True Fire** | Internal-energy flame demonstrated by the unnamed old man. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 좌장 | **presiding chair** | Authority overseeing the Star-Array Grand Banquet. |
| 계인 | **Buddhist precept seals** | Seals carved into the foreheads of Shaolin martial monks. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 역용술 | **disguise technique** | Technique used by the Third Fiend to conceal his identity. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 대장군 | **Great General** | Military title used for the official who claimed credit after the Demonic Cult withdrew. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 인시 | **Insi** | The traditional time period from three to five in the morning. |
| 묘시 | **the hour of the Rabbit** | Traditional time period following Insi. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 진화 | **evolution** | The transformation the Southern Heaven Demon Empress claims the rift will produce. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 적천강 | 청허자 | senior martial master to former acquaintance and younger martial master | you / Fellow Daoist | blunt and familiar | Jeok Cheongang mocks Cheongheoja for addressing him as a fellow Daoist. |
| 진태경 | 청허자 | younger martial artist to senior sect leader | Sect Leader | respectful | Uses a formal greeting and bow. |
| 청허자 | 진태경 | senior sect leader to younger martial artist | Fellow Daoist Jin | warm and polite | Greets Taekyung by surname and confirms Hak Woo is well. |
| 청해성주 | 진태경 | city official to imperial marquis | Marquis of Shangshan | extremely deferential | Uses 상산후 while responding to Taekyung. |

## Listed compact profiles

### Cheongheoja.md

# Cheongheoja (청허자)

- **Safe through:** Chapter 1096
- **Aliases:** None
- **Role:** Cheongheoja is the Kunlun Sect Leader and Hak Woo’s master.
- **Personality:** Warm, composed, and patient, he faces setbacks with resolve and receives even startling company with good humor.
- **Voice:** Measured and gentle, using formal Daoist courtesies and calm metaphors.
- **Relationships:** Hak Woo is his Disciple; he knows Jin Taekyung by reputation and treats him warmly.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1098
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 1094
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1063
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1098
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1098
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1098
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 1050
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

## Korean source

```text
1099화




그날의 밤은 유난히도 길었다.

그것은 도무지 그칠 기미가 보이지 않는 폭우 때문일지도, 수 시진이 지나도록 여전히 제자리를 지키고 있던 먹구름 때문일지도 몰랐다.

그리고 숨 막히는 분위기 속에서 이어지던 회의는, 묘시(卯時)에 이르러서야 마무리되었다.

“이제 남은 것은 단 한 번의 결전뿐이니, 이 자리에 계신 여러 대협께서는 충분한 휴식을 취하시고 맡은 바 책무를 다해 주십시오.”

평소와는 너무나도 다른, 격식을 갖춘 말투.

하지만 그런 내 모습에 조금의 어색함을 느끼거나, 까마득한 후배의 좌장(座長) 행세에 거북함을 느끼는 이는 이 자리에 모인 수뇌부 중 단 한 사람도 없었다.

애당초 조금이라도 물을 흐릴 만한 인물들은 전부 물갈이가 된 상황.

청해 무림의 명숙과 장군들은 정중하면서도 결의 어린 태도로 내게 예의를 갖춘 뒤, 각자에게 주어진 소임을 다하기 위해 자리를 떠났다.

지금 이 순간에도 이미 한참 전에 식어 버린 찻잔을 기울이고 있는, 어느 노 도사만큼은 예외였지만.

“식은 차만큼 맛대가리 없는 게 또 없지. 어때, 노부가 뜨끈하게 덥혀 주랴?”

나가려다 말고 문득 멈춰 선 적천강이 불쑥 던진 한마디에, 노 도사가 고개를 가로저었다.

“식은 것은 식은 것대로, 뜨거운 것은 뜨거운 대로의 맛이 있는 법이지요. 게다가…….”

구름이 떠다니는 듯한 어조로 대답한 노 도사가 나를 향해 빙긋 웃었다.

“굳이 노 선배께 손을 빌리지 않아도, 여기 있는 젊은 도우에게 부탁해도 되지 않겠습니까?”

다른 누가 들었다면 말장난이라고 생각했을 것이다.

노 도사, 아니 곤륜파의 장문인인 청허자에게 있어 삼매진화(三昧眞火)로 찻물을 덥히는 것 정도는 아주 손쉬운 일일 테니까.

하지만 조금 전 청허자가 한 대답은 어디까지나 완곡한 거절의 표현이었다.

나와 단둘이 할 이야기가 남아 있다는.

그리고 그 뜻을 알아듣지 못할 적천강이 아니었다.

“뜬구름 잡는 소리를 하는 걸 보아하니 확실히 말코 도사답군. 마음대로 하거라.”

작게 코웃음을 친 적천강이 마지막으로 떠나자, 비로소 나와 단둘이 남게 된 청허자가 앞에 놓인 찻주전자를 들었다.

“도우도 한잔 들겠나?”

무슨 할 말이 남아 있는지는 모르겠지만, 나로서는 거절할 이유도 명분도 없다.

“감사히 받겠습니다.”

“감사할 것까지야.”

흐릿하게 웃은 청허자가 채워 주는 찻잔을 예의상 한 모금 머금자, 뭐라 표현하기 어려운 맛과 씁쓸한 향이 입안을 가득 채웠다.

“어떤가? 차 맛이.”

“어, 차갑네요.”

“또?”

“씁니다. 엄청나게.”

“빈도는 종종 이리 차갑게 마신다네. 도우의 입맛에 맞춰서 좀 데워 줄 걸 그랬군.”

“음. 괜찮습니다. 따뜻한 차여도 제 입맛에는 잘 안 맞아서요.”

“그런가? 빈도가 나름 공들여서 기른 찻잎인데.”

“……?”

아니, 도대체 왜 이런 중요한 얘기를 나중에 말하는 건데.

순간 당황해하는 내 모습에 청허자가 너털웃음을 터트렸다.

“농담일세. 따로 차밭을 가꾸는 건 사실이지만, 그 시급한 상황에서 어찌 따로 찻잎을 챙겼겠나.”

“아.”

그제야 장난에 걸려들었음을 깨달은 나는 고개를 절레절레 저었다.

하긴, 십만에 달하는 적들이 곤륜산으로 몰려드는 와중에 찻잎까지 싸 들고 왔다는 것부터가 말이 안 된다.

무슨 금잔디 명예 장문인도 아니고.

“한 방 먹었네요. 이런 분이신 줄 몰랐습니다.”

“이하동문일세.”

“예?”

그게 무슨 뜻이냐고 묻기도 전에, 빙긋 웃은 청허자가 말을 이었다.

“도우는 참으로 여러 모습을 갖고 있더군. 청해성주와 그 일파를 단숨에 뿌리 뽑을 때는 천하를 호령하는 대장군 같기도 하고, 어느 때는 단지 감정에 모든 것을 맡기는 미숙한 협객 같으면서도, 결국은 모두가 따를 수밖에 없는 대종사(大宗師)의 면모를 갖추었으니 말일세.”

음.

이걸 뭐라고 대답해야 하나.

청허자의 갑작스러운 칭찬에 머쓱해진 나는 괜히 턱을 긁적였다.

“과찬이십니다.”

“누구도 그렇게 생각하지 않을 걸세. 적어도 ‘그분’을 한 번이라도 대면했던 적이 있는 사람이라면.”

그분.

지극한 공경이 담긴 그 두 글자가 누구를 가리키는 것인지 깨달음과 동시에, 청허자가 천천히 입술을 뗐다.

“무신(武神). 고금을 통틀어 가장 위대했던 대종사. 비록 지금은 그 행적조차 묘연해진 지 오래지만…… 빈도는 그분의 향취를 도우에게서 느꼈네.”

문득, 그런 생각이 들었다.

어쩌면 청허자의 저 말이, 내 마음속에서 점점 짙어지고 있는 어떠한 진실과 가깝게 맞닿아 있을지도 모른다는 생각을.

나보다 앞서 현대와 무림을 오간 경계인(境界人).

끝없는 차원 어딘가에 실존하는 이 세상을, 마치 게임처럼 누비고 다녔을 플레이어(Player).

아마도 그래서였을 것이다.

그 순간, 나도 모르게 입술을 비집고 아주 작은 중얼거림이 흘러나온 것은.

“……그럴지도 모르죠.”

“음?”

“아니, 아닙니다. 그냥 그분처럼 되고 싶다는 이야기였어요.”

스스로 생각하기에도 옹색한 변명이었지만, 청허자는 내가 앞서 한 말에 대해 딱히 깊게 생각하는 눈치가 아니었다.

그도 그럴 것이, 목소리 자체도 워낙 작았거니와 그 존재 자체로 수수께끼나 다름없는 무신과 달리 나는 출신 성분이 확실한 인물이었으니까.

“그렇군. 도우라면 가능할걸세.”

별다른 의문 없이 고개를 끄덕인 청허자가, 다시금 찻잔을 기울인 뒤 덧붙였다.

“일평생을 바쳤음에도 그분의 발치에도 미치지 못한, 어느 말코 도사와는 다르게 말일세.”

곤륜파의 장문인으로서, 또한 한 사람의 도사로서 명망 높은 삶을 살아온 그였지만 자조 섞인 목소리에는 알 수 없는 회한이 담겨 있었다.

“무신께서는 누구보다 훌륭한 분이셨지. 언제나 역용술(易容術)로 당신의 모습을 감추고, 진실된 신분조차 제대로 드러내지 않았음에도 온 천하가 그분을 믿고 따랐을 만큼.”

지금의 청허자는 무신이 이룬 위대한 업적과 무위에 자신을 비교하며 깎아내리는 것이 아니다.

인품, 포용과 지도력에 관하여 얘기하고 있을 뿐.

그리고 이러한 일련의 흐름은, 그가 나와의 대화를 원한 진짜 목적을 향해 다가가고 있었다.

“물론 그분께서도 완전무결하시진 않았네. 이미 오래전부터 보이지 않는 곳에서는 암천의 흉계가 자리 잡고 있었으니까.”

“그분이 남아 계셨다면 지금 같은 상황이 벌어지지 않았을 거라 생각하십니까?”

“물론일세. 내 비록 입적하신 굉도 대사처럼 천문(天文)을 읽는 재주는 없으나, 적어도 무신께서 건재하셨다면 그들 또한 마음을 달리 먹었을 것이라 확신할 수 있지.”

단호하게 대답한 청허자가 한숨을 내쉬었다.

“허나 빈도는 결코 그분처럼 될 수 없었네. 온 세상을 피로 물들였던 혼란의 시대가 저물고 평화가 찾아왔음에도, 천하는커녕 본산(本山)조차 제대로 이끌지 못했으니.”

그 순간, 나도 모르게 미간이 좁혀졌다.

‘설마?’

본능이 속삭인다.

지금부터 흘러나올 이 이야기는 심상치 않다고.

어쩌면 이번 전투에서 아주 중요한 일부분을 차지할지도 모른다고.

그리고 일변한 분위기를 감지한 나를 보며, 청허자가 씁쓸한 표정으로 찻잔을 어루만졌다.

“지금까지는…… 제아무리 얼음장처럼 차가운 찻물이어도 상관없었네. 결국 빈도가 삼킬 수만 있다면, 그렇게라도 포용할 수 있다면 된다고 생각했으니까.”

지금까지는, 이라고 했다.

분명히.

“이제는 아니라는 말씀으로 들리는군요.”

“그렇네. 이 늙은이 홀로 냉병(冷病)으로 고생한다면 상관없으나, 수십 만이나 되는 사람들이 배앓이를 하게 둘 수는 없지 않겠나?”

“수십만……입니까.”

그 말을 듣는 순간, 비로소 확신할 수 있었다.

바로 이곳, 서녕의 내부에 배신자가 있다는 것을. 

그것도 아주 깊숙하고, 가까운 곳에 암천의 숨겨놓은 복검(覆劍)이 도사리고 있다는 것을.

그와 더불어, 곧이어 귓가를 파고든 청허자의 나직한 음성과 함께 깨달을 수 있었다.

왜 그가 나와 단둘만 남아 있기를 원했는지.

어째서 그토록 고통스럽고 자조 섞인 표정을 지었는지.

“빈도의 잘못일세. 그 아이를 제대로 가르치지 못한.”

“……!”

눈을 부릅뜬 나를 뒤로한 채, 못난 제자를 둔 노도사는 말없이 찻잔을 기울였다.

어느덧 삼매진화의 수법으로 뜨겁게 달구어진 그것을.

화아악.

퍼져나가는 온기 속, 모락모락 김이 피어오르는 찻물을 천천히 삼켜낸 청허자가 그 어느 때보다 무겁게 가라앉은 목소리로 입을 열었다.

“한 가지 부탁할 것이 있네.”

그 순간.

띠링.

때맞춰 귓가에 울려 퍼지는 시스템 알림과 함께, 반투명한 홀로그램 창이 눈앞에 떠올랐다.

그리고…… 하루의 시간이 흘렀다.



* * *



서녕(西寧)의 공기는 그 어느 때보다 무겁고 냉랭했다.

불과 며칠 전. 새롭게 합류한 지원군을 환영하며 웃음꽃을 피웠던 백성들의 표정은 머리 위 하늘처럼 어두컴컴했고, 그것은 마치 그들이 어렴풋이 떠올리고 있는 미래와 닮아 있었다.

파괴와 죽음.

그 끝에 기다리고 있을, 살아 있는 모든 것의 소멸.

하지만 누가 그랬던가.

인간은 희망의 동물이라고.

다른 이에게서 무언가를 빼앗으려 할 때보다, 빼앗길 때 그 어느 때보다 강한 힘을 내는 자들이라고.

그렇기에 그들은 완전한 절망의 구렁텅이에 빠지지 않을 수 있었다.

바로 지금 이 자리에서.

실낱과 같은 마지막 희망과 염원을 담아, 사방에 내려앉은 이 어둠을 밝혀 줄 구원자들을 바라보고 있었다.

철벅. 철벅.

수십여 명의 걸음이 하나가 되어 나아갈 때마다, 폭우에 의해 종아리까지 차오른 빗물이 첨벙인다.

지금 이 순간에도 시야를 가릴 만큼의 굵은 빗줄기가 쏟아지고 있었지만, 대로를 가득 메운 수많은 백성은 숨소리마저 낮춘 채 길을 비켰다.

솨아아아아.

요란한 빗소리 속에서 서서히 갈라지는 인의 파도.

그리고 헤아릴 수 없이 많은 백성의 중심을 가로지르는 선두에, 거침없이 걸음을 내딛는 한 사람이 있었다.

어느덧 천하의 만백성과 무림인들의 뇌리에 자신의 이름 석 자를 각인시킨, 어느 젊은 거인이.

‘진태경.’

이제는 모두가 그를 안다.

누군가는 상산후(上山后)로, 또 다른 누군가는 열화신룡(烈火神龍)이라는 별호로 저 청년을 기억할지도 모른다.

하지만 그 누가, 어떻게 그를 받아들인다 할지라도 변치 않는 사실이 있었다.

그것은 바로 오늘의 전투가.

그리고 진태경이라는 이름이 기나긴 역사의 한 자락을 장식하리라는 것이었다.

비록 그 끝이, 허망하고 비참한 최후일지라도.

“시벌, 하늘에 구멍이라도 뚫렸나.”

누군가 들었다면 깜짝 놀랐을 걸쭉한 욕설을 들릴 듯 말 듯 한목소리로 중얼거린 젊은 거인이 고개를 들었고, 그 시선 끝에 닿은 하늘은 어두웠다.

빌어먹을 정도로.

“딱, 죽기 싫은 날씨다.”

실소 섞인 뇌까림과 함께, 진태경은 아득한 빗줄기 너머로 서서히 가까워지는 그림자들을 바라보았다.

끔찍하리만치 거대한, 적의 대군세를.

그리고 그 순간.

우우우웅.

청해성. 아니 어쩌면 천하의 운명을 결정지을 전투의 시작을 알리는 효시(嚆矢)가 허공을 가로질렀다.

쐐애애액!

수백 개에 달하는 얼음송곳의 형태로.
```

## Final English reading copy

```markdown
# Chapter 1099

That night was unusually long.

Maybe it was because the torrential rain showed no sign of letting up. Maybe it was because the dark clouds still hadn’t budged, even after several shichen had passed.

And the meeting, which had dragged on in that suffocating atmosphere, didn’t wrap up until the hour of the Rabbit.

“Now, all that remains is one final battle. I ask each Great Hero here to get plenty of rest and fulfill the duties entrusted to you.”

My tone was much more formal than usual.

Yet among the leaders gathered here, not a single person seemed uncomfortable with my unfamiliar formality or with such a distant junior presiding over them.

Anyone liable to cause even the slightest trouble had already been removed from the picture.

The eminent masters and generals of Qinghai Murim treated me with respectful, resolute courtesy, then left to fulfill their respective duties.

There was one exception: an old Daoist still tilting a teacup that had gone cold quite some time ago.

“Nothing tastes worse than cold tea. What do you say? Want this old man to warm it up for you?”

Jeok Cheongang had been on his way out, but stopped and tossed out the question. The old Daoist shook his head.

“Cold things have their own flavor, just as hot things do. Besides…”

The old Daoist answered in a voice as airy as drifting clouds, then smiled at me.

“Must I trouble Senior for help when I could simply ask this young Fellow Daoist here?”

Anyone else might have thought he was just playing with words.

For Cheongheoja—the old Daoist, or rather the Sect Leader of the Kunlun Sect—warming tea with Samadhi True Fire would have been child’s play.

But Cheongheoja’s answer had been a roundabout way of refusing the offer.

He still had something to discuss with me alone.

And Jeok Cheongang wasn’t the sort to miss that.

“You’re talking like a Daoist who grabs at clouds. Do as you please.”

Jeok Cheongang gave a quiet snort and finally left. Only then did Cheongheoja pick up the teapot in front of him.

“Would you care for a cup, Fellow Daoist?”

I didn’t know what he still wanted to say, but I had no reason—or excuse—to refuse.

“I’d be grateful.”

“No need to be grateful.”

Cheongheoja smiled faintly as he poured. I took a polite sip, and a hard-to-describe taste and bitter aroma filled my mouth.

“How is it? The tea?”

“Uh, it’s cold.”

“And?”

“Bitter. Really bitter.”

“I often drink it cold like this. I should have warmed it to suit your taste.”

“Mm. It’s fine. Even warm tea doesn’t really suit my palate.”

“Is that so? I put quite a bit of effort into growing these tea leaves.”

“……?”

Why on earth would you wait until now to tell me something that important?

At my momentary dismay, Cheongheoja burst into hearty laughter.

“I’m joking. It’s true that I tend my own tea garden, but why would I have brought tea leaves along in a situation this urgent?”

“Oh.”

Only then did I realize I’d fallen for his trick. I shook my head.

Well, it made no sense to bring tea leaves along when a hundred thousand enemies were bearing down on Mount Kunlun.

It wasn’t as if he were Geum Jandi, honorary Sect Leader, or anything.[^1]

“You got me. I didn’t know you were like this.”

“Likewise.”

“Pardon?”

Before I could ask what he meant, Cheongheoja smiled and continued.

“You have so many sides to you, Fellow Daoist. When you uprooted the Qinghai City Lord and his faction in one stroke, you seemed like a Great General who could command the world. At times, you seem like an immature hero who leaves everything to his emotions. And yet, in the end, you have the bearing of a grand master whom everyone cannot help but follow.”

Hmm.

What was I supposed to say to that?

Flustered by Cheongheoja’s sudden praise, I scratched my chin for no reason.

“You’re too kind.”

“No one would think so. At least, no one who’s ever met ‘that person.’”

That person.

As I realized who those two words, filled with the deepest reverence, referred to, Cheongheoja slowly parted his lips.

“The Martial God. The greatest grand master in all of history. Though his whereabouts have long been unknown…”

He paused.

“I sensed his presence in you, Fellow Daoist.”

A thought suddenly occurred to me.

Maybe Cheongheoja’s words came close to a certain truth that was growing clearer in my mind.

A boundary-crosser who had traveled between the modern world and Murim before me.

A Player who’d roamed this world—which truly existed somewhere in the endless dimensions—as if it were a game.

Maybe that was why, in that moment, a tiny murmur slipped from my lips before I could stop it.

“…Maybe.”

“Hmm?”

“No, nothing. I just meant I wanted to become like him.”

It was a pretty flimsy excuse, even to me, but Cheongheoja didn’t seem to give my earlier words much thought.

That was understandable. My voice had been very quiet, and unlike the Martial God, whose very existence was a mystery, my origins were clear.

“I see. I believe you could.”

Cheongheoja nodded without a hint of suspicion, took another sip of tea, then added:

“Unlike a certain Daoist who never even reached his feet, despite devoting his whole life to it.”

As the Kunlun Sect Leader, and as a Daoist in his own right, he had lived a life of great renown. Yet his self-deprecating voice carried an unfathomable regret.

“The Martial God was a truly great man. Everyone under heaven trusted and followed him, even though he always concealed his appearance with the disguise technique and never properly revealed his true identity.”

Cheongheoja wasn’t putting himself down by comparing his skill or great achievements to the Martial God’s.

He was talking about character, tolerance, and leadership.

And this whole conversation was drawing nearer to the real reason he’d wanted to speak with me.

“Of course, he wasn’t flawless. Dark Heaven’s schemes had already taken root out of sight, long ago.”

“If he’d still been around, do you think this situation would never have happened?”

“Of course. Though I lack the gift for reading the heavens that Master Hong Dao possessed before he entered Nirvana, I’m certain that if the Martial God had still been around and strong, they would have made a different choice.”

Cheongheoja answered firmly, then sighed.

“But I could never become like him. Even after the age of turmoil that drenched the world in blood had ended and peace had arrived, I couldn’t properly lead even my own sect, let alone all under heaven.”

Without meaning to, I furrowed my brow.

*Don’t tell me…*

My instincts whispered that what came next wasn’t going to be trivial.

Maybe this story would turn out to be a crucial part of the battle ahead.

Cheongheoja noticed my expression change. He stroked his teacup with a bitter look.

“Until now… I didn’t mind that the tea was as cold as ice. I thought that as long as I could swallow it, as long as I could embrace it that way, that was enough.”

Until now, he’d said.

Definitely.

“I take it you mean that’s no longer the case.”

“That’s right. It wouldn’t matter if this old man alone suffered from cold illness. But surely I can’t let hundreds of thousands of people get stomachaches?”

“Hundreds of thousands…?”

At those words, I finally understood for certain.

There was a traitor right here inside Xining.

And deep, deep inside our ranks—close at hand—lurked Dark Heaven’s hidden sword.

Along with that realization, Cheongheoja’s low voice pierced my ears.

Now I understood why he’d wanted to be alone with me.

Why he’d looked so pained and self-deprecating.

“It’s my fault. I didn’t teach that child properly.”

“……!”

Leaving me staring wide-eyed, the old Daoist with a hopeless Disciple silently lifted his teacup to his lips.

By then, it had been heated until hot with Samadhi True Fire.

*Fwoosh.*

Warmth spread, steam curled from the tea, and Cheongheoja drank it slowly. Then he spoke in a voice heavier than ever.

“I have a favor to ask.”

At that moment—

*Ding.*

A System alert rang in my ears, and a translucent holographic window appeared before my eyes.

And then… a day passed.



* * *



The air in Xining was heavier and colder than ever.

Just a few days ago, the townspeople had welcomed the newly arrived reinforcements with smiles. Now their faces were as dark as the sky overhead, as though they vaguely sensed the future awaiting them.

Destruction and death.

The erasure of every living thing that would come at the end.

But who was it that said it?

That humans were creatures of hope.

That they were at their strongest when something was being taken from them—stronger than when they were trying to take something from someone else.

And so, they had not fallen into the depths of complete despair.

Here and now.

With the last sliver of hope and yearning in their hearts, they looked toward the saviors who would light up the darkness settling all around them.

*Splash. Splash.*

Each time the steps of dozens of people fell together, the rainwater—which had risen to their calves in the downpour—splashed beneath their feet.

Even now, rain fell in thick sheets, enough to obscure their vision. But the countless townspeople filling the main road made way, scarcely daring to breathe.

*Whoooosh.*

The human tide slowly parted amid the clamor of the rain.

At its head, cutting through the countless people gathered around him, strode a man without hesitation.

A young giant who had already carved his name into the memories of all the people under heaven and the martial artists of Murim.

*Jin Taekyung.*

By now, everyone knew him.

Some might remember that young man as the Marquis of Shangshan; others, by his sobriquet, the Blazing Flame Divine Dragon.

But no matter how anyone chose to regard him, one fact would never change.

Today’s battle—

And the name Jin Taekyung—

Would become part of the long sweep of history.

Even if it ended in a hollow, miserable death.

“Fuck, did a hole open up in the sky or something?”

The young giant muttered a thick curse in a voice barely loud enough to hear, one that would have shocked anyone who’d overheard it. He lifted his head, and the sky at the end of his gaze was dark.

*Dark as fucking hell.*

“Exactly the kind of weather that makes you not want to die.”

With a snort of laughter, Jin Taekyung watched the shapes slowly approaching through the distant curtain of rain.

An enemy force, horrifyingly vast.

And at that moment—

*Wooooong.*

The opening shot of the battle—one that would decide the fate of Qinghai, or perhaps all under heaven—cut through the air.

*Shhheeeek!*

In the form of hundreds of ice spikes.

[^1]: Geum Jandi is the heroine of *Boys Over Flowers*. The joke refers to her namesake, the Golden Grass.
```
