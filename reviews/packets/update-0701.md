<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0701.txt",
      "sha256": "34542203f73ad8303300db807c4ab175e35f1a66bf1a8599b7a035b386cf3a9d",
      "bytes": 12872
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ba6888bbb696efbf412242c65967dee63b489ba75dce1bed0ef7187abfcc9502",
      "bytes": 2187
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "b692e6c1c95949375957ebd4a1696a83b8ec456ca92678c22b38b1d7d70fe36b",
      "bytes": 205908
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "2db120b07e763c933f129bbe04d9192b77f7179107c4f3398fe54091bafd7246",
      "bytes": 781
    },
    {
      "path": "characters/Blood Lord.md",
      "sha256": "aa4bb3d522ca0d79f910a7d7926666aebafe1b0006da793798371be167e4954a",
      "bytes": 830
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "492537252bc8871ad3c03e4648652ae48375f74e7aa7717d193fb5a88de5d525",
      "bytes": 553
    },
    {
      "path": "characters/Great Snow Fiend.md",
      "sha256": "035fb34fce9fd47c17e1d9a755b4329578c829998d678a0c30b78b09bb669cca",
      "bytes": 898
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "933b46145883b9638f5f6064aca06f515fca8be46a7226dcffbe79b266fb2af9",
      "bytes": 1702
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "8d55ddf23ceec2789a31b8cb28ba1687ef476ee293e1e6e4fafde36dbbcc715b",
      "bytes": 1931
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "375bdaf9ffd3eb7649c1e80eb461a2e2a90eebfda927ab43ea8c8fbcd0d41164",
      "bytes": 622
    },
    {
      "path": "characters/Southern Heaven Demon Empress.md",
      "sha256": "d3f2d007f326e0c640d41d34f0ebc829d2b9535f0fe6914cac7ec5385041c779",
      "bytes": 815
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "39588518517f0306c0f8c6983a12c725399d58da9336fd2022f2fd66d620875e",
      "bytes": 216408
    }
  ],
  "estimated_tokens": 12007
}
-->

# Durable State Update — Chapter 701

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 701. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 701. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
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
  "chapter": 701,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 701,
    "continuity_sources": [701],
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
    "The rift's magical power is spreading through the collapsing Inner Palace and can mutate humans and beasts into monsters.",
    "Jin Taekyung has left the Guardian Spirit temporarily to protect the remaining humans and beasts from the magical power.",
    "Jin can sense the invisible grain or flow within objects and energies after reaching the Supreme Peak realm.",
    "A masked man serving the Southern Heaven Demon Empress uses dark Force, a sword, twin wheels, and overwhelming speed and destructive power.",
    "Jin stabbed the masked man through the chest, crushed one arm, and struck him with the Flame Divine Palm, but the masked man survived and threw the dagger back.",
    "Jin's left hand is badly torn and injured, though it remains usable.",
    "Jin suspects the masked man's twin wheels indicate a relationship with the Great Snow Fiend, but the masked man's identity and connection remain unknown.",
    "The Southern Heaven Demon Empress describes the masked man as her hunting dog and says she trained him carefully.",
    "The Guardian Spirit is badly wounded and exhausted while continuing its confrontation with the Southern Heaven Demon Empress."
  ],
  "continuity_sources": [
    700
  ],
  "open_questions": [
    "What is the masked man's identity, and what is his relationship with the Great Snow Fiend?",
    "Can Jin protect the remaining humans and beasts from the spreading magical power and prevent the planned slaughter?",
    "Can the wounded Guardian Spirit survive its confrontation with the Southern Heaven Demon Empress?",
    "Can Jin continue fighting effectively with his injured left hand?"
  ],
  "safe_through": 700,
  "temporary_decisions": [
    "Use magical power for 마력 and demonic qi for 마기 when the source distinguishes the terms.",
    "Use grain for 결 when Jin describes the invisible flows and gaps within things.",
    "Use masked man for 복면인 and leave his identity and relationship to the Great Snow Fiend unresolved.",
    "Retain Flame Divine Palm for 화염신장, White Flame for 백염, Fire Dragon Armor for 화룡갑, and Supreme Peak for 초절정."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 십왕     | **Ten Kings**       |
| 열화문    | **Fire Gate Clan**               |
| 소림     | **Shaolin**                      |
| 암천     | **Dark Heaven**                  |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 하남     | **Henan**              |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 혈주 | **Blood Lord** | Title of the unidentified young man encountered by Han Su. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 대설귀 | **Great Snow Fiend** | Fiend who ruled Great Snow Mountain and killed Baekhwi and Venerable Wusang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 염화일로 | **Flamefire Path** | Fire Gate Clan signature movement technique; Jeok Cheongang has reached its ninth stage. |
| 천주 | **Lord of Heaven** | Authority invoked by the masked attackers. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 지풍 | **Finger Qi** | Invisible qi attack fired by the Western Heaven Demon Lord. |
| 호북성 | **Hubei Province** | Province where the chapter’s Dark Heaven incidents occurred. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 내궁 | **Inner Palace** | The inner compound of the Nanman Beast Palace. |
| 마후 | **Demon Empress** | Title used for the Southern Heaven Demon Empress. |
| 수호령 | **guardian spirit** | Ancient title for the Black Tiger. |
| 균열 | **rift** | The dark rift opening in the cliff behind the Inner Palace. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 상인 | 적천강 | merchant_to_legendary_martial_master | Great Hero Jeok | deferential and flattering | Praises Jeok Cheongang while presenting the Poison-Averting Ring and requesting help. |
| 적천강 | 상인 | legendary_guest_to_merchant | you | blunt and transactional | Cuts off the merchant’s praise, asks his identity and origin, and accepts the gift without committing to the requested favor. |
| 혈주 | 적천강 | claimed enemy to enemy | your enemy | calm and threatening | The Blood Lord identifies himself as Jeok's enemy and claims to have killed Jeok's most precious friend. |
| 혈주 | 진태경 | hostile_opponent_to_hostile_opponent | Sleeping Dragon of Shanxi | casual, amused, and taunting | Addresses Taekyung by his established epithet while asking whether he agrees with the Blood Lord's judgment of Han Su. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 남천마후 | 진태경 | hostile_supernatural_opponent_to_young_martial_artist | Young Great Hero / Child | lighthearted and taunting | Addresses Taekyung while refusing to explain the Gate. |
| 진태경 | 남천마후 | young_martial_artist_to_hostile_demon_empress | you | hostile and determined | Promises that the Southern Heaven Demon Empress will die when they meet again. |
| 적천강 | 남천마후 | legendary_martial_master_to_hostile_demon_empress | you bitch | blunt and threatening | Threatens to punish her and Lord of Heaven. |
| 남천마후 | 적천강 | hostile_demon_empress_to_legendary_martial_master | Fire King Jeok / you | flattering and mocking | Addresses Jeok Cheongang as the Fire King while praising Lord of Heaven. |
| 혈주 | 천주 | servant_to_absolute_master | Lord of Heaven | worshipful and deferential | Blood Lord repeatedly addresses the Lord of Heaven while apologizing and receiving power. |
| 천주 | 혈주 | absolute_master_to_servant | Blood Lord | commanding and reproachful | The Lord of Heaven directly rebukes Blood Lord and then empowers him. |
| 진태경 | 야수묘왕 | younger allied master to Ten Kings elder | Great Hero Yayul | urgent and respectful | Uses 야율 대협 while warning the Beast Miao King not to enter the valley. |
| 야수묘왕 | 진태경 | senior allied master to younger allied master | you | informal and cautionary | Warns Taekyung not to lower his guard and to be careful while crossing the swamp. |
| 진태경 | 대설귀 | hostile_martial_opponents | old man | mocking, casual, and profane | Jin taunts the Great Snow Fiend while preparing to continue the fight. |
| 대설귀 | 진태경 | hostile_martial_opponent | Jin Taekyung | cold, incredulous, and confrontational | The Great Snow Fiend addresses Jin while demanding an explanation for his survival. |
| 진태경 | 수호령 | human ally to guardian spirit | guardian spirit | quiet and commanding | Jin whispers that they should go as they advance toward Baeksang. |
| 수호령 | 남천마후 | guardian_spirit_to_hostile_supernatural_opponent | you | terse, accusatory, and contemptuous | The guardian spirit tells the Southern Heaven Demon Empress that it knows her true essence and condemns her as a Fiend. |
| 남천마후 | 수호령 | hostile_supernatural_opponent_to_guardian_spirit | hideous beast | playful, taunting, and dismissive | She insults the guardian spirit while addressing it as a beast. |
| 수호령 | 진태경 | guardian spirit to human ally | Human | terse and alarmed | The guardian spirit cries out to Jin as the Southern Heaven Demon Empress sends him crashing into the ground. |
| 진태경 | 복면인 | hostile combatant to unknown hostile combatant | you | blunt, hostile, and incredulous | Jin directly questions the masked man about his identity and his relationship with the Great Snow Fiend. |

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 693
- **Aliases:** Heugung
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace and a Supreme Peak master who secretly lived for decades under Heugung's identity through the Bone-Shrinking Technique.
- **Personality:** The Beast Miao King is calculating, patient, ruthless, and willing to endanger Nanman's people to advance Dark Heaven's grand plan.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He maintained his public bond with Baeksang while secretly monitoring Baeksang and Yohi for the Southern Heaven Demon Empress, but he has now been branded a traitor, fled the Nanman Beast Palace, and disappeared.

### Blood Lord.md

# Blood Lord (혈주)

- **Safe through:** Chapter 684
- **Aliases:** None
- **Role:** Young-seeming high-ranking Dark Heaven figure who seeks Jin Taekyung, Cheongpung, and Jeok Cheongang after escaping the confrontation at Mount Song.
- **Personality:** Calm, confident, theatrically frivolous, casually cruel, and ruthlessly destructive; treats allies as disposable tools and enjoys provoking stronger opponents.
- **Voice:** Light, cheerful, and joking even while threatening or killing; turns cold and contemptuous when challenged.
- **Relationships:** He serves the Lord of Heaven alongside the Western Heaven Demon Lord, has received the Lord of Heaven's power for the coming Great War, and still seeks to kill Cheongpung, Jeok Cheongang, and Jin Taekyung.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 700
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Great Snow Fiend.md

# Great Snow Fiend (대설귀)

- **Safe through:** Chapter 700
- **Aliases:** Hanbaek (한백)
- **Role:** The Great Snow Fiend was the former ruler of Great Snow Mountain and a Supreme Peak fiend who killed Baekhwi and Venerable Wusang during the Great Faction War before Jin Taekyung killed him.
- **Personality:** The Great Snow Fiend is cold, pragmatic, controlled, proud, and unwilling to risk his life foolishly when outnumbered.
- **Voice:** The Great Snow Fiend speaks in measured, archaic, calm, and authoritative language that becomes frost-cold when challenged.
- **Relationships:** The Great Snow Fiend was an enemy of Baeksang, Baekhwi, Venerable Wusang, the Beast Miao King, and the allied Southern Army; he was senior to Black Hand and served under the Southern Heaven Demon Empress before Jin Taekyung killed him.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 682
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 699
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and the leader of the beast-army assault who continues fighting the Southern Heaven Demon Empress despite severe Internal Injury and cracked bones.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 699
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Southern Heaven Demon Empress.md

# Southern Heaven Demon Empress (남천마후)

- **Safe through:** Chapter 700
- **Aliases:** None
- **Role:** The Southern Heaven Demon Empress is Honglan, the former Lower District Sect singing courtesan, the creator of the massive rift behind Nanman's Inner Palace, and the enemy seeking to seize the Beast King Stone for the Lord of Heaven.
- **Personality:** Playful, cruel, confident, and casually dismissive of mass death and the suffering of others.
- **Voice:** Light, taunting, amused, and delighted even when discussing murder or imminent catastrophe.
- **Relationships:** She commands and advises Baeksang, treats Jin Taekyung and Yayul Cheok as expendable to the grand plan, and keeps a masked hunting dog whom she trained carefully.

## Korean source

```text
＃701화



“내 사냥개란다. 아주 공들여 길들인.”

나직하게 울려 퍼지는 남천마후의 목소리. 그와 동시에 복면인이 걸음을 내디뎠다.

저벅.

뿌옇게 내려앉은 먼지구름 사이, 나아가는 걸음에는 한 치의 흔들림도 느껴지지 않는다.

서서히 또렷해지는 복면인의 모습을 확인한 나는 신음처럼 중얼거렸다.

“……시발. 저건 또 뭐야.”

대답을 듣고자 흘린 말이 아니다. 나는 이미 이 의문에 대한 답을 알고 있으니까.

재생(再生).

그 두 글자로 지금 이 순간에도 눈앞에서 펼쳐지고 있는 저 기이한 광경을 설명할 수 있었다.

으득, 스르륵.

조각난 뼈가 붙고, 살과 피가 차오른다.

마치 살아 있는 뱀처럼 구불거리는 어둠이 복면인의 전신을 스쳐 지나갈 때마다 상처가 회복되고, 새로운 힘이 스며들고 있었다.

- 역천(逆天)의 힘…….

역천.

하늘의 뜻을, 순리를 역행하는 듯한 광경.

수호령이 한탄과 같은 의념을 흘린 그때, 회복을 끝마친 복면인이 기이하게 뒤틀린 팔꿈치를 꺾었다.

우두둑.

이미 붙어 버린 팔꿈치를 스스로 부수고, 위치를 맞춰 다시 회복한다.

엄청난 고통을 수반하는 행위임에도 눈썹 하나 까딱하지 않는 복면인의 모습에, 나는 전투 도중 느꼈던 위화감의 정체를 깨달았다.

‘저놈은, 고통을 느끼지 못한다.’

아무리 통각(痛覺)이 무딘 사람이라도 최소한의 고통은 느끼기 마련이다.

하지만 복면인은 단 한 번도 신음이나 비명을 지르지 않았다.

가슴에 비수가 박히고 팔꿈치가 으스러질 때도. 끔찍한 열기를 머금은 화염신장에 적중당했을 때도 마찬가지였다.

‘도대체 무슨 짓을 한 거지?’

어디서 무통 주사라도 맞고 왔나.

복면 위로 드러난 무감정한 눈동자를 바라보며 침음성을 삼킨 그때, 새하얗고 자그마한 누군가의 발이 축축한 흙을 밟았다.

사박.

하늘에서 땅으로. 마침내 지면 위에 사뿐히 내려앉은 남천마후가 싱긋 웃었다.

“귀신이라도 본 얼굴이네. 아니, 사실 그리 놀라진 않았겠구나? 하남에서 한 번 본 적이 있으니까.”

크르르.

낮은 울음소리와 함께, 군데군데 피로 얼룩진 거대한 동체가 지친 몸을 일으킨다.

그러나 처음과는 확연한 차이가 있는 거친 호흡. 지금 당장 맞붙는다면 필패다.

나는 수호령의 앞을 막아서며 입을 열었다.

“그래, 혈주(血主). 그 미친 새끼도 마찬가지였지.”

“아쉽네. 그때 혈주를 만나지 않았다면 지금쯤 기절초풍하는 네 모습을 볼 수 있었을 텐데.”

“그 정도로 담이 작았으면 진작 뒈졌지.”

“어려서 그런가? 허세는 어쩔 수가 없네.”

허세라.

소림혈사 당시 혈주가 보여 준 모습은 분명 놀라웠지만, 기절초풍할 정도는 아니었다.

그러기에는 지금껏 내가 나고 자란 현대에서 보고 겪은 것이 너무나도 많다.

“좋을 대로 생각하든지.”

담담한 대답에서 무언가를 느낀 남천마후가 미간을 좁힌다.

가늘어진 눈으로 나를 위아래로 훑어보던 그녀가 붉은 입술을 혀로 핥았다.

“단순히 간이 큰 건지. 아니면 아무도 모르는 무언가가 있는 건지는 모르겠지만…… 역시 묘하단 말이야. 왜 천주께서 네게 흥미를 보이시는지, 조금은 알 것 같기도 해.”

“관심?”

되물은 나는 남천마후가 눈치채지 못할 만큼, 아주 천천히 공력을 순환시켰다.

남천마후라는 괴물로도 벅찬데, 어디서 무통 주사를 처맞고 온 약쟁이까지 더해졌다. 조금이라도 앞서 입은 내상을 회복시키며 시간을 벌어야 한다.

“그렇지 않아도 대설귀, 그 늙은이도 그런 헛소리를 지껄이긴 했지.”

“어머. 그럼 혹시 지금도 헛소리라고 생각해?”

남천마후가 싱긋 웃으며 한 걸음을 내디딘다. 나는 창대를 움켜쥔 손에 힘을 더하며 대답했다.

“헛소리였으면 하는 바람이지.”

“어째서?”

“천주고 나발이고, 그런 정신 나간 늙은이한테는 관심받기 싫으니까. 지금 눈앞에 보이는 어느 미친년도 포함해서.”

쉭, 피핏!

아릿한 통증과 함께, 뺨이 뜨겁게 달아오른다. 간발의 차로 지풍(指風)을 피해 낸 내 모습에 남천마후가 안도의 한숨을 내쉬었다.

“휴. 하마터면 죽일 뻔했네. 잘 피했어. 생각했던 것 이상인데?”

이런 상황에서, 그것도 적에게 칭찬이라니.

기분이 더러웠지만, 덕분에 두 가지 사실을 알았다.

첫째. 저 괴물 같은 년이 전력을 다하더라도, 조금 전처럼 최소한의 피해를 입는다면 감당할 수 있다는 것.

둘째. 나를 죽이면, 남천마후에게도 득보다 실이 크리라는 것.

주르륵.

나는 뺨을 타고 흐르는 피를 닦는 대신, 창대를 움켜쥔 손에 힘을 더하며 대꾸했다.

“천주. 그 늙은이가 생각보다 나한테 관심이 많나 보네. 너 같은 미친년도 날 죽일까 봐 걱정하는 모습을 보면.”

“……!”

“이제야 대충 알 것 같아. 왜 호북성에서 나를 지켜만 봤었는지.”

남천마후는 실로 강대한 무위를 지녔다. 내가 지금껏 보고 겪은 이들을 떠올려봐도, 그녀와 대적할 수 있을거라 여겨지는 사람은 극소수였다.

‘낮게 잡아도 십왕(十王). 그 이상.’

단지 마주하고 있는 것만으로도 느껴지는 거대한 힘.

십왕 중에서도 논외로 취급받는 적천강을 제외한다면, 남천마후는 작금의 천하를 통틀어 최소 열 손가락 안에 드는 강자일 것이다.

‘그런데도 아무 일도 없었지. 호북성에서 수십, 수백 번이나 손을 쓸 기회가 있었음에도.’

남천마후의 정체를 깨달았을 때부터 줄곧 마음 속에 품고 있던 의문이다.

왜 나를 살려 둔 걸까.

죽일 가치조차 없어서? 단순한 유희로?

비록 자세한 내막은 모르겠지만, 아니라는 확신이 들었다. 나는 다른 누구도 아닌 화왕(火王) 적천강의 하나뿐인 제자이자, 열화문의 후인이다.

나를 수중에 넣는다면 향후 암천의 행보에 큰 걸림돌이 될 적천강을 끌어들여 해치울 수도 있고, 그 시도가 헛물을 켜도 열화문의 신공절학을 손에 넣을 수 있다.

굳게 닫혀 있는 입을 벌릴 방법이야 많다.

고문. 고문. 그리고 끊임없는 고문.

하지만 남천마후는 자신에게 감쪽같이 속아 넘어간 나를 죽이지도, 그렇다고 납치하지도 않았다.

그저 눈앞에서 지켜보다 홀연히 사라졌을 뿐이다. 마치 누군가의 명을 받고 찾아온 감시자처럼.

나는 바싹 마른 입술을 달싹였다.

“천주가 도대체 왜, 무슨 이유로 이렇게까지 내게 흥미를 보이는 거지? 나보다 더 관심을 둘 만한 이들이 있는데도.”

그러나 내 물음에도, 언제부터인가 굳게 다물린 남천마후의 입술은 열리지 않았다.

잠깐의 침묵 끝에 짧은 대답을 내뱉었을 뿐이었다.

“너 따위 하찮은 존재가 뭘 알겠느냐. 전능하시고 지엄하신 그분의 뜻을.”

하찮은 존재라.

내심 중얼거린 나는 경직된 남천마후의 얼굴을 바라보았다.

착 가라앉은 시선와 지그시 입술을 깨무는 모습 역시 놓치지 않았다.

동시에 뇌리를 스친 한 줄기의 생각이 목소리가 되어 입 밖으로 흘러나왔다.

“너, 모르지?”

“……!”

똑똑히 봤다. 순간 세차게 흔들리는 남천마후의 눈빛을. 그와 함께 비웃음 섞인 실소가 터져 나왔다.

“병신.”

“……뭐?”

“병신이라고 했다. 이 하찮고 병신 같은 할망구야.”

그리고 그 한 마디가, 남천마후라는 폭탄의 심지에 불을 붙였다.

콰아아아아!

막대한 기의 폭풍이 사방을 휩쓴다.

전신에 새카만 어둠을 겹겹이 두른 남천마후의 모습에, 거친 숨을 가다듬은 수호령이 의념을 흘려보냈다.

- 기왕 할 거, 조금만 더 시간을 끌지 그랬나.

안 그래도 약간의 후회가 들었지만, 다른 방법이 없었다.

내궁에 남아 있는 인간과 맹수들이 변이(變異)를 끝마치기 전에 결말을 지어야 한다. 이 중 누가 쓰러지고, 누가 서 있느냐는 그다음의 이야기다.

나는 아직 성치 않은 몸으로 툴툴거리는 수호령을 향해 전음을 날렸다.

- 수호령 맞냐? 곧 쓰러질 것처럼 빌빌거리지 말고 죽을 힘을 다해서 싸워.

- 감히 날 모욕하다니. 삼백 년 전이었으면 인간 따위에게 이런 수모를 당하지도 않았을 것이다.

- 그랬겠지. 그땐 저 미친년도 안 태어났을 테니까.

- ……제기랄.

수호령이라는 이름에 어울리지 않게 상스러운 말을 내뱉은 수호령이 전신의 털을 바싹 곤두세운다.

앞뒤로 다가오는 두 인영을 스치듯 훑은 녀석이 중얼거렸다.

- 상황이 더 어려워졌군.

- 와. 난 진짜 전혀 몰랐던 사실인데, 역시 수호령이라 그런지 대단하네. 알려 줘서 고맙다.

- 각자 하나씩 맡지. 인간 수컷과 인간 암컷. 둘 중 하나를 선택해라.

- 그럼 내가 수컷.

- …….

이 새끼 양심 상태가?

나를 빤히 바라보는 청백색 눈동자가 그렇게 묻는 듯했다. 개 같은 상황 속에서도 피식, 실소를 흘린 나는 걸음을 옮겼다.

남천마후를 향해.

저벅.

긴장했기 때문일까.

발걸음 소리가 유난히도 크게 울려 퍼진다. 어느새 피처럼 붉어진 안광(眼光)에 가슴 한구석이 서늘해졌다.

“날 상대하겠다고? 너 따위가?”

스산한 목소리. 나는 한숨을 푹 내쉬며 대답했다.

“섭섭하네. 같은 하찮은 존재끼리 돕고 살아야지. 안 그래?”

“……!”

“선택해. 날 죽이고 천주한테 조인트 까이든지. 아니면 지금 여기서 곱게 뒈지든지.”

카악, 퉤.

죽은 피가 섞인 가래침을 탁 뱉은 나는 창날을 곧추세웠다.

평소와는 다른, 낯설 만큼 차가운 목소리가 입술을 비집고 흘러 나온다.

“참고로 난…… 죽을 때까지 싸운다.”

화륵, 파앙!

염화일로(炎火一路). 공기를 살라먹으며 쏘아지는 한 줄기의 화염.

그리고 그 길의 끝에, 짙은 어둠을 두른 괴물이 있었다.

쐐애애액, 꽈앙!



* * *



쾅!

엄청난 충격파와 함께 세상이 뒤흔들렸다.

진태경이 내리그은 창날에 지면이 갈라지고 끔찍한 열기가 터져 나온다.

털끝 하나 차이로 일격을 피해 낸 남천마후가 손을 뻗었다.

콰아아아!

미증유의 기운이 실린 일장(一掌)과 빛살처럼 공간을 가르며 나아간 창날이 부딪친다. 거대한 기의 격돌. 그러나 힘의 격차는 명확했다.

퍼엉!

압축된 공기가 터져 나가는 소리와 함께 튕겨지는 한 사람의 신형.

남천마후의 눈동자에 환희가 깃들었다.

‘저놈 따위, 아무것도 아니다.’

분명 진태경의 무위는 믿을 수 없이 진일보했다. 호북에서 만났던 바로 그 아이가 맞는지 의심이 들 만큼.

어쩌면 이번 대계의 가장 큰 걸림돌이 야수묘왕이 아니라 진태경이 되었을지도 모르겠다는 생각이 들 정도였다.

하지만…….

‘나는 더더욱 강해졌다.’

느껴진다. 전신에 들끓는 미증유의 기운이.

‘균열’에서 흘러나오는 마기가 짙어질수록, 남천마후의 힘 역시 강해지고 있었다.

바로 지금 이 순간에조차.

팟!

단 한 걸음.

유령처럼 사라진 남천마후의 신형이 허공에서 나타났다.

유성처럼 내리꽂히는 그녀의 모습에 지면 깊숙이 처박혀 있던 진태경이 눈을 부릅떴다.

콰드득.

단단한 지면이 진흙처럼 뭉개진다. 간발의 차로 공격을 피한 진태경은 소매를 떨쳤다.

마치 만들어 내기라도 한 듯, 어디선가 날아온 비수를 가볍게 피해 낸 남천마후가 섬전처럼 손을 뻗었다.

서걱!

단지 스친 것뿐이다.

그러나 갈고리처럼 휘어진 손가락은 무복(武服)을 찢고 허벅지살을 베었다.

촤아악, 솟구치는 핏물과 함께 비틀거리는 진태경의 신형.

그리고 그런 그를 향해, 남천마후가 환한 웃음을 지으며 손날을 내리그었다.

슈화악!
```

## Final English reading copy

```markdown
# Chapter 701

“He’s my hunting dog. One I trained with a great deal of care.”

The Southern Heaven Demon Empress’s voice rang out softly. At the same time, the masked man took a step forward.

Thud.

Between the hazy clouds of dust, his advancing step did not waver in the slightest.

As the masked man’s form gradually came into focus, I muttered like a groan.

“……Fuck. What the hell is that?”

I wasn’t asking for an answer. I already knew the answer to this question.

*Regeneration.*

Those two words were enough to explain the bizarre sight unfolding before my eyes even now.

Crack. Slither.

Shattered bones joined together, while flesh and blood swelled into place.

Each time darkness that writhed like a living snake brushed across the masked man’s body, his wounds healed and new strength seeped into him.

—The power of defying heaven……

Defying heaven.

It was a sight that seemed to run counter to the will of heaven and the natural order.

As the guardian spirit let its thought flow out like a lament, the masked man, having finished recovering, bent his strangely twisted elbow.

Crack.

He broke the elbow that had already fused back together himself, then aligned it and healed it again.

It was an act accompanied by tremendous pain, yet the masked man did not even twitch an eyebrow. That was when I realized the source of the incongruity I had felt during the battle.

*That bastard can’t feel pain.*

Even someone with a dulled sense of pain would feel at least a little.

But the masked man had not groaned or screamed even once.

Not when the dagger pierced his chest or his elbow was crushed. Not when he was struck by the Flame Divine Palm, which carried horrific heat.

*What the hell did they do to him?*

Did he go and get a painkilling shot somewhere?

As I stared at the emotionless eyes visible above his mask and swallowed a low groan, someone’s small, snow-white foot stepped onto the damp earth.

Scuff.

From the sky to the ground.

At last, the Southern Heaven Demon Empress landed lightly on the ground and smiled.

“You look like you’ve seen a ghost. Then again, I suppose you weren’t all that surprised? You saw it once in Henan.”

Grrr.

Along with a low growl, the enormous body, stained with blood in several places, rose on tired limbs.

But its breathing was far rougher than it had been at the beginning. If it fought right now, it would lose without question.

I stepped in front of the guardian spirit and opened my mouth.

“Yeah, the Blood Lord. That lunatic was the same.”

“It’s a shame. If you hadn’t met the Blood Lord back then, I could have watched you faint dead away by now.”

“If I were that timid, I would’ve been dead a long time ago.”

“Maybe it’s because you’re young. You can’t help the bluffing.”

A bluff.

What the Blood Lord had shown during the Shaolin Bloodshed had certainly been surprising, but not enough to make me faint dead away.

I had seen and experienced far too much in the modern world where I had been born and raised for that.

“Think whatever you want.”

The Southern Heaven Demon Empress narrowed her brow, sensing something in my calm answer.

She slowly looked me up and down with narrowed eyes, then ran her tongue over her red lips.

“I don’t know whether you’re simply brave, or whether you have something no one else knows about…… But you really are strange. I think I’m beginning to understand why the Lord of Heaven is interested in you.”

“Interested?”

As I asked the question, I very slowly circulated my internal energy without letting the Southern Heaven Demon Empress notice.

Dealing with a monster like her was already too much, and now some drugged-up bastard who had apparently gotten a painkilling shot had joined the fight. I had to recover some of the Internal Injury I had suffered earlier and buy myself time.

“Come to think of it, that old man, the Great Snow Fiend, spouted the same nonsense.”

“Oh my. Then do you still think it was nonsense?”

The Southern Heaven Demon Empress smiled and took another step. Tightening my grip on the spear shaft, I answered.

“I wish it were nonsense.”

“Why?”

“To hell with the Lord of Heaven. I don’t want attention from some insane old man. That includes the crazy woman standing in front of me.”

Whoosh—pfft!

A stinging pain flashed across my face, and my cheek grew hot. The Southern Heaven Demon Empress let out a sigh of relief when she saw that I had evaded the Finger Qi by the narrowest margin.

“Phew. I almost killed you. Nice dodge. You’re better than I thought.”

Praise from an enemy. In a situation like this, no less.

It left a foul taste in my mouth, but thanks to it, I learned two things.

First, even if that monstrous woman gave it her all, I could withstand her so long as I suffered only the minimum damage, as I had just now.

Second, killing me would cause the Southern Heaven Demon Empress a greater loss than gain.

Instead of wiping away the blood running down my cheek, I tightened my grip on the spear shaft and replied.

“The Lord of Heaven. Looks like that old man is more interested in me than I thought. Seeing you worry that a crazy woman like you might kill me.”

“……!”

“Now I think I roughly understand why you only watched me in Hubei Province.”

The Southern Heaven Demon Empress possessed truly tremendous martial power. Even when I thought of everyone I had seen and encountered until now, only a very small number of people seemed capable of standing against her.

*At the very least, one of the Ten Kings. Maybe even higher.*

The enormous power I could feel simply from standing in front of her.

Excluding Jeok Cheongang, who was treated as an exception even among the Ten Kings, the Southern Heaven Demon Empress would be one of the ten strongest people in the world today.

*And yet nothing happened. Even though she had dozens, hundreds of chances to act in Hubei Province.*

It was a question I had carried in my heart ever since I realized the Southern Heaven Demon Empress’s identity.

Why had she left me alive?

Because I wasn’t worth killing? For simple amusement?

I didn’t know the details, but I had become certain that wasn’t the case. I was none other than the sole Disciple of Fire King Jeok Cheongang and the successor of the Fire Gate Clan.

If she got me into her hands, she could lure in Jeok Cheongang, who would become a major obstacle to Dark Heaven’s future movements, and kill him. Even if that attempt came to nothing, she could still obtain the Fire Gate Clan’s supreme arts.

There were many ways to pry open a tightly closed mouth.

Torture. Torture. And endless torture.

But the Southern Heaven Demon Empress had neither killed me, who had been completely fooled by her, nor kidnapped me.

She had merely watched me right before my eyes, then vanished without a trace. Like an observer sent on someone else’s orders.

My parched lips moved.

“Why is the Lord of Heaven so interested in me? What reason does he have to take this far, when there are others more worthy of his attention than me?”

Yet even in response to my question, the Southern Heaven Demon Empress’s lips, which had been pressed tightly shut at some point, did not open.

After a brief silence, she gave only a short answer.

“What could a worthless thing like you know of the will of that omnipotent, exalted person?”

*A worthless thing.*

I muttered inwardly as I watched the Southern Heaven Demon Empress’s tense face.

I did not miss the way her gaze had gone still or how she gently bit her lip.

At the same time, a single thought flashed through my mind and became a voice.

“You don’t know, do you?”

“……!”

I saw it clearly.

The Southern Heaven Demon Empress’s eyes shook violently for an instant. A derisive chuckle escaped me.

“Fucking idiot.”

“…What?”

“I said you’re a fucking idiot. You worthless fucking idiot of an old hag.”

And that single remark lit the fuse of the bomb known as the Southern Heaven Demon Empress.

Kraaaaaash!

An enormous storm of qi swept in every direction.

As the Southern Heaven Demon Empress wrapped layer after layer of pitch-black darkness around her entire body, the guardian spirit, which had steadied its rough breathing, sent out a thought.

—If you were going to do it, why didn’t you stall for a little more time?

I did feel a little regret, but there was no other way.

I had to bring this to an end before the humans and beasts remaining in the Inner Palace finished mutating. Who fell and who remained standing would come afterward.

I sent a Sound Transmission to the guardian spirit, which was still grumbling despite its battered body.

—Are you really a guardian spirit? Stop dragging yourself around like you’re about to collapse and fight with everything you’ve got.

—How dare you insult me. If this had been three hundred years ago, I would never have suffered such humiliation at the hands of a mere human.

—Sure. That crazy woman wouldn’t have been born yet, either.

—……Damn it.

The guardian spirit, cursing in a manner unbecoming of its name, raised every strand of fur on its body.

It swept a glance over the two figures approaching from ahead and behind, then muttered.

—The situation has gotten worse.

—Wow. I really had no idea. Amazing, I guess, being a guardian spirit. Thanks for letting me know.

—We’ll each take one. The human male and the human female. Choose one.

—Then I’ll take the male.

—……

*What the hell is wrong with this bastard’s conscience?*

The blue-white eyes staring straight at me seemed to be asking exactly that.

Even in this godforsaken situation, I let out a quiet laugh and started walking.

Toward the Southern Heaven Demon Empress.

Thud.

Maybe it was because I was tense.

The sound of my footsteps rang out unusually loudly. Her eyes had already turned blood red, and a chill settled in one corner of my chest.

“You intend to face me? You?”

Her voice was cold and eerie. I let out a deep sigh before answering.

“That hurts. Worthless creatures like us should help each other survive. Don’t you think?”

“……!”

“Choose. Kill me and get your ass kicked by the Lord of Heaven, or die nicely right here.”

Hack—ptoo.

I spat out phlegm mixed with dead blood and raised the spearhead.

A voice unlike my usual one slipped between my lips, cold enough to feel unfamiliar.

“For the record…… I’ll fight until I die.”

Fwoosh—boom!

Flamefire Path.

A single line of flame shot forward, consuming the air as it flew.

And at the end of that path stood a monster wrapped in deep darkness.

Shwaaaak—boom!

* * *

Bang!

The world shook with an immense shockwave.

The ground split apart beneath the spearhead Jin Taekyung had swung down, and horrific heat burst upward.

The Southern Heaven Demon Empress avoided the attack by a hair and extended her hand.

Kraaaaaash!

A palm strike carrying unprecedented qi collided with the spearhead slicing through space like a ray of light.

A tremendous clash of qi.

But the difference in strength was clear.

Boom!

Along with the sound of compressed air exploding, one figure was hurled backward.

Joy filled the Southern Heaven Demon Empress’s eyes.

*That wretch is nothing.*

Jin Taekyung’s martial power had clearly advanced at an unbelievable pace. He had changed so much that she found herself wondering whether he was truly the same boy she had met in Hubei.

She even wondered whether the greatest obstacle to this grand scheme might have become Jin Taekyung instead of the Beast Miao King.

But……

*I have grown even stronger.*

She could feel the unprecedented power boiling throughout her body.

*The denser the demonic qi flowing from the rift becomes, the stronger I become.*

Even at this very moment.

Pop!

A single step.

The Southern Heaven Demon Empress vanished like a ghost, then appeared in midair.

As she plunged downward like a meteor, Jin Taekyung, buried deep in the ground, opened his eyes wide.

Crack.

The solid ground crumbled like mud.

Jin Taekyung narrowly evaded the attack and flicked his sleeve.

The dagger that came flying from somewhere, as if he had created it out of thin air, was easily avoided by the Southern Heaven Demon Empress. She then thrust out her hand like a flash of lightning.

Slash!

It had only grazed him.

But her fingers, curled like hooks, tore through his martial uniform and sliced into his thigh.

Blood gushed upward, and Jin Taekyung staggered.

The Southern Heaven Demon Empress smiled brightly as she brought a knife-hand strike down toward him.

Shu-whaack!
```
