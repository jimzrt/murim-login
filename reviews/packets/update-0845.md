<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0845.txt",
      "sha256": "feb2e3874d09e7e5c0d5eed78c1621e8f7f25357711a3c71ec2ea2cc420f32fd",
      "bytes": 14672
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b7ee70c45c2507195e89dcb82801dad6b6f0b3a50d9dc746e73c4fa41b0e787d",
      "bytes": 2775
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2ac235886e36b4a9cfac67990c4e303d5cbbbaacdc20104970ce04b7ba9ca08c",
      "bytes": 227427
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5043041d5f4c3fc3075b8705ec2959d7a79ce370105f53edfba0ca42415bf1d4",
      "bytes": 723
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "804565c93146c04437a6e2573e933b06ca63d1437cb7184c4f6c06ef7f997050",
      "bytes": 1573
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "d6b0cc9fea7660e7931872299f05f9a17f290008ede4ae96a4e37cd80b9683c5",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "8232fadcaae670878a5a518f825df3e9750c1672aa72ff84a6c4ea77a39fa433",
      "bytes": 622
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "50e6ca56d167b2ea44e7cc706eec1ef7adaa9f3767a3767b174a9e435c83e983",
      "bytes": 554
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fd4790bf594f3f982af466f12b95b581c707ae942c0105f2f4d7be2cafb615a6",
      "bytes": 252065
    }
  ],
  "estimated_tokens": 11537
}
-->

# Durable State Update — Chapter 845

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
1 and safe_through 845. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 845. Profile updates may replace only one
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
  "chapter": 845,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 845,
    "continuity_sources": [845],
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
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader.",
    "The supernatural Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin’s vision of a black-haired man killing Ahomed after the ritual remains unexplained; Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury around his lower dantian remains unresolved; leveling up did not heal it.",
    "Jin is at the Sichuan Tang Clan after returning from another world; he and Jeok Cheongang have been talking for two days.",
    "The Divine Physician is preparing a pill for Jin’s recovery.",
    "The Sichuan Tang Clan and Sichuan Murim are rebuilding after Dark Heaven’s attack; allied martial artists remain to treat patients and guard against another attack.",
    "Jeok Cheongang and Jin Taekyung trust each other deeply; their Master-Disciple bond remains unformalized.",
    "Dark Heaven has developed experimental seeds over years of research and has scattered some across the Central Plains; some have already blossomed.",
    "The Blood Lord orders the sorcerers to prepare selected seeds for later deployment and sends missives by hawk.",
    "The Lord of Heaven recently ordered the Blood Lord to bring down the heavens, then returned to sleep."
  ],
  "continuity_sources": [
    844
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, what is the Ark, and how did Dark Heaven reach Murim?",
    "What are Dark Heaven’s seeds, and what are the two effects the experiments seek to enhance?"
  ],
  "safe_through": 844,
  "temporary_decisions": [
    "Keep magical power distinct from mana; keep Blink distinct from Teleport and Warp. Extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”",
    "Render 균열 as a social fracture or division, not the supernatural Rift; render 醜王 as “Disgrace King” when used as Jin’s mocking imagined epithet for Jeok Cheongang."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 살성     | **Slaughter Saint**           | —              |
| 삼성     | **Three Saints**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 고블린 | **goblin** | Monster species reported at the F-rank Gate. |
| 점혈 | **Pressure-Point Strike** | System-named technique used by Jeok Cheongang on Taekyung. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 신력 | **divine strength** | Superhuman strength attributed to Taekyung. |
| 무형지독 | **Formless Ultimate Poison** | Unidentified poison discovered inside Jeok Cheongang's body. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 식경 | **half an hour** | Time limit given for the requested reports. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 황하 | **Yellow River** | River along which civilization began. |
| 지옥도 | **hellscape** | Metaphorical description of the devastated battlefield. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 진태경 | 헌터 | field commander to allied Hunters | you; Hunters | blunt and commanding | Orders the human forces to stop asking questions and kill the fleeing Minotaurs. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 844
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 844
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; they trust each other deeply but have never formalized their bond. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to the late Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and is a long-standing rival of Peng Cheolhu.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 844
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 844
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 689
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

## Korean source

```text
＃845화



“잘게 씹어 삼키십시오.”

“잘게 씹어요?”

“예. 한 번에 삼키거나, 도중에 뱉으면 안 됩니다. 아시겠습니까?”

날이 밝기 무섭게 찾아온 신의(神醫)의 신신당부에, 나는 실소를 흘리며 그가 건네는 단환을 받아들었다.

“당연히 그래야죠. 제가 무슨 어린애도 아니고, 다 절 위해서 만들어 주신 건데.”

구슬만 한 크기에 거무스름한 색깔의 단환.

감정 시스템도 막혔으니 정확히 어떤 재료와 약효가 들어갔는지는 모르겠지만, 신의는 이걸 만들기 위해 며칠 밤을 꼬박 새웠음이 틀림없다.

진한 피로가 드리운 눈가가 바로 그 증거였다.

‘달리 돌봐야 할 환자들도 많았을 텐데.’

천하에서 가장 뛰어난 의원이, 자신의 건강과 시간까지 희생하며 나를 위해 제조한 단환이다.

설령 돌덩어리처럼 딱딱하다 해도 단물이 나올 때까지 씹을 생각이었다. 그것이 사람 된 도리니까.

그리고 감사한 마음을 담아 단환을 씹은 그 순간.

으적.

나는 깨달았다.

사람 된 도리고 나발이고, 이건 사람이 먹을 수 있는 종류의 것이 아니라는 사실을.

퉤.

본능적으로 뱉어 낸 단환이 신의의 새하얀 옷 위에 철썩 눌어붙는다.

며칠간 공들여 만든 단환을 슬픈 눈으로 바라보던 신의가 중얼거렸다.

“뱉지 말라니까…….”

혼미한 정신을 부여잡은 채 헛구역질을 하고 있던 나는 진심을 담아 입을 열었다.

“죄송한데, 제정신이십니까?”

“제정신이고, 지금 그 심정 충분히 압니다.”

“혹시 직접 드셔 보셨어요?”

“그건 아닙니다만.”

“그럼 제 심정 모르실 건데. 절대.”

“원래 몸에 좋은 약은 원래 쓴 법입니다. 절대.”

“아니, 그냥 쓴 정도가 아니던데요. 혹시 독이라도 넣으셨어요?”

“갈!”

옆에서 이 모든 것을 지켜보고 있던 적천강이 호통과 함께 눈을 부라렸다.

“저놈이 상당히 믿음직스럽지 못하고, 약간 돌팔이 같긴 해도 네놈을 위해 정성 들여 만든 약이다. 독이라니, 어디서 그런 망발을!”

“죄송합니다.”

“노부가 아니라 저 돌팔이에게 사과하거라!”

“죄송합니다, 어르신. 실언을 했습니다.”

상당히 믿음직스럽지 못하고, 약간 돌팔이 같은 신의는 말없이 나와 적천강을 번갈아 보았다.

무공만 받쳐 줬어도 둘 중 하나는 대침으로 쑤셔 버렸을 거라는 의지가 강하게 느껴졌지만, 다행스럽게도 그의 별호는 신의였지 신침이 아니었다.

솟구치려는 살심을 억누르려는 듯, 깊게 심호흡한 신의가 침착한 목소리로 말했다.

“괜찮습니다. 어차피 의술에 남은 일생을 바친 몸. 치료 중 억울하고 더러운 일이 생겨도 참아야 하는 것이 의원 아니겠습니까.”

“…….”

“…….”

“만약 제 스승님이 이 자리에 계셨다면 하는 생각이 들기도 하지만, 괜찮습니다. 저는 의원이니까요. 며칠 밤을 지새우며 열심히 만든 단환을 씹다 뱉어도 그러려니 해야지요. 허허허.”

전혀 안 괜찮아 보이는데.

이 정도면 말에 뼈가 있는 게 아니라, 송곳만 한 대침이 숨어 있는 수준.

나와 적천강은 그런 신의의 눈치를 살피며 조용히 전음을 주고받았다.

- 이게 다 네놈 때문이다.

- 아까 거기서 노야가 끼어들지만 않았어도 이런 상황까진 안 왔습니다.

- 약을 가져온 의원한테 독을 탔냐니, 그게 인간으로서 할 말이냐?

- 돌팔이라고 하는 건 인간으로서 할 말입니까?

- 못 할 건 뭐냐?

- 명색이 신의잖아요. 기분 나쁠 수 있죠.

- 노부는 화왕인데?

- 저는 열화신룡인데요.

- 좆밥 주제에 어딜 감히 노부에게 비비려 드느냐.

- …….

- 여하튼 그냥 닥치고 처먹어라. 모두 다 네놈을 위한 것이니라.

아무리 그래도 그렇지, 좆밥이라니.

마음의 상처를 입은 나를 매섭게 쏘아본 적천강이 애써 부드러운 어투로 신의에게 말을 건넸다.

“마음 풀게. 저 녀석은 노부가 따끔하게 혼을 내 주지.”

“그럼 적 대협은 누가 혼내는지…….”

“응? 뭐라고?”

“아닙니다. 잠시 말이 헛나왔습니다.”

입에 침도 안 바르고 거짓말을 한 신의가 의복에 붙은 단환을 떼어 냈다.

내 이빨 자국이 선명하게 나 있는 단환을 처연하게 응시하던 그가 한숨을 푹 내쉬었다.

“약효가 좀 새어 나가긴 했지만, 아직 늦지 않았습니다. 이번에야말로 잘 씹어 삼키십시오.”

다른 건 몰라도, 새어 나온 게 약효뿐만은 아닌 것이 확실하다.

뭉개진 단환의 내부에서 흘러나온 끔찍한 악취를 맡은 적천강이 본능적으로 뒷걸음질 쳤다.

“이건 설마 무형지독(無形之毒)……!”

“치료고 뭐고 관두겠습니다. 이 단환은 그냥 측간에 처박을 테니 다른 의원이나 알아보십시오.”

“어, 어허!”

휙 돌아서려는 신의의 옷자락은 붙잡은 화왕이 코맹맹이가 된 목소리로 물었다.

이미 번개처럼 움직인 다른 한 손은 코를 움켜잡은 후였다.

“아, 노부도 모르게 그만. 미안하군. 하지만 이 악취는…… 도대체 이 단환에 무슨 재료들을 넣은 거지?”

“말씀드리면, 알아들으실 수는 있습니까?”

“…….”

“스승님께서 알려 주신 비전이니까 더 따지지 말고 그냥 넘어가십시오. 독은 아니니까 안심하시고요.”

적어도 내가 아는 적천강이라면 시원한 쌍욕과 함께 뜨끈한 화염신장을 동시에 갈겼을 텐데, 지금만큼은 신의가 슈퍼 갑이다.

환자와 환자 보호자의 신분인 우리는 조용히 입을 다문 채 고개를 끄덕였다. 특히 적천강은 걱정과 흥미가 반씩 뒤섞인 표정으로 나를 채근했다.

“우선 시키는 대로 해라. 노부가 있으니 뒷일은 걱정하지 말고.”

“…….”

아니, 그렇게 말하니까 진짜 무형지독이라도 삼키는 것 같잖아.

원망 어린 눈빛으로 적천강을 바라보던 나는 눈을 질끈 감았다.

그리고 최대한 감각을 차단하는 동시에 단환을 입안에 털어 넣었다.

으적으적으적.

쉴 새 없이 움직이는 턱. 조금이라도 미각을 느끼지 않기 위해 입안에서 한껏 오므린 혀. 마지막으로 헛구역질을 참기 위한 필사적인 노력 한 스푼까지.

‘흐읍.’

죽을 것 같다. 아니, 이미 죽었어도 놀랍지 않다.

한번 씹을 때마다 끔찍한 악취가 입안에서 터져 나온다.

정체 모를 걸쭉한 즙이 조금씩 목구멍을 타고 몸 안으로 흘러 들어가자 식도는 제로투를, 오장육부는 코카인 댄스를 추기 시작했다.

‘우욱, 씹……!’

맹세컨대, 이 정도의 악취와 역겨움은 난생처음이다.

초짜 헌터 시절 게이트에서 고블린 겨드랑이에 코를 박고 넘어졌을 때도, 비명을 지르며 손발을 휘두르다가 의도치 않게 놈의 불알을 맨손으로 터트렸을 때도 정도는 아니었다.

“욱, 우우욱!”

이성을 벗어난, 그야말로 본능적인 움직임.

새우처럼 허리를 굽힌 나는, 배 속 깊숙한 곳에서 솟구치는 뜨거운 무언가를 토해 냈다.

아니, 토해 내려 했다.

그 순간 내 입과 코를 틀어막은 누군가의 손길이 아니었다면.

콰득.

숨이 턱 막힌다. 반사적으로 몸부림쳐 보지만 단단하게 내 몸을 붙잡은 손아귀는 아교(阿膠)처럼 떨어지지 않았다.

그리고 이 정도로까지 나를 완벽하게 제압할 수 있는 사람은, 적어도 이 자리에서는 단 한 명뿐이다.

‘노야?’

마침내 질끈 감고 있던 눈을 부릅뜬 나는 볼 수 있었다.

열양지기로 불그스름하게 달아오른 적천강의 눈동자를. 거기에 더해 목젖을 후려치는 강렬한 충격을.

뻑!

입과 코를 빈틈없이 틀어막은 적천강의 손 때문일까. 비명은 새어 나오지 않았다.

나는 기껏 밝아졌던 시야가 까맣게 물드는 것을 보며 생각했다.

‘이 정도면 진짜 약이 아니라 독에 가까운 것 같은데.’

그게 끝이었다.

잘게 부서진 단환이 타액과 뒤섞여 몸속 깊숙이 흘러 들어가는 것을 느끼며, 나는 정신을 잃었다.

화아악.

더없이 익숙한 열기(熱氣)와 함께.



* * *



적천강은 당황하지도, 머뭇거리지도 않았다.

일백 하고도 수십여 년을 살아온 그다.

하늘의 뜻과 순리를 안다는 지천명(知天命)은 이미 옛날 옛적에 지나왔다. 적천강은 자신이 해야 하는 일을 그 누구보다 잘 알고 있는 사람이었다.

‘지금.’

전신이 열양지기로 들끓지만, 머릿속은 만년설처럼 차갑다.

언제 실없는 소리나 했었냐는 듯, 무겁게 가라앉은 얼굴을 한 그는 혼절한 진태경을 향해 손을 뻗었다.

쉭, 툭. 투두두둑!

실로 섬광 같은 속도에, 무서우리만치 침착한 손길.

적천강의 손이 흐릿해질 때마다 진태경의 몸뚱어리가 들썩인다.

점혈(點穴)과 동시에 스며든 열양지기가 단환을 녹이고 약효를 전신 곳곳으로 퍼트렸다.

‘서두르지 말고, 침착하게.’

적천강은 스스로에게 다짐하듯 마음속으로 뇌까렸다.

지금부터 조금의 실수도 있어서는 안 된다. 인간은 그리 쉽게 죽지 않지만, 그 육신은 놀랍도록 예민하니까.

수 갑자나 되는 공력을 품은 몸뚱어리라면 더 말할 것도 없다.

드드드득.

강대한 열기가 들끓었다. 단단한 나무로 만들어진 전각의 바닥이 새카맣게 그을리고, 사막에서나 볼 법한 아지랑이가 두 사람을 감쌌다.

스아아아아.

만약 지극히 평범한 의원이 이 광경을 보았다면 눈을 비비거나 비명을 지르며 도망쳤을 것이다.

그러나 신의(神醫)는 그 중 어디에도 해당하지 않는 유일한 의원이었다.

그는 지난 수십여 년간 스승을 따르며 수많은 환자를 치료했고, 훌륭한 가르침으로 그 이상의 경험을 쌓았다.

물론 그 스승의 정체가 살성(殺星)이라는 것 역시도 큰 이유였다.

‘더할 나위 없이 순조롭다. 바로 그 추궁과혈(推宮過穴)이라고는 믿기지 않을 만큼.’

신의는 경이에 물든 눈으로 적천강을 바라보았다.

추궁과혈은 그 누구도 쉽게 도전할 수 없는 행위였다.

인체에 존재하는 수백 개의 혈을 쓸고 때리는 동시에, 밀고 두드림으로서 막힌 기와 혈을 타통하고 뭉쳐진 근육을 풀어 주어야 한다.

이것만으로도 엄청난 정신력과 공력을 소모하는 일인데, 자칫 한순간이라도 실수한다면 시전자까지 큰 타격을 입을 수 있었다.

‘게다가 지금 같은 경우에는 단환의 기운까지 몸 구석구석 퍼트려야 하는 상황.’

결코 쉽지 않다.

아니, 극히 어렵다.

평소였다면 제아무리 신의라 해도 감히 이런 방식의 치료는 엄두조차 내지 못했을 만큼.

그러나 화왕(火王) 적천강이 있다면 다르다. 그는 천하에서 왕이라 불리는 열 명의 초절정 고수 중에서도 삼성(三星)과 비견되는 유일한 인물이었고, 하나뿐인 제자를 위해서는 그 어떤 위험도 감수할 수 있는 스승이기도 했다.

마치 자신의 스승처럼.

‘지금쯤 어디에선가 잘 지내고 계시겠지요. 그렇지 않습니까?’

지금으로부터 넉 달 전, 떠밀 듯이 헤어진 스승을 문득 떠올린 신의가 흐릿하게 미소지은 그때.

솨아아아아.

서서히 흩어지는 열기와 아지랑이 속, 살짝 파리해진 안색으로 일어나는 적천강이 그의 시야에 들어왔다.

“적 대협. 괜찮으십니까?”

“호들갑 떨 것 없다. 이 정도로는 끄떡없어.”

“그래도 잠시…….”

“노부는 괜찮으니, 저 천둥벌거숭이 같은 녀석부터 살펴 주어라.”

신의가 지켜본 바에 의하면 완벽한 추궁과혈이었다.

한데 그토록 열과 성을 다했음에도 걱정에 걱정을 거듭한다.

이렇게 굳이 살피라 부탁하는 것은 신의에 대한 신뢰라기보다는, 제자에 대한 끝없는 애정이 더욱 컸기 때문이리라.

그리고 그런 적천강의 마음을 모를 신의가 아니었다.

“알겠습니다. 제가 다시 살펴보지요.”

침착하게 대답한 그는 쓰러진 진태경에게 다가가 맥을 짚었다.

다시 고개를 들었을 때는 한 식경이라는 시간이 훌쩍 지나가 있을 만큼, 신의 역시 정성을 들였다.

“되었습니다. 약효가 완전히 스며들었습니다.”

그제야 지쳐 있던 적천강의 눈빛에 생기가 돌았다.

“그 말은…….”

“송구하오나, 완치까지는 멀었습니다. 아니, 저로서는 완치를 장담키 어렵습니다.”

“뭐라?”

“적 대협께서도 이미 알고 계시지 않습니까. 원기(元氣)가 상했다는 것을.”

“……!”

“강철도 열이 가해지면 구부러집니다. 결국은 한 줌 쇳물이 될 뿐입니다. 하물며 피륙으로 이루어진 몸뚱어리는 어떻겠습니까.”

신의는 깊게 가라앉은 눈으로 적천강을 바라보았다.

파르르 떨리는 그의 눈빛을 마주 보기 힘들었지만, 환자의 상태를 두고 거짓을 입에 담는다면 의원으로서 자격이 없다.

“단환을 제조하며 다시 한번 깨달았습니다. 완치는 불가(不可), 허나 호전은 가능하다는 것을요.”

으득.

적천강은 이를 악물었다.

이미 남만에서부터 짐작했던 사실. 그러나 차마 대면하고 싶지 않은 진실이기도 했다.

‘이 미련한…… 미련한 놈을 보았나.’

도대체 무슨 일이 있었던 것일까. 지옥도(地獄道)로 변해 가는 그곳에서 얼마나 치열하게 싸우고, 또 싸웠던 것일까.

어느덧 평온하게 잠든 진태경을 바라보는 적천강의 눈동자가 파르르 떨린 그때였다.

덜컹!

다급히 문이 열림과 동시에, 창밖에서 거친 말발굽 소리가 울려 퍼졌다.
```

## Final English reading copy

```markdown
# Chapter 845

“Chew it thoroughly before you swallow.”

“Chew it?”

“Yes. Don’t swallow it whole, and don’t spit it out halfway through. Understood?”

The Divine Physician had come first thing in the morning and was now giving me his sternest warning. I let out a faint laugh and accepted the pill he held out.

“Of course. I’m not a child, and you made it for my sake.”

The pill was about the size of a marble and dark in color.

The Appraisal System was still inaccessible, so I couldn’t tell exactly what ingredients it contained or what effects it had. But the Divine Physician must have spent several sleepless nights making it.

The deep fatigue around his eyes was proof enough.

*He must have had plenty of other patients to care for, too.*

This pill had been made for me by the best physician in the world, at the expense of his own health and time.

Even if it were as hard as a rock, I planned to chew it until the sweetness came out. It was the least I could do.

And the moment I chewed the pill with heartfelt gratitude—

Crunch.

I realized that doing the right thing as a human being could go to hell. This wasn’t the sort of thing a human being could eat.

Ptooey.

The pill I spat out on instinct stuck fast to the Divine Physician’s pristine white robe.

He gazed sorrowfully at the pill he’d spent days making and muttered, “I told you not to spit it out…”

I was trying to hold on to my fading senses while retching when I opened my mouth, completely sincere.

“Sorry, but are you in your right mind?”

“I am, and I understand exactly how you feel.”

“Have you tried eating it yourself?”

“I haven’t.”

“Then you have no idea how I feel. None.”

“Medicine that’s good for you is supposed to taste bitter. It always is.”

“No, this wasn’t just bitter. Did you put poison in it or something?”

“Enough!”

Jeok Cheongang, who’d watched the whole thing from the side, bellowed and glared at me.

“He may not be particularly trustworthy and may seem a bit of a quack, but he made that medicine with care for your sake. Poison? Where did you get the nerve to say such blasphemous nonsense?”

“Sorry.”

“Don’t apologize to me. Apologize to that quack!”

“Sorry, Divine Physician. I misspoke.”

The Divine Physician—who was not particularly trustworthy and seemed a bit of a quack—looked silently back and forth between Jeok Cheongang and me.

I could practically feel his determination to stab one of us with a large acupuncture needle if only his martial arts were up to the task. Fortunately, his sobriquet was Divine Physician, not Divine Needle.

The Divine Physician took a deep breath, as if trying to suppress his murderous urge, then spoke in a calm voice.

“It’s all right. I’ve devoted my life to medicine. Isn’t it a physician’s duty to endure unfair and filthy treatment during a patient’s care?”

“……”

“……”

“Sometimes I do wonder what my Master would think if he were here, but it’s all right. I’m a physician, after all. I should expect a pill I spent several sleepless nights making to be chewed up and spat out. Ha ha ha.”

He did not look all right at all.

At this point, it wasn’t that his words had a barb in them. There was a needle as big as an awl hidden in there.

The Divine Physician’s eyes made Jeok Cheongang and me exchange Sound Transmission in silence.

—This is all your fault.

—If you hadn’t butted in back there, it wouldn’t have come to this.

—You asked the physician who brought you medicine if he’d put poison in it. What kind of thing is that to say?

—And what kind of thing is it to call him a quack?

—What’s wrong with that?

—He’s the Divine Physician. He might take offense.

—I’m the Fire King.

—I’m the Blazing Flame Divine Dragon.

—How dare a fucking nobody like you pretend you’re on my level?

—……

—Anyway, shut up and eat it. This is all for your sake.

Still, “weakling”? That hurt.

Jeok Cheongang glared at me, and then, making a show of softening his tone, addressed the Divine Physician.

“Don’t take it to heart. I’ll give the boy a proper scolding.”

“Then who’s going to scold Sir Jeok…?”

“Hm? What was that?”

“Nothing. I misspoke.”

The Divine Physician lied without a hint of remorse as he peeled the pill off his robe.

He stared mournfully at the clear tooth marks I’d left in it, then let out a long sigh.

“Some of the medicinal properties have seeped out, but it’s not too late. This time, chew it up and swallow it properly.”

One thing was clear: the medicinal properties weren’t the only thing that had seeped out.

Jeok Cheongang caught a whiff of the hideous stench escaping the crushed pill and instinctively stepped back.

“Could this be Formless Ultimate Poison…!”

“I’m done with this treatment. I’ll toss this pill in the latrine. Find yourself another physician.”

“W-wait!”

The Fire King grabbed the Divine Physician’s robe as he turned to leave, then asked in a nasal voice.

His other hand had already moved like lightning to pinch his nose shut.

“Ah, I didn’t mean to do that. Sorry. But this stench… What in the world did you put in this pill?”

“If I told you, would you even understand?”

“……”

“It’s a secret technique my Master taught me, so don’t press me on it. And don’t worry, it’s not poison.”

If I knew Jeok Cheongang, he would have let loose a string of curses and followed it up with a scorching Flame Divine Palm. But right now, the Divine Physician held all the cards.

We were the patient and his guardian, so we kept our mouths shut and nodded. Jeok Cheongang, in particular, urged me on with an expression half full of worry and half full of interest.

“Just do as you’re told. I’m here, so don’t worry about what comes next.”

“……”

The way he put it, it sounded like I was really about to swallow Formless Ultimate Poison.

I looked at Jeok Cheongang resentfully, then squeezed my eyes shut.

I blocked out my senses as much as I could and tossed the pill into my mouth.

Crunch, crunch, crunch.

My jaw moved without pause. I curled my tongue tight against the inside of my mouth to keep from tasting even a hint of it. And, for good measure, I added one heaping spoonful of desperate effort to keep myself from retching.

*Hnnngh.*

I felt like I was going to die. No, I wouldn’t have been surprised if I was already dead.

A hideous stench burst into my mouth with every chew.

Some unidentified, viscous juice slowly trickled down my throat, and my esophagus started doing the “Zero Two,” while my guts began doing the cocaine dance.

*Urgh, shit…!*

I swear, I’d never experienced a stench or a disgust this bad in my life.

Not even when I was a novice Hunter and fell with my nose buried in a goblin’s armpit in a Gate. Not even when I screamed and flailed my arms and legs, accidentally bursting the creature’s balls with my bare hands.

“Urk! Uuugh!”

My body moved on pure instinct, beyond reason.

I bent over like a shrimp and started to throw up something hot that surged from deep in my stomach.

Or I tried to.

If someone hadn’t clamped a hand over my mouth and nose at that very moment—

Crack.

The breath caught in my throat. I struggled on reflex, but the hand holding me fast wouldn’t budge, like glue.

And there was only one person here who could restrain me so completely.

*Old Master?*

I finally pried my eyes open, which I’d squeezed shut, and saw them.

Jeok Cheongang’s eyes, glowing red from the Scorching Yang Qi. And then came a powerful blow to my Adam’s apple.

Thwack!

Maybe because Jeok Cheongang’s hand was sealed over my mouth and nose, not a sound escaped me.

As my vision, which had just brightened, turned black, I thought:

*At this point, that medicine sounds more like poison than medicine.*

That was my last thought.

I felt the finely crushed pill mix with my saliva and flow deep into my body, and then I lost consciousness.

Whoosh.

Along with a heat more familiar than anything.

* * *

Jeok Cheongang didn’t panic or hesitate.

He had lived for a hundred and several dozen years.

He had passed the age of fifty, when a man understands Heaven’s will and the natural order, long, long ago. Jeok Cheongang knew better than anyone what he had to do.

*Now.*

His whole body roared with Scorching Yang Qi, but his mind was as cold as a glacier.

His face had grown heavy and still, as if he’d never once said anything frivolous. He reached toward the unconscious Jin Taekyung.

Whoosh. Tap. Dudududud—

His movements were as swift as a flash of light, his hands terrifyingly calm.

Each time Jeok Cheongang’s hands blurred, Jin Taekyung’s body jerked.

As he struck Jin’s pressure points, the Scorching Yang Qi seeped in, melting the pill and spreading its medicinal effects throughout his body.

*Don’t rush. Stay calm.*

Jeok Cheongang repeated the words to himself as if making a vow.

From this moment on, he couldn’t afford the slightest mistake. Humans didn’t die that easily, but the body was astonishingly sensitive.

All the more so when it housed the internal energy of several jiazi.

Rumble.

A tremendous heat raged around them. The floor of the pavilion, built of solid wood, charred black, and heat shimmered around the two men like a mirage in the desert.

Hssssss.

If an ordinary physician had witnessed the scene, he would have rubbed his eyes or screamed and run away.

But the Divine Physician was the one physician who did neither.

For decades, he had followed his Master and treated countless patients, gaining even more experience from his excellent teachings.

Of course, the fact that his Master was the Slaughter Saint was another major reason.

*It’s going more smoothly than I could have hoped. It’s hard to believe he’s performing something as difficult as this technique.*

The Divine Physician watched Jeok Cheongang, his eyes filled with wonder.

Working the channels and pressure points was not something anyone could easily attempt.

He had to sweep and strike the hundreds of pressure points in the human body while pressing and tapping them, opening blocked qi and blood channels and loosening knotted muscles.

That alone took enormous mental and internal energy. If he made even a single mistake, he could suffer a serious injury himself.

*And in this case, he also has to spread the pill’s energy throughout every part of the body.*

It was by no means easy.

No—it was exceedingly difficult.

Under normal circumstances, even the Divine Physician wouldn’t have dared attempt treatment this way.

But with the Fire King, Jeok Cheongang, it was different. He was the only one among the ten Supreme Peak masters known as kings throughout the world who could be compared to the Three Saints. And he was a Master who would take any risk for his only Disciple.

Just like his own Master.

*You’re doing well somewhere, aren’t you? Aren’t you?*

The Divine Physician had just thought of the Master he’d parted from four months earlier, almost as if he’d been forced to leave, and smiled faintly when—

Whoosh.

Through the slowly dissipating heat and haze, Jeok Cheongang came into view, rising to his feet with a slightly pale face.

“Sir Jeok. Are you all right?”

“Don’t make a fuss. I’m fine.”

“Even so, at least for a moment…”

“I’m fine. Look after that reckless brat first.”

From what the Divine Physician had seen, the treatment had been flawless.

And yet, after pouring so much effort into it, Jeok Cheongang was still consumed with worry.

That he would specifically ask the Divine Physician to examine Jin was not so much a matter of trust in the physician as it was a reflection of his boundless affection for his Disciple.

And the Divine Physician understood Jeok Cheongang’s feelings.

“Understood. I’ll examine him again.”

He answered calmly and approached Jin Taekyung, who lay collapsed. By the time he looked up again, half an hour had passed.

“It’s done. The medicine has been completely absorbed.”

Only then did Jeok Cheongang’s tired eyes come alive again.

“That means…”

“I’m sorry, but he’s still a long way from a full recovery. No—speaking for myself, I can’t guarantee a full recovery at all.”

“What?”

“You already knew, Sir Jeok. His vital essence has been damaged.”

“……”

“Even steel bends when it’s heated. In the end, it becomes a lump of molten metal. What chance does a body made of flesh and blood have?”

The Divine Physician looked at Jeok Cheongang with heavy eyes.

It was hard to meet his trembling gaze, but a physician who lied about a patient’s condition was no physician at all.

“Making this pill made me realize it once again. A full recovery is impossible, but improvement is possible.”

Grind.

Jeok Cheongang clenched his teeth.

He had suspected it since Nanman. But it was a truth he couldn’t bring himself to face.

*You foolish… foolish boy.*

What in the world had happened? How fiercely had he fought, again and again, in that place turning into a hellscape?

Jeok Cheongang watched Jin Taekyung, who had fallen asleep peacefully, his eyes trembling.

Then—

Crash!

The door flew open in a rush, and the rough sound of horses’ hooves rang out from beyond the window.
```
