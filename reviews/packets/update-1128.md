<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1128.txt",
      "sha256": "d27ec32a8d9721c308bdf8b8155236d917a9f73df0cf90159049c050700d4ef2",
      "bytes": 13691
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "257038d591948062d1f98e79dd51c812487ebffa44141073c785e9525b5c534e",
      "bytes": 861
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "307189767337c5394589bdcaa7f59f3e28cdf1da9d380fecae4d63447025be4b",
      "bytes": 245178
    },
    {
      "path": "characters/Cheongheoja.md",
      "sha256": "38ed7e798ebfcc3ed96e12137c54bb32d14bbc5a2e7800d579efa5bfa98850fe",
      "bytes": 649
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "d0f5f822e3078f6efa3447edc14450c17b9c130f376cd25da5f8eb12946db4e5",
      "bytes": 1230
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "1d2a03a7584cbfc7ee7ccb54e7b3381934d292447c168f08d22e36a57bffe528",
      "bytes": 670
    },
    {
      "path": "characters/Hak Eui.md",
      "sha256": "138c9c57f577e82c05958450bb1c5d24beca4e0dd404741487180b1181f778ec",
      "bytes": 554
    },
    {
      "path": "characters/Hong Dao.md",
      "sha256": "9550c8c56c403545d561c7080421429caf429995565db522a7ad08ab44a0e60c",
      "bytes": 1001
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "e45de9bffed23c1257b246d51b896f0b39f4a30270c4c7578cdbb2917070285f",
      "bytes": 1357
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "1cb77a1fbee9dc659f792b47d25e1e7c3f27557b590d7a72e734bf6063b7c9c9",
      "bytes": 1513
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "135e40bdc9453196517cdfc2acf2b191299c981221c5c388dfd72ef49cb70f8b",
      "bytes": 1828
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "f024c137eb23336728e344385785aed6f28e8d31fe65767553147ba037efb6f4",
      "bytes": 623
    },
    {
      "path": "characters/Ju Hwaran.md",
      "sha256": "7ac78f265d9a40216273ce32345dd2e4653ce66bf8de0e36e9b1579dbec30d82",
      "bytes": 974
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "97b88deddd5bf23fb09c6ad877b3b81f203626e95fe7ab88d518c9aaff0afcb0",
      "bytes": 1084
    },
    {
      "path": "characters/Martial God.md",
      "sha256": "d5da37c789b27529dc461f035d059c160cf0998d00bfbce0a1d19731946b72f9",
      "bytes": 779
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "eee8b3f4c25be2fe017db0fb1ef8256bed1cc7ddcbf89d46e493ef306f12ceb1",
      "bytes": 1042
    },
    {
      "path": "characters/Sama Pyo.md",
      "sha256": "e9ea7e9eec8c907ebf0e3eb1861fc9459245334d2a6a1e0fdd310d408bbef865",
      "bytes": 850
    },
    {
      "path": "characters/Song Il.md",
      "sha256": "b382945f26b5230fd48b45cffb0f6e1c5a57d24918c1eb9e80a674cc6380f2e2",
      "bytes": 774
    },
    {
      "path": "characters/Song Ilseom.md",
      "sha256": "3eb5b3e428ea1b4bff8d211a81c9820a37acfbd79336cda31fd5be9346c4d9d6",
      "bytes": 980
    },
    {
      "path": "characters/Taishan.md",
      "sha256": "a27256bc3e09d86c662ecacb6b8006cccb3893dfec2a59d30408ac8c957079f7",
      "bytes": 686
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a5d3d61e2339d630995f6a706169bc5f6be7b39afba1c4ffd564f089037b1146",
      "bytes": 290077
    }
  ],
  "estimated_tokens": 16948
}
-->

# Durable State Update — Chapter 1128

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
1 and safe_through 1128. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1128. Profile updates may replace only one
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
  "chapter": 1128,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1128,
    "continuity_sources": [1128],
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
    "The Blood Lord is dead, and the Dark Heaven army has collapsed.",
    "The Murim Alliance and its allies have surrounded the battlefield.",
    "Jeok Cheongang blocked the Blood Lord’s final attack on Taekyung.",
    "Taekyung’s innate qi is irreversibly damaged; his Final Rally has 5 minutes 35 seconds remaining after the Level Ups.",
    "Taekyung believes he is going to die and is preparing to say goodbye to his remaining companions.",
    "Taekyung and Cheongpung exchanged a brief farewell."
  ],
  "continuity_sources": [
    1127
  ],
  "open_questions": [
    "Will Taekyung survive the damage to his innate qi and the end of Final Rally?",
    "What will happen to the battlefield and the allied forces now that the Blood Lord is dead?"
  ],
  "safe_through": 1127,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 송일     | **Song Il**        |
| 굉도     | **Hong Dao**       |
| 주화란    | **Ju Hwaran**      |
| 쾌풍검    | **Swift Wind Sword**          | Hyuk Mujin     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 무신     | **Martial God**               | —              |
| 궁성     | **Bow Saint**                 | —              |
| 살성     | **Slaughter Saint**           | —              |
| 해상왕    | **Seafaring King**            | Pa Ryun        |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 상태               | **Status**                     |
| 정마대전   | **Great Faction War**         |
| 노부      | **this old man / I**                                            |
| 방장      | **Abbot**                                                       |
| 청허자 | **Cheongheoja** | Kunlun Sect Leader. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 학의 | **Hak Eui** | Kunlun Sect First-Generation Disciple. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 사마표 | **Sama Pyo** | Young Sect Leader of the Black Dragon Demon Gate. |
| 송일섬 | **Song Ilseom** | Young escort captain of the Yongbong Escort Bureau; distinct from Song Il of Zhongnan. |
| 태산 | **Taishan** | Sama Pyo's giant subordinate. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 평화 | **Peace Guild** | Guild name. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 화룡 | **fire dragon** | Fire-dragon image within Taekyung's dantian that awakens before the duel. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 화란 | **Hwaran** | Familiar short form of Ju Hwaran. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 사혈 | **lethal acupoint** | An acupoint whose strike can kill. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 무한 | **Wuhan** | Capital of Hubei Province near Dongting Lake. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 녹림투왕 | **Green Forest Battle King** | Epithet of the Green Forest Alliance Leader, distinguished from the Ten Kings. |
| 화룡각 | **Fire Dragon Pavilion** | New name chosen for Taekyung's pavilion. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 선계 | **realm of immortals** | The other world that Jin travels to and from. |
| 십만마도 | **Hundred Thousand Demonic Disciples** | The earlier force used as a comparison for Dark Heaven’s army. |
| 대인 | **Great Sir** | Name used for the mysterious figure in Ningxia. |
| 서녕 | **Xining** | Capital of Qinghai. |
| 창도 | **Chamdo** | Town named as the site of Songhak’s inn stay. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 송일 | 진태경 | hostile Zhongnan Elder to accused outsider | you / Jin Taekyung | hostile and threatening | Song Il questions Taekyung's identity and later threatens him over Gong Ilhyuk's injury. |
| 송일 | 청풍 | hostile Zhongnan Elder to younger martial artist | Sword Saint's heir / you | hostile and threatening | Song Il identifies Cheongpung as the Sword Saint's heir and demands that he face the consequences of injuring Gong Ilhyuk. |
| 송일 | 적천강 | former rescued junior to former rescuer | Great Hero Jeok | formal, fearful, and defensive | Uses 적 대협 while insisting that Jeok has no business interfering in the dispute. |
| 적천강 | 송일 | former rescuer to former rescued junior | Zhongnan brat; you; insolent bastard | blunt, mocking, and humiliating | Jeok recalls Song's youthful arrogance and addresses him with contempt while publicly disciplining him. |
| 적천강 | 굉도 | old_friends | Hong Dao | familiar and teasing | Uses Hong Dao's personal name in their casual reunion. |
| 굉도 | 적천강 | old_friends | Fire Gate Sect Leader | familiar and teasing | Teases Jeok as the carefree Fire Gate Sect Leader. |
| 굉도 | 진태경 | senior_monk_to_guest_benefactor | Benefactor | formal-polite and probing | Hong Dao repeatedly addresses Taekyung as 시주 while identifying him as the Master of Morning Star. |
| 궁기방 | 진태경 | rival_finalists | you bastard | insulting-casual | Gung Gibang answers Taekyung's collective insult with a profane threat. |
| 진태경 | 궁기방 | rival_finalists | you three idiots | insulting-casual | Taekyung addresses Gung Gibang as part of the trio and threatens them before a duel. |
| 매종학 | 진태경 | older_ally_to_younger_friend | friend | casual-familiar | Mae Jonghak uses 친구 when arriving at Taekyung's window and asking to talk. |
| 송일섬 | 주화란 | escort_captain_to_young_bureau_head | Hwaran | urgent and familiar | Calls out 화란아 while urgently warning Ju Hwaran before stepping into the confrontation. |
| 주화란 | 진태경 | escort_bureau_leader_to_famous_younger_martial_artist | Young Hero Jin | formal-deferential | Hwaran introduces herself as the Young Bureau Head and formally greets Taekyung as 진 소협. |
| 진태경 | 주화란 | visitor_to_young_bureau_head | Young Lady Ju | formal-polite | Taekyung uses 주 소저 while announcing that his party must leave. |
| 주화란 | 혁무진 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Mujin among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 궁기방 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Gung Gibang among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 청풍 | rescued_survivor_to_benefactor | Benefactor | formal-deferential | Hwaran includes Cheongpung among the Benefactors when greeting Taekyung's companions. |
| 주화란 | 송일섬 | bureau_head_to_escort_captain | Captain Song | formal and prosecutorial | Uses his office title, then his personal name, while exposing and confronting him. |
| 송일섬 | 궁기방 | senior_martial_artist_to_Beggars_Sect_successor | Successor Beggar | blunt and irritated | Uses 후개 while objecting to Gung Gibang’s spitting and insults. |
| 궁기방 | 송일섬 | Beggars_Sect_successor_to_young_escort_captain | Young Hero Song | casual and admiring | Uses 송 소협 while praising the famous Soul-Chasing Guest and comparing their looks. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 매종학 | 적천강 | long-standing martial rival and friend | Great Hero Jeok | casual and familiar | Mae addresses Jeok as 적 대협 while discussing the Alliance Leader position. |
| 적천강 | 매종학 | long-standing martial rival and friend | you | blunt and familiar | Jeok addresses Mae as 당신 while recalling their meeting at Mount Jiuhua. |
| 주화란 | 사마표 | former_fiancés | Young Sect Leader | formal and guarded | Hwaran formally greets her former fiancé. |
| 사마표 | 태산 | Young Sect Leader to subordinate | Taishan | informal and patronizing | Sama Pyo calls Taishan by name while ordering him to leave. |
| 태산 | 사마표 | subordinate to Young Sect Leader | Lord | crude and deferential | Taishan uses 주군 while obeying Sama Pyo. |
| 태산 | 진태경 | subordinate_to_respected_outsider | Jin Taekyung | clipped and familiar | Taishan says he likes Jin Taekyung but will fight him without hesitation if Sama Pyo commands it. |
| 청풍 | 매종학 | grandson to grandfather | Grandpa | casual-familiar | Repeatedly calls Mae Jonghak 할아버지 while mistaking the Alliance Leader's summons as a family visit. |
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
| 진태경 | 태산 | pavilion_master_to_pavilion_member | Taishan | forceful and commanding | Taekyung orders Taishan to stop eating the bear. |
| 태산 | 주화란 | Pavilion member to Pavilion member | Young Lady Ju | clipped, childlike, and deferential | Agrees with Ju Hwaran after she mentions the evening banquet. |
| 사마표 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | formal but sardonic | Sama Pyo addresses Jin as 각주 while questioning his account of the incident. |
| 태산 | 각주 | Fire Dragon Pavilion member to pavilion master | Pavilion Master | clipped, childlike, and informal | Taishan directly asks Jin whether his Lord Sama Pyo is safe. |
| 주화란 | 태산 | pavilion_member_to_pavilion_member | Young Hero Taishan | formal but stern | Ju Hwaran reprimands Taishan for speaking ominously about Jin and warns that she will muzzle him. |
| 혁무진 | 주화란 | Fire Dragon Pavilion member to fellow member | Young Lady Ju | polite and deferential | Mujin addresses Hwaran as 주 소저 while asking her to call a physician. |
| 주화란 | 적천강 | younger ally to legendary martial master | Great Hero Jeok | formal and deferential | Ju Hwaran addresses Jeok as 적 대협 while asking whether he is all right. |
| 진태경 | 상산왕 | protector addressing a young prince | His Highness | respectful royal address | Taekyung refers to the prince as 상산왕 전하 when ordering Mujin to bring him. |
| 궁성 | 진태경 | elder who spent decades searching for the chosen one | you | casual and teasing | Uses 너/널 while testing and praising Taekyung. |
| 진태경 | 궁성 | chosen one addressing the elder who sought him | you | polite, shifting to familiar-casual under stress | Begins with formal-polite phrasing, then speaks more casually as the conversation intensifies. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 살성 | 청풍 | senior martial figure to younger companion | you | blunt and familiar | The Slaughter Saint scolds Cheongpung for disappearing without a word. |
| 청풍 | 살성 | younger companion to senior martial figure | old man | polite and familiar | Cheongpung apologizes and explains why he wandered off. |
| 송일섬 | 혁무진 | Older fellow Pavilion member and martial senior | you | casual and informal | Song insists that his age and martial experience entitle him to speak casually to Mujin. |
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
| 학의 | 진태경 | Kunlun Sect disciple to renowned martial artist | Great Hero Jin Taekyung | formal and deferential | Uses 진태경 대협 when introducing himself and greeting Taekyung. |
| 청풍 | 대인 | younger companion addressing an older benefactor | Uncle Great Sir | polite and familiar | Cheongpung repeatedly calls him 대인 아저씨. |
| 대인 | 청풍 | older benefactor addressing a younger companion | you | familiar and teasing | Great Sir addresses Cheongpung as 자네. |
| 청허자 | 적천강 | younger martial artist to senior martial artist | Senior | polite | Cheongheoja refers to Jeok Cheongang as 노 선배 while politely declining his offer. |
| 궁성 | 살성 | allied martial masters | Slaughter Saint | formal-polite | The Bow Saint directly addresses him as 살성 and uses 당신 while urging him to stay and defend the South Gate. |

## Listed compact profiles

### Cheongheoja.md

# Cheongheoja (청허자)

- **Safe through:** Chapter 1120
- **Aliases:** None
- **Role:** Cheongheoja is the Kunlun Sect Leader and Hak Woo’s master.
- **Personality:** Warm, composed, and patient, he faces setbacks with resolve and receives even startling company with good humor.
- **Voice:** Measured and gentle, using formal Daoist courtesies and calm metaphors.
- **Relationships:** Hak Su and Hak Eui are his Disciples; he knows Jin Taekyung by reputation and treats him warmly; he and Tae Gunak were once fellow Daoists, but are now estranged over irreversible choices.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 1127
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, Sword Saint Mae Jonghak’s grandson and Disciple, a Supreme Peak master known as the Huashan Divine Dragon, creator of Mimi Step, and master of the Azure Dragon Pavilion; he has mastered the Slaughter Saint’s Ghost Illusory Slaughter Step and blended it with his Dark Fragrance Drift.
- **Personality:** Affable, dreamy, and childlike, with innocent curiosity, a deep love of martial arts, and compassion; guided by his grandfather’s righteousness and Taekyung’s chivalry, he meets danger with resolve and trusts Taekyung without wavering.
- **Voice:** Dreamy and hazy, with innocent, polite phrasing; he has begun imitating Taekyung's profanity.
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions; Taekyung is his true martial rival and the person whose way of life he admires, and the Slaughter Saint is his mentor in concealment and Ghost Illusory Slaughter Step.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 1120
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered, but grieves deeply for fellow Beggars’ Sect disciples and defends those who risk their lives for others.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun, and shares a blunt, teasing friendship with Taekyung.

### Hak Eui.md

# Hak Eui (학의)

- **Safe through:** Chapter 1116
- **Aliases:** None
- **Role:** Hak Eui is a First-Generation Disciple of the Kunlun Sect.
- **Personality:** Composed, observant, and assertive; he investigates matters closely and uses his standing to bring consequential findings before the leaders.
- **Voice:** Calm and formal, with measured phrasing and dry, blunt statements of fact.
- **Relationships:** He has met Jin Taekyung and respectfully addresses him as a Great Hero.

### Hong Dao.md

# Hong Dao (굉도)

- **Safe through:** Chapter 1115
- **Aliases:** Dharma King
- **Role:** Abbot of Shaolin and the Murim's Dharma King; master of Unnamed and the only friend to whom Jeok Cheongang had opened his heart; after leaving the Star-Array Grand Banquet, he was found in a massive pit with both legs severed and catastrophic internal injuries, whispered final words to Jeok Cheongang, and died.
- **Personality:** Calm, responsible, quietly playful, and still regarded by Jeok as lazy for sleeping whenever possible.
- **Voice:** Quiet, deep, weighty, and resonant, with casual familiarity when speaking to Jeok Cheongang.
- **Relationships:** Old friend of Jeok Cheongang and close friend of Peng Cheolhu; master of Unnamed; before his death, entrusted the Green Jade Buddha Staff to Unnamed, warned Jeok about Jongni Chu, Dark Heaven, Unnamed, and the Buddhist Staff, and sent Unnamed to find the Master of Morning Star.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1123
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and Vice Captain of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, whom he deeply admires, and has developed a warm friendship with fellow Fire Dragon Pavilion member Taishan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1127
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, and dryly teasing, he fears water and freely follows his own path rather than pursuing grand causes; he cares about protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, believes Taekyung’s compassion makes him worthy of being called a Great Hero, and insists on protecting him; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 1127
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan and the original owner of his current body, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master who has reached the realm of the Ten Kings as its eleventh member and can detect and eavesdrop on nearby Sound Transmissions subject to the participants’ relative levels, and a publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and fiercely defiant when others try to dictate his choices or survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Hyuk Mujin trusts Taekyung to fight beside him; Taekyung trusts Sama Pyo as a friend despite suspecting his betrayal, and values him beyond his unorthodox affiliation; Peng Cheolhu regarded Taekyung as a worthy successor, and the Bow Saint relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 1127
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ju Hwaran.md

# Ju Hwaran (주화란)

- **Safe through:** Chapter 1120
- **Aliases:** Hwaran
- **Role:** Ju Hwaran is a Level 88 Young Bureau Head, leader of the Yongbong Escort Bureau, an experienced Nanman guide, and an active member of the Fire Dragon Pavilion.
- **Personality:** Intelligent, capable, responsible, and filial; remains controlled under pressure but has grown more assertive and openly impatient after the hardships she has endured.
- **Voice:** Clear, polite, restrained, and determined.
- **Relationships:** Escort King Ju Gongsan was her paternal grandfather, Ju Hogun is her father, Heo Jun was her uncle, Sama Pyo was her former fiancé in a political engagement she accepted for her father's sake, Song Ilseom is her direct escort who accompanied her previous journey to Yeongin, and Jin Taekyung is a trusted ally; the Yongbong Escort Bureau has longstanding ties with Yeongin’s inhabitants.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 1127
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather who now serves as the New Murim Alliance's Alliance Leader and has ordered Jin Taekyung's first Fire Dragon Pavilion mission to Nanman.
- **Personality:** Playful and easygoing in ordinary company, yet guided by a principled commitment to chivalry that can outweigh strategic caution.
- **Voice:** Friendly, casually familiar, and cheerfully teasing, including when greeting old acquaintances and discussing leadership.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Martial God.md

# Martial God (무신)

- **Safe through:** Chapter 1126
- **Aliases:** None
- **Role:** An unidentified legendary martial artist regarded as a pinnacle above the Ten Kings; more than fifty years ago, he defeated five Supreme Peak fiends and five hundred Blood Ghost Squad members alone.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** He met the Beast Miao King twice more than fifty years ago, Mae Jonghak received several teachings from him, and he left the Bow Saint a letter describing a chosen one; the Bow Saint says he chose her, while his identity, whereabouts, and possible connection to Cheon Taemin remain unknown.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 941
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is the Emperor’s thirteen-year-old younger brother, an exceptionally skilled young swordsman, and the newly appointed Crown Prince.
- **Personality:** Earnest and compassionate, he takes responsibility for others’ suffering and dreams of a peaceful age founded on justice, care for the people, wise counsel, and accountability, even when doing so demands personal sacrifice.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Zhu Bao is the Emperor’s younger brother and Crown Prince, and Hong Jin has been his steadfast caretaker since childhood. He admires Jin Taekyung and calls him a friend; his compassion for the Eastern Heaven Demon Lord reflects the different path made possible by those who supported him.

### Sama Pyo.md

# Sama Pyo (사마표)

- **Safe through:** Chapter 1123
- **Aliases:** Black Dragon Saber
- **Role:** Young Sect Leader and heir of the Black Dragon Demon Gate, a Morning Star reputed to be no less than the Ten Dragons and Phoenixes.
- **Personality:** Courteous and calculating, he chooses what he believes is right over expedience and accepts responsibility for his choices, even when they expose him to blame.
- **Voice:** Polite and ingratiating in public, with sardonic humor and controlled evasiveness.
- **Relationships:** Sama Pyo is Sima Gong’s son and chosen heir, commands Taishan, and is Jin Taekyung’s friend; he deliberately let Namho suspect his father’s actions to protect their companions, was Ju Hwaran’s former fiancé, and is hostile toward Song Ilseom.

### Song Il.md

# Song Il (송일)

- **Safe through:** Chapter 1123
- **Aliases:** Roaring Fury Swordsman
- **Role:** Elder of the Zhongnan Sect, known as the Roaring Fury Swordsman and one of Sect Leader Gong Iljung’s two Senior Brothers.
- **Personality:** Arrogant and domineering, but capable of remorse over choices that harmed his sect and those he failed to protect.
- **Voice:** Gruff, cutting, condescending, and threatening, with formal authority used to pressure those beneath him.
- **Relationships:** Gong Iljung is his junior Sect Leader and martial younger brother; Gong Ilhyuk is a junior Disciple of his sect; he recognizes Baek Museong and Cheongpung through their Huashan and Sword Saint connections.

### Song Ilseom.md

# Song Ilseom (송일섬)

- **Safe through:** Chapter 1123
- **Aliases:** Escort Captain Song
- **Role:** Song Ilseom is a Level 110 escort captain of the Yongbong Escort Bureau, one of its Dragon-Phoenix Three Escorts, and a member of Jin Taekyung and Cheongpung’s Fire Dragon Pavilion.
- **Personality:** Blunt, decisive, survival-hardened, and dryly self-aware, with little patience for insults or disorder and practical survival skills such as making disguise masks.
- **Voice:** Direct and rough, with dry, matter-of-fact teasing among allies and forceful urgency in command.
- **Relationships:** He serves under Ju Hwaran and has expressed concern that she not be hurt or die needlessly; he is Song Pyosan’s son, his grandmother was the surviving Guangdong Chen child rescued by Ju Gongsan during the Great Faction War, and he remains openly hostile toward fellow Fire Dragon Pavilion member Sama Pyo.

### Taishan.md

# Taishan (태산)

- **Safe through:** Chapter 1124
- **Aliases:** Tiger Giant Child
- **Role:** Taishan is a giant subordinate of Sama Pyo in the Black Dragon Demon Gate and a member of the Fire Dragon Pavilion.
- **Personality:** Childlike, obedient, food-obsessed, and dim-witted, with intense wariness toward strangers and absolute trust in Sama Pyo; becomes explosively violent when his meat is threatened.
- **Voice:** Clipped, simple, and childlike.
- **Relationships:** He serves Sama Pyo, whom he calls Lord, trusts Jin Taekyung as Pavilion Master, and has grown attached to the Fire Dragon Pavilion members.

## Korean source

```text
＃1128화



만약 조금만 더 생각이 이어졌다면 나는 무심코 눈물을 흘렸을지도 모른다.

아직 떠날 준비가 되지 않았다는 건, 그 누구보다 나 자신이 잘 알고 있었으니까.

하지만 무한(無限)이라 여겼던 시간은 지금 이 순간에도 조금씩 끝을 향해 다가가고 있었고, 나는 애써 입꼬리를 말아 올렸다.

나를 위해서.

더불어 내 마지막 순간을 오랫동안 기억할, 남아 있을 이들을 위해서.

“어, 왔어?”

개인적으로는 매우 훌륭한 연기였다고 생각한다.

웃는 얼굴, 태연한 목소리.

다만 마침내 다시 마주한 화룡각 대원들이, 지금의 내 모습과 착 가라앉은 주변의 공기가 무엇을 뜻하는지 모를 만큼 어리석지 않았을 뿐이다.

“……각주.”

이어지는 뒷말은 없었다.

멍하니 나를 바라보던 사마표는 입술을 깨물었고, 송일섬은 조용히 눈을 감았으며, 송아지처럼 커다란 태산의 눈에는 희뿌연 습막(濕膜)이 차올랐다.

그리고 주화란은.

철벅. 철벅.

호수처럼 고인 피 웅덩이를 비틀비틀 가로질러, 잘게 떨리는 고개를 내 어깨에 묻었다.

그것이 전부였다.

더 이상의 말은 없었으나, 내게는 그것으로 충분했다.

‘살아 있었어, 모두.’

불길한 짐작은 빗나가는 법이 없었지만, 이번만큼은 예외였다.

무사한 그들의 모습을 확인하자, 경직되어 있던 입꼬리가 부드럽게 풀어지는 것이 느껴졌다.

‘다행이다. 정말…… 다행이야.’

이 순간, 내 입가에 떠오른 미소는 더 이상 연기가 아니었다.

화룡각 대원들에 이어 나타난 궁기방과 청허자.

심지어는 볼 때마다 두통을 유발하던 어느 산발괴인(散髮怪人)의 얼굴마저도 가슴 한구석이 울렁일 만큼 반가웠으니까.

아니, 어쩌면 이토록 반가운 것은 대인이 아니라 그의 등에 업혀 있는 한 사람 때문일지도 몰랐다.

“걱정하지 말게. 비록 심각한 내상을 입은 상태였으나, 해상왕이 늦지 않게 사혈(死血)을 빼냈으니 생명에는 아무런 지장이 없을 거야.”

불현듯 귓가에 내려앉는 음성에, 나는 대답 대신 작게 고개를 끄덕였다.

혁무진은 머리부터 발끝까지 피투성이가 된 채 의식을 잃은 모습이었지만, 백번 천번이고 믿을 수 있었다.

다른 누구도 아닌, 당대의 천하제일인(天下第一人)이라 불릴 만한 이의 장담이니.

“쾌풍검(快風劍) 혁무진, 실로 훌륭하게 싸웠네. 한 치의 물러섬도 없이. 당당하게.”

검성(劍星) 매종학이 나직이 덧붙였다.

“자네처럼.”

진심이 묻어 나오는 그의 한 마디에, 나는 핏물이 말라붙은 입술을 달싹였다.

“예. 분명히 그랬을 겁니다.”

그리고, 혁무진을 응시하며 흐릿하게 웃었다.

“제 오른팔이니까요.”

깊게 가라앉은 눈빛으로 나를 바라보던 매종학도, 이내 나를 따라 웃었다.

“역시, 그랬군.”

“그런데 아마 저 녀석은 모르고 있을 겁니다.” 

“어째서인가?”

“제가 늘 구박만 했거든요. 고작 그 정도로 오른팔은 턱도 없다고.”

만약 내가 회생(回生)할 수 있는 일말의 가능성이라도 남아있었다면, 매종학은 지금 이 말을 듣자마자 망설임 없이 대답했을 것이다.

나중에 직접 말해 주라고.

그럼 혁무진도 기뻐할 것이라고.

하지만 말없이 이를 악물고 있는 살성과 궁성처럼, 그 또한 내게 허락된 시간이 얼마 남지 않았음을 잘 알고 있었다.

“그가 의식을 되찾으면 전해 주겠네. 지금 자네가 했던 말을, 토씨 하나 빼놓지 않고.”

“워낙 칭찬에 굶주렸던 녀석이라, 훨씬 더 과장해 주셔도 됩니다. 이를테면…….”

문득, 한참 전에 혁무진과 나누었던 대화를 떠올린 내가 피식 웃었다.

“무림맹주(武林盟主)가 될 자질이 충분하다, 예. 그 정도면 좋아서 까무러치겠네요.”

“차기 무림맹주라, 깊이 반성해야겠군. 내 후임자를 눈앞에 두고도 못 알아보다니.”

“이번만큼은 넘어가 드리겠습니다. 대신 모두를 구하셨으니까요.”

“아니, 그 말은 틀렸네.”

툭.

단호한 음성과 함께, 매종학의 손이 내 어깨에 닿았다.

“모두를 구한 것은 내가 아니라 자네일세. 동시에 저들 자신이기도 하지.”

“……!”

“보고, 듣게. 저들이 지금 누구를 위해 싸우고 있는지, 또한 누구의 이름을 부르짖고 있는지.”

그 순간.

스아아아.

어깨에 닿은 손끝을 타고 흘러내린 따스한 기운이 몸 안으로 스며들었다.

노을을 닮은 그것은 차츰 가라앉아 가던 정신을 일깨우고. 지금 이 순간에도 산산이 허물어지고 있는 광신도들의 모습과 그런 그들을 파도처럼 휩쓸고 있는 아군의 함성을 내게 전해 주었다.

세찬 바람과 빗줄기를, 여덟 글자의 교언(敎言)마저 집어삼킨 그 거대한 외침을.

- 맞서 싸우라! 열화신룡(烈火神龍)을, 진태경을 위하여!

하늘을 찌를 듯 높이 솟은 깃발들이 어지럽게 흩날린다.

번뜩이는 강철의 숲이 성내를 뒤덮고, 붉은 꽃을 피워 올리며 전진한다.

무림인, 관군, 양민.

물과 기름처럼, 어울리지 않는 세 가지 색이 하나로 뒤섞인 채 침략자들을 관통하고 있었다.

모두가 내 이름을 부르짖으며.

광신도들의 광기(狂氣)조차 지워 내는, 필사적인 의지와 결의로.

“……!”

나도 모르게 몸이 부르르 떨렸다.

등줄기를 타고 솟구친 벼락과도 같은 전율과 함께, 매종학의 음성이 귓가로 흘러들었다.

“한 달 전 해상왕(海上王)을 설득하기 위해 찾아갔을 때, 그는 말했네. 풍랑이 휘몰아치는 밤에는 배를 띄울 수 없다고. 돛과 노는 부러지고, 빛 한 점 보이지 않아 어디가 앞이고 뒤인지조차 분간할 수 없을 것이라고.”

마침내 찾아온 전란(戰亂)의 시기.

지난 오십여 년간 찬란하게 천하를 비추었던 평화의 태양은 어느덧 자취를 감추었고, 암천이라는 먹구름과 함께 찾아온 밤은 칠흑처럼 깊었다.

천마(天魔)를 중심으로 한 십만마도와도 맞서 싸웠던, 흑도의 두 거인마저 마음이 흔들릴 만큼.

“그와 같은 말을 한 것은 녹림투왕(綠林鬪王) 역시 마찬가지였네. 그들은 분명 암천의 힘을 두려워하고 있었고, 이미 오래전부터 내부에 심어져 있던 간자들은 굴복을 통한 생존을 제의했었지.”

그러나 지금, 내 시야에 들어온 광경은 정반대였다.

콰드드득!

멀리서도 알아볼 수 있을 만큼 강렬하게 번뜩이는 붉고 푸른 두 줄기의 강기.

광신도들을 무참히 도륙하며 나아가는 그 거대한 기운의 중심에는, 천하의 강산을 지배하는 두 초절정 고수가 있었으니까.

“그래, 나는 결국 그들을 설득할 수 있었네. 그리고 그건 생각보다 쉬웠어.”

“도대체 어떻게.”

“정마대전(正魔大戰) 때와 같았지. 저들에게는 단지 우리를 믿고 함께 나아갈 수 있는, 한 줄기 빛과도 같은 이가 필요했을 뿐이니.”

나는 모른다.

이미 아득한 세월에 흘러 지나가 버린 그 과거의 시간을.

하지만, 그럼에도 불구하고 충분히 짐작할 수 있었다.

정마대전이라는 어둠을 밝혔던 빛의 정체를.

일순간 나도 모르게 눈이 부릅떠진 것은, 아마도 그런 이유에서였을 것이다.

전란의 시기를 밝힌 그 찬란한 빛은, 이미 자취를 감춘 지 오래였으니까.

“……설마.”

나는 빙긋 웃고 있는 매종학을 바라보며, 신음하듯 물었다.

“그가, 무신(武神)이 돌아온 겁니까?”

그리고 다음 순간 이어진 매종학의 대답에, 나는 가슴 깊은 곳에서 울컥 솟아오르는 뜨거운 무언가를 느꼈다.

“아니, 하지만 자네가 있었지.”

“……!”

“누구보다 앞서 나아가 등불을 밝히는 이. 신분의 고하와 그 어떤 격식에도 얽매이지 않기에 모두를 하나로 이을 수 있는 자. 하여 열화신룡이며 상산왕, 그 이전에 한 사람의 인간이라.”

시를 읊듯 뇌까린 음성이 전장 곳곳으로 퍼져나간다.

동시에 헤아릴 수 없을 만큼 수많은 발걸음이 침략자들이 만들어낸 피 웅덩이를 짓밟고, 눈부신 창칼이 어둠을 밝혔다.

어둠도, 내 안의 불꽃도 서서히 꺼져 간다.

그러나 함성은 꺼지지 않았다.

서녕의 모든 이가, 지금 이 순간에조차 목청이 터지도록 내 이름을 부르짖고 있었다.

마치 코앞에 닥친 내 죽음을 애도하듯.

“고마웠네. 그리고 미안하네. 너무 늦게 와 버려서. 자네를 지켜 주지 못해서.”

청풍과 비슷한 말을 하며, 똑같은 모습으로 눈물을 흘리던 매종학은 곧 나를 두고 돌아설 수밖에 없었다.

그는 맹주니까.

이 빌어먹을 전투를 촌각이라도 앞당겨 마무리 짓고, 한 사람이라도 더 많은 목숨을 구할 의무와 책임이 있었으니까.

아니.

어쩌면 그것은 나름의 배려였을지도 모르겠다.

몸도 마음도 얼어붙은 듯, 몇 걸음 뒤에서 모든 것을 그저 말없이 지켜만 보고 있었던 누군가를 위한 배려.

“무엇이 그리 즐겁더냐.”

화왕(火王)이라는 별호가 무색하게 느껴질 만큼 차가운 음성.

하지만 그러한 분노가 적천강 자신을 향한 것임을, 나는 누구보다 잘 알고 있었다.

마음속으로는 피눈물을 흘리고 있을 그를 위해 웃는 것만이, 내가 할 수 있는 유일한 도움이라는 사실 역시도.

“아니, 제 맘대로 웃는 것도 못합니까?”

“억지인 거, 티 난다.”

“……많이 나요?”

“그래. 지금 네놈 꼴을 봐라.”

“저야 못 보죠. 거울이라도 가져다 주시든지.”

“꼭 봐야 알겠느냐? 머리부터 발끝까지 피투성이가 된 몰골로 웃으니 흉신악살이 따로 없다.”

“뭐, 남말 하실 처지는 아니신 것 같은데.”

적천강과 나는 침묵했다. 

그리고 마치 약속이라도 한 것처럼 동시에 웃었다.

그것만이 서로의 마음을 조금이나마 위로해 주리라는 사실을 알고 있었으니까.

물론, 그마저도 우리는 상대의 눈빛을 통해 깨닫고 있었다.

“억지로 웃는 거, 확실히 티가 나네요.”

“쉽지 않군.”

“예. 쉽지 않네요. 돌이켜 보면 모든 것이 늘 그랬어요.”

나는 힘없이 중얼거리며 적천강을 바라보았다. 

어느 방향으로 고개를 돌려도 시야 한구석에서 사라지지 않는, 반투명한 홀로그램 창도 함께.



제한 시간 : 59초



“노야.”

“말하거라.”

“혹시, 저승이라는 게 정말 있을까요?”

“있을 것이다. 아니, 분명히 존재한다.”

“어떻게 아세요?”

“굉도, 그놈이 그렇게 말했으니까. 그 대단한 소림사 방장이 하는 말이니 네놈도 군말 없이 믿어라.”

“참 나, 평소에는 늘 땡중이라고 무시하셨으면서.”

“이번만큼은 믿어 볼 작정이다.”

“왜요?”

“……저승이 있어야 우리가 다시 만날 날도 있지 않겠느냐.”



제한 시간 : 30초



“한참 뒤에 만나도 괜찮으니까, 가급적이면 늦게 오세요.”

“그렇지 않아도 시간이 제법 걸릴 것이다. 죽여야 할 놈들이 한 둘이어야 말이지.”

“듣고 보니 그렇네요. 듣다 보니 좋은 계획이 생각났어요.”

“무엇이냐.”

“그 씹새끼들 죽이시면, 제가 기다리고 있다가 저승에서 한 번 더 죽이겠습니다.”

“불가.”

“아니, 어째서요?”

“네놈은 딱 죽을 때까지만 두들겨 패 놔라. 그래야 노부랑 같이 한 번 더 죽일 것이 아니냐.”

“이야, 천재십니까?”

“천재지변에 가까웠던 것 같긴 하구나.”



제한 시간 : 15초



“그런데, 노야.”

“응?”

“저 조금 졸린 것 같아요.”

“……그래, 많이 피곤하겠지.”

“죄송한데, 부탁 하나 드려도 될까요.”

“들어주마. 무엇이든.”

“제 가족들이 있어요. 여기에는 없는. 그래서 지금은 못 볼 것 같아요.”



제한 시간 : 10초



“혹시, 아마도 그럴 일은 없겠지만 만약 나중에 만나게 되면 제 소식 좀 전해주실래요?”

“네가 머무르던 그 선계(仙界)에 가려면 노부가 어떻게 해야 하느냐?”

“글쎄요. 우화등선(羽化登仙)? 저도 잘 모르겠네요.”

“알겠다. 무슨 수를 써서라도, 내 방법을 찾아낼 것이다. 허나 네놈도 노부의 부탁을 들어주어야 한다.”

“말씀하세요.”



제한 시간 : 5초



나는 힘없이 눈을 깜빡였다.

흐릿해지는 시야 너머로, 어린아이처럼 울고 있는 적천강의 얼굴이 비치고 있었다.

“제발…… 살아 줄 수는 없겠느냐.”

나는 짓쳐드는 어둠을 느끼며, 대답했다.

“죄송해요. 스승님.”



제한 시간 : 1초



그리고, 나를 둘러싸고 있던 모든 세상이 닫혔다.
```

## Final English reading copy

```markdown
# Chapter 1128

If I’d let myself think for just a little longer, I might have started crying without meaning to.

I knew better than anyone that I wasn’t ready to leave yet.

But the time I’d thought was endless was inching toward its end even now, and I forced the corners of my mouth upward.

For my sake.

And for the sake of those who would remain, and remember my final moments for a long time.

“Oh, you’re here?”

Personally, I thought it was a very convincing performance.

A smiling face. A calm voice.

But the Fire Dragon Pavilion members, reunited with me at last, weren’t foolish enough to miss what my condition and the heavy silence around us meant.

“……Pavilion Master.”

There was nothing more to say.

Sama Pyo stared at me blankly, then bit his lip. Song Ilseom quietly closed his eyes, and a cloudy film of tears welled in Taishan’s enormous eyes.

And Ju Hwaran—

*Squish. Squish.*

She staggered across the pool of blood spread like a lake and buried her trembling head against my shoulder.

That was all.

There were no more words, but it was enough for me.

*They’re all alive.*

My ominous hunches were never wrong, but this time, they’d been the exception.

As I confirmed they were safe, I felt my stiffened smile soften.

*Thank God. Really…… thank God.*

The smile on my lips now wasn’t an act anymore.

Gung Gibang and Cheongheoja appeared after the Fire Dragon Pavilion members.

Even the face of that wild-haired weirdo who gave me a headache every time I saw him made my heart swell with relief.

No—maybe it wasn't Great Sir himself I was so glad to see, but the person on his back.

“Don’t worry. He suffered a serious Internal Injury, but the Seafaring King got the stagnant blood out in time. His life isn’t in danger.”

At the voice that suddenly reached my ears, I gave a small nod instead of answering.

Hyuk Mujin had lost consciousness, covered in blood from head to toe, but I could trust those words a hundred times over.

They came from none other than a man worthy of being called the greatest under heaven in this age.

“Swift Wind Sword Hyuk Mujin fought magnificently. He never gave an inch. He stood his ground with pride.”

Sword Saint Mae Jonghak added in a low voice.

“Just like you.”

At the sincerity in his words, I parted my blood-crusted lips.

“Yes. I’m sure he did.”

I looked at Hyuk Mujin and smiled faintly.

“He’s my right arm, after all.”

Mae Jonghak had been watching me with a deeply solemn gaze. Then he smiled along with me.

“So that’s how it is.”

“But he probably doesn’t know.”

“Why not?”

“I was always giving him a hard time. Told him he wasn’t nearly good enough to be my right arm.”

If there’d been even the slimmest chance I could recover, Mae Jonghak would’ve answered without hesitation.

*Tell him yourself when you get the chance.*

*Hyuk Mujin would be happy to hear it.*

But like the Slaughter Saint and Bow Saint, who stood with clenched jaws, he knew I didn’t have much time left.

“When he wakes, I’ll tell him. Every word you just said. I won’t leave a thing out.”

“He’s so starved for praise that you can exaggerate all you like. Like……”

A conversation I’d had with Hyuk Mujin a long time ago came to mind, and I let out a quiet laugh.

“He has what it takes to become the next Alliance Leader. Yeah. That’d make him faint with joy.”

“The next Alliance Leader, you say? I have much to reflect on. To have my successor right in front of me and not recognize him.”

“I’ll let it slide this time. You saved everyone, after all.”

“No. That’s not right.”

*Tap.*

With a firm voice, Mae Jonghak placed a hand on my shoulder.

“It wasn’t me who saved everyone. It was you. And them, too.”

“……!”

“Look. Listen. See who they’re fighting for—and whose name they’re shouting.”

At that moment—

*Fwoooosh.*

Warm energy flowed from the tips of his fingers resting on my shoulder and seeped into my body.

Like the sunset, it roused my consciousness as it sank into darkness, showing me the fanatics crumbling apart and the shouts of our allies sweeping over them like a wave.

A roar that swallowed the fierce wind, the rain, and even the eight-character maxim.

—Fight back! For the Blazing Flame Divine Dragon, Jin Taekyung!

Banners soared so high they seemed to pierce the sky, whipping wildly in the wind.

A forest of glittering steel covered the city and advanced, raising red flowers as it went.

Murim warriors, government troops, and commoners.

Three forces as incompatible as water and oil had blended into one, piercing the invaders.

Everyone was shouting my name.

With a desperate will and resolve that drowned out even the fanatics’ madness.

“……!”

My body trembled before I knew it.

As a bolt of lightning-like shiver ran up my spine, Mae Jonghak’s voice drifted into my ears.

“A month ago, when I went to persuade the Seafaring King, he told me that ships couldn’t sail through a storm. The sails and oars would break, and there wouldn’t be a single glimmer of light. You wouldn’t even know which way was forward or back.”

At last, the age of war had come.

The sun of peace that had shone brilliantly over the land for more than fifty years had disappeared, and night had fallen with the dark clouds of Dark Heaven, black as pitch.

The darkness was deep enough to shake even the two giants of the dark path, who had once fought the Hundred Thousand Demonic Disciples led by the Heavenly Demon.

“The Green Forest Battle King said much the same thing. They were afraid of Dark Heaven’s power, and spies planted in their ranks long ago had urged them to submit in order to survive.”

But what I saw now was the exact opposite.

*KRA-DRRRK!*

Two streaks of red and blue Force flashed so fiercely I could make them out even from here.

At the heart of those vast energies, cutting down fanatics without mercy, were two Supreme Peak masters who ruled the mountains and rivers of the land.

“Yes, I did manage to persuade them. And it was easier than I expected.”

“How on earth?”

“It was just like the Great Faction War. All they needed was someone to believe in, someone who could move forward with them—a single ray of light.”

I didn’t know.

That past had long since faded into the distant years.

And yet, I could still guess.

I knew what light had shone through the darkness of the Great Faction War.

That was probably why my eyes widened without my meaning to.

That brilliant light, which had illuminated an age of war, had disappeared long ago.

“……No way.”

I looked at Mae Jonghak, smiling faintly, and asked as if groaning.

“Has the Martial God returned?”

At his answer, a hot, sudden swell rose from deep in my chest.

“No. But you were here.”

“……!”

“One who goes ahead of everyone else to light the way. Someone who can bring everyone together because he isn’t bound by status or formality. That’s why you are the Blazing Flame Divine Dragon and Prince Shangshan—but before either of those, you’re a human being.”

His voice, reciting the words like a poem, spread across the battlefield.

At the same time, countless footsteps trampled through the pools of blood left by the invaders, and dazzling spears and blades lit up the darkness.

The darkness was fading.

The flame inside me was fading, too.

But the shouting didn’t stop.

Everyone in Xining was still screaming my name until their voices broke.

As if mourning my death, just around the corner.

“Thank you. And I’m sorry. For coming too late. For failing to protect you.”

Mae Jonghak said much the same thing as Cheongpung had, and cried in the same way. Then he had no choice but to turn away from me.

He was the Alliance Leader.

He had the duty and responsibility to end this damn battle even a moment sooner and save as many lives as he could.

No.

Maybe he was sparing someone.

Someone who stood a few steps behind me, frozen in body and spirit, silently watching everything.

“What’s so amusing?”

His voice was so cold it seemed at odds with his title, the Fire King.

But I knew better than anyone that his anger was aimed at himself.

And I knew that the only help I could offer him, as his heart bled tears, was to smile.

“What, I’m not even allowed to smile when I feel like it?”

“I can tell you’re forcing it.”

“……Is it that obvious?”

“Yeah. Look at the state you’re in.”

“I can’t see myself. Why don’t you bring me a mirror?”

“Do you need one? You’re covered in blood from head to toe, grinning like some evil spirit.”

“Like you’re in any position to talk.”

Jeok Cheongang and I fell silent.

Then, as if we’d planned it, we smiled at the same time.

We knew it was the only thing that might comfort each other, even a little.

Of course, we could tell from each other’s eyes that it was forced.

“I can definitely tell you’re forcing that smile.”

“It isn’t easy.”

“No. It isn’t. When I look back, nothing ever has been.”

I murmured weakly and looked at Jeok Cheongang.

The translucent hologram window was still there in the corner of my vision, no matter which way I turned my head.

> **System**
> **Time Limit:** 59 seconds

“Old Master.”

“Speak.”

“Do you think there really is an afterlife?”

“There must be. No—there definitely is.”

“How do you know?”

“Hong Dao said so. The great Abbot of Shaolin Temple said it, so you’d better believe him without arguing.”

“Come on. You’re always dismissing him as a drunken monk.”

“This time, I’ll choose to believe him.”

“Why?”

“……There has to be an afterlife for us to meet again.”

> **System**
> **Time Limit:** 30 seconds

“I don’t mind if it takes a long time. Just try to take as long as you can.”

“It’ll take quite a while regardless. There are too many people I need to kill.”

“Now that you mention it, you’re right. You know, that gives me an idea.”

“What is it?”

“Once you’ve killed those sons of bitches, I’ll be waiting in the afterlife. I’ll kill them one more time.”

“Unacceptable.”

“What? Why not?”

“You only need to beat them to within an inch of their lives. Then we can kill them together once more.”

“Wow. Are you a genius?”

“I suppose I was close to a natural disaster.”

> **System**
> **Time Limit:** 15 seconds

“By the way, Old Master.”

“Hmm?”

“I think I’m getting sleepy.”

“……Yeah. You must be exhausted.”

“I’m sorry, but could I ask you for one favor?”

“I’ll grant it. Anything.”

“I have a family. They’re not here. So I don’t think I’ll get to see them now.”

> **System**
> **Time Limit:** 10 seconds

“If you happen to meet them someday—though I know that probably won’t happen—could you tell them how I’m doing?”

“What must this old man do to reach the realm of immortals where you once stayed?”

“I’m not sure. Ascend to immortality? I don’t really know.”

“Understood. I’ll find a way, whatever it takes. But you must grant this old man one favor in return.”

“Tell me.”

> **System**
> **Time Limit:** 5 seconds

I blinked weakly.

Beyond my blurring vision, I saw Jeok Cheongang crying like a child.

“Please…… can’t you stay alive?”

As the darkness swept toward me, I answered.

“I’m sorry, Master.”

> **System**
> **Time Limit:** 1 second

And then the entire world surrounding me closed.
```
