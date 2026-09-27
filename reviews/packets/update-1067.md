<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1067.txt",
      "sha256": "42d6cc1932771e264fa314a07a72b98e1fb71e9eac41cfc46853ada1570d2a52",
      "bytes": 12553
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3c389c7e8286fd9c0d55bfd9f72d3b1db30510ec1868eeef9010b64d3fa8f8c9",
      "bytes": 1111
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "30eaa2be30abc53c7f0555f378868db0fa2a48f03969e97280dbb9724020e47a",
      "bytes": 242084
    },
    {
      "path": "characters/Cang Gong.md",
      "sha256": "fae2d3aaaaf50a3d6af769da21762d4c190968c35e2d5bb42de6b864f755fee0",
      "bytes": 778
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f75a6cea421e6accf113f7167fd9be128106a3dc2eab82f8ce5ed92bd6fe6a00",
      "bytes": 760
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "84bbd2162a9075ea0510d9137c7f1469f1deab0f9cd9f58aeeb7b7f1d81a5ca8",
      "bytes": 839
    },
    {
      "path": "characters/Hak Woo.md",
      "sha256": "e2f918344d2a723f44110fabcbc6a0f5bd20ab9a1f4d31189cde296a9d85967f",
      "bytes": 612
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "aa008788b569fb30467e949ff41644d2e2e3e22ea33a76597554e9d17061b4de",
      "bytes": 651
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "cadae7ca91f861feac9486e606813d32ed30067880e18c31c0fd00625f1e31f9",
      "bytes": 1502
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "0bb616958ff97c6bf5d13fa931c40d004eb240936b543c21f7fbff59f371ff82",
      "bytes": 700
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "b1b8e87c70a15258a57be8dddaf8374a896ebd5e69dd420d9af0e8bda4c6fdb1",
      "bytes": 700
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "0580b9545abca680a096b4229e2e66c1ec3e5a1b5e081dc5c84161b78131e079",
      "bytes": 832
    },
    {
      "path": "characters/Namho.md",
      "sha256": "0972592a1982b463ee846eb9d1425cbdbc3979d2e91f879539efa8220386d7f5",
      "bytes": 1092
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "9922ad6de052789427be9a5d3f930987d1cee0e08405118e49c66fa40d8d8fa2",
      "bytes": 686
    },
    {
      "path": "characters/Wei Zhong.md",
      "sha256": "ef0ac2ef71c04a40349eecebadbca72b374fc891efc21f413abfae12496fe503",
      "bytes": 714
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "1ac8dc5b2856e6ece74f7fdd27ebde745e4188f34b12c969181f1facd6c7f96c",
      "bytes": 889
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3187f1a2d77b9ba4e276ef4ce8ab41c3fb3fa577b62db4b4a5c2fa391601eceb",
      "bytes": 283802
    }
  ],
  "estimated_tokens": 12053
}
-->

# Durable State Update — Chapter 1067

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
1 and safe_through 1067. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1067. Profile updates may replace only one
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
  "chapter": 1067,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1067,
    "continuity_sources": [1067],
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
    "The Emperor has called for the government and Murim to unite against Dark Heaven.",
    "Dark Heaven occupies Kunlun; the Kunlun Sect and its allies retreated to Qinghai Lake, suffering about a thousand killed or wounded.",
    "Jin Taekyung’s roughly three-thousand-strong allied force has entered northwestern Qinghai with the help of the Great Sir.",
    "Taekyung’s force pauses to rest in the mountains as unknown enemies approach.",
    "The allied force includes the Kongtong Sect, Zhongnan Sect, Black Dragon Demon Gate, and Embroidered Uniform Guard.",
    "Sama Pyo exposed and dealt with traitors among Gansu’s faction leaders before the departure.",
    "Ma Sanbao now serves the Blood Lord and has found something sought by Dark Heaven."
  ],
  "continuity_sources": [
    1066
  ],
  "open_questions": [
    "What has Ma Sanbao found?",
    "What enemies are approaching Taekyung’s force?",
    "Why does the System prevent Jin from logging out beyond the incomplete linked Quest?"
  ],
  "safe_through": 1066,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 적천강    | **Jeok Cheongang** |
| 궁성     | **Bow Saint**                 | —              |
| 곤륜파    | **Kunlun Sect**                  |
| 암천     | **Dark Heaven**                  |
| 십봉룡    | **Ten Dragons and Phoenixes**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마교     | **Demonic Cult**                                 |                                                       |
| 제자     | **Disciple**                                 |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 도사      | **Daoist**                                                      |
| 창공 | **Cang Gong** | The bedridden East Depot leader for whom Ma Sanbao acts. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 학우 | **Hak Woo** | Kunlun Sect top young prodigy known as the Kunlun Cloud Dragon; Taekyung addresses him as Hak. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 위충 | **Wei Zhong** | The pledge’s first signer and the personal name of Lord Cang Gong. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 성라대연 | **Star-Array Grand Banquet** | Major martial gathering held in Henan every two or three years. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 곤륜운룡 | **Kunlun Cloud Dragon** | Epithet of a Kunlun Sect young prodigy. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 삼도천 | **Sanzu River** | Buddhist river associated with the boundary between life and death; footnote on first use. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 무량수불 | **Infinite Life Buddha** | Buddhist invocation used by Taekyung. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 천호 | **Thousand Captain** | Rank held by Jeong Hogun in the Embroidered Uniform Guard. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 정호군 | 태산 | guard officer questioning a performer | you | blunt and direct | He calls Taishan forward and asks whether he belongs to the circus troupe. |
| 마삼보 | 정호군 | East Depot de facto leader to Embroidered Uniform Guard Thousand Captain | Commander Jeong | courteous and controlled | Ma Sanbao addresses him as 정 천호 while asserting procedural limits and drawing him into a conversation. |
| 정호군 | 마삼보 | Embroidered Uniform Guard Thousand Captain to East Depot official | Eunuch Ma | formal and guarded | Jeong Hogun addresses him as 마 태감 and shows wariness despite his restrained replies. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 적천강 | 창공 | hostile opponents | you; you bastard | blunt and threatening | Jeok Cheongang uses 네놈, 이 불알 없는 놈, and 호로새끼 while taunting Cang Gong. |
| 창공 | 적천강 | hostile opponents | Fire King Jeok Cheongang | taunting and sardonic | Cang Gong names Jeok by his title, then comments on how alike master and disciple are. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 마삼보 | 동천마군 | disciple_to_master | Master | deferential | Ma Sanbao addresses the Eastern Heaven Demon Lord as 스승님 when rejoining him. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |

## Listed compact profiles

### Cang Gong.md

# Cang Gong (창공)

- **Safe through:** Chapter 940
- **Aliases:** None
- **Role:** Cang Gong is the Eastern Heaven Demon Lord’s assumed identity, through which he became the East Depot’s Brush-Holding Eunuch and a power second only to the Emperor.
- **Personality:** Calculating and self-assured, he is driven by vengeance and believes the rulers and the world betrayed him first.
- **Voice:** Dry and sardonic, he delivers taunts and judgments in measured statements.
- **Relationships:** He was raised by a master and fellow disciples in the Maoshan Sect, whose members died resisting the forced relocation of the capital; Ma Sanbao is his disciple, and he regards Jin Taekyung as a potential recruit.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1066
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 1049
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hak Woo.md

# Hak Woo (학우)

- **Safe through:** Chapter 997
- **Aliases:** Kunlun Cloud Dragon
- **Role:** Hak Woo is the Kunlun Sect's greatest young prodigy and is known as the Kunlun Cloud Dragon.
- **Personality:** He is wary, easily intimidated by threats to his hair, and eager to avoid unnecessary confrontation.
- **Voice:** He speaks politely and defensively, frequently using Daoist invocations.
- **Relationships:** Jin Taekyung is his former rival and can pressure him into leaving, while Ju Hwaran is an acquaintance he addresses formally.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1066
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1066
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1065
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1065
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 1066
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s former Brush-Holding Eunuch, a sorcerer and former Disciple of another Demon Lord who now serves the Blood Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, served the Eastern Heaven Demon Lord, and led a restoration effort for Prince Shangshan; he now serves the Blood Lord.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1058
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1065
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Wei Zhong.md

# Wei Zhong (위충)

- **Safe through:** Chapter 929
- **Aliases:** None
- **Role:** Wei Zhong, addressed as Cang Gong, was the East Depot’s Seal-Holding Eunuch and Eastern Heaven Demon Lord; Jin Taekyung killed him with White Flame.
- **Personality:** Politically perceptive and self-possessed, he uses courteous remarks and veiled barbs to challenge the Emperor.
- **Voice:** He speaks in formal, deferential language, using repeated praise and respectful address to deliver pointed challenges.
- **Relationships:** He has a long-standing connection to the Emperor, with whom he exchanges polite but adversarial remarks about the succession.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 1049
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
1067화




반 시진.

그것은 청해성에서의 첫 전투가 시작되고, 끝나기까지 걸린 시간이었다.

“여기 있었군.”

어느새 짙은 피비린내가 감도는 숲속.

이름 모를 적의 몸뚱아리 위에 주저앉아 호흡을 가다듬던 나는, 목소리가 들려온 방향을 따라 고개를 돌렸다.

철퍽.

피와 진흙을 짓뭉개며 성큼성큼 다가오는 발걸음.

본래의 황금빛 광채를 잃어버린, 붉게 물든 갑주를 걸친 익숙한 얼굴이 시야에 들어왔다.

“여기 계셨습니까, 라고 해야겠지?”

내 말에 작게 한숨을 내쉰 금의위 천호 정호군이 입을 열었다.

“여기 계셨습니까. 이제 됐나?”

“전혀 아니지. 뒷말에서 갑자기 혀가 반 토막이 됐잖아.”

“……적당히 하지. 피차 고생한 처지에.”

“안 그래도 그러려고. 아군의 피해 상황은?”

“피해라고 하기도 무색하지. 사상자라고 해 봤자 고작 삼십여 명뿐이니까. 그마저도 죽은 이는 아무도 없고.”

시체가 가득 쌓인 주위를 둘러본 정호군이 덧붙였다.

“천여 명이나 되는 적들을 전멸시킨 것치고는, 실로 기적 같은 결과지.”

삼천 대 일천.

비록 아군이 시작부터 수적 우위를 점한 상황이었다고는 해도, 전사자가 한 명도 없다는 것은 터무니없을 정도의 대승이다.

이 모든 것이 반 시진이라는 짧은 시간 만에 만들어 낸 결과라는 것을 생각한다면 더욱더.

하지만 정호군을 향한 내 대답은 담담했다.

“기적이 아니야. 당연한 결과지.”

“부정할 수는 없군. 전력 차가 워낙 극심했으니.”

이런 성과를 거둔 것에는 아군 모두가 나름대로 가려 뽑은 정예라는 것도 한몫했겠지만, 그보다는 초절정 고수들의 활약이 너무나도 컸다.

궁성. 적천강. 현천진인. 나.

마지막으로 딱히 도움은 되지 않았지만, 대인까지도.

이 정도의 전력 차라면 승리하는 것보다 패배하는 게 더 어려울 정도다.

다만 한 가지 문제가 있다면…….

“다들 어때?”

“어때 보이나?”

망설임 없이 되돌아온 정호군의 반문에, 나는 입맛을 다셨다.

솔직히 물어볼 필요도 없었다.

당장 고개를 들어 주위를 둘러보아도 온통 딱딱하게 굳은 얼굴들뿐이었으니까.

별다른 피해 없이 엄청난 대승을 거두었음에도 아군들의 표정은 하나같이 창백하게 질려 있었고, 눈빛에는 희미한 두려움이 깃들어 있었다.

마치, 보아서는 안 될 끔찍한 무언가를 목격한 사람들처럼.

그리고 그것은 틀림없는 사실이기도 했다.

당장 지금 이 순간에도 내 엉덩이 밑에 깔린 채 꿈틀거리고 있는 이름 모를 적 또한, 분명 괴물이라 칭할 만한 존재였으니까.

- 크륵, 크르륵.

갈라진 목젖 사이로, 흐릿하게 새어 나온 괴성.

그제야 괴물의 존재를 알아차린 정호군이 미간을 좁혔다.

“아직 살아 있었나.”

“글쎄. 이것도 살아 있는 거라 말할 수 있다면, 그런 거겠지.”

그 저주받은 괴물을, 나는 물끄러미 내려다보았다.

처참하게 잘려 나간 사지와 부패한 몸뚱어리.

이미 며칠 전에 죽음을 맞이한 것이 분명한 괴물은, 삼도천(三途川)을 건너지 못하고 이승에 남아 끈질기게 몸부림치고 있었다.

생전의 자신이 누구였는지조차 기억하지 못한 채.

그러나 온통 찢어지고 헤진 괴물의 옷자락에 수실로 새겨진 두 글자는, 여전히 주인을 기억하고 있었다.

“곤륜(崑崙)…….”

정호군의 침음성에 나는 조용히 고개를 끄덕였다.

맞다.

이 괴물은 다름 아닌 곤륜파의 제자다.

아니, 였었다.

“곤륜산에서 퇴각하는 과정에서 사상자가 발생했다고 하더니, 그중 하나였던 모양이군.”

“그렇겠지. 아마도.”

“혹시, 그대가 아는 사람인가?”

조심스러운 정호군의 물음에 나는 고개를 저었다.

“아니, 전혀.”

성라대연 당시 곤륜파 최고의 후기지수이자 십봉룡의 일원이던 곤륜운룡(崑崙雲龍) 학우와 인연을 맺기는 했지만, 이제는 괴물이 되어 버린 이 도사의 얼굴은 기억 속에 없다.

그러나, 누가 그를 이와 같은 괴물로 만들었는지는 얼핏 짚이는 구석이 있었다.

“어때, 제법 눈에 익지?”

“그래.”

일순간, 정호군의 눈동자가 깊게 가라앉았다.

“창공(廠公). 그자가 부리던 사술과 놀라울 만큼 흡사하군.”

위충.

동창장인태감(東廠掌印太監), 소위 창공이라 불렸던 그에게는 가장 깊은 비밀이 두 가지 있었다.

첫 번째는 그가 천주의 충복 중 하나인 동천마군(東天魔君)이라는 것이고.

두 번째는 오래전 황실에 의해 멸문당한 모산파(茅山派)의 후예였다는 사실이었다.

하지만 그런 위충이 내 손에 최후를 맞이한 이후에도, 모산파의 명맥은 완전히 끊어지지 않았다.

“마삼보. 그놈이야.”

위충의 모든 것을 물려받은 제자.

자신의 스승처럼 가면을 쓴 채 동창의 태감으로 암약하던 그의 시체는 끝끝내 찾을 수 없었고, 이는 한 가지 사실만을 의미했다.

“어디로 갔나 했더니. 결국 끈질기게 살아남아 암천과 합류한 모양이군.”

물론 마삼보가 아닐 수도 있다.

적천강의 말에 따르면 위충이 보여 준 강시공(僵尸功)은 기존의 한계를 아득히 벗어났다고 했고, 이는 곧 천주의 도움으로 개량되었음을 뜻하니까.

하지만 암천에서 강시공을 다루는 이들을 키워 냈다고 한들, 위충과 가장 가까운 곳에서 직접 사사한 마삼보의 경지만큼은 아닐 것이다.

더군다나.

‘이곳 청해는 놈들에게도, 우리에게도 중요한 전장이야. 그렇기에 어느 때보다 총력을 가하는 것일 테고.’

이미 십만을 아우르는 암천의 대군세가 청해성의 절반을 집어삼킨 상황.

도대체 천주가 무슨 이유로 감숙성에서의 패배를 의도했는지는 모르겠지만, 이번만큼은 그 어느 때보다 총력을 다할 것이 분명했다.

제아무리 과거의 마교를 아득히 뛰어넘은 전력을 갖춘 암천이라 한들, 십만에 달하는 병력을 단순히 먹잇감으로 던져 줄 리는 없을 테니까.

‘마삼보 역시 승리를 위해 필요한 조각 중 하나. 절대 빼놓을 수 없겠지.’

그 순간 문득 뇌리를 스치는 어떤 생각에, 나는 새어 나오려는 침음성을 삼켰다.

십만에 달하는 적들이 전부 강시화 되어 있다면, 이건 도저히 막을 수 없는 재앙이다.

더군다나…….

‘천주. 그놈이 직접 전장에 모습을 드러낼 수도 있다.’

제대로 대면한 적조차 없었음에도, 나는 천주라는 두 글자를 떠올린 순간 가슴이 무겁게 가라앉았다.

어찌 잊을 수 있을까.

지금까지 천주가 모습을 드러낸 것은 단 한 번뿐이었고, 나는 그 모든 순간을 선명하게 기억하고 있었다.



‘재미있군. 재미있어.’



그 날, 그 순간 나와 적천강을 바라보며 웃고 있던 것은 서천마군(西天魔君)이 아니었다.

한 인간의 몸을 빌린 악마였고, 심연의 어둠 그 자체였으며, 그 누구라 할지라도 대적할 수 없을 것 같은 절대자였다.



‘다음에 또 보도록 하지.’



하지만 그날 이후, 천주는 두 번 다시 내 앞에 모습을 드러내지 않았다.

그저 짙은 어둠 속에 웅크린 채, 모든 것을 지켜볼 뿐이었다.

서천마군을 포함한 자신의 충복들이 하나둘씩 최후를 맞이 할 때도, 적지 않은 공과 세월을 들여 준비한 계획이 차근차근 분쇄될 때에도.

천주는 나타나지 않았다.

하지만 동시에 모든 것을 주시하고 있었다.

천하의 그 누구도 짐작할 수 없는, 천주 자신만이 알고 있을 순간만을 기다리며.

더불어 나는 천주가 원하는 그 순간이 그리 머지않았음을 마음속으로 직감하고 있었다.

그것이 나 자신과 매우 깊고 선명히 연결되어 있다는 사실도 함께.

‘도대체 나를 통해서 뭘 얻고자 하는 거지?’

그리고 도무지 해결되지 않는 의문을 머릿속으로 되뇌인 그 순간.

쐐애애액, 뻑!

일순간 울려 퍼진 파공성과 함께, 상념에서 깨어난 나는 그리 멀지 않은 곳에서 들려온 외침을 들을 수 있었다.

“오, 잡았다! 잡았어!”

“와! 대인! 대단하다! 태산이 진심으로 감탄했다!”

“엣헴. 보았는가? 내가 마음만 먹으면 이런 것 정도는 아주 손쉽게 할 수 있다네.”

무슨 일인가 싶어 보니, 한껏 으스대는 대인의 손에 웬 날짐승 한 마리가 붙잡혀 있었다.

머리가 곤죽이 된 것을 보아하니 돌팔매질로 급사한 모양.

그리고 태산은 그런 대인을 보며, 정확히는 날짐승을 보며 군침을 흘리는 중이었다.

“맛있, 아니 멋있다! 태산이가 불 피울 테니 얼른 굽자!”

적진 한가운데에서 캠프 파이어라니, 나를 포함한 다른 이들의 가슴에 불을 지르는 개소리였지만 어느 정신 나간 인간은 달랐다.

“젊은 친구가 제법 도리를 지킬 줄 아는구먼. 수고해 주는 값으로 내 살점 좀 떼어 줌세. 어느 부위를 선호하나?”

“다리! 무조건 다리!”

“닭 좀 씹어 본 친구로군. 좋아. 하나는 양보하지.”

“두 개! 전부!”

“……선 넘지 말게.”

갑자기 정신이라도 차린 듯, 급정색한 대인의 모습에 태산이 시무룩하게 고개를 숙인 그때였다.

“아주 염병들을 떨고 자빠졌네. 어디서 굴러먹다 왔는지 악취가 진동을 하는데 먹긴 개뿔이.”

이제는 제 자리처럼 편안하게 태산의 어깨에 걸터앉은 남호의 한마디에, 어떤 생각이 불현듯 뇌리를 스쳤다.

‘잠깐, 설마?’

그리고 그 설마 했던 마음은, 날짐승을 확인한 정호군의 말을 듣는 순간 역시로 바뀌었다.

“썩었군. 뼈가 드러날 정도로.”

“그렇다는 건.”

“아무래도…… 괴물이 지상에만 있던 건 아닌 모양이야.”

애초에 낯선 인간들이 영역을 침범했는데 새가 남아 있던 것부터 이상한 일.

뒤늦게 상황을 알아차린 사람들의 시선이 쏠리자, 대인이 영문을 모르겠다는 얼굴로 눈을 껌뻑였다.

“무슨 문제라도 있나? 그냥 저놈이 나뭇가지 위에서 빤히 쳐다보길래…….” 

“쳐다봤다고요?”

내 물음에 대인이 고개를 끄덕였다.

“확실하네. 눈깔도 시뻘건 게, 하도 기분이 나빠서 확 그냥 돌팔매질을 갈겨 버렸지.”

“……패밀리어(Familiar)?”

“응? 뭐라고 했나?”

“별거 아닙니다. 그냥 혼잣말이에요.”

대인을 향해 손을 내저은 나는 허공을 말없이 노려보았다. 

이제야 동쪽으로부터 서서히 번져오는 서광(曙光)을 받아, 아득히 높게 솟은 나뭇가지들 사이로 드문드문 드러나는 윤곽들이 있었다.

어둠 속에 숨어 있던, 그리고 어둠의 힘으로 되살아난 괴물들.

‘이미 감시 중이었어.’

나는 머릿속이 차갑게 식는 것을 느끼며 천천히 일어났다.

그리고 아직도 영문을 몰라 하는 대인을 향해 말을 건넸다.

“앞으로도 저런 새들이 있으면, 보이는 족족 전부 죽이세요.”

“전부?”

“예. 전부.”

“그건 좀. 아무리 그래도 귀한 생명 아닌가.”

뭐라고 할까 잠시 고민하던 나는 짧게 대답했다.

“해로운 새라서 그래요.”

“오. 그럼 죽여야지.”

“부탁합니다.”

대인의 어깨를 두드려 주고 자리를 뜨려던 나는, 잊고 있던 한 가지 사실을 깨닫고 걸음을 멈췄다.

그리고 조용히 뇌까리며 손을 뻗었다.

“무량수불.”

푹.

완전히 움직임을 멈춘 괴물을, 곤륜파의 제자를 뒤로한 채 나는 걸음을 옮겼다.

이제는 한시가 급하다.

감시의 눈이, 추격자들이 따라붙을테니.
```

## Final English reading copy

```markdown
# Chapter 1067

Half a shichen.

That was how long the first battle in Qinghai had taken—from its beginning to its end.

“So this is where you were.”

The forest now reeked of blood.

I sat on the body of an enemy I didn’t recognize, catching my breath. Then I turned toward the voice.

*Squish.*

Footsteps squelched through blood and mud as someone strode closer.

A familiar face came into view, clad in armor stained red and stripped of its original golden luster.

“Shouldn’t you say, ‘So this is where you were, sir’?”

Jeong Hogun, the Embroidered Uniform Guard Thousand Captain, let out a small sigh before answering.

“So this is where you were, sir. Happy now?”

“Not even close. You suddenly dropped half your tongue for the second part.”

“...Cut it out. We’ve both been through enough.”

“I was about to. How are our casualties?”

“Calling them casualties feels like an insult. We have only around thirty wounded, and not a single one of them died.”

Jeong Hogun glanced around at the heaps of bodies and added,

“A miraculous result, considering we wiped out more than a thousand enemies.”

Three thousand against one thousand.

Even though we’d started with the advantage in numbers, winning without a single fatality was an absurdly decisive victory.

Even more so when you considered we’d achieved all this in the space of half a shichen.

But my answer to Jeong Hogun was matter-of-fact.

“It wasn’t a miracle. It was only natural.”

“I can’t argue with that. The difference in strength was simply overwhelming.”

Our troops had all been chosen for their skill, each faction bringing its own elite. But more than anything, the Supreme Peak masters had made an enormous difference.

Bow Saint. Jeok Cheongang. Perfected Being Hyeoncheon. Me.

And last of all, even the Great Sir—though he hadn’t been much help.

With a difference in strength like that, losing would have been harder than winning.

There was only one problem…

“How’s everyone doing?”

“What do they look like?”

At Jeong Hogun’s immediate question in return, I clicked my tongue.

Honestly, there was no need to ask.

I could look around and see nothing but rigid faces.

Despite our overwhelming victory and almost nonexistent losses, every one of our allies looked deathly pale. A faint fear lingered in their eyes.

As if they’d witnessed something horrible they were never meant to see.

And that was exactly what had happened.

The unknown enemy writhing beneath my ass right now was undeniably a monster.

*Grrk. Grrrk.*

A hoarse cry seeped through its torn throat.

Only then did Jeong Hogun notice the monster and furrow his brow.

“It’s still alive?”

“Maybe. If you can call this being alive.”

I gazed down at the cursed monster.

Its limbs had been brutally severed, and its body was rotting.

It had clearly died days ago, yet it hadn’t crossed the Sanzu River[^1] and passed on to the next world. It remained here, writhing stubbornly.

It couldn’t even remember who it had been in life.

But two characters embroidered with thread on its torn and ragged robe still remembered their owner.

“Kunlun…”

At Jeong Hogun’s low murmur, I quietly nodded.

That was right.

This monster was none other than a Disciple of the Kunlun Sect.

No—it *had been* one.

“I heard there were casualties during the retreat from Kunlun Mountain. I suppose this was one of them.”

“Probably.”

“Did you know him?”

I shook my head at Jeong Hogun’s cautious question.

“No. Not at all.”

I’d crossed paths with Hak Woo—the Kunlun Cloud Dragon, the Kunlun Sect’s greatest young prodigy and a member of the Ten Dragons and Phoenixes—during the Star-Array Grand Banquet. But I didn’t recognize the face of this Daoist, now turned into a monster.

Still, I had a rough idea who might have made him this way.

“What do you think? Look familiar?”

“Yes.”

Jeong Hogun’s eyes darkened.

“Cang Gong. This is astonishingly similar to the dark arts he used.”

Wei Zhong.

The East Depot’s Seal-Holding Eunuch, known as Cang Gong, had two deep secrets.

The first was that he was the Eastern Heaven Demon Lord, one of the Lord of Heaven’s most loyal servants.

The second was that he was a descendant of the Maoshan Sect, which had been wiped out by the imperial family long ago.

But even after Wei Zhong met his end at my hands, the Maoshan Sect’s legacy hadn’t been completely extinguished.

“Ma Sanbao. It has to be him.”

The Disciple who’d inherited everything from Wei Zhong.

Like his Master, he’d worn a mask while working in secret as an East Depot eunuch. His body had never been found, and that could only mean one thing.

“So that’s where he went. He must’ve clung to life and joined Dark Heaven after all.”

Of course, it might not be Ma Sanbao.

According to Jeok Cheongang, the Corpse Art Wei Zhong had shown him had far surpassed its former limits. That meant it had been improved with the Lord of Heaven’s help.

But even if Dark Heaven had trained others to use the Corpse Art, none could match Ma Sanbao, who’d learned directly from Wei Zhong himself.

Besides…

*Qinghai is an important battlefield for them and for us. They’ll be committing more troops than ever.*

Dark Heaven’s army of a hundred thousand had already swallowed half of Qinghai Province.

I couldn’t begin to guess why the Lord of Heaven had intended for them to lose in Gansu, but this time, he’d surely commit everything he had.

Even Dark Heaven, with strength that far surpassed the Demonic Cult of the past, wouldn’t throw a hundred thousand troops away as mere bait.

*Ma Sanbao is another piece they need to win. They wouldn’t leave him out.*

A thought flashed through my mind, and I swallowed the groan that threatened to escape.

If all a hundred thousand enemies had been turned into jiangshi, it would be an unstoppable disaster.

And on top of that…

*The Lord of Heaven could show up on the battlefield himself.*

I’d never even faced him properly, but the thought of those two words made my heart sink.

How could I forget?

The Lord of Heaven had appeared only once, and I remembered every moment of it clearly.



*“Interesting. Very interesting.”*



That day, the one who’d watched Jeok Cheongang and me with a smile hadn’t been the Western Heaven Demon Lord.

He’d been a demon borrowing a human body. The darkness of the abyss itself. An absolute being who seemed beyond the reach of anyone.



*“Until next time.”*



But after that day, the Lord of Heaven never appeared before me again.

He simply crouched in the deepest darkness, watching everything.

Even as his loyal servants, including the Western Heaven Demon Lord, met their ends one by one. Even as the plans he’d spent considerable effort and years preparing were systematically dismantled.

The Lord of Heaven never appeared.

But he was watching everything all the same.

Waiting for a moment that no one in the world could guess—the moment only he knew.

And deep in my heart, I sensed that the moment he wanted wasn’t far off.

I also sensed that it was connected to me, deeply and unmistakably.

*What is he trying to get from me?*

The moment I repeated that unanswerable question in my head—

*Whoosh! Thwack!*

A sharp whistle cut through the air. Snapping out of my thoughts, I heard a shout from not far away.

“Oh, I got it! I got it!”

“Wow! Sir! That was amazing! Taishan is truly impressed!”

“*Ahem.* Did you see that? When I put my mind to it, something like this is easy.”

Curious, I looked over. The Great Sir was proudly holding a bird in his hands.

Its head was smashed to a pulp. It looked like it had died from being hit by a stone.

And Taishan was staring at the Great Sir—or, more precisely, at the bird—with drool in his mouth.

“Tasty—no, impressive! Taishan will start a fire, so let’s hurry and cook it!”

Starting a campfire in the middle of enemy territory was bullshit that set everyone’s blood boiling, mine included. But one lunatic didn’t seem to mind.

“Young friend, you do know how to show proper courtesy. As a reward for your hard work, I’ll let you have some of my meat. Which part do you prefer?”

“The legs! Definitely the legs!”

“You know your way around a chicken. Fine, I’ll give you one.”

“Both! All of them!”

“...Don’t push your luck.”

The Great Sir suddenly sobered up. Taishan drooped his head in disappointment, and that was when—

“You’re all acting like a bunch of damn fools. It reeks like something crawled out of who knows where, and you want to eat it? Like hell.”

At Namho’s words, delivered from his comfortable perch on Taishan’s shoulder, a thought suddenly struck me.

*Wait. Could it be?*

The suspicion became certainty the moment Jeong Hogun examined the bird.

“It’s rotting. The bone’s showing.”

“Which means…”

“Looks like the monsters aren’t only on the ground.”

It had been strange enough that any birds were still around after a group of strangers invaded their territory.

When the others finally realized what was happening and turned to look, the Great Sir blinked in confusion.

“Is something wrong? That fellow was staring right at me from a branch, so…”

“It was staring at you?”

The Great Sir nodded.

“Definitely. Its eyes were bloodred, too. It creeped me out, so I just went ahead and threw a stone at it.”

“...A Familiar?”

“Hm? What was that?”

“Nothing. Just talking to myself.”

I waved the Great Sir off and stared silently into the air.

The light of dawn was beginning to spread from the east. Between the lofty branches, I could make out shapes here and there.

Monsters that had hidden in the dark—and been brought back to life by its power.

*They’ve been watching us this whole time.*

I felt my mind turn cold as I slowly rose to my feet.

Then I spoke to the Great Sir, who still looked confused.

“If you see any more birds like that, kill every last one.”

“Every one?”

“Yes. Every one.”

“I don’t know about that. Even so, isn’t life precious?”

I thought about how to answer for a moment, then said,

“They’re dangerous birds.”

“Oh. Then I’ll kill them.”

“Please do.”

I patted the Great Sir’s shoulder and started to leave, but then remembered something and stopped.

Quietly murmuring, I reached out.

“Infinite Life Buddha.”

*Stab.*

The monster had stopped moving completely. I left it—and the Kunlun Sect Disciple—behind and walked away.

Every second counted now.

Eyes were already watching us, and pursuers would soon be on our heels.

[^1]: The Sanzu River is a Buddhist river associated with the boundary between life and death.
```
