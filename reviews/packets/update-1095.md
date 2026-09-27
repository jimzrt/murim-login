<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1095.txt",
      "sha256": "e17a0a463bec21f87484dcd9ddc3a80b19748646c27e7b47db3a0ee20c9d27e7",
      "bytes": 13455
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "aea505df0de3d5f52611599d7d94284a997f023fb115bf4695dab04bc4cd4efd",
      "bytes": 1130
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "aa2e383c274853719aee6fdad641fd15982ff6289e42ddd0f942d170d98f7815",
      "bytes": 243957
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "d2cd39e34dbc049473d1569209c5807c31126cd1a5e36f9df3f2e0e7809a1db8",
      "bytes": 936
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "b3bbb5ebc5a2606b59f0a7fcf3e63cc11d20a3d480133b4e559a086b5e859b2e",
      "bytes": 877
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "4dead8d09d55746d88f3c66f67042c418b82824f9ad957ca08dbd74feefe46f7",
      "bytes": 834
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "5b58301e26fb2668debed94c2b85219be6efe2645be39c9948e20651ff94c426",
      "bytes": 1120
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e11acafc8bab9f456d4345c84ac24d74a8a247e88e82192a087691b5ffc47c45",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "3280800b293bb023567a4ae3b4a7867bb966afac26f39d90dd416c5f8ed7d731",
      "bytes": 1375
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "fd55b954f68a644ce0384091f81775b058f909934cf91d0c10d581c0602c8070",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "714356e1c10c6c730c450b4e104c9775f8e38ea2d190940839a083cc97aa08ff",
      "bytes": 623
    },
    {
      "path": "characters/Namho.md",
      "sha256": "002e3a1d1ed787cb4f74fc24eda78d47406f64afe7ddf7dec97134f3ddd1971a",
      "bytes": 1092
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "372a9c5cab78949a6da2fc56bdfe02bef7c065f64d941a22c61051a6f1868a98",
      "bytes": 716
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "870faf2dded17b9a1d4f994b0c934e26d36a468f8639bad33790d4531391ec67",
      "bytes": 686
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "02d306ba8028336f9c1edce572f441c249ee3aa0e9e44b173218c0440771dc5c",
      "bytes": 889
    },
    {
      "path": "characters/Yayul Cheok.md",
      "sha256": "4c9fbd3958a0504ae17a90694354934a20b1293c9162cdbf108548cfc27bd79d",
      "bytes": 935
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ebe79c16d6adf08cf85ebe92be4ce390014b7513b9c2f13e94caedd0cd180dd5",
      "bytes": 287086
    }
  ],
  "estimated_tokens": 14649
}
-->

# Durable State Update — Chapter 1095

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
1 and safe_through 1095. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1095. Profile updates may replace only one
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
  "chapter": 1095,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1095,
    "continuity_sources": [1095],
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
    "Dark Heaven's army has arrived at Xining under the Blood Lord.",
    "Jin Taekyung and the Blood Lord are fighting; the Blood Lord is stronger, but Taekyung continues to resist.",
    "The Bow Saint is supporting Taekyung; Cheongpung, Cheongheoja, Perfected Being Hyeoncheon, and the Slaughter Saint have joined them.",
    "About a dozen Black Ghosts and the Grand Mage encircle the allied fighters.",
    "The Blood Lord believes the Lord of Heaven wants Taekyung kept alive, though he wants to kill him.",
    "A horn sounds in the distance during the standoff."
  ],
  "continuity_sources": [
    1094
  ],
  "open_questions": [
    "Who is the black-robed captive in Qinghai, and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "What will happen in the confrontation at Xining, and what does the distant horn signal?"
  ],
  "safe_through": 1094,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 궁성     | **Bow Saint**                 | —              |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 중원     | **Central Plains**                               |                                                       |
| 사천     | **Sichuan**            |
| 청해     | **Qinghai**            |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 야율척 | **Yayul Cheok** | Beast Miao King and lord of the Nanman Beast Palace. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 서장 | **Tibet** | Region considered by the Third Fiend as a possible escape route. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 새외 | **Outer Lands** | Lands outside the Central Plains and its Murim. |
| 포달랍궁 | **Potala Palace** | Palace in Tibet. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 혈주 | 청풍 | hostile_opponent_to_newly_revealed_identity | Huashan's Invincible Divine Sword; Sword Saint's Disciple or grandson | mocking and taunting | Recognizes Cheongpung's public identity and needles him with his Sword Saint lineage while dismissing the added threat. |
| 서천마군 | 청풍 | commander_to_young_opponent | you | gentle and taunting | Uses 자네 while identifying Cheongpung and discussing the Blood Lord. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 엄마 | son_to_mother | Mom | casual and startled | Jin cries out to his mother as she charges at him during the hospital visit. |
| 엄마 | 진태경 | mother_to_son | my son | warm and affectionate | Taekyung's mother praises him during the public welcome. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 야율척 | 진태경 | Nanman_Beast_Palace_Palace_Lord_to_Jeok_Cheongang's_Disciple | you / Disciple of Old Master Jeok / Jin Taekyung | rough, testing, and later welcoming | Yayul Cheok questions Taekyung as a suspected culprit, strikes him as a test, and then welcomes him after recognizing Jeok's Disciple. |
| 진태경 | 야율척 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Palace_Lord | Great Hero Yayul Cheok | formal and deferential | Taekyung gives Yayul Cheok a formal greeting as the nineteenth successor of the Fire Gate Clan. |
| 야율척 | 남호 | Palace_Lord_to_Hidden_Shadow_Pavilion_agent_and_guest | old man | blunt and inquisitive | Yayul Cheok calls on the old man beside Taishan to identify him. |
| 야율척 | 태산 | Palace_Lord_to_Fire_Dragon_Pavilion_member | you | puzzled and blunt | Yayul Cheok asks Taishan, standing beside Hwaran, to identify him, receiving only Taishan's declaration that he is hungry. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |
| 백상 | 진태경 | Nanman great chieftain to Murim Alliance Pavilion Head | you bastard | cold, hostile, and contemptuous | Baeksang calls Jin a Han Chinese man, rejects his status, and orders him to leave. |
| 진태경 | 백상 | Murim Alliance Pavilion Head to Nanman great chieftain | you | polite but deliberately provocative | Jin tells Baeksang that Nanman's blood was shed for the world rather than merely for the Central Plains. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 백상 | 야수묘왕 | Nanman great chieftain to the Nanman Beast Palace Lord | Palace Lord | restrained and apologetic | Apologizes for causing the disturbance after the Beast Miao King stops the fight. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 백상 | 남천마후 | Nanman Great Chieftain to hostile demon empress | Southern Heaven Demon Empress | formal and shocked | Baeksang directly identifies the woman who appears before him. |
| 남천마후 | 백상 | Dark Heaven controller to coerced Nanman leader | Great Chieftain Baeksang / Palace Lord | playful, taunting, and threatening | She repeatedly addresses Baeksang while mocking his grief, acknowledging his effort, and issuing her order. |
| 야수묘왕 | 남천마후 | allied_Ten_Kings_master_to_hostile_Demon_Empress | you | cold and threatening | The Beast Miao King addresses the Southern Heaven Demon Empress while promising to tear off her limbs and kill her. |
| 남천마후 | 천주 | devoted_servant_to_revered_master | Lord of Heaven | reverent and prayerful | The Southern Heaven Demon Empress prays that the Lord of Heaven will remember her loyalty and love. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 태산 | 대인 | ally addressing an elder | Sir | informal and enthusiastic | Calls out to the Great Sir while praising his shot. |
| 대인 | 태산 | elder addressing a younger ally | young friend | familiar and playful | Offers Taishan a portion of the bird as a reward. |
| 청풍 | 대인 | younger companion addressing an older benefactor | Uncle Great Sir | polite and familiar | Cheongpung repeatedly calls him 대인 아저씨. |
| 대인 | 청풍 | older benefactor addressing a younger companion | you | familiar and teasing | Great Sir addresses Cheongpung as 자네. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 1027
- **Aliases:** None
- **Role:** Baeksang was the Palace Lord of the Nanman Beast Palace and sole Great Chieftain of Nanman, and he died by the Beast Miao King's hand after confessing to serving Dark Heaven's plan.
- **Personality:** Cold, rigid, meticulous, and strategically resolute, yet burdened by regret, grief over Hwi's death, and a final conflicted impulse to spare others from the coming bloodshed.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion, Yayul Mok's sworn uncle, and the father of Baekhwi, whom he believed the Great Snow Fiend killed but Dark Heaven has kept alive in a deep sleep; he cultivated Yohi with gold and influence and used her support to advance Dark Heaven's preparations.

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 724
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, the publicly recognized sole priest of the Earth Mother Goddess, and the ruler of unified Nanman committed to opposing Dark Heaven.
- **Personality:** The Beast Miao King is boisterous and warmhearted toward Nanman's people, but their corruption and destruction awaken fierce grief and wrath in him.
- **Voice:** Low, growling, and forceful.
- **Relationships:** Baeksang was his sworn younger brother and childhood companion, and the Beast Miao King killed him at his request; Yayul Mok is his Young Palace Lord, Jeok Cheongang is an old acquaintance, and Jin Taekyung is Jeok's Disciple and ally.

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 1094
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who directs its sorcerers’ seed experiments and prepares their deployment for the Lord of Heaven’s great cause.
- **Personality:** Confident, cruel, and controlling; strategically manipulates allies and adversaries, and conceals failures from the Lord of Heaven when he fears being discarded.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven with deep loyalty, yet believes his master values Jin Taekyung’s safety above that of loyal servants; he considers Taekyung and Cheongpung formidable adversaries.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1094
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has also learned concealment from the Slaughter Saint.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, competitive pride, and compassion that leaves him unsettled by killing; he admires Taekyung’s resilience in the way he lives.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint has become his mentor in concealment.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1094
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1088
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1094
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1094
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1067
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 1049
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress was Honglan, the creator of the rift behind the Inner Palace, and was killed after the rift closed.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1093
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 1067
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

### Yayul Cheok.md

# Yayul Cheok (야율척)

- **Safe through:** Chapter 723
- **Aliases:** Beast Miao King
- **Role:** Yayul Cheok is the over-eighty Palace Lord of the Nanman Beast Palace, a Supreme Peak master among the Ten Kings, Great Chieftain of the Miao people, and public priest of the Earth Mother Goddess.
- **Personality:** Boisterous, warmhearted, forthright, playful, and politically conscious of the tribal coalition he leads.
- **Voice:** Rough, loud, convivial, and teasing, becoming authoritative when discussing Nanman's laws or political decisions.
- **Relationships:** Jeok Cheongang is an old acquaintance whom he respects; Baeksang is his sworn younger brother and childhood companion, and they fought together during the Great Faction War; Yayul Mok serves as his Young Palace Lord; Jin Taekyung is Jeok's Disciple whom he welcomes into the Nanman Beast Palace.

## Korean source

```text
1095화




부우! 부우우우!

수백여 장의 공간을 가로지른 웅혼한 뿔피리 소리가 귓가를 파고든 그 순간, 진태경은 문득 생각했다.

이와 비슷한 소리를, 분명 어디선가 들어 본 적이 있다고.

축축하고 어두컴컴했던 수천 리 밖의 땅, 바로 남쪽의 끄트머리에서.

‘……설마?’

섬광처럼 머리를 스친 어떠한 짐작과 함께, 진태경은 크게 뜨인 두 눈으로 뿔피리 소리가 들려온 방향을 응시했다.

그와 동시에 마침내 볼 수 있었다.

어느덧 저 멀리에서 자욱하게 일어난 먼지구름 사이, 상당한 거리임에도 불구하고 확연하게 눈에 띄는 커다란 코를 휘날리며 이곳으로 달려오는 거대한 존재들을.

‘저건.’

그것들의 정체는 다름 아닌 코끼리였다.

그 어떤 맹수보다, 아니 육지와 강에 서식하는 모든 것들을 통틀어 가장 크고 강인한 생명체.

그리고 중원인들이 상(象)이라 부르며 신비롭게 여기는 저 동물들은, 진태경을 비롯한 몇몇 인물들에게는 제법 익숙한 존재이기도 했다.

코끼리를 포함한 수많은 동물과 더불어 살아가는 동시에, 저들을 조련하여 길들이고 죽은 후에는 아름다운 상아(象牙)를 깎아 뿔피리를 만드는 이들과 잠시나마 함께 했었으니까.

“남만야수궁(南蠻野獸宮)! 남만야수궁이 왔다!”

이제는 그리 멀지 않은 성벽 위, 어림잡아도 수백 마리에 달하는 코끼리 떼를 발견하고 한껏 고양된 혁무진이 의기양양하게 외쳤다.

“보고 있냐, 이 개자식들아!”

불과 일각 전까지만 해도 성벽 아래의 격전을 지켜보며 마른침만 꼴깍꼴깍 삼켰던 혁무진이었지만, 이제는 아니었다.

“붙어, 제대로 붙어! 이제는 우리도 쪽수로 엥간치 꿇리지 않는다 이거야!”

혁무진의 확신에는 충분한 이유가 있었다.

남천마후(南天魔后)의 흉계로 인해 벌어진 엄청난 파란이 수습된 직후부터 남만야수궁은 본격적으로 움직이기 시작했다.

아니, 그것은 단순히 움직였다고 표현할 수 없을 정도의 대대적인 이동이었다.

내부에서 자라난 병든 싹을 모조리 숙청하고, 그것으로도 모자라 아득한 과거부터 선조들이 머무르던 터전마저 버렸으니까.

야수묘왕(野獸苗王) 야율척은 남만의 밀림을 피로 물들게 한 암천의 흉계에 그 어느 때보다 분노했고, 의형제였던 백상의 죽음에 누구보다 슬퍼했으며, 동시에 이 크나큰 위기에서 자신들을 구해 준 중원의 이방인들에게 가슴 깊이 감복했다.

그리하여, 야수묘왕의 중심으로 완전히 하나가 된 남만야수궁은 마침내 무림맹으로의 입맹(入盟)과 동족의 복수를 맹세하며 피로 얼룩진 고향을 떠났다.

물경 수만에 달하는 모든 남만인들과, 그들이 거느린 숱한 맹수들도 함께.

그리고 사천에 머무르고 있어야 할 남만야수궁의 전력이 이곳에 나타났다는 것은, 또 하나의 사실을 의미하는 것이기도 했다.

“남만야수궁에, 사천당가에, 청성과 아미까지 한 묶음으로 왔을 거다! 네놈들은 이제 전부 다 뒈졌어!”

주먹을 불끈 움켜쥔 채 부르짖음는 혁무진의 모습에, 압도적인 암천의 군세 앞에서 바짝 얼어붙어 있던 성벽 위의 아군들도 그제야 얼굴에 화색이 돌았다.

“와아아아!”

“지원군이다! 지원군이 왔다!”

“그래, 이 개자식들아! 시원하게 한번 붙자!”

들려오는 풍월로는 소왕국이나 다름없다는 남만야수궁의 전력에 더하여, 천하 무림 그 자체를 상징하는 명문대파가 무려 세 곳이나 합류한 상황.

그렇기에 이미 패배를 직감하고 체념하던 이들도, 마음속 불안감을 애써 억누르며 희망을 부여잡고 있던 이들도 언제 그랬냐는 듯 온 힘을 다해 함성을 내질렀다.

하지만 단숨에 성벽 위를 뒤덮은 그 환희의 물결 속에서도, 어째서인지 더욱 깊게 가라앉은 눈동자로 저 멀리 다가오는 먼지구름을 응시하는 이가 있었다.

‘남만야수궁으로 모자라 사천의 다른 세 문파까지? 저들은 결코 사천을 비울 수 없는 상황이었을 텐데.’

유난히도 우뚝 솟아 있는 태산의 어깨 위에 걸터앉은 채, 노회한 시선으로 성벽 너머를 바라보던 남호는 천천히 자신의 머릿속을 되짚었다.

남만야수궁의 전력. 이미 서천마군을 중심으로 벌어진 일련의 사건으로 엄청난 타격을 입은 바 있던 사천 무림의 현재 상황.

그리고 그들이 이곳에 올 수 없다고 생각한 이유까지.

‘사천은 천하에서 손꼽히는 광활한 땅. 그 광범위한 전선(前線)을 생각한다면 황군만으로는 역부족이다. 한데 어떻게?’

작금의 천하는 무림과 국가의 경계선마저 사라진 가파른 산비탈과 같다.

암천이라는 눈덩이는 이미 반세기 전부터 굴러가고 있었고, 만근거석(萬斤巨石)이나 다름없게 된 적들은 눈 덮인 산비탈을 구르고 굴러 그 아래의 마을을 덮치기 일보 직전이다.

아니, 천하를.

그렇기에 무림맹 또한 이런 상황에서 청해를 구원할 별다른 묘수를 떠올리지 못했을 터다.

조금이라도 공백이 생긴다면, 암천은 예리한 송곳이 되어 그 공백을 파고들 테니까.

단지 표면을 찌르는 것이 아닌 내부 깊숙한 어딘가, 이동진이라는 기괴한 술법을 사용해서.

심지어 현재 사천 무림이 처한 상황은 중원의 어느 지방보다도 좋지 않았다.

정확히는 좋지 않은 것을 넘어, 최악이라고 할 수 있었다.

그들이 신경 써야 하는 것은 내부 어딘가에서 유령처럼 나타날 적들뿐만이 아니었으니.

‘진정으로 저들이 자신들의 본거지마저 버리고 우리를 구원하러 온 것이라면, 사천과 맞닿아있는 서장(西藏)의 적들이 곧장 사천을 넘어 중원으로 향할 수도 있…….’

그 순간.

남호의 머릿속에서 뒤죽박죽 얽히고 이어지기를 반복하던 수많은 생각이 단숨에 증발했다.

그리고 등골을 타고 흐르는 한기를 느끼며 얼어붙은 그의 귓가로, 누군가의 나직한 탄성이 흘러들어왔다.

“키야, 저렇게 많은 상(象, 코끼리)이 한자리에 모이다니. 높은 곳에서 보니 장관도 이런 장관이 없구먼. 역시 남아 있길 잘했어.”

대인(大人).

바로 그였다.

궁성과 청풍을 비롯한 다른 초절정 고수들과는 달리, 지금까지도 꿋꿋하게 자리를 지키고 있던 그는 마치 구경꾼처럼 태평한 어조로 중얼거렸다.

“확실히 독특하긴 하네. 가만히 서 있기만 해도 숨이 턱턱 막히는 동네라고 듣긴 했지만, 남만 사람들은 죄다 저렇게 머리를 빡빡 밀고 다니나?”

그때, 넋이 나간 사람처럼 멍하니 굳어 있던 남호가 벼락처럼 고개를 돌려 대인을 바라보았다.

“지금 그게…… 대관절 무슨 소리요?”

“무슨 소리냐니? 그냥 보이는 대로 말한 것뿐인데.”

고개를 갸웃거린 대인은 수백여 장 밖에서 서서히 가까워지는 먼지구름을 가리켰다.

수십여 장이나 되는 높이의 성벽 위라는 조건과 초절정의 안력(眼力)을 갖춘, 오직 그만이 볼 수 있는 광경을.

아니.

정확히는 한 치 앞도 분간할 수 없을 것 같은 희뿌연 먼지구름 속, 붉고 노란 의복을 두른 채 코끼리 떼를 앞세워 진군하고 있는 수천여 명의 무리를.

“어라? 가만. 지금 다시 보니…….”

그들을 뚫어져라 응시하던 대인이, 턱을 긁적이며 덧붙였다.

“꼭 승려 같기도 한데?”

그 순간.

어느덧 슬슬 팔순을 바라보는 늙은 은영각 요원의 입술 사이로, 그 자신도 깜짝 놀랄 만큼 커다란 고함이 뛰쳐나왔다.

“이 염병할 호래자식아! 포달랍궁(布達拉宮)이잖아!”

그와 동시에.

부우우우!

웅혼한 뿔피리 소리에 맞춰, 수백 마리의 코끼리를 앞세운 포달랍궁의 군세가 미친 듯이 질주하기 시작했다.



* * *



21세기의 현대와 이 세상의 사이에는 무시할 수 없는 간극이 있다.

흡사한 것도, 조금 다른 부분도 있다.

그리고 세인들이 서장(西藏)이라 부르며 중원에서 수만 리나 떨어진 새외(塞外)로 규정지은 땅은, 내가 이해하기로 후자에 가까웠다.

서장.

무림에서 나만이 아는 다른 명칭으로는, 티베트(Tibet).

그리고 그곳에서 자신들만의 울타리를 쌓고 살아가는 또 하나의 종교 집단, 포달랍궁(布達拉宮).

그것이 갑작스럽게 나타난 저 거대한 먼지구름의 정체였다.

뿌우우우!

수백 마리의 코끼리 떼가 동시에 울음소리를 토해 내며 미친 듯이 달려온다.

지금 보니 길고 아름다워야 할 상아는 어디에 한 번 튀기기라도 했는지 거무튀튀했고, 벌겋게 달아오른 눈깔은 이미 맛이 갔다.

‘저딴 게…… 내가 알던 코끼리?’

시시각각 가까워지는 그 모습을 보며 다시금 느꼈다.

다르다. 차원이 다르다.

저 코끼리들은 엄마 손을 잡고 갔던 동물원 철창 속에서 보았던 모습과도, 남만에서 보았던 것들과도 그 궤를 달리했다.

덩치, 광기, 흉포함. 그 모든 것에서.

어릴 적 보았던 아기코끼리 덤보?

지랄하지 마라.

만약 원작자가 저 미친것들을 소재로 삼았다면, 내가 본 애니메이션의 제목은 ‘일단 아기인데 존나 쎈 코끼리 천마군림보’가 되었을 테니까.

구구구구궁!

진짜 천마군림보라도 쓰고 있는지 지축이 요동친다.

아니, 그것으로도 모자라 이제는 쩍쩍 갈라진다.

반지 부수는 난쟁이 영화에서나 보던 거대 코끼리들을 실사화로 마주한 청풍이 반쯤 넋이 나간 목소리로 감상평을 중얼거렸다.

“으아, 저런 건 진짜 태어나서 처음 봐요…….”

나도 처음이야, 시발.

그 한 마디가 목구멍을 타고 튀어나오려고 했지만, 간신히 억누를 수밖에 없었다.

이유?

간단하다.

상당한 거리를 빠르게 좁히며 시시각각 가까워지는 포달랍궁이 아니더라도, 지금 이 순간에도 주위를 빽빽하게 둘러싼 암천의 군세가 있었으니까.

“생각보다도 일찍 도착했군. 운 좋게도.”

어느덧 여유로운 미소를 머금은 혈주가 말을 이었다.

“물론, 네놈들에게는 더없는 불운이겠지만.”

나는 대답 대신 창대를 힘껏 움켜쥐었다.

점입가경이다.

가뜩이나 불리한 형세에, 생각지도 못한 서장의 포달랍궁까지 암천에 가세하다니.

‘처음부터 사천 따위는 안중에도 없었던 거야.’

물론 이런 상황을 아예 염두에 두지 않은 것은 아니다.

다만, 확률 자체는 희박하다고 여겼다.

나뿐만이 아니라 대부분이 그렇게 생각했다.

암천이 서장에 잠자코 있던 포달랍궁까지 끌어들인 이유는, 사천의 전선을 틀어막고 청해성으로 향할지도 모를 지원군을 사전에 방지하기 위해서일 것이라고.

하지만 틀렸다.

혈주가, 아니 그의 뒤에 있는 천주(天主)가 청해성의 일을 통해 반드시 얻고자 하는 것은 중원으로 나아갈 수 있는 교두보 따위가 아니었다.

‘나. 바로 나였어.’

비로소 찾아온 깨달음과 함께, 거대한 바위가 가슴 한구석을 짓눌렀다.

더없이 무겁고. 저려올 만큼.

“도대체 어째서?”

나도 모르게 입술 사이로 흘러나온 짤막한 물음.

그러나 내 말뜻에 담긴 뜻을 알아차린 혈주는 선선히 대꾸했다.

“너는 호숫가에 드리워진 낚싯대가 주인의 마음을 알고 있다고 생각하나?”

“뭐?”

“나도 모른다. 다만 주인이 시키는 대로 행할 뿐이지. 저들로 하여금 사천을 공격했다면 중원으로 향할 길이 뚫렸을지도 모르지만…… 그분께서는 생각이 다르시더군.”

“……!”

“걱정하지 마라. 오늘만큼은 살려 주겠다는 그 약속은 지킬 테니. 다만 한 가지는 똑똑히 알아 둬. 너희는 이미 그물에 갇혔다. 절대 빠져나올 수 없는 그물에.”

그리고 바로 다음 순간.

낮게 깔린 혈주의 전음(全音)이 귓가를 파고들었다.

- 하루. 앞으로 단 하루의 시간을 주마. 그 안에 스스로 근맥을 끊고 투항한다면 너 이외의 다른 이들은 살려 주지.

천천히 손을 들어 올리며, 얼어붙은 나를 향해 혈주가 입꼬리를 말아 올렸다.

- 그분, 내 유일한 빛이자 하늘이신 천주의 이름을 걸고 맹세한다. 이게 내 마지막 자비이자 네 사람들을 살릴 유일한 길이야.

그것으로 끝이었다.

혈주의 손짓을 따라 갈라지는 포위망과 함께, 그의 입가에 걸린 조소가 내 폐부를 찔렀다.
```

## Final English reading copy

```markdown
# Chapter 1095

Bwooo! Bwooooooo!

The deep, resonant sound of a horn pierced Jin Taekyung’s ears, carrying across hundreds of yards. At that moment, he suddenly thought of something.

He was sure he’d heard a similar sound somewhere before.

In a damp, pitch-dark land thousands of miles away, at the very southern edge.

*…No way.*

A suspicion flashed through his mind like lightning. Eyes wide, Jin Taekyung stared in the direction the horn had come from.

And at last, he saw them.

Through a thick cloud of dust rising in the distance, enormous creatures came charging toward them. Even from this far away, he could clearly make out their great trunks swinging as they ran.

*Those are…*

They were none other than elephants.

The largest, strongest living creatures of all—not just among beasts, but among every creature that lived on land or in rivers.

The people of the Central Plains called them *xiang*—elephants—and regarded them as mysterious animals. But to a few people, Jin Taekyung among them, they were fairly familiar.

They’d spent a brief time with people who lived alongside countless animals, elephants included, and who trained and tamed them. When the elephants died, those people carved their beautiful tusks into horns.

“Nanman Beast Palace! The Nanman Beast Palace is here!”

On the nearby wall, Hyuk Mujin spotted the herd—hundreds of elephants by his rough estimate—and shouted, brimming with excitement.

“Do you see that, you bastards?!”

Barely fifteen minutes ago, Hyuk Mujin had only been able to stand on the wall, watching the fierce battle below and swallowing nervously. But not anymore.

“Come on, bring it on! Now we’re not so badly outnumbered!”

He had good reason to be sure of himself.

The Nanman Beast Palace had begun to move in earnest soon after the enormous upheaval caused by the Southern Heaven Demon Empress’s scheme was brought under control.

No, “move” hardly did it justice. This was a mass migration on a staggering scale.

They’d purged every diseased shoot that had grown within their ranks. And that wasn’t enough—they’d even abandoned the homeland where their ancestors had lived since time immemorial.

Beast Miao King Yayul Cheok was more furious than ever at Dark Heaven’s scheme, which had drenched Nanman’s jungles in blood. He grieved the death of his sworn brother Baeksang more than anyone. And at the same time, he was deeply moved by the outsiders from the Central Plains who had saved them from this enormous crisis.

Thus, with the Beast Miao King at their center, the Nanman Beast Palace became wholly united. They swore to join the Murim Alliance and avenge their people, then left their bloodstained homeland.

Every last one of Nanman’s tens of thousands of people went with them, along with the countless ferocious beasts they commanded.

And the fact that the Nanman Beast Palace’s forces—who should have been in Sichuan—had appeared here meant something else, too.

“The Nanman Beast Palace, the Sichuan Tang Clan, Qingcheng, and Emei must all have come together! You’re all dead now!”

At Hyuk Mujin’s shout, his fist clenched, the allies on the wall—who had been frozen stiff before Dark Heaven’s overwhelming forces—finally brightened.

“Waaah!”

“Reinforcements! The reinforcements are here!”

“Yeah, you bastards! Let’s give them a proper fight!”

The Nanman Beast Palace’s forces were said to be practically a small kingdom in their own right. And now they had three great sects with them, each representing the very heart of the martial world.

Even those who had already sensed defeat and resigned themselves to it, and those who had clung to hope while forcing down their unease, all let out a full-throated cheer as if they’d never felt that way at all.

But amid the wave of joy that swept over the wall, one person gazed at the approaching dust cloud in the distance with eyes that had somehow sunk even deeper.

*The Nanman Beast Palace, and the other three Sichuan factions, too? They couldn’t possibly have left Sichuan unguarded.*

Sitting on Taishan’s unusually high shoulder, Namho slowly retraced his thoughts as he watched beyond the wall with a seasoned gaze.

The Nanman Beast Palace’s strength. The current state of Sichuan’s Murim, already dealt a tremendous blow by the chain of events centered on the Western Heaven Demon Lord.

And why he’d thought they couldn’t come here.

*Sichuan is one of the largest regions in the world. Given the length of its front lines, the imperial army alone wouldn’t be enough. So how could they…?*

The world today was like a steep mountainside where even the boundary between Murim and the state had disappeared.

The snowball that was Dark Heaven had been rolling for half a century already. The enemy had become a boulder weighing ten thousand pounds, rolling down the snow-covered slope and on the verge of crushing the villages below.

No—the entire world.

That was why the Murim Alliance wouldn’t have been able to think of a way to rescue Qinghai under these circumstances.

If even the slightest gap opened, Dark Heaven would become a sharp awl and drive straight into it.

Not just to pierce the surface, but to reach somewhere deep inside, using that bizarre sorcery called a Moving Formation.

On top of that, the situation in Sichuan’s Murim was worse than anywhere else in the Central Plains.

More than bad—it was the worst it could be.

The only enemies they had to watch out for weren’t the ones who might appear like ghosts somewhere within Sichuan.

*If they really have abandoned their homeland to come save us, the enemies bordering Sichuan in Tibet could cross straight through Sichuan and head for the Central Plains…*

At that moment—

The countless thoughts tangled together in Namho’s mind, looping and colliding, vanished all at once.

A chill ran down his spine. As he froze, a low exclamation reached his ears.

“Damn, there are a lot of elephants gathered in one place. Seeing them from up high is quite a sight. Sure glad I stayed.”

Great Sir.

It was him.

Unlike Bow Saint, Cheongpung, and the other Supreme Peak masters, he had stubbornly held his position until now. He muttered in a carefree tone, like a spectator enjoying the view.

“Sure is unusual. I’d heard it was the kind of place where you’d be gasping for breath just standing still, but do all the people of Nanman shave their heads like that?”

Namho, who’d been staring blankly like a man in a daze, whipped his head around to look at Great Sir.

“What… What on earth are you talking about?”

“What do you mean? I’m just saying what I see.”

Great Sir tilted his head and pointed at the dust cloud slowly drawing nearer from hundreds of yards away.

From atop the wall, dozens of yards high, he could see what no one else could—not with anyone else’s eyes, anyway. His Supreme Peak eyesight let him pick out the scene.

No.

More precisely, he could see thousands of people wearing red and yellow robes, advancing with a herd of elephants at their head through the pale, hazy dust cloud, where it seemed impossible to make out anything a few feet ahead.

“Huh? Wait. Now that I look again…”

Great Sir stared hard at them, scratching his chin, then added:

“They kind of look like monks, too.”

At that moment—

A shout erupted from the lips of the old Hidden Shadow Pavilion agent, who was nearing eighty, so loud that even he was startled by it.

“You damn bastard! That’s the Potala Palace!”

And at the same time—

Bwooooooo!

To the deep, resonant sound of the horn, the Potala Palace’s army charged forward like mad, led by hundreds of elephants.



* * *



There was an undeniable gap between the modern world of the twenty-first century and this one.

Some things were similar. Others were a little different.

And the land people here called Xizang, thousands of miles from the Central Plains and classified as part of the Outer Lands, was closer to the latter, as far as I understood it.

Xizang.

In Murim, I alone knew its other name: Tibet.

And the Potala Palace—a religious group that had built its own little world there.

That was the identity of the enormous dust cloud that had suddenly appeared.

Bwooooo!

Hundreds of elephants charged like mad, trumpeting all at once.

Now that I could see them up close, their long, beautiful tusks were blackened, as if someone had deep-fried them. Their bloodshot eyes were completely out of control.

*Those things… are elephants?*

Watching them draw closer by the second, I realized it again.

They were different. On another level entirely.

They were nothing like the elephants I’d seen behind the bars at the zoo when I’d gone with my mom as a kid, or the ones I’d seen in Nanman.

Their size, their madness, their ferocity. Everything.

Dumbo the baby elephant I’d seen as a kid?

Give me a break.

If the original author had used these lunatics as inspiration, the cartoon I’d watched would’ve been called *He’s Just a Baby, but He’s Freaking Strong: Elephant Heavenly Demon’s Reign*.

Rumble, rumble, rumble!

The earth shook as if they really were using the Heavenly Demon’s Reign.

No—as if that weren’t enough, the ground was cracking apart.

Facing real-life versions of the giant elephants from that movie about little folk destroying a ring, Cheongpung murmured his verdict, half dazed.

“Whoa. I’ve never seen anything like that in my life…”

Neither have I, shit.

The words nearly slipped out of my mouth, but I barely managed to hold them back.

Why?

Simple.

Even without the Potala Palace rapidly closing the distance, Dark Heaven’s forces still surrounded us on every side, packed tightly around us even now.

“They arrived sooner than expected. How fortunate.”

The Blood Lord spoke with a relaxed smile.

“Of course, it’s the worst possible luck for you.”

I tightened my grip on the shaft of my spear instead of answering.

This was getting worse by the second.

We were already at a disadvantage, and now the Potala Palace from Tibet had joined Dark Heaven, too.

*They never cared about Sichuan in the first place.*

It wasn’t as if I hadn’t considered this possibility.

I’d just thought the odds were slim.

I wasn’t the only one. Most people thought so.

We believed Dark Heaven had drawn in the Potala Palace, which had been quietly staying in Tibet, to block the front lines in Sichuan and stop any reinforcements from reaching Qinghai Province.

But we were wrong.

What the Blood Lord—or rather, the Lord of Heaven behind him—wanted from what was happening in Qinghai wasn’t some foothold from which to advance into the Central Plains.

*It was me. I was the one he wanted.*

As the realization finally came, a huge rock seemed to press down on one corner of my chest.

So heavy it made me ache.

“Why?”

The brief question slipped from my lips before I knew it.

But the Blood Lord understood what I meant and answered readily.

“Do you think a fishing rod cast over a lake knows what its owner is thinking?”

“What?”

“I don’t know, either. I only do as my master commands. If he’d had them attack Sichuan, they might have opened a route into the Central Plains… but the Lord of Heaven had other ideas.”

“…”

“Don’t worry. I’ll keep my promise to spare you today. But understand this: you’re already caught in a net. One you’ll never escape.”

And then, right after that—

The Blood Lord’s low Sound Transmission pierced my ears.

*I’ll give you one day. If you sever your Sinews and Meridians and surrender of your own accord within that time, I’ll spare everyone but you.*

The Blood Lord slowly raised a hand and curled his lips into a smile at me, frozen in place.

*I swear by the name of the Lord of Heaven, that person who is my one and only light and sky. This is my last mercy—and the only way to save your people.*

That was the end of it.

As the encirclement parted at the Blood Lord’s gesture, the scornful smile on his lips stabbed into my chest.
```
