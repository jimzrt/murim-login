<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1134.txt",
      "sha256": "30d74d67e46d00e449a0861c64a86d97bd43fe84a7fdb1f824c0ea5d64ebf064",
      "bytes": 14061
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9a87f17225f5233f8860a9537c71e42a736bfd4e3a2602201403e5a85436a1b7",
      "bytes": 946
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "54fe8adf3889eb517bdfb5dfd1b309608c9e69dcb5ab99853766ea1ba936d28e",
      "bytes": 245292
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "929ebad03960013b82e6080735c766d07cf4ac80150e343abb7d1d0c1a34b4e7",
      "bytes": 950
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "c073a1b394e61d0baacdb901249f548961ab770344560a8a0da6b1e6918935c9",
      "bytes": 844
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "8c06a75859583a89dfae0028dcb1f1cc6180bf20f0b029bb3fdd6d9d0e8b0aa6",
      "bytes": 760
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "0726c7fcfd63b7adbe739b71c9707c9488f569e52790362df899712d2308de86",
      "bytes": 554
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "cd44749258b7b497a49bd09d78cd8dc673f002567b8432d89917633480fda5d6",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "308f28c8c55f2bd57a03a6c7975f540cb2cb4a76cf3f9f5883df3f8705813492",
      "bytes": 1929
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "05838f4d616a2c630c936bf06e9e669031ba7d6f41a283e2820d0f75ee9eeef7",
      "bytes": 623
    },
    {
      "path": "characters/Ju Gongsan.md",
      "sha256": "5e12305e42a4a589850fb576c5043d3a83b56b70a41aaf9c463869f142d7dc8b",
      "bytes": 901
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "64d62585df48fd702d3aa0a997ea8cb433c00a612ea7821ca08bf841dfc25939",
      "bytes": 959
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "4e691bd45e69c8370d620497a60810804d09b65ace205a1a5aeb7b12ae6a262f",
      "bytes": 1084
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "0d1a59cc7890c25fd803e63fb600d65cb5cf6ea8d01b4ee15891d386ccb28baf",
      "bytes": 650
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "61532188d3a991ab36991c2170577e7b708fc70e8dd5c647227b212a6b82e0b2",
      "bytes": 290261
    }
  ],
  "estimated_tokens": 13744
}
-->

# Durable State Update — Chapter 1134

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
1 and safe_through 1134. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1134. Profile updates may replace only one
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
  "chapter": 1134,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1134,
    "continuity_sources": [1134],
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
    "Taekyung recovered and awakened after another Bone Transformation; Mae Jonghak used a Pressure-Point Strike to make him rest.",
    "The Blood Lord and Grand Mage died in the battle at Qinghai; the allied forces won.",
    "Ma Sanbao remained at Mount Kunlun and intends to use a Moving Formation to attack the Central Plains; he has departed with his subordinates.",
    "The Helper is the unknown old man who taught Taekyung to circulate qi and can communicate within his mind.",
    "Taekyung received an unidentified gift from the Helper; the Helper chose to remain in the enduring gray-white space, waiting for an unknown end."
  ],
  "continuity_sources": [
    1132,
    1133
  ],
  "open_questions": [
    "What did the Helper give Taekyung?",
    "Will Ma Sanbao’s attack through the Moving Formation reach the Central Plains?"
  ],
  "safe_through": 1133,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 곤륜파    | **Kunlun Sect**                  |
| 무림맹    | **Murim Alliance**               |
| 제갈세가   | **Zhuge Clan**                   |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 사숙     | **Martial Uncle**                            |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 주공산 | **Ju Gongsan** | Former head and founder of the Yongbong Escort Bureau. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 간장 | **Gan Jiang** | Legendary swordsmith named in comparison with Mo Ye. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 산군 | **mountain lord** | Traditional epithet for a tiger; retain an explanatory footnote on first use. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 와룡객 | **Crouching Dragon Guest** | Epithet of Zhuge Feng. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |
| 마조 | **Demon Bird** | Title given by the revealed impostor who wore Chinggen’s face. |
| 십만마도 | **Hundred Thousand Demonic Disciples** | The earlier force used as a comparison for Dark Heaven’s army. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 태청전 | **Taiqing Hall** | Hall in Kunlun where the Blood Lord and Grand Mage meet. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 매종학 | 혈주 | legendary_martial_master_to_enemy | you | cold and judgmental | After revealing himself, Mae Jonghak condemns the Blood Lord's accumulated sins and orders him to pay the price. |
| 혈주 | 매종학 | enemy_to_revealed_legendary_master | you | shocked and hostile | The Blood Lord addresses Mae Jonghak with 당신 immediately after recognizing him as the Sword Saint. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 적천강 | 제갈풍 | senior_martial_artist_to_old_acquaintance | you / ill-mannered brat | blunt, familiar, and teasing | Jeok treats Zhuge Feng as the younger acquaintance he remembers from childhood. |
| 제갈풍 | 적천강 | younger_old_acquaintance_to_legendary_senior | Senior | respectful but relaxed | Zhuge Feng recalls Jeok's earlier visit and addresses him as an old senior. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 가솔 | 진태경 | Zhuge Clan retainer to Great Hero | Great Hero Jin | polite and pleading | Uses 진 대협 while urging Taekyung to stop provoking Ju Wongong. |
| 진태경 | 제갈풍 | younger martial artist to senior clan head | Sir Zhuge | blunt and challenging | Uses 제갈 대협 while disputing Zhuge Feng's attempted ten-percent claim. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 매종학 | 제갈풍 | Alliance Leader to Zhuge Clan Family Head | Family Head Zhuge | formal and familiar | Mae Jonghak asks whether Zhuge Feng completed his assignment. |
| 천주 | 대술사 | master to servant | you | commanding and authoritative | Addresses her through mind-voice, ordering her to report, raise her head, and depart. |
| 대술사 | 천주 | servant to master | Lord of Heaven | extremely deferential | Uses reverent titles and self-abasing language while reporting and pleading. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 혈주 | 마삼보 | superior_to_subordinate | you; you fool | hostile and threatening | The Blood Lord berates Ma Sanbao after the surveillance is exposed. |
| 마삼보 | 혈주 | subordinate_to_superior | My Lord | deferential | Ma Sanbao reports to the Blood Lord and pleads for mercy. |
| 학의 | 진태경 | Kunlun Sect disciple to renowned martial artist | Great Hero Jin Taekyung | formal and deferential | Uses 진태경 대협 when introducing himself and greeting Taekyung. |
| 제갈풍 | 맹주 | Zhuge Clan Family Head to Murim Alliance Leader | Alliance Leader | polite | Zhuge Feng addresses the concealed Alliance Leader in the Zhuge Clan garden. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |
| 적천강 | 혈주 | hostile_opponents | you | blunt and threatening | Jeok Cheongang blocks the Blood Lord’s final attack on Taekyung and rebukes him. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 941
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a martial arts instructor to the Emperor, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, Baek Yeon prioritizes the Great Nation and its people over Murim’s interests, and is willing to dismantle Murim if it becomes a threat to them.
- **Voice:** Baek Yeon speaks with measured formality in public, but with the Emperor he shifts easily into familiar teasing and earnest, eloquent praise.
- **Relationships:** Baek Yeon is the Emperor’s trusted confidant and former martial arts instructor, and he is entrusted with protecting Zhu Bao; he commands the Embroidered Uniform Guard and treats Taekyung as a dangerous potential obstacle.

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1133
- **Aliases:** None
- **Role:** Deceased young-seeming high-ranking Dark Heaven figure who claimed command of its army after killing the Grand Mage.
- **Personality:** Cunning and controlling, he trusts his overwhelming power and relishes opponents who survive and resist him; he resents the Lord of Heaven’s attention to Taekyung and rationalizes his intended murder as loyalty, yet believes his choice is right.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He served the Lord of Heaven, killed the Grand Mage, and died after Jin Taekyung defeated him; at death, he recognized that the Lord had never valued his loyalty.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1133
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1133
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1133
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1133
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; the Helper first taught Taekyung to circulate qi; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1133
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Gongsan.md

# Ju Gongsan (주공산)

- **Safe through:** Chapter 1133
- **Aliases:** Escort King
- **Role:** Founder and former head of the Yongbong Escort Bureau; during the Great Faction War, he was a wandering escort who refused to surrender a pregnant woman of the Guangdong Chen Family to the Demonic Cult after accepting her escort fee, carried her from Guangdong through Jiangxi and Hubei to Henan over two years, and became known as the Escort King; he later founded an escort bureau in his hometown of Shaanxi and died from internal injuries sustained during the war.
- **Personality:** Remarkably skilled, chivalrous, principled, and unwavering in his obligations.
- **Voice:** Not established.
- **Relationships:** Ju Hogun was his only blood child and successor as head of the Yongbong Escort Bureau; Ju Hwaran is his granddaughter.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 1133
- **Aliases:** None
- **Role:** Ma Sanbao is a sorcerer and Supreme Peak martial artist, former disciple of the Eastern Heaven Demon Lord, and servant of the Lord of Heaven, whose power lets him raise the dead within limits and command beasts with ritual bells.
- **Personality:** He is ambitious and confident in his usefulness to the Lord of Heaven, dismissive of his former master’s weakness, and pragmatic about losing subordinates.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao served the Eastern Heaven Demon Lord as his disciple and now serves the Lord of Heaven; he regards Jin Taekyung as an adversary who will make a captured operative betray him.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1133
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 1088
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃1134화



곤륜산의 공기는 그날따라 무거우면서도 서늘했다.

높이 솟은 봉우리들을 타고 흐르는 안개는 유독 짙었고, 사방에 펼쳐진 아름다운 자연 속에서 인간과 함께 공존하던 크고 작은 생물체들의 흔적은 사라진 지 오래였다.

다만, 짙은 안개 속에서도 붉게 빛나는 안광과 섬뜩한 괴성(怪聲)만이 있을 뿐.

- 크르르.

싯누런 이빨 사이로 흘러나오는 흉포한 울음소리.

불과 한 달 전까지만 하더라도 곤륜산을 호령했던 산군(山君)은, 살아 있을 적보다도 거대해진 몸뚱어리를 굽혀 자신의 주인을 맞이했다.

어느덧 곤륜파의 상징과 같은 태청전(太淸殿)을 빈틈없이 둘러싸고 있던, 수천의 인마(人魔)와 함께.

“명령하신 대로 모두 집결시켰습니다.”

칠흑 같은 장포로 전신을 휘감은 일백여 명의 무리.

그중 앞으로 나선 흑의인의 보고에, 마삼보는 열기 띤 음성으로 물었다.

“전부 몇이냐.”

“약 오천, 그중 삼천은 마물(魔物)입니다.”

마삼보의 입꼬리가 부드럽게 올라갔다.

“곤륜산의 영물이 씨가 말랐겠군.”

만약 무림의 사정에 밝은 누군가가 이들의 목적과 대화를 들었다면, 허무맹랑한 소리라며 코웃음을 쳤을지도 몰랐다.

오천의 병력은 결코 적은 숫자가 아니지만, 그 옛날 천하를 새카맣게 뒤덮었던 마교의 십만마도(十萬魔徒)조차 중원 무림을 손에 넣지 못했으니까.

하지만 마삼보의 입가에 맺힌 미소에는 그만한 이유가 있었다.

‘충분하다. 아니, 그 이상이야.’

마삼보는 깊게 가라앉은 눈동자로 온 사방을 빼곡히 메운 수하들을 쓸어보았다.

쉼 없이 번뜩이는 마물들의 핏빛 눈동자와, 오직 명령에 따라 움직이는 실혼인(失魂人)이나 다름없는 광신도들.

지금 이 순간, 만반의 준비를 끝마친 채 마삼보의 명령만을 기다리고 있는 저들은 실로 마군(魔軍)이라 불릴 만한 존재들이었다.

이제는 과거의 망령이 되어 버린, 한낱 마교도 따위와는 비교하는 것이 실례일 만큼.

그리고 이와 같은 마삼보의 확신에 가장 큰 비중을 차지하는 것은, 눈앞의 흑의인을 포함한 일백여 명의 강시술사(僵尸術士)였다.

비록 자신에 비할 수는 없으나, 시체만 있다면 각각 일군을 이끌 수 있는 진정한 괴물들.

그런 그들을 흡족한 눈빛으로 바라보던 마삼보가 입을 열었다.

“군을 두 개로 나누어 이동할 것이다.”

“송구합니다만, 계획이 변경된 것입니까?”

흑의인의 조심스러운 물음에, 마삼보가 고개를 끄덕였다.

기존의 계획대로라면 그들은 일곱 갈래로 나뉘어 천하 곳곳에 혼란을 일으켰겠지만, 이제는 상황이 달라졌다.

다름 아닌 검성(劍星) 매종학이 무려 일만에 달하는 무림맹의 정예를 이끌고 청해성에 나타났으니.

‘설마 맹주라는 자가 직접 지원군을 이끌고 올 줄이야.’

혹시 모를 이런 상황을 위해 남아 있던 마삼보였지만, 그럼에도 매종학의 등장은 녹림맹과 장강수로맹의 배신만큼이나 놀라운 것이었다.

하지만 맹주인 매종학이 무림맹을 비웠다는 건, 하남에도 최소한의 방비를 해 놓았다는 뜻.

‘물론 주력이 빠진 이상 턱없이 부족한 전력이겠지만…… 만일의 상황을 대비해서라도 우리 역시 과한 분산은 피하는 것이 상책이다.’

마삼보는 신중했다.

실로 어렵게 잡은, 어쩌면 천운(天運)이라 할 수도 있는 절호의 기회다.

강시술사들의 능력을 생각한다면 과한 우려일 수도 있겠으나, 그는 조금이라도 더 안전하면서도 확실한 방법을 택하고자 했다.

마삼보가 원하는 바는 천주의 지배 아래 재정립될 천하에서 일인지하(一人之下) 만인지상(萬人之上)의 지위를 누리는 것이었지, 혈주처럼 비참한 최후를 맞이하는 것이 아니었으니까.

그리고 이러한 심사숙고한 끝에 마삼보가 결정한 표적은, 마침내 단 두 곳으로 좁혀져 있었다.

“하남(下南)과 산서(山西).”

짧은 침묵을 깨트리는 상관의 음성에, 흑의인이 깊게 고개를 숙였다.

“존명(尊命). 실로 옳으신 결정입니다.”

태원진가가 자리를 비운 이상 현재의 산서성은 무주공산(無主空山)이나 다름없고, 하남은 천하 무림에서 차지하는 상징성과 지리적 이점을 위해서라도 반드시 차지해야 하는 곳이었다.

아니, 매종학이 없는 지금이야말로 하남을 손쉽게 점령할 수 있는 최고의 적기였다.

더군다나 하남과 산서는 서로 경계가 맞닿아 있는 위치.

만일의 상황이 벌어지더라도 언제든 지원할 수 있다는 것이 가장 큰 장점 중 하나가 될 것이다.

“이천의 병력과 술사 절반을 내어준다면, 칠주야(七晝夜) 안에 산서성을 손에 넣을 수 있겠느냐?”

태원진가가 산서성을 일통한 이래, 하루가 다르게 나날이 발전을 거듭해온 산서성이다.

그러나 이와 같은 상관의 요구에, 흑의인은 생각할 필요도 없다는 듯이 입을 열었다.

‘고작’ 이천에 불과한 병력은, ‘무려’ 수십여 명의 술사들에 의해 끝없이 증식할 테니까.

“나흘이면 족합니다.”

“하북(河北)까지 포함한다면?”

“열흘을 주시옵소서. 하면 십만의 대군을 이끌고 돌아오겠습니다.”

흑의인의 막힘없는 대답에, 마삼보의 미소가 더욱 짙어졌다.

“그 약속, 기억하마.”

바로 그 순간.

스아아아아.

희미한 빛이 지면을 타고 올올이 피어오르기 시작했다.

대술사가 곤륜산에 머무를 당시 설치해 두었던 이동진. 아니 마법진(魔法陳)이 마삼보와 함께 남아 있던 몇몇 술사들에 의해 발동되기 시작한 것이다.

우우우우웅.

시시각각 크기를 더해 가는 빛과 함께, 모두를 감싸 안으며 퍼져 나가는 두 개의 거대한 원.

사방에서 들끓어 오르는 그 신비로운 기파(氣波)를 느끼며, 마삼보는 솟구치는 희열에 몸을 떨었다.

‘단숨에, 모든 것을 끝낼 것이다. 이 두 손으로 직접.’

마삼보를 아는 이라면 누구도 부정할 수 없는, 충분한 근거가 있는 자신감이었다.

그는 모산파의 명맥을 이은 가장 강력한 강시술사이자, 한 명의 무인으로서도 능히 십왕(十王)과 어깨를 나란히 하는 초절정 고수였으니까.

삼성(三星)도, 진태경과 적천강도 없는 작금의 중원 무림은 마삼보에게 있어 조금의 두려움도 심어 주지 못했다.

‘검성, 최소한 당신만큼은 자리를 비우지 말았어야 했소.’

무슨 방비를 해 놓았건, 이 정도의 전력이라면 단숨에 중원의 허리를 끊어 낼 수 있었다.

자신들의 출현을 알리는 급보가 저들에게 알려졌을 때는, 이미 수천이 아닌 수만의 대군세가 완성되어 있을 테니까.

끊임없이 죽이고 또 죽여도, 다시금 채워지는 불사(不死)의 군단이.

‘바로 오늘, 천하의 역사가 뒤바뀐다.’

또한 세상은 영원히 기억하게 될 것이다.

능히 천년 간 이어질 이 장대한 역사의 첫걸음에, 마삼보 자신이 있었음을.

화아아악!

시야를 새하얗게 물들이는 휘황한 섬광 속, 마삼보는 웃으며 눈을 감았다.

저 멀리 아득한 어딘가로 자신의 영육(靈肉)을 끌어당기는 신비의 힘에 몸을 맡긴 채.

앞으로 이어질 자신의 한 걸음, 한 걸음과 함께 천하에 새겨질 거대한 족적을 떠올리며.

파앗.

변화는 한순간이었다.

다음 순간, 확연히 달라진 주위의 공기와 바람을 느낀 마삼보는 본능적으로 깨달았다.

대술사가 준비해 두었던 마법진이, 자신을 비롯한 삼천여 명의 수하들을 약속한 곳으로 이동시켜 주었다는 것을.

‘드디어, 시작이다.’

위대한 첫걸음을 내디딘 자에게만 허락된 전율과 함께, 마삼보는 감았던 눈을 떴다.

아니, 정확히는 뜨려고 했다.

퍼걱, 촤아악!

불현듯 울려 퍼진 섬뜩한 파육음과 동시에, 뜨거우면서도 끈적한 무언가가 그의 얼굴을 뒤덮기 전까지는.

“……!”

콧속 깊이 스며드는, 지긋지긋하리만치 익숙한 혈향(血香).

마치 온 세상이 멈춘 듯한 감각 속에서, 마삼보는 어느덧 파르르 떨리고 있는 눈꺼풀을 힘겹게 들어 올렸다.

그리고 두 눈으로 똑똑히 볼 수 있었다.

자신이 미처 깨닫지 못했던, 또 하나의 사실을.

쿵, 철퍽!

달빛조차 찾지 않는 어느 이름 모를 심산유곡(深山幽谷)에서, 단말마조차 남기지 못한 채 짚단처럼 허물어지는 크고 작은 그림자들.

마삼보는 막을 수도, 움직일 수도 없었다.

아니 그와 함께 살아남은 이들 역시 마찬가지였다.

그들이 할 수 있는 일이라곤, 그저 멍하니 바라보는 것뿐이었다.

하남에서의 첫발을 떼기도 전에 쓰러진, 무려 이천에 달하는 아군들의 죽음을.

창칼이 아닌 바위나 나무 따위와 한 몸이 된 채, 실로 괴이한 형태로 숨이 끊어진 그들의 끔찍한 최후를.

“이게, 이게 도대체 무슨.”

바로 그때였다.

무언가에 홀린 듯, 넋 나간 목소리로 뇌까리던 마삼보의 귓가로 생각지도 못한 대답이 들려온 것은.

“무슨 일이긴, 보고 있는 그대로지.”

짙은 어둠 너머에서 울려 퍼지는 담담한 음성.

목소리의 주인을 쫓아 벼락처럼 고개를 돌린 마삼보는 눈을 부릅떴다.

도대체 언제부터 그곳에 있던 것일까.

수십여 장 밖, 담장처럼 주위를 둘러싼 언덕 위에서 모습을 드러낸 어느 중년인이 공포와 혼란에 휩싸인 분지(盆地)를 굽어보고 있었다.

아니, 마삼보를.

“만나서 반갑네. 이건 진심이야. 혹여 안 오면 어쩌나 하는 마음에 애간장이 탈 정도였거든.”

마치 석상처럼 딱딱하게 굳어 버린 마삼보와, 살아남은 그의 수하들을 천천히 훑어본 중년인이 입맛을 다시며 덧붙였다.

“물론 살짝 아쉬운 감이 없지 않아 있긴 한데…… 그래도 이 정도면 환영 인사는 충분한 것 같군. 안 그런가?”

마삼보는 대답하지 않았다.

보다 정확히는, 대답할 수 없었다.

지금 당장은 새하얗게 물든 뇌리를 가득 채운 두 글자를 이해하는 것만으로도 벅찼으니까.

‘함정……!’

그래, 이건 함정이었다.

그것도 아주 치밀하게 준비한.

그리고 언덕 위에서 빙긋 웃고 있는 저 청수한 인상의 중년인은, 과거 대술사가 아무도 찾지 않는 하남의 심산유곡 깊숙이 새겨넣은 이동 마법진에 덫을 설치한 장본인이 틀림없었다.

가장 간단하면서도 확실한, 동시에 끔찍한 덫을 놓은 사냥꾼.

“그렇게 흉흉한 눈빛으로 보지 말게. 되려 아쉬운 건 이쪽이야. 이동진(移動陳)의 정확한 범위를 알아낼 수만 있었다면, 단숨에 끝장낼 수도 있었을 텐데.”

짐짓 한숨마저 내쉬는 중년인의 모습에, 마삼보는 피가 거꾸로 솟구치는 듯한 분노를 느끼며 입을 열었다.

“그러지 못한 것을 후회하게 될 것이다. 네놈은 물론, 네 가솔(家率)들까지 전부 갈기갈기 찢어 죽일 테니.”

중년인은 아직 신분을 밝히지 않았지만, 마삼보는 이미 그의 정체를 알고 있었다.

동창에 몸담고 있던 시절 보았던 용모파기(容貌疤記)와 중년인의 손에 들린 저 새하얀 부채는 한 사람을 떠올리기에 충분했으니까.

“와룡객(臥龍客) 제갈풍.”

확신이 담긴 마삼보의 한 마디에, 제갈세가의 현 가주인 제갈풍이 눈을 크게 떴다.

“오, 날 알고 있나?”

“그래. 기억하고 있었지. 오늘 이후로는 머릿속에서 잊히겠지만.”

건조한 음성으로 대답한 마삼보는 몸 안의 기운을 끌어올렸다.

비록 생각지도 못한 함정에 태반이 넘는 수하들을 잃었으나, 가장 중요한 전력인 강시술사들의 피해는 크지 않다.

전투가 시작되면 시체가 늘어나는 것은 당연지사.

제갈풍이 어떤 대비를 해 놓았건, 해가 떴을 때 이곳에서 살아 나가는 것은 자신이 되리라고 마삼보는 확신했다.

적어도 다음 순간, 제갈풍의 등 뒤로 모습을 드러낸 낯익은 얼굴을 보기 전까지는.

“그렇다면 나도 기억하고 있겠군. 안 그런가? 마 태감(太監).”

마삼보는 일순간 가슴 한구석이 서늘해지는 것을 느꼈다.

어찌 잊을 수 있을까.

수십여 년간 봐 왔던 저 얼굴을.

그 어떤 위태로운 상황에서도 황실을 지켜 온, 노장(老將)의 웅혼한 음성을.

그러나 마삼보를 격동케 만든 것은, 황실 제일의 고수인 금의위 지휘사(錦衣衛指揮使) 백연의 존재뿐만이 아니었다.

황실의 수호하는 검이자 방패인 그가 이곳에 나타났다는 것은, 또 다른 사실을 의미했으므로.

사박.

거구의 노장에게 가려져 있던, 호리호리한 인영이 앞으로 나섰다.

그리고 고귀한 혈통을 타고난 자만이 보일 수 있는 오연한 시선으로, 자신의 옛 신하를 굽어보았다.

아니, 감히 황실을 뒤엎으려 한 천고의 죄인을.

“그래, 역적(逆賊)질은 할만 하던가.”

천자(天子)의 물음에, 마삼보는 신음했다.
```

## Final English reading copy

```markdown
# Chapter 1134

The air on Mount Kunlun felt heavy and cold that day.

The mist flowing over its towering peaks was unusually thick, and it had been a long time since any sign remained of the large and small creatures that once lived alongside humans amid the beautiful landscape stretching in every direction.

Only blood-red eyes glimmered through the dense mist, accompanied by eerie cries.

“Grrr.”

A vicious growl spilled between yellowed teeth.

The mountain lord[^1] who had ruled Mount Kunlun only a month ago bent his body, now larger than it had been in life, to greet his master.

Along with thousands of human demons who now surrounded Taiqing Hall—the very symbol of the Kunlun Sect—without leaving a single gap.

“Everyone has gathered, as you commanded.”

The report came from one of the hundred or so men wrapped head to toe in jet-black robes. Ma Sanbao’s voice grew eager.

“How many in all?”

“About five thousand. Three thousand of them are monsters.”

The corners of Ma Sanbao’s mouth lifted in a gentle smile.

“Then Mount Kunlun’s spiritual creatures must be nearly extinct.”

Anyone familiar with the state of Murim who heard their purpose and conversation might have scoffed at such an absurd claim.

Five thousand troops was no small force. But even the Hundred Thousand Demonic Disciples, who had once blanketed the world in darkness, had failed to bring the Central Plains under their control.

But there was good reason for the smile on Ma Sanbao’s face.

*It’s enough. More than enough.*

Ma Sanbao swept his sunken gaze over the subordinates packed in all around him.

The monsters’ blood-red eyes flashed without pause. The fanatics moved only at his command, little more than soulless puppets.

Now that they had completed their preparations and waited only for his orders, they truly deserved to be called a Demon Army.

Comparing them with the mere Demonic Cult of the past, now only a ghost of history, would be an insult to them.

And the greatest source of Ma Sanbao’s confidence was the hundred or so corpse sorcerers standing before him, including the man in black.

They might not measure up to Ma Sanbao himself, but each was a true monster capable of leading an army, as long as there were corpses to work with.

Ma Sanbao regarded them with satisfaction, then spoke.

“We’ll split the army in two and move out.”

“Forgive me, but has the plan changed?”

At the black-clad man’s cautious question, Ma Sanbao nodded.

Under the original plan, they would have split into seven groups and stirred up chaos across the land. But circumstances had changed.

Sword Saint Mae Jonghak had appeared in Qinghai, leading no less than ten thousand elite troops from the Murim Alliance.

*Who would’ve thought the Alliance Leader himself would bring reinforcements?*

Ma Sanbao had stayed behind in case of a situation like this. Even so, Mae Jonghak’s arrival was as surprising as the Green Forest Alliance and the Yangtze River Channel League betraying them.

But the fact that Alliance Leader Mae Jonghak had left the Murim Alliance meant he must have left at least a minimal defense in Henan.

*Of course, with its main force gone, it’ll be nowhere near enough. Still, to prepare for any eventuality, we’d be wise not to spread ourselves too thin.*

Ma Sanbao was cautious.

This was an opportunity he had fought hard to seize—perhaps one granted by Heaven itself.

The corpse sorcerers’ abilities might make such caution excessive, but he wanted to choose the safest and surest method possible.

Ma Sanbao wanted to enjoy a position second only to one and above ten thousand in a world reshaped under the Lord of Heaven’s rule—not meet a miserable end like the Blood Lord.

After carefully weighing the matter, he had finally narrowed his targets down to just two places.

“Henan and Shanxi.”

At his superior’s voice, which broke the brief silence, the black-clad man bowed deeply.

“Understood. A most excellent decision.”

With the Jin Family of Taiyuan gone, Shanxi Province was all but an ownerless mountain. Henan, meanwhile, had to be taken for its symbolic importance and strategic location in Murim.

In fact, with Mae Jonghak absent, this was the perfect opportunity to seize Henan with ease.

And Henan and Shanxi shared a border. One of the greatest advantages was that they could support each other at any time, should anything go wrong.

“If I give you two thousand troops and half the sorcerers, can you take Shanxi Province within seven days and nights?”

Ever since the Jin Family of Taiyuan united Shanxi Province, it had continued to grow stronger by the day.

But the black-clad man answered without so much as a pause.

The mere two thousand troops would multiply endlessly, thanks to the several dozen sorcerers he would have at his disposal.

“Four days will suffice.”

“And if I include Hebei?”

“Give me ten days. I’ll return leading an army of a hundred thousand.”

The black-clad man’s prompt answer deepened Ma Sanbao’s smile.

“I’ll remember that promise.”

At that very moment—

Sssaaaa.

Faint light began to rise in strands from the ground.

The Moving Formation the Grand Mage had set up during her stay on Mount Kunlun—no, the Magic Formation—began to activate, stirred into motion by the few sorcerers who had remained behind with Ma Sanbao.

Vroooom.

Two enormous circles spread outward, growing larger by the second and enveloping everyone in light.

Feeling the mysterious energy surge from every direction, Ma Sanbao trembled with rising elation.

*I’ll end it all in one stroke. With my own two hands.*

His confidence was more than justified. No one who knew Ma Sanbao could deny it.

He was the most powerful corpse sorcerer to carry on the Maoshan Sect’s legacy, and even as a martial artist, he was a Supreme Peak master who could stand shoulder to shoulder with the Ten Kings.

With the Three Saints, Jin Taekyung, and Jeok Cheongang all absent, the current Murim of the Central Plains held not the slightest fear for him.

*Sword Saint, if nothing else, you shouldn’t have left.*

No matter what defenses they had prepared, with this much power, he could cut through the heart of the Central Plains in an instant.

By the time word of their arrival reached the enemy, their force would number not thousands but tens of thousands.

An immortal army that would replenish itself no matter how many times it was killed.

*Today, the course of history will change.*

And the world would remember forever that Ma Sanbao himself had been there at the first step of this grand history, destined to last a thousand years.

Fwoosh!

As a brilliant flash of light washed his vision white, Ma Sanbao smiled and closed his eyes.

He let himself be carried by the mysterious force pulling his spirit and flesh toward some distant place.

He imagined the great strides he would take, one after another, and the mighty trail they would carve across the world.

Paht.

The change happened in an instant.

In the next moment, Ma Sanbao felt the air and wind around him had changed completely. Instinctively, he realized that the Magic Formation prepared by the Grand Mage had transported him and some three thousand of his subordinates to their promised destination.

*At last, it begins.*

With the thrill reserved for the one taking the first great step, Ma Sanbao opened his eyes.

Or, more precisely, he tried to.

Crunch—splat!

A gruesome sound of flesh being torn rang out, and something hot and sticky covered his face before he could open them.

“……!”

The scent of blood seeped deep into his nostrils, sickeningly familiar.

As though the whole world had stopped, Ma Sanbao struggled to lift his trembling eyelids.

And then he saw it clearly with his own two eyes.

The other thing he hadn’t realized.

Thump. Splatter.

In some nameless, remote mountain valley where even the moonlight didn’t reach, large and small figures crumpled like bundles of straw without so much as a dying cry.

Ma Sanbao couldn’t stop it. He couldn’t move.

Neither could the few who had survived alongside him.

All they could do was stare, dumbfounded.

At the deaths of fully two thousand of their comrades, felled before they could take their first step in Henan.

They had died in horrific, bizarre shapes, their bodies fused not with blades or spears, but with rocks and trees.

“What—what in the world is this?”

Just then, an unexpected answer reached Ma Sanbao’s ears as he muttered in a dazed voice, as if under a spell.

“What does it look like? It’s exactly what you’re seeing.”

A calm voice rang out from beyond the thick darkness.

Ma Sanbao whipped his head toward it like lightning and stared.

How long had he been there?

Several dozen *jang* away, an unfamiliar middle-aged man stood on a hill that walled in the area, looking down at the basin—now gripped by fear and confusion.

No. He was looking at Ma Sanbao.

“Good to meet you. I mean that. I was so worried you might not show up that I was beside myself.”

The middle-aged man slowly looked over Ma Sanbao, frozen stiff as a statue, and the subordinates who had survived. He smacked his lips, then added:

“Of course, I can’t say I’m not a little disappointed…but this should be enough of a welcome, don’t you think?”

Ma Sanbao didn’t answer.

More accurately, he couldn’t.

For now, he could barely process the word filling his blank mind.

*A trap…!*

Yes, it was a trap.

One laid with extraordinary care.

And the refined-looking middle-aged man smiling on the hill was unmistakably the one who had laid a trap in the Moving Formation the Grand Mage had carved deep into a remote valley in Henan that no one ever visited.

A hunter who’d set the simplest, surest—and most horrific—trap of all.

“Don’t look at me with such murderous eyes. I’m the one who should be disappointed. If I’d only figured out the exact range of the Moving Formation, I could’ve finished it in one stroke.”

At the middle-aged man’s feigned sigh, Ma Sanbao felt his blood boil with fury.

“You’ll regret failing to do so. I’ll tear you and every last one of your family to pieces.”

The middle-aged man hadn’t yet revealed his identity, but Ma Sanbao already knew who he was.

The portrait he’d seen during his time in the East Depot, and the pure-white fan in the middle-aged man’s hand, were enough to bring one man to mind.

“Crouching Dragon Guest, Zhuge Feng.”

At Ma Sanbao’s confident declaration, Zhuge Feng, the current Family Head of the Zhuge Clan, raised his eyebrows.

“Oh? You know me?”

“I do. I remembered you. After today, though, I’ll forget you.”

Ma Sanbao answered in a dry voice and drew up the energy inside his body.

Though he had lost more than half his subordinates to an unexpected ambush, the most important force—the corpse sorcerers—had suffered little damage.

As soon as the battle began, the number of corpses would naturally increase.

Whatever Zhuge Feng had prepared, Ma Sanbao was certain that he would be the one to leave this place alive at sunrise.

At least, he was—until he saw a familiar face appear behind Zhuge Feng.

“Then I suppose you remember me, too. Don’t you, Eunuch Ma?”

Ma Sanbao felt a chill in his chest for an instant.

How could he forget?

He had seen that face for decades.

He knew the resonant voice of the veteran general who had protected the imperial household through every peril.

But it wasn’t only Baek Yeon, the greatest master in the imperial household, who had shaken Ma Sanbao.

The presence of the man who was the imperial household’s sword and shield meant something else, too.

Scuff.

A slender figure stepped out from behind the burly veteran.

He looked down at his former servant with the haughty gaze only someone born to noble blood could possess.

No—at the criminal for the ages who had dared to overthrow the imperial household.

“So, how did you like being a traitor?”

At the Son of Heaven’s question, Ma Sanbao groaned.

[^1]: *San-gun*, literally “mountain lord,” is a traditional epithet for a tiger.
```
