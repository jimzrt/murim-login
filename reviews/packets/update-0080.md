<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0080.txt",
      "sha256": "d8cbff0990a51f8703fb9019c64f28f3f84e0a21ab9ae00de4675578465e235c",
      "bytes": 13074
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "13aaefea0d63e7e56367b0764c0043fac50845afdeefe6d6391fed8cb3959196",
      "bytes": 7510
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "a859d36481cc25a9326e4962e8169bcdb7a63976a041a1a097e673ced7578021",
      "bytes": 5565
    },
    {
      "path": "characters/Im Kkeokjeong.md",
      "sha256": "a110b00dbd79b98d06d662393adb777f4f6e1802d9a357ca2c4c3d043eeb0bc1",
      "bytes": 1610
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8217834ff68c2d3022c7ee5c0460029217fe3749d298ec7864fbe6a3a050340e",
      "bytes": 5331
    }
  ],
  "estimated_tokens": 12466
}
-->

# Durable State Update — Chapter 80

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 80. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 80. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 80,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 80,
    "continuity_sources": [80],
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
    "Taekyung is a member of the Peace Guild, completed the Guild Membership achievement, and received 10 points. His contract provides a 500 million won signing bonus, a fixed monthly salary of 50 million won, a seventy-percent settlement share, housing, a car, and other benefits.",
    "The Peace Guild's Guild house is Sooni's Super, a dilapidated corner store in Bucheon's Gate-dense district, on property purchased from the former owner's surviving family for slightly more than 2 billion won per pyeong.",
    "Im Kkeokjeong joined the Peace Guild after Team Leader Choi recruited him while hospitalized. He is married and has two children.",
    "The Peace Guild has five members: Taekyung, Team Leader Choi, Butler Kim, Im Kkeokjeong, and Song Song. Butler Kim is the Guild Master, Team Leader Choi leads Team 1, and the other three are team members.",
    "Essence of the Himalayas increases Taekyung's Intelligence by 1 for one hour.",
    "Team Leader Choi formerly served as a Team Leader in the Ares Guild, where Song Song was a member of his team. Butler Kim is a retired mage and former Hunter who trained at Nonsan's 28th Regiment, 1st Battalion, as did Taekyung.",
    "The Peace Guild is preparing for its first raid. Choi Minwoo is Level 75, Kim Hwajong Level 80, Song Song Level 64, and Im Hyeokjun Level 24.",
    "A Bucheon Terminal Guild raid against seven B-rank Minotaurs ended with the monsters defeated but two C-rank Hunters dead, making Taekyung judge the Peace Guild's coming raid dangerous."
  ],
  "continuity_sources": [
    79
  ],
  "open_questions": [
    "The identity and sponsor of the assassin who attacked Taekyung and Hyuk Mujin remain unconfirmed.",
    "It remains unresolved whether Hyuk Mujin will actually become the next Master of the Gatekeeper Pavilion.",
    "It remains unresolved whether the Shanxi sects will answer Jin Wikyung's summons and whether he will become Alliance Leader.",
    "It remains unresolved whether Song Sword Sect has any connection to the attack.",
    "The reason the System displayed the same 2-hour-22-minute Time Limit twice remains unexplained.",
    "The nature of the minor misunderstanding that injured Childeuk remains undisclosed.",
    "Taekyung's prior relationship with Lee Seowol and the missing details of his memories about her remain unclear.",
    "Butler Kim's former Hunter rank and background remain unclear, and it is unclear whether Song Song heard Taekyung's interrupted confession."
  ],
  "safe_through": 79,
  "temporary_decisions": [
    "Use gongcheong seokyu for 공청석유 with a footnote explaining the elixir and petroleum pun; use junzi for 군자 and Junzi Sword for 군자검 with a cultural footnote; render 도덕책 as ethics textbook with a footnote explaining the pun.",
    "Retain Hyung-nim for 형 and 형님 in Taekyung's deferential speech; use Three Questions Gorge for 삼문협, Great Hero for 대협, and Ghost Sword for 귀검.",
    "Use Alliance Leader for 맹주 and summon for 소집; use New Year's Day for 원단 and close the sect's gates for 봉문.",
    "Use Sleep Mode for 수면 모드, Medicine King Hall Master for 약왕당주, four-horse carriage for 사두마차, and goshiwon for 고시원 with a footnote.",
    "Use Return for 귀환, Returnee for 귀환자, Ren and Du meridians for 임독양맥, Heart Demon for 심마, Paralysis Acupoint for 마혈, and Mute Acupoint for 아혈.",
    "Use fist-and-kicking technique for 권각술 and recognition for 인정; render 낙류검 as Falling Flow Sword, 질풍십이권 as Twelve Gale Fists, 화염신장 as Flame Divine Palm, and 분근착골 as Tendon-Splitting and Bone-Twisting.",
    "Render 비급 제작 as Martial Arts Manual Creation, 맷집 as Toughness, 천무지체 as Heavenly Martial Physique, 장칠득 as Jang Childeuk, Martial Artist Jang for 장 무인, 인의예지 as benevolence, righteousness, propriety, and wisdom, 호환 as killed by a tiger, 일각 as fifteen minutes, and 모태 솔로 as lifelong single; use “Let's eat noodles” for 국수 먹자 with a cultural footnote.",
    "Use Squad Leader for 조장님, Third Young Master for 삼공자님, Mujin for 무진아, seventh-tier student for 내신 칠 등급, Team Leader Choi for 최 팀장, Designer-Brand Junkie for 명품충, Qi Sense for 기감, Peace Guild for 평화, Essence of the Himalayas for 히말라야의 정수, Sooni's Super for 순이네 수퍼, Song Song for 송송이, Miss Song for 송이 씨, Taurus for 황소자리, Ares Guild for 아레스 길드, Senior for 선배님, Young Master for 도련님, Guild Master for 길드장님, Minotaur for 미노타우로스, Bucheon Terminal Guild for 부천터미널 길드, The Minotaur's Labyrinth for 미노타우로스의 미로, haejangguk for 해장국, and makgeolli for 막걸리."
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
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |

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
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |

## Exact glossary matches

| 무림     | **Murim**          |
| 김화종    | **Kim Hwajong**   |
| 임창수    | **Im Changsoo**   |
| 절정     | **Peak**          |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 장비               | **Equipment**                  |
| 아이템              | **Item**                       |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 몬스터     | **monster**           |
| 레이드     | **raid**              |
| 길드      | **Guild**             |
| 길드장     | **Guild Master**      |
| 팀장      | **Team Leader**       |
| 마법사     | **mage**              |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 임꺽정 | **Im Kkeokjeong** |
| 평화 | **Peace Guild** | Guild name. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |

## Listed compact profiles

### Im Kkeokjeong.md

# Im Kkeokjeong (임꺽정)

- **Safe through:** Chapter 79
- **Aliases:** Im Hyeokjun; Kkeokjeong hyung; Uncle Kkeokjeong
- **Role:** E-rank Hunter; veteran member of the Peace Guild’s Gate party and current member of the Peace Guild
- **Personality:** Good-natured, sociable, modest about his family, and shamelessly confident about their age difference
- **Voice:** Hearty, casual, teasing, and quick to laugh
- **Relationships:** An old acquaintance of Jin Taekyung from the Ilsan manpower office; calls Taekyung his little brother, recommends him to Team Leader Choi, and is married with two children

## Korean source

```text
＃80화



게이트 관리소.

번쩍거리는 갑옷을 입은 청년이 얼굴을 구겼다.

“그러니까, 왜 안 되냐고.”

B급 게이트인 ‘미노타우로스의 미로’를 담당하는 공무원이 곤란한 기색을 내비쳤다.

“이미 말씀드렸잖습니까. 지난주에 있었던 사망 사고 때문에…….”

“내가 지금 그걸 몰라서 물어? 알 만한 사이에 왜 이렇게 빡빡하게 구냐, 이거지.”

“안전 단속 기간입니다. 인원이 부족하면 저도 허가해 드리기가 곤란해요.”

공무원은 죽을 맛이었다.

사망 사고가 발생한 게이트는 일주일간 안전 단속이 들어온다. 즉, 게이트 입장 인원이나 수준을 높여 사고를 방지하겠다는 건데…… 눈앞의 청년은 막무가내였다.

“평소보다 좀 더 넣었다. 됐지?”

“이게 무슨!”

청년이 불쑥 내민 흰 봉투에 공무원은 화들짝 놀라 주위를 살폈다. 얼마 전에 들어온 신입 하나가 눈을 동그랗게 뜨고 자신을 바라보고 있었다.

“이, 이러시면 안 됩니다.”

“안 되긴 무슨. 지금까지 잘 받아 놓고.”

“…….”

“게이트 담당이 원래 이런 재미지. 맞잖아?”

청년의 노골적인 말에 중년 공무원은 얼굴이 벌겋게 달아올랐다. 그의 말대로 하루 이틀 일은 아니지만 신입 앞에서 이 무슨 개망신이란 말인가.

하지만 어차피 엎질러진 물이다. 두툼한 흰 봉투만큼 공무원의 양심은 얇아졌다.

“……지금 팀 구성이 어떻게 되십니까?”

“나 포함해서 열 명.”

“열 명이요?”

“B급 다섯에 C급 다섯. 왜, 문제 있어?”

당연히 있다. 바로 지난주 있었던 사고의 당사자인 부천터미널 길드는 B급 헌터 다섯에 C급 헌터 열 명이 참여했고, 그들이 어떻게 됐는지는 지역 신문 1면에 대대적으로 실렸으니까.



[허술한 레이드가 불러온 참사]

[부천터미널 길드장, 헌터 협회 조사에 적극적으로 임할 것]



이런 상황에 열 명이라니. 공무원이 갈등하던 그 순간이었다.

“아저씨, 잠깐만.”

방금까지만 해도 험악한 얼굴로 쪼아 대던 청년의 얼굴에 언제부터인지 웃음이 맺혀 있었다.

“어차피 숫자는 얼추 맞춰야 하잖아. 그치?”

“아, 예. 그럼 좋죠.”

“그럼…… 쟤들 끼워서 가자. 모양새 좋게.”

공무원은 청년의 손가락을 따라 고개를 돌렸다. 막 관리소로 들어온 다섯 명의 남녀가 보였다.

‘중년 남자 둘. 젊은 놈 둘. 그리고…….’

끝내주는 미인 하나.

청년의 시선이 떨어지지 못하는 걸로 봐서, 속셈이 뭔지는 안 봐도 뻔했다.

“이제 됐지?”

빠르게 셈을 끝마친 공무원이 봉투를 집어 들었다.

“문제없습니다.”



* * *



중년의 공무원은 친절하게 상황을 설명해 주었다.

지금은 안전 단속 기간이라는 사실과 그로 인해 입장이 지연되는 길드들이 꽤 많다는 것. 현재 우리 인원으로는 용병을 구하든가, 다른 길드와 합류해야 한다는 사실까지.

“운이 좋으시네요. 상동 길드에서 온 분들이 대기 중이신데 딱 다섯 분이 부족하거든요.”

“저희까지 합류하면 게이트 진입까지 얼마나 걸리겠습니까?”

“들어오시면 바로 처리할 수 있습니다.”

그럼 우리야 땡큐지. 실질적인 결정권자인 최 팀장도 별말 없이 고개를 끄덕였다.

“그럼 좋습니다.”

길드장을 맡은 김 집사가 계약서에 서명한 그때, 불쑥 끼어드는 목소리가 있었다.

“반가워요. 상동 길드에서 팀장직을 맡고 있는 임창수라고 합니다.”

유들유들한 목소리와는 다르게 제법 다부진 체격이다.

성큼성큼 걸어오는 그의 모습에서 감출 수 없는 자신감이 흘러나왔다.

‘상동 길드 정도면 그럴 만하지.’

상동 길드는 부천 인근에서 다섯 손가락 안에 드는 중견 길드로, 소속된 B급 헌터만 스무 명이 넘는다.

기껏해야 20대 후반으로 보이는데 직책은 팀장이라니. 고스톱으로 올라갈 수 있는 자리가 아니다.

‘한가락 하는 놈이네.’

뒤이어 끌어 올린 [기감]이 짐작을 확신으로 바꿔 주었다.



[Lv.65 임창수]



그런데 어째 이름이 낯이 익다. 어디서 들어 봤더라?

내가 고개를 갸웃거리는 사이 김 집사가 인사를 건넸다.

“안녕하십니까. 평화 길드의 김화종입니다.”

우리야 김 집사님, 아저씨, 김 형 등등으로 부르고 바지 길드장인 걸 알고 있지만 외부인 시선에서는 딱 봐도 책임자일 거다.

임창수가 환하게 웃으며 응대했다.

“아하, 평화 길드요. 이름은 많이 들었습니다.”

옆에 서 있던 임꺽정과 송이 씨가 소곤거렸다.

“송 양, 우리 길드 만들어진 지 얼마나 됐지?”

“음. 2주 정도 됐을걸요?”

“레이드는? 많이 했어?”

“무슨 말씀이세요. 길드 하우스 리모델링도 시작 안 했는데. 이게 첫 공식 레이드예요.”

“…….”

B급 헌터쯤 되면 아무리 작게 말해도 다 들리는 법이다. 임창수의 고개가 두 사람을 향했다.

“이분들은?”

“우리 길드원들입니다.”

그의 시선이 두 사람을 스쳤다. 임꺽정에게 잠깐, 그리고 송이 씨에게는 좀 더 길게.

“그렇군요. 이거 제가 괜한 말을 해서, 하하.”

“별말씀을요.”

“어찌 됐든 이것도 인연인데, 기왕 한 팀이 됐으니 잘 부탁드립니다.”

“네, 그럼 저희는 장비로 갈아입고 오겠습니다.”

“게이트 앞에서 기다리죠.”

번쩍거리는 사슬 갑주를 쩔그럭거리며 떠나는 임창수의 뒷모습을, 최 팀장이 심각한 얼굴로 응시했다.

“저 사람…….”

“무슨 문제라도 있어요?”

“장비가 한정판이네요. 저거 굉장히 구하기 어려운 건데.”

“…….”

어, 그래. 비싸 보이긴 하더라.



* * *



헌터는 선망받는 직업이다. 대격변으로부터 인류를 지켜 낸 수호자들이라서……인 것도 있겠지만 일단 돈을 많이 벌기 때문이다.

최하급 헌터였던 나도 빡세게 생활해서 연봉 1억 이상은 벌었으니 두말할 것도 없다.

‘문제는 나가는 돈도 많다는 거지만.’

지출 중 가장 큰 비중을 차지하는 것이 바로 장비다.

기본적으로 마정석이 들어가니 아무리 가성비를 따져도 돈이 왕창 깨질 수밖에 없다. 거기에 꾸준한 관리와 파손 시 수리비까지.

가슴이 찢어지는 건 둘째치고 통장 잔고가 찢어진다.

‘장비 관련 보험이 괜히 나온 게 아니지.’

그런 의미에서 최 팀장의 최고의 고용주다.

고급 장비를 무상 대여해 주니까.

돌돌돌.

캐리어를 끌고 탈의실로 들어온 최 팀장이 우리를 불렀다.

“각자 포지션에 맞게 괜찮은 것들로 골라 왔습니다. 하나씩 가져가세요.”

단기 여행용으로나 쓸 법한 조그마한 캐리어다. 임꺽정이 실망한 얼굴로 중얼거렸다.

“내 건 없나 보네.”

최 팀장의 입꼬리가 슬며시 올라갔다.

“그럴 리가요. 이게 뭔지 아시면 깜짝 놀라실…….”

“어, 이거 공간 확장 마법이 걸린 캐리어네.”

“…….”

딱 맞췄군.

내 정확한 예측에 미소가 흐릿해진 것도 잠시. 순식간에 마음을 추스른 최 팀장이 재차 입을 열었다.

“맞습니다. K사에서 제작한 공간 확장 캐리어. 북미 최고의 장인으로 알려진 니콜라스가…….”

덜컹!

“우와, 진짜네! 태경아, 이거 봐라. 안이 엄청 넓어!”

“그러네요.”

“그밖에도 세계 굴지의 디자이너들이 참여…….”

“이야, 이런 건 또 처음 보네. 그냥 여기 들어가서 자도 되겠는데?”

“캐리어 닫으면 누가 열어 주기 전까진 못 나올걸요.”

“그런가?”

“해당 제품은 항상 적절한 온도와 환기를 통해 보관한 물건을 최상의 상태로…….”

철컥, 철컥.

“이거 엄청 멋있네. 어떠냐, 나 잘 어울려?”

“찰떡인데요. 맞춤 정장인 줄.”

“너도 멋있다. 그건 뭐야?”

“흑색 드레이크 가죽 세트라는데요? 아니, 가죽 세트예요.”

“그래? 최 팀장 거니까 좋은 거겠지 뭐. 으하하! 최 팀장 고마워!”

“……별말씀을.”

완전히 전의를 상실한 최 팀장이 힘없이 장비를 갈아입는 사이, 나는 입고 있는 장비들을 하나씩 확인해 나갔다.

‘아이템 확인.’

띠링.



아이템창



[장인의 흑색 드레이크 가죽 세트]

종류 : 갑옷

등급 : 절정

설명 : B급 몬스터 흑색 드레이크의 가죽으로 제작된 갑옷 세트. 훌륭한 장인의 손길이 느껴진다.

효과 : 근력, 체력, 민첩, 맷집 +10

- 풀 세트 효과가 적용 중입니다.





아이템창



[장인의 검은 가시 창]

종류 : 창

등급 : 절정

설명 : B급 몬스터 흑색 드레이크의 척추 뼈로 제작된 창. 매우 단단함과 동시에 날카롭다. 훌륭한 장인의 손길이 느껴진다.

효과 : 적에게 명중 시 90% 확률로 [출혈] 발동





확인 뒤 드는 생각은 딱 하나다.

‘미쳤네.’

착용하는 것만으로도 40포인트가 부여되는 갑옷에, 찌르는 족족 과다 출혈로 사망시킬 수 있는 창까지.

아이템 정보만 봐도 어마어마한 효과라는 걸 알 수 있었다.

‘이런 게 템빨이구나.’

무림에서의 기억을 문득 떠올리니 눈물이 앞을 가린다.

갑옷은 개뿔, 보들보들한 천 쪼가리 걸치고 싸구려 창만 수십 자루는 부러트렸다. 무림인들이야말로 하드보일드의 진수, 진정한 상남자들이 아닐 수 없다.

“명품이라 그런지 느낌부터 확실히 다르네.”

옆을 돌아보니 상기된 표정의 임꺽정이 제자리에서 펄쩍펄쩍 뛰고 있었다.

“무지 가볍고, 몸도 빨라진 것 같고. 기분 탓인가?”

“아닐걸요.”

기분 탓일 리가 있나. D급 헌터인 임꺽정을 위해서 최 팀장이 준비한 장비인데 당연히 좋은 거겠지.

‘살짝 확인해 볼까?’

내가 임꺽정이 입고 있는 풀 플레이트 메일에 손을 올리려던 그때, 어느새 장비를 갖춘 최 팀장이 다가왔다.

“준비되셨으면 출발하시죠.”

“김 집사님은요?”

“밖에서는 길드장님입니다.”

나를 향한 최 팀장의 일침에 김 집사가 허허 웃었다.

“괜찮습니다. 그리고…… 전 항상 장비를 입고 있어서요.”

말과 함께 정장 단추를 푸니 양 손목의 팔찌와 목걸이가 드러났다. 물론 일반적인 장신구가 아니다.

마정석이 박힌 목걸이와 기이하면서도 아름다운 문양이 음각된 팔찌.

“아티팩트(Artefact)?”

“지팡이보다는 이게 더 편하더군요.”

김 집사는 겸손하게 대답했지만 저 정도로 간편한 복장의 마법사는 흔치 않다. 생존율을 높이기 위해 경갑옷이나 호신용 지팡이 하나쯤 들고 있는 게 보통이지.

‘뭐, 보통 마법사는 아니겠지.’

아레스 길드 출신이라고 하면 다들 한 수 접고 들어간다.

문득 김 집사의 과거가 궁금해졌지만 다음 순간 의문은 깨끗이 지워졌다.

똑똑.

“남자분들. 아직 멀었어요?”

“아, 준비 끝났습니다.”

탈의실 밖에서 들려온 송이 씨의 목소리. 최 팀장이 대답하자마자 문이 살며시 열렸다.

“빨리 가요. 사람들 기다릴 텐데.”

“헉.”

질끈 올려 묶은 긴 생머리. 가벼운 가죽 갑옷을 착용한 그녀의 모습에 나는 헛숨을 삼켰다.

‘사람이 이렇게 예뻐도 되나.’

콩깍지가 아니라 사실이 그렇다. 지금까지 귀여운 조카 대하듯 굴던 임꺽정이 침을 삼키는 것만 봐도 알 수 있다.

꿀꺽.

“…….”

이 인간 조심해야겠군.

어쨌든 임꺽정이 이 정도인데 다른 놈들이야 말할 것도 없을 거다. 좀 젊고 한가락 한다 싶은 놈들이 트럭으로 몰려와 껄떡거릴 게 분명하다.

‘예를 들면 임창수라든지, 임창수라든지. 혹은 임창수라든지…….’

임창수. 상동 길드의 젊은 팀장.

아까부터 자꾸 놈의 얼굴이 눈앞에 어른거린다.

‘분명히 처음 보는 얼굴인데.’

그런데…… 왜 이렇게 신경이 쓰일까. 그 자식이 송이 씨한테 관심 있어 보여서 그런가?

“뭐 해? 안 나오고.”

“아, 네.”

생각은 이어지지 못했다. 임꺽정의 재촉에 나는 황급히 탈의실을 빠져나갔다.
```

## Final English reading copy

```markdown
# Chapter 80

Gate Management Office.

A young man in gleaming armor scowled.

“So why isn’t it allowed?”

The public official in charge of the B-rank Gate *The Minotaur’s Labyrinth* looked troubled.

“I already told you. Because of the fatal accident last week……”

“You think I don’t know that? What I’m saying is, why are you being so uptight with someone you know?”

“It’s a safety-inspection period. If you’re short on personnel, I can’t exactly approve your entry.”

The official was at his wit’s end.

Any Gate where a fatal accident occurred was subjected to a week of safety inspections. In other words, they raised the required number or level of personnel to prevent another accident. But the young man in front of him was being completely unreasonable.

“I put in a little extra this time. Good enough?”

“What is this!”

The official jumped at the white envelope the young man thrust out and glanced around in alarm. A new employee who had joined the office recently was staring at him with wide, round eyes.

“You—you can’t do this.”

“Can’t do what? You’ve been taking it just fine until now.”

“……”

“Being in charge of a Gate is supposed to have perks like this, right?”

At the young man’s blatant remark, the middle-aged official’s face flushed red. It wasn’t as if this was anything new, but what kind of disgrace was this in front of a new employee?

Still, the milk had already been spilled. His conscience grew thinner in proportion to the thickness of the white envelope.

“So……how is your team composed at the moment?”

“Ten, including me.”

“Ten?”

“Five B-ranks and five C-ranks. Why? Is there a problem?”

Of course there was. The Bucheon Terminal Guild, which had been involved in last week’s accident, had sent five B-rank Hunters and ten C-rank Hunters into the Gate. What happened to them had been plastered all over the front page of the local newspaper.

> **The Tragedy Brought on by a Shoddy Raid**
>
> **Bucheon Terminal Guild Master to Cooperate Fully with Hunter Association Investigation**

And now they were talking about ten people. Just as the official was hesitating—

“Hey, mister. Hold on.”

The young man’s menacing face had somehow acquired a smile.

“The numbers have to be roughly right anyway, don’t they?”

“Ah, yes. That works.”

“Then let’s take those guys along. Make it look good.”

The official followed the young man’s finger and turned his head. Five men and women had just entered the management office.

*Two middle-aged men. Two young men. And……*

One stunningly beautiful woman.

Judging by how the young man couldn’t take his eyes off her, his intentions were obvious.

“Good enough now?”

After quickly finishing his calculations, the official picked up the envelope.

“No problem.”

* * *

The middle-aged official kindly explained the situation to us.

It was currently a safety-inspection period, which meant that quite a few Guilds were experiencing delays in entering Gates. He even explained that with our current numbers, we would either have to hire mercenaries or join up with another Guild.

“You’re in luck. The people from Sangdong Guild are waiting, and they’re exactly five people short.”

“If we join them, how long will it take until we can enter the Gate?”

“We can process it immediately once you join.”

*That worked great for us.*

Team Leader Choi, who held the real decision-making power, nodded without objection.

“Then that sounds good.”

Just as Butler Kim, the Guild Master, signed the contract, an unexpected voice cut in.

“Nice to meet you. I’m Im Changsoo, the Team Leader from Sangdong Guild.”

His voice was smooth and easygoing, but his build was quite solid.

Unmistakable confidence radiated from him as he strode over.

*Sangdong Guild was strong enough to justify it.*

Sangdong Guild was one of the five leading mid-sized Guilds in the area around Bucheon, with more than twenty B-rank Hunters alone.

He looked to be in his late twenties at most, yet he was already a Team Leader. That wasn’t a position one could luck into over a game of cards.[^1]

*This guy’s no pushover.*

The Qi Sense I activated soon afterward changed my guess into certainty.

> **System**
>
> **Level 65 — Im Changsoo**

And yet, his name sounded familiar. Where had I heard it before?

While I was tilting my head, Butler Kim greeted him.

“Hello. I’m Kim Hwajong of Peace Guild.”

We called him Butler Kim, Uncle, Kim Hyung, and plenty of other things, and we knew he was only a figurehead Guild Master. But from an outsider’s perspective, it was obvious at a glance that he was the person in charge.

Im Changsoo answered with a bright smile.

“Ah, Peace Guild. I’ve heard the name quite a bit.”

Im Kkeokjeong and Miss Song, who were standing beside him, whispered to each other.

“Miss Song, how long has our Guild been around?”

“Hmm. About two weeks, I think?”

“Raids? Have we done many?”

“What are you talking about? We haven’t even started remodeling the Guild house. This is our first official raid.”

“……”

A B-rank Hunter could hear everything, no matter how quietly someone spoke. Im Changsoo’s head turned toward the two of them.

“And who are these people?”

“They’re Guild members.”

His gaze passed over the two of them—briefly over Im Kkeokjeong, then lingering a little longer on Miss Song.

“I see. I said something unnecessary, haha.”

“Not at all.”

“In any case, it seems fate brought us together. Since we’re on the same team now, I look forward to working with you.”

“All right, then. We’ll go change into our gear and be right back.”

“We’ll wait for you in front of the Gate.”

Team Leader Choi watched Im Changsoo’s back as he walked away, his gleaming chainmail clanking with every step. His face was serious.

“That man……”

“Is there a problem?”

“His equipment is limited edition. That stuff is incredibly hard to get.”

“……”

Oh. Right. It did look expensive.

* * *

Hunters were an enviable profession. Partly because they were guardians who had protected humanity from the Great Cataclysm……but mainly because they made a lot of money.

Even I made over 100 million won a year as a lowest-rank Hunter by working my ass off, so that said it all.

*The problem was that they spent a lot, too.*

The single biggest expense was equipment.

Magic Gems went into equipment as a matter of course, so no matter how carefully you considered cost-effectiveness, you couldn’t help but spend a fortune. On top of that, there were regular maintenance costs and repair fees whenever something broke.

The heartbreak was one thing. Your bank balance got ripped apart.

*There was a reason equipment insurance existed.*

In that regard, Team Leader Choi was the best employer ever.

He loaned us high-end equipment for free.

Rumble, rumble.

Team Leader Choi came into the changing room pulling a suitcase and called us over.

“I picked out decent equipment suited to each of your positions. Take one set each.”

It was a small suitcase, the sort you might use for a short trip. Im Kkeokjeong muttered in disappointment.

“Guess there isn’t one for me.”

The corners of Team Leader Choi’s mouth curled up.

“Of course there is. If you knew what this was, you’d be shocked……”

“Oh, this is a suitcase with a space-expansion spell on it.”

“……”

He had guessed it exactly.

My accurate prediction briefly wiped the smile off Team Leader Choi’s face. But he quickly composed himself and continued.

“That’s right. A space-expansion suitcase made by K Company. Nicholas, known as the greatest craftsman in North America……”

Clatter!

“Wow, it really is! Taekyung, look at this. It’s huge inside!”

“It is.”

“World-renowned designers also participated……”

“Wow, I’ve never seen anything like this before. I could probably sleep in here.”

“Once you close the suitcase, you won’t be able to get out until someone opens it.”

“Really?”

“This product keeps stored items in optimal condition through proper temperature control and ventilation at all times……”

Click, click.

“This is awesome. What do you think? Does it suit me?”

“It fits you perfectly. I thought it was a tailored suit.”

“You look good too. What’s that?”

“It says it’s a Black Drake Leather Set? No, it’s a leather set.”

“Really? If it’s Team Leader Choi’s, it must be good. Hahaha! Thanks, Team Leader Choi!”

“……Don’t mention it.”

Team Leader Choi had completely lost the will to fight by then and changed into his equipment without another word. I checked each piece of equipment I was wearing.

*Item Check.*

Ding.

> **System**
>
> **Item Window**
>
> **Masterwork Black Drake Leather Set**
>
> **Type:** Armor  
> **Grade:** Peak  
> **Description:** An armor set made from the leather of the B-rank monster Black Drake. You can feel the hand of a superb craftsman in it.
>
> **Effect:** Strength, Stamina, Agility, Toughness +10
>
> — Full Set Effect is active.
>
> **Item Window**
>
> **Masterwork Black Thorn Spear**
>
> **Type:** Spear  
> **Grade:** Peak  
> **Description:** A spear made from the spine of the B-rank monster Black Drake. It is extremely hard and sharp. You can feel the hand of a superb craftsman in it.
>
> **Effect:** Upon hitting an enemy, Bleeding activates with a 90% chance.

After checking them, I had exactly one thought.

*This is insane.*

An armor set that gave me forty points simply by wearing it, plus a spear that could kill an enemy from massive blood loss with nearly every stab.

The item information alone made it clear how incredible the effects were.

*So this is what gear advantage feels like.*

When I suddenly remembered my time in Murim, tears clouded my vision.

*Armor, my ass.*

I had fought in soft scraps of cloth and broken dozens of cheap spears. The people of Murim were the very definition of hard-boiled—the real tough guys.

“Maybe it’s because it’s designer gear, but it feels different right away.”

I turned my head and saw Im Kkeokjeong hopping up and down in place, his face flushed with excitement.

“It’s incredibly light, and I feel like my body’s faster too. Is it just my imagination?”

“I doubt it.”

There was no way it was just his imagination. Team Leader Choi had prepared this equipment specifically for Im Kkeokjeong, a D-rank Hunter. Of course it was good.

*Should I take a quick look?*

Just as I was about to place my hand on the full plate armor Im Kkeokjeong was wearing, Team Leader Choi approached us, already fully equipped.

“If you’re ready, let’s head out.”

“What about Butler Kim?”

“Out here, he’s the Guild Master.”

At Team Leader Choi’s pointed correction, Butler Kim chuckled.

“It’s fine. Besides……I’m always wearing my equipment.”

As he spoke, he unbuttoned his suit jacket, revealing bracelets on both wrists and a necklace. They were not ordinary accessories, of course.

The necklace was set with a Magic Gem, and the bracelets were etched with strange yet beautiful patterns.

“An artifact?”

“This is more convenient than a staff.”

Butler Kim answered modestly, but it was rare to see a mage dressed so lightly. Most carried at least some light armor or a staff for self-defense to improve their chances of survival.

*He’s probably not an ordinary mage.*

Everyone deferred to anyone who came out of Ares Guild.

I suddenly found myself curious about Butler Kim’s past, but the question was wiped clean from my mind the next moment.

Knock, knock.

“Hey, guys. Are you still not done?”

“Ah, we’re ready.”

It was Miss Song’s voice from outside the changing room. As soon as Team Leader Choi answered, the door opened a crack.

“Hurry up. People will be waiting.”

“Whoa.”

Her long, straight hair was tied tightly up, and she was wearing light leather armor. I swallowed a startled breath at the sight of her.

*Can a person really be this beautiful?*

It wasn’t just love making me see her through rose-colored glasses. That was simply the truth. I knew that much just from seeing Im Kkeokjeong, who had treated her like a cute niece until now, swallow hard.

Gulp.

“……”

*I’d better keep an eye on this guy.*

If even Im Kkeokjeong was reacting like this, the other guys would be no exception. Any young man who seemed even moderately capable would come crawling out by the truckload to hit on her.

*Take Im Changsoo, for example. Im Changsoo, say. Or maybe Im Changsoo……*

Im Changsoo. The young Team Leader from Sangdong Guild.

His face had been hovering in my mind since earlier.

*I was sure I’d never seen him before.*

And yet……why was he bothering me so much? Was it because that punk seemed interested in Miss Song?

“What are you doing? Aren’t you coming out?”

“Ah, yes.”

My thoughts were cut short. At Im Kkeokjeong’s urging, I hurried out of the changing room.

[^1]: Go-stop is a Korean card game traditionally played with a deck of flower cards.
```
