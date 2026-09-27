<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1135.txt",
      "sha256": "2be796c9132dcfc9231a872dcb690a9f062faae2a6028416e6ca04f1a53817d1",
      "bytes": 16943
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "8d80e10fd4d7a7c5704c608c4b8f48df31428926897a7fe879b7c86774db167b",
      "bytes": 612
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a748a23dd04ae8f0d0c8056ba9e2d3b28b4a655e79077f108552bb0f78f6c332",
      "bytes": 245483
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "02a27386e72e6d968db918fb50b16d9c0d4eac82b50279ef686ea04587e5e2dd",
      "bytes": 951
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "cbe75d6b40449e40472bbafd4873a0700cf02b832635cc430b72e29a1652369e",
      "bytes": 760
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "aca1b337cd7568ebdaf8c467161fb3bd21a2a94011cb0dc738bce7726085366a",
      "bytes": 839
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "bcc837fd161876a4f1f4ca168996acf1501ea81ee760f4b01007f407155cf610",
      "bytes": 670
    },
    {
      "path": "characters/Hak Woo.md",
      "sha256": "ba33bee790095ddb3a5e232f69f22c33823788115287068be09620458c8631f1",
      "bytes": 613
    },
    {
      "path": "characters/Jang Sam.md",
      "sha256": "6c2019cae75425e7e1ab0c153105305dd188056ee7a984c279cc516ededc3974",
      "bytes": 509
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "0c82f5f997f425a08f64e2ac585fb9179968be0d20a9fe02bb8e0ead1e13dd10",
      "bytes": 1929
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "219769ca21f3ab614879b4b6b1c0876e077aba0681852e84a1d4ec19647b7df7",
      "bytes": 623
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "7c538152fc6688fd9517501955ed5c9fc1ffd6f3bd654700fe0837e3a519308d",
      "bytes": 948
    },
    {
      "path": "characters/Masked Man.md",
      "sha256": "be20b92b87bdb1f2a0fb4b0837e5a8bd44ed2938b52275bbcb89d1fdd10058b0",
      "bytes": 683
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "b8f7b5817a6b580163de606bcc1af4aa66e32c276ae01ecf3617907b8f30a382",
      "bytes": 896
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "4ec25d76a71efedcbe21979e04d4b0e68688fa903376734f06ece61872b4595c",
      "bytes": 1043
    },
    {
      "path": "characters/Zhuge Feng.md",
      "sha256": "1a5e0d744bc7a32acdad77c5d705dc4525c9a8e416a18fee109ec8c4bb834da4",
      "bytes": 650
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a2d0b132c6b5c100792a4fa466bc2deeab7921a8134b7206d6d4a5220049871a",
      "bytes": 290762
    }
  ],
  "estimated_tokens": 15683
}
-->

# Durable State Update — Chapter 1135

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
1 and safe_through 1135. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1135. Profile updates may replace only one
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
  "chapter": 1135,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1135,
    "continuity_sources": [1135],
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
    "The Helper gave Taekyung an unidentified gift and chose to remain in the enduring gray-white space, awaiting an unknown end.",
    "Ma Sanbao and roughly one thousand followers survived Zhuge Feng’s ambush in a remote Henan valley; Baek Yeon and the Son of Heaven confronted him while he was unable to move."
  ],
  "continuity_sources": [
    1133,
    1134
  ],
  "open_questions": [
    "What did the Helper give Taekyung?",
    "What will happen to Ma Sanbao after the Son of Heaven confronts him?"
  ],
  "safe_through": 1134,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 파륜     | **Pa Ryun**        |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 권왕     | **Fist King**                 | Yan Hwapyeong  |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 십왕     | **Ten Kings**       |
| 하오문    | **Lower District Sect**          |
| 화산파    | **Huashan**                      |
| 무림맹    | **Murim Alliance**               |
| 제갈세가   | **Zhuge Clan**                   |
| 남궁세가   | **Nangong Family**               |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 안휘     | **Anhui**              |
| 화산     | **Huashan**            |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 학우 | **Hak Woo** | Kunlun Sect top young prodigy known as the Kunlun Cloud Dragon; Taekyung addresses him as Hak. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 복면인 | **Masked Man** | The Southern Heaven Demon Empress's trained hunting dog; identity remains unknown. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 제갈풍 | **Zhuge Feng** | Current Family Head of the Zhuge Clan. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 검왕 | **Sword King** | Short form for the Azure Sky Sword King, Nangong Cheon. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 만리추행 | **Myriad-Mile Pursuit** | Epithet of the Beggars' Sect Leader and master of movement techniques. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 선화아 | **Ship-Fire Boy** | Mu Song's sobriquet; literally a child who lights fires aboard a ship. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 일원 | **One Origin** | Named Tang Clan organizational unit in Tang Sadok's mobilization order. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 뇌옥 | **underground prison** | The Tang Clan's subterranean prison. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 장성 | **Great Wall** | Wall used in the discussion of the Outer Lands. |
| 위압 | **Intimidation** | System attribute strengthened by the achievement reward. |
| 대역 | **stand-in** | Jin's term for the substitute Go Jun used to fake Song Cheonwoo's departure. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 무영 | **No Shadow** | The concealed Supreme Peak assassin serving the Emperor. |
| 황도십이궁 | **Twelve Palaces of the Zodiac** | Collective title for twelve Supreme Peak masters representing the imperial court. |
| 금위군 | **Imperial Guards** | Imperial force distinct from the Embroidered Uniform Guard. |
| 주체 | **Zhu Di** | The Emperor names himself as Zhu Di. |
| 백환강시공 | **White Illusion Jiangshi Art** | Martial art named on the old bamboo slip. |
| 황도 | **Imperial Capital** | The capital where the imperial court resides. |
| 천수 | **Tianshui** | City on Gansu’s eastern edge, bordering Shaanxi. |
| 황태제 | **Imperial Younger Brother** | Title for the Emperor’s appointed heir apparent. |
| 강시공 | **Corpse Art** | Wei Zhong’s technique for creating or controlling jiangshi. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 무송 | junior_martial_artist_to_senior_martial_artist | Senior | formal-polite | Taekyung uses 선배님 after recognizing Mu Song as a senior martial artist and disciple of the Seafaring King. |
| 무송 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | familiar-teasing | Mu Song calls Taekyung 후배 and jokes about his supposed taste for men. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 제갈풍 | 무송 | family_head_to_stronghold_lord | Ship-Fire Boy Mu Song | calm, formal, and pointed | Zhuge Feng stops Mu Song from leaving by saying the coming information concerns him. |
| 무송 | 제갈풍 | stronghold_lord_to_orthodox_family_head | Great Hero Zhuge | formal and concerned | Mu Song addresses Zhuge Feng after realizing why he was asked to remain. |
| 제갈풍 | 진태경 | senior strategist_to_younger_martial_artist | you | calm and familiar | Uses 자네 while inviting Taekyung to continue questioning the Hubei incident. |
| 제갈풍 | 궁기방 | family_head_to_beggars_sect_successor | Successor Beggar | calm and conversational | Uses 후개 when confirming Gung Gibang's guess about the broken weapon. |
| 궁기방 | 무송 | martial companion to Stronghold Lord | Senior Mu Song | pleading-deferential | Begins pleading for Mu Song to save them from Tianling Falls. |
| 가솔 | 진태경 | Zhuge Clan retainer to Great Hero | Great Hero Jin | polite and pleading | Uses 진 대협 while urging Taekyung to stop provoking Ju Wongong. |
| 진태경 | 제갈풍 | younger martial artist to senior clan head | Sir Zhuge | blunt and challenging | Uses 제갈 대협 while disputing Zhuge Feng's attempted ten-percent claim. |
| 진태경 | 학우 | former_rival_to_Kunlun_young_prodigy | Hak | mocking and threatening | Taekyung uses Sound Transmission to intimidate Hak Woo into leaving. |
| 학우 | 진태경 | Kunlun_young_prodigy_to_famous_senior | Fellow Daoist Jin | formal and defensive | Hak Woo addresses Taekyung as 진 도우 while denying that he is busy. |
| 진태경 | 복면인 | hostile combatant to unknown hostile combatant | you | blunt, hostile, and incredulous | Jin directly questions the masked man about his identity and his relationship with the Great Snow Fiend. |
| 주표 | 백연 | prince addressing an imperial military officer | Commander Baek Yeon | formal and authoritative | Addresses Baek Yeon by name and office while insisting that he answer. |
| 백연 | 주표 | imperial officer addressing a prince | Your Highness | formal and deferential | Uses 전하 when apologizing to and answering Prince Shangshan. |
| 진태경 | 백연 | young martial artist confronting an imperial military commander | you | casual and insulting | Refers to Baek as 이 양반 while challenging his conduct. |
| 백연 | 천자 | imperial officer addressing the Emperor | Your Majesty | formal, deferential in address but openly defiant in private counsel | Baek uses formal honorifics while sharply confronting the Emperor over their shared undertaking. |
| 천자 | 백연 | Emperor addressing his military commander | Baek Yeon | familiar and authoritative | The Emperor addresses Baek by name and gives him a direct warning. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 백연 | 진태경 | imperial commander confronting a young martial artist | Jin Taekyung | measured and familiar, using 자네 | Baek Yeon cautions Taekyung about his words and asks whether he must cause a scene. |
| 마삼보 | 진태경 | political ally recruiting a young martial artist | you; my friend | courteous and familiar | Ma uses 자네 and 이보게 while explaining his choice of Jin and inviting him to join the restoration army. |
| 진태경 | 마삼보 | young martial artist addressing the East Depot’s Brush-Holding Eunuch and prospective ally | you; Brush-Holding Eunuch | polite and direct | Jin asks Ma why he withheld information and presses him for a clear answer; he refers to him as 태감. |
| 마삼보 | 동천마군 | disciple_to_master | Master | deferential | Ma Sanbao addresses the Eastern Heaven Demon Lord as 스승님 when rejoining him. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 상산왕 | 동천마군 | young imperial prince addressing the enemy who killed his parents and brothers and suffered at the hands of his grandfather | you | formal-polite | He apologizes for his grandfather’s actions using 당신 and deferential speech. |
| 제갈풍 | 맹주 | Zhuge Clan Family Head to Murim Alliance Leader | Alliance Leader | polite | Zhuge Feng addresses the concealed Alliance Leader in the Zhuge Clan garden. |
| 무송 | 파륜 | disciple_to_master | Master | respectful, but frank and challenging | Mu Song addresses Pa Ryun as 스승님 while pleading with him to reconsider. |
| 파륜 | 무송 | master_to_disciple | you | gruff and commanding | Pa Ryun addresses Mu Song as 네 녀석 while assigning him punishment. |
| 마삼보 | 제갈풍 | hostile opponents | you; bastard | insulting and threatening | Ma Sanbao threatens to tear Zhuge Feng and his family apart. |
| 백연 | 마삼보 | former imperial colleagues; Baek Yeon addresses a former servant of the throne | Eunuch Ma | formal title | Baek Yeon recognizes him as 마 태감. |
| 천자 | 마삼보 | Emperor addressing his former servant and traitor | traitor | familiar and imperious | The Son of Heaven asks whether Ma Sanbao enjoyed his rebellion. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 1134
- **Aliases:** Blood Envoy
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard, a martial arts instructor to the Emperor, and the Blood Envoy who helped the fourth prince seize the throne and led the purge.
- **Personality:** Politically assured and controlled, Baek Yeon prioritizes the Great Nation and its people over Murim’s interests, and is willing to dismantle Murim if it becomes a threat to them.
- **Voice:** Baek Yeon speaks with measured formality in public, but with the Emperor he shifts easily into familiar teasing and earnest, eloquent praise.
- **Relationships:** Baek Yeon is the Emperor’s trusted confidant and former martial arts instructor, and he is entrusted with protecting Zhu Bao; he commands the Embroidered Uniform Guard and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1134
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 1081
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 1128
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered, but grieves deeply for fellow Beggars’ Sect disciples and defends those who risk their lives for others.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun, and shares a blunt, teasing friendship with Taekyung.

### Hak Woo.md

# Hak Woo (학우)

- **Safe through:** Chapter 1078
- **Aliases:** Kunlun Cloud Dragon
- **Role:** Hak Woo is the Kunlun Sect's greatest young prodigy and is known as the Kunlun Cloud Dragon.
- **Personality:** He is wary, easily intimidated by threats to his hair, and eager to avoid unnecessary confrontation.
- **Voice:** He speaks politely and defensively, frequently using Daoist invocations.
- **Relationships:** Jin Taekyung is his former rival and can pressure him into leaving, while Ju Hwaran is an acquaintance he addresses formally.

### Jang Sam.md

# Jang Sam (장삼)

- **Safe through:** Chapter 1129
- **Aliases:** Killing Ghost
- **Role:** Jang Sam is a bandit chief who abruptly rose from Level 40 to Level 60 and attacked Taekyung while apparently irrational; he is currently unconscious and being taken to the Nangong Family.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** No relationships established.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1134
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; the Helper first taught Taekyung to circulate qi; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1134
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 1134
- **Aliases:** None
- **Role:** Ma Sanbao is a sorcerer and Supreme Peak martial artist, former disciple of the Eastern Heaven Demon Lord, and servant of the Lord of Heaven, whose power lets him raise the dead within limits and command beasts with ritual bells.
- **Personality:** He is ambitious and confident in his usefulness to the Lord of Heaven, dismissive of his former master’s weakness, and pragmatic about losing subordinates.
- **Voice:** He speaks in measured, courteous language and uses calm repetition, feigned agreement, and procedural reminders to steer conversations while keeping sensitive details guarded.
- **Relationships:** Ma Sanbao served the Eastern Heaven Demon Lord as his disciple and now serves the Lord of Heaven; he was once an imperial servant before rebelling against the Son of Heaven.

### Masked Man.md

# Masked Man (복면인)

- **Safe through:** Chapter 873
- **Aliases:** None
- **Role:** The Masked Man is the Southern Heaven Demon Empress's trained hunting dog; after being crushed beneath a massive boulder in the Inner Palace ruins, he remains capable of twitching while awaiting his abnormal recovery.
- **Personality:** The Masked Man is emotionless, silent, and indifferent to extreme bodily damage.
- **Voice:** No spoken voice has been established.
- **Relationships:** He serves the Southern Heaven Demon Empress as her hunting dog; his identity and relationship with the Great Snow Fiend remain unknown.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 1098
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan, belongs to the Yangtze River Channel League's moderate faction, and is an exceptionally skilled ship captain.
- **Personality:** Ambitious and domineering, yet deeply troubled by needless bloodshed; he will defy his Master when conscience demands it.
- **Voice:** Blunt and direct, with dry barbs even when addressing his Master respectfully.
- **Relationships:** Mu Song is Pa Ryun’s second Disciple and the Water Dragon Stronghold Lord; he opposes Pa Ryun’s orders to kill captured imperial troops and credits Jin Taekyung with showing him that even a bandit can pursue chivalry.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 1128
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s thirteen-year-old younger brother, an exceptionally skilled young swordsman, and the newly appointed Crown Prince.
- **Personality:** Earnest and compassionate, he takes responsibility for others’ suffering and dreams of a peaceful age founded on justice, care for the people, wise counsel, and accountability, even when doing so demands personal sacrifice.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Zhu Bao is the Emperor’s younger brother and Crown Prince, and Hong Jin has been his steadfast caretaker since childhood. He admires Jin Taekyung and calls him a friend; his compassion for the Eastern Heaven Demon Lord reflects the different path made possible by those who supported him.

### Zhuge Feng.md

# Zhuge Feng (제갈풍)

- **Safe through:** Chapter 1134
- **Aliases:** Crouching Dragon Guest
- **Role:** Zhuge Feng is the current Family Head of the Zhuge Clan and father of its Lesser Family Head, Zhuge Gyun.
- **Personality:** Analytical, disarmingly casual, eccentric, and inventive; he treats comfort and time as principles while delivering grave intelligence with unsettling directness.
- **Voice:** Clear, calm, polished, and conversational, with understated humor and pointed questioning.
- **Relationships:** Zhuge Gyun is his son, and Zhuge Gonghu was his grandfather.

## Korean source

```text
＃1135화



흐릿한 달빛이 비쳐 오는 언덕 위, 홀연히 나타난 그의 모습은 실로 이질적이었다.

비단 마삼보 뿐만이 아닌, 그들 모두에게.

그리고 다음 순간, 창백한 입술 사이로 흘러나온 음성에는 앞서 그들이 느낀 이질감의 정체가 담겨 있었다.

“그래, 역적질은 할 만하던가.”

잔잔한 수면처럼 평온한 어조.

하지만 그 안에 담긴, 군림하는 자만이 지닐 수 있는 위압감.

그것은 품격(品格)이었다.

어둠에 녹아든 새카만 장삼과 깊게 눌러쓴 죽립으로도 미처 가리지 못한.

화려하기 그지없는 곤룡포(袞龍袍)나 면류관(冕旒冠) 없이도 자연스럽게 배어 나오는, 그야말로 타고난 품격.

“오랜만이구나, 마 내관(內官).”

까마득한 높이에서 굽어보는 듯한 하대.

생각지도 못한 천자(天子)의 등장에, 내심 신음을 삼킨 마삼보가 가라앉은 음성으로 입을 열었다.

“예까지 어인 일이시오, 황상(皇上).”

천자가 담담하게 대꾸했다.

“긴히 처리할 일이 있어 와 보았지.”

“황도(皇都)를 비울 정도로 중요한 일이라 생각하시오?”

“희한하군. 왜 짐이 황도를 비워도 될 만큼 철저히 준비해 두었다고는 생각하지 않느냐?”

“……!”

“한낱 역적 따위가 황도의 안위를 걱정할 필요는 없지. 적어도 황도십이궁(黃道十二宮)이 지키고 있는 한은.”

침묵하는 마삼보를, 천자는 깊게 가라앉은 눈빛으로 응시했다.

황도십이궁.

황실을 수호하는 열두 명의 초절정 고수.

비록 동천마군을 중심으로 벌어진 반역 이후로 그 숫자가 몇 남지 않았으나, 지금처럼 이동진의 위치만 알고 있다면 그들과 휘하 금위군만으로도 차고 넘치는 전력이었다.

단, 어디까지나 적들이 황도를 친다는 가정하에서만.

“허장성세(虛張聲勢)는 그만두어라. 애당초 황도를 노릴 계획이었다면, 네놈과 짐이 이리 마주할 일은 벌어지지 않았을 테니. 그렇지 않느냐?”

정곡을 찌르는 한 마디에, 마삼보는 조용히 메마른 입술을 핥았다.

천자의 말은 사실이었다.

괴조(怪鳥)들로부터 정보를 입수한 그 순간, 마삼보는 황도라는 두 글자를 뇌리에서 깨끗이 지웠다.

만약 황도를 함락시키고 천자를 손에 넣는다면 천하를 무릎 꿇릴 수 있겠지만, 그보다는 이미 크나큰 전력의 공백이 드러난 중원 무림이 훨씬 탐나는 먹잇감이었으니까.

빠르고 편한 길을 놔두고 어려운 길을 택할 이유는 없었다.

그리고, 이와 같은 마삼보의 착각이야말로 가장 커다란 패착(敗着)이었다.

“……제법이구나, 주체(主體).”

천자의 본명을 입에 담는 것은 그 자체로 대역죄.

하지만 마삼보는 아랑곳하지 않고 말을 이었다.

그는 지금껏 단 한 순간도 스스로를 천자의 신하라 생각하지 않았으니.

다만 더는 물러설 길이 없는 이 상황 속에서, 아직 해결되지 않은 의문에 대한 답을 얻고자 할 따름이었다.

“도대체 어찌 알았느냐. 이곳의 위치를.”

그리고 그 물음에 답한 것은, 천자가 아닌 제갈풍이었다.

“이 년.”

“뭐?”

“아, 욕한 것이 아니니 오해는 말게. 뭐 자네가 고자라는 사실은 알고 있지만, 그래도 겉보기에는 확실히 년이 아니라 놈이니까.”

얼굴이 딱딱하게 굳은 마삼보를 향해 빙긋 웃은 제갈풍이 재차 입을 열었다.

“이동진의 존재를 알아차린 후부터 온 천하를 이 잡듯이 뒤졌지. 정확히는 이 년이 아니라 일 년 반 정도겠군.”

“……!”

“오, 그래. 나도 처음 이 미친 짓거리를 시작할 때는 딱 지금 자네와 같은 표정이었지. 가솔들의 경우에는 더 안 좋았고, 검왕(劍王)과 권왕(拳王) 선배는 내 목을 조르려고 들더군. 지금은 돌아가시고 없는 도왕(刀王)께서는 그보다도 심했어.”

안 좋은 기억을 떠올리며 목덜미를 쓰다듬는 제갈풍의 모습을, 마삼보는 믿을 수 없다는 듯이 바라보았다.

“뒤졌다고? 그것도 십왕(十王)들까지 동원해서?”

“어떤 심정인지 충분히 이해하네. 하지만 뭐, 우리가 그것 말고 달리 뭘 할 수 있었겠나?”

제갈풍은 한숨과 함께 손에 쥔 학우선을 살랑살랑 흔들었다.

사실 처음 한두 달은 지옥이나 다름없었다.

아니, 그보다 더했다.

차라리 지옥에는 군데군데 유황불이라도 피어오르지, 그들은 끝없는 망망대해(茫茫大海) 한복판에 표류당한 기분이었으니까.

그러나 첫 결실을 보기까지는 그리 오래 걸리지 않았다.

“석 달 만에 한 곳을 발견했지. 안휘성의 황산(黃山) 깊숙이 숨겨져 있더군. 다행히 그다음부터는 찾는 속도가 훨씬 빨라졌어.”

그 모든 것은 매우 극비리에, 그것도 은영각(隱影閣)의 선별 과정을 통해 확실히 검증받은 이들만을 통해 진행되었다.

구파일방과 오대세가의 일원이라 할지라도 예외는 없었다.

아니, 설령 장문인이라 해도 다르지 않았다.

그들은 오직 한 사람, 무림맹주의 명령을 따랐고 각자에게 주어진 임무를 충실히 수행했다.

궁기방의 스승이자 개방의 방주인 만리추행(萬里追行)은 하오문과 함께 믿을 만한 수하들을 총동원하여 이동진이 존재할 만한 위치를 찾았고, 제갈세가와 은영각의 지자(智者)들은 그들이 가져온 정보를 바탕으로 더욱 구체적인 장소를 유추해 냈다.

“아무리 어려운 문제라도 풀이 방법을 안다면 능히 답을 얻어낼 수 있지. 다행히 이동진의 위치를 찾는 과정 역시도 이와 같더군.”

그것은 어릴 적부터 신동으로 이름 높았던 제갈풍에게도 매우 어려운 문제였지만, 그는 머지않아 풀이 방법을 알아냈다.

인적이 드물고 유독 기의 흐름이 강하며, 최소 수백의 인원을 수용할 수 있는 면적에 풀숲이 형성되지 않는 곳.

제갈풍은 이처럼 특정 조건을 갖춘 장소만을 선별했고, 그의 결정이 내려지면 제갈세가의 이름난 진법가들과 기감에 뛰어난 고수들이 직접 현장을 찾아 검증했다.

이를테면, 남궁세가의 태상가주인 창천검왕이나 권왕과 같은 초절정 고수들이.

“허나 아무리 애써도 부족함이 있더군. 나름대로 적지 않는 수였지만, 우리만으로 기밀을 철저히 유지하면서 이 드넓은 구주(九州)를 완벽하게 뒤지기에는 무리였거든.”

한 치의 실수도 용납되어서는 안 되는 일이었다.

아무리 단단한 성벽이라 해도, 붕괴는 아주 작은 하나의 균열에서 시작되는 법이니까.

그런 의미에서 이동진은 그 자체로 거대한 화약고(火藥庫)나 다름없었다.

단 하나만 터져도 천하를 불길에 휩싸이게 만들 수 있는.

그러나 불과 몇 달 전 찾아온, 생각지도 못했던 도움의 손길에 제갈풍은 마음 한구석에 남아 있던 마지막 불안감마저 떨쳐낼 수 있었다.

“어느 높으신 분이 맹주께 그러셨다는군. 도울 수 있는 일이 있다면 무엇이든 하시겠노라고. 덕분에 아주 큰 도움이 됐지.”

제갈풍의 말에, ‘어느 높으신 분’이 입을 열었다.

“제일 높으신 분, 이 맞지 않겠나?”

“아, 결례를 용서하십시오. 폐하.”

“물론 용서할걸세. 대역죄만 아니라면 무엇이든.”

멍하니 제갈풍과 천자가 주고받는 대화를 듣고 있던 마삼보는 이를 악물었다.

‘당했다, 그것도 완벽하게.’

중원의 적들은 바로 이 순간만을 위해 인내해 왔던 것이 분명했다.

찾아낸 이동진을 폐쇄할 능력이 있음에도 방치했고, 그 대신 완벽한 덫을 깔았다.

사냥감이 군침을 흘리며 달려들 수 있도록.

그리하여 마지막 근심마저 완전히 뿌리 뽑을 수 있도록.

“앞서 보낸 선발대도 이런 방식으로 처리한 거였나?”

마삼보의 물음에 제갈풍은 부드럽게 학우선을 흔들었다.

“도착과 동시에 화산파(華山波)에 의해 전멸당했지. 그 빈자리는 맹주께서 이끄시는 무림맹의 정예가 채웠고.”

“우리가 입수한 정보에는 분명 두 도적 놈들과 합류했다는 것이었는데.”

“뭐 그리 어렵겠나. 비슷한 머릿수에 흑의(黑衣)만 걸치면 되는 일인데. 그에 대한 소문은 알아서 퍼져 나가기 마련이지. 실제로도 그랬고.”

녹림맹과 장강수로맹에 합류했어야 할 일만의 광신도들은 그렇게 죽었다.

장강수로맹의 선박에 몸을 싣기도 전에.

그리고 해상왕 파륜은 그 사실을 철저히 숨겼다.

그가 자신의 제자인 선화아(船火兒) 무송을 제압한 것 또한, 어디까지나 기밀을 지키려는 방편이었을 뿐이었다.

사전에 계획을 듣지 못한 제자가 정의감에 불타 제멋대로 움직인다면, 애써 분리까지 해 둔 후미의 선박에 타고 있는 자들이 무림맹 소속이라는 사실이 알려질 위험이 있었으니까.

“하지만 그전에 수적 놈들이 격파한 수백 척의 함대는 도대체…….”

일순간, 마삼보는 문득 말꼬리를 흐렸다.

서늘한 미소를 머금고 있는 천자의 모습이, 마지막 남은 의문에 대한 답을 알려 주었기 때문이었다.

“과연, 그렇게 된 거였나.”

마침내 모든 것을 깨달은 마삼보는 자신도 모르게 헛웃음을 터트렸다.

잠시 잊었다.

천자의 저 창백한 피부 속에는, 뜨겁고 붉은 피 대신 차가운 철혈(鐵血)이 흐른다는 사실을.

“지금쯤 황궁의 뇌옥이 텅 비었겠군. 주체, 네놈의 농간이었느냐?”

천자가 담담하게 대꾸했다.

“그간 나라를 좀먹던 역적들이 워낙 많다 보니, 일일이 죽이는 것도 일이더군. 나름대로의 값을 치렀으니 그자들에게도 썩 나쁜 최후는 아니었을 것이다.”

동천마군의 반란 직후 벌어진, 대국 역사상 두 번 다시 없을 대숙청(大肅淸).

그중 아직까지 살아남아 처분을 기다리고 있던 수많은 죄인들에게 천자는 제안했다.

법에 따라 일족과 함께 죽음을 맞거나 평생 노비로 살아갈 것인지. 혹은 가문이 진 오명을 조금이라도 벗겨 낼 것인지.

당연하게도 대부분의 죄인들은 후자를 택했다.

그들은 전신을 속박하던 사슬과 칼을 벗고, 떨리는 손으로 창칼을 받아 대국의 선박에 올랐다.

자신들의 이 선택으로 피붙이 중 누군가는 살아남아 가문을 이으리라는, 천자의 약속을 끊임없이 마음속으로 되새기며.

“그래, 어쩐지 예상했던 것보다도 쉽게 풀린다 했었지. 제아무리 썩어 빠졌어도 그 정도의 대패(大敗)를 겪는 건 확실히 이상한 일이었으니.”

애당초 훈련받은 군인이 아니었으니, 수백의 함대와 화포가 있다 해도 전멸은 당연지사.

그 수많은 죄인들을 먹잇감으로 던져 준, 오직 천자만이 벌일 수 있는 이 대담한 계획의 전말을 알게 된 마삼보는 실소할 수밖에 없었다.

아니, 그래야만 했다.

이미 모든 것을 포기한 듯한 실없는 웃음이 있어야, 자신에게 남은 마지막 기회를 감출 수 있었으니까.

‘아직, 아직 끝나지 않았다.’

비록 입은 웃고 있으나, 눈은 아니다.

마삼보는 깊게 가라앉은 시선으로 빠르게 주위를 훑었다.

사방을 둘러싼 언덕 위, 우거진 풀숲 사이로 조용히 고개를 내밀고 있는 무수한 화살촉들을 보았고 숨죽인 채 자신의 명령을 기다리는 수하들의 호흡을 느꼈다.

‘병력 차는 최소 다섯 배. 혹은 그 이상.’

하지만 상관없다.

이미 만반의 준비를 끝마친 적들 중 한 명.

단 한 명만 사로잡는다면 이 절망적인 상황을 충분히 뒤집을 수 있었다.

아니, 어쩌면 뒤집는 것을 넘어 모든 것을 손에 넣을지도 몰랐다.

천자란, 그런 존재니까.

더군다나 이미 마삼보에게는, 그들에게는 더 이상 남은 선택지가 없었다.

“지금-!”

모든 것은 한순간이었다.

마삼보가 거대한 외침과 함께 지면을 박차며 솟구친 것도. 

팽팽하게 당겨져 있던 활시위가 일제히 화살을 쏘아 보낸 것도.

그리고.

슈확!

그 빛살 같은 속도를 따라가지 못하고 스쳐 지나간 무수한 화살이 지면을 뒤덮기도 전, 마삼보의 머리 위 허공에서 낮게 깔린 파공성이 울려 퍼진 것도.

‘무영(無影)……!’

마삼보는 어느새 자신의 앞을 가로막은 복면인의 모습에 이를 악물었다.

그다.

얼굴조차 제대로 본 적 없지만, 존재만은 알고 있었던 천자의 암중호위(暗中護衛).

그림자조차 드러내지 않는다는 황실 제일의 살수가, 흐릿한 달빛 아래에서 강기에 휩싸인 단검을 내리긋고 있었다.

어디까지나, 마삼보가 예상했던 대로.

퍼걱!

섬뜩한 파육음과 함께 팔뚝을 파고드는 검신.

그러나 마삼보는 아랑곳하지 않고 반쯤 잘려 나간 왼손을 뻗어 무영을 후려쳤다.

콰드득!

강맹한 장력(掌力)에 의해 튕겨 나가는 무영의 모습을 뒤로한 채, 마삼보는 발끝에 공력을 실어 터트렸다.

퍼엉!

마삼보는 한 줄기의 유성이 되어 언덕을 향해 내리꽂혔다. 

황실에서의 혈전 이후 더욱 강해진 백환강시공(魄環僵尸功)은 고통도, 두려움도 잊게 만들기에 충분했다.

“주체-!”

마삼보는 포효했다. 

다음 순간 사각에서 쏘아진 십여 대의 화살이 전신 곳곳을 파고들고, 곧이어 제갈풍과 백연이 앞을 가로막았지만 시체처럼 회백색으로 물든 동공은 오직 한 사람만을 향하고 있었다.

마지막으로 보았을 때와 같이, 병색이 완연한 창백한 얼굴을 한 천자를.

퍼걱, 푹! 

콰드드득!

이미 강시나 다름없는 몸에서 흘러나올 핏물은 없었다. 잘려 나간 살점과 뼈마디만 흩날릴 뿐.

다만, 필사적인 의지가 있었다.

서걱!

백연이 휘두른 언월도가 마삼보의 왼팔의 어깻죽지를 파고드는 동시에 비스듬히 상반신을 갈라 낸 그 순간.

콰득!

하나밖에 남지 않은 마삼보의 손이, 마침내 원하던 것을 움켜쥐었다.

다름 아닌 천자의 목줄기를.

“모두, 멈춰라.”

일순간 찾아온 정적.

천자가 허리춤의 검을 뽑기도 전, 벼락처럼 그를 제압한 마삼보는 흐릿하게 웃었다.

그리고 점혈당한 천자의 귓가에 속삭였다.

“고맙군. 네놈이 친히 여기까지 와 준 덕분…….”

푹.

마삼보는 문득 눈을 깜빡였다.

어째서일까.

왜, 어떻게 이미 점혈 당한 천자가 움직일 수 있는 것일까.

그리고 이제야 가까이에서 마주한 천자의 얼굴은, 어찌하여 이토록 자신의 피부색과 닮아 있을까.

“……너. 설마.”

우득.

마삼보의 가슴 정중앙을 관통한 손을 천천히 비틀며, 천자가 입을 열었다.

“몇 달 전, 한 사람에게서 아주 큰 선물을 받았지. 자네도 잘 아는 무언가를.”

“……!”

“고심하고, 또 고심했다. 그것은 축복인 동시에 저주나 다름없었으니.”

하지만 천자의 고민은 그리 길지 않았다.

하나밖에 남지 않은 혈육이자, 천하를 물려받을 유일한 후계자가 그에게 한 부탁 때문이었다.

“천수(千壽)를 누리라더군. 천자가 아닌 가족으로서, 앞으로도 오랫동안 함께하고 싶다고.”

상산왕 주표, 아니 황태제(皇太弟) 주표의 진심에 천자는 선택했다.

금기를 범해서라도, 언젠가 이 결정을 후회하게 될 날이 오더라도 허락되는 한 자신의 아우와 함께하겠노라고.

그리고 그의 선택이, 지금의 이 순간을 만들었다.

“이제야 알았다. 진태경이 백환강시공을 준 이유를. 그건 짐뿐만이 아니라…… 또 다시 홀로 남게 될 아우를 위해서였다.”

그 순간.

“대국의 법도에 따라, 역적을 벌하노라.”

콰드드득!

생애 마지막이 될 천자의 음성과 함께, 마삼보가 바라보던 세상이 까맣게 물들었다.
```

## Final English reading copy

```markdown
# Chapter 1135

On a hill washed in faint moonlight, his sudden appearance seemed utterly out of place.

Not just to Ma Sanbao. To all of them.

And the next moment, the voice that slipped between pale lips revealed the source of that unease.

“So, traitor—have you enjoyed your rebellion?”

His tone was as calm as still water.

But within it lay the imposing authority only a ruler could possess.

It was dignity.

A dignity that even a black robe blending into the darkness and a bamboo hat pulled low couldn’t conceal.

A born dignity that shone through naturally, without the need for an elaborate imperial robe or a crown of hanging beads.

“Long time no see, Eunuch Ma.”

He spoke down to Ma Sanbao as if gazing from a dizzying height.

At the unexpected appearance of the Son of Heaven, Ma Sanbao stifled a groan, then spoke in a low voice.

“What brings Your Majesty all the way here?”

“I came to take care of some urgent business.”

“Was it important enough to leave the Imperial Capital?”

“How curious. Why don’t you think I prepared thoroughly enough to leave the capital?”

“……!”

“A mere traitor like you needn’t worry about the capital’s safety. Not while the Twelve Palaces of the Zodiac are guarding it.”

The Son of Heaven fixed his deep, sunken gaze on Ma Sanbao, who had fallen silent.

The Twelve Palaces of the Zodiac.

Twelve Supreme Peak masters who protected the imperial household.

Though few remained after the rebellion led by the Eastern Heaven Demon Lord, if they knew the location of the Moving Formation, they and the Imperial Guards under their command were more than enough.

But only on the assumption that their enemies would attack the capital.

“Stop bluffing. If you’d planned to strike the capital in the first place, you and I wouldn’t be facing each other like this. Isn’t that right?”

The remark hit home. Ma Sanbao quietly licked his dry lips.

The Son of Heaven was right.

The instant he received information from the strange birds, Ma Sanbao had erased the Imperial Capital from his mind.

If he captured the capital and took the Son of Heaven, he could bring the world to its knees. But the Murim of the Central Plains, already left with a massive gap in its defenses, was far more tempting prey.

There was no reason to take the hard road when an easier, faster one lay open.

And that mistake had been Ma Sanbao’s greatest blunder.

“……Not bad, Zhu Di.”

Speaking the Son of Heaven’s personal name was high treason in itself.

Ma Sanbao didn’t care. He continued.

He had never once thought of himself as the Son of Heaven’s subject.

Now, with nowhere left to retreat, he wanted only an answer to the question that still remained.

“How did you find out where this place was?”

It wasn’t the Son of Heaven who answered, but Zhuge Feng.

“Two years.”

“What?”

“Ah, don’t misunderstand. I wasn’t calling you a bitch. I know you’re a eunuch, but you look unmistakably like a man.”

Zhuge Feng smiled at Ma Sanbao, whose face had stiffened, and continued.

“Since we discovered the Moving Formation, we’ve turned the whole world upside down looking for them. Not quite two years—more like a year and a half.”

“……!”

“Oh, right. When I first started this lunatic undertaking, I had exactly the same look on my face as you do now. My retainers looked even worse. Even my seniors, Sword King and Fist King, tried to strangle me. The late Blade King was worse still.”

Zhuge Feng rubbed the back of his neck, recalling those unpleasant memories. Ma Sanbao stared at him in disbelief.

“You searched for them? And even brought in the Ten Kings?”

“I understand how you feel. But what else could we have done?”

With a sigh, Zhuge Feng gently waved the feather fan in his hand.

The first month or two had been nothing short of hell.

No, worse than that.

At least hell had sulfur fires burning here and there. They’d felt like they were adrift in the middle of an endless ocean.

But it hadn’t taken long to see their first results.

“We found one after three months. It was hidden deep in Mount Huang in Anhui. Fortunately, after that, we found the others much faster.”

The entire operation had been conducted in the utmost secrecy, using only people vetted through the Hidden Shadow Pavilion’s screening process.

Even members of the Nine Sects and One Gang and the Five Great Families were no exception.

Not even a Sect Leader was exempt.

They answered to one person alone—the Alliance Leader—and faithfully carried out the tasks assigned to them.

Myriad-Mile Pursuit, Gung Gibang’s master and the Beggars’ Sect Leader, mobilized all his trusted subordinates alongside the Lower District Sect to find places where a Moving Formation might be located. The wise men of the Zhuge Clan and the Hidden Shadow Pavilion then used the information they brought back to narrow down the locations.

“No matter how difficult the problem, if you know how to solve it, you can find the answer. Fortunately, finding the Moving Formations worked the same way.”

It had been an extremely difficult problem even for Zhuge Feng, who had been renowned as a prodigy since childhood. But before long, he had worked out how to solve it.

Places where few people ventured, the flow of qi was unusually strong, the area could hold at least several hundred people, and grass didn’t grow.

Zhuge Feng selected only places that met those specific conditions. Once he made his decision, famed formation masters from the Zhuge Clan and experts with an exceptional Qi Sense went to investigate in person.

Among them were Supreme Peak masters like the Azure Sky Sword King, Grand Family Head of the Nangong Family, and the Fist King.

“But no matter how hard we tried, it wasn’t enough. We had a fair number of people, but we couldn’t thoroughly search this vast Nine Provinces while keeping the secret completely safe.”

Not a single mistake could be allowed.

Even the sturdiest wall could begin to collapse with one tiny crack.

In that sense, the Moving Formations were nothing less than vast powder kegs.

One explosion could set the whole world ablaze.

But a few months ago, help had arrived from an unexpected source. With it, Zhuge Feng could finally put to rest the last of his worries.

“I heard a very high-ranking person told the Alliance Leader that they would do anything they could to help. That was a tremendous help.”

At Zhuge Feng’s words, the “very high-ranking person” spoke up.

“Wouldn’t you say the highest-ranking person?”

“Ah, forgive my discourtesy, Your Majesty.”

“Of course I forgive you. Anything but high treason.”

Ma Sanbao had been listening blankly to the exchange between Zhuge Feng and the Son of Heaven. Now he clenched his teeth.

*They got me. Completely.*

The enemies in the Central Plains must have been waiting for this very moment.

Even though they could have shut down the Moving Formations they found, they’d left them alone and laid a perfect trap instead.

A trap their prey would rush into, salivating.

A trap that would root out even their final concern.

“Was that how you dealt with the advance party, too?”

Zhuge Feng gently waved his feather fan.

“They were wiped out as soon as they arrived, by the Huashan Sect. The Murim Alliance’s elite, led by the Alliance Leader, filled their ranks.”

“The information we obtained clearly said they’d joined up with those two bandit bastards.”

“What’s so hard about that? We put on black clothes and got together a similar number of people. Rumors about it were bound to spread on their own. And they did.”

The ten thousand fanatics who were supposed to join the Green Forest Alliance and the Yangtze River Channel League had died before ever boarding the league’s ships.

And Seafaring King Pa Ryun had kept the truth thoroughly concealed.

Even the fact that he had subdued his Disciple, Ship-Fire Boy Mu Song, had only been a way to protect the secret. If his Disciple, unaware of the plan, had acted on his sense of justice, he might have exposed the fact that those aboard the rear ships—deliberately kept separate—belonged to the Murim Alliance.

“But then what about the hundreds of ships the river bandits supposedly destroyed……?”

Ma Sanbao trailed off.

The Son of Heaven’s cold smile had given him the answer to his last question.

“I see. So that’s what happened.”

At last, Ma Sanbao understood everything. A hollow laugh slipped from his lips.

He’d forgotten for a moment.

Beneath the Son of Heaven’s pale skin, instead of hot, red blood, ran cold iron and blood.

“The underground prison in the palace must be empty by now. Zhu Di, was this your doing?”

The Son of Heaven answered in an even tone.

“There were so many traitors who had been eating away at the nation that killing them one by one became a chore. They paid a price of their own, so it wasn’t such a bad end for them.”

In the aftermath of the Eastern Heaven Demon Lord’s rebellion came a purge without precedent in the history of the Great Nation.

Among the many criminals who had survived it and awaited their punishment, the Son of Heaven made an offer.

They could die with their families, as the law required, or live out their lives as slaves. Or they could do something to lift even a little of the stain from their family name.

Naturally, most chose the latter.

They were freed from the chains and swords that had bound them, and with trembling hands, accepted spears and blades before boarding the ships of the Great Nation.

They clung to the Son of Heaven’s promise in their hearts: that this choice would let at least one of their kin survive and carry on the family name.

“Right. No wonder it all went more smoothly than I expected. Even if their forces were rotten to the core, it was strange for them to suffer such a crushing defeat.”

They were untrained soldiers. Even with hundreds of ships and cannons, their annihilation had been inevitable.

Learning the full details of this audacious plan, one only the Son of Heaven could have carried out—using so many criminals as bait—Ma Sanbao could only laugh in disbelief.

No. He had to.

Only a hollow laugh that made it seem he’d given up on everything could hide the last chance he had left.

*Not yet. It’s not over yet.*

His lips were smiling, but not his eyes.

Ma Sanbao quickly swept his sunken gaze around.

On the hills surrounding them, he saw countless arrowheads quietly poking through the thick grass. He sensed the breathing of his subordinates, holding their breaths as they waited for his command.

*We’re outnumbered by at least five to one. Maybe more.*

But it didn’t matter.

If he could capture just one of the enemies who had already made every preparation, he could turn this desperate situation around.

No—he might do more than turn it around. He might seize everything.

That was what the Son of Heaven represented.

Besides, Ma Sanbao and his men had no other choice left.

“Now—!”

It all happened in an instant.

Ma Sanbao’s mighty shout as he kicked off the ground and shot upward.

The tightly drawn bowstrings releasing their arrows all at once.

And—

Before the countless arrows that couldn’t keep up with his lightning speed had even finished sweeping across the ground, a low whistle of air split through the space above Ma Sanbao’s head.

*No Shadow……!*

Ma Sanbao clenched his teeth at the masked figure who had suddenly appeared in his way.

It was him.

Ma Sanbao had never seen his face clearly, but he knew he existed: the Son of Heaven’s hidden bodyguard.

The imperial household’s greatest assassin, who never even revealed his shadow, was bringing down a dagger wrapped in Force beneath the faint moonlight.

Just as Ma Sanbao had expected.

*Shhk!*

With a gruesome sound of flesh being cut, the blade sank into his forearm.

But Ma Sanbao didn’t flinch. He thrust out his half-severed left hand and struck No Shadow.

*Crack!*

No Shadow went flying from the force of the blow. Ma Sanbao drove internal energy into the tips of his feet and released it.

*Boom!*

Ma Sanbao shot toward the hill like a falling star.

The White Illusion Jiangshi Art, made even stronger after the bloody battle at the imperial palace, was enough to make him forget pain and fear.

“Zhu Di!”

Ma Sanbao roared.

A dozen or so arrows shot from his blind spots and buried themselves throughout his body. Then Zhuge Feng and Baek Yeon blocked his path. But Ma Sanbao’s corpse-gray eyes remained fixed on just one person.

The Son of Heaven, his pale face still showing the unmistakable signs of illness, just as it had the last time Ma Sanbao saw him.

*Shhk! Thud!*

*Crack!*

There was no blood left to spill from a body that was already no different from a jiangshi. Only chunks of flesh and pieces of bone flew through the air.

But his will remained, desperate and unyielding.

*Slash!*

Baek Yeon’s crescent-bladed polearm sank into Ma Sanbao’s left shoulder and sliced diagonally through his upper body.

*Crack!*

Ma Sanbao’s one remaining hand finally grasped what he wanted.

The Son of Heaven’s throat.

“Everyone, stop.”

Silence fell all at once.

Before the Son of Heaven could even draw the sword at his waist, Ma Sanbao had pinned him down like a bolt of lightning. He gave a faint smile.

Then he whispered into the ear of the Son of Heaven, whose pressure points he had struck.

“Thank you. You came all the way here yourself, so—”

*Thud.*

Ma Sanbao blinked.

Why?

How could the Son of Heaven move after his pressure points had been struck?

And why, now that he was finally face-to-face with him, was the Son of Heaven’s skin so similar to his own?

“……You. Don’t tell me—”

*Crack.*

The Son of Heaven slowly twisted the hand that had pierced the center of Ma Sanbao’s chest and spoke.

“A few months ago, I received a great gift from someone. Something you know well.”

“……!”

“I thought long and hard about it. It was as much a curse as it was a blessing.”

But the Son of Heaven’s deliberation hadn’t lasted long.

His only remaining blood relative, the sole heir who would inherit the realm, had made him a request.

“He told me to live a thousand years. Not as the Son of Heaven, but as family—as someone he wanted to stay with for a long time.”

Moved by Prince Shangshan Zhu Bao’s sincerity—no, Imperial Younger Brother Zhu Bao’s—the Son of Heaven made his choice.

Even if it meant breaking a taboo. Even if he might one day regret it, he would stay with his younger brother for as long as he was allowed.

And that choice had brought them to this moment.

“Now I understand why Jin Taekyung gave me the White Illusion Jiangshi Art. It wasn’t only for me…… It was for my brother, so he wouldn’t be left alone again.”

At that moment—

“By the law of the Great Nation, I punish this traitor.”

*Crack!*

As Ma Sanbao heard the Son of Heaven’s voice for the last time, the world before his eyes went black.
```
