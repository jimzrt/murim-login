<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0481.txt",
      "sha256": "b083e75b553078d25a663f88d17d976929607681d588ac69d844b685d0fbba02",
      "bytes": 13984
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "3fdb43365eddb59270531e2e78e82a21c827a93cd26ee39f3e6cabb1d30bc828",
      "bytes": 3200
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "713b279c2e5f8b02dc152deb489c2f754939729f8b9f8aba1bcd2d3854012735",
      "bytes": 153963
    },
    {
      "path": "characters/Dongting Fisherman.md",
      "sha256": "eaae03f588aea3aa757ca35f5f459658a02483cb0f130dcdf460d37942f84330",
      "bytes": 778
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "32fe80a143b230a9cb0934ce3917696b965648657ba71d567d7257621eee5d45",
      "bytes": 662
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "7aa35d4006db39f999b57d78cf695e4c213a0d0ffde9766873d05822232690cd",
      "bytes": 918
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "b50f6999373ebf3633a1883025103140bfd3274641d3b95221dce6ac14f863cc",
      "bytes": 1542
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "95d120e2f3fb75368847b2e5d3c244b0da4a8e5db53048f6e67c00f08b88dec9",
      "bytes": 1777
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "091f1ed7f7492bbaac19cfb9253edf25a040f0aa19b40b17f7a23328550643bc",
      "bytes": 622
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "43a1abd143aca852440fe1ca162e4a68e22419b69d09676fa8a9ad462fdf2d5b",
      "bytes": 771
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8f4fe4c30c5acce105935edec058ad638164a53867808030053f6f9d3f99ad97",
      "bytes": 148964
    }
  ],
  "estimated_tokens": 12619
}
-->

# Durable State Update — Chapter 481

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 481. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 481. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 481,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 481,
    "continuity_sources": [481],
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
    "The Water God Dragon died after regaining its reason and giving Taekyung its purified Origin Essence, which humans call an inner core.",
    "The dragon's Memory Fragment showed its five-hundred-year history, including its benevolent rule of Dongting Lake and its sacrifice to contain the Gate's demonic qi.",
    "Taekyung identifies Honglan as the person who corrupted the benevolent Dongting Lake imugi and used it to kill many people.",
    "Honglan's silver hairpin carries a faint scent and was found in Taekyung's hair after the Memory Fragment ended.",
    "Honglan can enthrall people by seizing their emotions and souls; Officer Song is currently under her control and obeying her command to change the ship's destination.",
    "Taekyung has completed the Corrupted Spirit Beast Surprise Quest and acquired substantial EXP, Fame, and two Levels.",
    "The Gate or rift that corrupted the Water God Dragon remains connected to unresolved questions involving demonic qi and Dark Heaven.",
    "Honglan's motives, her exact relationship to Dark Heaven, and the full extent of her role in the Hubei incidents remain unresolved.",
    "Gwak Bongchul is an elderly boatman from the Wuhan and Dongting Lake area who survived the Dongting Lake spirit's rampage and awakened after two days in Mungyeong's clinic.",
    "Gwak remembers the lake spirit's enraged roar, the deaths of thousands, and blood and corpses filling the Yangtze and Dongting Lake.",
    "Mungyeong has instructed Gwak to erase the incident from his memory and adopt a false account in which he collapsed after being summoned to Dongting Lake with government troops.",
    "Mungyeong warns that the Hubei City Lord may silence Gwak to suppress the incident and advises him to sell his boat and remain silent."
  ],
  "continuity_sources": [
    480
  ],
  "open_questions": [
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Did the Mutated Water Dragon destroy Donghu Stronghold and the related Yangtze River Channel League strongholds, and why was no Moving Formation trace left?",
    "Who created or controlled the Gate or rift that corrupted the Water God Dragon, and how is that power related to Dark Heaven?",
    "Why did Honglan corrupt the Water God Dragon and what is the full extent of her role in the Hubei incidents?"
  ],
  "safe_through": 480,
  "temporary_decisions": [
    "Render 광폭화 as Berserk and preserve the System Status distinction.",
    "Render 장수 돌침대 as Jangsu stone bed and 효자손 as hyojason, each with an explanatory footnote when used.",
    "Retain established jang and geun measurements, along with established renderings of live-fish sashimi and bone-in sashimi.",
    "Continue rendering 수염 as whiskers; distinguish Force, Sword Energy, Hellfire, and Water Breath.",
    "Render 원정 as Origin Essence, 내단 as inner core, and 꽃뱀 as flower snake with an explanatory footnote."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 신법     | **movement technique**                           |                                                       |
| 영약     | **elixir**                                       |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 낭인     | **wandering martial artist**                     |                                                       |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 상태               | **Status**                     |
| 태원     | **Taiyuan**            |
| 노부      | **this old man / I**                                            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 동정어옹 | **Dongting Fisherman** | Publicly condemned the Yangtze River Channel League and disappeared three days before this chapter. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 평화 | **Peace Guild** | Guild name. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 국밥 | **gukbap** | Korean dish of rice served in hot soup; footnoted in the reading copy. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 둘리 | **Dooly** | Korean cartoon character referenced in the goodwill proverb. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 의생 | **medical apprentice** | Mungyeong's occupation. |
| 살수 | **assassin** | Professional killer considered as a possible suspect. |
| 괴력난신 | **supernatural powers** | Term for extraordinary and unnatural powers. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 해사방 | **Sea Serpent Society** | Hubei association formed by fishermen and boatmen; it was annihilated at Red Cliffs. |
| 적벽 | **Red Cliffs** | Site where the Sea Serpent Society's leaders and core members were killed. |
| 장강일도 | **Yangtze One Saber** | Hwang Chung's sobriquet. |
| 천령폭 | **Tianling Falls** | Dangerous waterway leading to Donghu Stronghold. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 사공 | **boatman** | Old boatman piloting the ferryboat. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 진태경 | 문경 | young_martial_artist_to_medical_apprentice | Young Hero | formal-polite | Taekyung addresses the non-martial Mungyeong as 소협 while praising his actions. |
| 문경 | 진태경 | young_passenger_to_younger_martial_artist | Young Hero | deferential | Mungyeong uses 소협 while asking Taekyung for help boarding the ship. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 홍란 | 진태경 | Lower District Sect courtesan to honored guest | honored guest | humble and formal | Introduces herself with 소녀 and addresses Taekyung as 귀인. |
| 진태경 | 사공 | passenger_to_boatman | Boatman | commanding | Taekyung orders the boatman to continue to the final site and asks how long the journey will take. |
| 진태경 | 동정어옹 | hostile interrogator confronting a suspected perpetrator | you | blunt informal and abusive | Taekyung addresses the Dongting Fisherman without honorifics and calls him a sibu-leol bastard. |
| 궁기방 | 사공 | passenger to ferryboatman | Boatman | direct and formal-polite | Addresses the old boatman as 사공 while challenging his refusal to sail. |
| 사공 | 진태경 | ferryboatman to honored martial guest | Great Hero | fearful and deferential | Repeatedly addresses Taekyung as 대협 while explaining the storm and the boat’s limits. |
| 진태경 | 수신룡 | hostile martial artist to monster | you, sibu-leol eel bastard | blunt, insulting, and fearless | Taekyung directly insults the emerged Water God Dragon before attacking it. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |

## Listed compact profiles

### Dongting Fisherman.md

# Dongting Fisherman (동정어옹)

- **Safe through:** Chapter 471
- **Aliases:** None
- **Role:** The Dongting Fisherman is a previous-generation Supreme Peak master whose water arts rival the Seafaring King; he joined Dark Heaven, committed the Dongting Lake massacre, and is now captured alive for interrogation.
- **Personality:** The Dongting Fisherman appears eerily emotionless and savage, eating live fish raw and reacting violently when provoked.
- **Voice:** Not established.
- **Relationships:** The Dongting Fisherman opposed the Yangtze River Channel League and was monitored by the Lower District Sect for several years after friction with it, while current records place him in Hubei Province.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 470
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung and uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and search for Dark Heaven’s Hubei forces.

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 479
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name while serving as Ju Wongong's singing courtesan.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** Honglan is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, lost her clan and parents overnight as a child, can respond to Taekyung through Sound Transmission, is the sole surviving eyewitness to the Dongting Lake attack who knows several possible locations of the Dongting Fisherman's hidden refuges, corrupted the benevolent imugi in Dongting Lake and used it to kill many people, and can enthrall people and command them.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 479
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, and pathologically afraid of water. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 477
- **Aliases:** Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple and the Fire Gate Clan's nineteenth successor, a Supreme Peak master who possesses the Heavenly Martial Physique and superhuman physical strength, has manifested Force, opened his Middle Dantian, crossed the wall into true mastery, can perceive the texture of qi well enough to sever layered magic, can resist high-level monster Fear through exceptional mental strength, is publicly recognized as an S-rank-level Hunter while formally retaining an A-rank license pending testing, and can command coordinated raids against powerful monsters.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate, student, and trusted manager of media and official arrangements, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, and Xiao Shen regards him as an older brother after Jin saved him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 477
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 480
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, having passed the Divine Physician title to his Disciple, and he has reached the Returned to Youth realm.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple; Jeok Cheongang is an old acquaintance, and Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃481화



끼이익, 탁.

뱃사공을 홀로 남겨 둔 채 방문을 닫은 문경은 내심 뇌까렸다.

‘이 정도면 충분하겠지.’

뱃사공은 살아온 세월이 적지 않아서인지, 생각했던 것보다 훨씬 눈치가 빨랐다.

비록 관부의 감시 속에서 살아야 하겠지만 쥐도 새도 모르게 변사체로 발견되는 것보다야 백배 낫다.

이미 호북성주와의 거래는 끝난 상태. 입에 자물쇠만 채운다면야 조용히 남은 여생을 보낼 수 있을 것이다.

아니, 괜히 입을 놀려 봤자 주위에서 미친 늙은이 취급받을 것이 뻔했다.

‘앞으로는 재물 걱정도 없을 테니 저 자에게도 썩 괜찮은 조건이겠지.’

문경은 문득 저 뱃사공이 화로 옆에 놓아둔 전낭(錢囊)을 발견하면 무슨 표정을 지을까 생각했다.

자신에게 전낭을 전해 달라 부탁하며 건넨 누군가의 한 마디도.



‘그래도 괜히 따라와서 죽을 뻔했는데, 생명 수당에 산재처리는 해 줘야죠.’



산재처리?

난생처음 들어 보는 해괴한 단어였으나 다시 생각해 보면 진태경이라는 놈은 늘 그랬다.

새파랗다 못해 샛노란 어린놈. 그리고 매번 놀랍게 만드는 놈.

‘도무지 알 수 없는 녀석이다.’

하나하나 열거하자면 끝도 없지만, 이번 일을 겪고 나니 더더욱 그런 생각이 굳혀졌다.

듣도 보도 못한 거대한 괴물 앞에서도 위축되기는커녕 더욱 미친 듯이 날뛰던 진태경의 모습을 떠올린 문경이 미간을 좁혔다.

‘타고난 담력? 그럴 수도 있겠지만 무언가…… 그래, 익숙해 보였다. 마치 닳고 닳은 백전노장처럼.’

그간 암천(暗天)을 상대하며 괴력난신이라 불리는 기이한 것들에 익숙해진 것일까.

아니면 진태경에게 누구도 모르는 비밀이 있는 것일까.

문경이 상념에 젖어 걸음을 옮기던 그때였다.

“송 의원님. 그 쳐 죽일 놈들이 잡혔다면서요?”

“어허, 쳐 죽일 놈이라니. 향이 너는 의녀(醫女)가 되어 어찌 그리 험한 말을…….”

여러 사람이 오가는 의방의 마당. 나이 지긋한 중년 의생의 말에 아직 약관도 되어 보이지 않는 의녀가 입을 삐죽 내밀었다.

“의녀는 사람 아닌가요. 그리고 그자들은 죽어도 싸요.”

“크흠, 언행을 삼가거라. 맞는 말이긴 해도 누가 들을까 겁난다.”

“저분 때문에 그러시는 거죠? 무슨 상관이에요. 어차피 멀어서 들리지도 않을 텐데.”

물론 의녀의 맘 편한 생각과는 달리, 문경은 주위에서 벌어지는 모든 소리와 행동을 빠짐없이 받아들이고 있었다.

이어지는 두 남녀의 대화 역시 마찬가지였다.

“송 의원님은 어떻게 생각하세요?”

“무엇을 말이냐?”

“아이, 참. 모르는 척하지 마시고요. 암천(暗天)의 사주를 받아 천인공노할 짓을 저지른 무림의 흑도인들 말고 뭐가 있어요?”

“나 같은 일개 의생이 무슨 할 말이 있겠느냐? 다만 이제라도 흉수들이 잡혔으니 천만다행으로 생각하고, 본분에 충실할 따름이지.”

“하지만 좀 이상하지 않아요? 적벽에서 침몰한 해사방의 배와 동정호에서 벌어진 참극. 그리고 천령폭 너머의 수적들에 얽힌 죽음까지 전부 그자들이 벌인 짓이라는 게.”

“이상하다니? 뭐가 말이냐?”

“그게 그러니까. 음. 황 언니 아시죠?”

“내가 아는 황 의녀를 말하는 것이냐?”

“네. 그 황 언니가 해 준 얘긴데요. 음.”

말을 하다말고 고개를 돌려 주위를 둘러보던 의녀가 까치발을 들고 속삭였다.

그래 봤자 문경에게는 천둥소리처럼 크게 들렸지만.

“지금 자기가 담당하고 있는 환자가 꽤 유명한 낭인인데, 그분이 그 얘기를 듣고 코웃음을 쳤다는 거예요. 아무리 흑도 놈들의 머릿수가 많아 봤자 장강일도의 상대가 될 것 같냐고.”

“장강일도?”

“이번에 변을 당한 수적 두령의 이름, 아니 별호래요. 어찌나 무공이 강한지 무림인들 사이에서는 모르는 사람이 없다는데요?”

“……그래서?”

“그 낭인의 말에 의하면 이번에 관부에서 흑도의 무리를 대거 잡아들인 것이, 뭔가를 감추기 위해서라고 하더라고요.”

문경은 내심 실소를 흘렸고, 중년 의생의 얼굴은 딱딱하게 굳었다.

“향아, 이 이야기를 나 말고 다른 누군가에게 했느냐?”

“아니요. 조금 전에 듣고 있는데 송 의원님께서 부르셔서 바로 왔는걸요.”

“황 의녀는? 너 말고 다른 이가 그 이야기를 들었더냐?”

“갑자기 왜 그러세요, 송 의원님?”

“대답하거라.”

사람 좋아 보이던 중년 의생이 얼굴을 굳히며 묻자, 어린 의녀가 기어가는 목소리로 말했다.

“아무도 없이 단둘이 나눈 이야기에요. 황 언니도 제게 처음 말한 거였고요.”

“휴우. 그나마 다행이로구나.”

“제가 잘못한 건가요?”

“아니다. 황 의녀나 너나, 아직 어린 탓에 경솔했을 뿐이지. 다만 앞으로 그에 관한 이야기는 하지 않는 것이 좋겠다. 알아들었느냐?”

“아, 알겠어요.”

“향아야.”

중년 의원은 잔뜩 주눅이 든 의녀의 머리를 쓰다듬어 주며 자상하게 말을 이었다.

“저 천인공노할 짓을 벌인 흑도 개잡놈들은 내일 정오에 참수형과 거열형(車裂刑)에 처할 거란다. 무한의 저잣거리에 놈들의 사지가 굴러다니고 핏물이 흥건하겠지.”

“네?”

“이게 전부 존귀하신 황상 폐하의 명을 받은 성주께서 나서신 덕분이고, 협객으로 이름 높은 태원진가의 진태경 대협께서 몸소 흉수들을 소탕했기 때문이다. 그러니 너는 유언비어에 휘둘리지 말고 그분들을 찬양하면 된다.”

“네, 네에.”

“아니, 그거 말고. 날 따라 하거라. 황상 폐하 만세! 성주님 천세! 진태경 대협 천세!”

“화, 황상 폐하 만세…….”

“더 크게!”

미친놈인가?

황망한 눈빛으로 중년 의생을 바라보던 문경은 내심 혀를 찼다.

나름 배운 사람이라 할 수 있는 의생조차 이럴진대, 평범한 민초들의 반응이야 보나 마나다.

‘아무런 의심 없이 천자를 찬양하겠지. 고작 이틀이 지났으니 이번 일에 관한 보고는 아직 황궁에까지 알려지지도 않았겠지만.’

꾸며진 거짓. 숨겨진 진실. 역시 세상은 달라지지 않는 법이다.

작게 고개를 내저은 문경은 재차 걸음을 옮겼다.

드넓은 호북성부(湖北省府)에 속한 의방을 완전히 벗어난 그가 곧장 향한 곳은 수많은 전각 중에서도 귀빈에게 배정되는 커다란 장원이었다.

그리고 그곳에는, 끈끈한 정을 과시하는 한 쌍의 스승과 제자가 있었다.

“다시 말해 봐라, 뭐? 적천강? 똥을 싸?”

“노야, 부디 고정하시고…….”

“네놈의 사지를 고정한 다음 면상에 똥을 싸 버릴라.”

“어어. 혹시 그쪽 취향이셨어요?”

“이 개썅노무…….”

“도르마무, 똥을 싸러 왔. 아, 죄송해요. 본능적으로 그만.”

“노부가 본문의 선조들께 맹세컨대, 네놈의 아가리에 똥을 처넣을 것이다!”

“으아아, 살려 줘요.”

“당장 이리 오지 못할까!”

쉬쉬쉬쉭! 쐐애애애액!

“…….”

치열한 추격전을 바라보던 문경은 문득 생각했다.

참으로 끈끈하고, 더러운 사승 관계라고.



* * *



천만다행으로, 적천강이 내 입에 똥을 싸는 일은 벌어지지 않았다.

물론 그렇다고 해서 평화롭고 멀쩡하게 일이 마무리되었다는 뜻은 아니다.

뻑!

“아, 잠깐만요. 뼈 맞았…….”

퍼엉!

“어억!”

아니 시벌, 화염신장은 선 넘은 거 아닙니까.

인간으로서의 양심은 있었는지 위력을 엄청나게 줄이긴 했지만 아무리 그래도 그렇지 제자를 상대로, 아니 제자나 다름없는 나한테 화염신장을 사용하다니.

‘속이 다 뜨끈해지네.’

국밥이 필요 없다. 화염신장 한 그릇 했더니 속이 다 든든할 지경이다.

“어우, 으.”

가슴을 움켜쥔 채 신음을 내뱉는 내게, 적천강이 음산한 목소리로 말했다.

“엄살 그만 피우고 일어나라.”

“끄, 끝난 겁니까?”

“아직 한참 남았다. 감히 하늘 같은 스승에게…….”

“스승?”

“크흠. 하늘 같은 스승보다 더 하늘 같은 노부에게 말을 놓다니. 노부가 이런 대접을 받으려고 네놈을 키운 줄 아느냐!”

“……키우신 건 저희 어머닌데, 왜 노야께서 생색을 내세요.”

“이놈이 그래도!”

적천강이 쌍심지를 켠 그때, 구원의 동아줄이 내려왔다.

“그쯤 해 두지.”

기척도 내지 않고 들어온 한 사람. 문경의 한 마디에 적천강이 눈살을 찌푸렸다.

“들어왔으면 조용히 구경이나 할 것이지. 뭐 하러 끼어들어?”

“보다 보니 너무 과한 것 같아서 끼어든 거다. 문제 있나?”

세상에, 존나 카리스마 있어. 저러니까 살수 시절 표적들이 골로 가지.

나는 감동이 넘실거리는 눈빛으로 문경을 바라보았다.

“오오, 갓성이시여…….”

“이놈 봐라. 또 헛소리를 늘어놓는 걸 보니 정신 차리려면 앞으로 한참 맞아야겠구나.”

흉흉하게 소맷자락을 걷어 올리는 적천강을 향해, 문경이 고개를 가로저었다.

“그만해라. 과하다.”

“아까부터 거슬리는군. 왜 자꾸 남의 집 일에 감 놔라, 배 놔라…….”

“아무리 생각해도 과하다. 내 몫도 있어야 하지 않겠나.”

“아, 그 부분은 인정이지.”

“…….”

염병. 저게 저 뜻이었네.

적천강이 훈훈하게 다음 타자에게 순번을 양보하며 물러서자마자, 새하얀 은빛 선이 채찍처럼 휘둘러졌다.

쉭, 서걱!

등골이 서늘해지고, 잘려 나간 옷자락 사이로 시원한 바람이 스며든다.

나는 정확히 두 갈래가 되어 좌우로 갈라지는 상의를 보며 마른침을 꿀꺽 삼켰다.

‘미친.’

그야말로 한 끗 차이.

콩닥콩닥 뛰는 가슴을 안고 서 있는 나를, 문경이 물끄러미 응시했다.

“피하지 않았군.”

“살기(殺氣)가 안 느껴져서요.”

“그래도 피할 수 있었을 텐데.”

“피해서 뭐합니까. 괜히 한 대 맞을 거 두 대 맞을 텐데. 어차피 절 죽일 생각도 없으셨잖아요?”

“역시 네 녀석은 이상해. 기분이 나쁠 정도로.”

글쎄, 기분 나쁜 것 치고는 표정이 모호한데?

반면 적천강의 표정은 누가 봐도 기분이 더러워 보인다.

“감히 노부의 제자에게 검을 휘둘러?”

“제자?”

문경의 반문에 적천강이 재빨리 말을 고쳤다.

“제자 같지도 않은 놈에게 검을 휘둘러?”

“조금 전까지 무공까지 사용해 가면서 개처럼 두들겨 패던 작자가 할 소린가?”

“개처럼 패든, 소처럼 굴리든 노부만 할 수 있는 것이다! 그리고 차라리 주먹을 써! 검 말고!”

“…….”

날 생각해 주는 건 알겠는데, 이거 묘하게 슬퍼지네.

도무지 앞뒤가 안 맞는 적천강의 주장을 듣고 있던 문경이 미간을 좁혔다.

“가만히 있어도 선천지기가 닳아 없어지는 기분이로군. 됐다. 이따위 문답을 하려고 온 것이 아니니.”

나는 적천강이 뭐라 하기 전에 잽싸게 입을 열었다.

“의방에 다녀오시는 길입니까?”

“그래. 동정어옹의 상태를 확인할 겸, 뱃사공도 만나고 왔지.”

“두 사람의 상태가 어떻습니까?”

“뱃사공은 의식을 회복했다. 별다른 징후도 없고, 말귀도 밝더군. 반면 동정어옹은…… 좋지 않아.”

나는 무겁게 고개를 끄덕였다.

뱃사공은 피어에 제대로 노출되기 전에 점혈로 의식을 잃었다.

하지만 동정어옹은 정반대다. 이건 짐작이지만, 아마 변이된 상태의 수신룡을 동정채에서 만났고 피어에 심각하게 노출되었음이 분명했다.

“많이 심각한 모양이군요. 하긴, 아무래도 제정신이 아닌 게 당연…….”

“부상이 심각하다.”

“예?”

“우선 사지가 으스러졌고 내상도 상당해. 초절정 고수인 데다 호북성주가 내준 영약이 있으니 빠르게 회복할 수는 있겠지만, 아무래도 그 이무기에게 제대로 당한 것 같더군.”

“…….”

“왜 그러지?”

“……아닙니다. 아무것도.”

내가 깜빡하고 말을 안 했던 모양이다.

정말, 진심으로 깜빡했었다.

지난 이틀 동안 말할 기회는 얼마든지 있었지만, 아무튼 깜빡한 거다.

‘실제로 정신이 없기도 했고.’

물론 그 이유는 단 한 사람을 추적하기 위해서였다.

홍란(紅蘭). 이 모든 사건의 원흉.

장장 오백여 년간 장강과 동정호를 수호하던 이무기를 타락시켜 숱한 희생을 불러일으킨 장본인.

그리고 끝끝내 찾을 수 없었던 그녀.

‘도대체…… 어디로 도망친 거지?’

나도 모르게 꺼내 든 은비녀를 바라보며 생각에 잠긴 그때였다.

쾅!

대문을 부술 듯 열어젖히며 장내에 뛰어든 한 사람.

전력으로 신법을 발휘하여 달려왔는지, 거친 숨을 내쉰 궁기방이 입을 열었다.

“훅. 후욱. 홍란의 흔적을, 찾았다.”

“……!”
```

## Final English reading copy

```markdown
# Chapter 481

*Click. Thud.*

After closing the door and leaving the boatman alone, Mungyeong thought to himself,

*This should be enough.*

Perhaps because he had lived a long life, the boatman was far more perceptive than Mungyeong had expected.

Although he would have to live under the authorities’ watch, that was still a hundred times better than being found dead somewhere without anyone knowing what had happened.

His deal with the City Lord of Hubei Province was already settled. As long as the boatman kept his mouth shut, he could spend the rest of his life in peace.

*No. Even if he tried to tell anyone, they’d obviously just treat him like a crazy old man.*

*And he won’t have to worry about money anymore. This should be a fairly decent arrangement for him.*

Mungyeong suddenly wondered what expression the boatman would make when he found the money pouch left beside the brazier.

And when he heard the words of the person who had handed it over and asked Mungyeong to deliver it.

*Still, he followed us for no reason and nearly died. He deserves hazard pay and workers’ compensation.*

Workers’ compensation?

It was a bizarre term Mungyeong had never heard before, but then again, Jin Taekyung had always been like that.

A boy so young he was practically yellow instead of merely green. And a boy who never stopped surprising him.

*I can’t make sense of him at all.*

Mungyeong could have listed his peculiarities forever, but after everything that had happened, that impression had only grown stronger.

He remembered how Jin Taekyung had rampaged even more wildly instead of shrinking back in the presence of that enormous monster, unlike anything Mungyeong had ever seen or heard of. His brow furrowed.

*Natural courage? That may be part of it, but there was something else… Yes. He looked used to it. Like a battle-hardened veteran who had fought countless battles.*

Had Jin Taekyung become accustomed to strange beings called supernatural powers while fighting Dark Heaven?

Or was there some secret about Jin Taekyung that no one knew?

Mungyeong was lost in thought as he continued walking when he heard voices.

“Physician Song. I heard those bastards who deserve to be beaten to death were captured.”

“Good heavens, ‘bastards who deserve to be beaten to death’? Hyang, you’re a medical apprentice. How can you use such harsh language…?”

In the courtyard of the clinic, where people came and went, a middle-aged medical apprentice of respectable age scolded a young female medical apprentice who did not even look old enough to be twenty. She pouted.

“A medical apprentice is still a person, isn’t she? Besides, those men deserve to die.”

“Ahem. Watch your words. You may be right, but I’m afraid someone might hear you.”

“You’re saying that because of that gentleman, aren’t you? What does it matter? He’s too far away to hear us anyway.”

Of course, unlike the young woman’s carefree assumption, Mungyeong was taking in every sound and movement around him without missing a thing.

The conversation between the two of them was no different.

“What do you think, Physician Song?”

“What are you talking about?”

“Oh, come on. Don’t pretend you don’t know. What else could I mean besides the dark-path figures of Murim who committed those heinous crimes at Dark Heaven’s instigation?”

“What could a mere medical apprentice like me possibly say? Still, I’m simply grateful that the culprits have finally been captured, and I intend to focus on my duties.”

“But isn’t it strange? The Sea Serpent Society ship that sank at Red Cliffs, the tragedy at Dongting Lake, and even the deaths connected to the river bandits beyond Tianling Falls. They’re saying all of it was done by those men.”

“Strange? What do you mean?”

“Well, it’s just… Hmm. You know Sister Hwang, right?”

“You mean the Medical Apprentice Hwang I know?”

“Yes. She told me something. Um…”

The young medical apprentice broke off and turned to look around. Then she rose onto her toes and whispered.

It still sounded as loud as thunder to Mungyeong.

“She said the patient she’s looking after is a pretty famous wandering martial artist, and when he heard the story, he snorted. He said that no matter how many dark-path figures there were, there was no way they could have been a match for the Yangtze One Saber.”

“The Yangtze One Saber?”

“That’s the name—or rather, the sobriquet—of the river bandit chief who suffered a disaster this time. Apparently, his martial arts are so powerful that there isn’t a martial artist anywhere who hasn’t heard of him.”

“…And?”

“According to what the wandering martial artist said, the authorities rounded up so many dark-path figures this time to cover something up.”

Mungyeong let out a quiet laugh inwardly, while the middle-aged medical apprentice’s face stiffened.

“Hyang, have you told anyone else this story?”

“No. I was listening to it just now when Physician Song called for me, so I came straight here.”

“What about Medical Apprentice Hwang? Did anyone else hear it besides you?”

“Why are you suddenly acting like this, Physician Song?”

“Answer me.”

The genial-looking middle-aged medical apprentice’s face hardened as he questioned her. The young woman replied in a tiny voice,

“No one else was there—it was just the two of us. And I was the first person Sister Hwang told.”

“Phew. That’s fortunate, at least.”

“Did I do something wrong?”

“No. You and Medical Apprentice Hwang were merely careless because you’re both still young. But from now on, it would be best not to discuss this matter. Do you understand?”

“Ah. Yes.”

“Hyang.”

The middle-aged medical apprentice gently patted the young woman’s head as she shrank in on herself, then continued kindly.

“Those dark-path mongrels who committed such heinous crimes will be put to death at noon tomorrow—some beheaded, others torn apart by chariots. Their severed limbs will be rolling through the streets of Wuhan, and the ground will be soaked in blood.”

“What?”

“This is all thanks to the City Lord, who acted on the orders of His Imperial Majesty the Emperor, and to Great Hero Jin Taekyung of the Jin Family of Taiyuan, who personally exterminated the culprits. So don’t let yourself be swayed by rumors. Praise those noble men instead.”

“Yes, yes.”

“No, not like that. Repeat after me. May His Majesty the Emperor live ten thousand years! A thousand years to the City Lord! A thousand years to Great Hero Jin Taekyung!”

“L-long live His Imperial Majesty the Emperor…”

“Louder!”

*Is he insane?*

Mungyeong stared at the middle-aged medical apprentice in disbelief and clicked his tongue inwardly.

If even a medical apprentice who could be considered educated acted like this, then the reaction of ordinary people was obvious.

*They’ll praise the Son of Heaven without a shred of doubt. It’s only been two days, so the report about this incident probably hasn’t even reached the imperial palace yet.*

A fabricated lie. A hidden truth.

The world truly never changed.

Mungyeong gave a small shake of his head and continued walking.

After leaving the clinic entirely—it was part of the vast Hubei provincial government compound—he headed straight for a large estate among the many pavilions, one reserved for honored guests.

And there, he found a master and Disciple proudly displaying the depth of their affection for each other.

“Say that again. What? Jeok Cheongang? Shitting?”

“Old Master, please calm down…”

“I’ll pin your limbs down and shit on your face.”

“Whoa. Is that your thing?”

“You fucking piece of—”

“Dormammu, I came to take a shit. Ah, sorry. Muscle memory.”

“I swear on the ancestors of our sect, I’ll stuff shit into your mouth!”

“Waaah! Somebody save me!”

“Get over here this instant!”

*Swish! Swish! Swish! Whoooosh!*

“…”

Watching the fierce chase unfold, Mungyeong suddenly thought,

*What an affectionate—and filthy—master-and-Disciple relationship.*

* * *

Fortunately, Jeok Cheongang did not end up shitting in my mouth.

Of course, that didn’t mean things ended peacefully or normally.

*Bam!*

“Ah, wait a second. That hit bone…”

*Boom!*

“Ugh!”

*Damn it. Isn’t using Flame Divine Palm going too far?*

He had drastically reduced its power, presumably because he possessed at least a shred of human conscience. But still—how could he use Flame Divine Palm against his Disciple? No, against me, who was practically his Disciple?

*My insides are getting nice and warm.*

I didn’t need gukbap.[^1] One bowl of Flame Divine Palm, and my stomach felt stuffed to the brim.

“Ugh…”

As I groaned while clutching my chest, Jeok Cheongang spoke in a sinister voice.

“Stop whining and get up.”

“Is it… over?”

“It’s still far from over. How dare you speak so casually to a master as high as the heavens…”

“Master?”

“Ahem. Not merely a master as high as the heavens, but this old man, who is even higher than the heavens. Do you think I raised you so I could be treated like this?”

“…My mother raised me, though. Why are you taking credit, Old Master?”

“You insolent brat!”

Just as Jeok Cheongang lit both his eyes like candles, a lifeline descended from heaven.

“That’s enough.”

Someone had entered without making a sound. At Mungyeong’s single remark, Jeok Cheongang frowned.

“If you came in, you should have quietly watched. Why did you have to interfere?”

“It seemed excessive, so I stepped in. Is there a problem?”

*Damn. He’s got so much charisma. No wonder his targets ended up in the grave when he was an assassin.*

I looked at Mungyeong with eyes overflowing with emotion.

“Oh, what a saint…”

“Look at this brat. He’s babbling nonsense again. I suppose he’ll need to be beaten for quite a while before he comes to his senses.”

Jeok Cheongang ominously rolled up his sleeve, but Mungyeong shook his head.

“Stop. This is excessive.”

“You’ve been irritating me for a while now. Why do you keep telling me what to do in someone else’s house…?”

“No matter how I look at it, this is excessive. Shouldn’t I get a turn too?”

“Ah. I admit that.”

“…”

*Damn it. So that’s what he meant.*

The moment Jeok Cheongang graciously stepped aside to let the next person take his turn, a pure-white silver line lashed out like a whip.

*Swish. Shhk!*

A chill ran down my spine, and cool air slipped through the gap in my severed clothes.

I swallowed hard as I watched the upper half of my outfit split cleanly into two pieces, left and right.

*Crazy.*

It had come down to a single hair’s breadth.

I stood there with my heart pounding as Mungyeong gazed at me impassively.

“You didn’t dodge.”

“I couldn’t sense any killing intent.”

“You could have dodged anyway.”

“What would have been the point? If I dodged, I’d just get hit twice instead of once. You weren’t planning to kill me anyway, were you?”

“As expected, you’re strange. Strange enough to put me in a bad mood.”

*Really? For someone who’s in a bad mood, your expression is pretty ambiguous.*

Jeok Cheongang, on the other hand, looked unmistakably pissed off.

“How dare you swing a sword at my Disciple?”

“Disciple?”

At Mungyeong’s questioning repetition, Jeok Cheongang hastily corrected himself.

“How dare you swing a sword at that bastard who isn’t even fit to be called my Disciple?”

“Is that really something you can say after beating him like a dog while using martial arts?”

“Whether I beat him like a dog or drive him like an ox, I’m the only one allowed to do it! And use your fists! Not a sword!”

“…”

I knew he was trying to look out for me, but somehow, that only made me feel sad.

Mungyeong narrowed his eyes as he listened to Jeok Cheongang’s utterly incoherent argument.

“Just standing here is making me feel my innate qi withering away. Enough. I didn’t come here for this sort of pointless exchange.”

Before Jeok Cheongang could say anything else, I hurriedly spoke up.

“Are you coming back from the clinic?”

“Yes. I went to check on the Dongting Fisherman and meet the boatman.”

“How are they?”

“The boatman has regained consciousness. There are no unusual symptoms, and he understands everything clearly. The Dongting Fisherman, on the other hand… isn’t doing well.”

I nodded heavily.

The boatman had lost consciousness from a Pressure-Point Strike before he was properly exposed to Fear.

The Dongting Fisherman was the exact opposite. This was only my guess, but he had evidently encountered the Water God Dragon in Donghu Stronghold and been seriously exposed to Fear.

“He must be in pretty bad shape. Though I suppose it’s only natural that he’s not in his right mind…”

“His injuries are severe.”

“What?”

“His limbs were crushed, and he has considerable internal injuries. He’s a Supreme Peak master, and the City Lord gave him an elixir, so he should recover quickly. But it seems that imugi really did a number on him.”

“…”

“What’s wrong?”

“…Nothing. It’s nothing.”

It seemed I had forgotten to tell him.

I had truly, genuinely forgotten.

I’d had plenty of opportunities to mention it during the past two days, but I had forgotten anyway.

*I’d also been a little preoccupied.*

Of course, the reason for that was because I had been pursuing one person.

Honglan. The mastermind behind this entire incident.

The woman who had corrupted the imugi that had guarded the Yangtze and Dongting Lake for more than five hundred years, bringing countless deaths in its wake.

And the woman I had never managed to find.

*Where the hell did she run off to?*

I was lost in thought as I stared at the silver hairpin I had taken out without realizing it.

*Bang!*

Someone burst into the courtyard, throwing open the main gate as if they intended to break it down.

Gung Gibang must have used his movement technique at full speed to get here, because he was breathing heavily when he spoke.

“Huff. Hah… I found a trace of Honglan.”

“……!”

[^1]: *Gukbap* is rice served in a hot, hearty soup, a common Korean comfort food.
```
