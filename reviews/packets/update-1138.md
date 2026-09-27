<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1138.txt",
      "sha256": "5dcd120b51b1d31b1b24550f2b16a93e042549e154799bf587894da44bf479d7",
      "bytes": 11988
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e8b22dc2e368ba1f59198967f9860051e340b39bbc97e46339576a43a8751ed6",
      "bytes": 1288
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a77573feec836df54e35248f8b975bf7696cac58abec08a1c5a945ccb8c3d729",
      "bytes": 245575
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "38ba72a44f35fe846bfe9253fce4ddee0fb386073ff69b6e4855532765639398",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "cc7c1f399a7770f4677b9a59b20963145bc3272ade1eaeb908da6888e327d225",
      "bytes": 1357
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "984584e96dfecbb682a0bf6317318b1fe54a29a4eac1d713b9136f0369b5b46e",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "82441ce1faac0d2cedcf181a2a2926e49f456e6655df7ffa88c1e7e477f7019d",
      "bytes": 1929
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "1c7a11438ca78e898f745f3bfb97aef60f10ea2aa2b50422e6cdd50d7442d5cf",
      "bytes": 623
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "bbb008ed5563f5632b40eb2641bb171ea67cb82d88ec29e322c4e0a7170a9f6a",
      "bytes": 974
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "ed13bfa8f7fccb869205a775422a02c9f9526f99d99d8978937c0ea624a625c5",
      "bytes": 1084
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "b05541a4cac0d23d4de554521783618025f1f133adfb46338b650c9569e69feb",
      "bytes": 850
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "b8186c809b59d1422402d9b4f0c36cf5cdb75df60367ef08c728ed5222ebbd86",
      "bytes": 774
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "042f701633d7e044c526d5f5b40b357c4f17ab758b1e5de69771c1384bda5489",
      "bytes": 980
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "ed1396217666460f0ee5c0c949c6f8e92de38f443c58ed4d693da3819717b369",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5895951d60d69a56331fdfdc592502035283d3a48acfa6cb07fdeb7d2eb418c2",
      "bytes": 291096
    }
  ],
  "estimated_tokens": 12906
}
-->

# Durable State Update — Chapter 1138

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
1 and safe_through 1138. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1138. Profile updates may replace only one
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
  "chapter": 1138,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1138,
    "continuity_sources": [1138],
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
    "The Son of Heaven has declared Great Ming and ordered a personal expedition to Xinjiang, vowing not to return to the palace until the traitors are rooted out.",
    "The postbattle coalition of the Imperial House, the Murim Alliance, martial artists, and volunteer militias is beginning a westward advance toward Xinjiang to defeat the Lord of Heaven.",
    "Seven days after the battle, Jin Taekyung has awakened.",
    "The search for an unnamed target has not succeeded and will continue with reduced manpower.",
    "The Slaughter Saint suspects the Bow Saint concealed another motive when Jin Taekyung was in mortal danger."
  ],
  "continuity_sources": [
    1136,
    1137
  ],
  "open_questions": [
    "What was the target the searchers failed to find?",
    "What was the Bow Saint’s motive when Jin Taekyung was in mortal danger?",
    "What will happen in the campaign against the Lord of Heaven in Xinjiang?",
    "Why does the Son of Heaven’s title give the Slaughter Saint a sense of foreboding?"
  ],
  "safe_through": 1137,
  "temporary_decisions": [
    "Render 大明 as “Great Ming” and 親征 as “personal expedition.”",
    "Render 滅魔正天 as “Exterminate the Demons and Set Heaven Right.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 살성     | **Slaughter Saint**           | —              |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 지능               | **Intelligence**               |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 성우 | **Sacred Rain** | Name later given to the rain released as the Earth Mother Goddess's blessing. |
| 적도 | **Red Blade** | Named blade that shatters in Taekyung’s flames. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 거한 | 사마표 | Subordinate addressing the Black Dragon Demon Gate Young Sect Leader | Young Sect Leader | Crude and deferential | Uses 소문주 in short, childlike replies. |
| 사마표 | 거한 | Young Sect Leader addressing his giant subordinate | This fellow | Informal and patronizing | Refers to him as 이 녀석 while assigning him responsibility for Do Sangho's death. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 진태경 | 매종학 | younger ally to newly installed Alliance Leader | Alliance Leader | formal and deferential | Uses 맹주님 while formally greeting Mae Jonghak as the Alliance Leader. |
| 사마표 | 적천강 | Young Sect Leader to legendary elder | Great Hero Jeok | formal-deferential | Sama Pyo formally pays his respects to Jeok Cheongang as the Fire King. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 사마표 | legendary elder to unorthodox Young Sect Leader | you / young brat | blunt, suspicious, and contemptuous | Jeok addresses Sama Pyo with 네놈 and 어린놈 while probing his lineage and motives. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 사마표 | 진태경 | prospective recruit to pavilion master | you | polite, controlled, and candid | Sama Pyo uses 자네 while asking about Taekyung's attitude and admitting his intention to use him. |
| 진태경 | 사마표 | pavilion master to prospective recruit | you / that guy | blunt, informal, and distrustful | Taekyung speaks to and about Sama Pyo with casual forms such as 녀석 and 저놈. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 송일섬 | 사마표 | fellow_pavilion_member_to_hostile_fellow_member | you | hostile and casual | Song Ilseom discusses fighting Sama Pyo and answers him while preparing to move away. |
| 사마표 | 송일섬 | fellow_pavilion_member_to_hostile_fellow_member | you | controlled and antagonistic | Sama Pyo responds to Song Ilseom's accusations and proposes moving aside to fight. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
| 노인 | 진태경 | older opponent to younger opponent; no family relation established | you | calm, familiar speech | The old man addresses Taekyung as 자네 while testing him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1137
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1128
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, whom he deeply admires, and has developed a warm friendship with fellow Fire Dragon Pavilion member Taishan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1134
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1137
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure and fiercely defiant, he is driven to protect himself and others and live peacefully with those he cherishes, while carrying guilt over those he failed to save.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; the Helper first taught Taekyung to circulate qi; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1137
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1128
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1137
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1128
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir, commands Taishan, and is Jin Taekyung’s friend; he deliberately let Namho suspect his father’s actions to protect their companions, was Ju Hwaran’s former fiancé, and is hostile toward Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1128
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1128
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1137
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1138화



진태경은 조용히 눈을 깜빡였다.

이곳은 어디일까.

온통 어둡고, 희뿌옇다.

그의 자그마한 몸뚱어리는 활짝 펼쳐진 날개를 따라 빠르게 앞으로 나아가고 있었지만, 남의 것처럼 무딘 감각은 전신을 스치는 바람조차 선명히 느끼지 못했다.

그래.

지금의 그는 한 마리의 새였다.

그리고 머지않아 사방을 휘감은 이 축축하고도 희뿌연 구름에서 벗어날 터였다.

아니, 바로 지금.

화악.

일순간, 힘찬 날갯짓과 함께 진태경의 주위를 창살처럼 메우고 있던 구름이 사라졌다.

동시에 차가워 보일 만큼 어두운 밤하늘이 눈앞에 펼쳐졌다.

광활한 허공 곳곳을 물들이는, 형형색색의 불꽃도.

퍼버버버벙!

예고도 없이 시작된, 동시다발적인 폭발이 밤하늘을 집어삼킨다.

그저 멀리서만 지켜보았다면 얼핏 아름답다 느껴졌을 광경.

하지만 날짐승의 타고난 안력(眼力)을 지닌 지금의 진태경은 그 화려한 불빛 너머의 실체를 볼 수 있었다.

압축된 공기를 터트리며 허공을 누비는 수많은 전투기. 땅과 하늘에서 쉴 새 없이 쏘아지는 탄환과 빛줄기들.

그리고.

쐐애애액!

그 촘촘한 화망(火網)을 뚫고 날아드는 거대한 괴물들까지도.

- 키이이익!

소름 끼치는 포효와 함께, 눈으로는 헤아릴 수도 없을 정도로 많은 괴물이 어두운 밤하늘을 가로지른다.

그렇게 각자의 살의가 뒤엉키고, 폭발과 함께 터져 나온 굉음의 끄트머리에는 반드시 누군가의 죽음이 이어진다.

콰과과광!

허공을 집어삼키는 아득한 섬광.

단지 한 마리의 날짐승에 불과한 진태경은 그저 멍하니 그 광경을 바라볼 수밖에 없었다.

끊임없이 뒤섞이는 강철과 마법 속, 흩어진 불씨처럼 힘없이 추락하는 인간과 괴물들을.

그리고 문득, 온 세상이 어두워진 듯한 감각에 사로잡혀 고개를 들었다.

스아아아.

처음에는 먹구름이라고 생각했다.

달빛마저 가릴 만큼, 커다란 먹구름.

하지만 아니었다.

그것의 정체는 날개였다.

보는 이로 하여금 숨 쉬는 것조차 잊게 할 만큼 거대한.

동시에 한편으로는 아름답게 느껴지기까지 하는 어느 강력한 존재의 날개.

그 압도적인 존재를 마주함과 동시에, 진태경은 놀라우리만치 선명해지는 감각을 느낄 수 있었다.

달빛마저 지운 채 모두를 오연히 굽어보던, 흑요석을 닮은 두 개의 눈동자와 시선이 마주쳤다고 느낀 것 또한 그 때문이었다.

화아아아악!

일순간, 공간이 일그러진다.

한낱 날짐승으로는 버틸 수 없는 무시무시한 압력이 허공을 짓눌렀다.

아니, 그것은 비단 진태경에게만 해당되는 일이 아니었다.

콰드드드득!

압력을 이기지 못하고 으스러지는 수많은 전투기.

불길에 휩싸여 유성우처럼 추락하는 강철들 사이로, 진태경은 흐릿해지는 의식을 느꼈다.

그와는 반대로 더욱 선명하게 귓가를 파고드는, 의미 모를 소음도 함께.

째깍.

동시에, 저 멀리서 달려온 새하얀 빛줄기가 그를 덮쳤다.



* * *



인간의 두뇌란 무릇 쇠와 같다.

일정 이상의 열기가 가해져야만 무쇠의 형태를 바꿀 수 있듯이, 이제 막 깨어난 인간의 두뇌 역시 활동을 위해서는 약간의 시간이 필요한 것이다.

하지만 의식을 되찾은 그 순간, 나는 그 어느 때보다 선명한 감각 속에서 주위를 둘러싼 모든 것을 느낄 수 있었다.

무엇이 나를 이 깊은 잠에서 깨웠는지도.

띠링.



- [수면] 상태가 해제되었습니다.



은은하게 귓가를 울리는 맑은 종소리.

솜털보다도 가벼워진 눈꺼풀을 들어 올리자, 낯선 천장을 반쯤 가린 채 나를 내려다보고 있는 한 사람의 얼굴이 시야에 가득 찼다.

“저, 정신이 드느냐?”

격정으로 잘게 떨리는 그의 눈동자를 마주하자 문득 그런 생각이 들었다.

내가 얼마나 이 순간을 기다려 왔는지.

그 사실을 깨달음과 동시에, 부드러운 미소가 입가에 번졌다.

본드의 잔재물처럼 끈적하게 남아 있던 조금 전의 악몽 따위는, 이미 흔적도 없이 씻겨 나간 채로.

“예, 스승님.”

“……!”

한 치의 망설임도 없는 자연스러운 호칭에 잠시 멈칫하던 그, 적천강이 먹먹한 음성으로 대답했다.

아니.

정확히는 대답하려고 했다.

다음 순간, 요란한 발걸음 소리와 함께 한 무리의 불청객들이 들이닥치기 전까지는.

“그래, 제…….”

콰드드득!

이어지려던 뒷말을 흔적도 없이 집어삼키는 굉음.

단숨에 문을 박살 내며 병실로 난입한 거한의 등 뒤로, 낯익은 얼굴들이 줄줄이 모습을 드러냈다.

“깼다!”

“깼어!”

“진짜 깼네!”

“와! 칠주야 만에 깨어난 사람 처음 봐요!”

딱, 일 초쯤 걸린 것 같다.

보면서도 믿을 수 없다는 듯, 크게 뜨인 눈으로 나를 바라보던 사람들이 미친 듯이 괴성을 지르며 나를 덮치기까지 걸린 시간이.

“으아아아! 은인!”

“각주우!”

“조장니이이임!”

“…….”

음. 분명히 좋긴 한데.

조금 더 잘 걸 그랬나.



* * *



내가 깨어났다는 소식을 듣고 몰려온 사람들, 그중에서도 특히 화룡각 대원들의 감정이 가라앉기까지는 꽤 오랜 시간이 필요했다.

“저는 정말 아무런 걱정도 안 했어요. 진 공자…… 아니, 각주님이라면 분명히 깨어날 줄 알았으니까.”

말과는 달리 콧물을 훌쩍이며 말하는 주화란의 옆에서, 송일섬이 담담한 어조로 부연 설명을 덧붙였다.

“엄청나게 울더군. 이러다가 영영 못 깨어나는 거 아니냐면서.”

“내, 내가 언제요!”

“어제, 그제. 칠주야 내내.”

얼굴이 벌겋게 달아오른 주화란을 향해 무자비한 팩트 폭격을 날리던 송일섬은, 어느 순간 삽시간에 태도를 뒤집었다.

“아, 내가 사람을 착각했군.”

“들으셨죠? 저 하나도 안 울었어요.”

“…….”

언제 그랬냐는 듯 당당하게 말하는 주화란의 모습에, 나는 모른 척 넘어갈 수밖에 없었다.

조금 전, 그녀가 송일섬에게 슬쩍 건넨 묵직한 전낭의 존재를.

사실 이 귀여운 촌극이 아니더라도, 사방에서 온갖 말들이 물밀듯이 쏟아지고 있었기 때문에 도무지 눈코 뜰 새가 없었다.

“의식을 되찾아서 다행이군. 각주.”

거의 인공지능 수준으로 감정 표현이 미숙한 사마표는 어색한 한 마디를 끝으로 입을 다물었고, 그와는 반대로 짐승 수준으로 감정 표현이 활발한 태산은 눈물을 펑펑 흘렸다.

“태산이, 각주 깨어나서 기쁘다. 너무 걱정돼서 칠주야 내내 하루 세끼씩밖에 못 먹었다.”

“그거 굉장하네.”

비아냥이 아니라, 진심으로 감탄했다.

얼핏 들으면 이게 무슨 정신 나간 소린가 싶겠지만, 태산의 평소 식성을 생각하면 최소 단식 투쟁이나 다름없는 수준이니까.

이제는 지정석처럼 태산의 어깨를 차지한 남 노인이 탄식했다.

“원래 하루 세끼가 정상이다, 이 미친 새끼야…….”

“하도 울었더니 배고프다. 각주, 나는 밥 먹고 오겠다.”

“나는 내려놓고 가라, 이 웬수 같은 놈아.”

물론 씨알도 안 먹힐 소리였다.

태산은 바람처럼 사라졌고, 그저 살기 위해 녀석의 목덜미를 꽉 움켜쥔 남 노인의 비명은 금세 멀어졌다.

그리고 그 빈자리를 채운 건, 미라처럼 붕대로 전신을 칭칭 감은 채 차례를 기다리고 있던 누군가였다.

“조장님…….”

촉촉하게 젖은 목소리.

나는 뭉클한 눈빛으로 녀석을 바라보았다.

“너…….”

“예. 접니다. 조장님의 오른팔, 조장님의 심장. 혁무진입니다.”

“그래, 살아 있었구나. 내 새끼발가락.”

“…….”

“꼬라지만 보면 반쯤 죽은 거 같기는 한데, 용케 숨은 붙어 있는 모양이구나.”

붕대 너머, 금방이라도 눈물을 쏟아낼 것 같던 혁무진의 두 눈동자가 짜게 식었다.

“왜, 뭐.”

“……진짜 너무하신 거 알죠?”

섭섭한 기색이 역력한 녀석의 모습에, 나는 문득 눈살을 찌푸렸다.

“너무하긴 뭘 너무해. 약속을 헌신짝처럼 저버리려고 한 놈이 할 소리는 아니지.”

“예?”

“잊었어? 나랑 했던 약속. 전투 시작되기 전에.”

“아.”

분명히 말했었다.

죽을 거라면, 반드시 내 앞에서 죽으라고. 그럼 반드시 복수해 주겠다고.

하지만 혁무진은 그 약속을 지키지 않을 생각이었던 모양이다.

녀석은 실로 무모했고, 미련하게 싸웠다. 자신의 목숨을 내던지면서까지.

그렇기에, 지금 내가 혁무진에게 해 줄 수 있는 말은 하나밖에 없었다.

“고생했어.”

불쑥 튀어나온 말에 뭐라 대꾸하려던 혁무진이 눈을 동그랗게 뜬다.

아니, 그건 어쩌면 나도 모르게 가라앉은 얼굴과 음성을 때문일지도 모른다.

그랬기에, 나는 애써 웃으며 말을 이었다.

“그리고…… 고맙다. 살아 있어 줘서.”

“……!”

“……!”

일순간, 병실 안의 공기가 찌르르 울렸다.

조금 전까지만 하더라도 소란스럽게 떠들던 사람들이 약속이라도 한 것처럼 입을 다문 채 나를 바라본다.

그들 역시 알고 있을 것이다.

조금 전의 짤막한 한 마디가, 혁무진 뿐만이 아니라 모두에게 하는 말이라는 것을.

이 서투른 감정 표현만이, 지금의 내가 할 수 있는 최선이라는 사실도.

“뭐, 그냥 그렇다고. 꼭 말해야 할 것 같아서.”

가슴 한구석이 일렁이는 기분이다.

나는 기쁨과 슬픔. 그리고 알 수 없는 벅차오름을 감추기 위해 희미하게 웃었다.

그리고 그건 다른 이들 역시 마찬가지였던 모양이다.

누군가는 나를 따라 웃고, 누군가는 조용히 울고, 그런 이들을 그저 말없이 지켜보는 사람들도 있었다.

이 모든 과정을 이미 오래전에 겪은 사람들, 익숙해지는 것이 아니라 무뎌진 이들이 바로 그랬다.

“생각해 보니, 급히 처리해야 할 일이 있었군.”

혼잣말처럼 중얼거린 적천강이 자리에서 일어나며 덧붙였다.

“한, 반 시진은 걸리지 않을까 싶다.”

그 말을 끝으로 적천강을 병실을 빠져나갔다.

어느샌가 문 앞에 선 채, 조용히 우리를 바라보고 있던 또 다른 두 사람과 함께.

- 문득, 그런 생각이 들 때가 있더군.

살성과 함께 돌아서려던 검성 매종학이, 불현 듯 입술을 달싹였다.

- 웃을 수 있을 때 웃고, 울고 싶을 때 울 수 있는 건 큰 축복일지도 모른다고.

노인들이 겪어온 그 길을, 이제는 젊은이들이 걷고 있다.

그렇기에 그들은 잠시나마 자리를 비켜 주려는 것이다.

어쩌면 마지막이 될지도 모르는 이 순간의 감정을 우리가 온전히 누릴 수 있도록.

살아남아 다시 조우한 기쁨도, 떠나간 이들에 대한 슬픔도 모두 받아들여 남은 여정을 이어나갈 수 있도록.

- 쉬고 있게. 다시 오겠네.

나는 조용히 고개를 끄덕였다.

그리고 다시 돌아온 그들과의 대화가 끝났을 때는, 온 세상이 어둠에 잠겨 있었다.

의식을 되찾기 전 꾸었던 악몽 속에서처럼.
```

## Final English reading copy

```markdown
# Chapter 1138

Jin Taekyung slowly blinked.

Where was he?

Everything was dark and hazy.

His small body raced forward, wings spread wide, but his senses felt so dull and чуж-like that he couldn’t clearly feel even the wind brushing over him.

That’s right.

He was a bird now.

And before long, he would escape these damp, hazy clouds swirling all around him.

No—right now.

*Whoosh.*

With one powerful flap of his wings, the clouds that had filled the air around Jin Taekyung like bars vanished.

At the same time, a night sky so dark it looked cold spread before him.

And brilliant, multicolored flames painted across the vast open sky.

*Boom-boom-boom!*

Explosions began without warning, erupting all at once and swallowing the night sky.

From far away, it might have looked beautiful.

But with a bird’s naturally keen eyesight, Jin Taekyung could see what lay beyond the dazzling lights.

Countless fighter jets tore through the sky, rupturing the compressed air around them. Bullets and beams of light shot ceaselessly from the ground and sky.

And—

*Shriek!*

Even the gigantic monsters streaking through the dense web of fire.

*—Kieeeek!*

With a chilling roar, more monsters than the eye could count crossed the dark night sky.

Killing intent tangled with killing intent. At the tail end of every thunderous blast, someone died.

*Kwa-gwa-gwang!*

A blinding flash swallowed the sky.

Jin Taekyung was nothing more than a bird. All he could do was stare, dumbfounded, at the scene before him.

At the humans and monsters falling helplessly like scattered embers amid the ceaseless clash of steel and magic.

Then, suddenly seized by the sense that the whole world had gone dark, he looked up.

*Hsssss.*

At first, he thought it was a storm cloud.

A huge, dark cloud, big enough to blot out even the moonlight.

But it wasn’t.

It was a wing.

The wing of a powerful being, so enormous that anyone who saw it would forget how to breathe—and, in a way, so beautiful.

The moment he faced that overwhelming presence, Jin Taekyung felt his senses sharpen with astonishing clarity.

Perhaps that was why he thought he met the gaze of two eyes like black obsidian, looking down imperiously on everyone below, blotting out even the moonlight.

*Fwoooosh!*

The space warped in an instant.

A terrifying pressure, too much for a mere bird to withstand, crushed the air.

No. It wasn’t only Jin Taekyung.

*Crack-crack-crack!*

Countless fighter jets crumpled under the pressure.

Amid the steel engulfed in flames and falling like a meteor shower, Jin Taekyung felt his consciousness fading.

At the same time, an incomprehensible noise grew ever clearer in his ears.

*Tick.*

A streak of pure white light raced from far away and swallowed him.

* * *

The human brain is much like iron.

Just as iron needs enough heat before it can be reshaped, a human brain that has only just awakened needs a little time before it can function.

But the moment I regained consciousness, I could feel everything around me with a clarity sharper than ever before.

Even what had woken me from that deep sleep.

*Ding.*

> **System**
>
> Sleep status has been lifted.

A clear chime rang softly in my ears.

I raised my eyelids, now lighter than down. A face filled my vision, watching me from above as it half-obscured the unfamiliar ceiling.

“A-Are you awake?”

When my eyes met his, trembling with emotion, a thought came to me.

I realized how long I’d been waiting for this moment.

As that truth sank in, a gentle smile spread across my lips.

The nightmare from moments ago, still clinging to me like the sticky residue of glue, had already been washed away without a trace.

“Yes, Master.”

“……!”

Jeok Cheongang paused at the effortless way I’d addressed him without a moment’s hesitation. Then he answered in a choked voice.

No.

He tried to answer.

Until a crowd of uninvited guests came rushing in with a clamor of heavy footsteps.

“That’s it, my—”

*Crash!*

A deafening crash swallowed the rest of his words.

A burly man smashed the door to pieces and charged into the room. Familiar faces streamed in behind him.

“He’s awake!”

“He woke up!”

“He really woke up!”

“Wow! I’ve never seen anyone wake up after seven days!”

It must have taken about one second.

That was all the time it took for the people staring at me with wide eyes, as if they couldn’t believe what they were seeing, to start screaming like mad and pounce on me.

“Aaah! Benefactor!”

“Pavilion Master!”

“Captain!”

“……”

Yeah. It was nice.

But maybe I should’ve stayed asleep a little longer.

* * *

It took quite a while for everyone who’d rushed over to hear I was awake—especially the members of the Fire Dragon Pavilion—to calm down.

“I really wasn’t worried at all. I knew you’d wake up, Young Master Jin… I mean, Pavilion Master.”

Ju Hwaran sniffled as she spoke, her words at odds with the tears and runny nose. Beside her, Song Ilseom added in his usual calm tone:

“She cried like crazy. Kept saying you might never wake up.”

“I-I never did!”

“Yesterday. The day before. All seven days.”

Song Ilseom delivered that merciless barrage of facts to Ju Hwaran, whose face had turned bright red. Then, in an instant, he changed his tune.

“Ah. I must have mistaken you for someone else.”

“You heard him, right? I didn’t cry at all.”

“……”

Ju Hwaran said it so confidently, as though nothing had happened. I could only pretend not to notice the heavy pouch of money she’d slipped Song Ilseom a moment ago.

Even without that cute little farce, voices were pouring in from all sides, leaving me no time to catch my breath.

“I’m glad you’ve regained consciousness, Pavilion Master.”

Sama Pyo, whose emotional expression was about as sophisticated as artificial intelligence, fell silent after that awkward remark. By contrast, Taishan’s emotions were as lively as a beast’s. He burst into tears.

“Taishan glad Pavilion Master awake. Worried so much, only ate three meals a day for seven days.”

“That’s incredible.”

I wasn’t being sarcastic. I was genuinely impressed.

It sounded insane at first, but considering Taishan’s usual appetite, it was practically a hunger strike.

The old man perched on Taishan’s shoulder as if it were his assigned seat sighed.

“Three meals a day is normal, you crazy bastard……”

“I cried so much, now hungry. Pavilion Master, I go eat.”

“Put me down before you go, you walking disaster.”

Of course, those words went in one ear and out the other.

Taishan vanished like the wind. The old man, who’d grabbed him firmly by the nape just to stay alive, let out a scream that quickly faded into the distance.

The next person to fill the empty space had been waiting his turn, his whole body wrapped in bandages like a mummy.

“Captain……”

His voice was thick with tears.

I looked at him with misty eyes.

“You……”

“Yes. It’s me. Your right arm. Your heart. Hyuk Mujin.”

“Right. You’re still alive, my little toe.”

“……”

“You look half-dead, but somehow you’re still breathing.”

Beyond the bandages, Hyuk Mujin’s eyes, which had looked ready to spill over with tears, turned cold.

“What? What’s with that look?”

“……You know you’re really too much, right?”

At his obvious hurt, I frowned.

“Too much? You’re the one who was about to throw our promise away like it was worthless.”

“What?”

“You forgot? The promise we made before the battle started.”

“Oh.”

I’d told him plainly: if he was going to die, he had to do it in front of me. Then I’d make sure to avenge him.

But Hyuk Mujin apparently hadn’t planned to keep that promise.

He’d fought recklessly, stubbornly, even throwing away his own life.

So there was only one thing I could say to him now.

“You’ve been through a lot.”

Hyuk Mujin had been about to answer my sudden remark, but his eyes widened.

Or perhaps it was the look on my face, and the subdued tone of my voice, that stopped him.

So I forced a smile and continued.

“And…… thank you. For staying alive.”

“……!”

“……!”

The air in the room quivered.

Everyone who’d been chattering noisily a moment earlier fell silent as if on cue and looked at me.

They knew, too.

That my brief words weren’t meant only for Hyuk Mujin. They were for all of them.

And that this clumsy expression of emotion was the best I could manage right now.

“Well, that’s all. I just felt like I had to say it.”

Something stirred in a corner of my heart.

I smiled faintly to hide my joy, my sorrow, and a swelling emotion I couldn’t name.

It seemed the others felt the same.

Some smiled back at me. Some quietly cried. Others simply watched them in silence.

The ones who’d been through all of this long ago were like that. They hadn’t grown used to it. They’d grown numb.

“Come to think of it, I have something urgent to take care of.”

Jeok Cheongang rose to his feet, muttering as if to himself, then added:

“I think it’ll take about half a shichen.”

With that, Jeok Cheongang left the room.

Two other people had appeared at the door at some point, quietly watching us. They went with him.

*There are times when that thought comes to me.*

Sword Saint Mae Jonghak, who had been about to turn away with the Slaughter Saint, moved his lips.

*Being able to laugh when you want to laugh, and cry when you want to cry, may be a great blessing.*

The old men had walked that road before. Now the young were walking it.

That was why they were giving us some space, at least for a little while.

So we could fully experience the emotions of this moment, which might be our last.

So we could accept both the joy of surviving and meeting again, and the grief for those who had left us, and continue along the journey ahead.

“Get some rest. I’ll be back.”

I quietly nodded.

And by the time the conversation with them, who had returned, was over, the whole world had sunk into darkness.

Just like the nightmare I’d had before regaining consciousness.
```
