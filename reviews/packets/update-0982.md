<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0982.txt",
      "sha256": "35945bed2999ce95ddd8798bed2163f91541db593da66729f10971d69d55f2cb",
      "bytes": 13488
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "359c0b1356489775a0e439f8850a15f80e7c0d286086ecce7d2be3f94ba01b6c",
      "bytes": 769
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "534144353e21b1e77df6e1cab1ddd1ec71ab53581386f9d3c49a34452f7ba359",
      "bytes": 235946
    },
    {
      "path": "characters/Cheolyeong.md",
      "sha256": "31ec2c21aab8ff9709bdba2ca072e1115d4d2c73ebfa21fa7bb90ebb1966e9c3",
      "bytes": 342
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "0b39ae0bf229bd7e6eb948b037dc959f57a6aada362d99ae8d769d5e8ef74688",
      "bytes": 759
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "857f461279a03d9ca75dddc004da10eef2502fa6adbc1233e276c8dc8413ab0d",
      "bytes": 1374
    },
    {
      "path": "characters/Jamukha.md",
      "sha256": "5baf953e5978387026ecf4e9415d3d0d94e392259cb07960561ea268268641ed",
      "bytes": 611
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "51c19ee01a7f2bedde421425bbc56a1081314625e18979e4ce0e6ec18e5377f1",
      "bytes": 1291
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "856fd406bfad5c903cd1dcb53e3eb15e2303ae7f50e2d8d4d870f1d5a183cdd4",
      "bytes": 699
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "b7e5333f8560ba8d77f784f3b5cd5292f1faafd61ed58ccaeb198f45f7622433",
      "bytes": 1665
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "91115abfe13185c60d0e92c52d19be3d66d92e61fe773d8a9e002427c85de5da",
      "bytes": 1116
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "4158bd130a39e18546bf5161dbbde443d82eacf645b9d39bd92c536bb3e2b121",
      "bytes": 699
    },
    {
      "path": "characters/Murong Baek.md",
      "sha256": "c1a0b736e6ffe1771ce798788c9e38f77481d7fc9ff9b7bb9c88d939461d0487",
      "bytes": 660
    },
    {
      "path": "characters/Murong Yeonghwi.md",
      "sha256": "293384bb5235e212152ac63fd6bf93460dc98e70f0470a31fb788d81b8d9d56b",
      "bytes": 548
    },
    {
      "path": "characters/Peng Cheolhu.md",
      "sha256": "e6a42bc8a3f768aae1ca9f41f5fcd9df6a48733c37d4f5a9518fb4d2b235da89",
      "bytes": 898
    },
    {
      "path": "characters/Peng Cheolyeong.md",
      "sha256": "c9621311ef0c22baea716d2b71482be4328bb1d0e1bd6e88798db771be743147",
      "bytes": 679
    },
    {
      "path": "characters/Temur.md",
      "sha256": "37289e5bf9e192a3944b7ea7c918077f6b8457411ce1abce0d3b4b950bc6655a",
      "bytes": 664
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "72b0d9a52c66f2121e2ec65972b15461f692c3f85e248be2e14d1cd9eccceea1",
      "bytes": 271880
    }
  ],
  "estimated_tokens": 13407
}
-->

# Durable State Update — Chapter 982

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
1 and safe_through 982. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 982. Profile updates may replace only one
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
  "chapter": 982,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 982,
    "continuity_sources": [982],
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
    "The battle at Eight Spring Gorge ended in victory, with over five thousand casualties, including more than three thousand dead.",
    "Cheol Mubaek died protecting Jin Mukyung against the Demon Bird and left him the Shura Annihilating Fist manual.",
    "Peng Cheolhu remains unconscious from severe injuries.",
    "The Emperor remains gravely ill with Blood Soul Gu; the treatment said to require him to die once remains unresolved."
  ],
  "continuity_sources": [
    981
  ],
  "open_questions": [
    "Will Peng Cheolhu regain consciousness?",
    "Can the Emperor be treated for Blood Soul Gu, and what does the treatment requiring him to die once entail?"
  ],
  "safe_through": 981,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 궁성     | **Bow Saint**                 | —              |
| 벽력도왕   | **Thunderbolt Saber King**    | Peng Cheolhu   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 하북팽가   | **Hebei Peng Family**            |
| 진주언가   | **Jinzhou Yan Family**           |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 정파     | **orthodox faction**                             |                                                       |
| 중원     | **Central Plains**                               |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 선배     | **Senior**                                   |
| 은인     | **Benefactor**                               |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 철영 | **Cheolyeong** | Peng Cheolhu’s eldest son and the current Family Head of the Peng Family. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 자무카 | **Jamukha** | Khan of the western grasslands and the steppe army’s practical leader. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 모용백 | **Murong Baek** | Former northern rival and later comrade of Peng Cheolhu. |
| 모용영휘 | **Murong Yeonghwi** | A blood relative of the Murong Family regarded as an overwhelmingly powerful young prodigy. |
| 팽철영 | **Peng Cheolyeong** | Family Head of the Hebei Peng Family and successor to the Thunderbolt Saber King. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 대칸 | **Great Khan** | Title of the former ruler whose descendants Temur and Chinggen claim to be. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 철혈도 | **Iron Blood Saber** | Epithet of Peng Cheolyeong. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 이동진 | **Moving Formation** | Dark Heaven's inactive long-distance transportation formation. |
| 모용세가 | **Murong Family** | One of the Five Great Families, based in Liaoning. |
| 요녕 | **Liaoning** | Northeastern region from which the Murong Family arrives. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 북천 | **North Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 전서 | **missive** | A written message exchanged or delivered in secret. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 상산후 | **Marquis of Shangshan** | Title bestowed on Jin Taekyung by the Emperor. |
| 요녕성 | **Liaoning Province** | Province ruled by the Murong Family. |
| 중양절 | **Double Ninth Festival** | Festival used as the expected date for the invasion of the Central Plains. |
| 북천마군 | **North Heaven Demon Lord** | Title of Murong Baek. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 적천강 | 벽력도왕 | rival_martial_master_to_rival_martial_master | Virility Saber King | insulting and taunting | Jeok coins 정력도왕 as a taunting replacement for the established title. |
| 벽력도왕 | 적천강 | rival_martial_master_to_rival_martial_master | Jeok Cheongang | boisterous and hostile-teasing | The Thunderbolt Saber King calls Jeok by name before their argument escalates. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 테무르 | 자무카 | fellow_khan_to_elder_khan | Khan Jamukha | formal-respectful | Temur affirms Chinggen’s public praise of Jamukha. |
| 자무카 | 진무경 | hostile opponents | you | familiar, blunt, and patronizing | Jamukha uses 자네 while urging Mukyung to submit and become his hunting dog. |
| 벽력도왕 | 모용백 | former rivals turned comrades and friends | Murong Baek; Family Head Murong | familiar and warm | Peng Cheolhu greets him by name and asks whether he should now use his family-head title. |
| 모용백 | 벽력도왕 | former rivals turned comrades and friends | you | familiar and cautionary | Murong Baek asks Peng Cheolhu whether he agrees that people like Jamukha require constant vigilance. |
| 모용백 | 자무카 | commander_to_subordinate | you | plain and authoritative | Murong Baek gives Jamukha direct orders and rebukes him without honorific speech. |
| 자무카 | 모용백 | subordinate_to_commander_and_savior | you | deferential and honorific | Jamukha thanks Murong and addresses him with honorific speech. |
| 적천강 | 북천마군 | former battlefield adversaries | you; you pup | blunt, familiar, and taunting | Jeok addresses him informally while challenging his alliance with Dark Heaven. |
| 북천마군 | 궁성 | hostile martial opponents | Bow Saint | calm and formally familiar | Addresses her directly while acknowledging her effort. |
| 북천마군 | 자무카 | lord to subordinate | my lord | formal-deferential | Jamukha answers the Demon Lord’s command with 하명하십시오. |
| 북천마군 | 적천강 | former battlefield adversaries | Fire King | calm and familiar | Addresses Jeok Cheongang as 화왕 while asking him not to rush. |
| 궁성 | 모용백 | opponents | Murong Baek; North Heaven Demon Lord | calm, formal, and admonitory | The Bow Saint directly addresses Murong while telling him to accept the consequences of his choices. |
| 진위경 | 테무르 | Alliance Leader addressing a captured opposing chieftain | you | formal and firm | Uses 그대 while offering Temur a choice to surrender. |
| 테무르 | 진위경 | submitting chieftain to his new lord | my lord | deferential and honorific | Temur submits and addresses Jin Wikyung as 주군. |

## Listed compact profiles

### Cheolyeong.md

# Cheolyeong (철영)

- **Safe through:** Chapter 979
- **Aliases:** None
- **Role:** Cheolyeong is the current Family Head of the Peng Family in Hebei.
- **Personality:** Not established.
- **Voice:** Not established
- **Relationships:** He is Peng Cheolhu’s eldest son.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 980
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 981
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jamukha.md

# Jamukha (자무카)

- **Safe through:** Chapter 981
- **Aliases:** None
- **Role:** Jamukha was the ruler of the western steppe and a former eastern-steppe chieftain recruited into Dark Heaven by Murong Baek; Jin Taekyung killed him.
- **Personality:** Patient and ambitious, he was willing to feign loyalty to gain the power to rule the steppe and north.
- **Voice:** Not established
- **Relationships:** Peng Cheolhu defeated him more than fifty years ago; Murong Baek spared and recruited him, but Jamukha’s loyalty to him was feigned.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 980
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, remains Peng Cheolhu's rival, and once fought alongside Murong Baek, now his enemy.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 942
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he follows imperial orders without hesitation and reads the political consequences of events with care.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** Jeong Hogun serves under Baek Yeon’s command in the Embroidered Uniform Guard and honors Jin Taekyung as a comrade-in-arms after their shared battle.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 981
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Supreme Peak swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and guided by a strong sense of chivalry and responsibility; losses deepen his self-reproach and resolve to grow strong enough to protect others.
- **Voice:** Quiet and resonant, clipped and blunt, with dry sarcasm in familiar exchanges.
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, who shares his own grief and encourages him to keep trying; Cheol Mubaek died protecting Mukyung and left him the Shura Annihilating Fist manual; their father—the Jin Family Head—once apologized to Mukyung for his mother’s death in childbirth.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 979
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm and politically capable, Jin Wikyung takes responsibility for his people and prioritizes their lives; he commits firmly to his principles, even when doing so means remaining in a losing battle.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Jin Wikyung is Taekyung’s eldest brother and future Family Head, protects and mentors him, and commands the Jin Family’s forces; Jin Mukyung is his younger brother, and he considers the Jin Family indebted to the Dongting Fisherman and the other fallen defenders of Shanxi.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 942
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Murong Baek.md

# Murong Baek (모용백)

- **Safe through:** Chapter 979
- **Aliases:** North Heaven Demon Lord, Divine Spear of the Imugi
- **Role:** Murong Baek was the North Heaven Demon Lord, known as the Divine Spear of the Imugi; Jin Taekyung killed him after he burned his life to gain power.
- **Personality:** He coveted the dragon pearl and the chance to become a dragon, rationalizing his pursuit while choosing to seize what belonged to others.
- **Voice:** Not established
- **Relationships:** Jeok Cheongang and the Bow Saint fought him alongside Jin Taekyung, who delivered the killing blow.

### Murong Yeonghwi.md

# Murong Yeonghwi (모용영휘)

- **Safe through:** Chapter 546
- **Aliases:** One-Ride Heavenly Dragon
- **Role:** Murong Yeonghwi is a blood relative of the Murong Family, an overwhelmingly powerful young prodigy, and a recently appointed Squad Leader of the Murim Alliance's Outer Hall who remains in Liaoning to oversee his family's defenses.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He is a blood relative of the Murong Family.

### Peng Cheolhu.md

# Peng Cheolhu (벽력도왕)

- **Safe through:** Chapter 981
- **Aliases:** Thunderbolt Saber King
- **Role:** Peng Cheolhu is the Thunderbolt Saber King, a Ten Kings master and Great Hero of the Hebei Peng Family.
- **Personality:** Boisterous, hot-tempered, argumentative, and protective toward those connected to his close friend Hong Dao; relentlessly disciplined in training, having continued every day after the Great Faction War.
- **Voice:** Loud, blunt, confrontational, and prone to disguising embarrassment or retreat as serious martial instruction.
- **Relationships:** Long-standing rival and friend of Jeok Cheongang; close friend of Hong Dao; protective toward Hong Dao's Disciple Unnamed; father of Peng Cheolyeong; longtime friend and former youthful rival of Murong Baek, who has now betrayed and attacked him.

### Peng Cheolyeong.md

# Peng Cheolyeong (팽철영)

- **Safe through:** Chapter 979
- **Aliases:** Iron Blood Saber
- **Role:** Family Head of the Hebei Peng Family; son and successor of the Thunderbolt Saber King.
- **Personality:** Calm and prudent under pressure, prioritizing consultation over risking his family’s lives on a hasty decision.
- **Voice:** He speaks calmly and deliberately, even when explaining grave decisions.
- **Relationships:** Son of the Thunderbolt Saber King; Jeok Cheongang says his past fight was followed by no further contact and that the Peng Family fabricated a later story about their encounter.

### Temur.md

# Temur (테무르)

- **Safe through:** Chapter 981
- **Aliases:** None
- **Role:** Temur is the surviving chieftain of the northern grasslands who submitted to Jin Wikyung and the Jin Family of Taiyuan.
- **Personality:** Hot-tempered and proud of his khan lineage, Temur chose survival over loyalty and now recognizes with guilt that his actions have led his followers to slaughter.
- **Voice:** Blunt, heated, and confrontational
- **Relationships:** The real Chinggen was Temur’s cousin and sworn brother through the anda oath, but was killed; Temur now submits to Jin Wikyung as his lord.

## Korean source

```text
＃982화



나는 이기적인 놈이다.

나와 내 주위 사람들만 행복할 수만 있다면 다른 곳에서 무슨 일이 터지든지 말든지 크게 신경조차 쓰지 않는.

하지만 어느 날부터인가 나 자신이 변화했다는 것을 종종 느끼고는 한다.

이를테면, 스스로를 자책하며 질질 짜는 누군가가 신경 쓰여서 웃기지도 않는 촌극을 벌인 때라든지.

“가끔 조장님을 보면 그런 생각이 듭니다.”

진무경을 뒤로하고 도망치듯 전각을 빠져나온 지 한참.

말없이 걷던 도중 혁무진이 불쑥 꺼내 든 한마디에 내가 대꾸했다.

“생각하지 마. 아니, 그냥 말을 하지 마.”

“왜요?”

“듣기 싫으니까.”

“괜히 부끄러워서 그런 건 아니고요?”

맞다.

계속해서 빤히 날 응시하는 혁무진의 시선을 애써 모른 척하고 있었던 이유도 그래서였으니까.

“그냥…….”

“그냥?”

“왠지 모르게 신경 쓰여서 오지랖 한번 떨어 본 거야. 딱 그 정도인 거지.”

그리고 문 하나를 사이에 두고 진무경에게 해 주었던 말은, 내가 오랜 고민 끝에 찾아낸 결론이기도 했다.

과연 그것이 정답일지는 모르겠지만, 지금 당장 조금이나마 위로가 된다면 그것으로 충분하다.

결국 대부분의 문제는 시간과 경험을 통해 해결된다.

답은 누군가가 알려 주는 것이 아니라, 스스로 찾는 것이니까.

‘녀석에게는 이제 겨우 첫걸음이겠지.’

태원진가가 배출해 낸 희대의 천재이자 이 세상에서만큼은 내 형이지만, 진무경의 나이는 이제 고작 이십 대 중반.

무공만 갈고 닦아 온 만큼 실전 경험은 손에 꼽고, 그로 인한 상실감에도 익숙하지 않은 상태다.

그런 그에게 조금이라도 위안이 될 수 있다면, 낯간지러운 말 몇 마디쯤은 수십 수백 번이라도 해 줄 수 있다.

진무경의 마음과 발끝은, 단 한 치의 흐트러짐도 없이 정도(正道)를 향해 뻗어 있으니까.

녀석이 성장할수록, 조금 더 살 만한 세상이 될 테니까.

‘걸어라. 주저앉지 말고 계속해서 걷고 또 걸어라.’

그 길의 끝에, 답이 있다.

빛이 있다.

나는 그렇게 믿고 있었다.

더할 나위 없이 진심으로.

“그런데 조장님. 한 가지 말씀드려도 됩니까?”

“뭘.”

“이 방향 아닙니다. 이대로 계속 가면 막다른 길이에요.”

잠시 침묵하던 나는 어이없다는 눈빛으로 혁무진을 바라보았다.

“아니……. 그걸 왜 이제 말해, 이 새끼야.”

“그게 좀, 갑자기 눈에 힘주고 멋있는 표정을 짓고 계시길래.”

“…….”

때리고 싶다.

진심으로.



* * *



진무경에게 모두 말하지 못했을 정도로, 지난 사흘 동안 있었던 일들은 무수히 많았다.

물경 수만에 달하는 적과 아군이 뒤얽힌 대전투.

산서인들이 위대한 승리를 거둔 그날로부터 벌써 사흘이라는 시간이 흘렀지만, 그것이 남긴 여파와 후유증은 실로 막심했다.

갑작스럽게 찾아온 불청객들이 어지르고 더럽히고 나면, 뒤처리는 결국 집주인의 몫으로 남는 법.

승리를 거두었던 그날부터 진위경은 몸이 열 개라도 부족할 지경이었고, 전투의 피로를 완전히 회복하기도 전에 사태 수습에 나서야 했다.

물론, 주위에서 그 꼴을 가만히 두고 보지는 않았지만.

“내 지금부터 소가주께 세 가지 선택지를 드리리다. 우선 하나씩 전부 듣고 나서 마음에 드는 것을 고르시오.”

그중에서도 가장 먼저 나선 사람은 약왕당주였다.

얼핏 보면 단순히 고집 센 할아버지처럼 생긴 그는, 침착한 어조와는 어울리지 않는 흉흉한 눈빛으로 자신의 손에 들린 대침과 진위경을 번갈아 바라보며 이렇게 말했다.

“그렇게 계속 말 안 듣고 일만 하다가 골병들어서 죽든가, 지금이라도 치료받고 쉬엄쉬엄하면서 오래 살든가. 그것도 아니면 길게 갈 것 없이 내 손에 뒈지든가. 무엇으로 하시겠소?”

진위경은 그제야 제대로 된 휴식을 취하기 시작했고, 그 광경을 지켜본 사람들은 뒤에서 치열한 갑론을박을 펼쳤다.

그날 진위경의 얼굴이 시체처럼 창백했던 이유가 피로 때문이냐, 아니면 약왕당주의 대침 때문이냐로.

그리고 혁무진은 딱 잘라 이렇게 말했다.

“무조건 대침 때문입니다. 그때 그 노인네 눈 못 보셨어요? 의술을 안 익혔으면 지금쯤 암천에서 한자리 꿰차고 있었을 겁니다.”

여하간 중요한 사실은 진위경이 고집을 꺾었다는 것이었고, 그가 그런 선택을 할 수 있었던 배경에는 또 다른 이들의 도움이 크게 작용했다.

“약왕당주인지 뭔지 하는 저 돌팔이 말이 백번 옳다. 네 녀석은 몸이나 추스르고 있거라. 남은 일은 다른 놈들이 알아서 처리할 것인즉.”

중양절의 전투는 승리로 끝났지만, 아직 모든 위협이 사라졌는지는 확신할 수 없는 상황.

그러나 화왕(火王) 적천강이라는 거인의 존재감은 일말의 걱정마저 씻은 듯이 사라지게 만들기에 충분했다.

장장 수십여 년의 세월을 뛰어넘어, 비로소 사람들의 앞에 모습을 드러낸 궁성(弓星)의 존재 역시도.

“하북(河北)에 다녀오마.”

전투가 끝나자마자 짧은 한마디를 남긴 궁성은 곧장 떠났다.

벽력도왕의 아들이자 하북팽가의 현 가주, 철혈도(鐵血刀) 팽철영도 거동이 가능한 가솔들을 이끌고 그녀와 함께 하북으로 귀환할 수밖에 없었다.

당연한 일이었다.

북천마군, 아니 모용백의 배신은 그 한 사람만의 것이 아니었기에.

이는 곧 모용세가 전체가 암천에 가담하고 있었음을 뜻했고, 그로부터 이틀 뒤 태원진가로 도착한 전서응에 적힌 소식은 그 예측의 일부가 사실이었다는 것을 증명해 주었다.

“앞서 예상했다시피, 하북에서 변고가 있었다.”

비록 여러 사람의 강권에 못 이겨 휴식을 취하고는 있지만, 진위경의 손에서 서류를 빼앗는다는 것은 불가능에 가깝다.

전서응이 태원진가에 도착한 동시에 소식을 접한 진위경은 그 즉시 나를 불러 하북에서 있었던 일을 알려 주었다.

“모용세가는 처음부터 산서와 하북 두 곳을 동시에 노린 모양이다. 우리를 지원하겠다는 명분으로 하북을 가로지르는 한편, 일부 병력을 남겨 팽가를 기습했다는구나.”

중양절에 휘몰아쳤던 피바람은 산서성에만 국한된 것이 아니었다.

도무지 예측할 수 없었던 모용세가의 갑작스러운 배신에 벽력도왕을 비롯한 주력 고수 상당수가 빠져나가 있던 하북팽가는 큰 피해를 입었고, 목숨을 걸고 결사항전한 끝에 간신히 본가를 지켜 낼 수 있었다고 했다.

“하나 그것도 시간문제였을 것이다. 모든 것이 이틀만 늦어졌더라면, 더는 돌이킬 수 없는 일이 벌어졌겠지.”

하지만 풍전등화의 위기 속에서, 마침내 가주인 팽철영이 나타났다.

노호성과 함께 나타난 그의 뒤에는 가주를 따라 산서성에서 귀환한 가솔 오백여 명과, 하북팽가의 가신 격이라 할 수 있는 진주언가(晋州彦家)의 무인 수백이 있었다.

아마도 그뿐이었다면 하북팽가의 입장에서는 힘겨운 전투가 될 수도 있었을 것이다.

갑작스러운 기습을 당한 하북팽가는 이미 극심한 피해를 입은 상황이었고, 팽철영이 거느린 병력은 지치고 급조된 병력 일천이 전부였으니까.

그러나 그런 그들의 선두에는, 하북팽가의 가주인 팽철영조차 감히 앞에 설 수 없는 거인이 있었다.

“궁성 선배께서 결심하신 이상, 결과는 이미 정해져 있었다고 해도 무방하겠지.”

우리에게는 또 한 번의 승리였고, 모용세가로서는 끔찍한 패배였다.

재기불능(再起不能)이라는 표현이 정확히 들어맞을 정도의 패배.

그렇게 모용세가는 궤멸했다.

소가주인 모용영휘를 비롯한 수십여 명의 적들은 간신히 전장을 빠져나가 자취를 감추었지만, 글쎄.

“어딘가에 숨겨 둔 이동진(移動眞)이 아니라면 금세 붙잡힐 것이다. 온 사방에 우리의 이목이 있으니.”

진위경의 장담은 결코 허언이 아니었다.

머지않아 암천이 드리운 먹구름이 모두의 머리 위를 뒤덮더라도, 아직 천하의 주인은 정파 무림이니까.

모용세가는 천하를 적으로 돌렸다.

태원진가와 하북팽가를 정면으로 돌파하지 않는 이상 드넓은 중원으로 도망칠 수 없고, 동쪽의 대해(大海)에는 대국의 군함이 버티고 있다.

그리고 놈들의 뿌리이자 무법자들의 종착역이나 다름없는 대초원은, 이미 태원진가의 영역이나 다름없었다.

“부족민들을 풀어 놈들을 쫓게. 세상 끝까지라도.”

그것은 부탁이 아니었다.

산서성의 맹주이자 위대한 승리자이며, 패배한 사냥개를 굴복시킨 주인으로서 진위경이 내리는 첫 번째 명령이었다.

“자네로서도 후환(後患)을 남겨서는 안 되겠지. 그렇지 않나, 테무르.”

“명을…… 받들겠습니다.”

한때 광활한 초원을 아우르는 대칸을 꿈꾸었던 젊은 부족장은 힘없이 복종했다.

당연한 일이었다.

그는 전투에서 진 패장이고, 죽음이 두려워 형제와 부족민을 배신한 비겁자였으니까.

전자에 대해서는 자무카와 북천마군의 흉계에 휘말렸다는 명분과 태원진가에 굴복함으로써 더 큰 희생을 막았다는 거짓 면죄부를 쥐여 주었지만, 후자는 달랐다.

모든 진실이 밝혀진다면 테무르는 죽는다.

우리도, 암천도 아닌 자신의 부족민들에게.

그것이 진위경이 틀어쥔 목줄이었고, 사냥개는 감히 배신할 생각조차 할 수 없었다.

진위경의 제안을 받아들여 모용세가에 합공을 가한 그 순간부터, 그 외의 모든 선택지는 사라진 것이나 다름없었으니.

‘역겹지만, 목줄을 틀어쥔 이상 아군에게는 반드시 필요한 놈이다.’

테무르의 그 알량한 비겁함과 생존 본능 탓에 희생된 목숨이 몇 명인가.

“가라. 보고 있으면 열 받으니까.”

내 경멸 섞인 어조에 고개를 떨군 테무르는 그렇게 떠났고, 나는 남아 있는 문제를 완전히 처리해 줄 해결사를 불렀다.

“불렀나?”

어디서나 모두의 시선을 빼앗을 만큼 휘황한 황금빛 갑옷.

옆구리에 낀 투구만큼이나 딱딱하기 그지없는 표정과 말투를 지닌 그.

금의위의 천호(千戶) 정호군을 향해 나는 짐짓 눈살을 찌푸렸다.

“뭐야, 왜 이렇게 멀쩡해?”

“그만큼 잘 싸웠다는 증거지.”

“마지막에 와서 숟가락만 얹은 건 아니고?”

“그것이 수천 리 길을 마다하고 도우러 온 은인에게 할 말인가?”

“마, 그 전에 내가 도운 것도 생각해야지. 그때 황궁에서 나 아니었으면 어쩔 뻔했어?”

“어쩌긴, 궁성께서 도우셨겠지.”

“……어라, 생각해 보니 그러네.”

“……그걸 그대로 인정할 줄은 몰랐군.”

잠시 내려앉은 침묵 속, 나와 정호군은 약속이라도 한 것처럼 서로를 향해 실소를 터트렸다.

이래저래 괜한 장난을 치긴 했지만 고마운 놈이다.

녀석이 내게 감사한 마음을 갖고 있듯이, 나 역시 마찬가지였다.

“부탁할 게 있어서 불렀어.”

“부탁?”

“그래. 어쩌면 조금, 아니 상당히 어려운 부탁이 될 수도 있겠지.”

“누군가 죽을 수도 있다는 이야기로군.”

내가 조용히 고개를 끄덕이자, 정호군이 생각할 것도 없다는 듯이 입을 열었다.

“그렇다면 거절한다.”

“아.”

칼날 같은 어조.

예상치 못한 단호한 거절에 내가 침음성을 삼킨 그때, 정호군이 나직한 목소리로 말을 이었다.

“명령.”

“뭐?”

“사사로운 부탁은 들어줄 수 없다. 하지만 명령이라면 다르지.”

그제야 정호군의 의도를 깨달은 내가 실소를 흘렸다.

“굳이 이렇게까지 해야 하는 이유가 뭐지?”

“그것이 대국의, 군문의 법도(法度)니까.”

재미있는 녀석이다.

한편으로는 문득 그런 생각도 들었다.

정호군 같은 이가 있기에, 대국이라는 나라가 존재할 수 있다는 생각이.

그리고 그가 원하는 대로, 나는 입을 열었다.

“금의위 천호 정호군.”

언제 그랬냐는 듯, 정호군이 공손한 눈빛으로 고개를 숙였다.

“명하십시오.”

“휘하의 금의위를 이끌고, 요녕(遼寧)으로 향하라.”

요녕성.

모용세가의 본거지이자, 마지막 후환.

내 명령에, 정호군이 갑옷을 두드렸다.

“상산후(上山侯)의 명을 받드나이다.”
```

## Final English reading copy

```markdown
# Chapter 982

I’m a selfish bastard.

As long as I and the people around me can be happy, I hardly care what happens anywhere else.

But every now and then, I feel like I’ve changed somewhere along the way.

Like the time I got so concerned about someone beating himself up and crying that I put on a ridiculous little show.

“Sometimes, when I look at you, Captain, I get this feeling.”

It had been a while since I’d left the pavilion, practically running away from Jin Mukyung.

As we walked in silence, Hyuk Mujin suddenly spoke up. I answered him.

“Don’t think about it. No—just don’t say it.”

“Why not?”

“Because I don’t want to hear it.”

“It’s not because you’re embarrassed, is it?”

He was right.

That was why I’d been doing my best to ignore Hyuk Mujin’s gaze as he stared at me.

“It’s just…”

“Just what?”

“I somehow felt concerned, so I stuck my nose in where it didn’t belong. That’s all.”

And the words I’d said to Jin Mukyung through the door had been the conclusion I’d reached after a long time thinking about it.

I didn’t know if it was the right answer, but if it could comfort him even a little right now, that was enough.

In the end, most problems were solved through time and experience.

The answer wasn’t something someone else could give you. You had to find it yourself.

*This is only the first step for him.*

He was an unparalleled genius born of the Jin Family of Taiyuan, and in this world, at least, he was my older brother. But Jin Mukyung was only in his mid-twenties.

He’d spent all his time honing his martial arts, so his real combat experience could be counted on one hand. He still wasn’t used to the grief that came with it.

If I could bring him even a little comfort, I’d say a few embarrassing words like that tens or hundreds of times over.

Jin Mukyung’s heart and the direction of his steps were set toward the righteous path, without a hair’s breadth of deviation.

The more he grew, the more livable the world would become.

*Keep walking. Don’t sit down. Just keep walking, and walking, and walking.*

At the end of that road was an answer.

There was light.

I believed that.

With all my heart.

“But, Captain. Can I tell you something?”

“What?”

“This isn’t the right way. If we keep going, it’s a dead end.”

I fell silent for a moment, then looked at Hyuk Mujin in disbelief.

“Wait… Why are you only telling me now, you bastard?”

“Well, you suddenly got this intense look in your eyes and started making a cool face.”

“…”

I wanted to hit him.

I really did.

* * *

There had been far too much going on over the past three days for me to tell Jin Mukyung everything.

A great battle, with tens of thousands of enemies and allies tangled together.

Three days had already passed since the day the people of Shanxi won a great victory, but the fallout and aftereffects were severe.

When unexpected guests show up and make a mess of the place, cleaning up is ultimately the homeowner’s job.

From the very day we won, Jin Wikyung had more work than ten people could handle. Before he’d even recovered from the exhaustion of battle, he had to start dealing with the aftermath.

Of course, those around him didn’t just stand by and watch.

“From this moment on, I’ll give the Lesser Family Head three options. Listen to all of them, one by one, and then choose the one you like.”

The first to step forward was the Medicine King Hall Master.

At a glance, he looked like a stubborn old man. But with a menacing gleam in his eyes that didn’t match his calm tone, he glanced back and forth between the long needle in his hand and Jin Wikyung, then said:

“You can keep ignoring my orders and working until you ruin your health and die. Or you can get treated now, take it easy, and live a long life. Or, if you’d rather not drag it out, you can die by my hand. Which will it be?”

Only then did Jin Wikyung start taking proper time to rest. The people who saw it debated fiercely behind his back.

Was his face as pale as a corpse that day because he was exhausted—or because of the Medicine King Hall Master’s long needle?

Hyuk Mujin put it plainly.

“It was definitely the needle. Didn’t you see that old man’s eyes? If he hadn’t learned medicine, he’d probably have carved out a place for himself in Dark Heaven by now.”

In any case, what mattered was that Jin Wikyung had finally relented. And the help of others had played a large part in making that choice possible.

“That quack they call the Medicine King Hall Master is absolutely right. You focus on recovering. The others will take care of the rest.”

The battle on the Double Ninth Festival had ended in victory, but we still couldn’t be sure that every threat had disappeared.

Still, the very presence of a giant like the Fire King, Jeok Cheongang, was enough to wipe away even the slightest worry.

And so was the return of the Bow Saint, who had finally appeared before the world again after vanishing for decades.

“I’ll go to Hebei.”

The Bow Saint left immediately after the battle, leaving only that brief remark behind.

The Thunderbolt Saber King’s son, Peng Cheolyeong—the current Family Head of the Hebei Peng Family and the Iron Blood Saber—had no choice but to return to Hebei with her, leading the family members who were able to travel.

It was only natural.

The North Heaven Demon Lord—no, Murong Baek—hadn’t been the only one to betray us.

It meant the entire Murong Family had joined Dark Heaven. Two days later, the news carried by a messenger eagle to the Jin Family of Taiyuan proved that at least part of our prediction had been right.

“As we expected, trouble broke out in Hebei.”

Even though he’d been forced to rest by several people, taking documents out of Jin Wikyung’s hands was nearly impossible.

The instant the messenger eagle arrived at the Jin Family of Taiyuan, Jin Wikyung received the news. He immediately called me in and told me what had happened in Hebei.

“Looks like the Murong Family had been targeting both Shanxi and Hebei from the start. Under the pretense of coming to support us, they crossed Hebei while leaving part of their forces behind to launch a surprise attack on the Peng Family.”

The bloodshed that had swept through the region on the Double Ninth Festival hadn’t been confined to Shanxi Province.

Caught off guard by the Murong Family’s sudden betrayal, the Hebei Peng Family had suffered heavy losses. With the Thunderbolt Saber King and many of their strongest masters away, they’d barely managed to defend their family home after fighting to the death.

“But even that would only have bought them time. If everything had been delayed by two days, something irreversible would have happened.”

But just as the family stood on the brink of ruin, Peng Cheolyeong, its Family Head, finally arrived.

Behind him, accompanying the roar with which he announced his arrival, were more than five hundred family members who’d returned from Shanxi with him, along with several hundred martial artists from the Jinzhou Yan Family, a vassal family of the Hebei Pengs.

If that had been all, the battle would have been a hard one for the Hebei Peng Family.

They’d already suffered devastating losses in the surprise attack, and Peng Cheolyeong had only a thousand exhausted, hastily assembled troops at his command.

But leading them was a giant whom even Peng Cheolyeong, Family Head of the Hebei Peng Family, would not dare step ahead of.

“Once Senior Bow Saint made up her mind, the outcome was already decided.”

It was another victory for us—and a terrible defeat for the Murong Family.

A defeat that deserved to be called unrecoverable.

And so the Murong Family was annihilated.

Several dozen enemies, including its Lesser Family Head, Murong Yeonghwi, barely escaped the battlefield and vanished. But who knew?

“Unless they have a Moving Formation hidden somewhere, they’ll be caught soon enough. Our eyes are everywhere.”

Jin Wikyung’s confidence wasn’t an empty boast.

Even if the dark clouds cast by Dark Heaven eventually covered everyone’s heads, for now, the orthodox Murim factions still ruled the land.

The Murong Family had made an enemy of the world.

Unless they could break through the Jin Family of Taiyuan and the Hebei Peng Family, there was no way to escape into the vast Central Plains. To the east, the Great Nation’s warships guarded the open sea.

And the Great Steppe—their roots and little more than the final destination for outlaws—was already practically under the Jin Family of Taiyuan’s control.

“Release the tribespeople to hunt them down. Even if it takes them to the ends of the earth.”

It wasn’t a request.

As Shanxi’s Alliance Leader, the great victor, and the master who had broken a defeated hunting dog to heel, Jin Wikyung gave his first order.

“You wouldn’t want to leave trouble for the future, either. Would you, Temur?”

“I… will obey.”

The young chieftain who had once dreamed of uniting the vast steppe as its Great Khan submitted helplessly.

It was only natural.

He was a defeated commander who had betrayed his brothers and his tribespeople because he feared death.

As for the former, he’d been given a pretext—that he’d fallen into Jamukha and the North Heaven Demon Lord’s schemes—and the false absolution that submitting to the Jin Family of Taiyuan had prevented even greater losses. But the latter was different.

If the whole truth came out, Temur would die.

Not at our hands, or Dark Heaven’s—but at the hands of his own tribespeople.

That was the leash Jin Wikyung held tight. The hunting dog couldn’t even think of betraying him.

From the moment Temur accepted Jin Wikyung’s offer and joined the attack on the Murong Family, all his other options had effectively disappeared.

*It’s disgusting, but now that we’ve got a leash on him, we need him on our side.*

How many lives had Temur’s petty cowardice and instinct for survival cost?

“Go. You’re pissing me off just standing there.”

Temur lowered his head at my contemptuous words and left. Then I called over the man who could take care of the remaining problem for good.

“You called?”

His brilliant golden armor drew everyone’s eyes wherever he went.

His expression and speech were as stiff as the helmet tucked under his arm.

I looked at Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard, and deliberately frowned.

“What’s with you? Why do you look so fine?”

“Because I fought well.”

“Or did you just show up at the end and take all the credit?”

“Is that what you say to a Benefactor who traveled thousands of li to help you?”

“Hey, you’ve got to remember that I helped you first. What would you have done if I hadn’t been there at the Imperial Palace?”

“What would I have done? The Bow Saint would have helped.”

“…Huh. Now that I think about it, you’re right.”

“…I didn’t expect you to admit it just like that.”

A brief silence settled between us. Then, as if on cue, Jeong Hogun and I both chuckled.

I’d been teasing him for no reason, but I was grateful to the guy.

Just as he was grateful to me, I felt the same way about him.

“I called you because I have a favor to ask.”

“A favor?”

“Yeah. It might be a little—or rather, a pretty difficult favor.”

“Someone might die.”

I quietly nodded. Jeong Hogun answered without a moment’s hesitation.

“Then I refuse.”

“Ah.”

His tone was as sharp as a blade.

I swallowed a groan at his unexpected, unequivocal refusal. Then Jeong Hogun continued in a low voice.

“An order.”

“What?”

“I can’t grant a personal favor. But an order is different.”

Only then did I understand what Jeong Hogun meant, and I gave a short laugh.

“Why go this far?”

“That is the law of the Great Nation’s military.”

He was an interesting guy.

And for a moment, I thought that it was people like Jeong Hogun who made a nation like the Great Nation possible.

Then, as he wished, I spoke.

“Jeong Hogun, Thousand Captain of the Embroidered Uniform Guard.”

Jeong Hogun bowed his head with a respectful expression, as if nothing had happened.

“Give your order.”

“Lead the Embroidered Uniform Guard under your command to Liaoning.”

Liaoning Province.

The Murong Family’s stronghold—and the last trouble waiting to be dealt with.

At my order, Jeong Hogun struck his armor.

“I receive the command of the Marquis of Shangshan.”
```
