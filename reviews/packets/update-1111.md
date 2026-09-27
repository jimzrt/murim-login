<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1111.txt",
      "sha256": "49dc5ce1869d6b76ee24462476fef3c935408ef8b790c00e44bc493daa951cd8",
      "bytes": 12898
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "502dad0627e1be72813ea9fe4a8c019efbfb9942cd8cfe771e370d6823f6a371",
      "bytes": 1059
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bf6c4f7b66402118726cc38b45f04e6573af5660df71d2d9f176747ba040720c",
      "bytes": 244327
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "ac2ecb884688325f963ea037cc2e07bb349fad1d7386804cac24297b6e6e311a",
      "bytes": 915
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "f20fb85cebc0970a97c29bbe40b483f8e9b7a9d360d6f3e38dcf39feac9fec1e",
      "bytes": 1230
    },
    {
      "path": "characters/Dalai Lama.md",
      "sha256": "55bab9584b9be515ccd559272db9a7992f1bcbfd5d7cbc63ea107e525b0cd1b3",
      "bytes": 748
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "3f2821a23f80b66ee36b2d21e921d3cbd1759079ad8dc1c4f2d989fafb863826",
      "bytes": 760
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "ab6c9cdee9265cdfac82cffcfb2ed755fa9f0e80b9037df72734f4db20c1668c",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "cf5ea5cb040a57d4f4a3270839b77e687d4d3b3372a028b82e56c49a25674db5",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "32645577dc70d5470310c44de7693818409c588dfacc82df9dab5ffb55d56517",
      "bytes": 623
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "fd8e6ae36f78d8f8cea7fddfd815c859fe57588e8681e07937da495c311304f3",
      "bytes": 779
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "3587b35f9f46255635c2b9217320b6613dd49879b3cf950be82def2526ffc095",
      "bytes": 288328
    }
  ],
  "estimated_tokens": 11444
}
-->

# Durable State Update — Chapter 1111

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
1 and safe_through 1111. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1111. Profile updates may replace only one
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
  "chapter": 1111,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1111,
    "continuity_sources": [1111],
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
    "The Blood Lord has regained his strength and memories and continues fighting at Xining.",
    "Jeong Hogun and roughly three hundred surviving Embroidered Uniform Guards charged the Blood Lord and were engulfed by a blood-red flash.",
    "Jin Taekyung has regained consciousness; Cheongpung reports that the West Gate is in trouble."
  ],
  "continuity_sources": [
    1109,
    1110
  ],
  "open_questions": [
    "What is Jin Taekyung’s condition after regaining consciousness, and who was the voice in his mind?",
    "What is the state of the West Gate?",
    "What happened to Jeong Hogun and the guards after the blood-red flash engulfed them?",
    "What are the flying beasts and the being at their center?",
    "Why does the Lord of Heaven want Taekyung, and what does he intend to do with him?"
  ],
  "safe_through": 1110,
  "temporary_decisions": [
    "Render 西藏 as “Xizang” for the Murim region; retain “Tibet” when Taekyung identifies it from his modern-world perspective."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 달뢰라마 | **Dalai Lama** | Traditional title of the Potala Palace’s leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 소평 | **So Pyeong** | Alliance office worker assigned to prepare a report. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 서문 | **West Gate** | One of the Nanman Beast Palace's gates. |
| 북문 | **North Gate** | The gate where Jin Taekyung and Yohi arrive. |
| 남문 | **South Gate** | A gate that was never built because of the rear cliff. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대술사 | **Grand Mage** | Title of the veiled woman leading the white-robed mages. |
| 십이밀승 | **Twelve Secret Monks** | The Potala Palace’s twelve top fighters. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 혈주 | 대술사 | fellow servant of the same person | you; you bitch | insulting-casual | Blood Lord taunts the Grand Mage and uses a crude insult. |
| 대술사 | 혈주 | fellow servant of the same person | you | contemptuous-casual | The Grand Mage addresses the Blood Lord while rebuking him. |
| 혈주 | 달뢰라마 | allied leader to allied leader | Palace Lord | familiar, then threatening and insulting | Calls him 궁주, then warns him not to speak down to him. |
| 달뢰라마 | 혈주 | allied leader to allied leader | donor; you | formal, then angry and informal | Initially uses the Buddhist honorific 시주 before challenging the Blood Lord. |
| 진태경 | 혈주 | hostile_opponent_to_hostile_opponent | you; you son of a bitch | insulting-casual | Taekyung insults the Blood Lord while challenging his claim that he will kill him. |
| 달뢰라마 | 적천강 | hostile leader confronting a rival martial master | donor | formal and controlled | Addresses Jeok as 시주 while blocking his departure for the West Gate. |

## Listed compact profiles

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1110
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure and formidable combatant who commands weapons telekinetically and absorbs blood to restore vitality.
- **Personality:** Cunning and controlling, he plans around opponents’ strengths and learns from past mistakes; his confidence in his overwhelming power is genuine rather than bluster, and he remains devoted to the Lord of Heaven despite resenting being treated as disposable and Taekyung’s apparent favor.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven and suspects the Lord wants Jin Taekyung above all else; he recognizes Cheongpung and remembers a debt to Sword Saint Mae Jonghak.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1110
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Dalai Lama.md

# Dalai Lama (달뢰라마)

- **Safe through:** Chapter 1105
- **Aliases:** Palace Lord
- **Role:** The Dalai Lama is the Potala Palace’s leader and ruler of Xizang, commanding its Twelve Secret Monks.
- **Personality:** Fiercely hostile to the Fire Gate Clan and committed to the Potala Palace’s interests; he trusts the Lord of Heaven but distrusts the Blood Lord.
- **Voice:** Uses Buddhist self-reference and addresses others as “donor”; his Han speech is described as halting.
- **Relationships:** He leads the Potala Palace in an unequal alliance with Dark Heaven and commits its forces to ending the Fire Gate Clan, pursuing the Palace’s longstanding grievance.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1109
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1106
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1109
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1109
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 1099
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

## Korean source

```text
＃1111화



둥, 둥, 두두둥!

전투 중에 전고(戰鼓)가 울려 퍼지는 것은 결코 이상한 일이 아니다.

가장 높은 망루에 설치된 전고는 사면의 성벽 전체를 감시하는 또 하나의 지휘소나 다름없었으니까.

그러나 어느 때보다 다급하고 위태롭게 터져 나온 그 울림에는, 듣는 이의 심장을 옥죄이게 만드는 무언가가 있었다.

서걱!

성벽 아래를 벼락처럼 가로지르는 한 줄기의 섬광.

그와 동시에 검기를 흩뿌리며 들이닥치던 수십여 명의 광신도들이 조각조각 나뉘어 흩어졌지만, 정작 이와 같은 신위(神威)를 선보인 장본인의 표정은 딱딱하게 굳어 있었다.

“이건…….”

흐려지는 말꼬리와 함께, 성벽 바로 밑에서 적들을 상대하던 살성(殺星)은 반사적으로 고개를 돌려 바라보았다.

전고의 진원지인 내성이 아니라, 저 멀리 먹먹한 함성이 들려오는 서쪽을.

정확한 이유는 그 자신조차 몰랐다.

다만 숱한 경험을 통해 벼려진 본능과 촌각 전 서쪽으로부터 들끓었던 거대한 힘의 파동이 살성의 모든 감각을 자극하고 있을 뿐이었다.

찰나의 순간, 허공을 뒤덮으며 내리꽂히는 섬광들의 존재조차 잠시 뒷전으로 미룰 만큼.

쐐애애애액!

공간을 얼리며 쏟아져 내리는 무수한 얼음송곳.

하지만 자신을 향한 시린 한기(寒氣)를 느꼈음에도, 살성은 서쪽에 고정된 시선을 거두지 않았다.

그의 등 뒤에는, 실로 믿음직한 누군가의 존재가 있었으니까.

슈확!

성벽 위가 환해졌다고 느낌과 동시에, 한 사람의 손끝을 떠난 빛줄기가 수백여 개에 달하는 얼음송곳들을 집어삼켰다.

콰아아아아!

아득한 섬광과 함께 터져 나오는 굉음.

그리고 사방을 뒤흔든 그 격돌의 여파가 완전히 사라지기도 전, 궁성(弓星)의 선명한 전음이 살성의 귓가를 파고들었다.

- 서문(西門)이 함락당했어요.

“……!”

살성은 입술을 비집고 흘러나오려는 침음성을 삼켰다.

설마 했던 불길한 예감이 현실이 되고야 말았지만, 그렇기에 더욱더 탄식할 여유 따위는 없었다.

그나마 간신히 유지해 오던 이 균형의 한 축이 완전히 무너진 이상, 모든 것이 위태로워졌으니까.



- 그렇다면 서문을 지키던 아군은…….

- 현재까지 확인된 사상자만 오 할 이상. 그나마도 금의위가 결사 항전한 덕분에 조금이나마 시간을 벌었다더군요.



오 할.

그 어마어마한 수치에 살성이 입술을 깨문 것은 너무나도 당연한 일이었다.

서문에 배치되어 있던 수비군은 대략 일만 이상.

한데 그중 무려 절반이 증발했다고 한다. 그것도 본격적인 전투가 시작된 지 불과 한 식경 만에.



- 살아남은 자들은 어찌 되었소?

- 일부는 내성(內城)으로 퇴각. 일부는 아직까지 후미에서 적들을 막아 내고 있는 듯해요.

- 그렇다면 혹시.



문득 뇌리를 스쳐 지나간 불길한 짐작에 살성이 입을 다문 그때, 궁성의 나직한 전음이 이어졌다.



- 청풍과 진태경. 두 아이는 내성으로 물러났고요.

- ……운이 좋았군.



살성은 흘러나올 뻔한 안도의 한숨을 애써 억눌렀다.

이미 수많은 희생을 치른 지금, 단지 연이 닿아 있다는 이유만으로 두 사람의 생존에만 집중하는 모습을 보이는 건 결코 옳은 태도가 아니었으니까.

하지만 궁성이 전달받은 정보는, 단지 그것으로 끝이 아니었다.



- 그 두 녀석이 살아 있다면 아직 충분한 기회가 있소. 녀석들이 내성을 수비하는 동안 우리가 최대한 반격…….

- 그조차도 쉽지 않을 거예요. 지금 같은 상태라면.

- 그게…… 무슨 뜻이오?

- 진태경. 그 아이가 크게 다쳤다고 하더군요. 청풍 역시 결코 온전한 상태가 아니고.

- ……!



일순간, 살성의 눈이 크게 뜨였다.

그리고 자신도 모르게 움직임을 멈춘 그의 어깨 위로, 눈먼 칼날이 휘둘려졌다.

서걱!

빠르고 강한 일격.

마지막 순간 몸을 비틀었음에도, 아슬아슬하게 스쳐 지나간 칼날에 실린 검기는 살갗을 가르기에 충분했다.

물론, 그 놀라운 행운의 소유자마저도 죽음을 피할 수는 없었지만.

푹!

살성의 손끝을 떠난 소도(小刀)가 적의 미간을 파고들고, 그와 동시에 유령처럼 흐릿해진 신형이 성벽을 타고 솟구쳐 올랐다.

쉭, 서걱!

눈 깜짝할 사이에 성벽 위에 우뚝 선 살성이, 쇠사슬과 사다리 등을 걸쳐 기어오르던 적들을 베어 넘기며 입술을 달싹였다.

- 어느 정도인 거요?

살성과 마찬가지로, 쉴 새 없이 적들을 향해 강기의 화살을 쏘아 보내던 궁성이 대꾸했다.



- 생사를 장담할 수 없을 만큼. 이라 하더군요.

- ……혈주(血主), 우리가 그놈을 과소평가했군.



살성의 입술 사이로 낮게 깔린 침음성이 흘러나왔다.

그 역시 처음부터 서문을 진태경에게 맡기는 것이 썩 내키지 않았다. 다만, 적천강 때와 같은 논리로 설득당했을 뿐.



- 역시 녀석을 그곳에 남겨 두는 것이 아니었소.

- 변하는 것은 없었을 거예요. 혈주의 의중이 변하지 않는 한은.

- 내성으로 가야겠소. 그때까지 이곳을 지켜 주시오.



더 이상 지체할 시간이 없었다. 

진태경의 목숨이 경각에 달했다면, 그를 죽음에서 끌어올릴 수 있는 유일한 사람은 바로 자신뿐이었으니까.

그렇기에 살성은 무거운 마음으로 발걸음을 돌렸다.

아니, 돌리려 했다.

바로 그 순간, 귓가를 파고드는 선명한 목소리를 듣기 전까지는.

“과연 그게 최선일까요?”

“……그게 무슨.”

“살성, 당신마저 없으면 더는 이곳을 지킬 수 없어요. 나 혼자서는 결코.

살성은 불현듯 말문이 막혔다.

물론 그 역시 알고 있었다. 그들이 지키고 있는 이곳, 남문(南門)이 얼마나 위험한 상태인지.

대술사를 제외하고서라도 무려 넷이나 되는 흑귀들.

게다가 이를 뒷받침하는 술사들은 지금도 여러 마법으로 성벽을 노리는 한편, 광신도들에게 더욱 강한 힘과 속도를 부여하고 있었다.

애당초 동문(東門)을 수비하기로 되어있던 살성이 불과 일각만에 남문으로 합류할 수밖에 없었던 이유 역시 그 때문이 아니었던가.

그러나…….

“그렇다면 녀석을, 진태경을 이대로 죽게 놔두란 말이오?”

믿을 수 없다는 듯한 눈빛으로 자신을 바라보는 살성을 향해, 궁성은 그 어느 때보다 깊게 가라앉은 목소리로 입을 열었다.

“어쩔 수 없겠죠. 그것이 그에게 주어진 운명(殞命)이라면.”

“당신……!”

“그 아이에게는 신의(神醫)가 필요하죠. 알아요. 하지만 지금 우리 모두에게 필요한 건 살성(殺星)이에요.”

“……!”

“그래서, 무엇이 최선이죠?”

살성의 눈꺼풀이 파르르 떨렸다.

송곳처럼 가슴 한구석을 찌르는 궁성의 마지막 물음에 담긴 답을, 그 누구보다 잘 알고 있었으니까.

그리고 한편으로는, 눈앞의 저 여인이 너무나도 낯설었으니까.

‘어째서?’

오랫동안 자취를 감추었던 궁성이 나타난 이유에 대해서는 이미 들어서 알고 있었다.

그녀가 무신(武神)이 남긴 서신을 따라, ‘선택받은 자’라 칭해지는 이를 찾아 긴 세월을 헤매었다는 사실 역시도.

그렇기에 지금 이 순간 궁성이 보이는 언행이 더욱더 이해가 되지 않았다.

그녀가 선택받은 자, 아니 진태경을 구하려 하지 않는 이유를.

단지 그가 반드시 살아나리라는 믿음이 아닌, 지금으로서는 도무지 짐작조차 할 수 없는 저 뜻 모를 눈빛과 목소리가 무엇을 의미하는 것인지도.

‘궁성, 당신은 도대체…… 무엇을 숨기고 있는 거요?’

하지만 혀끝에 맴도는 그 물음과 머릿속 의문을, 살성은 힘주어 억누를 수밖에 없었다.

이와 같은 찰나의 고민조차 허락하지 않겠다는 듯, 적들의 공세는 더욱더 강해지고 있었으니까.

화아아악.

돌연 하늘을 붉게 물들이고, 바람과 빗물마저 지워내는 거대한 화염의 구.

실로 엄청난 위력을 간직한 채 쏘아진 그것을 향해, 살성은 망설임 없이 성벽을 박차고 솟구쳐 올랐다.

슈확!

손끝이 그리는 궤적을 따라 허공을 가로지르는 한 줄기의 빛. 그리고 이어지는 균열과 폭발.

콰아아아아앙!

수백 개의 조각으로 나뉜 불덩어리가 사방으로 비산함과 동시에, 본래의 위치로 착지한 살성이 심유한 눈빛으로 궁성을 응시했다.

“이것으로 충분한 대답이 되었소?”

조금 전과는 달라진 그의 눈빛을 읽어서일까, 일순간 궁성의 입가에 쓴웃음이 스쳤다.

“물론이에요.”

그런 그녀의 모습을 뒤로한 채, 살성은 말없이 고개를 돌려 성 밖을 새카맣게 물들인 적들을 응시했다.

정확히는, 지금까지와는 차원이 다른 위력이 담긴 마법을 선보인 누군가를.

‘대술사.’

마침내 전면에 나선 또 다른 수괴(首魁)의 얼굴이 살성의 망막에 틀어박힌다.

마치 호위병처럼 그녀를 지키고 있는 네 마리의 흑귀도 함께.

그리고 그 순간.

구구구구궁.

땅속 깊숙한 곳에서 울려 퍼지는 오싹한 울림을 느끼며, 살성은 문득 고개를 돌려 한 방향을 응시했다.

세상 그 누구보다도 진태경을 아끼고, 그를 위해서라면 물불 가리지 않고 달려들 유일한 사람을 떠올리며.

‘이제 자네밖에 없군. 부탁하네, 화왕(火王).’

살성이 마음속으로 나지막이 뇌까린 그때.

드드드드득!

남문을 중심으로, 반경 일백여 장에 달하는 지면이 그 무겁고도 거대한 육신을 일으켰다.

전장을 가로지르며 선명하게 울려 퍼지는, 한 사람의 목소리와 함께.

- 뒤흔들어라.

어스 퀘이크(Earthquake).

콰아아아아!



* * *



구구구궁!

찰나의 순간, 남쪽으로부터 시작되어 사방으로 번진 그 맹렬한 울림을 느낀 사람들의 반응은 가지각색이었다.

“지, 지진이다!”

인간의 힘으로는 막을 수 없는 재앙(災殃)을 떠올린 누군가는 공포에 질렸고.

“흔들리지 마라! 더 이상 무엇이 두렵단 말이냐!”

이미 죽음을 각오한 누군가는 한 치의 물러섬 없이 적들과 맞서 싸웠으며.

“빌어먹을 년. 벌써 눈치챈 건 아니겠지.”

익숙한 힘을 느낀 누군가는, 감히 내성으로 향하는 자신의 앞길을 가로막은 부나방들을 향해 핏빛 섬광을 쏘아 보냈다.

불편한 훼방을 받기 전에 한 시라도 더 빨리, 확실하게 한 사람의 목숨을 취하기 위해서.

그러나 그 누군가는, 아니 혈주는 몰랐다.

그로부터 수백여 장 밖의 북문(北門)에서, 자신의 예상을 아득히 뛰어넘는 또 다른 학살극이 벌어지고 있다는 사실을.

“마, 마구니…….”

쿨럭.

내장 조각이 섞인 핏물이 입술 사이로 흘러나온다. 

샛노란 가사(袈裟)는 어느덧 피에 흠뻑 젖어 본래의 색을 찾아볼 수 없었고, 새카맣게 타들어 간 시체는 온 사방에 널브러져 있었다.

그렇게 참혹한 죽음을 맞이한 이들의 숫자가 몇이나 되는지, 그들 중 누구도 몰랐다.

심지어, 이 한 편의 지옥도를 완성한 장본인조차도.

다만, 한 가지만큼은 잘 알고 있었다.

콰드득.

지금 이 순간, 자신의 손아귀에 목이 꺾여 쓰러진 중년의 승려가 서장 제일이라 불리는 십이밀승(十二密僧)의 마지막 생존자라는 것과.

“이제, 네놈 하나만 남았구나.”

석상처럼 굳어 있는 저 늙은 승려가, 이제 그의 앞을 가로막은 유일한 걸림돌이라는 것을.

“……!”

부릅뜬 두 눈. 파르르 떨리는 눈동자.

끔찍한 광경을 목도하고 석상처럼 굳어 버린 달뢰라마를 향해, 화왕(火王) 적천강은 지친 발걸음을 옮겼다.

지금쯤 위기에 처했을 제자를 떠올리며.

자신의 각오를 되새기며.

“빨리 끝내자. 녀석이 기다린다.”

화륵.

피로에 젖어 있던 동공 위로, 새하얀 불길이 번지고 있었다.
```

## Final English reading copy

```markdown
# Chapter 1111

Boom, boom, ba-boom!

There was nothing strange about war drums sounding in the middle of a battle.

The drum installed on the highest watchtower was practically another command post, keeping watch over the entire perimeter of the walls.

But this beat rang out more urgently and perilously than ever before. Something about it made the hearts of those who heard it tighten.

*Slice!*

A streak of light shot across the foot of the wall like a bolt of lightning.

Dozens of fanatics charging in while scattering Sword Energy were cut to pieces and sent flying. Yet the man responsible for this display of divine might wore a rigid expression.

“This is……”

His words trailed off. The Slaughter Saint, who had been fighting enemies right beneath the wall, turned his head on instinct and looked—not toward the Inner City, where the war drums had sounded, but far away, toward the west, where a muffled roar reached them.

Even he didn’t know exactly why.

All he knew was that his instincts, honed by countless experiences, and the immense surge of power that had boiled over from the west moments ago were stirring every one of his senses.

For an instant, they mattered enough to push even the streaks of light plunging down from above out of his mind.

*Shreeeeeeek!*

Countless ice spikes rained down, freezing the air around them.

The Slaughter Saint felt the icy chill aimed at him, but he didn’t take his eyes off the west.

Someone utterly dependable stood behind him.

*Whoosh!*

The wall lit up. A beam of light shot from someone’s fingertips and swallowed hundreds of ice spikes whole.

*KABOOOOOM!*

A thunderous crash burst out alongside a blinding flash.

Before the shockwaves of the collision had fully faded, the Bow Saint’s clear Sound Transmission rang in the Slaughter Saint’s ears.

—The West Gate has fallen.

“……!”

The Slaughter Saint swallowed the groan rising to his lips.

The ominous premonition he’d feared had come true. But that left him even less time to lament. With one of the pillars holding their already fragile balance now completely broken, everything was in danger.

—Then what happened to the allies defending the West Gate……

—More than half are casualties, according to the numbers confirmed so far. They say the Embroidered Uniform Guards bought us at least a little time by fighting to the death.

Half.

It was no wonder the Slaughter Saint bit his lip at that staggering number.

The West Gate’s garrison had numbered more than ten thousand.

And half of them had vanished—in barely half an hour after the battle began in earnest.

—What happened to those who survived?

—Some retreated to the Inner City. Others seem to still be holding off the enemy from the rear.

—Then, could it be—

A grim suspicion suddenly crossed his mind. The Slaughter Saint fell silent, and the Bow Saint’s low Sound Transmission continued.

—Cheongpung and Jin Taekyung. The two of them retreated to the Inner City.

—……They were lucky.

The Slaughter Saint suppressed the sigh of relief that nearly escaped him.

After so many had already been lost, it wouldn’t be right to focus only on the survival of those two just because he had ties to them.

But that wasn’t all the information the Bow Saint had received.

—If those two are alive, we still have a chance. While they defend the Inner City, we can counterattack as much as—

—That won’t be easy, not in their current condition.

—What…… do you mean?

—I heard Jin Taekyung was badly injured. Cheongpung isn’t in good shape, either.

—……!

The Slaughter Saint’s eyes widened.

And as he unconsciously froze, a stray blade swung at his shoulder.

*Slice!*

A swift, powerful strike.

He twisted at the last moment, but the Sword Energy trailing the blade still grazed him, slicing his skin.

Of course, even the man lucky enough to land that remarkable hit couldn’t escape death.

*Thud!*

The dagger that left the Slaughter Saint’s fingertips pierced the enemy between the brows. At the same time, his figure blurred like a ghost and shot up along the wall.

*Whoosh, slice!*

In the blink of an eye, the Slaughter Saint stood atop the wall, cutting down enemies climbing up ladders and chains as his lips moved.

—How bad is it?

The Bow Saint, like the Slaughter Saint, was firing arrows of Force at the enemies without pause. She answered him.

—I was told he might not survive.

—……Blood Lord. We underestimated that bastard.

A low groan slipped between the Slaughter Saint’s lips.

He hadn’t been comfortable leaving the West Gate to Jin Taekyung from the start. He’d only been persuaded by the same argument they had used with Jeok Cheongang.

—We shouldn’t have left him there after all.

—Nothing would have changed, not as long as the Blood Lord’s intentions remained the same.

—I have to go to the Inner City. Hold this place until I get there.

There was no more time to waste.

If Jin Taekyung’s life was hanging by a thread, he was the only one who could pull him back from death.

With a heavy heart, the Slaughter Saint turned to leave.

Or tried to.

Until a clear voice reached his ears.

“Are you sure that’s the best choice?”

“……What do you mean?”

“Without you, the Slaughter Saint, we won’t be able to hold this place any longer. Not on my own.”

The Slaughter Saint was suddenly at a loss for words.

Of course he knew how dangerous their position was here, at the South Gate.

Even without the Grand Mage, there were four Black Ghosts.

And the sorcerers backing them were still targeting the wall with various spells while granting the fanatics even greater strength and speed.

Wasn’t that why the Slaughter Saint, who had originally been assigned to defend the East Gate, had been forced to join them at the South Gate after only fifteen minutes?

But……

“Are you saying we should just let him—Jin Taekyung—die?”

The Bow Saint met the Slaughter Saint’s disbelieving gaze and spoke in a voice more somber than ever.

“We have no choice. If that’s the death he was destined for.”

“You……!”

“That boy needs the Divine Physician. I know. But what all of us need right now is the Slaughter Saint.”

“……!”

“So, what’s the best choice?”

The Slaughter Saint’s eyelids trembled.

He knew better than anyone the answer contained in the Bow Saint’s final question, which pierced his heart like a needle.

And, in another way, he found the woman before him utterly unfamiliar.

*Why?*

He already knew why the Bow Saint, who had disappeared for so long, had returned.

He’d also heard that she had followed the Martial God’s letter, searching for the one called the “chosen one” through the long years.

That only made her words and actions now harder to understand.

Why wasn’t she trying to save the chosen one—or rather, Jin Taekyung?

Her strange look and voice suggested something beyond simple faith that he would survive—something he couldn’t begin to fathom right now.

*Bow Saint, what exactly are you hiding?*

But he had no choice but to force down the question on the tip of his tongue and the doubts in his mind.

The enemy’s assault was growing stronger, as if it wouldn’t allow even this moment’s hesitation.

*Fwoooosh.*

A massive sphere of flame suddenly turned the sky red, wiping away even the wind and rain.

The Slaughter Saint leaped from the wall without hesitation to meet it, the enormous power hurtling toward them.

*Whoosh!*

A streak of light cut through the air along the path traced by his fingertips. A rift opened, followed by an explosion.

*KABOOOOOM!*

The ball of fire shattered into hundreds of pieces and scattered in every direction. The Slaughter Saint landed where he had started and fixed a profound gaze on the Bow Saint.

“Is that answer enough?”

Perhaps she had read the change in his eyes. A bitter smile briefly crossed the Bow Saint’s lips.

“Of course.”

Leaving her behind, the Slaughter Saint silently turned to face the enemies, who had dyed the land outside the wall pitch-black.

More precisely, he looked toward the one who had just displayed magic of a power beyond anything they’d seen so far.

*The Grand Mage.*

The face of another ringleader, who had finally stepped forward, burned itself onto the Slaughter Saint’s eyes.

Four Black Ghosts guarded her like bodyguards.

And then—

*Rumble……*

Feeling a chilling tremor rumble deep beneath the earth, the Slaughter Saint turned his head and looked in one direction.

He thought of the one person in the world who cherished Jin Taekyung more than anyone and would rush headlong into danger for his sake.

*You’re the only one left now. I’m counting on you, Fire King.*

Just as the Slaughter Saint murmured those words in his heart—

*Rrrrrumble!*

Centered on the South Gate, the ground within a radius of over a hundred jang heaved its massive, heavy body upward.

And a man’s voice rang clearly across the battlefield.

—Shake the earth.

Earthquake.

*KABOOOOOM!*

* * *

*Rumble!*

The people who felt the violent tremor begin in the south and spread in every direction reacted in all sorts of ways.

“An earthquake!”

Some, reminded of a disaster no human power could stop, were overcome with fear.

“Don’t falter! What could possibly scare us now?”

Others, already prepared to die, fought the enemy without giving an inch.

“Damn bitch. I hope she hasn’t figured it out already.”

And one person, feeling a familiar power, shot bloody flashes at the moths foolish enough to block his way to the Inner City.

He needed to take one man’s life quickly—and for good—before anything else could get in his way.

But that person—no, the Blood Lord—didn’t know that, several hundred jang away, an even more incredible massacre was unfolding at the North Gate.

“A-a demon……”

*Cough.*

Bloody spittle mixed with bits of entrails slipped from between his lips.

His bright yellow robe was drenched in blood, its original color long gone, and blackened corpses lay scattered all around him.

None of them knew how many had met such a horrific end.

Not even the one who had created this hellscape.

There was only one thing he knew for certain.

*Crack.*

The middle-aged monk whose neck he had just snapped in his grasp was the last surviving member of the Twelve Secret Monks, known as the greatest in Tibet.

“Now you’re the only one left.”

That old monk, frozen like a statue, was the only obstacle still standing in his way.

“……!”

The Dalai Lama’s eyes were wide open, his pupils trembling.

The Fire King, Jeok Cheongang, walked wearily toward the man frozen like a statue as he witnessed the terrible scene.

Thinking of the Disciple who must be in danger by now.

Remembering his own resolve.

“Let’s finish this quickly. He’s waiting.”

*Fwoosh.*

A white flame spread across his fatigue-dimmed pupils.
```
