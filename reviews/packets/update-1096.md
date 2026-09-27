<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1096.txt",
      "sha256": "ddaff1ca74c2053c2f66d21d58e8adf67d68df466209c46b83411aaea4ba9e6f",
      "bytes": 16478
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "49276300d8d19e729e8fe184279a7280f0e66a827824344fd5a1dde1f873bd44",
      "bytes": 1232
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "aa2e383c274853719aee6fdad641fd15982ff6289e42ddd0f942d170d98f7815",
      "bytes": 243957
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "e8237ca99621ea6ac8c56171e139eaba0ac0aeeb41d7663be6f4852f2700875a",
      "bytes": 847
    },
    {
      "path": "characters/Cheongheoja.md",
      "sha256": "949a9edfd9366baac43dd02e6bdcdcc08eb5650f13803980c8b5ee21ebe0f554",
      "bytes": 544
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "e9ec310eeb6a0cf96bb9661b4c1bbb8e19d06a7612f7f08bece1047f1766e608",
      "bytes": 1120
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c7c938b3e958af47e725813bd7e931222012f6cfc2400843f47c313c865fd3ac",
      "bytes": 760
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "525a28bafe8235bae1d2b92101be2c2426621074f25685130a0f8c7d3a0783e6",
      "bytes": 651
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "fd55be8bd622e6c9cf52fde1677cd94921a79a326dc4f9cb597b153c7e2fbc86",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e89eb247c9da5bcadeea165605ef883ea6dbb8c0a22cbbb28eda13d3ee7a5415",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "35bbcb15e62ea219976f1028efcaeb3173c070bf144f0b0c41055fb9ba821267",
      "bytes": 623
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "104fa790aae40c04f7e47f59045be3fdcfdbedb3570297259d291dfb7dcf88b3",
      "bytes": 1084
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ebe79c16d6adf08cf85ebe92be4ce390014b7513b9c2f13e94caedd0cd180dd5",
      "bytes": 287086
    }
  ],
  "estimated_tokens": 14827
}
-->

# Durable State Update — Chapter 1096

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
1 and safe_through 1096. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1096. Profile updates may replace only one
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
  "chapter": 1096,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1096,
    "continuity_sources": [1096],
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
    "Dark Heaven’s army has encircled Xining under the Blood Lord; the Potala Palace has arrived with elephants and joined its forces.",
    "The Nanman Beast Palace has left its bloodied homeland, sworn to join the Murim Alliance and avenge its people, and is moving with its people and beasts.",
    "The Lord of Heaven’s objective at Xining is Jin Taekyung.",
    "The Blood Lord gives Taekyung one day to sever his sinews and meridians and surrender, promising to spare everyone else if he does.",
    "Namho fears Sichuan may be exposed to enemies from Tibet after the Nanman Beast Palace’s departure."
  ],
  "continuity_sources": [
    1095
  ],
  "open_questions": [
    "Will the Nanman Beast Palace and other reinforcements reach Xining in time to affect the battle?",
    "Will Taekyung surrender, and what will happen when the Blood Lord’s one-day ultimatum expires?",
    "Will Sichuan be attacked from Tibet after the Nanman Beast Palace’s departure?"
  ],
  "safe_through": 1095,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” when naming the region in the Murim setting; retain “Tibet” as Taekyung’s modern-world identification of it."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 일격     | **One Strike**                         |
| 보상               | **Reward**                     |
| 청해     | **Qinghai**            |
| 화산     | **Huashan**            |
| 곤륜     | **Kunlun**             |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 청허자 | **Cheongheoja** | Kunlun Sect Leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화산신룡 | **Huashan Divine Dragon** | Title given to Cheongpung after the Star-Array Grand Banquet. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 소멸 | **Erasure** | Jin's term for the Skeleton Warlord's destruction by the Arch Lich's mana. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 포달랍궁 | **Potala Palace** | Palace in Tibet. |
| 황하 | **Yellow River** | River along which civilization began. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |
| 서녕 | **Xining** | Capital of Qinghai. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 천주 | 대술사 | master to servant | you | commanding and authoritative | Addresses her through mind-voice, ordering her to report, raise her head, and depart. |
| 대술사 | 천주 | servant to master | Lord of Heaven | extremely deferential | Uses reverent titles and self-abasing language while reporting and pleading. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 진태경 | 현천진인 | young martial artist addressing a senior Daoist Sect Leader | Perfected Being | polite | Jin responds respectfully to Hyeoncheon's assessment of the retreat. |
| 현천진인 | 진태경 | Kongtong Sect Leader addressing an allied martial artist | Daoist Friend Jin | respectful and measured | Refers to Jin as 진 도우 while discussing the Zhongnan Disciples’ future. |
| 적천강 | 청허자 | senior martial master to former acquaintance and younger martial master | you / Fellow Daoist | blunt and familiar | Jeok Cheongang mocks Cheongheoja for addressing him as a fellow Daoist. |
| 궁성 | 청허자 | fellow martial master and former acquaintance | Cheongheo | polite and familiar | Uses his shortened name and remarks on his graying hair. |
| 살성 | 청허자 | fellow martial master and former acquaintance | you | blunt and familiar | Recognizes him from a prior meeting. |
| 청풍 | 청허자 | younger martial artist to senior sect leader | Grandpa Cheongheoja | cheerful and polite | Uses a friendly, familial form because they share the surname Cheong. |
| 진태경 | 청허자 | younger martial artist to senior sect leader | Sect Leader | respectful | Uses a formal greeting and bow. |
| 청허자 | 진태경 | senior sect leader to younger martial artist | Fellow Daoist Jin | warm and polite | Greets Taekyung by surname and confirms Hak Woo is well. |
| 청풍 | 대인 | younger companion addressing an older benefactor | Uncle Great Sir | polite and familiar | Cheongpung repeatedly calls him 대인 아저씨. |
| 대인 | 청풍 | older benefactor addressing a younger companion | you | familiar and teasing | Great Sir addresses Cheongpung as 자네. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1095
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; strategically manipulates allies and adversaries, and conceals failures from the Lord of Heaven when he fears being discarded.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven with deep loyalty and carries out his plan to target Jin Taekyung, whom he promises to spare if Taekyung surrenders; he considers Taekyung and Cheongpung formidable adversaries.

### Cheongheoja.md

# Cheongheoja (청허자)

- **Safe through:** Chapter 1094
- **Aliases:** None
- **Role:** Cheongheoja is the Kunlun Sect Leader and Hak Woo’s master.
- **Personality:** Warm, composed, and patient, he faces setbacks with resolve and receives even startling company with good humor.
- **Voice:** Measured and gentle, using formal Daoist courtesies and calm metaphors.
- **Relationships:** Hak Woo is his Disciple; he knows Jin Taekyung by reputation and treats him warmly.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1095
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has also learned concealment from the Slaughter Saint.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, competitive pride, and compassion that leaves him unsettled by killing; he admires Taekyung’s resilience in the way he lives.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint has become his mentor in concealment.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1095
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1094
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1093
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1095
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1095
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1092
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

## Korean source

```text
1096화




구구구궁.

거대하면서도 육중한 서녕의 철문이 천천히 입을 벌린다.

조금 전 혈주의 손짓과 함께, 좌우로 갈라진 포위망을 벗어나 성문으로 향하는 적들의 뒷모습을 바라보던 대술사가 입술을 뗐다.

“너무 쉽게 풀어줬다고 생각하지 않아?”

“어쩌면, 그럴지도 모르지. 하지만…….”

나직하게 대꾸한 혈주가 드높이 우뚝 서 있는 성벽을 턱짓하며 덧붙였다.

“이대로 곧장 일전을 치렀다면, 우리 쪽 피해도 만만치 않았을 거야.”

대술사도 어느 정도는 그 말에 동의하는 바였다.

변방 중에서도 변방에 속한 청해성은 오랜 과거부터 혹시 모를 외적(外敵)의 침입에 맞서 준비되어 있는 최전선.

그래서인지 거대한 암석을 다듬어 쌓아 올린 석벽은 중원에 비할 수 없이 단단했고, 그 위에는 이미 은빛 화살촉이 번뜩이고 있었다.

거기에 더하여, 천천히 열리기 시작한 서녕의 성문 너머로 보이는 무수한 창칼의 숲도 함께.

“궁지에 몰린 만큼 더 필사적으로 몸부림쳤을 거다. 놈들에게도 무언가를 물어뜯을 이빨은 있으니.”

하찮은 쥐새끼조차 상황이 위급하다고 판단되면 고양이에게 달려드는 법인데, 하물며 저들이야 오죽할까.

게다가 초절정 고수만 무려 일곱.

아니, 끝끝내 성벽 아래로 내려오지 않은 대인이라는 수수께끼의 인물까지 포함한다면 총 여덟이나 된다.

더불어 별다른 손실 없이 일찌감치 서녕에 집결한 청해 무림인과 관군들까지 있으니, 혈주의 판단도 그리 틀린 것만은 아니었다.

물론, 대술사가 생각하기에 그가 이러한 판단을 내린 가장 결정적인 이유는 따로 있었지만.

‘확신이 없었던 거야. 그분의 뜻대로 진태경을 생포할 수 있을 거라는, 아니 어쩌면 그것을 넘어 승리에 대한 완전한 확신조차도.’

그러나 마음속에서 맴도는 그 생각을, 대술사는 굳이 소리 내어 내뱉지 않았다.

그녀에게 있어 혈주는 도무지 좋아할 수 없는 인간군상이었지만, 이런 상황에서까지 같은 주인과 목표를 공유하는 그의 역린(逆鱗)을 건드릴 필요는 없었으니까.

그와 동시에, 한편으로는 진태경을 비롯한 초절정 고수들을 순순히 돌려보낸 혈주의 판단에 일부나마 고개를 끄덕이기도 했다.

“뭐, 아쉽긴 하지만 어쩔 수 없지. 그분께 청해성의 일을 가장 먼저 위임받은 건 내가 아니니까.”

“별일이군. 네 입에서 그런 말이 나오다니.”

“공과 사는 구분하는 편이야. 쉽지 않은 전투가 될 거라는 건 나 역시도 충분히 느끼고 있었고.”

초절정의 경지에도 급이 있다.

그리고 그런 의미에서 보자면, 조금 전 그들이 포위하고 있었던 일곱 명의 초절정 고수들은 평범한 수준을 훌쩍 벗어난 존재들이었다.

비록 진태경의 활약상에 의해 조금 가려진 부분이 있지만, 타고난 무재(武才)만 따지자면 고금제일이라 해도 이상하지 않을 화산신룡 청풍.

공동과 곤륜이라는 저 유서 깊은 두 도맥(道脈)을 이끄는 현천진인과 청허자.

별다른 수식어조차 필요가 없는 궁성과 살성, 그런 그들과 비견되는 화왕 적천강.

마지막으로, 지난 행보를 통해 자신의 존재 자체가 변수나 다름없다는 것을 증명해 온 열화신룡 진태경까지.

그 압도적이면서도 화려한 면면들을 보고 있자면, 불사에 가까운 흑귀(黑鬼)들의 존재감마저 흐릿해질 지경이었다.

“만약 전투가 벌어졌다면, 최소한 우리의 안위를 떠나 저것들은 전부 소멸을 피하지 못했겠지.”

묵묵히 서 있는 흑귀들을 가리키며 입을 연 대술사가 덧붙였다.

“물론, 이미 하나는 형태도 못 남긴 채 녹아 버렸지만.”

그만큼 적천강이 전력을 다한 일격은 강력했다. 그녀가 펼친 방어 마법마저 일부나마 파훼시킬 정도로.

“거기에 더해, 살성과 궁성까지 끼어든다면 말할 것도 없겠지. 게다가 진태경은…… 나로서도 잘 이해할 수 없는 무언가가 있어.”

강자 지존의 무림에서 힘의 논리는 정직하다.

강자가 약자를 병탄하고, 약자가 강자에게 짓밟히는 것이 당연한 이치였다.

하지만 대술사가 지켜본 바에 의하면 오직 한 사람, 진태경만큼은 그 논리에서 누구보다 멀찍이 벗어나 있는 존재였다.

비록 매번 생사를 오가는 위기 때마다 주변인들의 도움을 받았다고는 해도, 네 명의 마군과 마후를 쓰러트린 것은 단순한 우연이 아니었다.

왜 선택받은 자라 불리는지 납득이 될 만큼.

“그런 이유에서겠지. 그 아이가 가진 특별함이, 그분을 그토록 집착하게 만드는 거야.”

미약한 탄성마저 담긴 대술사의 음성을 들은 혈주의 입매가 비틀렸다.

‘집착. 집착이라…….’

마음속 뇌까림과 함께, 그는 어느새 서서히 닫혀 가는 성문을 바라보았다.

정확히는 성문 사이로 사라져가는 진태경의 뒷모습을.

그리고 조금 전 자신이 했던 말을 불현듯 떠올렸다.



‘너는 호숫가에 드리워진 낚싯대가 주인의 마음을 알고 있다고 생각하나?’



그것은 비단 진태경에게만 하는 말이 아니었다. 

스스로에게 던지는 자조 섞인 질문이자, 이 자리에 없는 천주에게 건네는 간곡한 투정이었다.

‘왜 저 녀석만 당신께 특별한 존재인 겁니까. 도대체 왜?’

지금 이 순간, 혈주에게 있어 가장 죽이고 싶은 존재는 자신의 팔을 한 차례 빼앗아 간 매종학도, 적천강도 아니었다.

바로 진태경이었다.

불과 이 년 남짓한 시간 만에 거목으로 성장한 애송이.

하지만 이제는 한 걸음으로 짓밟을 수 있는 샛노란 새싹 따위가 아닌, 깊은 뿌리와 굵은 가지를 지니게 되었음에도 그의 주인은 당신의 하인들에게 벌목(伐木)을 허락하지 않았다.

‘천주이시여. 당신께서 진정으로 원하시는 것이 무엇인지, 이 어리석은 종복으로서는 도무지 짐작하기 어렵나이다.’

낚싯대.

미끼를 문 대어(大魚)의 힘을 이기지 못해 부러진다 해도, 그저 교체하면 그만인 낚싯대.

스스로의 의지로 내뱉은 그 세 글자와, 그것에 담긴 의미가 유난히도 무겁게 혈주의 가슴을 짓눌러 오던 그때였다.

부우우우!

길게 울려 퍼지는 뿔피리 소리와 함께, 서서히 속도를 줄인 포달랍궁의 군세가 이십여 장 밖에서 멈춰섰다.

그리고 철탑처럼 우뚝 멈춰 선 수백 마리의 코끼리 중, 가장 크고 화려하게 치장된 열세 마리의 코끼리가 앞으로 나섰다.

쿵, 쿠웅!

천천히 고개를 든 혈주의 얼굴 위로 드리워지는 거대한 그림자.

육중한 굉음을 토해 내며 혈주의 앞까지 도달한 코끼리들의 머리 위로, 누군가의 음성이 떨어져 내렸다.

“오랜만이오, 시주.”

중원인이 들었다면 코웃음을 쳤을 것 같은 어눌한 한어(漢語).

하지만 그 음성에 실린 막강한 공력과 위엄은 일파의 대종사(大宗師)만이 지닐 수 있는 종류의 것이었고, 선명한 분노마저 실려 있었다.

“한데.”

파팟!

거친 파공성과 함께 지면으로 떨어져 내리는 열세 개의 신형. 

그 중심에는 마치 말라 비틀어진 고목 나무처럼 호리호리한 키와 앙상한 뼈마디를 지닌 노승이 있었다.

“빈승(貧僧)이 잘못 본 것이 아니라면, 충분히 설득력 있는 설명이 필요한 상황인 것 같구려.”

하나의 왕국처럼 서장을 지배하는 포달랍궁의 궁주, 혹은 그들만의 오랜 관습으로는 달뢰라마(達賴喇嘛)라 칭해지는 노승이 형형한 안광으로 혈주를 응시했다.

“왜 저들을 그대로 보내 준 거요? 빈승이 제아무리 늙어 눈이 흐릿해졌다고는 하나, 멀리서 보기에도 분명 범상치 않은 자들이었거늘.”

상념에서 깨어난 혈주는 고개를 돌려 이미 굳게 닫힌 성문을 응시했다.

그리고 상당한 전력을 이끌고 와준 달뢰라마를 향해, 사람 좋은 미소를 지어 보였다.

“역시 궁주시군요. 정확히 보셨습니다.”

하지만 매우 보기 드문 혈주의 친절한 태도에도, 달뢰라마는 조금도 웃지 않았다.

지극히 폐쇄적인 종교 집단의 수장인 그가 수십여 년 전 암천의 제안에 응하여 동맹 관계를 구축하게 된 결정적인 이유도.

포달랍궁의 서장의 모든 전력을 끌어모아 청해까지 온 가장 큰 이유 중 하나도 바로 이곳에 있었으니까.

“하면 설마 하는 노파심에 묻건대.”

어눌함 따위는 조금도 느껴지지 않을 만큼 차가운 어조로, 달뢰라마가 말을 이었다.

“조금 전 시주께서 돌려보낸 적 중, 혹 혹 빈승이 찾고 있는 자들도 포함되어 있었소?”

바로 그 순간이었다. 

촘촘하게 짜인 은백색의 면사 너머로 대술사의 입술이 달싹인 것은.

- 혹시나 해서 말하는 거지만…… 잊지 마. 적어도 우리의 목적을 이루기 전까지, 포달랍궁은 제법 쓸모있는 패라는 사실을.

대답하기도 전에 한발 앞서 귓가를 파고든 대술사의 만류에, 혈주는 자신도 모르게 입꼬리를 비틀었다.

‘우리의 목적, 이라고?’

평소라면 대수롭지 않게 넘어갔을 그 한마디가, 지금만큼은 어째서인지 우습기 짝이 없었다.

그녀도, 자신도.

어차피 누군가에게는 언제든 갈아 치울 수 있는 낚싯대에 불과한데.

‘내 목적은 처음부터 줄곧 하나뿐이었다. 몸과 마음을 다해 그분을 보필하여, 만천하의 주인이자 어버이로 군림토록 돕는 것.’

그러나 어째서일까.

도대체 왜.

자신의 주인이, 위대한 천주께서 바라시는 것이 광대한 천하가 아닌 한 청년뿐이라는 어처구니없는 생각이 드는 것일까.

“하.”

끝끝내 참지 못하고 터져 나온 실소.

그런 혈주의 모습에 달뢰라마의 눈빛이 더욱더 깊숙이 가라앉았다.

“아직 대답을 듣지 못했소만.”

혈주가 웃음기 어린 음성으로 대꾸했다.

“그거야 뭐, 이미 짐작하고 계시지 않습니까?”

“그렇다는 건, 설마?”

“맞습니다. 화왕 적천강. 그리고 열화신룡 진태경. 궁주께서 그토록 찾아 헤매던 열화문(烈火門)의 종자들도 저들 중에 있었지요. 아, 그러고 보니…….”

딱딱하게 굳은 얼굴로 서 있는 달뢰라마의 발치를, 혈주가 곧게 편 손가락으로 가리키며 덧붙였다.

“지금 서 계신 바로 그 자리에 있었던 것 같군요. 물론, 어디까지나 촌각 전의 이야기지만.”

“……!”

“……!”

일순간, 주위의 공기가 요동쳤다.

그것은 달뢰라마가, 더불어 포달랍궁에서도 최고의 실력자들로만 이루어진 십이밀승(十二謐僧)이 뿜어내는 기세였다.

“그렇게 쉽게 돌려보냈다는 건가? 빈승이, 아니 우리가 얼마나 열화문을 증오하는지 알면서도?”

불현듯 달뢰라마의 입술을 비집고 흘러나온, 열사(熱沙)의 사막처럼 건조한 음성.

지금 이 순간, 광대한 서장 무림의 지배자는 진심으로 분노하고 있었다.

열화문.

잊으려야 잊을 수 없는, 포달랍궁의 밀승이라면 모두가 아는 그 저주받을 이름.

단지 필요 이상으로 호전적이라는 평가를 받고 있던 불교의 한 종파였던 포달랍궁을, 강력한 무력을 지닌 하나의 교국(敎國)으로 변모하게끔 만든 존재들.

“감히 약속을 어기다니, 이게 도대체 무슨 짓거리지?”

“이거 참…….”

어느덧 자연스러워진 하대와 함께, 서릿발 같은 기세로 자신을 노려보는 달뢰라마의 모습에 혈주가 피식 웃었다.

“똑똑히 기억하고 있으니 걱정마십시오. 이백 년이나 낡은 그 눈물겨운 사연도, 서로 간에 오간 그 끈끈한 약속도.”

“뭐라?”

대수롭지 않게 돌아온 대답에 달뢰라마가 눈을 부릅뜬 그때. 혈주가 나직한 음성으로 덧붙였다.

“한데, 저와 달리 궁주께서는 까맣게 잊어버리신 모양입니다.”

“잊었다니. 그게 무슨.”

“본인이 가장 잘 아시잖습니까. 지금의 포달랍궁이 있기까지 그분께 얼마나 큰 도움을 받았는지.”

“그건.”

일순간 말을 잇지 못하고 입술을 깨무는 달뢰라마의 모습에, 혈주가 작게 혀를 찼다.

“앞서 말했듯이, 약속은 반드시 지킵니다. 궁주께서 진태경을 사로잡는 것에 크게 일조하신다면, 화왕 그 늙은이의 신병은 물론이고 충분한 보상을 드리지요.”

잠시 침묵하던 달뢰라마가 무겁게 입술을 뗐다.

“그 말, 어떻게 믿을 수 있지?”

“왜, 못 믿겠습니까?”

“그분은 믿네. 하지만 자네는 놈들을 빈승의 눈앞에서 놓아줬지. 절호의 기회였음에도.”

혈주의 입가에 조소가 어렸다.

달뢰라마가 내비치는 불신이 불쾌해서가 아니라, 진정으로 그렇게 생각하는 그가 가소로웠기 때문이었다.

암천의 전폭적인 지원이 있었다고는 하나, 이를 감안하더라도 현재까지 포달랍궁의 일구어 낸 전력은 분명 강력하다. 

그중 최고의 고수인 달뢰라마의 무위 역시 말할 것도 없다. 당장 적천강을 제외한 십왕(十王)의 한 사람과 맞붙는다 해도 결코 아래가 아니었으니.

그러나.

‘딱 그 정도야. 당신은.’

무위의 고하를 따지는 문제가 아니다. 

내면의 그릇의, 사람 자체의 문제다.

그렇기에 혈주가 무엇을 예상하고 저들을 풀어줬는지 이미 알고 별다른 말을 하지 않는 대술사와 달리, 달뢰라마는 눈앞의 대어를 놓쳤음에 안타까워하는 것이다.

“아직도 모르겠습니까?”

“도대체 무엇을……?”

“저는 모든 것을 확실히 하고 싶었을 뿐입니다. 조금이라도 빠져나갈 빈틈조차 없이.” 

뭐라 말하려던 달뢰라마가 문득 무언가를 깨닫고 눈을 크게 떴다.

“설마?”

혈주가 말없이 고개를 끄덕였다.

그의 예상이 맞다면, 바로 오늘쯤일 것이다.

장강수로맹이 이끄는 수백 척의 함선이 마침내 청해로 이어지는 황하(黃河)의 지류에 접어들고, 녹림맹이 사전에 합류한 일만의 교도들과 함께 그들과 접선하는 것은.

“앞으로 하루, 길어도 이틀. 그 안에 이 전투는 끝납니다.”

가파른 물살을 가르고 청해에 도달하여 아주 미세한 틈새마저 틀어막을, 총 삼만의 추가 병력.

그것이 이 전투에서 확실한 승리를 가져다줄 마지막 열쇠였다.

진태경에게 하루 동안 생각할 말미를 준 것 역시도.

약속?

애초부터 지킬 생각 따위는 없었지만, 내심으로는 부디 진태경이 스스로 사지근맥을 끊는 멍청한 짓거리를 하지 않기를 바랐다.

그래야만.

진태경이 결사항전을 각오해야만 놈을 죽일 수밖에 없는 명분이 생기니까.

‘천주시여, 용서하소서. 설령 당신께서 그것을 원치 않는다 해도, 제 행동은 오직 충심으로 비롯된 것입니다.’

스스로의 죄를 고하듯, 마음속 깊이 뇌까린 혈주는 천천히 입술을 뗐다.

“그러니까…….”

조금 전보다 훨씬 밝아진 안색으로 자신을 바라보고 있던, 달뢰라마를 향해.

“입 닥치고 있어. 두 번 다시 내게 하대하는 순간 그 아가리를 찢어 버릴 테니까.”

“……!”

순간 얼어붙은 달뢰라마를 보며, 혈주는 광포하게 웃었다.

누군가에게 낚싯대 취급을 받는 것은, 한 번으로 족했다.
```

## Final English reading copy

```markdown
# Chapter 1096

Rumble, rumble, rumble.

The enormous, heavy iron gates of Xining slowly opened their mouths.

The Grand Mage watched the enemy’s backs as they passed through the encirclement, which had parted to either side at the Blood Lord’s signal, and headed for the gates. Then she spoke.

“Don’t you think you let them go too easily?”

“Maybe I did. But…”

The Blood Lord replied in a low voice, then nodded toward the towering city walls.

“If we’d fought them head-on right then, our losses would’ve been considerable, too.”

The Grand Mage had to admit he was right, at least to a point.

Qinghai was a frontier among frontiers, a province prepared since ancient times to stand against any foreign invasion.

Perhaps that was why its stone walls, built from enormous blocks of dressed rock, were sturdier than anything in the Central Plains. Silver arrowheads already glinted atop them.

And beyond Xining’s slowly opening gates, a forest of spears and blades stretched as far as the eye could see.

“Cornered prey fights all the harder. They still have teeth to bite with.”

Even a lowly rat would charge a cat if it thought the situation was desperate. How much more would those people?

And there were no fewer than seven Supreme Peak masters among them.

No—eight, if they counted the mysterious Great Sir who had never come down from the walls.

Then there were the Qinghai martial artists and imperial troops who had gathered in Xining early, with barely any losses. The Blood Lord’s judgment hadn’t been far off.

Of course, the Grand Mage thought there was another, far more decisive reason he’d made that choice.

*He wasn’t certain. He wasn’t certain he could capture Jin Taekyung as that person wished—or, for that matter, that they could win outright.*

But the Grand Mage didn’t say the thought circling in her mind aloud.

She could hardly stand the Blood Lord, but there was no need to touch a nerve when they shared the same master and goal.

At the same time, she could partly understand why he’d let Jin Taekyung and the other Supreme Peak masters leave without resistance.

“Well, it’s a shame, but there’s nothing to be done. I wasn’t the first to be entrusted with Qinghai’s affairs by that person.”

“That’s unusual. I never expected to hear you say that.”

“I can separate business from personal matters. I could feel it, too. That would’ve been a difficult battle.”

There were levels even among those who had reached Supreme Peak.

And in that regard, the seven Supreme Peak masters they’d just surrounded were far beyond ordinary.

Though Jin Taekyung’s exploits had somewhat overshadowed him, Cheongpung, the Huashan Divine Dragon, had martial talent so extraordinary that it wouldn’t have been strange to call him the greatest in history.

Perfected Being Hyeoncheon and Cheongheoja, who led the venerable Daoist lineages of Kongtong and Kunlun.

The Bow Saint and Slaughter Saint, who needed no embellishment—and the Fire King Jeok Cheongang, their equal.

And finally, the Blazing Flame Divine Dragon Jin Taekyung, who had proven through his every action that his very existence was a variable.

Looking at that overwhelming, dazzling lineup, even the Black Ghosts—nearly immortal as they were—seemed to fade into the background.

“If a battle had broken out, those things would’ve been wiped out, regardless of whether we survived.”

The Grand Mage gestured toward the silent Black Ghosts, then added:

“Though one of them has already melted away without even leaving a shape behind.”

Jeok Cheongang’s full-strength strike had been that powerful. It had even broken through part of the defensive magic she’d cast.

“And there’d be no question of it if the Bow Saint and Slaughter Saint joined in. Besides, there’s something about Jin Taekyung that even I can’t quite understand.”

In the Murim world, where the strong ruled above all, power followed an honest logic.

The strong devoured the weak; the weak were trampled by the strong. That was only natural.

But from what the Grand Mage had seen, there was one person—Jin Taekyung—who stood farther outside that logic than anyone.

Even if he’d received help from those around him whenever he faced a life-or-death crisis, defeating four Demon Lords and a Demon Empress hadn’t been mere luck.

It was enough to make her understand why people called him the Chosen One.

“That must be why. His special nature is what makes that person so obsessed with him.”

At the faint note of wonder in the Grand Mage’s voice, the Blood Lord’s lips twisted.

*Obsessed. Is that what it is?*

As the thought turned over in his mind, he watched the gates slowly closing.

More precisely, he watched Jin Taekyung’s back disappear between them.

And suddenly, he remembered what he’d said moments before.

*Do you think a fishing rod cast over a lake knows what its owner is thinking?*

Those words hadn’t been meant for Jin Taekyung alone.

They were a self-mocking question he’d asked himself—and a plaintive complaint addressed to the Lord of Heaven, who wasn’t here.

*Why is that brat special to you? Why, exactly?*

At that moment, the person the Blood Lord most wanted to kill wasn’t Mae Jonghak, who had taken his arm from him once, nor Jeok Cheongang.

It was Jin Taekyung.

A greenhorn who’d grown into a towering tree in barely two years.

But even though he was no longer a bright yellow sprout the Blood Lord could crush with one step, and now had deep roots and thick branches, his master still hadn’t allowed his servants to cut him down.

*Lord of Heaven. What is it you truly want? This foolish servant cannot begin to guess.*

A fishing rod.

Even if it broke under the strength of the great fish that had taken its bait, it could simply be replaced.

The three words he’d spoken of his own accord, and the meaning they carried, weighed unusually heavily on the Blood Lord’s heart.

That was when it happened.

Bwooooo!

A long blast of a horn rang out. The Potala Palace’s army slowed and came to a halt some sixty meters away.

Among the hundreds of elephants standing like iron towers, thirteen—each the largest and most lavishly adorned—moved forward.

Thud. Thud.

A massive shadow fell across the Blood Lord’s face as he slowly lifted his head.

The elephants reached him, their heavy footfalls rumbling. A voice came down from atop their heads.

“It has been a long time, donor.”

The clumsy Han speech would have drawn a snort from anyone in the Central Plains.

But the mighty internal energy and imposing authority in that voice belonged only to the grand master of a sect—and it carried unmistakable anger.

“And yet…”

With a sharp rush of air, thirteen figures dropped to the ground.

At their center stood an old monk, slender and bony, as thin as a withered tree.

“If this humble monk has not mistaken what he sees, then I believe a convincing explanation is in order.”

The old monk who ruled Xizang like a kingdom—the Potala Palace’s Palace Lord, known by their ancient custom as the Dalai Lama—fixed his piercing gaze on the Blood Lord.

“Why did you let them go? I may be old, and my eyes may be failing, but even from a distance it was clear they were no ordinary people.”

Waking from his thoughts, the Blood Lord turned to look at the gates, now firmly shut.

Then he smiled warmly at the Dalai Lama, who had brought a substantial force to join them.

“As expected of the Palace Lord. You saw them clearly.”

But even at the Blood Lord’s unusually friendly manner, the Dalai Lama didn’t smile.

One of the decisive reasons the head of that deeply insular religious sect had accepted Dark Heaven’s proposal decades ago and formed an alliance with them…

And one of the main reasons he’d gathered every last force in Xizang and brought them all the way to Qinghai…

…was here.

“Then forgive this old monk for asking, just in case.”

The Dalai Lama continued, his tone so cold there wasn’t a trace of clumsiness in it.

“Among the enemies you just sent back, were the people I’ve been searching for?”

At that very moment, the Grand Mage’s lips moved behind her tightly woven silver-white veil.

*I’m only saying this in case, but… don’t forget. Until we achieve our goal, the Potala Palace is a rather useful card to have.*

Before he could answer, the Grand Mage’s warning reached his ear first. The Blood Lord twisted his lips without meaning to.

*Our goal?*

Ordinarily, he would’ve let the words pass without a second thought. For some reason, right now they struck him as absurd.

She, too. And he, too.

They were only fishing rods, after all—things someone could replace whenever they pleased.

*My goal has been the same from the beginning. To serve that person with body and heart, and help him rule as the master and father of all under heaven.*

But why?

Why on earth was he suddenly thinking that his master, the great Lord of Heaven, wanted not the vast world, but one young man?

“Ha.”

A quiet laugh escaped him before he could stop it.

At the sight of the Blood Lord, the Dalai Lama’s eyes sank further.

“I’m still waiting for an answer.”

The Blood Lord replied, amusement in his voice.

“Surely you’ve already guessed.”

“Does that mean…?”

“That’s right. The Fire King Jeok Cheongang. And the Blazing Flame Divine Dragon Jin Taekyung. The Fire Gate Clan’s scions you’ve been searching for so desperately were among them. Ah, come to think of it…”

He pointed with a straightened finger at the spot where the Dalai Lama stood, then added:

“I believe they were standing right where you are now. Though, of course, that was only moments ago.”

“……!”

“……!”

The air around them shifted violently.

It was the aura emanating from the Dalai Lama—and from the Twelve Secret Monks, the Potala Palace’s finest fighters.

“You let them go so easily? Even knowing how much I—how much we—hate the Fire Gate Clan?”

The Dalai Lama’s voice suddenly spilled from his lips, as dry as a desert of burning sand.

At that moment, the ruler of Xizang’s vast martial world was truly furious.

The Fire Gate Clan.

A cursed name impossible to forget, known to every Secret Monk of the Potala Palace.

They were the ones who had transformed the Potala Palace from a Buddhist sect—known for being more belligerent than necessary—into a theocratic state with formidable martial power.

“How dare you break your promise? What in the world is this?”

“Well, now…”

The Dalai Lama glared at him with a frostbitten aura, and his familiar use of casual speech was now entirely natural. The Blood Lord gave a short laugh.

“Don’t worry. I remember it clearly: that heartrending story from two hundred years ago, and the unbreakable promise we made to each other.”

“What?”

The Dalai Lama’s eyes widened at the casual reply. The Blood Lord continued in a low voice.

“But it seems you’ve forgotten all about it.”

“Forgotten? What are you talking about?”

“You know better than anyone how much help you received from that person in building the Potala Palace you have today.”

“That…”

The Dalai Lama bit down on his lip, unable to continue. The Blood Lord clicked his tongue softly.

“As I said, I always keep my promises. If you help capture Jin Taekyung in a meaningful way, I’ll hand that old man, the Fire King, over to you—and give you a generous reward besides.”

The Dalai Lama was silent for a moment before speaking heavily.

“How can I believe that?”

“What, you don’t trust me?”

“I trust that person. But you let them go right before my eyes, despite the perfect opportunity.”

A sneer touched the Blood Lord’s lips.

The Dalai Lama’s distrust didn’t offend him. He simply found it laughable that the man genuinely believed that.

Dark Heaven had given the Potala Palace its full support, but even so, the strength the palace had built up was undeniable.

The Dalai Lama’s own martial prowess, the best of them all, went without saying. Even against one of the Ten Kings other than Jeok Cheongang, he wouldn’t be outmatched.

But…

*That’s all you are.*

It wasn’t a question of martial skill.

It was a question of the size of one’s inner self. Of the person one was.

That was why, unlike the Grand Mage—who already understood what the Blood Lord had expected when he let them go and said nothing—the Dalai Lama regretted losing the great fish right before his eyes.

“Do you still not understand?”

“What is it I’m supposed to understand…?”

“I only wanted to make sure of everything. To leave not even the smallest opening for them to slip through.”

The Dalai Lama was about to say something when he suddenly realized something and opened his eyes wide.

“Could it be…?”

The Blood Lord nodded without a word.

If his guess was right, it would be today.

The Yangtze River Channel League’s hundreds of ships would finally enter the Yellow River tributary leading to Qinghai, and the Green Forest Alliance would meet them with ten thousand followers who had joined in advance.

“Another day, two at most. This battle will be over within that time.”

A total of thirty thousand reinforcements would cut through the swift current and reach Qinghai, sealing even the tiniest gap.

They were the final key to ensuring victory in this battle.

That was why he’d given Jin Taekyung a day to think, too.

A promise?

He’d never intended to keep it in the first place. But deep down, he hoped Jin Taekyung wouldn’t do something foolish and sever the sinews and meridians in his own arms and legs.

Only then…

Only if Jin Taekyung resolved to fight to the death would the Blood Lord have a reason to kill him.

*Lord of Heaven, forgive me. Even if you do not wish it, my actions are born only of loyalty.*

As if confessing his sins, the Blood Lord murmured to himself, then slowly parted his lips.

“So…”

He spoke to the Dalai Lama, who was looking back at him with a far brighter expression than before.

“Shut your mouth. If you speak down to me again, I’ll tear it off your face.”

“……!”

Watching the Dalai Lama freeze in place, the Blood Lord laughed wildly.

Being treated like a fishing rod by someone else was enough to bear once.
```
