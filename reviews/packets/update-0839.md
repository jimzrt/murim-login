<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0839.txt",
      "sha256": "3353c73359f55d93c78ca4053ce611c23d00cc309a45c3eed76aa915550e41ca",
      "bytes": 12870
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "40e4412219bc55614044bef26c50533b551fdff65d155906e8a5f123548dfddb",
      "bytes": 2360
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2ac235886e36b4a9cfac67990c4e303d5cbbbaacdc20104970ce04b7ba9ca08c",
      "bytes": 227427
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "82500d052accc369e94305323f9aaaf3c29bb65a349c23522b147081e1557222",
      "bytes": 1888
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "678145775e4a7c32a8ab8938038b0687aa5b1b35678cf22fab47d2ed9a3a8fc0",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "81262f9d5526c144a7b624501bab1be99e59b721f54df08672507c87f97e0569",
      "bytes": 937
    },
    {
      "path": "characters/Ju Wongong.md",
      "sha256": "059b0c35a0b17c641bdf9b2338ed9551b12f01321b121619045b9ba315d71cc0",
      "bytes": 801
    },
    {
      "path": "characters/Namho.md",
      "sha256": "284f7fad3277eafb1bc8944524a178cba67dca0b2430289d6869cefb54ff80ff",
      "bytes": 936
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "e99c367383965c677dbdae4410497d38955e2882730af4e855efcfde86f7a74f",
      "bytes": 787
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "57e990740e8fe374c7e1dfc5de9b88dcc12833ec0d46adad8187b18ffc1573d9",
      "bytes": 822
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "09e949f005b5795b16fad277a81c1f21e02de6791b5fe89fcaa527acd7216eaa",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2d3ba6654cdbcc372510ec72e3979b0d7dd3413b49d0a44c281c59171f618c6d",
      "bytes": 251874
    }
  ],
  "estimated_tokens": 12421
}
-->

# Durable State Update — Chapter 839

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
1 and safe_through 839. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 839. Profile updates may replace only one
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
  "chapter": 839,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 839,
    "continuity_sources": [839],
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
    "Jin erased the Doppelganger, but Main Quest [Cataclysm] and its “Stop the Summoning” mission failed.",
    "The Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "Jin was transferred to Murim while unconscious and awakened in Nanman after several days.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin saw a vision of a black-haired man killing Ahomed after the ritual; whether it was real remains unknown, and Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury around his lower dantian remains unresolved; leveling up did not heal it.",
    "Jeok Cheongang went to Sichuan to bring the Divine Physician, his former Disciple, to treat Jin.",
    "Ju Wongong is temporarily acting City Lord of Sichuan Province by imperial order while still under exile.",
    "Jin intends to use Wongong’s authority and government manpower to prepare against possible Dark Heaven activity in Sichuan.",
    "Jin is heading to the Sichuan Tang Clan to meet someone; the person’s identity is not established."
  ],
  "continuity_sources": [
    837,
    838
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, and what is the Ark?",
    "What changed in the System update, and when will its functions return?"
  ],
  "safe_through": 838,
  "temporary_decisions": [
    "Keep magical power distinct from mana.",
    "Keep Blink distinct from Teleport and Warp; extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 주화란    | **Ju Hwaran**      |
| 암천     | **Dark Heaven**                  |
| 사천당가   | **Sichuan Tang Clan**            |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 낭인     | **wandering martial artist**                     |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 은인     | **Benefactor**                               |
| 사천     | **Sichuan**            |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 도사      | **Daoist**                                                      |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 주원공 | **Ju Wongong** | Qingxia Hall leader who claims distant kinship with the Emperor. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 수문위사 | **gate guard** | Jin Family guard stationed at the gate. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 아미타불 | **Amitabha** | Buddhist invocation spoken by the unidentified arriving group. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 독의 | **Poison Physician** | Taekyung's mocking description of Mungyeong after learning how aggressively he uses poison. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 암기 | **hidden weapon** | Term used in Mungyeong's promise not to throw one. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 서천 | **Western Heaven** | Short form used by the Lord of Heaven for the Western Heaven Demon Lord. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 파리 | **Paris** | The city containing Ares Guild's branch attacked at the chapter's end. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 진태경 | 당사독 | visitor_to_Sichuan_Tang_Family_Head | Great Hero Tang Sadok | formal-deferential | Taekyung formally introduces himself and addresses Tang Sadok as 대협. |
| 당사독 | 진태경 | Family_Head_to_visiting_younger_martial_artist | you; fearless brat | blunt and threatening | Tang Sadok uses 너 and later calls Taekyung 겁 없는 놈 while rejecting his challenge. |
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 서천마군 | 당사독 | hostile_opponents | you | calm and taunting | The Western Heaven Demon Lord uses 자네 while answering Tang Sadok's question. |
| 당사독 | 서천마군 | hostile_opponents | you bastard | hostile and threatening | Tang Sadok uses 네놈 after recognizing the disguised infiltrator. |
| 서천마군 | 진태경 | hostile_opponents | you | calm and taunting | Uses 자네 while questioning Taekyung and offering to take him alive. |
| 진태경 | 서천마군 | hostile_opponents | Western Heaven Demon Lord | casual and defiant | Identifies the Demon Lord by title and answers his surrender demand with sarcasm. |
| 진태경 | 주원공 | opponent to exiled imperial relative | you | casual and mocking | Uses 네놈 and the 주인공/주원공 wordplay while ordering Ju Wongong down. |
| 주원공 | 진태경 | Qingxia Hall young master to Great Hero | Great Hero Jin | imperious, then deferential | Initially uses 네놈 and 역적놈아 while asserting imperial authority, then switches to 진 대협 and respectful forms after seeing Prince Shangshan's token. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |

## Listed compact profiles

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 837
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, Jin-ho is his older friend and trusted confidant, and he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 837
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 838
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Ju Wongong.md

# Ju Wongong (주원공)

- **Safe through:** Chapter 838
- **Aliases:** Qingxia Hall young master
- **Role:** Ju Wongong is an exiled Qingxia Hall young master and distant imperial relative who, while still under punishment, has been temporarily appointed acting City Lord of Sichuan Province by imperial order.
- **Personality:** Entitled, status-conscious, theatrical, and amused by violence until his own protection is overcome.
- **Voice:** Pompous and imperious, with formal declarations of rank and authority.
- **Relationships:** His Qingxia Hall entourage and four Peak guards obey him; he asserts kinship with the Emperor, and Jin Taekyung is the benefactor who saved his life and can leverage Wongong’s temporary office.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 837
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 837
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 536
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, gravely wounded in the Three-Gate Bloodbath and recovering under medical care.
- **Personality:** Grim, cold, blunt, suspicious, and unsentimental, with fierce concern for the Tang Clan’s affairs.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor as Family Head, his unnamed nephew serves as Master of the Gatekeeper Pavilion, Mimi is his cherished old friend and companion currently entrusted temporarily to Cheongpung, and he regards Jin Taekyung and Cheongpung as benefactors to whom the Tang Clan owes an unrepayable debt.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 834
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃839화



시간은 많은 것을 변화시킨다.

살아 있는 것도. 죽어 있던 것도.

시간의 섭리 앞에서는 그 모든 것이 평등했다.

천하를 호령하던 절대자도 언젠가는 흙으로 돌아가고, 바람에 흩날려 흙에 섞여든 씨앗이 수백 년 뒤 울창한 풀숲을 이루기도 한다.

무림(武林)도 마찬가지였다.

아득한 과거, 그들은 각자의 목적을 이루기 위해 무공을 단련하고 자신들만을 위한 울타리를 세웠다.

그렇게 헤아릴 수 없이 수많은 낮과 밤을 흘려보내며, 거대한 전란과 빛나는 영웅들이 스쳐 지나간 끝에 현재에 이르게 되었다.

구파일방(九派一幇).

그리고 오대세가(五大世家).

중원 무림을 지탱하는 열다섯 개의 기둥.

지난 수백여 년간 흔들릴지언정 뽑혀 나가지 않은, 뿌리 깊은 거목들.

사천당가(四川唐家)도 그중 하나였다.

“바로 앞의 언덕만 넘으면 도착입니다.”

마부의 말에 고개를 끄덕인 주원공이 슬쩍 내 눈치를 살폈다.

“이대로 헤어져야 한다니 아쉽구려. 내 마음 같아서는 진 공자를 극진히 대접하고 싶으나…….”

“그럼 성으로 갈까? 까짓거 대접받지 뭐.”

“진 공자께서도 공사가 다망해 보이시니, 그런 즐거움은 나중으로 미루도록 하겠소.”

그냥 놀리려고 해 본 소린데, 자식이 괜히 겁먹기는.

나는 황급히 말을 비트는 주원공을 보며 피식 웃었다.

사실 따지고 보면 녀석도 딱히 나쁜 놈은 아니다. 무능한 주제에 여기저기서 돈 받아먹기 좋아하고, 황족이라는 권위를 이용해서 호사를 누릴 뿐이지.

“…….”

말하고 보니 좀 나쁜 놈 같긴 하다. 결국 주원공이 받아 처먹은 뇌물 중 일부는 백성들의 고혈을 쥐어 짜낸 것일 테니까.

‘죽다 살아난 후에도 정신 못 차린 것 같은데, 좀 더 갈궈야 하나.’

내 고민이 표정 위로 드러난 모양이다. 주원공이 새파랗게 질린 얼굴로 마부를 재촉했다.

“한시가 급하다! 속력을 높여라!”

“그 정도로 안 급해. 괜히 열심히 일하는 사람 갈구지 말고 너나 잘해.”

“한시가 급하지 않다! 지금 속력을 유지해라!”

마치 아바타를 조종하는 이 느낌, 의외로 재미가 쏠쏠하다.

상대가 방계 황족에다가 임시 사천성주라 더더욱 그런지도 모르겠다.

뭐, 이래 봬도 내가 생명의 은인인 데다가 다루기도 쉬우니 이렇게라도 인연을 맺어 두면 도움이 되겠지.

“더 갈 필요 없이 이쯤에서 멈추자. 어차피 거의 다 왔는데, 괜히 이대로 사천당가에 가 봤자 피차 반갑진 않으니까.”

숫자는 적지만 척 봐도 중무장한 기마병 수십 기에, 황실의 깃발이 달린 육두마차를 끌고 가 봤자 환영 인파가 몰리지는 않는다.

관과 무림의 관계는 좋게 말해서 불가침이지, 서로를 경원시하는 편에 가까우니까.

“오오, 그것참 좋은 생각이구려.”

나와 떨어질 수 있다는 생각에 대번에 얼굴이 밝아진 주원공은 냉큼 명령을 내려 행렬을 멈추게 했다. 그리고 친히 마차에서 내려 문까지 열어 주는 친절함을 발휘했다.

“멀리 배웅 못 하는 것을 양해하시오. 그리고 부디 진 공자의 앞날에 무, 무…….”

“무운?”

“아, 맞소. 무운(武運)이 가득하길 진심으로 바라겠소.”

진심으로 바라는지는 모르겠지만, 오는 말이 고우면 가는 말도 고운 법이다. 나는 웃는 얼굴로 주원공의 어깨를 두드려 주었다.

“그래, 우리 황족님도 다시 볼 때까지 몸 건강하고, 이참에 주색잡기도 좀 줄이시고. 알겠지?”

“알겠소. 진 공자의 조언을 잊지 않으리다.”

“좋아, 그럼 잘 가.”

“조심히 가시오.”

고개를 끄덕인 내가 마차의 문을 닫았다.

탁.

격자 창문 사이로 나를 멍하니 바라보던 주원공이 다시 문을 열었다.

“그…… 안 내리시오?”

내가 눈을 깜빡이며 되물었다.

“내가 왜 내려?”

“응?”

“아, 아직 말 안 했구나. 이 마차 내가 좀 쓰려고.”

“……?”

“너도 알다시피 우리 일행 중에 나이 든 사람도 있고, 아픈 사람도 있잖아. 있으면 편할 것 같더라고. 거리 나가면 사람들도 길 잘 비켜 주고.”

“……!”

“거기 화룡각 친구들. 이제 다들 안으로 들어오세요. 불편하게 말 타고 오느라 고생했네.”

평범한 무림인이었다면 내 말에 당황했을 거다.

그래도 황족 소유의 마차인데 이래도 되는 겁니까, 아닙니다, 저는 괜찮습니다, 등등의 온갖 모범 답안이 줄줄이 쏟아졌겠지.

하지만 대(大) 화룡각 대원들은 싹수부터 달랐다.

아니, 그나마 파릇파릇하던 싹수도 남만에서 노랗게 염색해서 돌아왔다.

“어후 시부럴 거, 가뜩이나 삭신이 쑤셔 죽겠는데 중원 놈들은 신분 높다고 노인 공경도 없나…….”

마치 들으라는 듯이 중얼거리며 허리춤을 툭툭 두드린 남호를 시작으로, 말에서 내린 화룡각 대원들이 줄줄이 마차 안으로 입성했다.

물론 한마디씩 하는 것도 잊지 않고.

“오향장육도 안 주고. 태산이 화난다. 다 때려 부수고 싶다.”

“어허, 태산아. 아무리 대접이 박하다 한들 그래서는 안 된다.”

“낭인 생활 막 시작했을 때가 생각나는군. 그때도 지금처럼 사람대접 못 받았는데.”

“마차 좋네요. 각주님. 이거 나중에 저희 표국으로 가져가면 안 될까요?”

나는 마차에 흥미를 보이는 주화란에게 그래도 된다고 말해 준 뒤, 벙찐 얼굴로 서 있는 마차 주인을 향해 정중하게 부탁했다.

“혹시 거기 매달려 있는 깃발 좀 뽑을 수 있을까? 우리가 황족도 아닌데, 저거까지 달고 다니면 좀 귀찮아질 것 같아서.”

“…….”

마차 안에 쏙 들어간 우리와 당황한 얼굴로 먼 산을 쳐다보는 기마병들을 번갈아 바라본 주원공이 한숨을 푹 내쉬었다.

그리고 호화찬란한 황금빛 깃발을 쑥 뽑았다.

“아, 문도 닫아 주라.”

“…….”

“싫어?”

탁.

마치 아바타를 조종하는 이 느낌, 역시 재미가 쏠쏠하다.



* * *



사천당가에 도착한 우리를 가장 먼저 맞이한 것은, 새롭게 쌓아 올린 석벽 위에서 대기 중인 수문위사의 무뚝뚝한 목소리와 경계심 어린 눈빛이었다.

“정지! 우선 소속과 이름. 만약 무림인이라면 별호와 찾아온 목적을 밝히시오.”

그리고 수문위사의 경계심은, 내가 마차 밖으로 고개를 내민 순간 흔적도 없이 사라져 버렸다.

“문을, 문을 열어라!”

“왜요? 누구 왔어요?”

“열라면 열어, 이 어린 노무 새끼야!”

몇 달 전 처음 사천당가를 찾았을 때만 해도 암기부터 날아왔던 것 같은데, 지금은 입 벙긋하기도 전에 문이 열렸다.

그그그긍.

육중하기 그지없는 철문이 열리는 사이, 어리버리한 신입의 뒤통수를 후려친 수문위사는 나를 향해 몇 번이나 포권을 취하고는 이내 헐레벌떡 어딘가로 달려갔다.

“모두 밖으로 나오시오! 화룡각이 도착했소!”

“뭣이! 또 적습이란 말이냐!”

“아니, 그게 무슨 미친 소리요. 열화신룡 진태경 대협이 이끄는 화룡각이 왔단 말이오!”

“뭣이이이!”

교대 근무 후 낮잠이라도 한숨 때리고 있었는지, 입가에 허연 침 자국이 남아 있는 사천당가의 무인이 손에 들고 있던 암기를 내던지고 달려온다.

아니, 정확히는 사천당가뿐만이 아니다.

“진 대협! 저를 기억하시는지요!”

“이리 다시 보게 되니 반갑구려. 그대 덕분에 본문의 제자들이 큰 희생을 피할 수 있었소.”

“아미타불. 진 시주께서 다시 사천 무림을 찾으시다니, 아미의 이름으로 재차 감사의 말씀을 전합니다.”

“어이쿠, 이게 누구신가! 개똥아, 애들 불러와라!”

녹색 무복을 걸친 사천당가를 시작으로 청성파와 아미파의 도사며 비구니들. 마지막으로 개방의 거지들까지.

그야말로 인산인해(人山人海)처럼 몰려드는 막대한 인파에, 남호가 입을 떡 벌렸다.

“허, 네놈은 도대체 무슨 짓을 하고 다녔던 게냐?”

“대충 말씀드렸잖아요. 사천에서 무슨 일이 있었는지.”

“아니, 아무리 그대로 이건…… 그 성질 더럽기로 소문난 사천당가에 타 문파의 사람들이 있다는 것만으로도 희한한 일인데, 뭘 이렇게까지 몰려들어?”

“그냥 뭐, 이것저것 했습니다.”

남호도 어느 정도의 사정은 알고 있었지만, 굳이 자세히 말하지는 않았다.

내 얼굴에 스스로 금칠하는 것만큼 낯간지러운 일도 없고, 어차피 자연스럽게 알게 될 일이니까.

‘그나저나, 다들 잘 지내고 있던 모양이네.’

사방에서 쏟아지는 환호와 포권 세례에 꾸벅꾸벅 고개를 숙이다 보니 마음 한구석이 간질간질하다.

사실 고백하자면, 조금이나마 불안한 마음도 있었다.

서천마군(西天魔君)이 이끄는 암천의 군세가 사천 땅을 휩쓸었던 것은 불과 반년도 되지 않은 일.

그 과정에서 중심 표적이 되었던 사천당가는 엄청난 피해를 입었고, 청성과 아미, 개방 역시 적지 않은 피를 흘려야 했으니까.

그러나 내 우려와 달리, 지금 주위를 둘러싼 그들의 얼굴에는 오직 기쁨만이 가득했다.

‘다행이다. 다행이야.’

떠나기 직전까지 검붉은 핏물 자국이 지워지지 않았던 외원(外院)은 이제 푸른 잔디로 가득했다.

연일 수많은 시신을 화장하는 불길과 새카만 연기로 뒤덮였던 하늘은 구름 한 점 없이 맑고, 그 아래에는 모두의 도움과 노력으로 새롭게 재건된 전각들이 즐비하다.

저들이 그날의 슬픔을 완전히 벗어났는지는, 나도 모르겠다.

하지만 한 가지는 확실하다.

사천당가는, 아니 사천 무림은 다시 일어섰다.

지금까지 줄곧 이어졌던 보이지 않는 균열을 멈추고, 하나가 되어 슬픔을 딛고 일어나고 있었다.

잃어버린 것에 대한 복수를 위해.

그리고 그 소중한 무언가를 두 번 다시 잃지 않기 위해.

‘그래, 그럼 된 거야.’

마치 스스로에게 다짐하듯, 마음속으로 힘주어 뇌까린 나는 마차에서 내렸다.

이미 사방에서 몰려든 인파 탓에 꼼짝없이 길이 막혀 버린 것도 있었지만, 그보다는 저 멀리 가까워지는 낯익은 얼굴을 발견했기 때문이었다.

저벅저벅.

호리호리하다 못해 비쩍 마른 몸. 병을 앓는 이처럼 파리한 안색과 그런 자신에게 호통치듯 힘있게 내딛는 발걸음.

저벅.

불현듯 걸음이 멈춘다.

서서히 잦아드는 환호와 함께 주위의 인파가 양옆으로 갈라졌다.

그리고 그 끝에 선 노인이, 은은한 녹광(綠光)이 흐르는 눈동자로 나를 바라보았다.

“오랜만이군.”

딱딱한 것을 넘어, 차갑게 느껴지기까지 하는 음성으로 건넨 인사.

하지만 다음 순간, 숨죽이며 그 모습을 지켜보던 모두는 똑똑히 볼 수 있었다.

누구에게도 굽혀질 것 같지 않던 노인의 허리가 나를 향해 기울어지는 모습을.

이 자리의 누구도 들어 본 적 없었을, 노인의 따뜻한 목소리를.

“사천당가의 가주, 만독수라(萬毒修羅) 당사독이 가문의 은인을 뵙소이다.”

미처 예상치 못했던 극진한 예의. 진심을 담아 포권지례를 취한 당사독이, 문득 할 말을 잃은 나를 바라보며 웃는다.

언제나 한 자루의 비수처럼 날카롭고 딱딱하던 그의 입가에는 단 한 번도 보지 못한 보조개가 패어 있었다.

“다시 만나게 되어 반갑네, 열화신룡 진태경.”

노인의 기쁨이 담긴 그 한 마디에, 억눌려 있던 함성이 쩌렁쩌렁하게 울려 퍼진다.

동시에 그 사이로 오직 나만이 들을 수 있는 음성이 귓가를 파고들었다.

- 하고 싶은 말은 많지만, 다음으로 미뤄야겠지. 안 그런가?

뒤늦게 따라 웃은 내가 고개를 끄덕이자, 당사독의 전음이 이어졌다.

- 따라오게. 노야께 안내해 드릴 테니.
```

## Final English reading copy

```markdown
# Chapter 839

Time changes many things.

The living. The dead.

Before the laws of time, all things were equal.

Even an absolute ruler who once commanded the world would one day return to the earth. A seed carried on the wind and buried in the soil might grow, hundreds of years later, into a dense thicket of grass.

Murim was no different.

In the distant past, people trained in martial arts and built fences around themselves, each pursuing their own goals.

Countless days and nights passed. Great wars and shining heroes came and went, until at last the present arrived.

The Nine Sects and One Gang.

And the Five Great Families.

Fifteen pillars supporting the Murim of the Central Plains.

Deep-rooted trees that had never been uprooted in the past several hundred years, even when they swayed.

The Sichuan Tang Clan was one of them.

“Once we cross that hill up ahead, we’ll be there.”

At the coachman’s words, Ju Wongong nodded, then sneaked a look at me.

“It’s a shame we have to part here. If it were up to me, I’d treat Young Master Jin with the utmost hospitality, but…”

“Then let’s go to the city. I don’t mind being treated.”

“Young Master Jin seems to have a great many important affairs to attend to, so we’ll save that pleasure for another time.”

I’d only said it to tease him, but the guy had gone and gotten scared.

I snickered as I watched Ju Wongong hastily change his tune.

When you got right down to it, he wasn’t exactly a bad guy. He was just incompetent, fond of pocketing money from anyone and everyone, and used his imperial status to live in luxury.

“……”

Now that I put it that way, he did sound like a bad guy. Some of the bribes Ju Wongong had accepted must have come from squeezing the people dry.

*He still hasn’t learned his lesson, even after nearly dying. Should I lay into him some more?*

My concern must have shown on my face. Ju Wongong went pale and urged the coachman on.

“Every second counts! Pick up the pace!”

“It’s not that urgent. Don’t hassle the poor guy for doing his job. You should worry about yourself.”

“Every second does not count! Maintain this speed!”

This feeling of controlling an avatar was surprisingly fun.

Maybe it was even more fun because he was a distant imperial relative and the acting City Lord of Sichuan Province.

Well, I had saved his life, and he was easy to handle. Keeping him on friendly terms could come in handy.

“No need to go any farther. Let’s stop here. We’re almost there anyway, and neither side will be happy if we show up at the Sichuan Tang Clan like this.”

We might not have many, but if we rolled up with dozens of heavily armed cavalrymen and a six-horse carriage bearing the imperial flag, we weren’t exactly going to draw a welcoming crowd.

The relationship between the government and Murim was, to put it nicely, one of noninterference. In practice, they tended to keep their distance from each other.

“Oh, that’s a very good idea.”

Brightening at the thought of parting ways with me, Ju Wongong quickly ordered the procession to stop. Then he kindly climbed out of the carriage and opened the door for me himself.

“I hope you’ll forgive me for not seeing you off any farther. And I sincerely wish Young Master Jin a future filled with w-w…”

“Martial fortune?”

“Ah, yes. I sincerely wish you the best of martial fortune.”

I had no idea how sincere he was, but kind words deserved kind words in return. I smiled and patted Ju Wongong on the shoulder.

“Right. You take care of yourself until we meet again, Your Highness. And maybe cut back a little on the wine, women, and gambling while you’re at it. Got it?”

“I understand. I won’t forget your advice, Young Master Jin.”

“Good. See you.”

“Travel safely.”

I nodded and shut the carriage door.

*Clack.*

Ju Wongong, who’d been staring blankly at me through the lattice window, opened the door again.

“Um… aren’t you getting out?”

I blinked and asked him back.

“Why would I get out?”

“Huh?”

“Oh, I haven’t told you yet. I’m going to borrow this carriage.”

“……?”

“As you know, we’ve got elderly people and sick people in our party. I figured it’d be more comfortable if we had one. And when we’re out on the road, people are more likely to clear the way.”

“……!”

“You Fire Dragon Pavilion folks. Come on in. You’ve had a hard time riding all this way.”

An ordinary martial artist would’ve been flustered by what I said.

It’s an imperial carriage, can we really do this? No, it’s all right, I’m fine, and so on—one model answer after another.

But the great Fire Dragon Pavilion members were a different breed.

Actually, whatever fresh-faced promise they’d once had had come back from Nanman dyed yellow.

“Aw, shit. My whole body’s aching bad enough to kill me, and these Central Plains bastards are so high and mighty they don’t even respect the elderly…”

Namho started, muttering just loud enough for everyone to hear and patting his lower back. The Fire Dragon Pavilion members climbed down from their horses and filed into the carriage.

Of course, they didn’t forget to make their own comments.

“They didn’t even give us five-spice pork. Taishan angry. Want to smash everything.”

“Now, now, Taishan. No matter how poorly they treat us, you mustn’t do that.”

“It reminds me of when I’d just started life as a wandering martial artist. People didn’t treat me like a person back then, either.”

“Nice carriage, Pavilion Master. Could we take it back to our Escort Bureau later?”

I told Ju Hwaran she could, then turned to the carriage’s owner, who stood there stunned, and politely asked:

“Could you pull off the flag hanging there? We’re not imperial family, and it’d be a pain if we went around with that thing still on.”

“……”

Ju Wongong looked from us, packed snugly inside the carriage, to the cavalrymen staring awkwardly off at the distant mountains. He let out a deep sigh.

Then he yanked the splendid golden flag free.

“Oh, and close the door for us.”

“……”

“Don’t want to?”

*Clack.*

This feeling of controlling an avatar really was a lot of fun.

* * *

The first to greet us when we reached the Sichuan Tang Clan were the gate guard’s gruff voice and wary eyes, watching from atop the newly built stone wall.

“Stop! State your affiliation and name. If you’re a martial artist, give your title and reason for coming.”

The gate guard’s wariness vanished without a trace the moment I leaned my head out of the carriage.

“Open the gate! Open the gate!”

“Why? Who’s here?”

“I said open it, you little bastard!”

When I first visited the Sichuan Tang Clan a few months ago, I was pretty sure hidden weapons had come flying at me. This time, the gate opened before I could even open my mouth.

*Rrrrumble.*

As the massive iron gate swung open, the gate guard smacked the dim-witted new recruit on the back of the head. He clasped his hands to me several times, then rushed off somewhere in a panic.

“Everyone, come outside! The Fire Dragon Pavilion has arrived!”

“What?! Are we under attack again?”

“What kind of crazy talk is that? The Fire Dragon Pavilion led by Great Hero Jin Taekyung, the Blazing Flame Divine Dragon, is here!”

“What?!”

Maybe he’d been taking a nap after his shift. A martial artist of the Sichuan Tang Clan, a white trail of drool still at the corner of his mouth, tossed aside the hidden weapon in his hand and came running.

Or, to be precise, it wasn’t just the Sichuan Tang Clan.

“Great Hero Jin! Do you remember me?”

“It’s a pleasure to see you again. Thanks to you, the disciples of our sect avoided a great many casualties.”

“Amitabha. To think that Benefactor Jin has returned to Sichuan Murim. On behalf of Emei, I offer you my thanks once more.”

“Well, well, who do we have here! Gae-ttong, go get the others!”

The martial artists of the Sichuan Tang Clan, dressed in green uniforms, were joined by Daoists from the Qingcheng Sect, nuns from the Emei Sect, and finally even the beggars of the Beggars’ Sect.

At the sight of that enormous crowd surging in like a sea of people, Namho gaped.

“Hell, what in the world have you been doing?”

“I more or less told you what happened in Sichuan.”

“Even so, this is… It’s strange enough that people from other sects are here with the Sichuan Tang Clan, who are famous for their foul tempers. But why are they all coming out to greet you like this?”

“I just did a few things here and there.”

Namho knew some of what had happened, but I didn’t go into detail.

There was nothing more embarrassing than praising myself, and he’d find out naturally anyway.

*Still, it looks like everyone’s been doing well.*

I kept bowing my head as cheers and clasped-hand greetings poured in from every direction. A warm feeling stirred in a corner of my heart.

To be honest, I’d been a little worried.

It hadn’t even been half a year since the forces of Dark Heaven, led by the Western Heaven Demon Lord, swept across Sichuan.

The Sichuan Tang Clan had been the main target and suffered enormous losses. Qingcheng, Emei, and the Beggars’ Sect had all paid in blood, too.

But contrary to my fears, the faces surrounding me now held nothing but joy.

*Thank goodness. Thank goodness.*

The Outer Court, where dark-red bloodstains had still been visible just before we left, was now full of green grass.

The sky, once blanketed in black smoke from the fires that burned countless bodies day after day, was clear without a single cloud. Beneath it stood rows of pavilions rebuilt through everyone’s help and hard work.

I didn’t know whether they had completely moved on from the grief of that day.

But one thing was certain.

The Sichuan Tang Clan—or rather, Sichuan Murim—had risen again.

They had stopped the invisible rift that had persisted all this time, coming together to rise above their grief.

To avenge what they had lost.

And so they would never lose something precious again.

*Yeah. That’s all that matters.*

As if making a promise to myself, I repeated those words with force in my heart and climbed down from the carriage.

The crowd that had gathered all around us had already blocked the road. But more than that, I’d spotted a familiar face approaching in the distance.

*Thud. Thud. Thud.*

A body so slender it was almost emaciated. A pallid face like that of someone suffering from an illness, and footsteps landing with vigor, as if he were scolding his own frailty.

*Thud.*

Suddenly, he stopped.

The cheers gradually died down, and the crowd parted to either side.

At the end of the path, an old man looked at me with eyes gleaming a soft green.

“It’s been a long time.”

His greeting was not merely stiff—it was cold.

But the next moment, everyone watching in bated breath saw it clearly.

The old man’s back, which seemed as if it would never bend to anyone, inclining toward me.

And they heard the warm voice of that old man—a voice no one there had ever heard before.

“I, Tang Sadok, Family Head of the Sichuan Tang Clan and the Myriad-Poison Asura, have the honor of meeting my family’s Benefactor.”

The unexpected courtesy was so profound that I was at a loss for words. Tang Sadok clasped his hands in a formal salute, his sincerity plain, then smiled at me.

At the corners of his mouth, always sharp and hard as a dagger, dimples appeared—dimples I’d never seen before.

“It’s good to see you again, Blazing Flame Divine Dragon Jin Taekyung.”

At that one line, filled with the old man’s joy, the suppressed cheers rang out thunderously.

At the same time, another voice slipped through the noise and into my ear—one only I could hear.

*I have plenty I want to say, but we’ll have to save it for later. Don’t you agree?*

I belatedly smiled back and nodded. Tang Sadok’s Sound Transmission continued.

*Come with me. I’ll take you to the Old Master.*
```
