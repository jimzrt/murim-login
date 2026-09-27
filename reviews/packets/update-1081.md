<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1081.txt",
      "sha256": "86695fb029f6edbb59975c86d1dc37ad4ba2f7c1d43e2775841e656d1ae0d570",
      "bytes": 11500
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "56ee3af575ae34e3a5bef23ded42b9e1e820cf16b7bc67e9dab8185d3b207a22",
      "bytes": 1250
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "73d0b9793e39bf1ab8230a23f587e74511cf7357ed4b4f1c5ed21df325d4abfe",
      "bytes": 243192
    },
    {
      "path": "characters/Cheongheoja.md",
      "sha256": "b2637b9b8596927ddb9441f03b6796c4956ace80387bfa09b348a5649818a965",
      "bytes": 544
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "1b94561e19fbff3087160073b577125d92e4eb3644ff590bcf74d8913bd9b6b6",
      "bytes": 1115
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "49055bd4aab671ccaa91af3eef0d4720ae46ae4fd8601bf049beecd8555c5f8e",
      "bytes": 760
    },
    {
      "path": "characters/Eastern Heaven Demon Lord.md",
      "sha256": "6b18b2b590c3b2625c4de47b51cab4d7cdebbe955e0372f9a7061508c9aff7af",
      "bytes": 839
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "406022ab91f8640b9d06a3edca288ebf278fb1cf5ca752110bf4c60f46d13a63",
      "bytes": 490
    },
    {
      "path": "characters/Hak Su.md",
      "sha256": "6c00e3ec8f644e8d397228297a3d42c191b437cfcd68ee91b39a5c580c3ee962",
      "bytes": 615
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "edbae3bb561d3964e3e2936b455026938cc3d8a91bf03743624828d21bb296b5",
      "bytes": 1502
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "7396b4729594b94ec7a1daad247f1e99a8acecb5a16acd447e887f4095bdd764",
      "bytes": 700
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "76904c6248574fb81eafc186bad81aa7932bfaa7cf00350a00e24d02bdd23547",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "3ff91a4b56b236371a25c4ad6e7d68bd3e279abfe2655f850a41471f6dac3548",
      "bytes": 623
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "e958483d1b8130dda70114fad55f4f1a89c2fe92ef2e8e9caf549bfd1c064eed",
      "bytes": 700
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "3d594ddb72d884e7bfd3f9a24ae809be06b0463fb5b1d9e16bbb0226f040aeb1",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1f5e163732c9516193969d12cde0c91050cbf77d3192d8b0b9b4c11686fa02b5",
      "bytes": 286270
    }
  ],
  "estimated_tokens": 12645
}
-->

# Durable State Update — Chapter 1081

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
1 and safe_through 1081. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1081. Profile updates may replace only one
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
  "chapter": 1081,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1081,
    "continuity_sources": [1081],
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
    "Xining is Qinghai’s capital and a stronghold against Dark Heaven; crowds from across the province have gathered there.",
    "Xining’s food stores can sustain its people for at most fifteen days; the City Lord and officials implicated in corruption have been detained.",
    "Kunlun Sect First-Generation Disciple Hak Eui has met Jin Taekyung and addressed him as a Great Hero.",
    "Hak Su is Cheongheoja’s Senior Disciple, Hak Woo’s senior brother, and a possible successor to Kunlun Sect leadership.",
    "Taekyung believes the Lord of Heaven does not want him killed, but does not know why.",
    "The black-robed captive survived interrogation and treatment and can now speak; Mujin is to talk with him."
  ],
  "continuity_sources": [
    1079,
    1080
  ],
  "open_questions": [
    "Who is the black-robed captive, and what does he know?",
    "Why did the Lord of Heaven spare Taekyung in Gansu, and what is his real purpose?",
    "Will the Alliance Leader and other righteous warriors reach Qinghai?",
    "What is the hidden ember Cheongheoja warned about?",
    "How will Xining secure food for its gathered refugees?"
  ],
  "safe_through": 1080,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 청풍     | **Cheongpung**     |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 곤륜파    | **Kunlun Sect**                  |
| 무림맹    | **Murim Alliance**               |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 문주     | **Sect Leader**                              |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 하남     | **Henan**              |
| 청해     | **Qinghai**            |
| 곤륜     | **Kunlun**             |
| 본좌      | **I / this lord** only when deliberately grandiose              |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 도사      | **Daoist**                                                      |
| 청허자 | **Cheongheoja** | Kunlun Sect Leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 동천마군 | **Eastern Heaven Demon Lord** | Title of the absurd masked antagonist in Jin's nightmare. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 학수 | **Hak Su** | Cheongheoja’s Senior Disciple and Hak Woo’s senior brother. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 평화 | **Peace Guild** | Guild name. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 곤륜운룡 | **Kunlun Cloud Dragon** | Epithet of a Kunlun Sect young prodigy. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 시리 | **City** | Second word in one of the necromantic chants. |
| 소하 | **Xiao He** | Historical civil official invoked in the same exchange. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |
| 청해호 | **Qinghai Lake** | Destination of the retreat; distinct source form from 청해성. |

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
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 상인 | 청년 | stranger_to_stranger | Young Brother | formal-polite | A merchant uses 소형제 after noticing the young man's sword, and the young man approves of the address. |
| 청년 | 상인 | stranger_to_stranger | friend | casual and shameless | The young man declares that they should be friends after drinking their Yeoahong. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 정호 | 진태경 | Shaolin Discipline Hall Master to patient and Benefactor | Benefactor Jin | formal-polite | Jung Ho repeatedly uses 진 시주 and 시주. |
| 진태경 | 정호 | patient to Shaolin Discipline Hall Master | Monk | polite and familiar | Taekyung addresses Jung Ho as 스님. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 진태경 | 정호군 | young martial artist to senior imperial officer | Commander Jeong | casual and teasing, then conciliatory | Jin addresses him by rank while trying to defuse the standoff. |
| 정호군 | 태산 | guard officer questioning a performer | you | blunt and direct | He calls Taishan forward and asks whether he belongs to the circus troupe. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 적천강 | 동천마군 | enemies | you | blunt and informal | Jeok Cheongang addresses the Eastern Heaven Demon Lord with hostile familiarity. |
| 동천마군 | 적천강 | enemies | you | informal | The Eastern Heaven Demon Lord speaks to Jeok Cheongang during their duel. |
| 진태경 | 동천마군 | young martial artist confronting an enemy | ugly-ass big bro | casual, profane, and taunting | Jin calls out to the Demon Lord after returning to the hall. |
| 동천마군 | 진태경 | enemy recognizing the spear wielder | Jin Taekyung | shouted, informal | The Demon Lord cries Taekyung's name after identifying him as the spear's owner. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 정호군 | 진태경 | imperial officer responding to the Marquis of Shangshan | Marquis of Shangshan | formal and deferential | Accepts the command with a formal acknowledgment of Taekyung’s title. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 태산 | 대인 | ally addressing an elder | Sir | informal and enthusiastic | Calls out to the Great Sir while praising his shot. |
| 대인 | 태산 | elder addressing a younger ally | young friend | familiar and playful | Offers Taishan a portion of the bird as a reward. |
| 적천강 | 청허자 | senior martial master to former acquaintance and younger martial master | you / Fellow Daoist | blunt and familiar | Jeok Cheongang mocks Cheongheoja for addressing him as a fellow Daoist. |
| 궁성 | 청허자 | fellow martial master and former acquaintance | Cheongheo | polite and familiar | Uses his shortened name and remarks on his graying hair. |
| 살성 | 청허자 | fellow martial master and former acquaintance | you | blunt and familiar | Recognizes him from a prior meeting. |
| 청풍 | 청허자 | younger martial artist to senior sect leader | Grandpa Cheongheoja | cheerful and polite | Uses a friendly, familial form because they share the surname Cheong. |
| 태산 | 청허자 | younger martial artist to senior sect leader | you | clipped and childlike | Asks whether Cheongheoja brought meat. |
| 진태경 | 청허자 | younger martial artist to senior sect leader | Sect Leader | respectful | Uses a formal greeting and bow. |
| 청허자 | 진태경 | senior sect leader to younger martial artist | Fellow Daoist Jin | warm and polite | Greets Taekyung by surname and confirms Hak Woo is well. |
| 학수 | 진태경 | Kunlun Senior Disciple to visiting martial artist | Fellow Daoist Jin | polite and respectful | Addresses Taekyung as 진 도우. |
| 학의 | 진태경 | Kunlun Sect disciple to renowned martial artist | Great Hero Jin Taekyung | formal and deferential | Uses 진태경 대협 when introducing himself and greeting Taekyung. |
| 청해성주 | 진태경 | city official to imperial marquis | Marquis of Shangshan | extremely deferential | Uses 상산후 while responding to Taekyung. |

## Listed compact profiles

### Cheongheoja.md

# Cheongheoja (청허자)

- **Safe through:** Chapter 1078
- **Aliases:** None
- **Role:** Cheongheoja is the Kunlun Sect Leader and Hak Woo’s master.
- **Personality:** Warm, composed, and patient, he faces setbacks with resolve and receives even startling company with good humor.
- **Voice:** Measured and gentle, using formal Daoist courtesies and calm metaphors.
- **Relationships:** Hak Woo is his Disciple; he knows Jin Taekyung by reputation and treats him warmly.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1079
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has also learned concealment from the Slaughter Saint.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, competitive pride, unusual resistance to monster-induced Fear, and discomfort when someone copies his martial arts.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival, and the Slaughter Saint has become his mentor in concealment.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1080
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Eastern Heaven Demon Lord.md

# Eastern Heaven Demon Lord (동천마군)

- **Safe through:** Chapter 1077
- **Aliases:** Wei Zhong
- **Role:** The Eastern Heaven Demon Lord was Wei Zhong, the East Depot’s Seal-Holding Eunuch and a former Maoshan Sect disciple who commanded the dead with a bell; Jin Taekyung killed him with blue-white flames.
- **Personality:** His hatred grew from losing his family and sect, but recognizing his own lonely childhood in Zhu Bao ultimately moved him to relinquish his vengeance and choose a less harmful final act.
- **Voice:** He speaks in measured, almost lyrical phrasing, recounting the past before turning to pointed accusations.
- **Relationships:** Ma Sanbao is his Disciple; he holds the Emperor responsible for Taizu’s actions against the Maoshan Sect.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1080
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed and observant, he reserves judgment about rumors until meeting their subject.
- **Voice:** Calm and measured, with reflective phrasing and formal deference.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Hak Su.md

# Hak Su (학수)

- **Safe through:** Chapter 1079
- **Aliases:** None
- **Role:** Hak Su is Cheongheoja’s Senior Disciple and a senior brother to Hak Woo in the Kunlun Sect.
- **Personality:** Gracious and hopeful, he responds to Taekyung’s mistakes with patience and warmth.
- **Voice:** He speaks in courteous, formal phrases and tempers earnest reassurance with hearty, lightly humorous remarks.
- **Relationships:** Cheongheoja is his Master, and Hak Woo is his youngest Junior Brother; he treats Jin Taekyung warmly as a Fellow Daoist.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1080
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 1080
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1080
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1080
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 1080
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1076
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
1081화




“곤륜파 일대제자 학의, 열화신룡 진태경 대협을 뵙습니다.”

호리호리한 체구와 청수한 인상.

더불어 과하지도, 부족하지도 않은 자연스러운 태도까지.

청년과 장년 그 사이쯤으로 보이는 그는 마치 도사(道士)의 전형과도 같았고, 시선이 맞닿은 순간부터 이미 그의 정체를 짐작하고 있던 나는 마주 고개를 숙였다.

“처음이군요. 이렇게 뵙는 건.”

상대의 신분을 모른다면 할 수 없는 대답이었지만, 학의는 조금의 미동도 없이 담담하게 대꾸했다.

“제 하나뿐인 사제(師弟)는 도사치고 제법 말이 많은 편이지요. 그런 의미에서 빈도에 대해 이미 어느 정도는 들어서 알고 계시리라 생각했습니다.”

곤륜운룡 학운의 바로 맏사형이자, 학수의 사제이며, 청허자의 두 번째 제자이기도 한 그를 향해 나는 턱을 긁적였다.

“아무리 이 자리에 없다지만, 하나뿐인 사제에 대한 평가로는 좀 박한 것 같은데요.”

“괜찮습니다. 설령 이 자리에 있었더라도 같은 말을 했을 테니.”

이래서 겉모습으로 판단하지 말라는 말이 생긴 건가.

청수한 인상과는 어울리지 않게도, 냉정하게 팩트를 찌르는 화법을 구사한 학의가 머뭇거림 없이 입을 열었다.

“앞서 진 대협께서는 제대로 된 이야기를 해 보자고 하셨는데, 그 전에 한 가지 여쭤볼 것이 있습니다.”

내가 긍정의 의미를 담아 어깨를 으쓱하자, 학의가 말을 이었다.

“혹, 조금 전 끌려 나간 청해성주와 그 측근들을 어찌 처분하실 생각입니까?”

조금은 뜬금없게 느껴지는 물음이었지만, 나는 선선히 대답했다.

“당연히 참수(斬首)할 생각입니다. 날이 밝은 후, 모두가 보는 앞에서.”

이건 오래전부터 정해진 결과다.

애당초 청해성주가 지금껏 탐관오리로서 착실하게 살아남을 수 있었던 이유도 천자와 동천마군의 대립 때문이었지, 그의 부정 축재는 이미 한참 전부터 금의위의 이목을 끌고 있었다.

결국 그 칼자루를 누가 넘겨 받았냐의 차이일 뿐, 최후에 잘려 나갈 목의 주인은 정해져 있었다는 뜻이다.

‘더군다나 지금 같은 상황에서는, 저런 인간이 살아남는 게 말이 안 될 정도지.’

평화가 길었던 것은 대국 역시 마찬가지.

청해성주는 그간 뒤꽁무니로 열심히 군량을 팔아 황금을 채웠고, 그런 놈 밑에서 군대가 제대로 돌아갔을 리는 만무하다.

그야말로 참수 말고는 답이 없다시피 한 수준.

하지만 다음 순간 들려온 학의의 한 마디는, 생각했던 범위를 훌쩍 벗어나는 것이었다.

“안 됩니다.”

“……!”

“……!”

“그 결정, 재고(再考)해 주시지요.”

단호한 음성에 전각 내부의 분위기가 술렁였고, 이는 당연한 결과였다.

앞서 그들의 처분에 대해 물어본 것이 단지 뜬금없는 수준이라면, 이건 주제를 넘은 일이니까.

제아무리 천자의 선포로 인해 관무불가침(官武不可侵)의 원칙이 희미해졌다고는 해도 정도라는 것이 있다.

곤륜파 장문인의 둘째 제자라는 신분으로는 넘을 수 없는, 최소한의 선이.

그리고 그 보이지 않는 선을 넘어간 학의의 모습에, 가장 먼저 반응한 한 사람이 있었다.

“도(道)를 좇느라 법(法)은 배우지 못했나 보군. 말을 삼가게, 곤륜파의 도사.”

평소와 다를 것 없는 무뚝뚝한 목소리였지만, 나는 학의를 바라보는 정호군의 눈빛에 은은한 노기가 담겨 있음을 알아차렸다.

그런 정호군의 기세에 긴장하는 몇몇 사람들과는 반대로, 아무런 말 없이 제자를 지켜보는 청허자의 모습도 함께.

‘성격은 자세히 모르지만, 이런 상황에서도 마냥 손 놓고 있을 양반은 아닌 것 같은데.’

싸는 놈 따로 있고 치우는 놈 따로 있다고.

제자가 잘못을 저질렀다면 스승이 나서서 수습하는 것이 보통이다.

심지어 한 성깔 하기로는 천하에서 첫손가락에 꼽는 적천강조차도, 내가 사리에 맞지 않는 행동을 한다면 종종 잊지 않고 지적해 왔다.

물론 그보다 먼저 앞뒤 안 가리고 내 편부터 들고 봤지만.

‘하지만 청허자는 다르지.’

청해호의 강가에서 청허자가 개노답 삼형제를 대하는 것을 보며 저 노도사의 인격이 최소 성자의 반열에 다다랐음을 깨달은 나다.

그런 그가 상황을 지켜보고만 있다는 것에는, 충분히 이유가 있을 거라는 생각이 들었다.

“그렇다면, 이유는?”

“……상산후.”

학의를 향해 불현듯 내뱉은 물음에 정호군이 미간을 좁혔지만, 나는 아랑곳하지 않고 학의를 향해 재차 물었다.

“말해 보세요. 굳이 그놈들을 살려 둬야 하는 이유를.”

하늘의 도리(道理)를 따라 최대한 살생을 피하고자 하는 한 사람의 도사로서의 자비일까. 아니면 또 다른 이유일까.

이쯤 되니 사뭇 그 이유가 궁금하기까지 한 상황.

모두의 시선이 집중된 그 순간, 굳게 닫혀 있던 학의의 입술이 열렸다.

“그런 말씀을 드린 기억은 없습니다만.”

“응?”

“저는 어디까지나 참수형을 재고해 달라고 청했을 뿐입니다.”

“아니, 그러니까 그게.”

도대체 뭐가 다르냐고 물어보려던 그때, 학의가 단호한 어조로 덧붙였다.

“참수형은 너무 관대한 처사입니다. 백성들이 보는 앞에서 능지처참(凌遲處斬)을 하시지요.”

“……어?”

“이럴 때일수록 일벌백계(一罰百戒)가 필요한 법. 지난 며칠간 성내의 상황을 면밀히 조사해 본 바로는, 능지처참도 살짝 아쉬운 감이 있을 정도입니다.”

“……!”

“……!”

일순간 침묵에 휩싸인 전각 내부, 흥미로운 눈빛으로 상황을 지켜보던 적천강이 문득 중얼거렸다.

“걸작이구먼.”

옆자리에 앉아 있던 살성과 궁성도 떨떠름한 얼굴로 입을 열었다.

“그, 아무래도 도사가 아닌 것 같은데.”

“아니, 곤륜파가 어찌 이렇게…….”

큰 어르신들의 탄식이 이어지던 그때, 얼빠진 표정으로 학의를 멍하니 바라보는 사람들의 모습에 고개를 갸웃거리던 개노답 삼형제가 쑥덕거렸다.

“와, 능지처참이라는 말 처음 들어 봐요. 근데 그게 도대체 뭐예요?”

“태산이, 안다.”

자신 있게 대답한 태산이 군침을 삼키며 말을 이었다.

“예전에 먹어 본 적 있다. 매우 맛있었다.”

아니, 그럴 리가 없는데.

“아하. 그런 요리도 있었구나. 전 못 먹어 봤는데. 대인 아저씨는 드셔 보셨어요?”

“그런 요리가 세상천지에 어디 있나. 하여간 요새 젊은것들은.”

정상인이 빙의라도 했는지, 웬일로 한심하다는 눈빛으로 태산과 청풍을 흘겨본 대인이 덧붙였다.

“능지처참은 요리가 아닐세. 별호지. 한때 천하를 공포로 몰아넣었던 어느 대마두의.”

헉, 하고 동시에 헛숨을 들이켠 청풍과 태산이 눈을 동그랗게 뜬 채 앞다투어 물었다.

“그 대마두는 어떻게 됐나요?”

“어떻게 되긴. 본좌의 손에 쓰러졌지.”

아니, 그럴 리가 없다니까.

“헙. 그럼 그때 태산이가 먹었던 게…….”

“미치고 환장하겠군. 아닐세.”

전적으로 동의하지만, 저걸 왜 저 인간이 말하는 거지.

“태산이, 정말 까맣게 몰랐다. 대마두가 그렇게 맛있을 줄이야.”

“거참, 아니라고 몇 번을 말하나.”

지금까지 딱 두 번 말했고, 심지어 대마두도 아니다.

“아니다. 진짜 먹었다.”

“……그래?”

이제 와서 설득당하지 마. 제발.

‘진짜 미친 새끼들인가.’

능지가 처참한 대화에 순간 정신이 혼미해진 내가 어지럼증을 호소하고 있던 그때, 늙수그레한 목소리가 불현듯 울려 퍼졌다.

“도(道)를 좇으라 그리 말했거늘, 스승이 부덕하여 제자에게 충분한 가르침을 내리지 못한 모양입니다.”

곤륜파 장문인, 청허자가 마침내 침묵을 깨트리며 꺼낸 한마디에 학의가 작게 고개를 숙였다.

“죄송합니다. 스승님.”

말과는 달리 전혀 죄송해 보이지 않는 표정.

하지만 지금 이 순간 그가 어떤 마음을 품고 있건, 내게는 중요하지 않았다.

다만 앞서 모두를 충격에 빠트린, 예상 밖의 대답에 담겨 있던 사실만을 주목할 뿐이었다.

“아닙니다. 이대로 계속하시죠. 제자분께서는 아직 할 말이 한참 남아 보이는데.”

숙여 있던 학의의 고개가 천천히 들린다. 나를 똑바로 응시하는 그의 시선에 이채가 스쳤다.

“무엇을 말입니까?”

“직접 말했잖습니까. 지난 며칠간, 그것도 아주 면밀하게 조사해 봤다고. 사실은 처음부터 그 말을 하고 싶었던 거 아니에요?”

“……!”

“아, 지난 며칠간이 아니라 줄곧 그러셨던 건가.”

수십여 명이 자리한 거대한 탁자 너머, 정곡을 찔렸는지 살짝 커지는 학의의 눈동자에 나는 내심 실소를 흘렸다.

그와 나는 아직 젊다.

아니, 청해성의 크고 작은 대소사를 좌지우지하는 여러 문주들이나 이 자리에 동석한 곤륜의 여러 중진들에 비교하면 젊다 못해 새파랗다.

그러나 이와 같은 공통점 속에서도, 서로의 위치는 하늘과 땅 차이다.

몇 안 되는 상석(上席)을 차지할 수 있는 나와는 달리, 지금의 그가 말석(末席)에 자리한 것처럼.

그렇기에 더더욱 발언권이 필요했을 것이다.

모두의 이목이 집중된 바로 지금 이 순간처럼.

“말씀하세요. 허심탄회하게. 아무도 뭐라 안 합니다. 그렇죠?”

“물론이다.”

내 말을 받아 준 적천강이 사람 좋은 미소와 함께 덧붙였다.

“불만 있는 놈은 지금 손들어라. 노부가 친히 설득해 줄 테니.”

당연히 아무도 손을 들지 않았고, 회의는 밤새도록 이어졌다.

그리고 길었던 밤이 끝난 후, 청해성주를 포함한 십여 명의 죄인들이 수많은 민중들의 욕설을 받으며 길거리에 끌려 나온 그때.

삐이잇!

마치 그들의 최후를 암시하듯, 날카로운 울음소리와 함께 드높은 하늘을 가로질러 도착한 한 마리의 날짐승이 있었다.

아니.

전서응(傳書鷹)이.



- 하남(河南), 무림맹(武林盟).



전서에 적힌 그 다섯 글자를 말없이 바라보던 나는 크게 숨을 삼켰다.

그리고 다음 순간.

스륵.

마침내 펼친 전서에 적힌 내용을 보자마자, 전신의 솜털이 곤두서는 듯한 감각에 사로잡혔다.

“……제기랄.”

불현듯 흘러나온 욕설과 함께 바라본 하늘은 어두웠고, 그 아래에서 휘둘려진 망나니들의 칼날은 잔혹하게 번뜩였다.

서걱!

떨어지는 수급 아래, 거대한 함성이 터져 나오고 있었다.
```

## Final English reading copy

```markdown
# Chapter 1081

“I am Hak Eui, a First-Generation Disciple of the Kunlun Sect. It’s an honor to meet you, Great Hero Jin Taekyung, the Blazing Flame Divine Dragon.”

Slender build. Refined features.

And a natural manner—not too much, not too little.

He looked somewhere between a young man and a middle-aged one, the very picture of a Daoist. I’d guessed who he was the moment our eyes met, so I bowed in return.

“This is the first time we’ve met like this.”

I couldn’t have said that without knowing who he was. Hak Eui replied calmly, without the slightest change in expression.

“My one and only Junior Brother is rather talkative for a Daoist. So I assumed you’d already heard a thing or two about me.”

I scratched my chin as I looked at the man who was the eldest Senior Brother of Kunlun Cloud Dragon Hak Unui, Hak Su’s Junior Brother, and Cheongheoja’s second Disciple.

“Even if he’s not here, that seems a bit harsh for a judgment of your one and only Junior Brother.”

“It’s all right. I would’ve said the same thing if he were here.”

So that was why people said not to judge by appearances.

Despite his refined looks, Hak Eui had a way of coldly stating the facts. Without hesitation, he continued.

“Earlier, Great Hero Jin, you said we should have a proper discussion. Before that, there’s something I’d like to ask.”

I shrugged in assent, and Hak Eui went on.

“What do you intend to do with the City Lord of Qinghai and his associates who were just taken away?”

The question felt a little out of the blue, but I answered readily.

“Of course I intend to behead them. At daybreak, in front of everyone.”

The outcome had been decided long ago.

The City Lord of Qinghai had been able to live so comfortably as a corrupt official because of the conflict between the Son of Heaven and the Eastern Heaven Demon Lord. His embezzlement had drawn the Embroidered Uniform Guard’s attention a long time ago.

In the end, it was only a question of who would take up the sword. The owner of the neck to be cut had already been decided.

*And in a situation like this, it’d be ridiculous to let a man like him live.*

Peace had lasted a long time in the Great Nation, too.

The City Lord of Qinghai had spent years lining his pockets with gold by selling off military provisions behind everyone’s backs. There was no way the army could have been functioning properly under a man like him.

There was hardly any answer but beheading.

But Hak Eui’s next words went well beyond anything I’d expected.

“No.”

“...!”

“...!”

“I ask you to reconsider that decision.”

His firm voice sent a stir through the pavilion. Naturally.

If asking what I planned to do with them had been a little out of the blue, this was overstepping.

Even if the Son of Heaven’s decree had weakened the principle that officials and martial artists must not interfere with one another, there were still limits.

A line that someone of Hak Eui’s standing—the Kunlun Sect Leader’s second Disciple—couldn’t cross.

And the first person to react to Hak Eui stepping over that unseen line was—

“Perhaps you pursued the Dao and never learned the law. Mind your words, Daoist of the Kunlun Sect.”

Jeong Hogun’s voice was as blunt as ever, but I noticed a faint anger in his eyes as he looked at Hak Eui.

While some people tensed beneath Jeong Hogun’s aura, Cheongheoja watched his Disciple in silence.

*I don’t know him well, but he doesn’t seem like the sort to sit back and do nothing in a situation like this.*

One person makes the mess; another cleans it up.

When a Disciple did something wrong, the Master usually stepped in to handle it.

Even Jeok Cheongang, who ranked among the most hot-tempered men in the world, would sometimes remember to call me out when I acted unreasonably.

Of course, he’d take my side without a second thought first.

*But Cheongheoja is different.*

Watching Cheongheoja deal with the hopeless trio by the shores of Qinghai Lake had convinced me that the old Daoist’s character was practically saintly.

If a man like him was simply watching the situation unfold, there had to be a good reason.

“Then why?”

“...Marquis of Shangshan.”

Jeong Hogun frowned when I suddenly spoke to Hak Eui, but I ignored him and asked Hak Eui again.

“Tell me. Why should those bastards be kept alive?”

Was this the mercy of a Daoist who followed the Way of Heaven and wanted to avoid taking lives as much as possible? Or was there another reason?

By now, I was genuinely curious.

Everyone’s attention fixed on him. At last, Hak Eui’s tightly closed lips parted.

“I don’t remember saying that.”

“Hm?”

“I only asked you to reconsider beheading them.”

“No, I mean, isn’t that—”

I was about to ask what the difference was when Hak Eui added, his tone firm:

“Beheading is far too lenient. Have them executed by slow slicing in front of the people.”

“...What?”

“At times like this, one punishment should serve as a warning to a hundred. Based on the close investigation I’ve conducted into the city’s affairs over the past few days, even slow slicing seems a little too lenient.”

“...!”

“...!”

Silence fell over the pavilion. Jeok Cheongang, who’d been watching with interest, muttered under his breath.

“What a masterpiece.”

The Slaughter Saint and the Bow Saint, seated beside him, spoke with dubious expressions.

“Is he... sure he’s a Daoist?”

“How did the Kunlun Sect end up like this...”

As the elders sighed, the hopeless trio tilted their heads at the sight of everyone staring blankly at Hak Eui, then whispered among themselves.

“Wow, I’ve never heard of ‘slow slicing’ before. What does that even mean?”

“Taishan knows.”

Taishan answered confidently, swallowing as he continued.

“I ate it once. It was very tasty.”

No, that couldn’t be right.

“Oh! So it’s a kind of dish. I’ve never tried it. Great Sir, have you?”

“What sort of dish could that possibly be? Honestly, young people these days.”

For once, Great Sir looked at Taishan and Cheongpung with an expression of pure contempt, as if a normal person had possessed him. Then he added:

“‘Slow slicing’ isn’t a dish. It’s a sobriquet. The name of a great fiend who once terrorized the whole world.”

Cheongpung and Taishan gasped at the same time. Their eyes went wide, and they eagerly asked:

“What happened to that great fiend?”

“What do you think? He fell to this lord’s hand.”

No, that couldn’t be right.

“Gasp! Then what Taishan ate back then was...”

“This is driving me insane. No, it wasn’t.”

I agreed completely, but why was that guy the one saying it?

“Taishan really didn’t know. Who knew a great fiend could be so tasty?”

“How many times do I have to tell you? That’s not what it was.”

He’d said it exactly twice so far—and it hadn’t even been a great fiend.

“No. Taishan really ate it.”

“...Really?”

Don’t let him convince you now. Please.

*Are these guys actually insane?*

Their intelligence had suffered a thousand cuts, and my head was spinning from listening to them. Just then, an old man’s voice rang out.

“I urged you to follow the Dao, yet it seems this unworthy Master failed to teach his Disciple well enough.”

At last, the Kunlun Sect Leader, Cheongheoja, broke his silence. Hak Eui bowed his head slightly.

“I’m sorry, Master.”

His expression didn’t look sorry at all.

But whatever he was thinking right now didn’t matter to me. I was only interested in what his unexpected answer had revealed—the fact that had just shocked everyone.

“No need. Go on, then. Your Disciple still seems to have plenty to say.”

Hak Eui slowly raised his bowed head. A glint passed through his eyes as he looked straight at me.

“What do you mean?”

“You said it yourself. You’ve spent the past few days investigating, and doing so very thoroughly. Wasn’t that what you wanted to talk about from the start?”

“...!”

“Oh, was it not just the past few days? Have you been at it all along?”

Across the enormous table, where dozens of people were seated, Hak Eui’s eyes widened slightly. I could tell I’d hit the mark, and I let out a quiet laugh to myself.

He and I were both young.

No—we were young compared to the Sect Leaders who held sway over Qinghai’s affairs and the Kunlun elders seated here.

But even with that in common, our positions were worlds apart.

I could claim one of the few seats at the head of the table. He had to sit at the far end.

That was all the more reason he’d need a chance to speak.

Like this moment, with everyone’s attention fixed on him.

“Go ahead. Speak freely. Nobody’s going to object, right?”

“Of course not.”

Jeok Cheongang answered for me, adding a genial smile.

“If anyone has a problem, raise your hand now. This old man will personally persuade you.”

Naturally, no one raised a hand. The meeting continued through the night.

And when the long night ended, a dozen or so criminals—including the City Lord of Qinghai—were dragged into the streets amid the curses of a vast crowd.

A shrill cry rang out.

A bird of prey streaked across the high sky and arrived as if heralding their end.

No.

A messenger eagle.

—

**Henan, Murim Alliance.**

I stared silently at the five characters written on the missive, then drew in a deep breath.

And the next moment—

*Rustle.*

As soon as I unfolded the message and read its contents, a shiver ran through me, raising the hairs all over my body.

“...Damn it.”

The sky above me was dark as I looked up, the curse slipping out before I could stop it. Beneath it, the executioners’ blades flashed cruelly.

*Shhk!*

As a severed head fell, a tremendous roar erupted.
```
