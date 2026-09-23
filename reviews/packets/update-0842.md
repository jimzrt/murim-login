<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0842.txt",
      "sha256": "6eb66fe7368a31cbf26ce30d0733df4dc28e929ac3b882a7ba2d3cf0b917b62e",
      "bytes": 12980
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "c69ed189e44777d4aaccc668f6fddfbc28c3ec31ec0f139ca59cd021f3047813",
      "bytes": 2682
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2ac235886e36b4a9cfac67990c4e303d5cbbbaacdc20104970ce04b7ba9ca08c",
      "bytes": 227427
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "1e0ddf49a4bbeb44d67cdd0ef58a810af6723f4def1f1c2c3e6d54692f90d346",
      "bytes": 723
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "be666c9303d8a50e7816a251e171b56e1f1cc1fd295ed0c668ef42f5cafb3fd6",
      "bytes": 1355
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "ad97f6713796bd65067fd5c80877dc07a0855916c1389ecd74c6ea728a1d412a",
      "bytes": 1599
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "e821f7a093a7b6ba03812bb299462ba7f9664ed9672d8d46c2695891906deca5",
      "bytes": 1888
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "fca824199a74f08c450016741a4434bb8209ddfe930ea2a71cac359c5913b00f",
      "bytes": 622
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "d3e87f5e36d4ba404b6f7115651da04634dbe6d42fcd5e03f067ef3cfb469372",
      "bytes": 937
    },
    {
      "path": "characters/Namho.md",
      "sha256": "34ce866bb3b3a81b869238add9d3cbfdb635298a8383723eadac616f3ec4fa65",
      "bytes": 936
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "13cfd8097baf3b55ccb02f4ca72643701e40e56ba23e8e6a1c1cb409627328b2",
      "bytes": 936
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "54ac604d7368b951a002c68d85575a1f0f272b8a5910f1c7f5f7bdc174dfadbe",
      "bytes": 964
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "7ee8b9a4ec3450da275b5f80c01b6a3f997556a827ab09cae5a471b5df457c5f",
      "bytes": 1074
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "b95b6c25fcfb47008968d7f08ef8cfe803564f915387cfeda304e8555dbdc5aa",
      "bytes": 787
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2d3ba6654cdbcc372510ec72e3979b0d7dd3413b49d0a44c281c59171f618c6d",
      "bytes": 251874
    }
  ],
  "estimated_tokens": 14343
}
-->

# Durable State Update — Chapter 842

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
1 and safe_through 842. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 842. Profile updates may replace only one
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
  "chapter": 842,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 842,
    "continuity_sources": [842],
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
    "The supernatural Rift began at 10%; its progress increases the distribution and concentration of magical power.",
    "The System’s Status Window is inaccessible; Jin suspects an update may be responsible.",
    "Jin saw a vision of a black-haired man killing Ahomed after the ritual; whether it was real is unknown, and Jin believes the man was not Asmodeus.",
    "Jin’s [Broken Body] injury around his lower dantian remains unresolved; leveling up did not heal it.",
    "Jin is at the Sichuan Tang Clan after being unconscious for three days; Jeok Cheongang has reunited with him.",
    "The Sichuan Tang Clan and Sichuan Murim are rebuilding after Dark Heaven’s attack; allied martial artists remain to help treat patients and guard against another attack.",
    "Tang Sadok is Family Head of the Sichuan Tang Clan and considers Jin and Cheongpung benefactors.",
    "Ju Wongong remains temporarily appointed acting City Lord of Sichuan Province by imperial order while under exile.",
    "Jeok and Jin have never formalized their Master-Disciple bond; Jeok suggests they may do so when the time comes and everything is set right."
  ],
  "continuity_sources": [
    840,
    841
  ],
  "open_questions": [
    "Why did the Main Quest fail despite the Doppelganger’s erasure, and who or what was summoned?",
    "Was Jin’s vision of the summoned being real, System-delivered, or prophetic?",
    "What will happen as the Rift progresses and more beings enter the world?",
    "Who or what chose Jin, and what is the Ark?",
    "What did Jeok mean by the time when everything returns to its proper place?"
  ],
  "safe_through": 841,
  "temporary_decisions": [
    "Keep magical power distinct from mana; keep Blink distinct from Teleport and Warp. Extended-range Blink causes severe strain.",
    "Keep Fire Storm and Aqua Storm as distinct named spells.",
    "Render [영웅의 검] as “Hero’s Sword,” 에어 슬래시 as “Air Slash,” and 실드 마법 as “Shield magic.”",
    "Render 선택받은 자 as “the Chosen One,” 방주의 주인 as “the Master of the Ark,” [격변] as [Cataclysm], [어데 도씹니꺼] as “Where’s Your Do Clan From?,” and [종족 학살자] as “Species Slayer.”",
    "In chapter 839, render 균열 as a social fracture or division, not the supernatural Rift; render 醜王 as “Disgrace King” when used as Jin’s mocking imagined epithet for Jeok Cheongang."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 송일     | **Song Il**        |
| 주화란    | **Ju Hwaran**      |
| 종남파    | **Zhongnan Sect**                |
| 사천당가   | **Sichuan Tang Clan**            |
| 용봉표국   | **Yongbong Escort Bureau**       |
| 사파     | **unorthodox faction**                           |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 표국     | **Escort Bureau**                            |
| 총표두    | **Chief Escort**                             |
| 상태               | **Status**                     |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남호 | **Namho** | Hidden Shadow Pavilion code name; literally associated with amber from the south. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 은자 | **silver nyang** | Silver currency unit. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 당가 | **Tang Family** | Short form for the Sichuan Tang Clan when distinguished from 사천당문. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |

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
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
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
| 적천강 | 의원 | interrogator_to_physician | you; quack | blunt and threatening | Jeok shakes the physician and demands an explanation for Jin's seven-day sleep before ordering him to summon the Beast Miao King. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 840
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 841
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son; he uses quiet practices such as fishing to empty his mind. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 841
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan, though they have never formalized their bond; Jeok hints they may do so when the time comes. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to the late Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and is a long-standing rival of Peng Cheolhu.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 839
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Magic Johnson is an allied Grand Mage who supplies him with intelligence, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, Jin-ho is his older friend and trusted confidant, and he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 839
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 840
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, filial, composed under pressure, and burdened by intense guilt over the escort journey's deaths.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Namho.md

# Namho (남호)

- **Safe through:** Chapter 840
- **Aliases:** Elder Chao
- **Role:** Namho is an eighty-year-old non-Han Hidden Shadow Pavilion agent who spent more than fifty years operating under the cover of the Poison Flower Pavilion in Nanman and now serves as the Fire Dragon Pavilion’s guide.
- **Personality:** Duty-bound, pragmatic, and observant; uses theatrical violence to protect intelligence work and takes a veteran’s concern for the younger generation’s resolve.
- **Voice:** Measured and reflective when advising the younger generation, loudly abusive when maintaining his local cover, and capable of theatrical boasts and dry humor.
- **Relationships:** Namho is a Hidden Shadow Pavilion contact for Jin Taekyung and the Fire Dragon Pavilion, receives intelligence from the Pavilion Master, and knows the code used by the Thousand-Faced Fox.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 840
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes, and a member of the Fire Dragon Pavilion.
- **Personality:** Outwardly courteous and smiling, inwardly calculating, but genuinely protective of Taishan; in combat he is ruthlessly pragmatic, survival-focused, and unafraid to stake his life.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo commands the absolutely loyal Taishan, is Sima Gong's son, was Ju Hwaran's former fiancé in a political engagement, and has joined the Fire Dragon Pavilion while openly intending to use Jin Taekyung as a useful card; he is now openly hostile toward fellow member Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 840
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect and the Roaring Fury Swordsman; senior brother of Sect Leader Gong Iljung; came to the Jin Family of Taiyuan to demand redress for Gong Ilhyuk's injury and the alleged insult to Zhongnan; attacked Jin Taekyung with the Heavenly River Thirty-Six Swords, was stopped by Jeok Cheongang, and was publicly humiliated by him.
- **Personality:** Arrogant, domineering, punitive, and confident in his martial power and seniority.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 840
- **Aliases:** Escort Captain Song
- **Role:** Level 110 young escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a newly accepted member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion; he is currently bound and unconscious under the reconnaissance squad's guard after being struck at a Sleep Acupoint.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Forceful and urgent in command, with a rough and confrontational edge.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 840
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion; he helped Jin escape the underground prison by blocking the stairs and overpowering the Bai warriors.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃842화



불현듯 잠에서 깨어난 청년은 눈을 깜빡였다.

낯선 천장. 코끝을 감도는 알 수 없는 냄새. 그리고 미처 상황을 인지하기도 전에 불쑥 시야에 끼어든 무언가의 형체까지.

“으헉!”

빡!

그야말로 순식간이었다.

본능적으로 상반신을 일으킨 청년은 강렬한 충격과 함께 다시 쓰러졌다.

‘뭐지?’

모르겠다.

아니, 그런 것 따위는 신경도 안 쓰일 만큼 더럽게 아팠다.

“끄으으…….”

마치 바위로 얼굴을 찍히면 이런 기분일까.

청년이 몸을 구부린 채 신음하던 그때, 고통으로 인해 새하얗게 물든 시야 속에서 크고 두툼한 뭔가가 날아와 그의 뺨을 후려쳤다.

철썩.

“혁무. 정신 차려라.”

철썩. 철썩.

“혁무. 혁무.”

마치 꿈속처럼 아련하게 울려 퍼지는 누군가의 목소리에 청년, 아니 혁무진은 목소리의 주인이 누구인지 깨달았다.

조금 전 자신이 몸을 일으키자마자 부딪쳤던 단단한 물체가 바로 그 누군가의 얼굴이었다는 사실도 함께.

‘태산이, 이 개자식…….’

틀림없다.

익숙한 목소리. 그리고 도무지 인간 같지도 않은 단단함.

혁무진의 주변에 괴물들은 많았지만, 이 정도로 순수한 의미로서의 괴물은 한 사람밖에 없었다.

철썩. 철썩. 철썩.

“혁무, 괜찮나?”

너 때문에 안 괜찮다, 이 새끼야.

혁무진은 눈물이 날 것 같았다. 그냥 충격으로 인해 잠시 쓰러졌던 것뿐인데, 이 미친놈이 쉴 새 없이 귀싸대기를 올려붙이는 통에 일어날 겨를이 없었다.

“그, 그만…….”

“혁무우! 눈을 떠라!”

쩍!

이번엔 제대로 들어갔다. 간신히 입을 열었다가 혀를 깨물어 버린 혁무진의 신형이 축 늘어졌다.

서서히 흐려지는 시야 속에서는 지금까지의 삶이 빠르게 스쳐 지나가고 있었다.

‘어머니, 아버지. 죄송합니다. 두 분 말씀이 맞았어요.’

그냥 처음부터 얌전히 가업을 물려받았어야 했다.

그랬다면 지금쯤 혁가 포목점의 후계자로 공자님 소리 들으면서 길거리에 은자를 뿌리고 다녔을 텐데, 현실은 틈만 나면 진태경에게 깝죽대다가 처맞고 코피 뿌리는 게 일상이 되어 버렸다.

‘이제는 하다 하다 태산이 저놈한테 맞아 죽다니.’

혁무진은 서서히 아득해지는 시야 속에서 생각했다. 지금 이대로 죽는다면 단순한 사고사인지, 아니면 전사(戰死)로 취급될지.

그리고 모든 것이 끝났다고 생각한 순간, 구원의 종소리와도 같은 목소리를 들었다.

“세상에, 태산 소협! 당장 멈춰요!”

불현듯 울려 퍼진 낭랑한 음성. 혁무진의 뺨을 후려치던 손길이 우뚝 멎었다.

“어. 어어?”

갑작스럽게 나타난 주화란의 모습에, 태산이 송아지 같은 눈을 깜빡이며 말을 이었다.

“태산이. 혁무 깨우고 있었다. 나쁜 짓 안 했다.”

“혁무가 아니라 혁. 혁이 성씨예요. 그리고 태산 소협이 하려고 했던 건 깨우는 게 아니라 잠재우는 쪽에 가깝고요.”

“억울하다. 태산이. 혁무 도우려고 했을 뿐이다.”

“물론 그럴 수도 있겠죠. 인생에 회한을 느낀 혁 소협이 죽여 달라고 부탁했다면.”

작게 한숨을 내쉰 주화란이 혁무진의 상태를 살폈다.

한때 진태경에게 두들겨 맞아 두 배나 부풀어 올랐던 그의 얼굴은, 이제 세 배가 되어 있었다.

“혁 소협. 혁 소협. 지금 제 말 들리시…… 지금 울어요?”

살 수 있음을 깨달은 혁무진이 눈물을 줄줄 흘리며 대답했다.

“아닙니다, 주 소저. 사내대장부는 울지 않습니다. 크흐윽.”

“……그럼 앞으로 혁 소저라고 불러 드리면 되나요?”

“아니, 그건 좀.”

“말하는 거 보니 멀쩡하네요. 다행히 앞서 당가(唐家)에서 붙여 준 의원이 치료를 잘해 준 모양이에요.”

여느 때처럼 주화란의 곁을 지키던 송일섬이 그 모습을 보고 중얼거렸다.

“아무래도 그 의원을 다시 불러야 할 것 같은데.”

“괜찮아요. 이 정도면 의원이 주고 간 연고만 발라도 금방 나을 거예요.”

눈물을 닦고 있던 혁무진이 끼어들었다.

“주 소저. 죄송한 말씀이지만, 제가 안 괜찮습니다.”

“눈물이나 마저 닦으세요. 그런데 연고가 어디 있더라, 태산 소협. 여기 침상 옆에 있던 거 못 봤어요?”

“태산이. 안다. 작은 도자기에 담겨 있던 것을 말하는 것 아닌가?”

“맞아요. 어디 있어요?”

“먹었다. 그럭저럭 맛있었다.”

“아…….”

“주 소저, 제발 의원을 불러 주십시오. 죽을 것 같습니다.”

주화란은 연고를 처먹은 놈과 질질 짜면서 엄살을 부리는 놈 중 어느 쪽이 더 죄질이 나쁜지 고민했지만, 쉽게 답을 내리지 못한 채 새로운 연고를 가져오는 것을 택했다.

“송 호위, 미안한데 연고 좀 가져다줄래요?”

“미안할 필요는 없소. 단지 그건 내 임무에 포함되지 않는 일이라 추가 수당이 붙…….”

허리춤에 찬 검집을 만지작거리는 주화란의 모습을 발견한 송일섬이 굳은 얼굴로 말을 이었다.

“……지만, 지금은 농담할 때가 아닌 것 같군.”

“농담이었던 거 맞아요?”

“아마도. 아니, 확실하오.”

“그런데 아직도 안 가셨네요.”

“빨리 다녀오도록 하지.”

황급히 문을 나선 송일섬은 불과 촌각이 지나기도 전에 연고를 갖고 돌아왔다. 조금 전까지만 해도 자리에 없던 두 사람과 함께.

“저놈이 또 처먹을까 봐 일부러 연고를 넉넉히 챙겨왔는데, 이 정도면 충분한 거요?”

“잠시 자리를 비운 사이에 태산이가 또 사고를 쳤다고 들었소. 미안하군.”

연고의 양을 가늠하는 송일섬과 사과하는 사마표에 이어, 남호가 잔뜩 기대감이 서린 표정으로 물었다.

“이건 그냥 물어보는 건데, 혹시 화룡각에는 이런 잘못을 저질렀을 경우에 해당되는 규율이 없나? 예를 들자면 오체분시(五體分屍)라든지…….”

줄줄이 제 할 말만 쏟아내는 세 사람의 모습에, 주화란은 또다시 검집을 더듬었다. 언제부턴가 습관이 된 행동이다.

정확히는 혈육처럼 따랐던 총표두에 의해 용봉표국을 종남파에 뺏길 뻔하고, 남만에서 온갖 일을 겪으면서부터 이렇게 되었다.

‘참자, 화란아. 조금만 더 참자.’

마음 같아서는 미친년처럼 한바탕 칼춤이라도 추고 싶은 마음이었지만, 크게 심호흡한 주화란은 마지막 인내심을 발휘하여 차례대로 대답했다.

“연고는 그 정도면 충분하고, 사마 소협은 애초부터 자리를 비우지 마세요. 어차피 자리에 있어 봤자 또 다른 사고를 치겠지만 적어도 연고를 먹거나 혁 소협을 도로 기절시키는 일은 없겠죠. 그리고 남 노야.”

“응?”

“정 그렇게 태산 소협을 처리하고 싶으시면 직접 하세요. 마침 사천당가니까 독이라도 구해 보시든가.”

“…….”

“…….”

“…….”

“왜요, 누구 더 할 말 있어요?”

서릿발이 흩날리는 듯한 목소리에, 방 안의 모두가 입을 꾹 다물고 고개를 저었다.

심지어 눈치 없는 것으로는 천하에서 한 손가락에 꼽힐 태산과 끙끙 앓는 소리를 흘리던 혁무진도 침묵한 채 다른 이들과 눈빛을 교환할 뿐이었다.

‘주 소저가 많이 변했군. 근래 들어 고생을 많이 하긴 했지만 그래도 이 정도일 줄이야. 저자는 명색이 호위인데 뭐 아는 거 없나?’

‘저 사파 잡놈이 왜 날 쳐다보는 거지? 이번에야말로 제대로 한번 붙어 보자는 건가?’

‘허어, 말년에 귀엽고 착한 손녀 하나 생기나 했더니 어쩌다 이렇게…… 하긴, 아무리 그래도 오체분시는 좀 심했지. 우선 저 아이 말대로 독을 구해 봐야겠군.’

‘태산이. 연고 또 먹고 싶다. 나름 별미였다.’

‘이 염병할 인간들은 나 다친 건 관심도 없네. 그런데 사천당가라니, 뭐가 어떻게 된 거야?’

물론 서로 간의 소통은 눈곱만큼도 이루어지지 않았지만, 주화란을 제외한 모두는 암묵적으로 합의했다.

분위기가 어느 정도 진정되기 전까지는 입을 닥치고 있기로.

그리고 눈치를 살피며 스스로 연고를 퍼 바르던 혁무진이 일련의 상황을 들을 수 있었던 것은, 딱딱하게 굳어 있던 주화란의 얼굴이 부드럽게 펴진 후의 일이었다.

“예? 이틀이나 지났다고요?”

주화란이 고개를 끄덕였다.

“네. 시간상으로 정확히 이틀이네요.”

“그럼 여기가 정말로…….”

“앞서 말씀드렸듯이 사천당가죠. 더 정확히는 당가의 외원에 있는 의방(醫方)이고.”

혁무진은 멍하니 눈만 깜빡였다.

도무지 믿을 수 없었다. 그냥 잠시 푹 자고 일어난 것뿐인데 이틀이 지났고, 사천당가의 의방에서 눈을 뜨다니.

“도대체 무슨 일들이 있었던 겁니까?”

“혁 소협, 아무것도 기억 안 나세요?”

“예. 그 나룻터에서 조장님과 황족이 대화를 나눌 때 뭐라고 말했던 것까지만 기억납니다. 그 후로는 눈앞이 번쩍했고요.”

팔짱을 낀 채 비스듬히 벽면에 기대어 서 있던 송일섬이 중얼거렸다.

“정확히 기억하고 있군.”

“예? 그게 끝입니까?”

“그래. 사실 우리 중 그 광경을 제대로 본 사람은 아무도 없지만.”

사마표가 자신도 모르게 고개를 끄덕이며 덧붙였다.

“실로 엄청난 속도였지. 그렇게 빠른 일권(一拳)은 처음 봤어. 뭔가가 흐릿하더니 북 터지는 소리와 함께 자네가 쓰러지더군. 그게 전부야.”

“주군 틀렸다. 그게 전부 아니다. 태산이. 처음부터 끝까지 다 봤다.”

불쑥 끼어든 태산이 몸을 부르르 떨며 말을 이었다.

“각주. 혁무 팼다. 엄청 팼다. 진짜 존나게 팼다.”

“…….”

“각주. 이미 쓰러져 있는 혁무 밟았다. 마치 고기 다지듯이 잘근잘근 밟았다. 아, 고기 먹고 싶다.”

“…….”

“아, 그리고 고추도 밟으려고 했는데 사람들이 말렸다. 태산이도 말렸다. 그건 사람 할 짓 아니다. 아, 고추 듬뿍 넣은 사천식 오향장육 먹고 싶다.”

의방 한구석에서 곰방대를 뻐끔거리던 남호가 탄식했다.

“이런 시팔, 그냥 이참에 오체분시시키자니까.”

“태산이. 오체분시 모른다. 남호 아나?”

“알지. 누구처럼 염병할 놈들을 소나 말에 묶은 다음 그대로 팔다리를 아주 그냥 쫙쫙 찢어서…….”

“오, 그럼 다리 살은 태산이가 찜!”

우직.

곰방대를 부러트린 남호가 맹수처럼 포효하며 태산에게 달려들었다.

사마표에게 붙잡혀 버둥거리는 그의 모습에 한숨을 내쉰 주화란이 입을 열었다.

“여하튼 그렇게 됐어요. 그쪽은 안전하니까 괜히 지금 살펴보실 필요는 없고요.”

잠깐의 소란을 틈타 다급하게 주요부위의 안전을 확인한 혁무진이 힘없이 대답했다.

“다행이군요. 조장님은 어디 계십니까?”

“적 대협과 함께 계세요.”

“예? 이틀 내내 말입니까?”

“네. 두 분 사이에 쌓인 이야기가 많으신 모양이더라고요. 정확히 어떤 내용인지는 모르겠지만.”

“아니, 얼마 전까지 함께 있었으면서 무슨 이야기를 이틀씩이나…….”

“따로 말씀이 없으시니 저희야 모를 수밖에요. 다만 신의(神醫)께서 각주님을 위해 단환을 제조 중이시라고 들었어요. 아마도 단순한 이야기가 아니라 몸 상태를 회복시키기 위한 준비 과정일지도 몰라요.”

주화란의 그럴듯한 추측에, 혁무진이 고개를 끄덕였다.

“하긴, 머나먼 만리타향에 있다가 돌아온 것도 아닌데 할 얘기가 많으면 뭐 그리 많겠습니까. 다들 안 그래요?”



* * *



머나먼 만리타향에 떨어져 있다가 돌아오면 할 얘기가 많은 법이다.

특히 바로 그 만리타향에서 온갖 상상할 수도 없는 일들이 벌어지고 있다면 더더욱.

그리고 끝없이 이어지는 내 이야기를 모두 들은 적천강은 한참 동안 침묵하더니, 이내 짧고 굵은 한 마디로 소감을 대신했다.

“좆 됐군.”
```

## Final English reading copy

```markdown
# Chapter 842

The young man who had suddenly awakened from sleep blinked.

An unfamiliar ceiling. A strange smell tickling his nose. And, before he could even grasp what was happening, the shape of something abruptly intruding into his field of vision.

“Ugh!”

Wham!

It happened in an instant.

The young man instinctively sat up—and immediately collapsed again with a tremendous impact.

*What was that?*

He had no idea.

No, he was in too much damn pain to care.

“Urrgh…”

Was this what it felt like to have your face smashed in with a rock?

As the young man curled up and groaned, something big and thick flew through his vision, bleached white with pain, and slapped him across the cheek.

Smack.

“Hyukmu. Wake up.”

Smack. Smack.

“Hyukmu. Hyukmu.”

At the sound of someone’s voice echoing faintly, like it was coming from a dream, the young man—no, Hyuk Mujin—realized who it belonged to.

He also realized that the solid object he’d run into as soon as he sat up had been that person’s face.

*Taishan, you son of a bitch…*

No doubt about it.

That familiar voice. That inhumanly solid body.

There were plenty of monsters around Hyuk Mujin, but only one who was a monster in the purest sense of the word.

Smack. Smack. Smack.

“Hyukmu, are you all right?”

I’m not all right because of you, you bastard.

Hyuk Mujin felt like he was going to cry. He’d only passed out for a moment from the impact, but this lunatic kept slapping him across the face so relentlessly that he hadn’t had a chance to get up.

“P-please stop…”

“Hyukmuu! Open your eyes!”

Whack!

This time, the blow landed squarely. Hyuk Mujin had just managed to open his mouth when he bit his tongue, and his body went limp.

As his vision slowly faded, his life began flashing before his eyes.

*Mother, Father. I’m sorry. You were right.*

He should’ve just taken over the family business like a good son from the start.

If he had, by now he’d be the heir to the Hyuk Family Textile Shop, being called Young Master and scattering silver nyang in the streets. Instead, he’d made a habit of mouthing off to Jin Taekyung whenever he got the chance, then getting beaten until his nose bled.

*And now I’m going to get beaten to death by that bastard Taishan.*

With his vision growing dim, Hyuk Mujin wondered: if he died like this, would it be considered an accidental death or a death in battle?

Then, just as he thought everything was over, he heard a voice like the tolling of a bell of salvation.

“Good heavens, Young Hero Taishan! Stop right now!”

At the clear voice that suddenly rang out, the hand slapping Hyuk Mujin’s cheek came to an abrupt halt.

“Huh? Uh…”

At the sight of Ju Hwaran appearing out of nowhere, Taishan blinked his calf-like eyes and continued.

“Taishan waking Hyukmu. Not doing anything bad.”

“It’s not Hyukmu. It’s Hyuk. Hyuk is your family name. And what you were doing was closer to putting him to sleep than waking him up.”

“That’s unfair. Taishan only wanted to help Hyukmu.”

“Of course. If Young Hero Hyuk had asked you to kill him because he regretted his life, that might be true.”

Ju Hwaran let out a quiet sigh and checked Hyuk Mujin’s condition.

His face, once swollen to twice its size after Jin Taekyung had beaten him, was now three times as big.

“Young Hero Hyuk. Young Hero Hyuk. Can you hear me… Are you crying?”

Realizing he was going to live, Hyuk Mujin answered as tears streamed down his face.

“No, Young Lady Ju. A real man doesn’t cry. Sniff…”

“Then should I call you Young Lady Hyuk from now on?”

“No, I’d rather you didn’t.”

“You sound fine, at least. I’m glad the physician the Tang Family sent earlier treated you well.”

Song Ilseom, who—as usual—had been standing beside Ju Hwaran, looked on and muttered.

“I think we may need to call that physician back.”

“It’s fine. At this point, just applying the ointment the physician left should be enough to make him better soon.”

Hyuk Mujin, who’d been wiping his tears, cut in.

“Young Lady Ju. I’m sorry to say this, but I’m not fine.”

“Finish wiping your tears first. Now, where was that ointment? Young Hero Taishan, did you see it beside the bed?”

“Taishan knows. You mean the ointment in the small porcelain jar?”

“That’s right. Where is it?”

“Taishan ate it. It was pretty tasty.”

“Oh…”

“Young Lady Ju, please call the physician. I think I’m going to die.”

Ju Hwaran wondered which of the two had committed the worse offense—the one who’d eaten the ointment or the one sniveling and making a fuss—but, unable to decide, she decided to have more ointment brought in.

“Captain Song, sorry, could you bring me some ointment?”

“No need to apologize. It’s just that this isn’t part of my duties, so there’ll be an extra charge…”

Song Ilseom noticed Ju Hwaran fiddling with the scabbard at her waist. His face stiffened as he continued.

“…but this doesn’t seem like the time for jokes.”

“Were you joking?”

“Probably. No, definitely.”

“You’re still here, though.”

“I’ll be right back.”

Song Ilseom hurried out the door and returned with ointment before even a few moments had passed. He wasn’t alone—the two people who hadn’t been there a moment earlier were with him.

“I brought plenty of ointment in case that idiot eats it again. Is this enough?”

“I heard Taishan caused another problem while I was away. I’m sorry.”

After Song Ilseom, who was judging the amount of ointment, came Sama Pyo, apologizing. Then Namho asked with an expectant look:

“I’m just asking, but does the Fire Dragon Pavilion have any rules for dealing with this sort of offense? Something like being dismembered into five pieces, for instance…”

At the sight of all three of them firing off whatever they wanted to say, Ju Hwaran reached for her scabbard again. She’d started doing that without thinking, some time ago.

More precisely, it had started when the Chief Escort she’d followed like family had nearly cost the Yongbong Escort Bureau to the Zhongnan Sect, and had only gotten worse after everything she’d been through in Nanman.

*Stay calm, Hwaran. Just a little longer.*

She wanted to go on a rampage, dancing around with her sword like a madwoman. But Ju Hwaran took a deep breath, summoned the last of her patience, and answered them one by one.

“That’s plenty of ointment. Young Hero Sama, don’t leave in the first place. Taishan would probably cause some other trouble even with you here, but at least he wouldn’t eat the ointment or knock Young Hero Hyuk unconscious again. And Old Master Namho.”

“Yes?”

“If you really want to deal with Young Hero Taishan so badly, do it yourself. This is the Sichuan Tang Clan, after all. Why not see if you can find some poison?”

“……”

“……”

“……”

“What is it? Does anyone else have something to say?”

At her frosty voice, everyone in the room shut their mouths and shook their heads.

Even Taishan, who was second to none in the world when it came to being oblivious, and Hyuk Mujin, who’d been groaning in pain, fell silent. They only exchanged glances with the others.

*Young Lady Ju has changed a lot. She’s had a hard time lately, but I didn’t think it was this bad. That man’s supposed to be her escort. Doesn’t he know anything?*

*Why is that unorthodox bastard staring at me? Is he finally looking for a real fight?*

*Good heavens. I thought I’d finally gained an adorable, sweet granddaughter in my old age. How did things end up like this? Well, dismembering someone into five pieces is a bit much. I should look for some poison like that girl suggested.*

*Taishan wants more ointment. It was quite a delicacy.*

*These damn people don’t care that I’m hurt at all. And what does she mean, the Sichuan Tang Clan? What the hell happened?*

Of course, not one bit of communication passed between them, but everyone except Ju Hwaran reached an unspoken agreement.

Until the mood settled down a bit, they’d keep their mouths shut.

It wasn’t until Ju Hwaran’s stiff face softened that Hyuk Mujin, who’d been furtively checking the others’ expressions while applying ointment himself, was able to hear what had happened.

“Wait, two days have passed?”

Ju Hwaran nodded.

“Yes. Exactly two days.”

“Then this really is…”

“As I said earlier, we’re at the Sichuan Tang Clan. To be more precise, we’re in the Medical Hall in the Outer Court.”

Hyuk Mujin just blinked blankly.

He couldn’t believe it. He’d only taken a nap and woken up, but two days had passed—and he’d opened his eyes in the Medical Hall of the Sichuan Tang Clan.

“What on earth happened?”

“Young Hero Hyuk, you don’t remember anything?”

“No. I only remember what the Captain and the Huang tribe member were saying at the river landing. After that, there was a flash before my eyes.”

Song Ilseom, leaning against the wall at an angle with his arms crossed, muttered:

“You remember that much.”

“What? Was that all?”

“Yes. In fact, none of us really saw what happened.”

Sama Pyo nodded without realizing it, then added:

“It was astonishingly fast. I’d never seen a punch that quick. Something blurred, then there was a sound like a drum bursting, and you fell over. That’s all.”

“Lord is wrong. That’s not all. Taishan saw everything, from beginning to end.”

Taishan abruptly cut in, his body shivering as he continued.

“Pavilion Master. Beat Hyukmu. Beat him a lot. Really fucking beat him.”

“……”

“Pavilion Master. Hyukmu already down. Stomped on him. Like mincing meat, stomped him over and over. Ah, Taishan wants meat.”

“……”

“Oh, the Pavilion Master tried to stomp on his pepper, too, but people stopped him. Taishan helped stop him. No one should do that. Ah, Taishan wants Sichuan-style five-spice pork with lots of pepper.”

Namho, puffing on his long-stemmed tobacco pipe in a corner of the Medical Hall, groaned.

“Goddamn it, I told you we should just dismember him into five pieces.”

“Taishan doesn’t know what that is. Namho know?”

“I do. You tie bastards like a certain someone to oxen or horses, then tear their arms and legs right off…”

“Oh! Then Taishan gets the leg meat!”

Crack.

Namho snapped his pipe in two and charged at Taishan with a roar like a wild beast.

Ju Hwaran sighed as she watched Sama Pyo hold him back while he struggled, then spoke.

“Anyway, that’s what happened. That part is safe, so there’s no need to check it right now.”

Taking advantage of the brief commotion, Hyuk Mujin had hurriedly checked that his most important parts were safe. He answered weakly.

“That’s a relief. Where’s the Captain?”

“He’s with Great Hero Jeok.”

“What? For two whole days?”

“Yes. It seems they had a lot to talk about. I don’t know exactly what.”

“But they were together not long ago. What could they possibly have to talk about for two days?”

“They haven’t said anything, so we can only guess. I did hear the Divine Physician is making a pill for the Pavilion Master. Perhaps they haven’t just been talking—maybe they’ve been making preparations to help the Pavilion Master recover.”

At Ju Hwaran’s reasonable guess, Hyuk Mujin nodded.

“Fair enough. He didn’t come back from some far-off foreign land, after all. How much could they have to talk about? Right, everyone?”


* * *


When you return from somewhere far away, you have a lot to talk about.

Especially if all kinds of unimaginable things are happening in that faraway place.

After I’d told Jeok Cheongang my endless story, he stayed silent for a long while. Then he summed up his thoughts in a single, short, blunt remark.

“We’re fucked.”
```
