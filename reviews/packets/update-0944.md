<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0944.txt",
      "sha256": "bd80a5e5fd20ffe36dc2eb3ab6bbecdc2fc30b712fe3d3453ce5248760295ac0",
      "bytes": 13291
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5924b3fc6731e845724b3bd5553859eb07e07b606488e8f02ae0f5f34fbd6011",
      "bytes": 2661
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bf5fc17b6bb6e8afe85dde4372e566811c088e0e074d1913c7f254ffd989efbb",
      "bytes": 233310
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "68484295f356dbc88f187177ca4f61ad85ee9493ec5b8796ed41025481f871bb",
      "bytes": 759
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "117320657fdaebb58e4522b116169c84326df022924a5941681a823c20be2141",
      "bytes": 838
    },
    {
      "path": "characters/Jang Il.md",
      "sha256": "4b60ef143829f478ee03b4458d5dac2d03de6cab9b81425a23b8e557c24cde11",
      "bytes": 477
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1dfc7bc4c8c065968a0dc6fac3b5e6a8a65b279e2be586a61b7822900f49c995",
      "bytes": 1204
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "aaae9d51ddc00e373c7232613913f6b09ce342883c5d7b6313d3c385339148ad",
      "bytes": 1449
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "d79f922475ad19a4659277944e6ae614516bca91b0af11a4f289be0d7e8d9d0d",
      "bytes": 622
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "409dab31f1bbc82e20617d2a135087957b67d51a1c57f57b678f45daa03a7e4f",
      "bytes": 1061
    },
    {
      "path": "characters/Namgung Ryong.md",
      "sha256": "7f258ce4784d16bcb1fc32168d83063de46633665e45ff500445eb70955029da",
      "bytes": 1486
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "65635cdcda39ff7f6038e8872a12d5ba618b1efbe131ed075fb6619e35e50009",
      "bytes": 685
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f66daa4bae985fcbafa7ec30ad9fc462f9834c125f917088f6bc22c9afe669f8",
      "bytes": 267309
    }
  ],
  "estimated_tokens": 13375
}
-->

# Durable State Update — Chapter 944

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
1 and safe_through 944. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 944. Profile updates may replace only one
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
  "chapter": 944,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 944,
    "continuity_sources": [944],
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
    "The Emperor was poisoned with Blood Soul Gu, which reached his marrow; the Divine Physician said his vitality was at its limit and could not guarantee he would survive another couple of months.",
    "The Divine Physician says the Emperor’s only path to survival requires him to die once; the method is not yet explained.",
    "The old bamboo slip Taekyung gave the Divine Physician bears the names Maoshan Sect and White Illusion Jiangshi Art; its full significance is unknown.",
    "Taekyung’s System quest requires him to remove the Blood Soul Gu from the Emperor’s head and successfully treat him; its reward and failure consequence are unknown.",
    "The Emperor prepared for his death by transferring loyal retainers and his power base to Zhu Bao.",
    "War against Dark Heaven has begun, and the imperial court is mobilizing after Taekyung warned of a possible invasion of Shanxi before the Double Ninth Festival.",
    "Taekyung was appointed Marquis of Shangshan and Thousand Captain, with a thousand Embroidered Uniform Guards entrusted to him to fight the foreign enemy.",
    "The party is traveling toward Shanxi. Namho will contact the Murim Alliance and seek reinforcements from behind; Song Ilseom and Sama Pyo will lead the remaining group toward Shanxi, while Taekyung, Jeok Cheongang, and the Bow Saint advance over a mountain route.",
    "A bandit outpost has spotted an approaching group bearing the Great Nangong Family’s flags and alerted its stronghold.",
    "Ma Sanbao escaped and evaded the Imperial Army’s three-day search.",
    "The Eastern Heaven Demon Lord’s hidden iron chest contained old bamboo slips, recent papers, and a small silk pouch of unknown significance.",
    "The Bow Saint says the Martial God chose her; she tested Taekyung to confirm he was the chosen one and assess his power and character."
  ],
  "continuity_sources": [
    943,
    942
  ],
  "open_questions": [
    "What is the Martial God’s identity, and what is the full nature of his connection to the chosen one and the Bow Saint?",
    "How far has Dark Heaven infiltrated the Great Nation, and which officials or commanders are involved?",
    "Where is Ma Sanbao, and what is his current status?",
    "Who sent the Shanxi Annihilation Plan missive, and when will Dark Heaven’s invasion begin?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain, and what is their significance?"
  ],
  "safe_through": 943,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 남궁천    | **Nangong Cheon**  |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 남궁세가   | **Nangong Family**               |
| 남만야수궁  | **Nanman Beast Palace**          |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 마교     | **Demonic Cult**                                 |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 퀘스트              | **Quest**                      |
| 로그아웃             | **Logout**                     |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 안휘     | **Anhui**              |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 장일 | **Jang Il** | Twenty-five-year-old two-knot Beggars' Sect Disciple killed near Emei. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남궁룡 | **Namgung Ryong** | Family Head of the Namgung family. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남궁 | **Namgung** | Surname of the family led by Namgung Ryong. |
| 창천 | **azure heaven** | The cloudless sky seen by Namgung Ryong. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 합비 | **Hefei** | City on the Jin Family's new escort-trade route. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 검왕 | **Sword King** | Short form for the Azure Sky Sword King, Nangong Cheon. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 운남 | **Yunnan** | Region from which Jongni Chu comes. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 태산북두 | **Mount Tai and Northern Dipper of the Murim** | Honorific description of Shaolin's standing in the Murim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 비처 | **secret refuge** | Hidden retreat of the Dongting Fisherman. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 한나절 | **half a day** | Elapsed duration in Jeok's first time-loss episode. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 신물 | **divine artifact** | General term for a sacred or divine object, distinct from 신석. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 남궁룡 | 적천강 | family_head_to_legendary_martial_master | Fire King | formal-deferential | Namgung Ryong accepts three hundred silver nyang as compensation for offending Jeok Cheongang. |
| 남궁룡 | 진태경 | Family Head to younger visiting martial artist | you | formal-but-familiar | Namgung Ryong uses 자네 while asking Taekyung to stop the duel. |
| 진태경 | 남궁룡 | younger visiting martial artist to Family Head | Family Head | formal-polite | Taekyung addresses Namgung Ryong as 가주님 while acknowledging his inability to stop his father. |
| 진태경 | 남궁천 | junior martial artist to legendary martial master | Great Hero Nangong Cheon | formal-deferential | Taekyung uses the title and honorific 대협 when formally greeting the Azure Sky Sword King. |
| 남궁천 | 진태경 | legendary martial master to audacious junior | you / brat | blunt and intimidating | Namgung Cheon uses 네 녀석 and 놈 while testing and threatening Taekyung. |
| 남궁천 | 남궁룡 | father_to_son | you | formal-but-familiar | Nangong Cheon speaks to his sixty-year-old son while discussing martial mastery and Taekyung. |
| 적천강 | 남궁룡 | legendary_martial_master_to_family_head | Family Head Nangong | familiar and teasing | Jeok calls him 남궁 가주 while asking whether his son will compete. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 중년인 | 진태경 | veteran civilian Hunter to celebrated allied Hunter | Mr. Jin | formal-polite and awed | The casualty clerk addresses Jin as 진 선생님 after Jin asks him to list Lei Fei among the dead. |
| 진태경 | 중년인 | celebrated Hunter to older fellow Hunter | sir | casual and teasing | Jin addresses the older Hunter as 아저씨 while joking with him and giving him instructions. |
| 적천강 | 창천검왕 | long-standing martial rival and duel partner | Azure Sky Sword King | blunt and familiar | Explicitly names him while coming to fulfill their long-delayed duel promise. |
| 창천검왕 | 적천강 | long-standing martial rival and duel partner | Fire King | formal and familiar | Addresses Jeok Cheongang by title while welcoming the promised duel. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 942
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 940
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Jang Il.md

# Jang Il (장일)

- **Safe through:** Chapter 854
- **Aliases:** None
- **Role:** Jang Il is a junior military officer and one of the seven gate commanders at Yichang’s West Gate.
- **Personality:** He is complacent and greedy, yet regards his restrained corruption as respectable.
- **Voice:** Not established
- **Relationships:** He commands soldiers at Yichang’s West Gate and has an elderly servant.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 943
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and says they have shared everything since he accepted him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 942
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 942
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 895
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful, easygoing, and teasing, but capable of handling heavy administrative responsibilities efficiently.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Namgung Ryong.md

# Namgung Ryong (남궁룡)

- **Safe through:** Chapter 244
- **Aliases:** None
- **Role:** Family Head of the Namgung family; he has led the family for nearly twenty years and orders its intelligence network to investigate Jin Taekyung after learning that Jeok Cheongang has returned to Mount Jiuhua with Taekyung as his new Disciple; he arrives at Mount Jiuhua with dozens of highly trained martial artists, pays three hundred silver nyang for a ginseng root to compensate Jeok Cheongang for offending him, and identifies himself as the Family Head of the Nangong Family, whom Jeok describes as the richest man in Anhui; he receives Jeok Cheongang and Taekyung at the Nangong estate and uses his internal-energy voice to order the guards to admit Taekyung when they attempt to cut off Taekyung's chained iron balls; he has one child, Nangong Ok, the family's Lesser Family Head and Sword Dragon, whom he raised with great care but acknowledges remains immature; he apologizes to Taekyung for Ok's discourtesy and asks Taekyung to prevent his father, the Azure Sky Sword King, from dueling Jeok Cheongang while agreeing to try himself.
- **Personality:** Authoritative, calculating, decisive, and conscious of the Namgung family’s position as a Murim hegemon.
- **Voice:** Composed, concise, and commanding.
- **Relationships:** Family Head of the Namgung family; commands the Hidden Thread and the Lesser Threads.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 943
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃944화



대남궁세가(大南宮世家).

펄럭이는 깃발에 수놓아진 다섯 글자를 확인한 순간, 산적의 머릿속에 떠오른 생각은 하나뿐이었다.

‘아니, 남궁세가가 왜 여기서 나와.’

물론 충분히 일어날 수 있는 일이긴 했다.

이곳은 안휘성의 동남부 끝자락에 있는 산맥이었고, 남궁세가는 명실상부한 안휘성의 패자였으니까.

그러나 남궁세가의 깃발이 인근에서 모습을 드러낸 것은, 십여 년간의 산채 생활을 해 왔던 산적으로서도 처음 겪는 일이었다.

‘남궁세가가 어째서 이런 촌구석까지…….’

호랑이가 동굴 안에만 머무른다 해도 모든 짐승은 자신들의 왕이, 이 산의 주인이 누구인지 안다.

남궁세가는 바로 그 호랑이였다.

캄캄한 동굴 대신, 안휘의 중심부이자 합비(合肥)를 장악하고 수십여 개에 달하는 문파를 휘하에 거느린 맹수.

포효 한 번이면 숱한 무림인들이 남궁세가의 깃발 아래로 결집한다. 그것이 오대세가(五代世家)의 힘이고, 영향력이었다.

‘굳이 이 험준한 산맥까지 올 만한 이유는 없을 텐데.’

서쪽으로부터 시작해서 저 멀리 동쪽 끝까지 이어지는 산맥은 그 길이만 무려 수백 리에 이른다.

그런데 그 대단한 남궁세가가 잘 닦인 대로(大路)를 놔두고, 그것도 수십여 명밖에 되지 않는 인원으로 이곳에 왔다는 건 산적으로서는 선뜻 이해하기 어려운 일이었다.

물론 그전에, 심장이 터질 것 같은 두려움이 더욱 컸지만.

‘이런 염병할. 도대체 뭐 주워 먹을 게 있다고 여기까지 오고 지랄이여.’

내심 욕설을 퍼부은 산적은 떨리는 마음을 다잡으며 조심스럽게 뒷걸음질 쳤다.

다행히 수십여 장이나 떨어져 있는 데다 그의 위치가 수풀이 울창한 언덕이라, 한껏 숨죽인 채 물러나는 것은 그리 어렵지 않았다.

스슥, 슥.

지면에 깔린 잎사귀와 나뭇가지를 피해 느릿느릿 뒷걸음질 치기를 일각 여.

이제는 발각될 위험에서 벗어났다고 확신한 산적은 참았던 숨을 토해 냈다.

“허억, 헉.”

어느덧 식은땀으로 축축해진 등허리와 풍이라도 맞은 것처럼 후들거리는 두 다리.

불과 일각 남짓한 짧은 시간이 흘렀을 뿐이지만, 막 죽을 위기에서 벗어난 산적에게는 한나절보다도 길게 느껴졌다.

“사, 살았다. 살았어.”

가까이에 있는 나무를 붙잡고 안도의 한숨을 내쉬던 산적은 문득 자신의 처지가 서글퍼졌다.

‘이놈아. 이 한심한 놈아. 대관절 이게 무슨 꼴이냐.’

산적이 된 건 후회하지 않았다.

뭘 어쩌겠나.

어찌어찌 태어나 저찌저찌 살다 보니 이렇게 된 것을.

다만 기왕 이 바닥에 몸담을 거였다면, 최소한 규모 있는 산채로 들어갔어야 했다.

녹림맹(綠林盟) 산하의 칠십이 채(七十二寨) 중 한 곳에 속해 있었다면, 남궁세가의 깃발이 보이는 것만으로 생명의 위협을 느끼지는 않았을 테니까.

‘머슴이 될 거라면, 차라리 대감집 머슴을 해라.’

술주정뱅이 아버지가 했던 말이 이토록 가슴에 와닿은 적이 있던가.

낡은 소매로 눈가를 훔친 산적은 험준하기 그지없는 산길을 되돌아가기 시작했다.

대감집이건 개집이건, 결국 머슴이 살 집인 것은 다름없다.

한시라도 빨리 산채로 복귀해서 지금쯤 연락을 받고 이곳으로 오고 있을 형제들에게 이 소식을 알려야 했다.

녹림맹 소속도 아닌 그들이 남궁세가와 맞닥트렸다가는 필시 죽은 목숨일 테니.

‘그나마 거리가 있어서 천만다행이다. 지금 당장 돌아간다면 늦지 않게 다 같이 도망칠 수 있어.’

그리고 이 숭고한 동료애에 하늘이 감동했는지, 산적은 불과 일각이 흐르기도 전에 늠름하기 그지없는 두령이 이끄는 오십여 명의 형제들과 조우할 수 있었다.

정확히는 늠름하게 뻗어 있는 두령과, 어째서인지 대가리를 박고 엎드려 있는 형제들을.

“감히 앞길을 막을 의도는 없었습니다요. 그러니 제발…….”

낯선 뒷모습. 왠지 모르게 쎄한 느낌.

모두의 앞에 우뚝 서 있는 대머리와 웬 여인에게 뭔가를 열심히 설명하고 있던 부두령이, 돌연 십여 장 밖에서 멍하니 이 광경을 지켜보고 있던 산적을 발견하고 눈을 크게 떴다.

“어?”

뭔가 이상하다. 단단히 잘못됐다.

본능적으로 위기를 느낀 산적이 황급히 신형을 돌린 그때였다.

쿡.

볼을 찌르는 손가락과 함께, 어느샌가 코앞에 나타난 불청객이 그를 물끄러미 바라보며 물었다.

“누구니, 너?”

“……!”

산적은 벼락을 맞은 듯한 충격에 몸을 부르르 떨었다.

일말의 인기척도 느끼지 못했다는 것에 한 번.

그리고 이 초대받지 않은 손님이 생각 이상으로 젊다는 것에 또 다시 한번.

‘고수……!’

등골이 서늘하다.

생사의 기로에 선 산적은 간신히 목소리를 쥐어 짜냈다.

“소, 소인은 장일. 장일이라 합니다.”

세상은 불공평한 것이 확실하다.

턱없이 젊고, 상상 이상으로 강하고, 심지어 기생 오래비처럼 생겨 먹은 그놈이 재차 물었다.

“좋아. 장일. 하는 일은?”

“나무. 나무입니다.”

“하는 일이 뭐냐고 물었는데 나무는 뭔 시벌. 숲의 정령이니? 정령왕 장퀴네스야?”

“아닙, 아닙니다. 그저 나무꾼이라고 대답한다는 것이 그만.”

“그래. 장일. 나무꾼이란 말이지.”

작게 고개를 끄덕인 그놈이 허리춤에 걸린 도끼를 힐끗 바라보았다.

“도끼도 갖고 있네. 나무꾼이라서 그런 거겠지?”

“예, 예!”

“그런데 지게는?”

“……예?”

“지게. 힘들게 장작 패서 손으로 옮길 거야?”

“그러니까, 그것이.”

잠시 머뭇거리던 산적은 다급하게 말을 이었다.

“밑에! 밑에 두고 왔습니다.”

“밑에 두고 왔다. 뭐 그럴 수 있지.”

작게 중얼거린 젊은 놈이 어깨를 으쓱했다.

“그럼 한 번 물어볼까?”

“……?”

누구에게, 라는 질문은 할 필요도 없었다.

산적이 미처 입을 열기도 전에, 젊은 놈이 무성한 수풀을 향해 바라보며 불쑥 한마디를 던졌으니까.

“이 나무꾼이 밑쪽에 지게를 두고 왔다는데, 혹시 올라오면서 못 보셨습니까?”

그 순간.

쉭.

수풀 사이를 해치는 한 줄기 바람과 함께, 홀연히 나타난 반백의 중년인이 고개를 저었다.

“아무것도 보지 못했네. 혼비백산하여 도망치는 웬 산적 하나를 제외한다면 말일세.”

“저런.”

기절하기 직전인 산적을 힐끗 바라보며 작게 혀를 찬 젊은 놈이 중년인을 향해 공손히 포권을 취했다.

“알려 주셔서 감사합니다. 남궁 대협.”

남궁세가의 가주. 천뢰검(天牢劍) 남궁룡이 마주 포권을 취하며 대답했다.

“다시 만나게 되어 반갑네, 열화신룡 진태경.”



* * *



아무리 천하가 넓다고 한들, 연이 닿아 있다면 언제고 다시 만나기 마련이다.

물론, 이 모든 것이 단순한 우연으로 이루어진 만남은 아니었지만.

“안휘성부(安徽省部)에서 연락이 왔었네. 때마침 인근에 있던 덕분에 금방 이곳까지 수 있었고.”

남궁룡의 짧은 설명을 들은 나는 고개를 끄덕였다.

“안휘성부에 전서응이 도착한 모양이군요.”

“대략 한 시진 전이었지. 천자가 직접 내린 명령이라며 그쪽에서도 난리더군.”

하긴, 남궁룡이 무슨 남궁길동도 아닌데 동에 번쩍, 서에 번쩍 나타날 수는 없는 법이다.

우리보다 한 시진 앞서 안휘성에 접어든 황실의 전서응은 즉각 성부로 이동했고, 소식을 전달받은 남궁룡이 즉시 식솔들을 이끌고 이곳으로 향한 것이 일의 전말이었다.

“그런데 위치는 어떻게 아셨습니까? 그것도 이 더럽게 넓은 산자락에서.”

“아무리 넓다 해도 길은 정해져 있는 법이지. 산세(山勢)가 험하긴 해도, 가장 빠르게 올 수 있는 길은 이곳밖에 없어.”

안휘성을 손바닥 꿰뚫듯이 훤히 들여다보고 있는 남궁세가의 가주다운 대답이다.

그러나 그것과는 별개로, 나를 바라보는 남궁룡의 낯빛에는 어두운 그늘이 드리워져 있었다.

“전부…… 사실인가?”

무엇을 묻는지는 굳이 말할 필요도 없다.

순간 무거워진 공기 속에서 적천강이 불쑥 입을 열었다.

“왜, 못 믿겠느냐?”

“그럴 리 있겠습니까. 다만 좀처럼 믿고 싶지 않은 사실이기에 다시 한번 확인코자 했을 뿐입니다.”

그 마음은 모두가 마찬가지다.

이미 하남과 사천, 운남에 이어 황도에까지 혈풍(血風)이 휘몰아친 상황.

한데 그 피비린내가 채 가시기도 전에 그보다 훨씬 더 끔찍하고, 거대한 먹구름이 밀려오고 있다니.

특히 일가(一家)의 가주인 남궁룡이라면 자신을 따르는 수많은 식솔들을 생각하지 않을 수 없었다.

“중양절. 중양절이라…….”

깊게 가라앉은 목소리로 뇌까린 그가 복잡한 눈빛으로 나를 바라보았다.

“유감일세. 설마하니 놈들이 북부 초원을 넘어 산서성을 노릴 줄이야.”

잠시 침묵하던 내가 입을 열었다.

“잘 막아 낼 수 있을 겁니다. 그들이라면 충분히.”

말을 하면서도 알고 있었다.

지금 이 대답이 본심을 숨긴, 자기 위로에 가까운 거짓말이라는 것은.

‘태원진가만으로는 무리다.’

이미 무림의 태산북두라 불리는 소림사도, 무서운 극독을 보유한 사천당문도 큰 피해를 입었다.

다행히도 청성과 아미, 그리고 남만야수궁은 피해를 최소화하여 전력을 보전할 수 있었으나 엄청난 위기가 있었던 것만은 분명하다.

한데, 이번에는 무려 암천의 본대라고 했다.

신물을 탈취하거나 한 명문 대파를 끝장내기 위한 목적이 아니라, 중원으로 향하는 교두보로 삼기 위해 벌이는 진정한 의미의 침공인 것이다.

‘최소 일만. 혹은 그 이상.’

일만이라는 어마어마한 병력조차 내 바람이 담긴 최소치에 불과했다.

지금까지의 상황이 변이 게이트였다면, 이번에는 몬스터 웨이브나 다름없다.

약 반세기 전, 마교가 십만마도(十萬魔徒)를 앞세워 무림을 휩쓸었듯이.

‘빌어먹을.’

가슴이 답답하다.

조금이라도 일찍 동천마군이 남긴 전서를 발견했다면, 혹은 그전에 로그아웃이라도 했다면 시간을 벌 수 있었을지도 모른다는 생각이 자꾸만 뇌리를 맴돌았다.

‘물론, 이미 늦어 버렸지만.’

나는 의식을 잃은 채 꼬박 사흘이라는 시간을 낭비했고, 철궤 안의 전서를 확인한 순간 발생한 퀘스트는 현실과 연결된 문에 자물쇠를 채웠다.

내 마지막 도피처이자, 안식처를 없애 버리고 앞으로 나아가라 강요하고 있었다.

마치 이것만이 내게 주어진 길인 것처럼.

‘그렇다면…… 달려 줘야겠지. 온 힘을 다해서.’

조용히 주먹을 말아쥔 나는, 뭐라 할 말을 찾지 못하고 있는 남궁룡을 향해 입을 열었다.

일말의 희망을 품은 채.

“창천검왕(蒼天劍王)께서는 어디에 계십니까?”

창천검왕 남궁천.

십왕(十王) 중에서도 세 손가락 안에 드는 초절정 고수이자, 남궁세가의 태상가주.

그가 우리와 합류하여 함께 산서로 향한다면 설령 생각했던 것 이상의 적들이 몰려와도 능히 막아낼 수 있다.

이미 내 곁에는 각각 화왕과 궁성이라 불리는 만인지적(萬人之敵)의 강자들이 있으니.

그러나 아주 잠깐 품었던 희망은, 곧이어 나직한 한숨과 함께 돌아온 남궁룡의 대답에 물거품이 되어 사그라졌다.

“아버님께서는 이미 두어 달 전부터 본가를 비우신 상황일세.”

“아.”

“안타깝지만 현재로서는 어디에 계시는지조차 모르네. 맹주이신 매종학 대협의 부탁으로 임무를 맡으셨다는 것밖에는.”

일이 이렇게 쉽게 풀리리라고는 기대하지도 않았지만, 그럼에도 슬며시 고개를 드는 실망감은 어쩔 수 없다.

“그렇군요.”

“다만 남궁세가의 가주로서 자네와 태원진가를 돕겠네. 명마와 적당한 식량, 그리고 가장 빠른 길로 안내할 식솔을 대기시켜 두었으니 곧장 출발…….”

그리고 남궁룡이 뭐라 말을 이으려던 그 순간.

크르륵, 큭.

억눌린 괴성과 함께, 그늘 속에서 한 인영이 일어났다.
```

## Final English reading copy

```markdown
# Chapter 944

The Great Nangong Family.

The moment the bandit made out the five characters embroidered on the fluttering flag, only one thought came to mind.

*Wait. What’s the Nangong Family doing here?*

Of course, it wasn’t impossible.

This mountain range lay at the southeastern edge of Anhui Province, and the Nangong Family was, by any measure, the hegemon of Anhui.

Still, even after more than ten years of living in a mountain stronghold, the bandit had never once seen the Nangong Family’s flag appear nearby.

*Why would the Nangong Family come all the way out to a backwater like this…?*

Even if a tiger stays in its cave, every beast knows who their king is, who owns this mountain.

The Nangong Family was that tiger.

Not hidden away in a dark cave, but a beast that held Hefei, the heart of Anhui, and commanded dozens of sects.

One roar was enough to rally countless martial artists beneath the Nangong Family’s flag. That was the power and influence of one of the Five Great Families.

*There’s no reason for them to come all the way to these rugged mountains.*

The mountain range stretched from the west to the distant eastern edge, running for hundreds of li.

It was hard for a bandit to understand why the mighty Nangong Family had left the well-maintained main road behind and come here with only a few dozen people.

Of course, his fear—the kind that made his heart feel ready to burst—was even greater than his confusion.

*Goddamn it. What the hell could they possibly be here to take?*

Cursing inwardly, the bandit tried to steady himself and carefully backed away.

Fortunately, he was dozens of yards away, on a hill thick with brush. It wasn’t too difficult to retreat while holding his breath.

Rustle, rustle.

For the better part of fifteen minutes, he slowly backed away, avoiding the leaves and branches scattered across the ground.

Once he was sure he’d escaped the danger of being spotted, the bandit finally let out the breath he’d been holding.

“Hah… hah.”

His back was damp with cold sweat, and both legs trembled as if he’d suffered a stroke.

Only fifteen minutes had passed, but to a bandit who’d just escaped death, it felt longer than half a day.

“I-I’m alive. I’m alive.”

Gripping a nearby tree, he sighed with relief—then suddenly felt sorry for himself.

*You pathetic fool. What a sorry state you’re in.*

He didn’t regret becoming a bandit.

What could he do about it?

He’d somehow been born, somehow lived, and somehow ended up here.

Still, if he was going to make his living this way, he should at least have joined a sizable mountain stronghold.

If he belonged to one of the Seventy-Two Strongholds under the Green Forest Alliance, he wouldn’t feel his life was in danger just from seeing the Nangong Family’s flag.

*If you’re going to be a servant, you might as well serve at a lord’s manor.*

Had his drunkard of a father ever said anything that hit so close to home?

The bandit wiped his eyes with his ragged sleeve and started back down the rugged mountain path.

Whether it was a lord’s manor or a doghouse, in the end, it was just somewhere for a servant to live.

He had to hurry back to the stronghold and tell his brothers the news. They should be on their way here by now, having received the signal.

If they ran into the Nangong Family—not being members of the Green Forest Alliance—they’d surely be dead.

*Thank God there’s some distance between us. If I head back right now, we can all get away in time.*

And perhaps Heaven had been moved by this noble display of camaraderie, because before even fifteen minutes had passed, the bandit ran into the fifty or so brothers led by their imposing chief.

More precisely, he found their imposing chief sprawled out, while his brothers were, for some reason, lying with their heads pressed to the ground.

“I never meant to block your way, sir. So please, just—”

An unfamiliar back. An ominous feeling he couldn’t explain.

The deputy chief was earnestly explaining something to a bald man and a woman standing before everyone when he spotted the bandit watching blankly from some forty yards away. His eyes widened.

“Huh?”

Something was wrong. Something had gone terribly wrong.

The bandit sensed the danger by instinct and hurriedly spun around. That was when—

Poke.

A finger jabbed his cheek. An uninvited guest had appeared right in front of him and looked him over before asking,

“Who are you?”

“……!”

The bandit shuddered as if struck by lightning.

First, because he hadn’t sensed a trace of the man’s presence.

And second, because the uninvited guest was much younger than he’d expected.

*A master…!*

A chill ran down his spine.

Standing at the edge of life and death, the bandit barely managed to squeeze out his voice.

“I-I’m Jang Il. My name is Jang Il.”

The world was definitely unfair.

The man was absurdly young, stronger than he’d imagined, and even had the looks of a pretty boy who’d grown up in a courtesan’s house. He asked again,

“Good. Jang Il. What do you do?”

“Trees. Trees.”

“I asked what you do. What the hell do trees have to do with it? Are you a forest spirit? Jangquines, King of the Spirits?”

“N-No. I meant to say I’m a woodcutter, but…”

“Right, Jang Il. A woodcutter.”

The young man gave a small nod and glanced at the axe hanging from the bandit’s waist.

“You’ve got an axe, too. Because you’re a woodcutter, I suppose?”

“Y-Yes!”

“Then where’s your carrier frame?”

“…What?”

“Your carrier frame. Are you planning to haul all that firewood by hand after chopping it?”

“Well, I…”

The bandit hesitated, then hurriedly added,

“Down below! I left it down below.”

“You left it down below. Sure, that happens.”

The young man muttered and gave a little shrug.

“Then let’s ask.”

“……?”

There was no need to ask who he meant. Before the bandit could open his mouth, the young man called toward the thick brush.

“This woodcutter says he left his carrier frame down below. Did you happen to see it on your way up?”

At that moment—

Whoosh.

A gust of wind swept through the bushes, and a silver-haired, middle-aged man appeared as if from nowhere. He shook his head.

“I saw nothing. Aside from one bandit fleeing in a panic, that is.”

“Oh, dear.”

The young man glanced at the bandit, who looked ready to faint, and clicked his tongue. Then he respectfully clasped his hands toward the middle-aged man.

“Thank you for letting me know, Great Hero Nangong.”

The Family Head of the Nangong Family, the Heavenly Thunder Sword, Namgung Ryong, clasped his hands in return.

“It’s good to see you again, Blazing Flame Divine Dragon Jin Taekyung.”

* * *

No matter how vast the world, people with a connection are bound to meet again eventually.

Of course, this meeting wasn’t simply a matter of chance.

“We received word from the Anhui Provincial Office. Luckily, we were nearby, so we were able to reach you quickly.”

I nodded at Namgung Ryong’s brief explanation.

“So the messenger eagle reached the provincial office.”

“About two hours ago. They were in quite a state over there, saying the Son of Heaven had issued the order himself.”

Well, Namgung Ryong wasn’t Namgung Gil-dong[^1]. He couldn’t just pop up in the east one moment and the west the next.

[^1]: A play on Hong Gil-dong, a legendary Korean outlaw known for appearing in one place and then another.

The imperial messenger eagle, which had entered Anhui two hours ahead of us, had gone straight to the provincial office. After receiving the news, Namgung Ryong had immediately led his family members here. That was how it had happened.

“But how did you know where we were? Especially in a mountain range this damn huge.”

“No matter how wide it is, the paths are set. The terrain is rugged, but this was the fastest way for us to reach you.”

An answer befitting the head of the Nangong Family, who knew Anhui Province as thoroughly as the palm of his hand.

Even so, a dark shadow hung over Namgung Ryong’s face as he looked at me.

“Is it all… true?”

There was no need to ask what he meant.

The air had suddenly grown heavy when Jeok Cheongang spoke up.

“What, you don’t believe him?”

“Of course I do. I only wanted to make sure, because it’s a truth I can hardly bring myself to believe.”

Everyone felt the same way.

A storm of blood had already swept through Henan, Sichuan, and Yunnan, and even reached the imperial capital.

And before the stench of blood had faded, an even more terrible, even greater storm cloud was bearing down on us.

Especially as the head of a family, Namgung Ryong couldn’t help thinking of the many people who followed him.

“The Double Ninth Festival. The Double Ninth Festival…”

He muttered in a voice weighed down with thought, then looked at me with a troubled expression.

“My condolences. I never imagined they’d cross the northern grasslands and set their sights on Shanxi Province.”

After a brief silence, I spoke.

“They’ll be able to hold them off. They’re strong enough.”

Even as I said it, I knew the truth.

This was a lie meant to hide what I really thought—something closer to an attempt to comfort myself.

*The Jin Family of Taiyuan can’t manage it alone.*

Even Shaolin Temple, called the Mount Tai and Northern Dipper of the Murim, and the Sichuan Tang Clan, with its terrifying poisons, had suffered heavy losses.

Fortunately, Qingcheng, Emei, and the Nanman Beast Palace had kept their losses to a minimum and preserved their forces. But there was no denying that they’d faced a tremendous crisis.

And now, it was Dark Heaven’s main force.

This wasn’t an attack to steal a divine artifact or destroy a single prestigious sect. It was a true invasion, intended to establish a foothold for an advance into the Central Plains.

*At least ten thousand. Maybe more.*

Even the staggering number of ten thousand was only my hopeful estimate of the minimum.

If everything so far had been a mutation Gate, this was no different from a monster wave.

Just as the Demonic Cult had swept through the Murim half a century ago, leading a hundred thousand demonic fighters.

*Damn it.*

My chest felt tight. I couldn’t stop thinking that if I’d found the missive left by the Eastern Heaven Demon Lord even a little sooner—or if I’d logged out before then—we might have gained some time.

*Of course, it was already too late.*

I’d lost three full days unconscious, and the moment I checked the missive in the iron chest, the Quest that appeared locked the door connecting me to reality.

It had taken away my last refuge, my place of rest, and forced me to move forward.

As if this were the only path I’d been given.

*Then… I’ll have to run. With everything I’ve got.*

Quietly clenching my fist, I turned to Namgung Ryong, who seemed unable to find the words.

With the faintest glimmer of hope, I asked,

“Where is the Azure Sky Sword King?”

Nangong Cheon, the Azure Sky Sword King.

A Supreme Peak master counted among the top three of the Ten Kings, and the Grand Family Head of the Nangong Family.

If he joined us and traveled with us to Shanxi, we could hold off even more enemies than we’d expected.

I already had two peerless fighters at my side, each a match for ten thousand men: the Fire King and the Bow Saint.

But the hope I’d briefly allowed myself to feel soon faded into nothing when Namgung Ryong’s answer came with a quiet sigh.

“My father has been away from the family estate for the past couple of months.”

“Ah.”

“I’m afraid we don’t even know where he is right now. All we know is that he took on a mission at the request of Great Hero Mae Jonghak, the Alliance Leader.”

I hadn’t expected everything to go so smoothly, but I couldn’t help the disappointment that quietly rose in me all the same.

“I see.”

“Still, as Family Head of the Nangong Family, I’ll help you and the Jin Family of Taiyuan. I’ve had fine horses, a reasonable supply of food, and a family member to guide you by the fastest route standing by, so you can set off at once…”

Just as Namgung Ryong began to continue—

Grrk. Krrk.

With a muffled, strangled growl, a figure rose from the shadows.
```
