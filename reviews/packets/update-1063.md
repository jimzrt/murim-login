<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1063.txt",
      "sha256": "f6e440a3302040ca6b74c0c0f7a4e4373ea3fb567817f23abb9f696fb8665d5a",
      "bytes": 13200
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6f471a526755fe2ab31f3a2b45670b9f9a69921e2c962dd32e6411cdb1e34628",
      "bytes": 1300
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8002639eea62f633af444c66affb0412418cfda94a4e957eb62f581e41d098aa",
      "bytes": 241674
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "870339c867552add727cd625a9d9752204672058825df9fcd28e0d44ede1aa1d",
      "bytes": 760
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "6073198fd59704f8d3eea509b8ff98ff31892b2960253726a47bc3a8a199f6ab",
      "bytes": 668
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "e2dd86e6c9b5e7b8b1e3bc6744be8dd04df609341b8fa6fd6c650e6acb1ec61a",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "51a923e48ccd856b03745687d83fd0a4df8a91d504aeb498506d43633de2b940",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "67bb569ca7334ba8627a79a6023bbe5d227881b9f80d28a1816d9da731e07b21",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "78fb04961946f07b381c4f0259fc88b735582cf3e4a5c94ce7aa61c2d79f047a",
      "bytes": 623
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3fb747d35d651bb11f40f88b245dcccce3538c58caf24b077427793b7a59a679",
      "bytes": 283398
    }
  ],
  "estimated_tokens": 11494
}
-->

# Durable State Update — Chapter 1063

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
1 and safe_through 1063. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1063. Profile updates may replace only one
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
  "chapter": 1063,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1063,
    "continuity_sources": [1063],
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
    "Great Sir’s identity remains unknown; he sincerely believes himself to be the changing names he adopts, and Taekyung accepts him as an ally while believing he is not a Dark Heaven spy.",
    "The Gansu battle ended in victory; Taekyung completed the Path of Blood Quest and accepted a new chain Quest whose details are not yet known.",
    "The Blood Lord has returned at the Taiqing Hall in Kunlun and claims to have retrieved an important item; the item is unidentified.",
    "The Blood Lord and Grand Mage both serve “that person”; that person’s identity and connection to Asmodeus remain unknown."
  ],
  "continuity_sources": [
    1061,
    1062
  ],
  "open_questions": [
    "Who is Great Sir, and why does he believe himself to be the changing names displayed by the System?",
    "What is the important item the Blood Lord retrieved, and what achievement is he boasting about?",
    "Who is the person served by the Blood Lord and Grand Mage, and is that person connected to Asmodeus?",
    "What are the details of the new chain Quest Taekyung accepted?"
  ],
  "safe_through": 1062,
  "temporary_decisions": [
    "Render 말똥 as “Malttong,” glossed as “Horse Poop.”",
    "Render 태청전 as “Taiqing Hall.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 열화문    | **Fire Gate Clan**               |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 헌터      | **Hunter**            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 정마대전   | **Great Faction War**         |
| 대사      | **Master** for a senior Buddhist monk                           |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 악귀 | **Fiend** | Descriptive epithet applied to the First Fiend. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 대장군 | **Great General** | Military title used for the official who claimed credit after the Demonic Cult withdrew. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 대설산 | **Great Snow Mountain** | Mountain where Baeksang's wartime account reaches its next episode. |
| 역천 | **defying heaven** | Supernatural power that regenerates the masked man's body. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 신강 | **Xinjiang** | Region beyond Qinghai described as the domain of the Demonic Path. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1062
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1058
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1060
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1062
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1062
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1062
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

## Korean source

```text
1063화




사람들은 말한다.

발 없는 소문은 천 리를 가지만, 날개 달린 정보는 수만 리 밖까지 뻗어 나간다고.

그리고 무림의 정보 상인들이 일종의 격언(格言)처럼 떠받드는 그 말은, 한 치의 과장도 없는 사실이었다.

푸드득!

먹구름이 하늘을 뒤덮고, 대지가 죽음에 잠긴 그날.

한날한시에 수십여 마리에 달하는 전서응(傳書鷹)이 동시에 날아오르는 광경은 퍽 장관이었다.

산처럼 쌓인 시체와 못을 이룬 핏물을 뒤로한 채, 하늘 높이 솟구친 전서응들은 제각각의 목적지를 향해 거대한 날개를 흔들었다.

붉게 물든 설원이 자그마한 핏방울처럼 멀어지고, 새하얀 만년설에 뒤덮인 대설산맥(大雪山脈)이 보이지 않을 때까지.

태양과 달, 낮과 밤이 몇 차례에 걸쳐 서로의 자리를 양보하고 세상의 끝까지 이어져 있을 것 같던 황톳빛 고원이 지평선 뒤로 사라질 때까지.

그리고 마침내 수십여 마리의 전서응들이 저마다의 여정을 모두 끝마쳤을 때, 중원 천하는 분화구 속의 용암처럼 들끓어 올랐다.

“와아아아!”

“대국 만세! 황제 폐하 만세!”

“무엇들 하고 있소! 다들 나오시오! 어서!”

제각각 장소와 시간의 차이는 있을지언정, 감숙성에서 벌어진 대사건을 접한 이들은 즉각 거리로 뛰쳐나와 환호했다.

심지어 해가 뜨기도 전, 때아닌 소란에 단잠에서 깨어나 대문 밖으로 나온 이들조차도 분노보다는 당혹스러움을 느낄 정도였다.

“어느 염병할 놈들이 암탉도 쳐 자빠져 자는 이 시간에…… 거기 당신들, 도대체 뭐 때문에 남의 집 앞에서 지랄들이오?”

아마도 평소였다면 날 선 말에 대뜸 서로 멱살부터 잡고 봤을 것이다.

그러나 환호와 함성을 내지르며 새벽을 몰아낸 군중들은 잔뜩 흥분한 채로 연거푸 소리칠 뿐이었다.

“대승이오! 대승!”

“다짜고짜 그게 무슨 헛소리요? 내가 묻는 건 그게 아니…… 잠깐. 대승이라니?”

“허어, 이 양반 보게. 아직 소식을 못 들은 모양이군.”

“몰랐소? 신강(新疆)의 역도들이 제 주제도 모르고 감숙성에 쳐들어갔다가 되려 씨 몰살을 당했답디다!”

“뭣이? 놈들이 감숙을 노려?”

그제야 뒤늦게 소식을 접한 이들은 눈을 부릅떴고, 그들이 느끼는 경악은 신분 고하에 상관없이 같았다.

어찌 그렇지 않겠나.

불과 일 년 전만 하더라도 눈 크고 귀 밝은 자들의 입에만 오르내리던 암천(暗天)이라는 집단은, 이제 궁벽한 시골 촌구석에서 하루 벌어 하루 먹고사는 촌부도 아는 존재가 되어 버렸다.

신강의 역도, 사막 너머의 악귀들.

반세기 전, 정마대전(正魔大戰)이라 불리는 피바람을 일으켰던 마교의 악명조차도 작금의 암천에 비교할 수는 없었다.

과거의 마교가 정복하고자 했던 것은 중원 무림이었으나, 암천은 천하 그 자체를 얻고자 하므로.

역천(逆天).

두 글자에 담긴 뜻 그대로 하늘을 뒤집고, 순리를 거스르며, 숱한 난세 끝에 세워진 통일 왕조와 평화를 무너트리려는 역도의 무리.

그것이 바로 암천이었고, 그러니 대국의 백성들은 지금 이 순간에도 거리를 누비며 환호했다.

“허어, 이런 경사가 있나. 아니 그런데 도대체 얼마나 큰 대승을 거두었길래 이 난리 통인 거요?”

잠이 싹 달아난 누군가의 물음에, 군중들 사이에서 의기양양한 대답이 들려왔다.

“놀라지 마시오. 내 듣기로는 단 한 번의 전투로 족히 수만에 달하는 역도가 죽거나 사로잡혔다 하더이다.”

“헉, 수만!”

일개 사이비(似而非) 집단을 벗어난 어마어마한 머릿수와 그에 따른 전공에 헛숨을 삼킨 것도 잠시, 어디선가 곧장 반박하는 목소리들이 튀어나왔다.

“무슨 헛소린가? 내가 잘 아는 무림인이 알려 줬는데, 한나절 만에 십만을 몰살시켰다더군.”

“십만? 삼십만 아니었나?”

“다들 무슨 소리요? 무려 백만이 넘는 역도들을 궤멸시켰다던데.”

“거 듣자 하니 헛소리도 적당히 좀 해야지. 아무리 그래도 백만은 아니지 않소?”

“그럼 딱 반으로 갈라서 오십만. 아니, 삼십만으로 칩시다.”

“삼십만도 너무 많은데. 도대체 어디에서 들은 거요?”

“당신 암천이오? 지금 분위기 파악이 안 돼?”

“아니, 갑자기 이야기가 왜 그렇게 흘러가는…….”

“그래서, 삼십만으로 할 거요, 말 거요?”

“……그걸 내가 정할 수 있소?”

“아, 삼십만! 더는 양보 못 한다는 것만 똑똑히 알아두시오!”

“아, 알겠소. 그럽시다. 삼십만으로 알고 있을 테니 제발 진정 좀 하시오.”

“이제야 좀 말이 통하는구먼. 자, 따라 하시오. 대국 만세!”

“대, 대국 만세.”

“어허, 목소리가 작다!”

“마, 만세!”

“한결 낫구먼. 자, 이번에는 무림맹 천세!”

“……이거 도대체 언제 끝나는 거요.”

“아직 남았소. 이 다음은 열화신룡, 아니 상산후 천세니까 미리 생각하고 있으시오.”

비록 소수의 몇몇은 떨떠름한 반응을 보이긴 했으나, 대부분의 양민들은 무림맹을 향해서도 아낌없는 환호를 보냈다.

그리고 그것은 불과 수년 전과 비교해도 아주 놀라운 수준의 인식 변화였다.

구파일방과 오대세가를 중심으로 한 정파가 중원 무림을 지배하고 있었다고는 해도, 길어진 평화는 부패를 불러왔고 힘에는 부정이 깃들었으니까.

잡티 하나 없는 흰옷을 걸친다고 그 마음까지 백색이 되던가.

자고로 고인 물은 언젠가 썩기 마련이요, 완전한 선악(善惡)이란 어디에도 존재하지 않았다.

그러나 이제는 다르다.

“상산후 천세!”

“열화신룡 천세!”

단 한 사람의 존재로 인해 얼마나 많은 것이 뒤바뀌었는지 떠올릴 때마다, 새삼 놀라지 않을 수가 없었다.

진태경.

지금으로부터 약 이 년 전부터 시작된 그의 발자취는 거인의 그것처럼 깊고, 동시에 거대했다.

조금씩 무너져 가던 태원진가가 산서성을 넘어 북방 초원까지 아우르는 일대의 패자가 된 것도 모자라, 오대세가(五代世家)의 일원으로 자리 잡은 것은 그가 이루어 낸 것 중에서도 일부에 불과했다.

진태경은 화왕 적천강의 후인이자 열화문의 계승자였고, 내로라하는 무림의 영수(領袖)들과 새로운 무림맹의 깃발을 들어 올린 젊은 거인이었으며, 나이가 믿기지 않을 정도의 무위를 바탕으로 암천과 맞서 싸우는 협의지사(愜意志士)였다.

이제, 천하의 무림인 중 진태경의 이름을 모르는 이는 없었다.

열화신룡(烈火神龍)이라는 네 글자에 실린 의미와 무게를 의심하거나 질시하는 이들 또한 존재하지 않았다.

아니, 감히 그럴 엄두조차 내지 못했다.

진태경은 스스로 증명했고, 수많은 이목이 그 모든 것을 똑똑히 지켜보았으니까.

그리고 이는, 비단 무림(武林)이라는 강철의 울타리 속에서만 벌어지는 일이 아니었다.



천하의 만백성에게 고하노라!



천자(天子).

하늘을 대신하여 강산을 다스린다는 위대한 존재가 온 세상에 천명(天命)했다.

그간 암천이 벌여 온 모든 흉계를 밝힌 황제는 하나밖에 남지 않은 자신의 아우를 황태제(皇太弟)로 세우고, 사막 너머의 악귀들을 역적으로 선포했으며, 기나긴 세월 동안 관과 무림 사이에 놓여 있던 단단한 성벽을 단숨에 허물어트렸다.

다름 아닌 상산후(上山侯) 진태경이라는 공성추로.



천자의 이름으로 명하노니, 이제 하나가 되어 싸우라! 감히 순리를 거스르고자 하는 괴력난신의 역도들로부터 그대들의 강산을 수호하라!



그렇게 진태경이라는 이름은 무림을 넘어 구주팔황과 사해오호를 떨어 울리게 되었다.

그의 존재는 무림인들에게 있어 새로운 시대를 이끌어 갈 젊은 거인이었고, 수많은 백성들에게는 황실의 수호자이자 지엄하신 황제의 명을 받들어 역적을 토벌하는 천하 대장군으로 각인되었다.

무림인인 동시에, 황제가 친히 임명한 열후(列侯).

대국뿐만 아니라 그 어떤 역사 속에서도 전례를 찾아볼 수 없는 일이었으나, 이는 현실로 이루어졌고 젊은 영웅은 매 순간 이 끔찍한 난세의 종결을 위해 싸우고 있었다.

그리고, 또다시 승리했다.

“와아아아아!”

“대국과 무림이 비로소 하나가 되어 역도를 몰아내고 있으니, 이게 전부 황제 폐하의 치세와 상산후의 활약 덕분이 아니겠소!”

“이런 날에는 취하지 않을 수가 없지. 여기 술 한 동이, 아니 세 동이 내오시오!”

입과 입을 통해 전해지며 부풀려지기도 했으나, 구태여 그러지 않더라도 누구도 부정할 수 없는 대승.

객잔을 꽉 채운 것으로도 모자라 거리로 몰려나온 이들은 감숙에서의 승리를 안주 삼아 기쁘게 술잔을 기울였다.

그들은 하나같이 황제를 칭송하고, 천하 만민을 지키고자 목숨 걸고 싸운 진태경과 무림맹에 감사했으며, 그로 인해 자신들과 친지들이 안전할 수 있다는 사실에 안도했다.

어쩌면 이 전쟁이 별다른 피해 없이 금세 끝날 수도 있겠다는, 그저 막연한 기대와 희망에 부푼 채.

“자, 마시게! 어서!”

“들이켜! 쭉! 옳지!”

어딜 가나 웃음소리는 끊이지 않았고, 곳곳에서 커다란 잔치를 벌이는 사람들의 표정에서는 조금의 두려움도 찾아볼 수 없었다.

무림인도, 백성들도.

그들 모두는 크게 소리 내어 웃으며 승리의 기쁨을 마음껏 누렸다.

적어도 그날 하루만큼은.

머나먼 서쪽의 변방, 청해(靑海)에서부터 날아온 한 마리의 송골매가 지친 여정을 끝마치기 전까지는.



* * *



어릴 적에는 지난밤 꾸었던 꿈을 기억하지 못하면 무척이나 아쉬워했었다.

분명히 흥미진진한 이야기였을 텐데, 하면서.

하지만 어느 날인가부터 알게 되었다.

꿈을 기억하지 못한다는 것은, 적어도 악몽이 남긴 여운에 몸서리칠 일은 없다는 뜻이라는 사실을.

물론 그렇다고 한들, 악몽을 꾸었다는 사실 자체가 사라지는 것은 아니었다.

“자, 여기요.”

흔들리는 말안장 위에서 눈을 뜨자마자 보인 건 혁무진의 얼굴. 그리고 녀석의 손에 들린 천 조각이었다.

“……뭐야?”

“뭐긴 뭐예요. 받으세요. 제가 닦아 드릴 수는 없잖아요.”

“아.”

그제야 전신에 착 달라붙은 의복의 감촉이 생생하게 느껴졌다. 도대체 무슨 꿈을 꿨길래 이 정도의 식은땀이 난 걸까.

‘뻔하지.’

헌터가 된 이후, 내가 자주 꾸게 된 악몽에 등장하는 부류는 통상 두 가지로 나뉘었다.

내가 미처 구하지 못한 탓에 죽은 사람.

혹은 내 손에 죽은 사람.

‘아, 최근에는 오랜만에 하나 추가되긴 했네.’

나는 문득 떠올렸다.

정체불명의 이상한 꿈. 

내 머릿속에는 절대 존재할 수 없는, 대한민국의 진태경이 아닌 태원진가의 진태경이 겪었을 과거의 기억들을.

혹시 조금 전에 꾸었던 꿈도 비슷한 내용이었을까, 하는 생각을 내심 되새기고 있던 그때였다.

삐잇!

허공 어디에선가 울려 퍼진 날짐승의 울음소리가 잠깐의 상념을 깨트린다. 

마치 허상이나 다름없는 꿈이 아니라, 현재에 집중하라는 듯.

‘하긴, 그럴 때가 아니지.’

작게 고개를 내저은 나는 몸 안의 열양지기를 끌어올렸다.

화아악. 투둑.

자욱하게 뿜어져 나오는 수증기와 함께 축축하게 젖어 있던 옷이 단숨에 건조해졌다. 그 훈훈한 열기에 얼굴이 벌겋게 달아오른 혁무진이 얼빠진 목소리로 중얼거렸다.

“……아. 맞다. 이런 방법도 있었지.”

“그렇지. 너랑은 다르게.”

“……지금 기만하시는 겁니까?”

“응.”

“아니, 그렇게 말씀하시면 할 말이 없긴 한데…….”

혁무진이 떨떠름하게 말꼬리를 흐린 그 순간.

삐잇!

다시 한번 들려온 울음소리에, 나는 문득 고개를 들어 하늘을 바라보았다.

그리고 이내 눈을 부릅떴다.

“……!”

커다란 날개를 펼친 채 허공을 유영하는 매의 발목에, 붉게 젖은 전서(傳書)가 매달려 있었다.
```

## Final English reading copy

```markdown
# Chapter 1063

People say that a rumor without feet can travel a thousand *li*, while information with wings can reach tens of thousands of *li* away.

And that saying, which the information merchants of Murim held up like a proverb, was no exaggeration.

*Flap!*

On that day, when dark clouds covered the sky and death claimed the land, the sight of dozens of messenger eagles taking flight at the same time was quite a spectacle.

Leaving behind mountains of corpses and pools of blood, the eagles soared high into the sky, beating their great wings as they flew toward their separate destinations.

The snowfield, stained red, dwindled into a tiny drop of blood. The Great Snow Mountain Range, covered in eternal snow, disappeared from view.

The sun and moon traded places, day and night giving way to each other several times. The ocher-colored plateau, seeming to stretch to the ends of the world, vanished beyond the horizon.

And at last, when the dozens of messenger eagles had each completed their journeys, the realm of the Central Plains seethed like lava in a crater.

“Waaaaah!”

“Long live the Great Nation! Long live His Majesty the Emperor!”

“What are you all doing? Come on out! Hurry!”

Though the time and place differed, everyone who heard of the great event in Gansu Province rushed into the streets and cheered.

Some were roused from a sound sleep before dawn by the sudden commotion. Even they, stumbling out past their gates, felt more bewildered than angry.

“Which goddamn fools are making a racket at this hour, when even the hens are fast asleep… Hey, you lot! What the hell are you doing carrying on in front of someone else’s house?”

On an ordinary day, sharp words like those would probably have led to people grabbing each other by the collars first and asking questions later.

But the crowd, cheering and shouting as they chased away the dawn, was too excited to do anything but yell again and again.

“A great victory! A great victory!”

“What are you talking about? That’s not what I asked—wait. A great victory?”

“Good heavens, look at you. You haven’t heard the news yet, have you?”

“You haven’t heard? The rebels from Xinjiang invaded Gansu without knowing their place, and got wiped out to the last man!”

“What? They went after Gansu?”

Only then did those who’d just heard the news widen their eyes. Their shock was the same, no matter their station.

How could it not be?

Just a year ago, Dark Heaven was a name known only to the sharp-eyed and sharp-eared. Now even a country bumpkin in some remote village, living hand to mouth, knew of them.

The rebels of Xinjiang. Fiends from beyond the desert.

Even the Demonic Cult, whose infamy had unleashed a storm of blood half a century ago in what was called the Great Faction War, could not compare to Dark Heaven today.

The Demonic Cult of old had sought to conquer the Murim of the Central Plains. Dark Heaven sought to claim the world itself.

Defying heaven.

The two characters said it all: a band of rebels who would overturn heaven, defy the natural order, and destroy the unified dynasty and peace established after countless turbulent eras.

That was Dark Heaven. And so the people of the Great Nation were still roaming the streets, cheering at that very moment.

“Good heavens, what a joyous occasion. But just how great a victory did you win to get everyone so worked up?”

At someone’s question—one that had chased away the last of his sleep—a proud answer rang out from the crowd.

“Don’t be shocked. From what I hear, tens of thousands of rebels were killed or captured in a single battle.”

“Gasp! Tens of thousands!”

The numbers were staggering—far beyond those of a mere cult—and so was the victory they represented. They had barely caught their breath when voices elsewhere in the crowd rose to contradict the claim.

“What nonsense! A martial artist I know well told me that a hundred thousand were wiped out in half a day.”

“A hundred thousand? Wasn’t it three hundred thousand?”

“What are you all talking about? I heard more than a million rebels were annihilated!”

“Now, that’s enough nonsense. However you look at it, a million is too many, isn’t it?”

“Then let’s split the difference and call it half a million. No—three hundred thousand.”

“Three hundred thousand is still too many. Where did you even hear that?”

“Are you with Dark Heaven? Can’t you read the room?”

“Why are we suddenly talking about—”

“So, are we going with three hundred thousand or not?”

“…Is that something I get to decide?”

“Ah, three hundred thousand! Just so you know, I’m not budging any further!”

“O-okay. Fine. I’ll remember it as three hundred thousand, so please calm down.”

“Now we’re getting somewhere. Come on, repeat after me: Long live the Great Nation!”

“L-long live the Great Nation.”

“Hey! I can barely hear you!”

“L-long live!”

“Much better. Now, long live the Murim Alliance!”

“…When is this going to end?”

“We’re not done yet. Next is the Blazing Flame Divine Dragon—no, long live the Marquis of Shangshan! Prepare yourself.”

A few people looked less than thrilled, but most of the common folk cheered the Murim Alliance without holding back.

And that was a remarkable change in public opinion, even compared to just a few years ago.

The orthodox faction, led by the Nine Sects and One Gang and the Five Great Families, had ruled the Murim of the Central Plains. But a long peace had brought corruption, and power had bred injustice.

Did wearing spotless white make the heart beneath it white, too?

Still waters were bound to grow foul eventually. Perfect good and evil existed nowhere.

But now things were different.

“Long live the Marquis of Shangshan!”

“Long live the Blazing Flame Divine Dragon!”

Whenever people thought about how much had changed because of a single person, they couldn’t help but marvel all over again.

Jin Taekyung.

His path, which had begun about two years ago, was as deep and immense as the footsteps of a giant.

The Jin Family of Taiyuan, which had been crumbling bit by bit, had become a power ruling over Shanxi Province and the northern grasslands. It had even secured a place among the Five Great Families. And that was only one of his many achievements.

Jin Taekyung was the heir of the Fire King, Jeok Cheongang, and the successor to the Fire Gate Clan. He was a young giant who had raised the banner of a new Murim Alliance alongside the most renowned leaders of Murim. And with martial prowess beyond belief for his age, he was a righteous hero who fought against Dark Heaven.

There was no martial artist under heaven who didn’t know Jin Taekyung’s name.

Nor was there anyone who doubted or resented the meaning and weight behind the four characters *Blazing Flame Divine Dragon*.

No. No one would even dare.

Jin Taekyung had proven himself, and countless eyes had watched it all with their own eyes.

And this wasn’t happening only within the iron fence of Murim.


“To all the people under heaven, hear this!”

The Son of Heaven.

The great ruler who governed the realm on heaven’s behalf had proclaimed his mandate to the whole world.

The Emperor revealed all the schemes Dark Heaven had carried out. He named his only surviving younger brother Imperial Younger Brother and heir apparent, declared the fiends beyond the desert traitors, and in a single stroke tore down the sturdy wall that had stood between the government and Murim for ages.

He used none other than Jin Taekyung, the Marquis of Shangshan, as his battering ram.

“By the command of the Son of Heaven, I order you: unite and fight! Protect your land from the rebels who dare defy the natural order and seek to wield supernatural powers!”

And so the name Jin Taekyung resounded beyond Murim, echoing across the Nine Provinces and Eight Wastes, the Four Seas and Five Lakes.

To the martial artists, he was a young giant who would lead a new era. To countless common folk, he was the guardian of the imperial court and the Great General of the realm, who obeyed the Emperor’s solemn command and put down traitors.

A martial artist, and at the same time a marquis personally appointed by the Emperor.

There was no precedent for such a thing in the history of the Great Nation—or anywhere else. And yet it had become reality. The young hero fought with every passing moment to bring an end to this terrible age of chaos.

And once again, he had won.

“Waaaaah!”

“The Great Nation and Murim have finally united to drive out the rebels! Isn’t it all thanks to His Majesty’s wise reign and the Marquis of Shangshan’s efforts?”

“On a day like this, there’s no way I’m not getting drunk. Bring me a jar of wine! No—three jars!”

The story grew as it passed from mouth to mouth, but even without the embellishments, it was a victory no one could deny.

The taverns were packed. Those who spilled out into the streets happily raised their cups to toast the victory in Gansu.

They praised the Emperor as one. They thanked Jin Taekyung and the Murim Alliance for risking their lives to protect the people of the realm, and felt relieved that they and their loved ones were safe because of them.

They were buoyed by a vague hope that the war might soon end without much further loss.

“Come on, drink! Hurry!”

“Down the hatch! That’s it!”

Laughter rang out wherever one went. In the towns where people held great feasts, there wasn’t a trace of fear on anyone’s face.

The martial artists and the common folk alike.

They all laughed loudly and reveled in the joy of victory.

At least, for that one day.

Until a peregrine falcon, having flown from Qinghai on the distant western frontier, completed its weary journey.

* * *

When I was a kid, I used to be really disappointed if I couldn’t remember a dream from the night before.

*It must’ve been a good one, too.*

But at some point, I learned something.

Not remembering a dream meant I could at least avoid shuddering at the lingering feeling of a nightmare.

Of course, that didn’t mean the nightmare itself had never happened.

“Here.”

The first thing I saw when I opened my eyes on the swaying saddle was Hyuk Mujin’s face. He held out a scrap of cloth.

“…What’s this?”

“What does it look like? Take it. It’s not like I can wipe you down myself.”

“Oh.”

Only then did I notice how vividly my clothes clung to my body. What the hell had I been dreaming about to work up that much of a cold sweat?

*I know.*

Since becoming a Hunter, the nightmares I often had had generally fallen into two categories.

People who died because I couldn’t save them.

Or people who died by my hand.

*Actually, there is one more, recently.*

I remembered it suddenly.

A strange, unidentifiable dream.

Memories of the past that Taewon Jin Family’s Jin Taekyung had lived through—memories that couldn’t possibly exist in my head, because I was Jin Taekyung of Korea.

I was mulling over the thought that the dream I’d just had might have been something like that, when—

*Screee!*

A bird’s cry rang out from somewhere overhead, breaking my brief reverie.

As if to tell me to focus on the present, not a dream that was little more than an illusion.

*Right. This isn’t the time.*

I shook my head and drew up the Scorching Yang Qi within me.

*Whoosh. Crackle.*

Steam billowed out, and my damp clothes dried in an instant. Hyuk Mujin’s face flushed from the gentle warmth, and he muttered in a dazed voice:

“…Oh. Right. You could do that.”

“Sure. Unlike you.”

“…Are you bragging right now?”

“Yeah.”

“I mean, if you put it that way, I don’t have anything to say…”

Hyuk Mujin let his words trail off, still not quite satisfied. At that moment—

*Screee!*

The cry rang out again. I looked up at the sky without thinking.

And then my eyes widened.

“……!”

A missive, wet with blood, was tied to the leg of a falcon gliding through the air with its great wings spread wide.
```
