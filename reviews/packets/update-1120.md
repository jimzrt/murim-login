<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1120.txt",
      "sha256": "150282f3a7e79adbe638f486f51fc319e40a325993ca523602c26d9bf2a5f56b",
      "bytes": 11549
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f6ea65b945d017947fd7852f97a2462a591df41852d1a0af2329fceb18ff6644",
      "bytes": 864
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "66b724f4d846741f2cbbc7e843d83ef54cdbfc708dd1f9b56308f753f4d5a999",
      "bytes": 244911
    },
    {
      "path": "characters/Cheongheoja.md",
      "sha256": "fe08c96ba90454063369beb2b60cc2b4512916fc1df3f2c69a56af45a13e9c8a",
      "bytes": 557
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "fa842a8d796b0268fffe27ff3b6ea48adcecc93bc44f1bbdbbc5e50bdfa6000d",
      "bytes": 760
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "e94c1f2905e157582e2caf8393c24bda3705de6a53273fd433edade377e196af",
      "bytes": 670
    },
    {
      "path": "characters/Human Butcher.md",
      "sha256": "24db26bba15eddf5f0d88b632fa6b2f2e108ab382a260db389294f5fbbf5ebe9",
      "bytes": 668
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "bb482c6f1daec6dff6a3f9af63e1706377624afc28487d1ae4891c7ae4aff3df",
      "bytes": 1357
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "3b164c12885860d45be33e91c69f628d956060aee695ee0bdbcc3e703018d3b0",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "0f9381494e5460ab361903b3f0f9c3e64cdf5ae5f4bcbec46e267aa56e2dee39",
      "bytes": 623
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "cb08070003a1ff73d2feff26bb0a64634830861b27ac51e9ea1dd10405f1d0d5",
      "bytes": 974
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "86b262b9b2ecd8815792abdd58e1d9402d4ce3a93658278fb695fef0a45f0ba0",
      "bytes": 850
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "4a595dcc35a0d9efbd07be121d69c564a2b34ed3a539d9460c192a9adc02b7b7",
      "bytes": 774
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "4e177e6a38d36019edb319cac5572a754e8b86572d827a7b22b12d150a954b1d",
      "bytes": 980
    },
    {
      "path": "characters/Tae Gunak.md",
      "sha256": "d0f7b4173b2cb6e3e276538d375764cd5bb514d20de43105aaa8ee3f878f2baa",
      "bytes": 642
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "63790e54c950c3ac5af86795603c117fe901a239f4b9d5ee1fa7a1459551b33b",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "d55475543ec1fb1c82a8c660ed8fc6b6c7536abad3e5c84ebccc42321005d0fd",
      "bytes": 289267
    }
  ],
  "estimated_tokens": 12459
}
-->

# Durable State Update — Chapter 1120

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
1 and safe_through 1120. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1120. Profile updates may replace only one
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
  "chapter": 1120,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1120,
    "continuity_sources": [1120],
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
    "The East Gate battle continues amid Dark Heaven fanatics, defenders, and monsters.",
    "Hyuk Mujin killed the jiangshi sorcerer; roughly three hundred surviving monsters stopped moving when the ritual bell fell.",
    "A powerful unidentified figure opened the East Gate and struck Hyuk Mujin in the chest; his condition is unknown.",
    "The coalition approaching from the east had not yet been shown reaching the East Gate."
  ],
  "continuity_sources": [
    1118,
    1119
  ],
  "open_questions": [
    "Will Hyuk Mujin survive the blow, and who is the figure that opened the East Gate?",
    "What will happen when the approaching coalition reaches the East Gate?"
  ],
  "safe_through": 1119,
  "temporary_decisions": [
    "Render 부각주 as “Vice Captain” when Taishan addresses Hyuk Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 송일     | **Song Il**        |
| 파륜     | **Pa Ryun**        |
| 주화란    | **Ju Hwaran**      |
| 쾌풍검    | **Swift Wind Sword**          | Hyuk Mujin     |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 암천     | **Dark Heaven**                  |
| 장강수로맹  | **Yangtze River Channel League** |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 곤륜     | **Kunlun**             |
| 도사      | **Daoist**                                                      |
| 청허자 | **Cheongheoja** | Kunlun Sect Leader. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태군악 | **Tae Gunak** | Green Forest Battle King. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 녹림맹 | **Green Forest Alliance** | Bandit alliance receiving Black Mountain Stronghold’s tribute. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 추혼객 | **Soul-Chasing Guest** | Song Ilseom’s former epithet; he was known by it ten years earlier. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 대초자곤 | **two-section staff** | Weapon carried by Sama Pyo's giant subordinate. |
| 내성 | **Inner City** | Fortified inner district of the Murim Alliance. |
| 녹림투왕 | **Green Forest Battle King** | Epithet of the Green Forest Alliance Leader, distinguished from the Ten Kings. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 고든 | **Gordon** | Pentagon employee tasked with repairing smashed warning lights. |
| 동문 | **East Gate** | One of the Nanman Beast Palace's gates. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |
| 흑귀 | **Black Ghost** | The Blood-Sword Demon Lord’s name for the Death Knights. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 송일섬 | 궁기방 | senior_martial_artist_to_Beggars_Sect_successor | Successor Beggar | blunt and irritated | Uses 후개 while objecting to Gung Gibang’s spitting and insults. |
| 궁기방 | 송일섬 | Beggars_Sect_successor_to_young_escort_captain | Young Hero Song | casual and admiring | Uses 송 소협 while praising the famous Soul-Chasing Guest and comparing their looks. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
| 진태경 | 대인 | young martial artist to benefactor | you | casual and blunt | Taekyung asks who Great Sir is, addressing him as 당신. |
| 대인 | 진태경 | older benefactor to young martial artist | you | familiar conversational | Great Sir addresses Taekyung as 자네. |
| 태산 | 대인 | ally addressing an elder | Sir | informal and enthusiastic | Calls out to the Great Sir while praising his shot. |
| 대인 | 태산 | elder addressing a younger ally | young friend | familiar and playful | Offers Taishan a portion of the bird as a reward. |
| 태산 | 청허자 | younger martial artist to senior sect leader | you | clipped and childlike | Asks whether Cheongheoja brought meat. |
| 진태경 | 청허자 | younger martial artist to senior sect leader | Sect Leader | respectful | Uses a formal greeting and bow. |
| 청허자 | 진태경 | senior sect leader to younger martial artist | Fellow Daoist Jin | warm and polite | Greets Taekyung by surname and confirms Hak Woo is well. |

## Listed compact profiles

### Cheongheoja.md

# Cheongheoja (청허자)

- **Safe through:** Chapter 1118
- **Aliases:** None
- **Role:** Cheongheoja is the Kunlun Sect Leader and Hak Woo’s master.
- **Personality:** Warm, composed, and patient, he faces setbacks with resolve and receives even startling company with good humor.
- **Voice:** Measured and gentle, using formal Daoist courtesies and calm metaphors.
- **Relationships:** Hak Su and Hak Eui are his Disciples; he knows Jin Taekyung by reputation and treats him warmly.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1119
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 1090
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered, but grieves deeply for fellow Beggars’ Sect disciples and defends those who risk their lives for others.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun, and shares a blunt, teasing friendship with Taekyung.

### Human Butcher.md

# Human Butcher (인도)

- **Safe through:** Chapter 1117
- **Aliases:** None
- **Role:** Former mysterious Han Chinese mounted-bandit power in Northern Gaoyuan commanding fifty subordinates; a Peak master killed by an unnamed old man in a single move
- **Personality:** Cold, intimidating, and murderous; he kills people as though slaughtering livestock
- **Voice:** Cold, curt, and quietly threatening
- **Relationships:** He is one of four powerful participants at the Northern Gaoyuan gathering, intimidates Temur, and has claimed Ghost Sword Wipeng as his personal target in the proposed attack

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1119
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, whom he deeply admires, and has developed a warm friendship with fellow Fire Dragon Pavilion member Taishan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1119
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1119
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1119
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1119
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir, commands Taishan, and is Jin Taekyung’s friend; he deliberately let Namho suspect his father’s actions to protect their companions, was Ju Hwaran’s former fiancé, and is hostile toward Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1119
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1119
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Tae Gunak.md

# Tae Gunak (태군악)

- **Safe through:** Chapter 1088
- **Aliases:** Green Forest Battle King
- **Role:** Tae Gunak is the Green Forest Battle King and the founder of the current Green Forest Alliance.
- **Personality:** Ruthless in pursuing what he wants, he is strategic enough to set aside his longstanding rivalry with Pa Ryun when their plan requires cooperation.
- **Voice:** He speaks in profane, cutting taunts and refers to himself as 노부.
- **Relationships:** Pa Ryun is his longtime rival and current collaborator in a plan to take control of the Yangtze.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1119
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1120화



퍼엉!

낮게 깔린 파공성이 울려 퍼진 그 순간, 마치 온 세상이 멈춘 것 같았다.

적어도 그 모든 것을, 섬광 같은 속도로 쏘아진 일장(一掌)이 한 사람의 가슴에 닿는 광경을 목격한 화룡각의 대원들에게는 그랬다.

그리고.

철퍽.

검붉은 핏물을 흩뿌리며 허물어지는 혁무진의 신형과 함께, 멈춰있던 세상이 움직이기 시작했다.

“안 돼!”

붉게 핏발선 눈동자와 터질 듯이 부풀어 오른 전신의 근육.

눈 앞에 펼쳐진 그 믿을 수 없는 광경에, 태산은 천둥과도 같은 고함을 내지르며 성문을 향해 돌격했다.

피로조차 잊었다. 두려움마저 지웠다.

마치 한 마리의 성난 들소처럼, 태산은 온 힘을 다해 대초자곤을 휘두르며 전진했다.

후우웅, 뻐억!

광포한 바람이 일어날 때마다 뇌수가 튀고, 뼈마디가 가루처럼 으스러진다.

강시술사의 죽음으로 석상처럼 굳어 버린 괴물들의 빈 자리를 대신한 광신도들이 그를 가로막았지만, 그들 중 누구도 거대한 분노에 사로잡힌 태산을 쉽사리 저지할 수 없었다.

아니, 정확히는 ‘그들’을.

콰드드득!

거칠게 들이닥친 도기(刀氣)가 공간을 난도질하고, 주인을 잃은 팔다리가 사방으로 비산했다.

휘몰아치는 피 보라 속, 언제나 침착하던 사마표의 눈동자가 시퍼런 불길을 쏟아내고 있었다.

동료의 죽음 따위는 아랑곳하지 않은 채, 그런 사마표를 포위하듯 덮치는 수십의 광신도들 사이를 파고든 또 다른 누군가 역시도.

쐐애애액!

바람을 가르며 쏘아지는 협봉검(狹鋒劍)의 움직임은 간결하면서도 쾌속했고, 동시에 더없이 잔혹했다.

추혼객(追魂客)이라는 별호조차 부족하게 느껴질 만큼.

푹! 푸푸푹!

송일섬은 닥치는 대로 찌르고 비틀었다.

가장 효율적인 움직임으로, 가장 확실한 고통과 죽음을 적들에게 선사했다.

끔찍한 비명과 함께 터져 나온 핏물이 얼굴을 뒤덮고, 사방에서 무차별적으로 쏟아지는 날붙이가 전신 곳곳에 크고 작은 상처를 남겨도 굳게 다문 입술은 조금도 떨리지 않았다.

송일섬의 혈관을 타고 흐르는 피는 명가(名家)의 것이나, 추혼객을 있게 만든 것은 전장에서 흘린 피였으므로.

선대의 빚을 갚기 위해 일평생 걸어왔던 낭인의 길을 벗어났듯이, 지금의 그는 동료의 혈채(血債)를 갚기 위해 자신의 목숨을 내던지고 있었다.

계산 따위는 조금도 없는, 순수한 분노에 몸을 맡긴 채.

그리고 그것은 비단 송일섬 혼자만이 느끼는 감정이 아니었다.

“감히……!”

“이 거지보다 못한 새끼들아!”

쉬쉬쉬쉭! 서걱!

주화란이, 궁기방이, 또한 간신히 살아남은 일천의 수비군들이 이를 악물며 억지로 몸을 일으켜 세웠다.

이길 수 있을 거라는 희망?

이미 마음속에서 깨끗이 지워 버린 지 오래다.

괴물들이 움직임을 멈췄다 한들 몇 배에 달하는 광신도들이 남아 있었고, 설상가상으로 수만에 달하는 적들의 지원군마저 등장했으니.

하지만 사람을 움직이는 동력은 희망뿐만이 아니다.

그 어둡고 아득한 절망 속에서, 그들은 똑똑히 보았다.

쓰러지는 마지막 순간까지 당당함을 잃지 않았던 혁무진의 모습을.

‘화룡각…… 아니.’

도무지 대적할 수 없는 강자의 앞에서도 조금도 꺾이지 않았던 그의 마음을.

‘쾌풍검(快風劍) 혁무진.’

차차차차창!

마침내 다시 빛을 발하기 시작한 일천의 날붙이가 파도처럼 물결쳤다.

그들은 잘려 나간 팔과 베어 나간 뱃가죽을 틀어막고, 고통과 두려움을 억누르기 위해 혀를 깨물면서도 병장기를 쥐고 일어섰다.

어쩌면 유언이 될지도 모르는, 자신들이 이 세상에 존재했음을 알리는 마지막 흔적을 온 힘을 다해 부르짖으며.

“담도비랑(覃刀匕郞) 소규혁이 여기 있다!”

“쾌도진천(快刀震天) 무철도 있느니라!”

“정파 놈들이라 그런지 죄다 별호가 번드르르하군. 이 몸은 흑살검(黑殺劍) 조혁이다. 이 개자식들아!”

정파, 사파, 혹은 그 어디에도 속하지 않은 정사지간의 고수들까지.

비록 타고난 뿌리도, 갈라져 나온 가지와 그 끝에 맺힌 결실도 달랐으나 그들이 지키고자 하는 대의(大義)만큼은 같았다.

“멸마정천(滅魔正天).”

마를 멸하고, 하늘을 바로 세운다.

십만 마도와 맞서 싸웠던 그 시절, 피를 토하도록 외쳤던 네 글자를 나직이 뇌까린 어느 노도사는 힘주어 검 자루를 쥐었다.

서걱.

공간을 가로지르는 백광(白光)을 따라 수십 개의 조각으로 나뉘어 흩어지는 몸뚱어리.

그제야 비로소 완전한 최후를 맞이한 흑귀를 뒤로한 채 돌아선 노도사, 아니 청허자의 입술 사이로 웅혼한 공력이 실린 음성이 흘러나왔다.

“그때가 그립구려. 그대와 내가 ‘우리’였던 시절이. 아니 그렇소?”

슬픔과 분노에 젖은 청허자의 눈동자에, 저 멀리 무너진 성문 앞에 우뚝 선 거대한 그림자가 비쳤다.

“해상왕(海上王) 파륜.”

다음 순간.

“여전하구려, 청허.”

쓰러진 혁무진의 머리 위를 스치는 무거운 목소리와 함께, 길고도 광활한 장강의 주인이 흐릿한 달빛 아래로 성큼 발을 내디뎠다.

그 위풍당당한 풍채 뒤에 가려져 있던, 또 다른 두 명의 불청객 역시도.

그리고 머리부터 발끝까지 새카만 흑의(黑衣)를 걸친 정체불명의 인물과는 달리, 그 옆에 선 왜소한 체구의 노인은 낯익은 얼굴을 하고 있었다.

“오랜만이오, 청허자.”

먼저 건네오는 인사에, 청허자의 눈빛이 차갑게 가라앉았다.

“그래, 당신도 있었지. 녹림투왕(綠林鬪王) 태군악.”

“말에 날이 서 있구려. 마지막으로 보았을 때는 당신이 아니라 도우(道友)라고 불렀던 것 같은데.”

“그 시절은 이제 두 번 다시 돌아오지 않을 거요. 어떤 이들의 돌이킬 수 없는 선택으로 인해서.”

주위를 둘러본 녹림투왕의 미간이 작게 찌푸려졌다.

“상황이 이리된 것에 대해서는 미안하게 생각하오, 이건 진심이오.”

“진심이라.”

공허한 음성으로 뇌까린 청허자는 얼마 남지 않은 공력을 모조리 끌어올렸다.

우우웅.

주인의 마지막을 직감한 듯, 일평생을 함께 해온 애검이 부르르 몸을 떨었다.

그리 멀지 않은 곳에서는 아직도 흑귀와 고군분투하고 있는 대인이 있었지만, 이미 청허자의 모든 감각과 기운은 오직 성문을 지킨 불청객들을 향해 집중되어 있었다.

그가 쓰러트려야 할 상대는 천하의 흑도를 양분하는 두 거인뿐만이 아니었다.

그런 그들에 비해 결코 아래가 아님을 본능적으로 직감할 수 있는, 저 정체불명의 흑의인.

‘암천의 핵심 인물이 분명한데, 누구일까.’

문득 그런 의문이 뇌리를 스쳤지만, 청허자는 이내 쓴웃음을 머금을 수밖에 없었다.

고민이란 것도 결국 살아남은 자의 몫인 법.

그런 의미에서, 홀로 세 명의 초절정 고수를 상대해야 하는 노도사에게 더 이상의 고민은 무소용이었다.

다만 그저, 지금 이 순간에도 적들을 베어 넘기며 전진하고 있는 저 훌륭한 젊은이들에게 부끄럽지 않은 최후를 다짐할 뿐.

“오너라, 천하의 도적놈들아. 빈도는 곤륜(崑崙)의 청허다.”

어느 때보다 차갑게 얼어붙은 노도사의 안광이 번뜩인 그 순간.

“빨리 끝내도록 하지.”

모두의 귓가를 파고드는 나직한 음성과 함께.

구구구궁.

불현듯 앞으로 나선 흑의인을 중심으로 거대한 기운이 들끓었다.

온 힘을 다해 쇄도하던 청허자도, 흑귀의 검을 피해 황급히 도망치던 대인도.

광신도들을 가로지르며 미친 듯이 분투하던 화룡각 대원들과, 그런 그들의 뒤를 따라 최후의 항전을 이어가던 일천의 수비군들도.

모두가 눈을 부릅떴고, 전율하며 바라보았다.

생애 마지막 광경처럼 시야를 물들이는, 강대한 힘의 폭발을.

솨아아악!

막을 수도 없고, 제대로 볼 수조차 없는 한 줄기의 선이 세상을 가로질렀다.



* * *



“……!”

그 순간, 신형이 덜컥 굳어 버린 것은 어째서일까.

가슴 한구석을 쿵, 하고 짓누른 이 거대한 바위는 무엇으로부터 비롯된 것일까.

진태경으로서는 그 원인도, 이유도 알 수 없었다.

아니, 알고 싶지 않았다.

불현듯 들이닥친 이 불안감의 정체를 확인하는 순간, 지금의 그를 가까스로 지탱하고 있는 마지막 한 가닥의 실마저 끊어져 버릴 것 같았으니까.

하지만 그런 마음과는 반대로, 적과 건물들에 가려져 보이지 않는 동쪽 어딘가를 향한 진태경의 시선은 어느샌가 파르르 떨리고 있었다.

‘이건.’

시야는 안개라도 낀 듯이 흐릿하고, 감각은 겨울을 기다리는 도끼처럼 무뎌졌으며, 전신은 물먹은 솜처럼 축 늘어져 있는 상황.

그럼에도 미약하게나마 듣고, 느낄 수 있었다.

저 멀리 동쪽에서 울려 퍼졌던 거대한 굉음을. 그 가파른 힘의 파동을.

그리고 이는 오직 하나의 사실을 가리키고 있었다.

‘동문이…… 함락당했다.’

절대 그럴 리 없다며 부정하고 싶었지만, 소용없다.

불길에 휩싸인 가슴에 달리, 차갑게 식은 머릿속은 곧 다가올 현실을 똑바로 직시하고 있었으니까.

‘놈들이다. 틀림없이.’

장강수로맹의 맹주, 해상왕 파륜.

그런 그와 비견되며 평생의 호적수로 여겨지는 녹림맹의 맹주, 녹림투왕 태군악.

천하의 흑도를 양분하는 두 거인이, 마침내 전장에 다다른 것이 틀림없었다.

그것도 물경 삼만에 달하는 대군을 이끌고.

‘……그렇다는 건.’

차마 끝맺어지지 못한 머릿속 생각과 함께, 진태경은 흐릿한 눈동자를 들어 주위를 둘러보았다.

내성(內城)의 야트막한 성벽에 등을 기댄 채, 사방에 널브러진 수많은 시체와 피 웅덩이 속에서 거친 숨을 몰아쉬는 사람들.

동문을 제외한 세 방향에서 퇴각해 온 그들 중에는 익숙한 얼굴도 있었지만, 끝끝내 모습을 보이지 않는 이들 또한 있었다.

‘어째서?’

진태경은 멍하니 생각했다.

그들이 왜 아직까지 돌아오지 못한 것에 대한 이유를.

그리고 이미 그에 대한 답을 알고 있음에도, 스스로에게 되묻는 자신의 모습을.

‘그래, 결국 그렇게 된 건가.’

진태경은 문득 힘없이 실소를 흘렸다.

이제는 영영 볼 수 없게 된 얼굴들을 떠올리며.

내성을 에워싸는 수만 명의 적들과, 그들을 이끄는 괴물의 존재감을 느끼며.

꽈아아아앙!

거대한 굉음과 함께, 내성이 허물어졌다.
```

## Final English reading copy

```markdown
# Chapter 1120

Boom!

The moment a low boom of breaking air rang out, it felt as if the whole world had stopped.

At least, that was how it seemed to the members of the Fire Dragon Pavilion who witnessed a palm, launched at lightning speed, strike a man in the chest.

And then—

Splatter.

As Hyuk Mujin’s body crumpled, scattering dark-red blood, the world that had stopped began to move again.

“No!”

Taishan’s eyes were bloodshot, and the muscles across his body swelled as if they might burst.

At the unbelievable sight before him, he let out a thunderous roar and charged toward the gate.

He forgot his exhaustion. He cast aside his fear.

Like an enraged bull, Taishan swung his two-section staff with all his strength and pressed forward.

Whoooosh! Wham!

Each time the furious wind rose, brains flew and bones shattered like powder.

Fanatics had taken the place of the monsters, frozen like statues at the death of the jiangshi sorcerer. They tried to stop him, but none of them could easily halt Taishan, consumed by an overwhelming rage.

No—more accurately, they couldn’t stop *them*.

KRRRUNCH!

A fierce rush of saber energy tore through the space, and severed limbs flew in every direction.

Amid the swirling spray of blood, Sama Pyo’s eyes—usually so composed—blazed with blue fire.

And someone else plunged into the dozens of fanatics closing in around Sama Pyo, heedless of their fallen comrades.

SHWEEEE!

The narrow-bladed sword cut through the air in quick, simple strokes—and with utter cruelty.

So much so that even the epithet Soul-Chasing Guest seemed inadequate.

Stab! Stab-stab!

Song Ilseom stabbed and twisted wherever he could.

With the most efficient movements, he dealt his enemies the surest pain and death.

Blood burst from a terrible scream and splashed across his face. Blades rained down indiscriminately from every direction, leaving cuts large and small across his body. But his tightly pressed lips didn’t tremble.

The blood flowing through Song Ilseom’s veins came from a noble family. But what had made him the Soul-Chasing Guest was the blood he’d shed on the battlefield.

Just as he had once left the path of the wandering martial artist he’d walked his entire life to repay his ancestors’ debt, now he was throwing his life away to repay the blood debt of his comrades.

He surrendered himself to pure rage, without a thought for the cost.

And Song Ilseom wasn’t the only one who felt that way.

“How dare you…!”

“You bastards are lower than this beggar!”

Sssshing! Slice!

Ju Hwaran, Gung Gibang, and the thousand defenders who had barely survived gritted their teeth and forced themselves to their feet.

Hope that they could win?

They’d long since erased that from their hearts.

Even if the monsters had stopped moving, fanatics remained—several times as many. And to make matters worse, tens of thousands of enemy reinforcements had appeared.

But hope wasn’t the only thing that could move people.

In that dark, bottomless despair, they had seen it clearly:

Hyuk Mujin, refusing to lose his dignity until the very last moment before he fell.

*The Fire Dragon Pavilion… No.*

His spirit hadn’t bent, not even before an enemy so powerful they couldn’t possibly oppose him.

*Swift Wind Sword Hyuk Mujin.*

CLANG-CLANG-CLANG!

At last, a thousand blades began to shine again, rippling like a wave.

They clamped their hands over severed arms and slashed-open bellies, bit their tongues to suppress their pain and fear, and rose with weapons in hand.

With all their strength, they cried out what might be their last words—the final trace of their existence in this world.

“Knife-and-Dagger Hero So Gyuhyeok is here!”

“Swift Blade Shakes the Heavens Mu Cheol is here!”

“Figures the orthodox faction would have such fancy titles. I’m Black-Killing Sword Jo Hyeok, you bastards!”

Orthodox faction, unorthodox faction, or masters belonging to neither—the gray area between the two.

Their roots, branches, and fruits might all have differed, but they shared the same great cause they sought to protect.

“Destroy the Demonic Path and restore Heaven.”

Destroy the Demonic Path and set the heavens right.

An old Daoist murmured the four characters they had shouted until they were spitting blood, back when they fought a hundred thousand followers of the Demonic Path. He tightened his grip on his sword.

Slice.

A body split into dozens of pieces along a streak of white light and scattered.

Leaving behind Black Ghost, who had finally met his true end, the old Daoist turned away. Then—no, Cheongheoja’s voice rang out, carrying the force of his internal energy.

“I miss those days. The time when you and I were ‘us.’ Don’t you agree?”

In Cheongheoja’s eyes, steeped in sorrow and anger, a huge figure stood before the ruined gate in the distance.

“Seafaring King Pa Ryun.”

The next moment—

“You haven’t changed, Cheongheoja.”

With a heavy voice that brushed over Hyuk Mujin’s fallen head, the master of the long, vast Yangtze strode out beneath the faint moonlight.

Two more unwelcome guests followed, hidden behind his imposing frame.

Unlike the mysterious figure dressed in black from head to toe, the short old man standing beside him had a familiar face.

“It’s been a long time, Cheongheoja.”

At the greeting offered first, Cheongheoja’s gaze turned cold.

“Right. You were there too. Green Forest Battle King Tae Gunak.”

“Such a sharp edge to your words. Last time we met, I believe you called me a fellow Daoist, not ‘you.’”

“Those days will never return. Not after the irrevocable choices some people made.”

Tae Gunak’s brow furrowed slightly as he looked around.

“I’m sorry things came to this. I mean that.”

“You mean that…”

Cheongheoja murmured hollowly, then drew up every last bit of his remaining internal energy.

Hummm.

As if sensing that his master’s end was near, the treasured sword that had been with him all his life trembled.

Not far away, Great Sir was still struggling against Black Ghost. But Cheongheoja’s senses and energy had already focused entirely on the unwelcome guests guarding the gate.

The opponents he had to bring down weren’t just the two giants who divided the underworld of the land between them.

There was also the mysterious man in black, who instinct told him was no weaker than either of them.

*He must be one of Dark Heaven’s key figures. But who?*

The question crossed his mind, but Cheongheoja could only smile bitterly.

Worry was ultimately a luxury for those who survived.

For an old Daoist who had to face three Supreme Peak masters alone, there was no point in worrying any further.

All he could do was resolve to meet his end without shame before those remarkable young people, still advancing as they cut down their enemies.

“Come, you thieves of the world. I am Cheongheoja of Kunlun.”

The old Daoist’s eyes flashed, colder than ever.

“Let’s finish this quickly.”

Along with a quiet voice that pierced everyone’s ears—

Rumble.

An enormous force began to churn around the black-robed man who had suddenly stepped forward.

Cheongheoja, charging forward with all his strength.

Great Sir, fleeing in haste from Black Ghost’s sword.

The Fire Dragon Pavilion members, fighting like mad as they cut through the fanatics, and the thousand defenders behind them, continuing their final stand.

Every one of them stared wide-eyed, watching in shock and dread.

A mighty explosion of force, painting their vision like the last sight of their lives.

SHWAAAA!

A single line—impossible to block, impossible even to see clearly—cut across the world.

* * *

“……!”

Why had his body suddenly gone rigid?

Where had this enormous rock come from, pressing down on his chest?

Jin Taekyung couldn’t tell what had caused it or why.

No—he didn’t want to know.

The moment he found out what this sudden feeling of dread meant, he felt the last thread barely holding him together might snap.

But despite that, Jin Taekyung’s gaze toward somewhere in the east, hidden behind enemies and buildings, had begun to tremble.

*This is…*

His vision was blurry, as though veiled in mist. His senses were as dull as an axe waiting out the winter. His entire body hung limp, like a waterlogged cotton ball.

Even so, he could faintly hear and feel it.

The enormous blast that had rung out far to the east. The sharp wave of power.

And it pointed to only one thing.

*The East Gate… has fallen.*

He wanted to deny it, to tell himself it couldn’t possibly be true. But it was no use.

Unlike the fire raging in his chest, his mind had gone cold. It faced the reality coming toward him head-on.

*It’s them. It has to be.*

Pa Ryun, the Alliance Leader of the Yangtze River Channel League. And Tae Gunak, the Alliance Leader of the Green Forest Alliance, his lifelong rival, considered Pa Ryun’s equal.

The two giants who divided the underworld between them had finally reached the battlefield.

And they’d brought a force of thirty thousand.

*…Then that means—*

With the thought in his mind left unfinished, Jin Taekyung raised his hazy eyes and looked around.

People leaned against the low walls of the Inner City, gasping for breath amid countless bodies and pools of blood scattered in every direction.

Among those who had retreated from the three sides other than the East Gate, some faces were familiar. But others had yet to appear.

*Why?*

Jin Taekyung wondered in a daze.

Why hadn’t they returned yet?

Even though he already knew the answer, he asked himself again.

*Right. So that’s how it ended.*

A weak, humorless laugh escaped him.

He thought of the faces he would never see again.

He felt the presence of tens of thousands of enemies surrounding the Inner City, and the monster leading them.

KWA-BOOOOM!

With a tremendous crash, the Inner City crumbled.
```
