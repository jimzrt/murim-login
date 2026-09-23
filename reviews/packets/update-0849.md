<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0849.txt",
      "sha256": "f440d6fbb96c726a647b75eccbdbd68a6fe63268d585fdb0609fd8efcd870243",
      "bytes": 14325
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a69bf7286bc0aa968fd3d860a07c35bf165d4c9da1baf49dc6f38471f6e782f5",
      "bytes": 697
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4457e8b40f7f008b9e72cc675f97dd2a5d576cdb2837cd3b5a882f70cd6820b7",
      "bytes": 227587
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "b2ca5b5978c5d8d6d19e0049891dc708e897771a3f522ba15a64247b5786d9d5",
      "bytes": 759
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "177c5d1e95b6d715fbf2f3e7382f7b549502fff2134a17a1ded8106257300594",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8c5287ceb3af7548d091492c081805b72bc65dc4afdfc1a33d0d64608e1fe4ec",
      "bytes": 1573
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1198a6e5ef2074f3cb63ec0538902ec42b867d324c6e218fbc559e7c7cd468e7",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "346bb1d1b3699e3ebff93991fc3d095125535fb5fd204ca1d125a845300d8059",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "540d9045fe007e1524abb952de309aab198860a670b42ed0899d2e1a7c168054",
      "bytes": 973
    },
    {
      "path": "characters/Ju Wongong.md",
      "sha256": "1a787c0c7ad2616e5fde9e7db2c20f2e0cbda63932cfe12e312e0766d8ad448a",
      "bytes": 801
    },
    {
      "path": "characters/Namho.md",
      "sha256": "248cbe8956a01ecc00312b475b2e95645ed9588468967b16feec14ad2c94a008",
      "bytes": 936
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "ae5c73259e47a7d16e113319b7e47644fda5c5b42dc03097d80e50604f59a037",
      "bytes": 914
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "e0fa895a87ee8a2c353cd660942ee21f687b024bbcafbb46bee60d2cf3a759e0",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "d3ce55159249afb435bec30de1a1966e5558c7122f60bd6b612df40b84d1eedd",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "a61e16e82aaacbb595ec46d0352527b61b0fce7bf7228dc64ff5156846d56d69",
      "bytes": 787
    },
    {
      "path": "characters/Won Gyun.md",
      "sha256": "64d8e91bda706b41725c175a5ab74cc21beb63b825d65b9cc630af98673ba549",
      "bytes": 683
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ef87894d7e6e58370eefc26a6e542406cf849311afb057ed00381198bbe91265",
      "bytes": 252436
    }
  ],
  "estimated_tokens": 14955
}
-->

# Durable State Update — Chapter 849

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
1 and safe_through 849. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 849. Profile updates may replace only one
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
  "chapter": 849,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 849,
    "continuity_sources": [849],
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
    "Jin Taekyung remains incompletely recovered; Jeok Cheongang’s treatment improved his condition, but pain persists in his lower dantian.",
    "The City Lord of Sichuan Province is dead. The Divine Physician found gu poison in his body and doubts the local physician’s sudden-death conclusion."
  ],
  "continuity_sources": [
    847,
    848
  ],
  "open_questions": [
    "What caused the City Lord’s death, and who placed the gu poison in his body?",
    "Will Jin’s lower-dantian injury improve further, or remain beyond full recovery?"
  ],
  "safe_through": 848,
  "temporary_decisions": [
    "Render 고독 as “gu poison.”"
  ],
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
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 낭인     | **wandering martial artist**                     |                                                       |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 산서     | **Shanxi**             |
| 사천     | **Sichuan**            |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 주원공 | **Ju Wongong** | Qingxia Hall leader who claims distant kinship with the Emperor. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 원균 | **Won Gyun** | Personal name of the City Lord of Sichuan Province. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 트롤 | **Troll** | Monster species with extraordinary regenerative ability. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 은영각 | **Hidden Shadow Pavilion** | Former Murim Alliance intelligence organization. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 도련님 | **Young Master** | Address used for Team Leader Choi by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 사천성 | **Sichuan Province** | Province form used in the title of its chief official. |
| 사천성주 | **City Lord of Sichuan Province** | Title held by Won Gyun. |
| 호위장 | **Captain of the Guards** | The Sichuan City Lord's guard captain. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 야명주 | **night-shining pearls** | Pearls embedded in the cavern ceiling that provide light. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 사천혈사 | **Sichuan Blood Tragedy** | Earlier incident in which Taekyung witnessed the strange formation. |
| 마법 | **Magic** | Taekyung's explanation for Dark Heaven's anomalous abilities. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 비도 | **throwing blade** | Mungyeong throws one past Taekyung's neck. |
| 황하 | **Yellow River** | River along which civilization began. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |

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
| 사천성주 | 진태경 | official_to_imperial_messenger | Messenger of His Highness Prince Shangshan | formal-deferential | The City Lord addresses Taekyung deferentially after seeing Prince Shangshan's Token. |
| 진태경 | 사천성주 | visitor_to_city_lord | City Lord | sarcastic-polite | Taekyung jokingly praises him as our City Lord after making him fund the reward. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 사천성주 | 호위장 | provincial_city_lord_to_guard_captain | Captain of the Guards | imperious and dismissive | The City Lord directly orders the Captain of the Guards to handle the troops stationed near Chengdu. |
| 진태경 | 주원공 | opponent to exiled imperial relative | you | casual and mocking | Uses 네놈 and the 주인공/주원공 wordplay while ordering Ju Wongong down. |
| 주원공 | 진태경 | Qingxia Hall young master to Great Hero | Great Hero Jin | imperious, then deferential | Initially uses 네놈 and 역적놈아 while asserting imperial authority, then switches to 진 대협 and respectful forms after seeing Prince Shangshan's token. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 태산 | 적천강 | subordinate of a Young Sect Leader to legendary elder | Fire King | clipped, childlike, and deferential | Taishan gives his awkward greeting and expresses admiration for Jeok's strength. |
| 적천강 | 태산 | legendary elder to giant subordinate | you / strange fellow | blunt, startled, and grudgingly tolerant | Jeok addresses Taishan as 네놈 while reacting to his greeting and appetite. |
| 진태경 | 송일섬 | pavilion master to prospective member | Song Ilseom | direct and evaluative | Taekyung directly names Song Ilseom while comparing his qualifications with Hwaran's. |
| 혁무진 | 송일섬 | pavilion_member_to_escort_captain | Great Hero Song | formal and deferential | Mujin addresses Song Ilseom while commenting on his broad experience. |
| 혁무진 | 태산 | pavilion_member_to_pavilion_member | you / hey | casual and coaxing | Hyuk Mujin calls after Taishan and offers jerky to persuade him to travel together. |
| 태산 | 혁무진 | pavilion_member_to_pavilion_member | you | clipped and dismissive | Taishan tells Hyuk Mujin not to follow, then accepts him as a friend after hearing about the jerky. |
| 남호 | 진태경 | Hidden_Shadow_Pavilion_agent_to_mission_leader | Jin Taekyung / you | guarded and familiar | Namho addresses Taekyung as 자네 while explaining the contact and offering guidance. |
| 진태경 | 남호 | mission_leader_to_hidden_shadow_agent | you / Namho | probing and respectful | Taekyung questions Namho’s affiliation and later discusses Dark Heaven’s threat to Nanman. |
| 남호 | 혁무진 | hidden_shadow_agent_to_pavilion_member | you there / Han bastard | performatively hostile and abusive | Namho attacks Mujin and insults him to make the meeting appear to be a genuine expulsion. |
| 혁무진 | 남호 | pavilion_member_to_hidden_shadow_agent | old man | indignant and insulting | Mujin protests Namho’s staged attack and objects to the insult about his parents. |
| 주화란 | 남호 | pavilion_member_to_hidden_shadow_agent | you / Elder Namho | formal and appreciative | Hwaran respectfully praises the effort Namho invested in mapping Nanman. |
| 남호 | 태산 | guide_to_pavilion_member | Taishan | blunt and exasperated | Namho directly rebukes Taishan for eating the poisonous blood-feeding fungus. |
| 남호 | 주화란 | guide_to_escort_bureau_head | Escort King's granddaughter | approving and familiar | Namho praises Hwaran for recalling Ju Gongsan's records about Nanman. |
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 태산 | 남호 | Fire Dragon Pavilion member to guide | Namho | clipped, childlike, and informal | Taishan directly addresses Namho while asking what Dark Heaven is. |
| 남호 | 각주 | guide to pavilion master | Pavilion Master | blunt, hostile, and abusive | Namho addresses Jin as 각주 while accusing him of causing the disturbance. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 적천강 | 호위장 | martial artist to official subordinate | you; bastard | blunt and threatening | Jeok uses familiar, insulting address while interrogating the Captain of the Guards. |
| 호위장 | 적천강 | official subordinate to senior martial artist | Sir | deferential | The Captain shifts to respectful speech after sensing Jeok’s status and danger. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 848
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 848
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 848
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; they trust each other deeply but have never formalized their bond. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to the late Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and is a long-standing rival of Peng Cheolhu.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 848
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 848
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 842
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Ju Wongong.md

# Ju Wongong (주원공)

- **Safe through:** Chapter 839
- **Aliases:** Qingxia Hall young master
- **Role:** Ju Wongong is an exiled Qingxia Hall young master and distant imperial relative who, while still under punishment, has been temporarily appointed acting City Lord of Sichuan Province by imperial order.
- **Personality:** Entitled, status-conscious, theatrical, and amused by violence until his own protection is overcome.
- **Voice:** Pompous and imperious, with formal declarations of rank and authority.
- **Relationships:** His Qingxia Hall entourage and four Peak guards obey him; he asserts kinship with the Emperor, and Jin Taekyung is the benefactor who saved his life and can leverage Wongong’s temporary office.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 842
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 838
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor's only younger full brother, and his token commands immediate deference from distant imperial relatives such as Ju Wongong; he admires Jin Taekyung and seeks to emulate him.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 842
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 842
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 848
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

### Won Gyun.md

# Won Gyun (원균)

- **Safe through:** Chapter 350
- **Aliases:** None
- **Role:** City Lord of Sichuan Province who commands the region's government forces and local officials.
- **Personality:** Corrupt, vain, cowardly, and self-important, but quick to submit when confronted with imperial authority or personal incentives.
- **Voice:** Blustering and pompous in public, then deferential and eager to please when threatened or rewarded.
- **Relationships:** He cooperates with Jin Taekyung after Taekyung invokes Prince Shangshan's authority and mobilizes Sichuan's resources to search for the Divine Physician.

## Korean source

```text
＃849화



한 시진.

우리가 사천성주의 거처인 동시에 관청인 성주부(星州府)에 도착하기까지 걸린 시간이었다.

두두두두!

주원공에게 마차를 빼앗, 아니 빌린 것이 신의 한 수였다.

척 보기에도 호화스럽기 그지없는 육두마차에는, 끔찍한 교통 체증을 사라지게 만드는 마법이 깃들어 있었으니까.

“정지! 정지! 당장 멈추시오!”

“신분과 용무를 밝히…… 잠깐, 이 마차 어디서 많이 봤는데.”

사람들로 바글바글한 대로변을 순식간에 아우토반으로 만들어 버렸으니, 멀리서도 눈에 띄는 것은 당연지사.

미친 듯이 질주해 오는 마차를 확인한 관병들은 눈을 동그랗게 떴으나, 이내 어디선가 터져 나온 고함은 잠깐의 시간마저도 허락하지 않았다.

“열어!”

“예, 예?”

“문 열라고, 이 등신들아!”

“아, 알겠습니다! 개문(開門)!”

구그그그긍!

앞서 무슨 지시라도 있었던 것일까.

마차가 멈추는 일도, 마땅히 거쳐야 할 확인 절차도 없었다.

빠르게 가까워지는 마차의 속도에 맞춰 거대한 철문이 열렸고, 마부석에 앉은 혁무진이 말고삐를 늦춘 것은 자그마치 다섯 개의 관문을 통과한 후의 일이었다.

푸륵. 푸르륵.

쉴 새 없이 전속력으로 달려온 여섯 마리의 준마가 거칠게 투레질을 하던 그때.

막 마차에서 내린 나와 화룡각 대원들을 향해 낯선 얼굴들이 다가왔다.

“열화신룡(烈火神龍) 진태경 소협?”

조금의 시간 낭비도 할 수 없다는 듯이, 대뜸 건네 온 물음.

그러나 그 속에는 일반적인 관인(官人)들과는 미묘한 차이가 존재했다.

설령 문관이 아닌 무관이라 할지라도, 관아에 속한 이들이라면 지금처럼 무림에서의 별호를 직접적으로 언급하는 것을 기피하기 마련이니까.

‘무림인?’

내가 다른 이들에 비해 비교적 가벼운 무장을 한 선두의 사내를 물끄러미 바라보던 그때.

송일섬의 전음이 귓가로 전해졌다.

― 아는 얼굴이다. 저자는 날 못 알아보겠지만.

― 아는 얼굴? 누구?

― 낭인으로서는 제법 유명했지. 나중에 은퇴했다고 들었는데…… 완전히 무림을 떠나 관에 투신한 줄은 몰랐군.

― 그래?

― 그렇다. 내 기억력은 정확해.

― 그런데 왜 또 은근슬쩍 반말하냐. 너 나보다 나이 많아?

― 내가 훨씬 더 많은 것으로 아는데.

어, 맞네.

잠시 깜빡했다. 현대 나이로 쳐도 송일섬이 나보다 몇 살은 연상이라는 사실을.

하지만 이대로 넘어가면 화룡각의 기강이 무너진다. 나는 각주의 위엄을 실어 전음을 날렸다.

― 나이 많은데 어쩌라고. 혁무진 꼴 나고 싶냐?

― …….

― 꼬우면 니가 각주 하든가.

짜게 식은 눈빛으로 나를 바라보던 송일섬이 한숨과 함께 고개를 내저었다.

그때, 낭인 출신이라는 선두의 사내가 재차 입을 열었다. 이번에는 나를 똑바로 응시하면서.

“진태경 소협, 아니십니까?”

“맞는데요.”

“앞서 오신 분들께 미리 언질을 들었습니다. 우선 이리로.”

뒤이어 사천성주의 호위장이라는 짤막한 자기소개를 덧붙인 그는 우리를 성주부 깊숙한 곳으로 이끌었다.

“일련의 사정은 이미 들으셨으리라 짐작됩니다만.”

호위장을 따라 걷던 나는 고개를 끄덕였다.

“어느 정도는요.”

“많이 당황하셨겠군요.”

“처음에는 조금 그랬죠. 제가 아는 사람인 줄 알고.”

“아, 혹시 임시 성주님을 말씀하시는 겁니까?”

“네.”

현재 이 땅의 성주는 두 명이다.

아니, 두 명이었다.

나와는 이전부터 나름대로 인연이 있는 방계 황족인 주원공.

그리고 몇 달 전부터 앓아누웠다는 기존의 사천성주.

‘이번에 죽은 그 양반 이름이 뭐였더라. 원균?’

육지에서라면 몰라도 바다에서는 개 트롤짓할 것 같은 이름이라 엑스트라치고는 선명하게 기억하고 있다. 어쩌면 출산 임박을 넘어 임신 20개월쯤 되어 보였던 그 엄청난 뱃살 때문인지도 모른다.

“기억하실지 모르겠지만, 일전에 한번 가까이에서 뵌 적이 있습니다.”

“저를요?”

“사천혈사(四川血史)가 일어나기 직전이었지요. 상산왕 전하의 증표와 함께 지원을 청하러 성주님을 찾아오시지 않으셨습니까.”

“아. 맞아요. 그럼 그때도?”

“예. 명색이 호위장이니, 성주님 곁을 지키고 있었습니다. 그때만 해도 이런 일이 일어날 줄은 몰랐지만요.”

씁쓸한 얼굴로 대답한 호위장은 계속해서 걸음을 옮겼다.

성주의 거처인 동시에 업무를 보는 관청인 성주부답게, 잘 갖춘 관복을 걸친 이들이 어딜 가나 눈에 띄었다.

“생각했던 것보다는 분위기가 그리 삼엄하진 않네요. 이미 한바탕 난리가 났을 줄 알았는데.”

등 뒤에서 따라오던 주화란의 중얼거림에, 호위장이 고개를 끄덕였다.

“그럴 수밖에 없습니다. 성주부에서 근무하는 이들이라면, 성주님의 병환을 일부나마 파악하고 있었으니까요.”

경내의 분위기가 이만큼 안정되어 있다는 건, 그만큼 성주의 죽음이 갑작스러운 일이 아니라는 증거.

하지만 나는 지금 이 상황을 곧이곧대로 받아들이지 않았다.

그 정도로 자연스럽고 평범한 사안이라면, 굳이 적천강과 신의가 움직일 이유도 없었을 테니까.

게다가…….

‘일부나마 파악하고 있었다는 건, 아직 외부에까지 알려지지 않은 무언가가 있다는 뜻.’

골똘히 생각에 잠긴 채 얼마나 이동했을까.

걸음이 이어질수록 인적은 드물어졌고 그 흔했던 관병조차 사라졌다.

그리고 마침내 발걸음을 멈춘 호위장의 앞에는, 전각보다는 장원에 가까운 으리으리한 석조 건물이 있었다.

“이곳이 성주님께서 머무르시던 거처입니다. 저 역시 더 안내해 드리고 싶지만, 앞서 들은 명령이 있어서.”

“명령이라면…….”

“임시 성주님께서 내리신 명입니다. 진 소협을 포함해서 단 두 분만 출입을 허락하라 하시더군요.”

두 분?

아예 나 혼자라면 모를까, 다른 한 사람이 누구인지는 모르겠다.

의문스러움에 눈살을 찌푸린 그때, 호위장의 입술 사이로 뜻밖의 이름이 흘러나왔다.

“혹시, 함께 오신 일행 중 남호라는 분이 계십니까?”

“어?”

“응?”

모두가 크게 뜨인 눈으로 한 방향을 바라보았다.

멍청한 표정으로 멀뚱멀뚱 서 있는 거한, 태산을 본 호위장이 감 잡았다는 듯이 고개를 끄덕였다.

“아, 저분이 남 대협이시군요. 역시 이름처럼 호랑이 같으신 풍모…….”

호위장의 목소리가 이어지려던 그때.

퍽! 퍽!

오늘따라 유난히도 앙증맞아 보이는 두 주먹으로 태산의 허벅지를 후려친 남호가, 그 커다란 덩치 뒤에서 씩씩거리며 모습을 드러냈다.

“비켜라! 썩 비키란 말이다! 이 식충이 같은 놈 같으니.”

“히히. 그만해라, 남호. 태산이 간지럽다. 히히히.”

“이런 씨팔……!”

차라리 진짜 바위라면 모를까. 계란으로 태산 치기가 통할 리가 있나.

간지러움에 꺄르르 웃는 태산과, 그런 녀석에게 한바탕 쌍욕을 퍼부으려던 남호가 자신을 응시하는 호위장을 향해 허허 웃어 보였다.

“본인이 바로 그 남호요. 남쪽에서 온 호랑이. 남호.”

“…….”

“……뭐요, 그 눈빛은?”

“그, 아닙니다.”

“아니, 설명을 해 보라니까.”

남쪽에서 온 개미. 뭐 그런 걸 쳐다보는 듯한 눈빛으로 남호의 위아래를 훑어본 호위장은 말을 아끼며 수하를 향해 눈짓했다.

끼이익.

새로운 불청객이 마음에 들지 않는지, 거슬리는 소음과 함께 좌우로 열린 문.

당연하게 걸음을 옮기는 내 옆으로 바짝 따라붙은 남호가 작게 속삭였다.

“도대체 반응이 왜 저러지? 호랑이가 그렇게 웃겨? 응?”

“…….”

노인 공경 차원에서, 차마 진실을 말해 주진 못했다.



* * *



본래 성주란 직책의 위상이 높기 때문인지, 아니면 죽은 성주의 부정부패 때문인지는 몰라도 전각 내부는 실로 넓고 호화스러웠다.

저벅. 저벅.

값비싼 청석(靑石)이 깔린 복도를 가로지르는 발걸음 소리가 겹쳐서 울린다.

맞은편에서 걸어오던 십여 명의 남녀가 나와 남호를 향해 고개를 꾸벅 숙이고는 사라졌다.

“의원과 의녀들이군. 시신을 살피러 온 모양인데?”

언제 그랬냐는 듯 차분해진 남호가 중얼거렸다. 그는 전각에 들어옴과 동시에 주위의 모든 것을 파악해 나가고 있었다.

“허, 천장에 야명주(夜明珠)를 박아넣다니. 모르긴 몰라도 백성들의 고혈을 어지간히 쥐어짰겠어.”

“잘은 모르지만, 제가 사천에 있을 때만 해도 죽은 성주에 대한 평이 그리 좋지는 않았죠.”

“저 값비싼 야명주를 쓴 미친놈이 이번에 죽은 성주라면, 그럭저럭 잘 뒈졌군.”

“내돈내산일 수도 있잖습니까.”

“그게 뭔데?”

“본인 돈으로 산 거요.”

남호가 코웃음 치며 대답했다.

“이럴 때 보면 세상 물정 모르는 도련님이 따로 없군. 이참에 노부가 하나 가르쳐 주지. 대저 돈 많고 힘 있는 부류들은 언제나…….”

“내가 가진 것을 쓰지 않고, 남의 재물로 배를 불리죠.”

“어? 아네? 혹시 산서성도 그 모양인가?”

“꼭 그런 건 아니지만…… 어딜 가나 똑같으니까요. 사람 사는 곳은.”

내 대답을 들은 남호가 짐짓 미간을 찌푸렸다.

“희한하군.”

“뭐가요?”

“아니, 그렇잖나. 산서성에서의 일도 아니라면서 그런 말을 한다는 게. 마치 꼭 다른 곳을 고향으로 둔 사람 같아.”

은영각 요원다운 날카로움.

간혹 남호가 슬쩍 내비치는 이런 모습들을 보면 확실히 짬밥이라는 게 있구나 싶다.

‘하지만 짐작도 못 하겠지. 진실이 어떤 건지.’

그간 여러 사건을 겪으며 늘어난 건 무공 실력뿐만이 아니다.

나는 아무렇지 않게 웃으며 입을 열었다.

“똥인지 춘장인지 꼭 찍어 먹어 봐야 압니까?”

“약관 언저리면 충분히 그러고도 남을 나이지. 누구나 겪는 시기야.”

“누구나 겪는 시기지만, 그들 모두가 약관쯤에 열화신룡이라는 별호를 얻을 수 있는 건 아니죠. 아, 이쪽으로.”

천연덕스러운 대답과 방향 전환.

잠시 가늘어진 눈으로 나를 바라보던 남호는 이내 군말 없이 뒤를 따라왔고, 나는 서서히 가까워지는 목소리들을 빼놓지 않고 귓가에 담았다.

― 그럼, 신의께서 보신 바에 의하면 자연사인 거요?

― 정신적 충격으로 인한 급사(急死)로 보는 게 정확합니다. 급격한 체중 감소 또한 가장 큰 이유 중 중 하나겠지요.

― 저런. 그러니까 평소에 살 좀 빼라니까.

― ……여하튼 저 역시 다른 의원들의 진단에 동의합니다. 성주, 아니 이제는 전임 성주로군요. 그분의 죽음에는 별다른 의문이 없습니다.

― 아, 감사하소. 호위장이라는 자가 하도 유난을 떠는 바람에 본 공자의 입장에서도 내심 당혹스러웠는데, 천하에 이름난 신의께서 이리 나서 주니 천군만마를 얻은 것 같구려.

― 과찬이시군요. 의원으로서 마땅히 해야 할 일을 했을 뿐입니다.

― 어허, 겸손이 너무 과해도 좋지 않소. 이번 일을 잘 처리해 주었으니 본 공자, 아니 본 성주가 아주 큰 상을 내리겠소. 여봐라, 게 누구 없느냐!

굽이진 복도를 돌아 선 내가 대답했다.

“있어.”

“당장 재정관을 불러 신의께 재물과 곡식을…….”

문득 흐려지는 말꼬리.

급격하게 어두워진 얼굴로 나를 응시하던 주원공이 긴 침묵 끝에 입을 열었다.

“언제…… 오셨소?”

“지금. 혹시 볼일 남았냐?”

“……조금.”

“그럼 가라. 할 얘기 있으니까.”

“……남았는데?”

“미뤄. 어차피 헛소리나 할 거 뻔하니까.”

내 단호한 대답에 주원공이 슬픈 표정으로 고개를 떨궜다. 이내 힘없이 멀어지는 녀석의 뒷모습을 바라본 적천강이 진지한 목소리로 말했다.

“만약 네 녀석이 일각만 늦었다면, 난생처음으로 황족 아가리를 찢는 진귀한 경험을 할 뻔했다.”

“처음이자 마지막으로 당부의 말씀을 드리자면, 절대 그러지 마세요.”

“노부가 그 정도로 미치진 않았느니라.”

“…….”

그 정도로 미친 것 같아서 문제다.

한숨을 푹 내쉰 나는, 몸은 어떻냐 묻는 적천강의 목소리를 못 들은 체하며 신의에게 고개를 돌렸다.

“그래서, 정확히 뭡니까?”

“무엇이 말입니까?”

“저런 병신한테 모든 걸 곧이곧대로 말했을 리는 없잖아요. 두 분 다 여기 계신 거 보면 견적 나오는데 뭘.”

내 시큰둥한 대답에, 신의가 쓰게 웃었다.

“역시, 적 대협의 제자시군요.”

저거 무슨 뜻이지.

내가 좋아해야 하나, 기분 나빠해야 하나 고민하던 그때.

신의가 소매 속에서 꺼내 든 무언가를 본 남호가 눈을 크게 떴다.

“저건…….”

“네? 저게 뭔데요?”

“고독이다. 그것도 남만 깊은 곳에서나 매우 드물게 나타나는. 혈혼고(血魂蠱)라는 놈이지.”

그 모습을 본 적천강이 고개를 끄덕였다.

“저 친구까지 부른 보람이 있군.”
```

## Final English reading copy

```markdown
# Chapter 849

One shichen.

That was how long it took us to reach the City Lord’s Hall, which served as both his residence and his government offices.

Thudududud!

Stealing Ju Wongong’s carriage—no, borrowing it—had been a stroke of genius.

The six-horse carriage, luxurious enough to be obvious at a glance, possessed a kind of magic that made the horrific traffic jam disappear.

“Stop! Stop! Halt at once!”

“State your identity and business… Wait, I’ve seen this carriage somewhere before.”

We’d turned a crowded main road into an autobahn in the blink of an eye, so of course we stood out even from a distance.

The guards’ eyes went wide when they saw the carriage racing toward them like a mad thing. But a shout from somewhere gave them not even a moment to react.

“Open it!”

“Yes, yes?”

“I said open the gate, you idiots!”

“Y-yes, sir! Open the gate!”

Rrrrmmmble!

Had they been given orders beforehand?

There was no stopping the carriage, no inspection of the sort we should have gone through.

The enormous iron gates swung open to match the carriage’s rapidly approaching speed. Hyuk Mujin, seated on the driver’s bench, didn’t ease up on the reins until we’d passed through no fewer than five gates.

Whinny. Whinny.

The six fine horses, which had been galloping at full speed without pause, snorted roughly. Just then, unfamiliar faces approached me and the Fire Dragon Pavilion members as we climbed down from the carriage.

“Are you Young Hero Jin Taekyung, the Blazing Flame Divine Dragon?”

He didn’t waste a moment before asking, as if he had no time to spare.

Yet there was something subtly different about him from the usual government officials.

Even a military officer working for the government would generally avoid directly using someone’s Murim sobriquet like that.

*A martial artist?*

As I studied the man at the front, who wore lighter armor than the others, Song Ilseom’s Sound Transmission reached my ear.

— I know him. He won’t recognize me, though.

— You know him? Who is he?

— He was fairly well-known as a wandering martial artist. I heard he retired later on…but I didn’t know he’d left Murim altogether and joined the government.

— Really?

— Yes. My memory is accurate.

— Then why are you slipping into casual speech again? Are you older than me?

— I’m fairly sure I’m much older.

Oh, right.

I’d briefly forgotten that even by modern standards, Song Ilseom was a few years older than me.

But if I let that slide, discipline in the Fire Dragon Pavilion would fall apart. I sent a Sound Transmission with all the authority I could muster as Pavilion Master.

— So what if you’re older? Want to end up like Hyuk Mujin?

— ……

— If you don’t like it, you can be Pavilion Master.

Song Ilseom looked at me with a cold, flat stare, then sighed and shook his head.

The man at the front, a former wandering martial artist, spoke again. This time, he looked straight at me.

“Are you Young Hero Jin Taekyung?”

“That’s me.”

“Those who arrived before you told me to expect you. This way, please.”

After briefly introducing himself as the Captain of the Guards for the City Lord of Sichuan Province, he led us deep into the City Lord’s Hall.

“I presume you’ve already heard about the circumstances.”

I nodded as I walked behind him.

“To some extent.”

“You must have been quite taken aback.”

“At first, a little. I thought it was someone I knew.”

“Ah, do you mean the Acting City Lord?”

“Yes.”

There were currently two City Lords in this land.

No—there had been two.

Ju Wongong, a distant imperial relative with whom I’d had some history.

And the former City Lord of Sichuan Province, who’d been bedridden for the past few months.

*What was the name of the guy who just died? Won Gyun?*

It was such a memorable name for an extra that I couldn’t forget it. He sounded like the kind of guy who’d be a complete disaster at sea, even if not on land. Maybe it was because of that enormous belly that had looked like he was twenty months pregnant, not merely about to give birth.

“I don’t know if you remember, but I once saw you up close.”

“You saw me?”

“It was just before the Sichuan Blood Tragedy. You came to see the City Lord with His Highness Prince Shangshan’s token and asked for support.”

“Oh. Right. So you were there then, too?”

“Yes. As the Captain of the Guards, I stayed by the City Lord’s side. I never imagined something like this would happen back then.”

The Captain answered with a bitter expression and kept walking.

As befitted a place that was both the City Lord’s residence and the government offices where he worked, people in well-appointed official robes were everywhere.

“The atmosphere isn’t as tense as I expected. I thought there’d already been a big uproar.”

At Ju Hwaran’s murmur behind me, the Captain of the Guards nodded.

“That’s only natural. Those who work in the City Lord’s Hall knew at least part of the City Lord’s condition.”

The calm atmosphere on the grounds was proof that the City Lord’s death hadn’t come as a sudden shock.

But I didn’t take the situation at face value.

If it were as natural and ordinary as it seemed, there’d be no reason for Jeok Cheongang and the Divine Physician to get involved.

Besides…

*If they knew only part of it, that means there’s something that hasn’t been made public yet.*

How long had we been walking, with me lost in thought?

The farther we went, the fewer people we encountered. Even the guards, who’d been everywhere before, disappeared.

At last, the Captain of the Guards stopped in front of a magnificent stone building, more like an estate than a pavilion.

“This is where the City Lord was staying. I’d like to escort you farther, but I have orders to follow.”

“Orders?”

“Orders from the Acting City Lord. He said only two people, including Young Hero Jin, are to be allowed inside.”

Two people?

I could understand if it were just me, but I had no idea who the other person was supposed to be.

I frowned, puzzled, when an unexpected name slipped from the Captain’s lips.

“Is there someone among your companions named Namho?”

“Huh?”

“Mm?”

Everyone’s eyes widened as we looked in one direction.

The Captain of the Guards nodded as if he’d figured it out when he saw Taishan, the giant standing there with a blank expression.

“Ah, that must be Great Hero Nam. His bearing is indeed tiger-like, just as his name suggests…”

Thwack! Thwack!

Namho emerged from behind Taishan’s huge frame, panting as he hammered Taishan’s thigh with his two fists, which looked unusually tiny today.

“Move! I said get out of the way! You useless freeloader!”

“Heehee. Stop it, Namho. Taishan’s ticklish. Heeheehee.”

“Son of a bitch…!”

If he’d been an actual rock, maybe, but there was no way an egg could crack Mount Taishan.

Taishan giggled at the tickling. Namho was about to unleash a torrent of curses at him, but instead gave the Captain of the Guards, who was watching him, a hearty laugh.

“I’m Namho. The tiger from the south. Namho.”

“……”

“What’s with that look?”

“N-no, it’s nothing.”

“No, explain yourself.”

The Captain of the Guards looked Namho up and down as if he were staring at an ant from the south. Then, without saying anything more, he gestured to one of his subordinates.

Creeeak.

The doors swung open to either side with an irritating squeal, as if the new intruder wasn’t welcome.

Namho hurried up beside me as I headed inside and whispered,

“What’s with his reaction? Is a tiger that funny? Huh?”

“……”

Out of respect for my elders, I couldn’t bring myself to tell him the truth.

* * *

Maybe it was because of the City Lord’s lofty station, or maybe because of the corruption of the dead City Lord. Whatever the reason, the inside of the pavilion was truly spacious and lavish.

Clop. Clop.

Our footsteps echoed over the corridor’s expensive bluestone tiles.

A dozen or so men and women walking toward us bowed deeply to Namho and me, then passed by.

“Physicians and female physicians. Looks like they came to examine the body.”

Namho murmured, calm again as if nothing had happened. The moment he entered the pavilion, he’d begun taking in everything around him.

“Heh. They even embedded night-shining pearls in the ceiling. I can only imagine how much they squeezed the people dry.”

“I don’t know much about it, but even when I was in Sichuan, people didn’t have much good to say about the dead City Lord.”

“If the bastard who put up those expensive night-shining pearls was the City Lord who just died, then good riddance to him.”

“Maybe he bought them with his own money.”

“What does that mean?”

“He paid for them himself.”

Namho snorted.

“Sometimes, you really are a sheltered young master who knows nothing about the world. Let this old man teach you something. Those with money and power always…”

“Use other people’s wealth to fill their own bellies instead of spending what they have.”

“Huh? You know? Is that how it is in Shanxi Province, too?”

“Not always, but…it’s the same everywhere. That’s just how people are.”

Namho furrowed his brow at my answer.

“That’s odd.”

“What is?”

“Well, you said it yourself—it’s not something you experienced in Shanxi Province. You sound like someone whose hometown is somewhere else.”

The sharp instincts of a Hidden Shadow Pavilion agent.

Whenever Namho let this side of himself show, even for a moment, I could tell he had years of experience behind him.

*But he’ll never guess what the truth is.*

The things I’d gained from all the incidents I’d been through weren’t limited to martial arts skill.

I smiled casually and replied,

“Do you have to taste shit to tell it from black bean sauce?”

“Someone around twenty would do exactly that. It’s a phase everyone goes through.”

“Everyone goes through it, but not everyone earns the sobriquet Blazing Flame Divine Dragon around that age. Ah, this way.”

I answered nonchalantly and changed direction.

Namho looked at me with narrowed eyes for a moment, but then followed without another word. Meanwhile, I kept an ear out for the voices slowly drawing nearer.

— So, according to the Divine Physician’s examination, it was a natural death?

— It would be more accurate to say he died suddenly from emotional distress. His rapid weight loss was one of the main causes as well.

— I see. That’s why I kept telling him to lose some weight.

— …In any case, I agree with the other physicians’ diagnoses. There’s nothing particularly suspicious about the City Lord’s—or rather, the former City Lord’s—death.

— Ah, thank you. That Captain of the Guards has been making such a fuss that even I, this Young Master, was getting a little flustered. Now that the renowned Divine Physician of the realm has stepped in, it feels like I’ve gained a thousand troops.

— You flatter me. I only did what any physician should.

— Come now, too much modesty isn’t good either. Since you’ve handled this matter so well, I, this Young Master—or rather, this City Lord—will reward you handsomely. Someone, come here!

I rounded the bend in the corridor and answered,

“I’m here.”

“Immediately summon the steward and have him give the Divine Physician wealth and grain…”

His voice trailed off.

Ju Wongong stared at me, his face darkening rapidly. After a long silence, he finally spoke.

“When…did you arrive?”

“Just now. Got anything left to do?”

“……A little.”

“Then go. I have something to talk about.”

“……I still have some things to do.”

“Put them off. You’re obviously just going to spout nonsense.”

At my firm reply, Ju Wongong lowered his head sadly. Jeok Cheongang watched him walk away, his back limp, then spoke in a serious voice.

“If you’d been a quarter-hour later, I might have had the rare experience of tearing the mouth off a member of the imperial family for the first time in my life.”

“One thing I’ll ask you for, now and forever: don’t do that.”

“This old man isn’t that crazy.”

“……”

That’s exactly the problem. He seems crazy enough to do it.

I sighed deeply and turned to the Divine Physician, pretending not to hear Jeok Cheongang asking how I was feeling.

“So, what exactly is it?”

“What do you mean?”

“You wouldn’t have told that idiot everything, would you? And seeing both of you here tells me enough.”

At my indifferent reply, the Divine Physician smiled ruefully.

“As expected of Sir Jeok’s Disciple.”

What was that supposed to mean?

I was wondering whether I should feel pleased or offended when Namho’s eyes widened at the thing the Divine Physician pulled from his sleeve.

“That’s…”

“What is it?”

“Gu poison. A very rare kind, found only deep in Nanman. It’s called Blood Soul Gu.”

Jeok Cheongang nodded as he looked at it.

“Bringing that fellow here was worthwhile.”
```
