<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0078.txt",
      "sha256": "d0e95fdfe7028c24aeb23b31eb26a8dac6e194e7685637033366a58f99125b01",
      "bytes": 11441
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "504cc8f13eb04399028c73f4a5ef820e7f94eb9f05b095112571acbfe5d31a35",
      "bytes": 6632
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d7a61f4eb769b5160c3d9d19475d46ead7e4f4aa0f3a194efd0b8710d3f5336d",
      "bytes": 5049
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "c5fa384971fba991989e56bfc54937316a500d5c0300a726b51a10a042530242",
      "bytes": 1610
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "72e027ed95ba6a820d646c78a849ea41f7ab789d6d83e0204da4f9364e701439",
      "bytes": 23807
    },
    {
      "path": "characters/Team Leader Choi.md",
      "sha256": "d2770f9356f099378fc00fc6cdb99de81c472fa7649d0276c4a297d527c7a4ae",
      "bytes": 3813
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "17c806e53ccce7126295a60ca8d0749c8207299ae172b0e5e0cbcfe241a3af3c",
      "bytes": 4958
    }
  ],
  "estimated_tokens": 11310
}
-->

# Durable State Update — Chapter 78

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 78. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 78. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 78,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 78,
    "continuity_sources": [78],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "Taekyung successfully logged out after roughly twenty days in Murim; his watch showed 2:05:35 in the modern world, and he states that ten modern-world days now correspond to one hour in Murim.",
    "Taekyung currently has fifteen years of internal energy. Circulating his qi slightly increases his internal energy, and Sleep Mode normally keeps his sleep below three hours except when he is seriously injured.",
    "Seong Jinho is thirty, has lived with Taekyung as a friend and brother for years, and now plans to move out of the goshiwon soon, though the date is not fixed.",
    "Team Leader Choi owns the café where he meets Taekyung and gives him a contract; Taekyung signs it, after which a System alert appears.",
    "After ten days of Mukyung's training, Taekyung mastered the Jin Family's Spear Technique and Jin Family's Manoeuvre Technique; the Training? Trial! Quest succeeded and granted a Level Up, an Inventory reward, and notice of an additional reward.",
    "Hyuk Mujin remains badly injured and under treatment after the attack; the unidentified assassin may be the Head Elder's hidden disciple.",
    "Jin Mukyung reunited with Jin Wikyung after three years but remains detached and prioritizes sword training. Jin Wikyung plans to summon every Shanxi sect on New Year's Day and may seek to become Alliance Leader.",
    "Wipeng leads thirty elites south under the pretext of pursuing the nonexistent assassin, visited Song Sword Sect, and delivered Wikyung's summons as both summons and warning; Wikyung found no information on Dark Heaven in the family records.",
    "Gong Yacheong is recovering and will take charge of the rebuilt Sakju Branch; Socheon and Soyul will accompany him in six months. Soyul is five and does not know her parents are dead.",
    "The Returnee title grants Taekyung All Stats +10 and activates Login and Logout. Taekyung accepted that he was half-finished, asked Mukyung for help, and received a System time limit of 9 days 20 hours 23 minutes.",
    "Childeuk is an injured former meal-delivery servant who became a Level 12 martial artist directly under Jin Wikyung; Wikyung publicly embraced and praised him after acknowledging a minor misunderstanding.",
    "Lee Seowol is the new female Sect Leader of the Mount Heng Sword Sect. Taekyung received the forced Yesterday's Enemy, Today's Ally Quest to deliver an invitation for New Year's Day; its completion and Reward remain unknown.",
    "Taekyung, Mukyung, and Hyuk Mujin departed for Eung-hyeon in a four-horse carriage because Lee Seowol requested their visit and Mukyung may learn Peak martial arts.",
    "Taekyung is now a member of the Peace Guild and completed the Guild Membership achievement, receiving 10 points.",
    "Taekyung's Peace Guild contract provides a 500 million won signing bonus, a fixed monthly salary of 50 million won, a seventy-percent settlement share, and Guild-provided housing, a car, and other benefits.",
    "The Peace Guild's Guild house is Sooni's Super, a dilapidated corner store in Bucheon's Gate-dense district, on property purchased from the former owner's surviving family for slightly more than 2 billion won per pyeong.",
    "Im Kkeokjeong joined the Peace Guild after Team Leader Choi recruited him while he was hospitalized. He is married and has two children.",
    "The Peace Guild has five members: Taekyung, Team Leader Choi, Butler Kim, Im Kkeokjeong, and Song Song. Song Song is a founding member.",
    "Essence of the Himalayas increases Taekyung's Intelligence by 1 for one hour."
  ],
  "continuity_sources": [
    77
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons and whether he will become Alliance Leader.",
    "It remains unresolved whether Song Sword Sect has any connection to the attack.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung's prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "Song Song's full background and capabilities remain mostly unrevealed, and it is unclear whether she heard Taekyung's interrupted confession."
  ],
  "safe_through": 77,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote; render 도덕책 as ethics textbook with a footnote explaining the pun.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year's Day for 원단 and close the sect's gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, four-horse carriage for 사두마차, and goshiwon for 고시원 with a footnote.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Use fist-and-kicking technique for 권각술 and recognition for 인정; render 낙류검 as Falling Flow Sword, 질풍십이권 as Twelve Gale Fists, 화염신장 as Flame Divine Palm, and 분근착골 as Tendon-Splitting and Bone-Twisting.",
    "Render 비급 제작 as Martial Arts Manual Creation, 맷집 as Toughness, 천무지체 as Heavenly Martial Physique, 장칠득 as Jang Childeuk, Martial Artist Jang for 장 무인, 인의예지 as benevolence, righteousness, propriety, and wisdom, 호환 as killed by a tiger, 일각 as fifteen minutes, and 모태 솔로 as lifelong single; use “Let's eat noodles” for 국수 먹자 with a cultural footnote.",
    "Use Squad Leader for 조장님, Third Young Master for 삼공자님, Mujin for 무진아, seventh-tier student for 내신 칠 등급, Team Leader Choi for 최 팀장, Designer-Brand Junkie for 명품충, Qi Sense for 기감, Peace Guild for 평화, Essence of the Himalayas for 히말라야의 정수, Sooni's Super for 순이네 수퍼, pyeong for 평당, Song Song for 송송이, Miss Song for 송이 씨, and Taurus for 황소자리."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 최민우    | **Choi Minwoo**   |
| 선배     | **Senior**                                   |
| 상태               | **Status**                     |
| 헌터      | **Hunter**            |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 대격변     | **Great Cataclysm**   |
| 대사      | **Master** for a senior Buddhist monk                           |
| 임꺽정 | **Im Kkeokjeong** |
| 평화 | **Peace Guild** | Guild name. |
| 대한민국 | **Korea** | Country reference. |

## Listed compact profiles

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 77
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** E-rank Hunter; veteran member of the Peace Guild’s Gate party and current member of the Peace Guild
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and is married with two children

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 77
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; F-rank Hunter; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling

### Team Leader Choi.md

# Team Leader Choi

- **Safe through:** Chapter 54
- **Aliases:** Choi Minwoo (최민우)
- **Role:** Reawakened Hunter publicly classified as C-rank; leader and employer of the Peace Guild’s E-rank Gate party
- **Personality:** Calm, observant, practical, and decisive under pressure
- **Voice:** Polite and measured in ordinary conversation; clipped and commanding during combat
- **Relationships:** Hires Jin Taekyung as a porter and leads him, Im Kkeokjeong, and three veteran E-rank Hunters through an E-rank Gate

## Korean source

```text
＃78화



헌터들은 하나같이 술고래다.

최하급인 F급 헌터라고 해도 일반인을 훌쩍 뛰어넘는 신체 능력과 신진대사의 소유자들이니까.

술을 안 먹는 헌터는 있어도 못 먹는 헌터는 없다는 말이 괜히 있는 게 아니다.

“히끅. 한 잔 더.”

그런데 여기 한 명 있었네.

어느새 반쯤 눈이 풀린 송이 씨가 맹렬하게 빈 잔을 흔들었다.

“한 잔 더어!”

취한 모습도 예뻐……가 아니고. 이 정도면 살짝 위험한 거 아닌가? 나는 걱정스러운 눈빛으로 송이 씨를 바라봤다.

‘너무 급하게 마신 것 같은데.’

본격적으로 술자리가 시작되자마자 소주 한 병을 나발로 불더니 쭉 저 상태다. 가끔은 혀 꼬인 발음으로 눈치도 더럽게 없다느니, 재수 옴 붙었다느니 하는 뜻 모를 소리를 중얼거리기도 했다.

‘안 좋은 일이라도 있는 건가?’

임꺽정이 그녀의 술잔을 채워 주는 틈을 타 최 팀장에게 소곤거렸다.

“팀장님. 송이 씨 무슨 일 있었어요?”

최 팀장이 떨떠름한 얼굴로 대답했다.

“……있긴 있죠.”

“역시.”

“그것도 아주 최근에.”

“앗. 아아.”

송이 씨의 불행은 곧 나의 불행. 지켜보고만 있자니 억장이 무너진다.

“후우. 잘 해결됐으면 좋겠네요.”

“…….”

“…….”

최 팀장은 물론이고 옆에 앉아 있던 김 집사까지 괴상한 표정으로 나를 바라본다.

이거 왠지 기분이 이상해지는데.

“왜요?”

“아닙니다.”

“젊을 때는 그럴 수도 있죠.”

어째 미적지근한 대답이지만 지금 그게 중요한 게 아니다.

까드득.

“마셔요! 오늘 마시고 죽어!”

세 병째 소주를 깐 송이 씨가 미쳐 날뛰고 있었으니까.

“으하하! 난 이래서 송이 씨가 참 좋더라!”

물 만난 고기. 아니, 술 만난 산적처럼 옆에서 거드는 임꺽정은 덤이다.

“말려야 되는 거 아니에요?”

“아, 송이 씨요?”

“네.”

최 팀장이 어깨를 으쓱했다.

“괜찮습니다. 하루 이틀 본 것도 아니고. 송이 씨 술버릇이 원래 저래요.”

“아무리 그래도…… 아니 잠깐만.”

나는 최 팀장을 지그시 노려봤다.

아까부터 수상하다 싶었는데, 이제야 덜미를 잡았다.

“팀장님이 송이 씨 술버릇을 어떻게 압니까?”

“같이 술을 마셨으니까 알죠.”

“…….”

이 자식이 누굴 놀리나. 내가 그걸 몰라서 물어본 것 같니?

“그 얘기가 아니잖아요.”

“그럼 어떤 얘깁니까?”

“그러니까…….”

막상 이렇게 나오니까 할 말이 없다. 생각해 보면 내가 뭐라고 두 사람 관계를 따진단 말인가?

순간 말문이 막힌 그때, 최 팀장이 불쑥 입을 열었다.

“아레스. 들어 보셨죠?”

“당연하죠.”

전신(戰神) 아레스.

고대 그리스 로마 신화에 등장하는 신의 이름이다. 지금에 이르러서는 다른 의미로 유명해졌지만.

“아레스 길드 모르는 사람이 어디 있어요?”

대한민국 헌터의 자존심이자 자부심.

국내에는 수백 개의 길드가 존재하지만 정점은 오직 하나, 아레스 길드였다. 대격변 초기부터 지금까지 그들이 이룩한 위업은 셀 수 없이 많다.

‘말 그대로 전설이지, 전설.’

학습 만화, 교육 애니메이션, 영화와 소설 등등. 심지어는 교과서에도 나온다.

아레스 길드가 국내에서 차지하는 위치는 살아 있는 세종대왕이요, 현역 이순신 장군에 버금간다. 아니, 그 이상일 것이다.

‘세계적으로 워낙 유명하니까.’

두 유노 킹 세종? 킹 갓 제너럴 순신 리? 하고 물어보면 대다수의 외국인들은 이 동양인 새끼가 뭐라는 거야, 하겠지만 아레스 길드는 다르다.

- 두 유노 아레스?

- 오, 예쓰!

터프하기 짝이 없는 텍사스 할아버지도 쌍권총을 탁 치며 알아듣는다는 게 학계 정설이다.

“그런데 아레스 길드는 왜요?”

맥주 한 모금을 삼킨 최 팀장이 대답했다.

“제가 거기 있었거든요.”

“아. 그렇구나…… 예?”

내가 지금 무슨 말을 들은 거지?

말문이 막혀 한동안 눈만 껌뻑이다가 입을 열었다.

“아레스 길드 소속이셨다고요?”

“팀장이었습니다. 그래 봤자 한참 말단이지만.”

아레스 길드의 문턱은 높다. 최고만 가려서 뽑고, 최고로 길러 낸다. 최 팀장은 스스로를 한참 말단이라고 했지만 이미 거기서 팀장을 달았다는 것부터가 대단한 거다.

지금 내 눈에는 그냥 미친놈처럼 보이지만.

“아니, 거길 왜 나왔어요?”

돈, 명예, 지위.

헌터라면, 남자라면 바라마지 않는 최고의 직장이다. 그걸 걷어차고 나오다니!

“혹시 사내 왕따, 뭐 그런 거 당했어요?”

곰곰이 생각하던 최 팀장이 대답했다.

“그랬을 수도 있겠네요. 절 편하게 대해 주는 사람은 송이 씨밖에 없었으니까.”

“……그럼 송이 씨도 아레스 길드?”

“제 팀원이었습니다. 팀 회식 때 술버릇을 알게 됐죠.”

침이 목울대를 타고 꿀꺽 넘어간다.

‘이거 완전 엘리트들이잖아.’

맥주를 홀짝이는 최 팀장과 병나발을 불고 있는 송이 씨를 번갈아 보던 내 시선이 한 사람에게 멈췄다.

“혹시 김 집사님께서도……?”

“저 말입니까?”

김 집사가 인자하게 웃으며 손을 내저었다.

“전 이미 오래전에 은퇴했습니다. 허허허.”

“네?”

그럼 전직 헌터란 소린데.

문득 김 집사를 대할 때마다 느꼈던 이질감이 떠올랐다. 지금까지 단 한 번도 그를 [기감]으로 파악해 보지 않았다는 사실도.

‘이 사람, 정체가 뭐지?’

기감을 끌어 올리려던 그때.

우리가 이야기를 나누건 말건 열심히 술과 고기를 흡입하던 임꺽정이 말했다.

“어, 버너 불 꺼졌다. 송 양. 가스 새 거 없어?”

“히끅. 그게 마지막이었는데요.”

“에이, 흐름 끊기면 안 되는데. 그냥 먹을까?”

한참 설익은 고기를 뒤집으며 투덜거리는 임꺽정을 향해, 김 집사가 부드럽게 웃어 보였다.

“그럼 안 되죠.”

그리고 다음 순간, 두 가지 일이 동시에 일어났다.

딱!

김 집사가 손가락을 튕겼고.

화아아악!

후끈한 열기가 뿜어져 나왔다. 정확히 불판 위로 솟구친 푸른 불꽃은 순식간에 판을 달구고 고기를 익힌 뒤 사라졌다.

“이건…….”

나와 임꺽정은 누가 먼저랄 것도 없이 외쳤다.

“마법사!”

“엄청 잘 구웠어!”

“…….”

“왜? 태경이 너도 빨리 먹어.”

됐네, 이 양반아. 나는 고개를 절레절레 저었다.

그보다 김 집사가 마법사였을 줄이야. 어쩐지 느낌이 이상하더라니.

“깜빡 속았네요.”

김 집사가 잘 익은 고기를 한 점 집어 올렸다.

“속일 생각은 없었습니다. 저야 말씀드렸다시피 이미 은퇴한 퇴물이니까요.”

퇴물은 무슨. 김 집사가 퇴물이면 지금 현역으로 활동하는 마법사 중에 절반은 대가리 박아야 한다.

‘최소 B급 이상.’

손가락 한 번 튕기는 것만으로도 불꽃을 불러내고 고기를 태우지도, 덜 익히지도 않고 알맞게 구울 만큼 컨트롤 역시 정교하다. 정황을 미루어 볼 때 은퇴 전에는 그 역시 아레스 길드 소속이었을 것이다.

만약 대격변 때도 활동한 인물이라면.

‘……이거 거물인데?’

거기에 더해 까마득한 대선배다.

나는 조심스럽게 물었다.

“저어, 혹시 헌터 훈련소는 어디 나오셨는지.”

“논산 나왔습니다. 태경 씨는요?”

“헉. 저도 논산입니다. 28연대 1대대.”

“그래요? 이거 우연이네요. 나도 28연대 1대대 나왔는데. 몇 중대 출신이에요?”

“2중댑니다.”

“우연이 아니라 인연인가 보네요. 하하.”

두말할 필요가 없다. 자리에서 일어난 나는 허리를 꺾었다.

“반갑습니다, 선배님.”

대한민국은 학연, 지연, 혈연이라는 말이 있다. 헌터도 마찬가지다.

각성 확률은 0.1퍼센트. 천 명당 하나꼴이고 이런 희박한 확률 때문에 사회에서 알던 지인이 각성하는 경우는 드물다. 별것 아닌 것처럼 보이는 헌터 훈련소가 인맥의 시작점인 셈이다.

“뭘 또 이렇게까지. 앉으세요.”

“말씀 편하게 하셔도 됩니다.”

“저는 그런 거 안 따지니까…….”

나와 김 집사가 선후배 간의 훈훈한 분위기를 연출하고 있던 그때, 가만히 지켜보던 최 팀장이 불쑥 끼어들었다.

“김 집사님. 진태경 씨 말대로 하는 게 어떻겠습니까?”

이런 버르장머리 없는 놈을 봤나. 감히 대선배님께 이래라저래라…….

‘으음. 할 수 있지.’

생각해 보면 최 팀장이 더 거물이다. 아레스 길드 출신 마법사를 집사로 쓰는 놈이니까.

‘도대체 어떤 집안이길래.’

할아버지가 대통령이고 아버지가 국무총리쯤 되나?

궁금증만 더해 갈 때 최 팀장의 말이 이어졌다.

“이쯤에서 호칭 정리를 해야겠죠. 명색이 우리 길드의 얼굴이신데 언제까지 집사님이나 아저씨라고 부를 수는 없는 것 아닙니까?”

잠시 고민하던 김 집사가 대답했다.

“도련님 말씀에 따르겠습니다.”

고개를 끄덕인 최 팀장이 준엄한 눈빛으로 좌중을 쓸어 보았다.

“그럼 앞으로 김 집사님에 대한 호칭은 길드장님으로 통일합니다. 이의 없으시죠?”

임꺽정과 송이 씨가 대답했다.

“크, 고기 맛 죽이네. 마법으로 구워서 그런가?”

“술이 들어간다. 술! 술술, 술술!”

“…….”

회한 어린 눈빛으로 두 사람을 응시한 최 팀장이 내게 시선을 돌렸다. 나는 보란 듯이 한쪽 팔을 들고 있었다.

“그건 무슨 뜻입니까?”

“질문드릴 게 있어서요.”

그나마 이놈은 좀 낫군. 최 팀장이 그런 얼굴로 말했다.

“말씀하세요.”

“최 팀장님이 길드장 아니었습니까?”

“…….”

배신당한 듯한 표정을 지은 최 팀장이 품에서 뭔가를 꺼내 건넸다. 받아 살펴보니 명함이다.

“저 이거 있는데요.”

“뭐라고 적혀 있습니까?”

“평화 길드 1팀장 최민우요.”

“네. 저 팀장입니다.”

“아.”

“김 집사님이 길드장. 제가 팀장. 나머지 세 분이 팀원입니다. 이제 이해되셨습니까?”

김 집사가 바지 사장인지, 얼굴마담인지는 모르겠지만 일단 고개를 끄덕였다. 그렇게 안 하면 최 팀장이 울 것 같아서.

“다른 분들도 알아들으셨습니까?”

최 팀장의 질문에 임꺽정과 송이 씨가 대답했다.

“이야, 술맛도 죽이네. 마법으로 구운 고기가 안주라 그런가?”

“언제까지 어깨춤을 추게 할 거야. 탈골됐잖아. 탈골! 탈골!”

“…….”

야, 우냐?
```

## Final English reading copy

```markdown
# Chapter 78

Every Hunter is a heavy drinker.

Even an F-rank Hunter, the lowest classification, possesses physical abilities and a metabolism far beyond those of an ordinary person.

There is a reason people say that while some Hunters do not drink, there are none who cannot.

“Hic. One more glass.”

Well, there was one here.

Miss Song’s eyes had already gone half-glazed as she furiously shook her empty glass.

“One more glaaass!”

*She’s pretty even when she’s drunk… No, that’s not the point. Isn’t this getting a little dangerous?*

I looked at Miss Song with concern.

*She must have drunk too quickly.*

The moment the drinking party had begun in earnest, she had chugged an entire bottle of soju straight from the bottle and had been like this ever since. Every now and then, she slurred incomprehensible things about someone having no damn tact and rotten luck clinging like a curse.

*Is something bad going on?*

While Im Kkeokjeong was filling her glass, I leaned toward Team Leader Choi and whispered.

“Team Leader. Did something happen to Miss Song?”

Team Leader Choi answered with an awkward expression.

“……Something did happen.”

“I knew it.”

“Something that happened very recently, too.”

“Oh. Ah.”

Miss Song’s misfortune was my misfortune. Just sitting there and watching her was breaking my heart.

“Whew. I hope things work out for her.”

“……”

“……”

Team Leader Choi, along with Butler Kim, who was sitting beside him, stared at me with strange expressions.

This was starting to feel weird.

“What?”

“Nothing.”

“People can be like that when they’re young.”

It was a lukewarm answer, but that was not important right now.

Crack.

“Drink! Drink until you drop dead today!”

Miss Song had opened her third bottle of soju and was going wild.

“Ha-ha-ha! This is why I really like Miss Song!”

Like a fish in water—no, like a bandit who’d found booze—Im Kkeokjeong egged her on from beside her.

“Shouldn’t we stop her?”

“Ah, Miss Song?”

“Yes.”

Team Leader Choi shrugged.

“It’s fine. It’s not like I’ve only known her for a day or two. That’s just how Miss Song gets when she drinks.”

“Even so… No, wait a second.”

I stared intently at Team Leader Choi.

I had thought he was suspicious for a while, but now I had finally caught him.

“How do you know what Miss Song is like when she drinks?”

“Because I’ve drunk with her.”

“……”

Was this bastard making fun of me? Did he think I was asking because I didn’t understand that?

“That’s not what I mean.”

“Then what do you mean?”

“I mean…”

Now that he had put it that way, I had nothing to say. When I thought about it, who was I to question the relationship between the two of them?

Just as I was rendered speechless, Team Leader Choi suddenly opened his mouth.

“You’ve heard of Ares, right?”

“Of course.”

Ares, the god of war.

The name of a god who appeared in ancient Greek and Roman mythology. These days, though, it was famous for something else.

“Who in Korea doesn’t know the Ares Guild?”

The pride and joy of Korea’s Hunters.

Hundreds of Guilds existed in Korea, but only one stood at the top: the Ares Guild. The achievements they had made from the early days of the Great Cataclysm to the present were too numerous to count.

*They’re legends. Plain and simple.*

They appeared in educational comics, educational animations, movies, novels, and all kinds of other media. They had even made it into textbooks.

The Ares Guild held a position in Korea comparable to a living King Sejong or an active General Yi Sun-sin. No, perhaps even higher.

*They’re famous all over the world, after all.*

If you asked most foreigners, *Do you know King Sejong? King-God-General Yi Sun-sin?* they would probably respond, *What the hell is this Asian guy talking about?* But the Ares Guild was different.

*Do you know Ares?*

*Oh, yeah!*

Even a tough-as-nails Texas grandpa would tap his twin pistols and understand. That was the accepted truth among scholars.

“Why are you asking about the Ares Guild?”

Team Leader Choi swallowed a mouthful of beer before answering.

“Because I used to be there.”

“Oh. I see… Huh?”

What had I just heard?

I blinked for a while before finally speaking.

“You used to belong to the Ares Guild?”

“I was a Team Leader. Though I was still pretty low-ranking.”

The Ares Guild had high standards. They selected only the best and trained them to become even better. Team Leader Choi had called himself a low-ranking member, but the fact that he had become a Team Leader there was already incredible.

Though at the moment, he just looked like a lunatic to me.

“Then why did you leave?”

Money, honor, and status.

It was the best job any Hunter—or any man—could dream of. And he had kicked it all away and left!

“Were you ostracized at work or something?”

Team Leader Choi thought about it for a moment before answering.

“That might have been the case. Miss Song was the only person who treated me normally.”

“……Then was Miss Song in the Ares Guild too?”

“She was on my team. I found out about her drinking habits during team dinners.”

I swallowed hard.

*These people are total elites.*

My gaze moved back and forth between Team Leader Choi, who was sipping his beer, and Miss Song, who was drinking straight from the bottle, before stopping on one person.

“Could it be that Butler Kim also…?”

“Me?”

Butler Kim smiled kindly and waved his hand.

“I retired a long time ago. Ha-ha-ha.”

“What?”

So he was a former Hunter.

Suddenly, I remembered the sense of incongruity I had always felt whenever I dealt with Butler Kim. I had also never once tried to assess him with my Qi Sense.

*What is this man’s real identity?*

Just as I was about to raise my Qi Sense, Im Kkeokjeong, who had been enthusiastically inhaling meat and liquor whether or not we were talking, spoke up.

“Oh, the burner went out. Miss Song, do we have another gas canister?”

“Hic. That was the last one.”

“Aw, we can’t let the momentum die. Should we just eat it?”

Im Kkeokjeong grumbled as he flipped a piece of meat that was still mostly raw. Butler Kim smiled gently at him.

“That won’t do.”

The next moment, two things happened at once.

Snap!

Butler Kim snapped his fingers.

Fwoosh!

A wave of scorching heat burst forth. Blue flames shot precisely up over the grill, heating the plate and cooking the meat in an instant before vanishing.

“This is…”

Im Kkeokjeong and I shouted at the same time.

“A mage!”

“It’s cooked incredibly well!”

“……”

“What? Taekyung, hurry up and eat.”

*Forget it, old man.*

I shook my head back and forth.

More importantly, who would have thought Butler Kim was a mage? No wonder something about him had always felt strange.

“You really fooled me.”

Butler Kim picked up a well-cooked piece of meat.

“I had no intention of fooling you. As I told you, I’m already a retired has-been.”

*Has-been, my ass.*

If Butler Kim was a has-been, half the mages still active today ought to bow their damn heads.

*At least B-rank.*

He could summon flames with a single snap of his fingers and control them precisely enough to cook the meat just right without burning or undercooking it. Judging from the circumstances, he had probably belonged to the Ares Guild as well before retiring.

If he had been active during the Great Cataclysm, too…

*……This guy’s a big shot.*

And on top of that, he was an incredibly senior one.

I asked cautiously.

“Um, which Hunter training center did you graduate from?”

“Nonsan.[^1] What about you, Mr. Taekyung?”

“Gasp. Me too. The 28th Regiment, 1st Battalion.”

“Really? What a coincidence. I was in the 28th Regiment, 1st Battalion too. Which company were you in?”

“Second Company.”

“Then it wasn’t a coincidence. I suppose it was fate. Ha-ha.”

There was no need for further discussion. I stood up and bent deeply at the waist.

“Nice to meet you, Senior.”

[^1]: Nonsan is home to Korea’s main Army recruit training center.

There is a saying in Korea about school ties, hometown ties, and blood ties.[^2] Hunters were no different.

The probability of awakening was 0.1 percent—one in a thousand. Because the odds were so slim, it was rare for someone you knew from ordinary society to awaken. The Hunter training center, which might seem like nothing special, was where a Hunter’s network began.

“You don’t have to go that far. Please, sit down.”

“You can speak comfortably with me.”

“I don’t really stand on ceremony…”

Just as Butler Kim and I were creating a warm senior-junior atmosphere, Team Leader Choi suddenly cut in.

“Butler Kim. Why don’t you do as Mr. Jin says?”

*What an ill-mannered bastard. How dare he tell such a senior what to do…*

*Hmm. He can do that.*

Come to think of it, Team Leader Choi was the bigger shot. He employed a mage from the Ares Guild as his butler.

*What kind of family does he come from?*

Was his grandfather the president and his father the prime minister?

As my curiosity continued to grow, Team Leader Choi went on.

“I think it’s time we sorted out everyone’s forms of address. You’re the face of our Guild, after all. We can’t keep calling you Butler Kim or Uncle forever, can we?”

Butler Kim considered it for a moment before answering.

“I’ll follow the Young Master’s wishes.”

Team Leader Choi nodded and swept his stern gaze over everyone present.

“Then from now on, we’ll all address Butler Kim as Guild Master. No objections, correct?”

Im Kkeokjeong and Miss Song answered.

“Man, this meat is incredible. Is it because it was grilled with magic?”

“The booze is going in. Booze! Down it goes, down it goes!”

“……”

Team Leader Choi gazed at the two of them with regret before turning his eyes toward me. I had raised one arm conspicuously.

“What does that mean?”

“I have a question.”

*At least this guy is a little better.*

Team Leader Choi spoke with an expression that seemed to say as much.

“Go ahead.”

“Wasn’t Team Leader Choi the Guild Master?”

“……”

Team Leader Choi wore an expression as if he had been betrayed, then pulled something from inside his coat and handed it to me. I took it and looked at it. It was a business card.

“I have this.”

“What does it say?”

“Choi Minwoo, Team Leader of Team 1, Peace Guild.”

“Yes. I’m the Team Leader.”

“Oh.”

“Butler Kim is the Guild Master. I’m the Team Leader. The other three are team members. Do you understand now?”

I didn’t know whether Butler Kim was a boss in name only or merely a figurehead, but I nodded anyway. If I didn’t, Team Leader Choi looked like he might cry.

“Did everyone else understand?”

At Team Leader Choi’s question, Im Kkeokjeong and Miss Song answered.

“Wow, even the liquor tastes amazing. Is it because we have magically grilled meat for an appetizer?”

“How long are you going to make me do the shoulder dance? It’s dislocated! Dislocated! Dislocated!”

“……”

*Hey, are you crying?*

[^2]: School ties, regional ties, and blood ties are traditionally regarded in Korea as major sources of social connections and influence.
```
