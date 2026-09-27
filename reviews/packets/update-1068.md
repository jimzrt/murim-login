<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1068.txt",
      "sha256": "c94e6f3bcde7a3d77603edfb4ee1bb11a70220d2eddc0089fea13e3ba5873000",
      "bytes": 11746
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c50f02f7b841405361db351171bddffc7f92d83eb5e1d61f26baadcf11bb7653",
      "bytes": 870
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "cbb307690b7054d976b71961f971e1bf72a83aaa04305f25cd1904bd7c29daca",
      "bytes": 242179
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "5c732f37bc75ece5e7a58a6a108c45f8b1a15f692a21eee39aa5e14b845ec449",
      "bytes": 928
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c560fd9f284501e8419cbf8c88cf2bd49153d00cab02a25970e36c5af451d184",
      "bytes": 760
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "a266056329e7f1ee4a908a6ae266ccccee407433d9700bcabc5df4dc7a270218",
      "bytes": 839
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "f9ea9bce7b25d990f50b970490d6c766e5f083fd956fba18a6863b324360196f",
      "bytes": 651
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "dd75251df7d7afa82a1ea2c7711d05ed7a1c6ab9424ed396ad4c70c07c294c4f",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1c69580d231384cec1dd1a455f56c00672e8192c03241118ac98a5aa65720260",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "afab537a3195f0c91ea8a0e3c8832ddb358f3e19e5f07262a328cd02e5887d0d",
      "bytes": 623
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "4dea938f829d17713654e44d9b7d36ea864261b6e733a46fd31af2c9eb6b3a10",
      "bytes": 832
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "32a6ea9c8a5bdf72544d5acf1410fa3e3458ec08a51904f7611cd07167e856e5",
      "bytes": 284081
    }
  ],
  "estimated_tokens": 11619
}
-->

# Durable State Update — Chapter 1068

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
1 and safe_through 1068. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1068. Profile updates may replace only one
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
  "chapter": 1068,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1068,
    "continuity_sources": [1068],
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
    "Jin’s allied force won its first battle in Qinghai with about thirty wounded and no fatalities.",
    "A reanimated Kunlun Sect Disciple and rotting birds were found watching or confronting the allied force; Jin suspects Ma Sanbao may be with Dark Heaven.",
    "Jin senses the Lord of Heaven’s intended moment is approaching and is deeply connected to him."
  ],
  "continuity_sources": [
    1067
  ],
  "open_questions": [
    "Is Ma Sanbao with Dark Heaven, and has he spread the Corpse Art to others?",
    "Are Dark Heaven’s forces broadly composed of reanimated corpses?",
    "What is the Lord of Heaven seeking through Jin, and when will he appear?",
    "How many reanimated creatures are monitoring the allied force, and where are the pursuers?"
  ],
  "safe_through": 1067,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 살기     | **killing intent**                               |                                                       |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 체력               | **Stamina**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 귀가      | **your family**                                                 |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 대성 | **Great Completion** | Completion stage of a martial technique. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 창룡후 | **azure dragon's roar** | Battle cry released by Tang Jinhu. |
| 창룡 | **Azure Dragon** | Divine dragon form invoked in Hyeongong's blessing. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 성하 | **Seongha** | Hunter named during the cave battle. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 백환강시공 | **White Illusion Jiangshi Art** | Martial art named on the old bamboo slip. |
| 녕하성 | **Ningxia Province** | Region between Gansu and Shaanxi. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 녕하 | **Ningxia** | Place name; origin of the mounted bandits mentioned by Sima Gong. |
| 강시공 | **Corpse Art** | Wei Zhong’s technique for creating or controlling jiangshi. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |
| 진태경 | 황제 | guest of the Emperor’s younger brother addressing the Emperor | Your Majesty | formal and deferential in address, despite blunt challenges | Taekyung repeatedly addresses the Emperor as 폐하. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 황제 | 진태경 | Emperor addressing a subject and Prince Shangshan’s guest | Jin Taekyung | formal and authoritative | The Emperor addresses Taekyung by his family and personal name before asking what to do with the two officials. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 마삼보 | 동천마군 | disciple_to_master | Master | deferential | Ma Sanbao addresses the Eastern Heaven Demon Lord as 스승님 when rejoining him. |
| 황제 | 동천마군 | former ruler addressing a former subject, now an enemy | you | measured and formal | The Emperor asks why the Demon Lord betrayed his father, the late Emperor. |
| 동천마군 | 황제 | former subject addressing the Emperor, now an enemy | you; you bastards | hostile and contemptuous | He denies ever being loyal to the imperial family and accuses the rulers of betrayal. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 황제 | 신의 | Emperor addressing a physician | Divine Physician | direct and familiar | The Emperor asks whether the Divine Physician left something behind. |
| 신의 | 황제 | physician addressing his patient and sovereign | Your Majesty | formal and deferential | The Divine Physician addresses the Emperor as 폐하 while explaining the treatment. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 진태경 | 현천진인 | young martial artist addressing a senior Daoist Sect Leader | Perfected Being | polite | Jin responds respectfully to Hyeoncheon's assessment of the retreat. |
| 현천진인 | 진태경 | Kongtong Sect Leader addressing an allied martial artist | Daoist Friend Jin | respectful and measured | Refers to Jin as 진 도우 while discussing the Zhongnan Disciples’ future. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1066
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1067
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 1067
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1067
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1067
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1066
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1066
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 1067
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s former Brush-Holding Eunuch, a sorcerer and former Disciple of another Demon Lord who now serves the Blood Lord.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao was a longtime friend and former East Depot cohort of Hong Jin, served the Eastern Heaven Demon Lord, and led a restoration effort for Prince Shangshan; he now serves the Blood Lord.

## Korean source

```text
1068화




만약 누군가가 내게 적의 추격을 성공적으로 뿌리칠 방법을 묻는다면, 나는 한 치의 망설임 없이 답할 것이다.

오직 두 가지.

속도와 체력뿐이라고.

그러나 아는 것과 행하는 것은 다르다.

나를 포함한 아군 모두가 그 사실을 알고 있음에도, 눈앞을 가로막은 현실의 벽은 높고 단단했다.

제대로 된 휴식을 취하지도 못한 삼천여 명의 아군과는 달리, 시시각각 가까워지는 추격자들은 피로조차 느끼지 못하는 괴물들이었으니까.

“서북쪽! 이백여 장 밖!”

휴식할 새도 없이 산맥을 내려온 지 고작 한 시진이 되었을 때.

“놈들입니다! 놈들이 나타났습니다!”

저 멀리서 피어오르는 먼지구름을 발견한 이들은 비명처럼 외쳤고, 즉각 신형을 돌려세운 나는 그 희뿌연 황색 구름의 크기를 가늠했다.

‘적게는 삼백, 많으면 오백.’

좁고 어두컴컴한 형태로만 이루어진 하급 게이트를 전전하던 F급 헌터는 이제 없다.

아니, 그 시절의 모습은 아직 가슴 한구석에 남아 있을지라도 많은 부분에서 큰 변화를 겪었다.

다수의 적을 상대로 싸우는 법과 여러 상황에 대한 즉각적인 판단력 역시 그 변화 속에서 터득한 것들이었다.

“노야.”

이제는 눈빛만 보아도 서로의 뜻을 아는 사이.

내 짤막한 부름에 담긴 뜻을 읽어 낸 적천강은 즉각 공력을 실어 크게 외쳤다.

“이런 굼벵이 같은 놈들! 무엇 하느냐! 발등에 불똥 떨어진 것처럼 내달리지 않고!”

저건 단순히 성격 괴팍한 노인네의 질타가 아니다.

웅혼한 공력이 깃든 적천강의 창룡후(蒼龍吼)는 아군의 마음에 깃든 두려움을 깨트리고, 잠시나마 머뭇거리던 그들의 발걸음을 재촉했다.

그리고 숱한 전투를 치르며 궁성(弓星)이라 불리게 된 위대한 무인 역시, 자신의 역량과 역할을 정확히 알고 있었다.

“가거라. 때에 맞춰 보낼 테니.”

고개를 끄덕인 나는 땅을 박차고 먼지구름을 향해 쇄도했다.

화아악!

바람이 갈라진다.

나아가는 발끝을 따라 지면을 뒤덮고 있던 것들이 뭉게뭉게 일어나고, 그렇게 또 다른 먼지구름을 만들어 낸다.

수백여 명의 적들을 휘감은 것보다도 크고, 짙은 먼지구름을.

‘보인다.’

휘몰아치는 모래와 먼지 너머, 죽지도 살지도 않은 괴물들의 모습이 망막을 선명하게 물들인다.

굳게 말아쥔 창대를 비스듬히 올려세운 순간, 그보다 한 걸음 먼저 적들에게 도달한 눈부신 빛줄기처럼.

콰아아앙!

강기(罡氣)의 화살이 폭발했다.

궁성의 손끝을 따라 쏘아진 그것은 선두에서 달려오던 수십의 괴물들이 단숨에 집어삼키고, 증발시켰다.

그리고 그 공백의 틈새를 파고든 나는, 이 완벽한 찰나의 기회를 놓치지 않았다.

쉬잉!

소름 끼치도록 희미한 파공성에 솜털이 곤두선다.

호흡, 속도, 힘.

날이 갈수록 진일보한 무위를 증명하듯, 모든 것이 한 치의 오차 없이 맞물린 일격은 적들을 스쳤고 그것으로 충분했다.

서걱! 푸화아악!

절삭음은 하나지만, 그 안에 담긴 죽음은 수십이라.

비스듬히 내리그은 한 번의 횡격(橫擊)을 따라 썩은 육신과 핏물이 갈라지고 터져 나온다.

그 끔찍한 광경과는 어울리지 않는, 맑은 종소리도 함께.

띠링. 띠링. 띠리리링!



- [Lv.56 타락한 하급 광신도]를 처치하셨습니다!

- [Lv.75 타락한 중급 광신도]를 처치하셨습니다!

- [Lv.52 타락한 무림인]을 처치하셨습니다!

.

.

.

- 상대와의 레벨 격차를 감안한 경험치와 명성이 정산됩니다!

- 미약한 양의 경험치를 획득했습니다!

- 미약한 양의 명성을 획득했습니다!



나는 겹겹이 울려 퍼지는 시스템 알림을 들으며 홀린 듯이 창날을 휘둘렀다.

사방이 온통 괴물이고, 적이었다.

창날이 한 번의 궤적을 그릴 때마다 십수 명이, 혹은 수십 명이 썩은 통나무처럼 허물어지고 두 번 다시 움직이지 못했다.

그들을 이승에 묶어 두었던 사슬에서 해방되어, 본래의 정해진 이치대로.

띠링.

어느 순간 들려온 마지막 종소리를 끝으로, 더는 무엇 하나 움직이는 것이 없음을 확인한 나는 문득 고개를 들었다.

태양을 반쯤 가린 구름 아래, 검은색 날개를 지닌 까마귀가 허공을 유영하고 있었다.

핏물처럼 붉은 눈동자를 빛내며.

“내려와. 얘기나 좀 하자.”

당연하게도 돌아오는 대답은 없었고, 나는 썩은 냄새를 풍기는 피 웅덩이 속에 잠겨 있던 누군가의 검을 집어 들며 덧붙였다.

“그게 싫으면, 직접 오든가.”

슈확!

일순간 바람을 찢으며 솟구친 검신이, 까마귀의 붉은 눈동자를 가렸다.

푹!



* * *



“음.”

불현듯, 낮은 침음성과 함께 눈을 뜬 사내는 미간을 문질렀다.

마지막 순간 시야를 가린 섬광과 함께 전해진 통증이, 아직도 그의 뇌리에 남아 송곳처럼 머릿속을 들쑤시는 듯했다.

‘괴물 같은 놈. 그새 더 강해졌군.’

사내, 마삼보는 새삼 놀라지 않을 수 없었다.

다른 존재의 감각을 빌려 지켜본 진태경의 무위는, 그가 황궁에서 보고 겪은 것보다도 한층 진일보한 상태였으니까.

‘그것이 가능한가? 고작 석 달도 되지 않는 짧은 시간 만에?’

스스로에게 되물은 마삼보는 이내 고개를 저었다.

멍청한 질문이었다.

가능한가, 불가능한가를 따질 단계는 이미 한참 전에 지났다.

중요한 것은 진태경이 이 모든 것을 현실로 만들었으며, 바로 이러한 점이야말로 고작 이립도 되지 않은 저 젊은 청년을 누구보다 특별한 존재로 여겨지게 한다는 사실이었다.

또한 마삼보는 이미 알고 있었다.

진태경과 달리 자신의 역할은 정해져 있고, 결코 이 무대의 주연이 될 수 없다는 사실을.

그리고 그런 마삼보에게 지금 당장 주어진 가장 중요한 임무는, 철저한 감시와 보고뿐이었다.

“혈주(血主)시여.”

불과 얼마 전부터 새롭게 모시게 된 상관을 찾아간 마삼보는 모든 것을 소상하게 고했고, 그의 보고를 듣고 있던 혈주는 미간을 찌푸렸다.

“잠깐. 감시하는 것까지 들켰다고?”

“예. 송구하오나 그리 되었…….”

퍼엉!

말이 끝맺어지기도 전에 날아온 장력(掌力).

어지간한 절정 고수조차 직격당한 순간 절명했을 일격이었지만, 장력에 휩쓸려 튕겨 나간 마삼보는 그 엄청난 충격과는 달리 곧장 엎드려 부복했다.

“허, 이놈 몸뚱어리 튼튼한 거 보게.”

“부디 죽여 주십시오.”

“보채지 말거라. 안 그래도 내 이 자리에서 당장 네놈을 쳐 죽여 버릴까 고민이 되려던 참이니까.”

“……혈주시여.”

“왜, 이제야 좀 두려움이 느껴지느냐? 하기사 네 스승도 결국 그리 뒈졌으니 그럴 만도 하겠군.”

마삼보는 더욱 깊게 몸을 수그렸다.

스승이었던 동천마군과 달리, 백환강시공(魄環僵尸功)을 대성하지 못한 그였기에 죽음에 대한 두려움은 더욱 클 수밖에 없었다.

“부디 자비를…….”

“주둥이 닥쳐라. 일각이라도 더 살고 싶다면.”

혈주는 짜증이 담긴 눈빛으로 마삼보를 내려다보았지만, 그가 내릴 수 있는 벌은 딱 거기까지였다.

마삼보는 여러모로 활용할 구석이 많은 소모품이었고, 몇 없는 쓸 만한 수하를 죽일 생각 따위는 처음부터 없었으니까.

애당초 혈주가 마삼보에게 이토록 위협을 가한 이유도, 마음에 들지 않는 누군가가 보는 앞에서 자신의 위엄과 지배력을 과시하고 싶었기 때문이었다.

물론, 그 누군가는 그런 혈주의 모습 따위는 아랑곳하지 않은 채 다른 문제에 집중하고 있었지만.

“발각됐다고? 이렇게 빨리?”

혼잣말 같은 대술사의 물음에 혈주가 대답했다.

“호들갑 떨 필요 없어. 예상보다는 빠르지만 그리 놀라운 일은 아니니까.”

“결과만 보면 그렇겠지. 딱 그 정도가 당신의 한계고.”

“뭐?”

“궁성, 화왕, 진태경. 그리고 그보다 떨어지긴 하지만 공동파의 늙은 도사까지 있으니 발각당할 수는 있었겠지. 하지만 내가 알고 싶은 건 그런 게 아니야.”

조소 어린 눈빛으로 혈주를 응시한 대술사가 마삼보를 향해 고개를 돌렸다.

“자, 여기 있는 네 멍청한 상관은 신경 쓰지 말고 솔직하게 말해 보렴. 네 은밀한 감시를 가장 먼저 알아차린 자가 누구인지.”

“그것은.”

“한 번 뱉은 말은 주워 담을 수 없지. 동천마군이 이 상황에서 거짓을 고할 만큼 어리석은 자를 제자로 들였다고는 생각하기 어려운걸.”

마삼보는 잠시 머뭇거렸지만, 심유하게 가라앉은 대술사의 눈빛을 마주친 순간 깨달았다. 

그녀가 이미 모든 것을 꿰뚫어 보고 있다는 것을.

난폭한 상관에게 더욱 큰 질책을 당할까 두려워 차마 말하지 못했던, 감춰진 사정을 짐작하고 있다는 것을.

“십여 년 전에 아주 어렴풋이, 짧은 소문과 정보로만 접했던 자였습니다.”

그제야 조심스럽게 입을 연 마삼보의 모습에 혈주는 살기를 흘렸고, 대술사는 그럴 줄 알았다는 듯이 희미한 미소를 머금었다.

“그랬겠지. 괜히 동창(東廠)이 아닐 테니.”

천하는 대국이라는 울타리에 속해 있고, 대국 황실은 울타리 내부와 밖을 관조하기 위해 감시탑을 세웠다.

바로 동창이라는 감시탑을.

그리고 천하를 굽어보는 그 천혜의 감시탑은, 동천마군이라는 매개체를 통하여 암천과 시야를 공유하고 있었다.

“비록 작금의 황제와 대립하며 영향력이 줄어들긴 했으나, 그럼에도 천하 곳곳에 심어둔 눈과 귀를 통해 온갖 정보가 흘러들어 왔지요.”

“그중에 오늘 감시를 알아차린 그놈이 있었고?”

“예, 녕하성에서는 대인(大人)이라 불리는 자입니다.”

“대인이라. 무림인의 별호치고는 희한하군.”

“그마저도 그리 잘 알려진 별호는 아닙니다. 워낙 광인(狂人)인 데다 과거의 행적 또한 묘연했던지라.”

“동창에서도 파악할 수 없을 정도로 말이더냐?”

“그것은 속하로서도 장담드릴 수 없으나, 당시에는 금의위를 앞세운 황제의 견제로 인해 한계가 명백했던 것이 사실입니다.”

공교롭게 맞물린 시대의 흐름 속에서 대인의 존재는 그렇게 조금씩 잊혀졌다. 

바로 오늘, 마삼보가 케케묵은 기억을 헤집기 전까지는.

그리고 이 정체불명의 인물에 대한 이야기를 듣고 있던 대술사는, 불현듯 잊고 있던 의문에 대한 답을 떠올릴 수 있었다.

‘공동파. 돈황에서 살아남은 현천진인과 공동파의 제자들이 도중에 어디로 사라졌나 했더니…….’

확신에 가까운 짐작. 동시에 또 다른 의문이 떠올라 그녀의 눈빛을 깊게 가라앉혔다.

‘도대체 누구지?’
```

## Final English reading copy

```markdown
# Chapter 1068

If anyone asked me how to shake off enemy pursuers, I’d answer without a moment’s hesitation.

There were only two things that mattered:

Speed and stamina.

But knowing what to do and doing it were two different things.

Even though every one of us knew that—including me—the wall of reality standing in our way was high and solid.

Unlike our three thousand allies, who hadn’t had a proper rest, the pursuers closing in by the moment were monsters who didn’t even feel fatigue.

“Northwest! About two thousand feet out!”

We’d been coming down the mountain without a break for barely two hours when—

“There! The bastards are here!”

The people who spotted the distant cloud of dust cried out. I immediately turned and sized up the hazy yellow cloud.

*Three hundred at least. Maybe five hundred.*

The F-rank Hunter who used to scrape by in narrow, pitch-dark Gates was gone.

No—even if some part of that old me still remained, I’d changed in many ways.

I’d learned how to fight multiple enemies and how to make snap decisions in all kinds of situations.

“Old Master.”

We’d reached the point where we understood each other from a glance.

Jeok Cheongang read the meaning in my brief call and immediately poured internal energy into his voice.

“You slowpokes! What are you waiting for? Run like your feet are on fire!”

That wasn’t just a scolding from a cranky old man.

Jeok Cheongang’s mighty Azure Dragon’s Roar shattered the fear lodged in our allies’ hearts and drove their hesitant feet forward, if only for a moment.

And the great martial artist who’d come to be known as the Bow Saint after countless battles knew her abilities and her role precisely.

“Go. I’ll send it at the right time.”

I nodded, kicked off the ground, and charged toward the dust cloud.

*Whoosh!*

The wind split.

The ground-covering dust billowed up behind my advancing feet, forming another cloud—one larger and denser than the cloud surrounding the several hundred enemies.

*I see them.*

Beyond the swirling sand and dust, the monsters who were neither dead nor alive came into sharp focus.

I tilted up the spear clenched in my hands just as a dazzling streak of light reached the enemy a step ahead of me.

*Boom!*

An arrow of Force exploded.

Shot from the Bow Saint’s fingertips, it swallowed up dozens of monsters charging at the front and vaporized them in an instant.

I plunged into the gap it left behind, not about to waste that perfect opening.

*Whoosh!*

The hair on my arms stood on end at the faint, spine-chilling whistle.

Breath, speed, strength.

As if to prove my skill advanced with every passing day, everything aligned in an attack without a hair’s breadth of error. It only grazed the enemies—but that was enough.

*Slice! Splatter!*

One cutting sound, but dozens of deaths within it.

A single diagonal sweep split and burst their rotting bodies, spilling blood.

Along with a clear chime, wholly at odds with the horrific sight.

*Ding. Ding. Ding-ding-ding!*



> **System**
>
> You have slain a Lv. 56 Corrupted Lower-Rank Fanatic!
>
> You have slain a Lv. 75 Corrupted Mid-Rank Fanatic!
>
> You have slain a Lv. 52 Corrupted Martial Artist!
>
> …
>
> …
>
> …
>
> EXP and Fame are calculated based on the level difference between you and your opponents!
>
> You have gained a small amount of EXP!
>
> You have gained a small amount of Fame!



I swung my spear as if entranced, listening to the System notifications ringing one over another.

Monsters and enemies surrounded me on all sides.

Each time my spear traced an arc, a dozen or even dozens of them crumpled like rotten logs, never to move again.

Freed from the chains that had bound them to this world, they returned to the order of things as it was meant to be.

*Ding.*

At the last chime, I confirmed that nothing else was moving and lifted my head.

Beneath a cloud that half-obscured the sun, a black-winged crow drifted through the air.

Its eyes glowed bloodred.

“Come down. Let’s talk.”

Naturally, I got no answer. I picked up a sword from the one submerged in a pool of foul-smelling blood and added,

“If you don’t like that, come yourself.”

*Whoosh!*

The sword shot upward, tearing through the air. In an instant, its blade covered the crow’s red eyes.

*Thrust!*



* * *



“Hmm.”

The man opened his eyes with a low groan and rubbed the space between them.

The pain that had come with the flash of light at the last moment still lingered in his mind, as if an awl were burrowing into his head.

*What a monster. He’s gotten even stronger.*

Ma Sanbao couldn’t help but be surprised.

Jin Taekyung’s martial skill, which he’d watched through another being’s senses, had advanced even further than when Ma had seen him at the imperial palace.

*Was that even possible? In less than three months?*

Ma Sanbao asked himself the question, then shook his head.

It was a stupid question.

The time to wonder whether it was possible had passed long ago.

What mattered was that Jin Taekyung had made it real—and that was precisely what made that young man, not even thirty yet, so exceptional.

Ma Sanbao already knew something else, too.

Unlike Jin Taekyung, his own role was already set. He would never be the star of this stage.

And the most important task currently before him was nothing more than keeping a thorough watch and reporting back.

“My Lord.”

Ma Sanbao went to find the superior he’d only recently begun serving and reported everything in detail. The Blood Lord listened, then furrowed his brow.

“Wait. They even found out you were watching them?”

“Yes. I’m ashamed to say that’s what happened—”

*Boom!*

A palm strike flew at him before he could finish.

Even an ordinary Peak master would have died on the spot if struck by that blow. Ma Sanbao was swept away by the force, yet despite the tremendous impact, he immediately prostrated himself.

“Huh. Look at how sturdy this body of yours is.”

“Please kill me.”

“Don’t rush me. I was just considering whether to beat you to death right here.”

“...My Lord.”

“What, are you finally scared? I suppose you have reason to be. Your Master died the same way, after all.”

Ma Sanbao lowered himself even further.

Unlike his Master, the Eastern Heaven Demon Lord, Ma hadn’t achieved Great Completion in the White Illusion Jiangshi Art. So his fear of death could only be greater.

“Please show mercy…”

“Shut your mouth. If you want to live even fifteen minutes longer.”

The Blood Lord glared down at Ma Sanbao with irritation, but that was the extent of the punishment he could give.

Ma Sanbao was a useful expendable in many ways, and the Blood Lord had never intended to kill one of the few subordinates worth keeping.

Besides, the reason the Blood Lord had threatened Ma so harshly was that he wanted to show off his authority and control in front of someone he disliked.

Of course, that someone paid no attention to the Blood Lord’s display and remained focused on another matter.

“They found out? This soon?”

The Blood Lord answered the Grand Mage’s question, which sounded almost like she’d asked herself.

“No need to make a fuss. It’s sooner than expected, but not all that surprising.”

“Looking at the result, sure. That’s about as far as your thinking goes.”

“What?”

“The Bow Saint, the Fire King, Jin Taekyung. And while he’s not on their level, even that old Daoist from the Kongtong Sect. They could’ve noticed. But that’s not what I want to know.”

The Grand Mage fixed the Blood Lord with a mocking look, then turned to Ma Sanbao.

“Come now. Don’t worry about your foolish superior. Tell me honestly: who was the first to notice your covert surveillance?”

“That was…”

“Once you’ve said something, you can’t take it back. I find it hard to believe the Eastern Heaven Demon Lord would take in a Disciple foolish enough to lie under these circumstances.”

Ma Sanbao hesitated for a moment. But when he met the Grand Mage’s deeply penetrating gaze, he realized—

She already saw through everything.

She had guessed what he’d been too afraid to say, worried that his violent superior would scold him even more.

“It was someone I’d encountered only vaguely, through brief rumors and bits of information, more than a decade ago.”

At last Ma Sanbao answered cautiously. The Blood Lord let killing intent seep from him, while the Grand Mage wore a faint smile, as if she’d expected as much.

“I thought so. The East Depot wouldn’t be what it is otherwise.”

The world belonged within the bounds of the Great Nation, and the Great Nation’s imperial family had built a watchtower to observe what lay inside and beyond those bounds.

The East Depot—the imperial watchtower.

And that peerless watchtower, overlooking the world, shared its sights with Dark Heaven through the Eastern Heaven Demon Lord.

“Though his influence has waned in his conflict with the current Emperor, information still flowed in from all across the realm through the eyes and ears he’d planted everywhere.”

“And among them was the man who noticed the surveillance today?”

“Yes. In Ningxia Province, he is called Great Sir.”

“Great Sir. An odd nickname for a martial artist.”

“It isn’t a particularly well-known name, either. He’s a madman, and his past is shrouded in mystery.”

“Even the East Depot couldn’t find out who he was?”

“I can’t say for certain, but at the time, the Emperor was using the Embroidered Uniform Guard to keep the East Depot in check. That clearly limited what we could find out.”

Caught up in the coinciding currents of the times, Great Sir’s existence had gradually been forgotten.

Until today, when Ma Sanbao dug through his old memories.

Listening to the story of this mysterious man, the Grand Mage suddenly found an answer to a question she’d forgotten.

*The Kongtong Sect. I wondered where Perfected Being Hyeoncheon and the Kongtong Disciples who survived Dunhuang had disappeared to along the way…*

A suspicion close to certainty. At the same time, another question surfaced, and her gaze grew distant.

*Who in the world is he?*
```
