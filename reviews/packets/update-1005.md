<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1005.txt",
      "sha256": "e1023a3ee1228249bd66ca1b2a64be2985d54ab0196d89ba6203323ed4c25667",
      "bytes": 12905
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ad3271cd955094715c10da371b09e7b570ca4e3c900e09f3bd60ba72cd791b24",
      "bytes": 615
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a2ba2080787f93b9df4a81c1f6c7b6f602a1beff6efab59540e4d4c1fd5ee248",
      "bytes": 237214
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c4fec4de4e2c5a1790b232ef81a9a9b7692dbe753cf8e704030e1bfd9b6b8cac",
      "bytes": 760
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "29fca7804822aa57de9af58cacc701d27ede0159b453521aedcdad5eac307b56",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "040b972605394037358c4aec37b43091eabf77984551d7de2367a261d5a9c1e7",
      "bytes": 1408
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e9fd3660d182e43bc24c789bd0cc125936e2ea15c2e0421c493943d0a615b6c7",
      "bytes": 1614
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "2e494ada3bc591edd2a9351f8d1924805adfc5745e42acf7ca948e349e159fcb",
      "bytes": 623
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "24851a1ed2eb5e39210336b6fc7b402ee8fd236847cd5e71ac426fd724cb4286",
      "bytes": 974
    },
    {
      "path": "characters/Namho.md",
      "sha256": "5b715427147621a0b36c5e45917c8f151fc2ebca1e0fa580a138349e1667e46b",
      "bytes": 1092
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "c0526d6152a08b332fcc9ab6f9cba70e06b7c8adefd7268db089c197958d017b",
      "bytes": 937
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "5874ec3975a1e880592716ca186c97797927d018c53f12e316f01aea39c7161f",
      "bytes": 742
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "a515dd77c2c14f4086c2b631eb63470911f817ad6028533bb0779c7072cc026f",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "7917fac196cc2d43a54ec5350534c88d7ef6ddc6e94e32c46fa129c3e32e7c6c",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "15e8d2d61ab054a660927780151270798b6de1cadfd2e02f0adccf68c3033809",
      "bytes": 275396
    }
  ],
  "estimated_tokens": 13857
}
-->

# Durable State Update — Chapter 1005

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
1 and safe_through 1005. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1005. Profile updates may replace only one
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
  "chapter": 1005,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1005,
    "continuity_sources": [1005],
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
    "Taekyung’s party has reached an occupied city where Sima Gong and roughly a thousand Black Dragon Demon Gate disciples are gathered; the streets are empty, with no visible battle or blood.",
    "Sima Gong is Sama Pyo’s father and has a familiar, openly contentious relationship with Jeok Cheongang.",
    "Taekyung noticed Sama Pyo’s eyes sink as his father approached."
  ],
  "continuity_sources": [
    1004
  ],
  "open_questions": [
    "Why did Sama Pyo’s eyes sink as his father approached?"
  ],
  "safe_through": 1004,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 주화입마   | **qi deviation**                                 |                                                       |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 낭인     | **wandering martial artist**                     |                                                       |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 문주     | **Sect Leader**                              |
| 소문주    | **Young Sect Leader**                        |
| 제자     | **Disciple**                                 |
| 선배     | **Senior**                                   |
| 민첩               | **Agility**                    |
| 태원     | **Taiyuan**            |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 소원 | **Sowon** | Name called out by Im Kkeokjeong during the Wyvern attack. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 기경팔맥 | **Eight Extraordinary Meridians** | The eight extraordinary meridians of wuxia physiology. |
| 흑룡마문 | **Black Dragon Demon Gate** | Unorthodox faction from Gansu. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |

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
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
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
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 남호 | 사마표 | guide_to_young_sect_leader | Young Sect Leader | blunt and admonishing | Namho warns Sama Pyo that all grass and animals in the territory belong to the Nanman Beast Palace. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 사마표 | 남호 | young_sect_leader_to_guide | Elder Namho | formal and apologetic | Sama Pyo apologizes after Taishan attempts to seize the calf. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 주화란 | 조장님 | pavilion member to squad leader | Captain | familiar and deferential | Hwaran asks Captain where he is going before he confronts the mistreatment. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 신의 | 주화란 | senior physician to younger ally | Young Lady Ju | warm and teasing | The Divine Physician lightly teases Hwaran about being more worried for Jin than he is. |
| 남호 | 적천강 | junior_to_senior | Senior | respectful and formal | Namho refers to Jeok as 노선배님 while agreeing with him. |
| 신의 | 태산 | senior physician to younger ally | Young Hero Taishan | urgent and respectful | The Divine Physician uses this address while pleading with Taishan to keep moving. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1002
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1004
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1004
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1004
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Peng Cheolhu regarded Taekyung as a worthy successor, inheriting all that Peng had to pass on; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1004
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1003
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 1004
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years undercover in Nanman and maintained contact with Central Plains intelligence through the Pavilion’s Hidden Thread; he guides the Fire Dragon Pavilion and represents Jin Taekyung and the Murim Alliance in negotiating the survivors’ chance to rebuild the Murong household.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1004
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1000
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 995
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1003
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1005화



나흘.

결코 길다고 말할 수 없는 시간이다.

그러나 꼬박 나흘 동안 일체의 휴식을 최소화한 채, 말안장 위에서 토막잠을 자며 달려왔다면 이야기는 달라진다.



‘쉴 수 있을 때 쉬어 둬. 지금이 아니면 언제 또 시간이 날지 모르니까.’



진태경은 그 한 마디를 남기고 수뇌부 회의를 위해 자리를 옮겼고, 남겨진 화룡각 대원들은 각주의 명령을 충실하게 이행했다.

그렇게 지금.

그들은 얼마 안 되는 짐을 풀고, 따뜻한 물로 목욕을 끝마친 다음 어느새 차려진 산해진미 앞에 앉아 있을 수 있었다.

물론 당연하게도 적천강과 사마표는 예외였다.

화왕(火王)이라는 일세의 거인은 굳이 이유를 설명할 필요조차 없고, 흑룡마문(黑龍魔門)의 소문주라는 직함 또한 충분히 수뇌부에 포함될 자격이 있는 위치였으니까.

“후아, 이제야 좀 살 것 같네요.”

주화란의 그 한마디는 화룡각 대원들의 마음을 대변하는 것이나 다름없었다.

육체적인 피로도 피로지만, 그와는 비교도 할 수 없이 몸과 마음을 옥죄는 것은 정신적인 피로다.

어쩌겠나.

일평생 동안 사선(死線)을 넘나드는 것은 무림인의 숙명이요, 전쟁으로 말미암은 상실감과 고통은 난세(亂世)를 살아가는 이들의 운명인 것을.

늘 그랬고, 앞으로도 그럴 터였다.

그나마 다행인 점은 이 자리에 있는 화룡각 대원 모두가 그런 자신들의 처지를 정확히 인지하는 동시에 받아들였다는 부분이었다.

“각주가 했던 말이 맞소. 시간이 있을 때 최대한 쉬어 두어야 후일을 대비할 수 있는 법. 그런 의미에서 어서 드십시다.”

식사를 권하는 송일섬의 말에, 이미 볼 한가득 음식을 쑤셔 넣고 있던 혁무진이 고개를 들었다.

“눼?”

“…….”

“밤금 머라 해써요.”

“…….”

“모라 해던 거 가튼데.”

말없이 혁무진을 바라보던 송일섬이 대답했다.

“아니다. 신경 쓰지 말고 마저 먹어라. 원래 아플수록 더 배고픈 법이지.”

“아, 눼.”

정수리에 볼록 솟아 있는 혹이 신경 쓰이는지, 흐름이 깨진 김에 슬쩍 자신의 머리를 쓰다듬은 혁무진이 다시 접시에 코를 박았다.

그리고 다음 순간, 다시 고개를 들어 송일섬을 빤히 바라보았다.

“잠깜. 왜 밤말해여? 갑자기 기븜 나브네.”

“쭉 그랬는데.”

“그래서 더 기븜 나브네. 내가 몉 번이나 그러지 말라 행는데.”

“그야 간단하지. 내가 그쪽보다 더 나이가 많으니까.”

꿀꺽.

입안에 든 것을 씹어 삼킨 혁무진이 눈살을 찌푸렸다.

“이거 웃기는 양반일세. 그래 봤자 꼴랑 한두 살 차이면서.”

“한두 살은 나이가 아닌가?”

“그건…… 맞긴 한데.”

“무림인으로서의 경륜도 내가 더 높다는 것 역시 익히 알고 있을 테고.”

“그것도…… 맞긴 한데.”

“선배인데다 연장자. 그럼 문제없는 것 아닌가?”

어째 대화가 이어질수록 불리해지는 상황.

그때, 눈동자를 뒤룩뒤룩 굴리던 혁무진의 뇌리에 반박의 단초가 떠올랐다.

“우리 조장님 나이 알죠?”

송일섬이 담담한 목소리로 대답했다.

“대충은.”

“나보다 훨씬 어립니다.”

“그래서?”

“어허, 그래서라니! 조장님한테는 최소한 하오체 쓰면서, 왜 나한테는 함부로 반말……!.”

“그래서?”

“……예?”

“그래서. 뭐 어쩔 거냐고 묻는 거다.”

“…….”

아니, 이렇게 나오면 할 말이 없는데.

터무니없이 당당한 송일섬의 모습에, 말없이 눈을 끔뻑거리던 혁무진은 문득 가슴 깊은 곳에서 솟구치는 불길을 느꼈다.

생각해 보니 이 얼마나 억울한 일인가.

틈만 나면 날아오는 진태경의 구박이야 그렇다 치자, 그 정도야 오른팔이자 심장을 자처하는 충복으로서 기쁘게 받아들일 수 있다.

하지만 도중에 합류한 낭인 나부랭이, 물론 나부랭이치고는 그 바닥에서 엄청 유명한 데다 알고 보면 대단한 무가(武家)의 후예지만 아무튼 그런 송일섬한테까지 이런 취급을 받다니.

‘내가 어? 엄연히 서열로 따지면 화룡각 부각주인데! 게다가 태원진가도 이제 오대세가의 반열에 들었는데!’

송일섬을 바라보는 혁무진의 눈동자에 불이 붙었다. 아까부터 손에 쥐고 있던 닭다리 구이가 마치 공명하는 검처럼 부르르 떨렸다.

“손에 든 그거, 집어 던지기라도 할 생각인가?”

“왜, 못 할 것 같아요?”

혁무진의 스산한 목소리에, 송일섬이 망설임 없이 고개를 끄덕였다.

“물론.”

“맞습니다. 정확하시군요.”

“다만 뒷일은 알아서 감당…… 지금 뭐라고?”

“먹을 거 버리면 천벌 받습니다. 그리고 저희 부모님이 그랬어요. 주위 사람들이랑 늘 사이좋게 지내라고.”

“…….”

“왜요. 할 말 있어요? 그럼 배고프니까 가급적 빨리 하세요. 귀한 음식 다 식기 전에.”

이걸 당당하다고 해야 하나, 비굴하다고 해야 하나.

아니면 둘 다?

‘뭐지, 이놈.’

이토록 당당하게 비굴함을 피력할 수 있다니.

짜게 식은 눈빛으로 혁무진을 응시하던 송일섬이 입을 열었다.

“……아니다. 좋은 부모님을 뒀군.”

“순박한 분들이시죠. 칭찬 감사합니다.”

기다렸다는 듯이 대답한 혁무진은 다시 맹렬한 기세로 눈앞의 음식들을 쓸어담기 시작했고, 송일섬은 내심 한숨을 내쉬었다.

‘이놈이고 저놈이고, 죄다 제정신이 아니군.’

제아무리 편하게 휴식을 취하라 했다지만, 누가 저 모습을 보고 전투를 앞둔 이라 생각하겠나.

객잔 거덜내러 온 거지새끼면 몰라도.

‘아니, 두려움이라는 게 아예 없나?’

미친놈들이 널리다 못해 사방에 깔린 낭인 바닥에서 구를 만큼 구른 그였지만, 약 일 년 전부터 함께하게 된 저들은 하나부터 열까지 뭔가 이상했다.

이를테면…….

‘진짜 광기.’

지금껏 겪어 왔던 미친놈들과는 농도부터가 다르다.

그리고 이미 상당히 미친놈인 혁무진조차 화룡각 전체로 보면 평균에 불과했다.

우선 첫 번째로, 화왕 적천강.

“…….”

말이 필요 없다. 단지 떠올리는 것만으로도 송일섬의 숨이 턱 막혀 오는 것이 바로 그 증거다.

적천강을 곁에서 지켜보며 송일섬이 다시금 크게 깨달은 부분이 있다면, 그건 바로 아직도 약육강식(弱肉强食)의 법칙이 이 세상을 장악하고 있다는 사실이었다.

‘그렇지 않았다면, 이미 몇 번쯤 죽고도 남았을 테니까.’

그렇게 생각하는 이유?

간단하다.

적천강은 자신의 마음에 들지 않는 놈이라면 그게 누구든 가리지 않고 공평하게 두들겨 팼다.

문파도, 성향도, 나이와 성별도 상관없었다.

상대가 정파인이라면 명검보다 날카로운 혀끝으로 상대방의 가슴을 후볐고, 사파나 흑도라면 즉시 주먹부터 날릴 각을 쟀으며, 마인에 대해서는 언젠가 그런 말을 남겼다.



‘이제 와서 하는 말이지만, 사실 노부의 오랜 소원은 천하의 마인 모두를 선하게 교화(敎化)시키는 것이다.’



그러자 진태경이 모두를 대신해 노망이 났냐고 물었고, 자신의 제자를 흠씬 두들겨 팬 적천강은 당당하게 덧붙였다.



‘물론, 착한 마인은 죽은 마인밖에 없느니라.’



적천강은 그런 사람이었다.

오죽하면 그의 하나뿐인 제자가 자신의 스승을 두고 이렇게까지 말했겠나.



‘내가 진지하게 생각해 봤는데, 저 양반은 정마대전 때 정파 도운 게 신의 한 수야. 덕분에 왕 소리 들으면서 합법적으로 여기저기 깽판 칠 수 있잖아. 안 그래요, 다들?’



아마 진태경은 모를 것이다.

모두가 그 말에 동의를 표하면서도, 진태경이 돌아선 순간 서로를 향해 비슷한 의미가 담긴 시선을 교환했다는 것을.



‘지는.’

‘저 입에서 저딴 소리가 나오네.’

‘조장님은 혹시 양심이라는 단어를 모르시는 걸까?’

‘죄송해요, 진 공자. 아무리 그래도 이건 좀 아닌 것 같아요…….’

‘태산이, 배고프다.’



그 누구도 차마 대놓고 말은 못 했지만, 적천강을 뛰어넘을 유일한 미친놈이 있다면 그건 바로 진태경이라는 것쯤은 모두가 알고 있는 사실이었다.

‘그놈이야말로 진짜 미친놈이긴 하지, 여러 가지 의미로.’

무공도 미쳤고, 성질머리도 미쳤다.

가끔은 무슨 바람이 불었는지 정상적인 척을 하지만, 한번 심기가 뒤틀려 버리면 스승인 적천강조차 뛰어넘는 모습들을 보여 주는 것이 진태경이었다.

‘그런 의미에서는 저놈이 오히려 더 악질이다.’

적천강과 진태경 중 한 명과 싸우라면, 송일섬은 망설임 없이 전자를 택할 것이다.

스승의 무공이 더는 제자보다 못하다고 생각해서?

틀렸다.

주화입마가 염려될 만큼 온갖 쌍욕을 얻어먹어도, 멸염신권으로 기경팔맥(奇經八脈)이 으스러져도 적천강이 낫다.

그는 화왕이니까.

천하에 모르는 이가 없는 거인이요, 그 자체로 아득한 세월을 살아온 노괴(老怪)니까.

하지만 진태경은?

‘……생각하기도 싫군.’

떠올리는 것만으로도 송일섬의 속이 울렁거렸다.

이제는 닿을 수 없을 만큼 멀어진 고강한 무위는 둘째치고, 확실히 스승을 뛰어넘었다는 평을 듣는 설공(舌功)은 악몽 그 자체다.

그나마 한 가지 위안이라면, 저 무시무시한 혓바닥이 항상 적들을 상대로만 제대로 된 위력을 발휘했다는 점이었다.

물론 그런 것을 제외하고서라도, 송일섬은 사마표나 주화란과 함께 가장 갈굼을 덜 받는 사람 중 하나였다.

설령 뭔가 갈굴 만한 일이 생기더라도 진태경은 짧은 한마디와 돌아서곤 했다.



‘개노잼.’



저 세 글자가 정확히 무슨 의미인지는 송일섬도 몰랐지만, 결코 좋은 의미가 아니라는 것쯤은 짐작할 수 있었다.

‘나한테는 개노잼. 사마표에게는 십노잼이라고 했었지. 하지만 주 소저에게는 아무 말도 하지 않았다.’

그럼 뭐겠는가. 뻔하지.

한때 심각하게 저 표현의 정확한 의미를 고민한 적도 있던 송일섬이었으나, 어느 순간부터는 신경조차 쓰이지 않았다.

익숙해져서?

글쎄. 그보다는…….

“음.”

무심코 흘린 침음성과 함께, 송일섬은 깊은 상념에서 깨어났다.

그리고 비로소 주위의 상황을 인지한 순간, 무언가 크나큰 문제가 생겼음을 깨달았다.

“도대체…… 무슨 일이 벌어지고 있는 거지?”

특정한 누군가에게 던진 물음이 아니라 경악에 가까운 혼잣말.

눈을 부릅뜬 채 굳어버린 송일섬을 향해, 심각한 얼굴을 한 주화란과 혁무진이 차례대로 입을 열었다.

“저희도 몰라요. 이게 어찌 된 일인지.”

“대담해! 맘도 암 대!”

주화란의 대답은 근심으로 가득했고, 혁무진의 대답에는 음식이 가득했다.

투두둑!

평소의 송일섬이었다면 민첩한 몸놀림으로 음식 찌꺼기 세례를 피했겠지만, 이번만큼은 불가능했다.

철퍽!

살에 닿는 불쾌한 감촉.

그러나 자신이 벌인 일에 굳어 버린 혁무진의 우려와 달리, 송일섬은 아무런 행동도 취하지 않았다.

다만 살아 있는 용을 마주친 것 같은 충격에 휩싸여, 한 사람에게서 시선을 떼지 못할 뿐이었다.

먹음직스러운 산해진미를 눈앞에 두고도, 두 어깨를 축 늘어트린 채 꼼짝도 안 하고 있는 태산의 모습을.

“지금 내가 헛것을 보고 있는 건가?”

누군가의 입술 사이로 불신에 찬 그 한마디가 흘러나온 순간이었다.

“제대로 보고 있네. 다만 지금은 좀 조용히 해 줬으면 좋겠는데.”

착 가라앉은 목소리.

처음부터 지금까지 줄곧, 어떤 생각에 잠겨 미동도 하지 않던 남호가 코끝을 움찔거렸다.

마치, 그리 오래되지 않은 어느 날의 기억에 남아 있는 냄새를 좇으려는 듯.
```

## Final English reading copy

```markdown
# Chapter 1005

Four days.

You couldn’t exactly call that a long time.

But if you’d spent all four days riding hard, barely stopping to rest and catching only snatches of sleep in the saddle, that was another matter.

*Rest while you can. Who knows when we’ll have another chance?*

Jin Taekyung had left them with those words, then gone off to a meeting with the leadership. The Fire Dragon Pavilion members he’d left behind had faithfully followed their Pavilion Master’s orders.

And so, now, they’d unpacked their few belongings, finished bathing in warm water, and settled in before a sumptuous feast that had somehow already been laid out.

Naturally, Jeok Cheongang and Sama Pyo were the exceptions.

The Fire King was a towering figure of his generation. He needed no explanation. And the title of Young Sect Leader of the Black Dragon Demon Gate placed Sama Pyo well within the ranks of the leadership.

“Whew. I finally feel alive again.”

Ju Hwaran’s words might as well have spoken for every member of the Fire Dragon Pavilion.

Physical exhaustion was bad enough, but mental fatigue squeezed at the body and mind in a way that put it to shame.

What could they do?

For a martial artist, crossing the line between life and death was a lifelong fate. The grief and pain brought on by war were the lot of those living through troubled times.

It had always been that way, and it would stay that way.

At least everyone in the Fire Dragon Pavilion understood their circumstances clearly—and had accepted them.

“Our Pavilion Master was right. We have to rest as much as we can while we have the time if we’re to prepare for what comes next. With that in mind, let’s eat.”

At Song Ilseom’s invitation, Hyuk Mujin looked up, his cheeks already bulging with food.

“Wha’?”

“……”

“Wha’ did you jus’ say?”

“……”

“Sounded like you said somethin’.”

Song Ilseom stared at him in silence, then answered.

“Nothing. Don’t worry about it. Go ahead and eat. The more pain you’re in, the hungrier you get.”

“Ah, okay.”

Perhaps the bump sticking out of the crown of his head was bothering him. With the conversation interrupted, Hyuk Mujin took the opportunity to rub it, then buried his face in his plate again.

A moment later, he looked up and stared intently at Song Ilseom.

“Wait. Why’re you talkin’ down to me? I don’t like that.”

“I’ve been doing it this whole time.”

“That’s why I don’t like it. I’ve told you a bunch of times not to.”

“It’s simple. I’m older than you.”

Gulp.

Hyuk Mujin swallowed what was in his mouth and frowned.

“What a ridiculous guy. You’re only a year or two older than me.”

“Does a year or two not count as an age difference?”

“Well… I guess it does.”

“And you know perfectly well that I have more experience as a martial artist.”

“That too… I guess.”

“I’m your senior, and I’m older. So what’s the problem?”

The longer the conversation went on, the worse things seemed to get for Hyuk Mujin.

His eyes rolled around as he searched for a counterargument. Then an idea came to him.

“You know how old our Captain is, right?”

“More or less.”

“He’s way younger than me.”

“So?”

“Hey, what do you mean, ‘So?’ You use at least a polite form of speech with the Captain. Why do you get to talk down to me—”

“So?”

“……Huh?”

“So. What are you going to do about it?”

“……”

There was nothing he could say to that.

As Hyuk Mujin blinked at Song Ilseom’s absurdly confident attitude, he suddenly felt anger rising from deep in his chest.

Now that he thought about it, how unfair was this?

He could put up with Jin Taekyung giving him a hard time whenever he got the chance. That much he could gladly accept as the loyal right hand and self-proclaimed heart of his Captain.

But now he was being treated this way even by Song Ilseom—a lowly wandering martial artist who’d joined them along the way. Sure, for a mere wanderer, he was famous as hell in those circles, and, as it turned out, he came from an impressive martial family. But still!

*I mean, come on! By rank, I’m the Vice Pavilion Master of the Fire Dragon Pavilion! And the Jin Family of Taiyuan is one of the Five Great Families now!*

A fire lit in Hyuk Mujin’s eyes as he glared at Song Ilseom. The roasted chicken leg in his hand, which he’d been clutching for a while, trembled as though it were a sword resonating with its wielder.

“Planning to throw that thing you’re holding?”

“Why? Think I can’t?”

At Hyuk Mujin’s chilly reply, Song Ilseom nodded without hesitation.

“Of course you can’t.”

“That’s right. You know me well.”

“But you’ll have to deal with what happens afterward… Wait, what did you say?”

“If you throw away food, heaven will punish you. Besides, my parents always told me to get along with the people around me.”

“……”

“What? Got something to say? Then say it quickly. I’m hungry, and I don’t want the precious food to get cold.”

Was that confidence? Cowardice?

Or both?

*What is with this guy?*

How could anyone be so shameless about being such a coward?

Song Ilseom watched Hyuk Mujin with a thoroughly unimpressed look, then spoke.

“……Never mind. You had good parents.”

“They’re kind, simple people. Thanks for the compliment.”

Hyuk Mujin replied as if he’d been waiting for those words, then set to work sweeping the food in front of him into his mouth with renewed vigor. Song Ilseom sighed inwardly.

*Every last one of them is out of their minds.*

They’d been told to rest and take it easy, but who would look at that and think they were about to go into battle?

They looked more like a pack of beggars come to bankrupt an inn.

*Or do they not feel fear at all?*

Song Ilseom had spent years among wandering martial artists—a crowd of crazies so thick you could hardly turn around without running into one. But the people he’d been with for the past year or so were strange from top to bottom.

For example…

*True madness.*

The degree of it was on another level from anything he’d seen before.

And Hyuk Mujin, who was already plenty crazy himself, was merely average by Fire Dragon Pavilion standards.

First, there was Jeok Cheongang, the Fire King.

“……”

No words were needed. The proof was how Song Ilseom’s breath caught just thinking about him.

Watching Jeok Cheongang up close had driven one point home once again: the law of the jungle still ruled the world.

*If it didn’t, Jeok Cheongang would have been dead several times over by now.*

Why did he think that?

Simple.

Jeok Cheongang beat the living daylights out of anyone he didn’t like. Anyone at all. He was fair about it, at least.

Their sect, their principles, their age, their sex—it made no difference.

If they belonged to the orthodox faction, he’d dig into their hearts with a tongue sharper than a famous sword. If they were from the unorthodox faction or the dark-path underworld, he’d immediately size them up for a punch. As for fiends, he’d once said:

> *“I may as well tell you now: for many years, my fondest wish has been to reform every fiend beneath heaven and make them good.”*

Jin Taekyung had asked on everyone’s behalf if he’d gone senile. Jeok Cheongang had beaten his own Disciple senseless, then added, as brazen as ever:

> *“Of course, the only good fiend is a dead fiend.”*

That was the kind of person Jeok Cheongang was.

What else could explain his one and only Disciple saying this about his own Master?

> *“I thought about it seriously, and helping the orthodox faction during the Great Faction War was the best move that old man ever made. Now he gets to be called a king and wreak havoc wherever he wants, all perfectly legally. Am I right, everyone?”*

Jin Taekyung probably didn’t know.

Everyone had agreed with him, but the moment he turned away, they’d exchanged looks that all meant roughly the same thing.

> *“Look who’s talking.”*
>
> *“How does he have the nerve to say that?”*
>
> *“Does our Captain even know what the word ‘conscience’ means?”*
>
> *“Sorry, Young Master Jin. This is a bit much, even for you……”*
>
> *“Taishan hungry.”*

No one dared say it outright, but everyone knew the only person crazier than Jeok Cheongang was Jin Taekyung.

*That guy’s the real lunatic, in more ways than one.*

His martial arts were insane, and so was his temper.

Sometimes, for reasons known only to him, he’d act like a perfectly normal person. But when something rubbed him the wrong way, he could show a side that even surpassed his Master, Jeok Cheongang.

*In that sense, he’s even worse.*

If Song Ilseom had to fight either Jeok Cheongang or Jin Taekyung, he’d choose the former without hesitation.

Because he thought Jeok Cheongang’s martial arts were no match for his Disciple’s anymore?

Wrong.

Even if Jeok Cheongang cursed him with every filthy word in the world until he feared qi deviation, even if his Flame-Extinguishing Divine Fist crushed Song Ilseom’s Eight Extraordinary Meridians, Jeok Cheongang would still be preferable.

Because he was the Fire King.

A giant known throughout the world, an old monster who had lived through ages beyond counting.

But Jin Taekyung?

*……I don’t even want to think about it.*

Just remembering him made Song Ilseom’s stomach churn.

His martial prowess, now so far beyond Song Ilseom’s reach, was one thing. But his reputation for surpassing his Master in the art of verbal abuse was a nightmare all on its own.

The one small comfort was that his terrifying tongue always seemed to work at full strength only against enemies.

And even aside from that, Song Ilseom was one of the people who got the least grief from Jin Taekyung, along with Sama Pyo and Ju Hwaran.

Even when he did something worth getting chewed out for, Jin Taekyung would just toss out a short line and turn away.

> *“So boring.”*

Song Ilseom didn’t know exactly what the expression meant, but he could guess it wasn’t a compliment.

*He said I was “so boring.” He called Sama Pyo “ten times more boring.” But he didn’t say anything to Young Lady Ju.*

What else could that mean? It was obvious.

Song Ilseom had once spent a long time seriously puzzling over the exact meaning of the expression, but at some point he’d stopped caring.

Had he gotten used to it?

Maybe. Or maybe…

“Hmm.”

With a low hum, Song Ilseom came back to himself from his deep thoughts.

Only then did he notice what was happening around him—and realize that something was terribly wrong.

“What on earth… is going on?”

It wasn’t a question directed at anyone in particular. It was closer to a disbelieving gasp.

Song Ilseom stood frozen, eyes wide. Ju Hwaran and Hyuk Mujin, both wearing serious expressions, answered in turn.

“We don’t know either. What happened?”

“Incredibuh! Makes no shensh!”

Ju Hwaran’s answer was full of worry. Hyuk Mujin’s was full of food.

Pth, pth!

Usually, Song Ilseom would have dodged the spray of food with a quick sidestep. This time, he couldn’t.

Splut!

Something unpleasant touched his skin.

Hyuk Mujin froze, worried about what he’d done. But despite his fears, Song Ilseom didn’t move.

He could only stare at one person, stunned as if he’d come face-to-face with a living dragon.

Taishan was sitting before a feast fit for a king, yet his shoulders drooped and he didn’t move at all.

“Am I seeing things?”

Just as those disbelieving words slipped from someone’s lips—

“You’re seeing it right. But I’d like you to keep it down for now.”

The voice was quiet and low.

Namho, who’d been sitting motionless from the start, lost in thought, twitched his nose.

As if he were following the scent of a memory from a day not so long ago.
```
