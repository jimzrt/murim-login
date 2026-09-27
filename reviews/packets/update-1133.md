<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1133.txt",
      "sha256": "8292477695e7f07f800592af1a9c8d5f39f4c5406f7221fed42ffe0f2f7eb9ba",
      "bytes": 12370
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "23fa22949f2eba99b259f610c373ba7b5f3b694245ad858368231fb7cc5d1ef7",
      "bytes": 730
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "54fe8adf3889eb517bdfb5dfd1b309608c9e69dcb5ab99853766ea1ba936d28e",
      "bytes": 245292
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "202322cb736fa8c7db33e793cc1cc160fcc9d25daf4414b496988ff25dd390a0",
      "bytes": 844
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "663af94fd884bc3a6a98f29908c874935eacbcc55f5111540a3cda69adcf16b9",
      "bytes": 760
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "6c45dba1f0318edf49d17a91664e3373e5eb6cdf6db85d2fd61fe2038776fabe",
      "bytes": 554
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "3396fca5e9151d08af23b5b14396223fc1686cc683fe0fac7bee4266ccebda03",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "5da0e6355e20f6caefb1596834d1821f5ef4423638066db0a3d9b4f08398ef7e",
      "bytes": 1929
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "b08d140d038b79061d641b575c94530531677483f924ff4dfaa37a707a0dee93",
      "bytes": 623
    },
    {
      "path": "characters/Ju Gongsan.md",
      "sha256": "8b8b801c10e23a3862fe3fe41871b5e978b1c4e8d819092557217445a7cb404a",
      "bytes": 900
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "6854605ecf6ae0e2183b66b0cc00c653a3fef00afacdff0296c1b433e94a022a",
      "bytes": 959
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "5e3302093fbfb04fead687e0692525b308607d9b73716a8f55f345cf5a12bfe0",
      "bytes": 1084
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "61532188d3a991ab36991c2170577e7b708fc70e8dd5c647227b212a6b82e0b2",
      "bytes": 290261
    }
  ],
  "estimated_tokens": 11554
}
-->

# Durable State Update — Chapter 1133

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
1 and safe_through 1133. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1133. Profile updates may replace only one
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
  "chapter": 1133,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1133,
    "continuity_sources": [1133],
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
    "The Helper is the unknown old man who taught Taekyung to circulate qi and can communicate within his mind.",
    "Taekyung perceived qi through the Mind’s Eye and received an unidentified gift from the Helper.",
    "The Helper remains in the enduring gray-white space by his own choice, waiting for an unknown end.",
    "Taekyung’s heart restarted; after undergoing Bone Transformation, he recovered and awoke."
  ],
  "continuity_sources": [
    1131,
    1132
  ],
  "open_questions": [
    "Who is the Helper beyond the name Taekyung recognizes, and what is his purpose?",
    "What did the Helper give Taekyung?"
  ],
  "safe_through": 1132,
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
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 중원     | **Central Plains**                               |                                                       |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 퀘스트              | **Quest**                      |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 도사      | **Daoist**                                                      |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 주공산 | **Ju Gongsan** | Former head and founder of the Yongbong Escort Bureau. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 요지부동 | **Unmoving** | Achievement earned after the waterfall training. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 진맥 | **take one's pulse** | Mungyeong's prior medical examination of Jeok. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 모산파 | **Maoshan Sect** | Jiangsu sect known for sorcery, destroyed by the founding emperor. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 미친놈 | **Madman** | Insult Great Sir adopts as a name; also appears in the System display. |
| 서녕 | **Xining** | Capital of Qinghai. |

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
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 천주 | 대술사 | master to servant | you | commanding and authoritative | Addresses her through mind-voice, ordering her to report, raise her head, and depart. |
| 대술사 | 천주 | servant to master | Lord of Heaven | extremely deferential | Uses reverent titles and self-abasing language while reporting and pleading. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 혈주 | 마삼보 | superior_to_subordinate | you; you fool | hostile and threatening | The Blood Lord berates Ma Sanbao after the surveillance is exposed. |
| 마삼보 | 혈주 | subordinate_to_superior | My Lord | deferential | Ma Sanbao reports to the Blood Lord and pleads for mercy. |
| 학의 | 진태경 | Kunlun Sect disciple to renowned martial artist | Great Hero Jin Taekyung | formal and deferential | Uses 진태경 대협 when introducing himself and greeting Taekyung. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |
| 적천강 | 혈주 | hostile_opponents | you | blunt and threatening | Jeok Cheongang blocks the Blood Lord’s final attack on Taekyung and rebukes him. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1130
- **Aliases:** None
- **Role:** Deceased young-seeming high-ranking Dark Heaven figure who claimed command of its army after killing the Grand Mage.
- **Personality:** Cunning and controlling, he trusts his overwhelming power and relishes opponents who survive and resist him; he resents the Lord of Heaven’s attention to Taekyung and rationalizes his intended murder as loyalty, yet believes his choice is right.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He served the Lord of Heaven, killed the Grand Mage, and died after Jin Taekyung defeated him; at death, he recognized that the Lord had never valued his loyalty.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1132
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1128
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1132
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1132
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; the Helper first taught Taekyung to circulate qi; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1132
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Gongsan.md

# Ju Gongsan (주공산)

- **Safe through:** Chapter 975
- **Aliases:** Escort King
- **Role:** Founder and former head of the Yongbong Escort Bureau; during the Great Faction War, he was a wandering escort who refused to surrender a pregnant woman of the Guangdong Chen Family to the Demonic Cult after accepting her escort fee, carried her from Guangdong through Jiangxi and Hubei to Henan over two years, and became known as the Escort King; he later founded an escort bureau in his hometown of Shaanxi and died from internal injuries sustained during the war.
- **Personality:** Remarkably skilled, chivalrous, principled, and unwavering in his obligations.
- **Voice:** Not established.
- **Relationships:** Ju Hogun was his only blood child and successor as head of the Yongbong Escort Bureau; Ju Hwaran is his granddaughter.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 1117
- **Aliases:** None
- **Role:** Ma Sanbao is a sorcerer and Supreme Peak martial artist, former disciple of the Eastern Heaven Demon Lord, and servant of the Lord of Heaven, whose power lets him raise the dead within limits and command beasts with ritual bells.
- **Personality:** He is ambitious and confident in his usefulness to the Lord of Heaven, dismissive of his former master’s weakness, and pragmatic about losing subordinates.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao served the Eastern Heaven Demon Lord as his disciple and now serves the Lord of Heaven; he regards Jin Taekyung as an adversary who will make a captured operative betray him.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1132
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

## Korean source

```text
＃1133화



한 사람의 입술 사이로 작지만 또렷한 목소리가 흘러나온 그 순간, 주위를 에워싼 무수한 사람들은 약속이라도 한 듯 동시에 눈을 부릅떴다.

이것을 뭐라 불러야 할까.

생존(生存)?

아니면, 부활(復活)?

그 의문에 대한 답은 누구도 몰랐다.

다만, 그들은 가슴 깊숙한 곳에서 울컥 솟구친 뜨거운 무언가를 느꼈다.

“……!”

“……!”

내성(內城)을 넘어, 천지를 뒤흔들 것만 같은 먹먹한 함성.

끝없이 쏟아져 내리던 빗줄기는 어느덧 그친지 오래였지만, 그들의 외침은 끊이지 않았다.

그 속에서 누군가는 울고, 누군가는 웃고, 누군가는 아직 전투가 끝나지 않은 것처럼 병장기를 높이 쳐든 채 힘찬 함성을 이어 갔다.

기진맥진한 와중에도 그들은 마음껏 기뻐했다.

끝나지 않을 것만 같던 이 처절한 혈투(血鬪)가 끝났다는 사실에.

더불어 한편으로는 형용할 수 없을 만큼 깊은 슬픔을 느꼈다.

불과 몇 시진 전까지만 하더라도 어깨를 나란히 하고, 등을 맞대며 싸우던 전우(戰友)의 빈자리를 보며.

마지막으로, 전율했다.

눈앞에서 펼쳐진 이 놀라운 이적(異蹟)의, 검푸른 광휘와 함께 깨어난 젊은 영웅의 모습에.

그리고 믿을 수 없다는 눈빛으로 자신의 제자를 바라보던 스승은, 잘게 떨리는 입술을 열어 이렇게 말했다.

“그래, 믿고 있었다.”

대답과는 달리 흠뻑 젖어 있는 눈가.

그런 적천강의 모습에 진태경은 말없이 희미한 웃음을 머금었다.

믿었든, 믿지 않았든 그것이 무슨 상관이랴.

중요한 것은 눈물에 담겨 있던 스승의 마음이었고, 자신은 그 약속을 지켰다는 것뿐이었다.

‘돌아왔구나, 정말로.’

이미 한계를 벗어난 정신의 피로 때문일까.

비록 의식은 수면 깊숙이 가라앉은 것처럼 흐릿했으나, 진태경은 자신을 둘러싼 모든 것이 결코 거짓이 아님을 알 수 있었다.

서서히 개어 가는 하늘도.

두 번 다시 보지 못하리라 생각했던, 지금 이 순간 자신의 주위를 에워싼 채 울고 웃는 익숙한 얼굴들도.

그리고.

허공에 떠 있는 무수한 홀로그램 창 가운데, 가장 크고 선명하게 시야에 들어온 글귀들도.



- [선천지기(先天眞氣)]가 회복되었습니다!

- 상태 이상, [회광반조(廻光返照)]가 해제되었습니다!

- 돌발 퀘스트, [바람 앞의 촛불, 혹은 불꽃]을 성공적으로 완료했습니다!



힘없이 사그라지는 촛불이 될 것이냐.

혹은 적을 집어삼키는 불꽃이 될 것이냐.

그 선택의 기로에서 진태경은 후자(後者)를 택했고, 그의 몸 안에서 꺼져가던 불씨는 마침내 되살아났다.

선천지기라는 이름의 불씨가.

그리고 잇따른 또 한 번의 환골탈태(換骨奪胎)는, 이 자리의 누구도 예상치 못한 기적이나 다름없었다.

검성(劍星)이라 불리는 희대의 거인조차도.

“자네, 생각보다 잠버릇이 요란하더군. 상상 이상이야.”

어느덧 곁으로 다가온 검성 매종학의 농담 섞인 한 마디에, 진태경은 피식 실소를 흘리며 대답했다.

“중간에 깰 뻔했습니다. 주위가 너무 시끄러워서.”

“지금도 그런가?”

“예.”

진태경은 계속해서 함성을 내지르고 있는 아군을 바라보며 덧붙였다.

“하지만…… 듣기 좋네요.”

듣기 좋다.

진태경이 내놓은 그 짧은 감상에, 말없이 그를 응시하던 매종학이 작게 고개를 끄덕였다.

“그래, 나 역시 그리 생각하네.”

전투의 결과는 묻지도, 대답하지 않아도 알 수 있었다.

전신이 포박당한 채 무릎 꿇려진 일부 광신도들과 달리, 사방을 에워싼 수많은 아군의 모습이 그것을 증명하고 있었으니까.

‘전투는, 끝났다.’

고작 몇 글자에 불과한 그 사실에, 진태경은 가슴 한구석에서 울컥 솟구치는 뜨거운 무언가를 느꼈다.

어쩌면 오늘 하루만의 승리일지도 모른다.

오늘날의 승리가, 언제가 될지 모를 내일의 패배로 지워질 수도 있다.

그러나…… 지금 당장은 그것으로 충분했다.

처절하고도 끔찍했던 이 지옥도(地獄道)가 끝났다는 것만으로도.

더불어 거대한 산처럼 앞을 가로막고 있던 암천(暗天)의 대군세와, 그들을 이끌던 강대한 적들을 쓰러트렸다는 사실만으로도.

‘혈주. 그리고 대술사.’

진태경은 고개를 들어 북동쪽을 바라보았다.

청해성 밖에 펼쳐진 저 광활한 사막 너머에 얼마나 더 많은 적이 도사리고 있을지는 모른다.

하지만 오늘 이 전장에서 최후를 맞이한 혈주와 대술사의 죽음은 아군에게 있어 크나큰 수확임이 분명했다.

완전히 단정 지을 수는 없더라도, 짐작하는 바에 따르면 그 두 사람은 천주(天主)에게 남은 마지막 사냥개들이었으니까.

‘그런데…… 지금 이 기분은 뭐지?’

진태경은 갑작스럽게 찾아온 기시감(旣視感)을 느끼며 눈꺼풀을 파르르 떨었다.

어째서일까.

무언가를 잊고 있는 듯한 기분이 들었다.

그것도 아주 중요한, 놓쳐서는 안 될 무언가를.

그러나 진태경이 그 기시감의 정체를 깨닫기까지는, 그리 오랜 시간이 필요하지 않았다.

쐐애애액!

다음 순간, 저 멀리 아득한 허공 위로 솟구쳐 오르는 십여 개의 그림자를 목격한 진태경이 눈을 부릅떴다.

‘저건……!’

그림자들의 정체는 다름 아닌 괴조(怪鳥)들이었다.

새하얀 뼈마디가 드러난 날개를 활짝 편 채, 핏빛 눈동자를 번뜩인 괴조들이 하늘을 가로질러 날아가고 있었다.

마치, 누군가에게 급보를 전하려는 전령처럼.

“안 돼!”

본능처럼 터져 나온 외침.

하지만 미처 손쓸 새도 없이, 이미 상당한 거리에서 솟구친 괴조들은 살아 있을 때와는 비교도 안 되는 빠른 속도로 서쪽을 향해 멀어졌다.

진태경의 머릿속을 벼락처럼 관통하는 한 사람의 이름을 남긴 채.

“……마삼보?”

잠시 잊고 있었다.

아니, 그에 대해 생각할 잠깐의 여유조차 없었다는 것이 더 옳은 표현일 것이다.

혈주와 대술사라는 두 괴물의 짙은 그림자에 가려져 보이지 않았던, 모산파의 명맥을 이은 강력한 강시술사의 존재를.

그리고 그와 동시에, 혈주가 최후를 맞이하기 직전 남겼던 마지막 한 마디가 환청처럼 진태경의 뇌리에 울려 퍼졌다.



‘마음껏 기뻐해라. 이 웃음이 마지막이 될 터이니.’



그 당시에는 몰랐다.

단지 전투에서 진 패장(敗將)의 구태의연한 허장성세라고 생각했던 저 말에 담긴 정확한 의미를.

그러나 지금 이 순간, 진태경의 등줄기를 타고 흘러내리는 서늘한 냉기는 또 다른 위기를 예고하고 있었다.

‘설마?’

머릿속에서 실타래처럼 뒤엉킨 정보들이 하나씩 풀어 헤쳐졌다.

비록 혈주와 대술사에 비견할 수는 없으나, 의심의 여지가 없는 강력한 전력임에도 끝끝내 전장에 나타나지 않은 마삼보.

아군에게마저 사실을 알리지 않은 채, 청해까지 수천 리 길을 떠나온 검성과 무림맹의 정예들.

덧붙여 이 모든 상황을 끝까지 지켜본 뒤 서쪽으로 날아간 한 무리의 괴조들까지.

‘잠깐, 서쪽이라면.’

틀림없다.

곤륜산(崑崙山).

이미 암천의 손아귀에 떨어진 그곳이 괴조들의 목적지일 것이다.

그리고 동시에, 진태경은 아직 풀리지 않았던 의문 중 하나를 떠올렸다.

그를 포함한 지원군이 청해성에 발을 내딛기 전부터 곤륜산을 점거하고 있던 암천의 대군세가, 어찌하여 그토록 요지부동이었는지.

더불어 이러한 혈주의 행보가, 단지 한 번의 그물질로 자신을 포함한 모든 대어(大漁)를 낚고자 했기 때문이었는지.

‘아니, 처음부터 혈주가 노린 건 그것만이 아니야. 다만…… 놈들에게도 시간이 필요했던 것뿐이다.’

이미 한계를 넘어선 정신적 피로 때문일까.

혹은 마침내 마주한 불길함의 실체 때문이었을까.

어느덧 백지장처럼 창백해진 안색으로 주위를 둘러싼 얼굴들을 바라보던 진태경은, 자신도 모르게 참고 있던 숨을 토해 냈다.

쓰디쓴 독처럼 혀끝에서 맴돌던, 두 글자도 함께.

“……이동진(移動陳).”

그것이 진태경이 찾아낸 답이었다.

그토록 강력한 전력을 갖춘 암천의 대군세가 곤륜산에 웅크리고 있던 가장 큰 이유 중 하나이자, 만약의 상황을 대비한 혈주의 마지막 한 수.

그리고 마삼보라는 복검(覆劍)은 이 소식을 듣는 즉시 움직일 것이다.

곤륜산 어딘가에 새롭게 각인된 이동진을 통해, 아군의 가장 치명적인 요혈(要血)을 관통할 것이 분명했다.

바로 중원(中原)이라 불리는 요혈을.

“당장, 지금 당장 움직여야 합니다. 이대로라면 중원이…….”

진태경은 파르르 떨리는 목소리로 신음했다.

숨이 턱 끝까지 차오르고, 심장이 두방망이질 친다.

어지럽게 흔들리는 시야 너머로 차례차례 스쳐 지나가는 얼굴들은, 어쩌면 오늘 이 자리에 나타나지 말았어야 했을지도 몰랐다.

지난 수십여 년간 검성(劍星)이라 불리었으나, 지금은 맹주(盟主)가 된 사내라면 더욱더.

하지만.

“그래, 움직여야겠지.”

진태경이 할 수 있는 것은 거기까지였다.

툭.

불현듯 목덜미로부터 전해지는 손길.

그와 동시에 벼락같은 속도로 진태경을 점혈(點穴)한 매종학이, 담담한 음성으로 말을 이었다.

“허나, 이번만큼은 쉬도록 하게.”

진태경은 대답했다.

아니, 대답하려 했다.

안 된다고. 절대 그럴 수는 없다고.

그러나 필사적인 의지와 달리 입술은 움직이지 않았고, 쏟아지는 피로와 졸음은 만근(萬斤)의 무게로 눈꺼풀을 짓눌렀다.

‘아.’

삽시간에 어두워지는 시야 속, 진태경은 환청처럼 귓가를 울리는 목소리와 함께 의식의 끈을 놓았다.

“고생했네, 친구.”



* * *



청해성은 실로 광활한 면적을 자랑한다.

하지만 죽음과 함께 무한한 활력을 얻은 괴조들의 날갯짓은, 수백 리도 넘게 떨어진 서녕과 곤륜산의 거리를 무색하게 만들기에 충분했다.

그리고 고금을 통틀어도 다시 없을 이 훌륭한 전령들이 가져온 충격적인 소식은, 불과 한 시진도 되지 않아 곤륜산의 가장 높은 봉우리에 닿았다.

아니.

모산파의 명맥을 이은 어느 강시술사에게.

“……그래, 그리되었단 말이지.”

혼잣말처럼 뇌까린 마삼보는 깊게 가라앉은 시선으로 동쪽 어딘가를 응시했다.

도무지 믿을 수 없는 소식이었으나, 믿지 않을 수 없었다.

이미 십여 마리의 괴조들이 보고 들은 모든 것을 생생하게 전달받았으니까.

한나절 동안 이어진 쉼 없이 대혈투의 결과와, 결코 청해성에 나타날 수 없으리라 생각했던 이들의 존재까지도.

‘혈주, 그자에게 사과해야겠군. 그저 피에 미친놈인 줄로만 알았는데.’

마삼보는 피식 실소를 흘렸다.

누구보다 진태경에게 집착했으면서도, 혈주는 마지막 한 수를 남겨둠으로써 제 목줄을 쥔 주인에 대한 최소한의 충의를 잊지 않았다.

무주공산(無主空山)이나 다름없는 중원을 초토화시킬, 최후의 일검을.

그리고 마삼보는, 기꺼이 그 역할을 수행할 생각이었다.

“이 지긋지긋한 산도 떠날 때가 되었군.”

태사의에서 일어난 마삼보가 대기하고 있던 수하들을 향해 덧붙였다.

“가자. 중원으로.”
```

## Final English reading copy

```markdown
# Chapter 1133

The moment a small but unmistakable voice slipped between someone’s lips, the countless people surrounding him all widened their eyes at once, as if they’d rehearsed it.

What should they call this?

Survival?

Or resurrection?

No one knew the answer.

All they knew was that something hot surged up from deep within their chests.

“……!”

“……!”

A muffled roar, powerful enough to shake heaven and earth, rose beyond the Inner City.

The rain that had poured down without end had stopped long ago, but their cries didn’t let up.

Some wept. Some laughed. Others raised their weapons high and roared as if the battle still raged.

Exhausted as they were, they rejoiced with all their hearts.

The brutal bloodbath that had seemed as if it would never end was over.

And yet, alongside their joy, they felt a grief too deep for words.

They looked at the empty places left by comrades who had stood shoulder to shoulder and fought back to back with them only a few hours ago.

Finally, they shuddered at the sight before their eyes: a young hero awakening amid a blue-black radiance, in a miracle beyond belief.

His Master watched his Disciple with an expression of disbelief, then parted his trembling lips and spoke.

“Yeah. I believed in you.”

His words said one thing, but his eyes were soaked with tears.

At the sight of Jeok Cheongang, Jin Taekyung said nothing, only managing a faint smile.

Whether his Master had believed in him or not—what did it matter?

What mattered was the feeling in his Master’s tears, and that he had kept his promise.

*I’m back. Really.*

Perhaps it was because his mind was exhausted beyond its limits.

His consciousness was hazy, as if sunk deep in sleep, but Jin Taekyung knew that everything around him was real.

The sky slowly clearing.

The familiar faces that surrounded him now, laughing and crying, though he’d thought he would never see them again.

And—

Among the countless holographic windows floating in the air, the words that stood out most clearly and prominently.

> **System**
>
> Innate qi has been restored!
>
> Status abnormality, Final Rally, has been lifted!
>
> The sudden Quest, A Candle in the Wind, or a Flame, has been successfully completed!

Would he become a candle, its flame dying helplessly away?

Or a blaze that devoured his enemies?

At that crossroads, Jin Taekyung had chosen the latter, and the dying ember inside him had finally been reignited.

The ember called innate qi.

And the second Bone Transformation that followed was nothing short of a miracle—one no one present could have expected.

Not even the peerless giant known as the Sword Saint.

“You make a lot of noise in your sleep. More than I ever imagined.”

At Mae Jonghak’s joking remark as he came over, Jin Taekyung let out a quiet snort of laughter.

“I almost woke up halfway through. It was so noisy around me.”

“Is it still noisy?”

“Yes.”

Jin Taekyung glanced at his allies, still shouting their lungs out, and added:

“But… it sounds good.”

It sounds good.

At Jin Taekyung’s brief comment, Mae Jonghak watched him in silence, then gave a small nod.

“Yes. I feel the same.”

No one needed to ask about the battle’s outcome, or explain it.

The proof was all around them: countless allies surrounding them, and a handful of fanatics on their knees, bound from head to toe.

*The battle is over.*

At those few words, something hot surged up from one corner of Jin Taekyung’s chest.

Perhaps this was only a victory for today.

Today’s victory might be erased by a defeat tomorrow, whenever that day came.

But… for now, this was enough.

Enough that this horrific hellscape had come to an end.

Enough that they had defeated the enormous Dark Heaven army that had stood in their way like a mountain, along with the powerful enemies who led it.

*The Blood Lord. And the Grand Mage.*

Jin Taekyung lifted his head and looked northeast.

He didn’t know how many more enemies were waiting beyond that vast desert outside Qinghai.

But the deaths of the Blood Lord and the Grand Mage on this battlefield were undoubtedly a major victory for the allies.

He couldn’t be certain, but as far as he could tell, those two had been the Lord of Heaven’s last hunting dogs.

*But… what is this feeling?*

A sudden sense of déjà vu made Jin Taekyung’s eyelids flutter.

Why?

He felt as if he’d forgotten something.

Something very important—something he couldn’t afford to overlook.

But it didn’t take him long to realize what that feeling was.

Whoooosh!

The next moment, Jin Taekyung’s eyes flew wide as he saw a dozen or so shadows shoot up into the distant sky.

*Those are…!*

They were none other than strange birds.

They flew across the sky with their wings spread wide, white bone joints exposed and blood-red eyes flashing.

Like messengers rushing to deliver urgent news to someone.

“No!”

The shout burst from him on instinct.

But before he could do anything, the birds, already far away, shot west at a speed far beyond anything they’d managed while alive.

Leaving behind one name that struck Jin Taekyung’s mind like a bolt of lightning.

“……Ma Sanbao?”

He’d forgotten about him for a moment.

No—that wasn’t quite right. He hadn’t had even a moment to think about him.

The powerful jiangshi sorcerer who carried on the Maoshan Sect’s legacy had been hidden from sight by the shadows of the two monsters, the Blood Lord and the Grand Mage.

And at the same time, the Blood Lord’s final words before he met his end rang through Jin Taekyung’s mind like an auditory hallucination.

*“Celebrate to your heart’s content. This will be your last laugh.”*

He hadn’t understood it then.

He’d thought those words were nothing more than the tired bluster of a defeated general.

But now, the cold running down Jin Taekyung’s spine foretold another crisis.

*Could it be?*

The tangled threads of information in his mind began to unravel one by one.

Ma Sanbao had never appeared on the battlefield, despite being an undeniably powerful force—if not a match for the Blood Lord and the Grand Mage.

The Sword Saint and the Murim Alliance’s elite had traveled thousands of *li* to Qinghai without even telling their own allies the truth.

And then there were the strange birds that had watched everything unfold before flying west.

*Wait. If they’re heading west…*

No doubt about it.

Mount Kunlun.

That place, already in Dark Heaven’s grasp, had to be the birds’ destination.

At the same time, Jin Taekyung recalled one of the questions he still hadn’t answered.

Why had Dark Heaven’s enormous army, which had occupied Mount Kunlun before he and the reinforcements even set foot in Qinghai, remained so immovable?

And had the Blood Lord really made all these moves just to catch him and every other big fish in a single sweep of the net?

*No. That wasn’t all the Blood Lord was after from the start. It was just… they needed time, too.*

Perhaps because his mind was already exhausted beyond its limits.

Or perhaps because he’d finally grasped the shape of the foreboding he’d felt.

His face had turned as pale as paper as he looked around at the people surrounding him. Without realizing it, Jin Taekyung let out the breath he’d been holding.

Along with two bitter words that lingered on the tip of his tongue.

“……Moving Formation.”

That was the answer Jin Taekyung had found.

It was one of the main reasons Dark Heaven’s powerful army had hunkered down on Mount Kunlun—and the Blood Lord’s last move, prepared in case things went wrong.

And Ma Sanbao, the hidden blade, would move as soon as he heard this news.

Through the Moving Formation newly inscribed somewhere on Mount Kunlun, he would pierce the allies’ most vital point.

The very place called the Central Plains.

“We have to move. Right now. If we don’t, the Central Plains—”

Jin Taekyung’s voice trembled as he groaned.

His breath caught in his throat, his heart pounded hard.

Beyond his vision, swaying wildly, he saw the faces around him one after another. Perhaps they shouldn’t have come here today at all.

Especially the man who had been known as the Sword Saint for decades, and was now the Alliance Leader.

But—

“Yeah. We have to move.”

That was as far as Jin Taekyung could go.

Tap.

A hand suddenly touched the back of his neck.

In the same instant, Mae Jonghak struck a Pressure-Point Strike with lightning speed. In an even voice, he continued:

“But this time, you’re going to rest.”

Jin Taekyung answered.

Or tried to.

No. Absolutely not. He couldn’t rest now.

But despite his desperate resolve, his lips wouldn’t move, and exhaustion and sleep washed over him, pressing down on his eyelids with the weight of ten thousand *geun*.

*Ah.*

As his vision went dark in an instant, Jin Taekyung let go of consciousness, a voice ringing in his ears like an auditory hallucination.

“You’ve done well, my friend.”

* * *

Qinghai is vast.

But the wings of the strange birds, granted boundless vigor by death, were swift enough to make the distance between Xining and Mount Kunlun—more than several hundred *li*—seem insignificant.

And the shocking news brought by these exceptional messengers, unlike any seen in the past or present, reached Mount Kunlun’s highest peak in less than a *shichen*.

No—

It reached a certain jiangshi sorcerer who carried on the Maoshan Sect’s legacy.

“……So that’s what happened.”

Ma Sanbao muttered to himself as he stared east, his gaze sinking deep.

The news was impossible to believe, but he had no choice.

More than a dozen strange birds had already relayed everything they’d seen and heard in vivid detail.

The result of a bloody battle that had continued without a break for half a day—and the presence of people who, he’d thought, could never appear in Qinghai.

*I owe the Blood Lord an apology. I thought he was just a man crazed by blood.*

Ma Sanbao let out a quiet snort of laughter.

More than anyone, the Blood Lord had obsessed over Jin Taekyung. Yet by keeping one last move in reserve, he hadn’t forgotten his most basic loyalty to the master who held his leash.

A final sword stroke that would lay waste to the Central Plains, now all but undefended.

And Ma Sanbao was willing to play that part.

“It’s about time I left this wretched mountain.”

Ma Sanbao rose from the grand chair and addressed his waiting subordinates.

“Let’s go. To the Central Plains.”
```
