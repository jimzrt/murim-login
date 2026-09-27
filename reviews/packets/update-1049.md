<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1049.txt",
      "sha256": "028fb3a3207b47ddd3272e4ea032ae81af93b323f22606da1b82be86b6a60a4f",
      "bytes": 13309
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c1b22ffbb91a08dbd15f45c0164341d4eeead57ffacf9894d7ccbff8efc7a179",
      "bytes": 1705
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "91edff1ea0e7f2d1bdf20f77998a86f250b89f1bc3f043cd106289bea1e118b4",
      "bytes": 240895
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "297e6325d7bd41070acdb0caedd4c292e76e517f399034020ea8da27b8fcccd0",
      "bytes": 928
    },
    {
      "path": "characters/Blood-Sword Demon Lord.md",
      "sha256": "388f88bfb584bb5231252aae52b2823c10259b63a3913c61238db111d6b652c2",
      "bytes": 914
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "f50b44132abd660ffaeb8438de2da16b38f45bca1b9dbe3b019eadd0f7688bbe",
      "bytes": 760
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "96c4170969044a212d366cba41effad8f2bed0dafbeb76ac9ebaa2e98e7596bd",
      "bytes": 839
    },
    {
      "path": "characters/Grand Mage.md",
      "sha256": "3e994a10c514b7d3f897ca6df7c519331a8394936841306db55db0d4d69e15d6",
      "bytes": 569
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "0bd064565121b4f3a72b4eee192f7d53031cae1ffdae2ebad172c54136912153",
      "bytes": 1502
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "f79d153b7155d5e1e3a61e41ac361fbf23c37ce4df0b9ffe0df16dd4f5ee9382",
      "bytes": 1823
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e79abee0bb927cd9cfff5874867a8f868751aab4c38ce68411ff41de3fa4e3f5",
      "bytes": 623
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "93b46a660114d23394330a02e740b624cd9492ad8f4d2749541950d547ed610d",
      "bytes": 716
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "175bdcb038129daa2e36a56e8510b35a2f97cc7b85716701205548dd5c21b6b1",
      "bytes": 889
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e476e49cdcddf6de4980fb9437ae78bed54ffc02a595fe7c61e28608999f8e34",
      "bytes": 281989
    }
  ],
  "estimated_tokens": 13139
}
-->

# Durable State Update — Chapter 1049

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
1 and safe_through 1049. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1049. Profile updates may replace only one
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
  "chapter": 1049,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1049,
    "continuity_sources": [1049],
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
    "The Blood-Sword Demon Lord serves the Lord of Heaven and commands the invading army.",
    "The Blood-Sword Demon Lord is gravely injured after Jeok Cheongang and the Bow Saint attack him; Sima Gong stabs his ankle, and he reaches the Grand Mage, who heals Jin Taekyung instead.",
    "Jin Taekyung collapses after the Grand Mage’s barrier deflects his spear attack; her healing light stabilizes his breathing.",
    "The battle at the Great Snow Mountain continues; Jeok Cheongang and the Bow Saint are closing in on the Blood-Sword Demon Lord.",
    "The Grand Mage has not reappeared since the enormous fireball attack until this battle.",
    "Sima Gong broke his bargain with Dark Heaven, aided Jeok Cheongang, and is gravely wounded and missing an arm; his fate remains unresolved.",
    "Sima Gong hopes the Black Dragon Demon Gate will survive and grow stronger under his absent heir."
  ],
  "continuity_sources": [
    1047,
    1048
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven?",
    "Did Dark Heaven cause the Great Faction War?",
    "Who are the white-robed mages, and what is their purpose?",
    "How were the former Demonic Cult fiends made into Black Ghosts?",
    "Why did the Grand Mage’s healing light stabilize Jin Taekyung rather than heal the Blood-Sword Demon Lord?"
  ],
  "safe_through": 1048,
  "temporary_decisions": [
    "Render 대마도사 as Grand Mage.",
    "Use Fire Ball, Stone Wall, and Magic Arrow for the named spells.",
    "Render 헬 파이어 as Hell Fire; use hellfire for descriptive 겁화.",
    "Render 쇄월검진 as Moon-Shattering Sword Formation."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 지능               | **Intelligence**               |
| 감숙     | **Gansu**              |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 혈검마군 | **Blood-Sword Demon Lord** | Antagonist commanding the army advancing on the Great Snow Mountain. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 대마도사 | **Grand Mage** | Title used for Magic Johnson. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 검마 | **Sword Demon** | A Demonic Cult swordsman whose final technique is compared with One Annihilation. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 북천마군 | **North Heaven Demon Lord** | Title of Murong Baek. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 서천마군 | 적천강 | hostile_invader_to_unconscious_patient | you | calm and predatory | Says someone wants to see Jeok Cheongang and attempts to move him with Seizing an Object Through Empty Space. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 서천마군 | hostile_opponents | you bastard | blunt and threatening | Jeok addresses the Western Heaven Demon Lord with 네놈 while defending Taekyung and ordering him not to touch his Disciple. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 진태경 | 북천마군 | hostile opponents | you | casual, taunting, and profane | Taekyung teases and insults him during their standoff. |
| 적천강 | 북천마군 | former battlefield adversaries | you; you pup | blunt, familiar, and taunting | Jeok addresses him informally while challenging his alliance with Dark Heaven. |
| 북천마군 | 궁성 | hostile martial opponents | Bow Saint | calm and formally familiar | Addresses her directly while acknowledging her effort. |
| 북천마군 | 적천강 | former battlefield adversaries | Fire King | calm and familiar | Addresses Jeok Cheongang as 화왕 while asking him not to rush. |
| 혈검마군 | 적천강 | former opposing martial masters | Senior Jeok | respectful and familiar | Addresses Jeok as 선배 while teasing him. |
| 적천강 | 혈검마군 | former opposing martial masters | you; you bastard | blunt and hostile | Uses 너 and 네놈 while confronting him. |
| 혈검마군 | 진태경 | enemy addressing a younger martial artist | you | familiar and measured | Uses 자네 while praising and assessing Taekyung. |
| 진태경 | 혈검마군 | young martial artist confronting an enemy | you | casual and challenging | Questions when the Blood-Sword Demon Lord and the Lord of Heaven appeared. |
| 혈검마군 | 천주 | servant_to_master | Lord of Heaven | deferential | In his inner monologue, he addresses his absent master as 당신 and refers to himself as 속하. |
| 대마도사 | 진태경 | adversary_to_adversary | you | polite, teasing | She uses polite phrasing while taunting him and warning him not to overexert himself. |
| 진태경 | 대마도사 | adversary_to_adversary | you bitch | insulting-casual | He curses at her while refusing to give up. |
| 대마도사 | 궁성 | Adversaries | Bow Saint | Not established | She identifies him by title when recognizing the archer who struck the Hell Fire sphere. |
| 대술사 | 혈검마군 | subordinate_to_commander | Demon Lord | respectful and formal | Addresses him as 마군 while acknowledging his injuries. |
| 혈검마군 | 대술사 | commander_to_subordinate | Grand Mage | blunt and commanding | Orders her to heal him immediately. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1034
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; readily kills subordinates who disappoint him, but restrains his violence when preserving valuable sorcerers serves Dark Heaven’s goals.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and seeks to advance the Lord’s great cause; he regards the deceased Western Heaven Demon Lord and Southern Heaven Demon Empress as powerful allies whose deaths cost Dark Heaven, and considers Jin Taekyung and Cheongpung formidable adversaries.

### Blood-Sword Demon Lord.md

# Blood-Sword Demon Lord (혈검마군)

- **Safe through:** Chapter 1048
- **Aliases:** None
- **Role:** The Blood-Sword Demon Lord is a formidable martial master who commands the force advancing on the Great Snow Mountain and now serves the Lord of Heaven.
- **Personality:** Devoted to his master and proud of his abilities, he is deeply wounded by perceived distrust and resolves to prove his worth.
- **Voice:** Casually familiar and self-amused, addressing Jeok Cheongang respectfully as Senior while trading blunt insults; his easy laughter can turn to a low, cold intensity.
- **Relationships:** He serves the Lord of Heaven with deep devotion but believes his master does not fully trust him; he has been ordered not to kill Jin Taekyung, admires Jeok Cheongang, and once shared the Demonic Cult with the fiends who became Black Ghosts.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1048
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 1034
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Grand Mage.md

# Grand Mage (대마도사)

- **Safe through:** Chapter 1045
- **Aliases:** None
- **Role:** The Grand Mage leads the white-robed mages and is a formidable mage who has reached the edge of truth.
- **Personality:** She remains composed and curious even as her own forces die, showing little concern for their suffering.
- **Voice:** Calm and politely phrased, with teasing remarks and a hint of excitement.
- **Relationships:** She commands the white-robed mages and is an adversary of Jin Taekyung.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1048
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1048
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him and feels no fear when Taekyung is with him; Taekyung trusts Sama Pyo and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1048
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 1039
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 1034
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃1049화



그 순간, 새하얗게 물든 혈검마군의 뇌리에 떠오른 생각은 하나뿐이었다.

‘지금 내가, 꿈을 꾸고 있는 건가?’

그것은 지극히 자연스러운 의문이었다.

왜 아니겠나.

눈앞의 여인, 대술사(大術士)와 그는 아군이었다.

같은 주인을 모시며 같은 목표를 지닌.

그랬기에 혈검마군은 자신의 눈 앞에 펼쳐진 이 믿을 수 없는 광경을 좀처럼 현실로 받아들일 수 없었다.

바로 다음 순간, 말없이 그를 내려다보던 대술사가 굳게 닫혀 있던 입술을 열기 전까지는.

“아직도 꿈을 꾸고 있나요?”

“……뭐?”

“이건 꿈이 아닙니다, 마군(魔君). 엄연한 현실이에요.”

혈검마군은 멍하니 대술사를 바라보며 생각했다.

조금 전 자신의 귓가를 파고든 목소리에 담긴 의미를.

이런 상황이 벌어진 이유를.

그리고 이 모든 것이 현실이라는 대술사의 말을 뒷받침하듯, 전신 구석구석에서 전해져 오는 격통을 느끼며 간신히 목소리를 쥐어 짜냈다.

“장난이…… 과하군.”

“장난이라니, 그것이 대관절 무슨 말씀이신지.”

천연덕스럽게 고개를 갸웃거리는 여인의 모습에 혈검마군은 이를 악물었다.

가슴 깊숙한 곳에서 솟구친 울화가 핏물이 되어 울컥 터져 나오고 있었다.

“어서, 쿨럭. 어서 나를 치유해라.”

“그 문제라면 더는 걱정하지 않으셔도 됩니다.”

면사 아래로 부드럽게 호선을 그리는 붉은 입술.

가쁘게 숨을 헐떡이고 있는 혈검마군을 향해 빙긋 웃어 보인 대술사가 고개를 돌리며 덧붙였다.

“이미 치유는 끝났으니까요.”

그녀의 말은 사실이었다.

그것은 말 그대로의 치유(治癒)였다.

완전하지 못한, 그러나 조금씩 어둠으로 물들어 가던 누군가의 의식을 부여잡기에는 충분한 수준의 치유.

후우우.

힘겹게 쌕쌕거리며 내뱉던 숨결이 안정되고, 새하얗게 질려있던 낯빛과 입술은 어느덧 본래의 혈색을 되찾는다.

청년을 휘감은 따스한 광휘가 완전히 사그라졌을 때, 대술사의 가느다란 손가락이 부드럽게 허공을 휘저었다.

쩌적, 촤르륵!

봉인되어 있던 상자가 열리듯 갈라지는 땅거죽.

동시에 땅속 깊숙이 숨어 있던 초목의 줄기가 솟구쳐 청년을, 진태경을 휘감아 들어 올렸다.

바로 그 순간에도 언덕을 향해 빠른 속도로 짓쳐 들던 훼방꾼들에게 보여 주려는 듯이.

그리고 저 멀리 인질처럼 포박당한 진태경의 모습에, 정확히 어떤 일이 벌어졌는지 모르는 적천강과 궁성은 발걸음을 멈춰 설 수밖에 없었다.

“진심이 통하지 않는 건 조금 슬프지만, 어쩌겠어요. 이렇게라도 하는 수밖에.”

작게 혀를 차는 대술사를 멍하니 바라보던 혈검마군은 그제야 비로소 완전히 깨달았다.

이것은 한낱 꿈도, 짓궂은 장난도 아니라는 것을.

“어째서?”

수많은 의미가 담긴 물음.

그러나 뒤이어 돌아온 대답은 짧으면서도 명료했다.

“그분께서 원하시니까.”

은백색의 면사가 흔들린다.

그 너머로 어렴풋이 보이는 대술사의 무감정한 눈빛은 이미 상관을 대하는 그것과는 거리가 멀었다.

석상처럼 굳어 버린 혈검마군을 향해 이어지는 담담한 목소리 역시도.

“일평생을 실컷 날뛰었으니, 이제는 쉴 때도 됐잖아. 안 그래?”

지금 이 순간에도 조금씩 무뎌지는 감각 때문일까.

아니면 생각지도 못한 충격 때문일까.

메아리처럼 귓가에 울려 퍼지는 그녀의 목소리를 멍하니 듣고만 있던 혈검마군은, 불쑥 한마디를 내뱉었다.

“개소리.”

숨길 수 없는 피로가 묻어나오는 음성이었으나, 그 안에는 흔들림 없는 확신이 깃들어 있었다.

자신이 이렇게 버림받을 리 없다는 확신.

설령 자신의 주인이 그를 단순한 사냥개로 여겨 왔다고 해도, 이토록 허무하게 가마솥에 집어넣을 수는 없었다.

토사구팽(兎死狗烹)?

그것도 결국 모든 사냥이 끝났을 때의 이야기다.

하지만 현재 천주가, 암천이 처한 상황은 어떠한가.

서천마군이, 남천마후가, 뒤이어 동천마군과 북천마군도 쓰러졌다.

가장 신뢰하던 네 마리의 맹수는 이제 없다.

무림맹의 깃발 아래 결집한 중원 무림은 한낱 토끼로 치부할만한 전력이 아니었고, 혈주와 함께 살아남은 혈검마군 자신은 사냥개 이상의 존재였다.

수만 명의 대군을 휘하에 거느리고 이곳까지 올 수 있었던 것이 바로 그 증거였다.

그뿐만이 아니다.

조금만, 아주 조금만 더 손을 뻗어도 달콤한 승리를 얻을 수 있었다.

이 빌어먹을 몸뚱어리만 회복할 수 있다면.

진태경을 인질로 삼는다면 화왕과 궁성이라 한들 감당할 수 있었다.

감숙의 패권이 천하로 향하는 승리의 교두보가 눈앞에 있었다.

‘그런데, 그런 나를 그분께서 버리신다고?’

혈검마군은 헛웃음을 흘렸다.

그리고 말도 안 되는 이야기로 주인과의 이간질을 시도하는 건방진 계집을 향해 검붉은 안광을 번뜩였다.

“헛소리 집어치워라, 계집. 네년의 배반을 그분께서 모르시리라 생각하느냐?”

틀림없었다.

대술사. 저 더러운 배반자가 모든 것을 망쳤다.

자신이 지금 같은 상황에 처한 이유는, 단지 내부의 종양 덩어리를 알아보지 못했기 때문이었다.

“그래, 저 간사한 놈들에게 무엇을 약속받았느냐? 거대한 장원? 산더미처럼 쌓인 금은보화? 아니면 네년의 그 더러운 욕망을 채워 줄 절세의 미남?”

혈검마군은 들끓어 오르는 목소리로 내뱉었다.

지금 이 순간, 그는 어느 때보다 분노하고 있었다.

이제 와 돌이켜 생각해 보면 처음부터 이상한 점투성이였다.

전투가 막 시작되었을 때 망설임 없이 나서려던 혈검마군을 대술사가 막아 세웠던 것도, 그로 인해 핵심 전력이었던 흑귀(黑鬼)들이 전멸한 것도.

심지어 혈검마군 자신조차 알지 못했던, 강력한 술법들을 사용할 수 있었음에도 끝끝내 돕지 않았던 것도.

속았다.

철저히 농락당했다.

그리고 그 견딜 수 없는 사실이 혈검마군으로 하여금 몸부림치게 만들었다.

“감히. 감히 네년 따위가 나를 죽일 수 있을 것 같으냐? 고작 이 정도로 그분의 대계(大計)를 망칠 수 있을 거라 생각하느냔 말이다!”

투둑, 툭.

혈검마군은 앞서 충돌의 여파로 생겨난 구덩이 속에서 온 힘을 다해 몸뚱어리를 일으켜 세웠다.

한쪽 팔을 잃고, 다리의 힘줄이 잘려 나가고, 뼈마디가 으스러졌음에도 그에게는 범인(凡人)이라면 상상조차 할 수 없는 인내심과 생명력이 남아 있었다.

하지만 극렬한 분노에 사로잡힌 혈검마군은 가장 중요한 사실을 잊고 있었다.

그가 몇 번이나 즉사하고도 남을 부상을 당한 상황에서도 살아남을 수 있었던 이유는, 대술사의 마법이 육신에 깃들어 있었기 때문이라는 것을.

“당신을 죽일 수 있겠느냐고? 그야 물론이지.”

대술사는 구덩이를 빠져나와 자신을 향해 기어 오는 혈검마군을 담담하게 응시하며 덧붙였다.

“심지어 그건 아주 간단할 테고.”

그녀의 말은 사실이었다.

현재의 혈검마군을 상대로는 마법을 쓸 필요도 없었다.

그저 그에게 부여한 신체 강화 마법을 해제하는 것만으로도 충분할 것이다.

지금 당장 대술사가 죽이고자 하는 의지만 품는다면, 일세를 풍미했던 대마두는 촌각도 지나지 않아 더없이 비참한 죽음을 맞이할 터였다.

하지만.

“어느 정도 맞는 말을 하긴 했어. 그래, 나 따위는 당신을 죽일 수 없지.”

“……뭐?”

사박.

혈검마군의 반사적인 물음에, 대술사는 대답 대신 사뿐히 뒷걸음질 쳤다.

그리고 그 말에 담긴 의미를 이해하지 못한 혈검마군을 뒤로한 채, 짐짓 과장되기까지 한 움직임으로 양팔을 활짝 펼쳤다.

“오늘 이 자리에서 당신을 죽일 수 있는 사람은, 오직 단 한 사람뿐이니까.”

바로 그때.

촤르륵.

쇠사슬보다도 굵고 단단해진 초목의 줄기가 주인의 의지에 반응했다.

그리고 마치 지능을 가진 생물체처럼 움직인 그것들은, 죽은 듯이 눈을 감은 채 깊은 잠에 빠진 한 청년의 육신을 주인의 앞으로 데려왔다.

정확히는, 깊은 잠에 빠진 ‘것처럼 보이는’ 그를.

“괜한 연기는 집어치우고 무슨 말이라도 하는 게 어때요? 계속 그렇게 있어봤자 내 경계심만 늘어날 텐데.”

다음 순간.

“시벌. 알고 있었으면 진작 말을 했어야지.”

침까지 흐르던 입술 사이로 난데없이 튀어나온 욕설과 함께, 슬그머니 눈을 뜬 진태경이 그녀를 날카로운 눈빛으로 응시했다.



* * *



하마터면 의식을 잃을 뻔했다.

아니, 어쩌면 아주 잠깐은 정말로 그랬을지도 모른다.

생각지도 못한 누군가의 도움이 없었더라면, 나는 지금쯤 여느 때와 같이 길고 긴 악몽에 파묻혀 허우적대고 있었을 것이다.

물론, 지금의 이 상황도 꿈이나 다름없게 느껴졌지만.

‘……허.’

나는 당장이라도 새어 나오려는 실소를 삼켜야만 했다.

그래, 이건 정말로 꿈이 아니다.

여전히 바람은 거칠었고 하늘은 어둡다.

끊이지 않는 전장의 함성은 점점 더 크게 귓가를 울리고 있었으며, 그들이 휘두르는 날붙이 아래로 각자의 죽음과 삶이 교차하고 있었다.

제자리에 못 박힌 듯 굳은 얼굴로 이쪽을 바라보고 있는 적천강과 궁성의 모습을 제외한다면 언덕 아래에 펼쳐진 광경은 마지막 순간 보았던 그대로였다.

달라진 것은 없었다.

아무것도.

다만 이 언덕 위의 상황은 달랐다.

어느덧 이 좁은 공간 속, 모든 것이 뒤바뀌어 있었다.

상식, 예측, 그리고 적과 아군까지도.

그리고 죽은 듯이 눈을 감은 채 모든 것을 듣고 있던 나는 눈앞의 여인, 대마도사를 향해 이렇게 물을 수밖에 없었다.

“너……. 아니, 당신. 도대체 무슨 생각이지?”

아직까지도 이해할 수 없었다.

왜 나를 치료해 주었는지.

당장이라도 혈검마군을 멀쩡하게 회복시킬 정도의 능력이 있으면서도 도리어 그를 처치하려 하는지.

“대답해. 어서.”

나는 타오르는 눈빛으로 대마도사를 응시했다.

마음 같아서는 지금 당장이라도 이 속박 마법을 풀고 저 새하얀 목을 틀어쥐고 싶었지만, 지금의 내게 그 정도의 여력은 없었다.

고작해야 흐려지는 의식의 끈을 간신히 부여잡고 사지를 조금이나마 자유롭게 움직일 수 있는 수준.

내게 깃든 치유의 힘에는, 딱 그 정도의 목적과 의도가 담겨 있었다.

그리고 그런 나를 향해 대마도사는 담담한 목소리로 입을 열었다.

“아쉽네요. 내가 당신이라면 그런 질문 따위에 얼마 없는 기력을 낭비하진 않을 텐데.”

“뭐?”

“질문 자체가 틀렸어요. 지금의 이 상황은, 내 의지로 인해 벌어진 일이 아니니까.”

“……!”

대마도사의 말에 담긴 의미를 알아차린 순간, 나도 모르게 눈이 크게 뜨였다.

“……그렇다는 건?”

“지금 당신이 생각하는 바가 맞아요. 사냥개는 언제나 소임을 다할 뿐이죠. 주인의 명령에 따라서.”

침착하게 대답한 대마도사는 혈검마군을 가리키며 말을 이었다.

“맡은 소임이 다하면, 필요도 없어지는 법이고요.”

등골이 서늘해질 만큼 차가운 한 마디.

그리고 애써 부정하던, 아니 누구라도 부정할 수밖에 없을 만큼 충격적인 진실과 직면한 혈검마군은 혼백이 빠져나간 눈빛으로 그녀를 바라보고 있었다.

“도대체…… 왜?”

그것은 나 역시도 묻고 싶은 말이었다.

도대체 왜, 무슨 이유로 천주는 혈검마군을 버리려 하는지.

그로 인해 이 거대한 전쟁의 향방을 결정지을 수도 있는 이 중요한 전투를, 어떻게 이토록 아랑곳하지 않고 내팽개쳐 버릴 수가 있는지.

하지만 그 의문에 대마도사는 대답하지 않았다.

다만 뜻 모를 눈빛으로 나를 응시하며, 천천히 입술을 뗐다.

“당신은 여기에서 쓰러져서는 안 되니까. 더 강해져야 하니까.”

“뭐……라고?”

“그를 죽이세요. 그리고.”

피처럼 붉은 입술이, 면사 아래로 달싹였다.

“더 강해지세요.”
```

## Final English reading copy

```markdown
# Chapter 1049

In that instant, the Blood-Sword Demon Lord’s mind went blank save for a single thought.

*Am I dreaming?*

It was a perfectly natural question.

How could it not be?

The woman before him, the Grand Mage, was his ally.

They served the same master and shared the same goal.

That was why the Blood-Sword Demon Lord could hardly accept the unbelievable sight before his eyes as reality.

Not until the next moment, when the Grand Mage—who had been silently looking down at him—parted her tightly closed lips.

“Are you still dreaming?”

“…What?”

“This isn’t a dream, Demon Lord. It’s very much real.”

The Blood-Sword Demon Lord stared blankly at the Grand Mage, thinking about what her voice had just whispered into his ear.

About why this was happening.

And then, as if to prove her words—that all of this was real—the agony spreading through every inch of his body hit him. He barely managed to squeeze out a voice.

“Your joke… has gone too far.”

“A joke? I’m afraid I don’t know what you mean.”

The woman tilted her head with an innocent air. The Blood-Sword Demon Lord clenched his teeth.

Rage surged from deep in his chest, and blood welled up with it.

“Hurry. Cough. Hurry and heal me.”

“You don’t need to worry about that anymore.”

Beneath her veil, her red lips curved softly.

The Grand Mage smiled at the Blood-Sword Demon Lord, who was panting hard, then turned her head and added,

“I’ve already finished healing you.”

She was telling the truth.

It was healing in the truest sense of the word.

Not complete healing, but enough to hold on to someone’s consciousness as it slowly sank into darkness.

Hoooo.

His ragged, wheezing breaths steadied. His deathly pale face and lips gradually regained their color.

As the warm radiance surrounding the young man faded away completely, the Grand Mage’s slender fingers swept through the air.

Crack! Shhhhk!

The earth split open like a sealed box being forced apart.

At the same time, plant stems hidden deep beneath the earth surged up, coiling around the young man—Jin Taekyung—and lifting him into the air.

As if to show him to the intruders who were still rushing toward the hill at full speed.

And when Jeok Cheongang and the Bow Saint saw Jin Taekyung bound like a hostage in the distance, they had no choice but to stop. They couldn’t tell exactly what had happened.

“I’m a little sad my sincerity didn’t get through, but what can you do? This is the only way.”

The Blood-Sword Demon Lord stared blankly at the Grand Mage as she clicked her tongue softly. Only then did he finally understand.

This was no mere dream or cruel prank.

“Why?”

The question held a multitude of meanings.

But the answer that came back was brief and clear.

“Because that person wants it.”

Her silver-white veil swayed.

The Grand Mage’s eyes, faintly visible behind it, were devoid of emotion. They no longer looked at him as a subordinate might look at a superior.

Her calm voice, addressed to the Blood-Sword Demon Lord, who had gone rigid as a statue, was no different.

“You’ve had a good long life to run wild. It’s about time you got some rest, don’t you think?”

Maybe it was because his senses were slowly growing dull even now.

Or maybe it was the shock of something he’d never expected.

The Blood-Sword Demon Lord had been listening blankly to her voice echoing in his ears like a distant call when a word suddenly slipped out.

“Bullshit.”

His voice carried unmistakable exhaustion, but within it lay unshakable certainty.

The certainty that he couldn’t possibly be abandoned like this.

Even if his master had always thought of him as nothing more than a hunting dog, he wouldn’t throw him into the cauldron so pointlessly.

The old saying about cooking the hound after the hare is dead?

That only happened after the hunt was over.

But what was the state of the Lord of Heaven—of Dark Heaven—now?

The Western Heaven Demon Lord and the Southern Heaven Demon Empress had fallen. Then the Eastern Heaven Demon Lord and the North Heaven Demon Lord had fallen, too.

The four fiercest beasts he’d trusted most were gone.

The Central Plains martial world, rallied under the Murim Alliance’s banner, was no mere hare. And the Blood-Sword Demon Lord, who had survived alongside the Blood Lord, was more than a hunting dog.

The proof was that he had brought an army of tens of thousands all the way here under his command.

And that wasn’t all.

He only had to reach out a little farther—just a little—and sweet victory would be his.

If only this damned body could recover.

If he took Jin Taekyung hostage, he could handle even the Fire King and the Bow Saint.

Dominion over Gansu lay before him—a bridgehead for victory across the realm.

*And he thinks he can abandon me now?*

The Blood-Sword Demon Lord gave a hollow laugh.

Then he glared with crimson-black eyes at the insolent woman trying to drive a wedge between him and his master with such absurd lies.

“Enough of your nonsense, woman. Do you think he doesn’t know you betrayed him?”

There was no doubt about it.

The Grand Mage. That filthy traitor had ruined everything.

The only reason he was in this situation was that he hadn’t recognized the tumor growing inside his own ranks.

“Tell me, what did those deceitful bastards promise you? A grand estate? Mountains of gold and treasure? Or a stunningly handsome man to satisfy those filthy desires of yours?”

The Blood-Sword Demon Lord spat out the words, his voice boiling over.

He was angrier now than he’d ever been.

Looking back, things had seemed suspicious from the beginning.

The Grand Mage had stopped him when he tried to step into the battle without hesitation. Because of that, the Black Ghosts, their core fighting force, had been wiped out.

And even though she could use powerful spells the Blood-Sword Demon Lord himself hadn’t known about, she had refused to help to the very end.

He’d been deceived.

Thoroughly toyed with.

That unbearable truth made the Blood-Sword Demon Lord thrash about.

“You dare! Do you think a mere woman like you can kill me? Do you think you can ruin his grand plan with this little stunt?”

Crack. Thud.

From the crater left by their earlier collision, the Blood-Sword Demon Lord used every ounce of strength he had to haul himself upright.

He had lost an arm. The tendons in his leg had been severed, and his joints shattered. Even so, he still had the endurance and vitality that an ordinary person couldn’t even imagine.

But consumed by his fury, the Blood-Sword Demon Lord had forgotten the most important fact.

The reason he’d survived injuries that should have killed him outright several times over was that the Grand Mage’s Magic had been imbued in his body.

“Can I kill you? Of course I can.”

The Grand Mage watched impassively as the Blood-Sword Demon Lord crawled out of the crater toward her, then added,

“And it would be very easy.”

She was telling the truth.

She didn’t even need to use Magic against the Blood-Sword Demon Lord in his current state.

All she had to do was dispel the body-enhancement Magic she’d placed on him.

If the Grand Mage decided to kill him right now, the fiend who had once made his mark on an entire age would meet a miserable death in moments.

“But…”

The Grand Mage continued.

“You’re right about one thing. Someone like me can’t kill you.”

“…What?”

Step.

In response to the Blood-Sword Demon Lord’s reflexive question, the Grand Mage took a light step backward instead of answering.

Then, leaving the Blood-Sword Demon Lord behind as he struggled to understand what she meant, she spread both arms wide in a movement that was almost exaggerated.

“Because there’s only one person here who can kill you today.”

At that very moment—

Shhhhk.

The plant stems, now thicker and sturdier than chains, responded to their mistress’s will.

They moved as if they were living creatures with minds of their own, carrying the young man before their mistress. His eyes were closed, and he looked to be in a deep sleep.

Or rather, he looked as if he were in a deep sleep.

“Enough with the pointless act. How about you say something? If you keep lying there, you’re only going to make me more suspicious.”

The next moment—

“Fuck. If you knew, you should’ve said so sooner.”

A curse burst from Jin Taekyung’s lips, which still had drool on them. He slowly opened his eyes and fixed the Grand Mage with a sharp gaze.

* * *

I’d nearly lost consciousness.

No—maybe I really had, for a little while.

If someone hadn’t helped me when I least expected it, I’d probably be floundering in another long, endless nightmare by now.

Of course, even this situation felt like a dream.

*…Hah.*

I swallowed the laugh that was about to escape me.

Right. This really wasn’t a dream.

The wind was still fierce, and the sky was dark.

The unceasing cries of battle were growing louder in my ears. Beneath the blades they swung, life and death crossed paths.

Aside from Jeok Cheongang and the Bow Saint, staring at me with faces frozen in place, the scene below the hill was exactly as I’d last seen it.

Nothing had changed.

Nothing at all.

But the situation on this hill was different.

In this narrow space, everything had turned upside down.

Common sense, expectations, even friend and foe.

And I, who’d been listening to everything with my eyes closed as if I were dead, had no choice but to ask the woman before me—the Grand Mage—

“You… No. What exactly are you thinking?”

I still couldn’t understand.

Why she’d healed me.

Why she was trying to finish off the Blood-Sword Demon Lord when she had the power to restore him to full health right now.

“Answer me. Come on.”

I glared at the Grand Mage, my eyes burning.

I wanted to break this binding Magic right now and grab her by that pale throat. But I didn’t have the strength for that.

All I could do was barely cling to my fading consciousness and move my limbs a little more freely than before.

That was all the healing power inside me was meant to do.

The Grand Mage spoke to me in a calm voice.

“That’s a shame. If I were you, I wouldn’t waste what little strength I had on questions like that.”

“What?”

“Your question is wrong. This situation isn’t happening because I chose it.”

“……!”

As soon as I grasped the meaning of her words, my eyes widened.

“…You mean?”

“You’re thinking along the right lines. A hunting dog only ever does its job. It follows its master’s orders.”

The Grand Mage calmly answered, then pointed at the Blood-Sword Demon Lord and continued,

“And when its job is done, it’s no longer needed.”

Her words were so cold they sent a shiver down my spine.

The Blood-Sword Demon Lord had done his best to deny it. Anyone would have. But now he was facing a truth so shocking that it seemed impossible to deny, his eyes staring at her as if his soul had left his body.

“Why…?”

That was the question I wanted to ask, too.

Why? For what reason was the Lord of Heaven abandoning the Blood-Sword Demon Lord?

How could he so casually throw away this crucial battle, one that could determine the outcome of this enormous war?

But the Grand Mage didn’t answer.

Instead, she gazed at me with an inscrutable look and slowly parted her lips.

“You can’t fall here. You have to get stronger.”

“What… did you say?”

“Kill him. And then…”

Her lips, red as blood, moved beneath the veil.

“Get stronger.”
```
