<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0104.txt",
      "sha256": "2f28f59ecd0b804d1933d3eb693cb083c6113996e5977fda4af02e96d9be6c0d",
      "bytes": 13063
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "594024fb11b63de61ec6c19204b47164dfac261a2c1984bd7ec1f436a67b4251",
      "bytes": 3204
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "1329763dd22b9879698a2049581afe5d26e7906f65c7006ac8c46fbf75efcad4",
      "bytes": 13525
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "310033612d744d8c6aee4c646b7eae09c449d8cbef847660e69c54c886f1975a",
      "bytes": 5011
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "4e0e4228faf6118a4fd691cd6d2c412da514ca2091f6a845c607fd796ce66af1",
      "bytes": 1221
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "85b7836fc62320b135464124f4ba280fd7dadf91a91fbe37e02ff6b8830a2f38",
      "bytes": 24117
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "b42e925090d5f52a2e93b1728d369df40f7a1f9e6554c4717cfd1f79326429f3",
      "bytes": 8153
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "4829e8f06f0b432ad12e37721fdb83cc281fbf9ec4fc74c8c79be81676435b85",
      "bytes": 13416
    }
  ],
  "estimated_tokens": 16198
}
-->

# Durable State Update — Chapter 104

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 104. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 104. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 104,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 104,
    "continuity_sources": [104],
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
    "Sangdong Guild's Security Team was assigned to surveil Jin Taekyung under Im Chunsoo's direction.",
    "Choi Byungil led the failed operation against Taekyung and was defeated alongside the other five field Hunters.",
    "Kim Junsu is the Security Team's sole Familiar mage, and Hong Woojin is a B-rank Familiar mage hired from outside by Team Leader 1.",
    "Seong Jinho is Taekyung's thirty-year-old civilian goshiwon manager and sworn-brother-like friend in Bucheon.",
    "Im Chunsoo is a Level 75 A-rank ice mage and Guild Master of Sangdong Guild.",
    "Kim Hwajong is a Level 80 mage and former Hunter Training Center instructor known as Butler Kim.",
    "Kim Hwajong trained Im Chunsoo, who was a Class 25 trainee assigned to the 28th Regiment, First Battalion, Second Company.",
    "The property being used as the surveillance base remains unidentified.",
    "The reason Kim Hwajong arrived at the confrontation remains unknown.",
    "Team Leader 1 assesses Taekyung as a top-tier B-rank or A-rank Hunter.",
    "The Security Team faces written disciplinary action, a pay cut, and possible dismissal for the failed assault.",
    "Taekyung owns a two-story detached house in Goyang intended as his family's home.",
    "Taekyung will live alone in the Goyang house until Hayeon finishes her college entrance exam.",
    "Logout is active, so Taekyung no longer needs the capsule to travel between the modern world and Murim.",
    "Seong Jinho unexpectedly emerged from Taekyung's capsule inside the new house after Taekyung logged into Murim.",
    "Taekyung, Mukyung, and Hyuk Mujin are traveling by carriage toward Honju.",
    "Mukyung is a Peak master and uses a superficially learned heat-yang technique to warm Hyuk Mujin.",
    "Taekyung must deliver the Jin Family of Taiyuan's Lunar New Year invitation to the weakened Mount Heng Sword Sect, now led by Lee Seowol, Taekyung's uncomfortable former accuser."
  ],
  "continuity_sources": [
    103
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation remains unknown.",
    "Why Kim Hwajong, despite his former instructor status and exceptional ability, now works as a butler remains unexplained.",
    "What final disciplinary action will be taken against the Security Team remains unknown.",
    "How and why Seong Jinho entered the capsule and emerged inside Taekyung's new house remains unknown.",
    "How Lee Seowol will react to the invitation remains unknown."
  ],
  "safe_through": 103,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술.",
    "Keep Fire Wall as the spell name.",
    "Render Im Chunsoo's 자네 as you while preserving his blunt senior voice.",
    "Render 김화종's 춘수 as Chunsoo.",
    "Render 교관님 as Instructor.",
    "Render 1번 훈련생 as Trainee Number One.",
    "Render 열양공 as heat-yang technique.",
    "Render 원단 as Lunar New Year."
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
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |

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
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 본가      | **our family / this family**                                    |
| 형장      | **Brother** / **Brother [Name]**                                |
| 공자      | **Young Master**                                                |
| 혼주 | **Honju** | Shanxi location |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 103
- **Aliases:** None revealed
- **Role:** Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 103
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 103
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 74
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

## Korean source

```text
＃104화



불야성(不夜城).

그것이 혼주의 첫인상이었다. 어둑한 밤이었음에도 수많은 전각이 늘어선 거리는 등불로 환했고, 사람들의 웃고 떠드는 소리가 끊이질 않았다.

‘생각 이상인데?’

현대의 밤거리만큼은 아니지만 나름 잘 꾸며진 번화가다.

뭐랄까, 그 문화가 가진 고유의 멋이 있다고 해야 하나?

‘오, 저거 좀 멋있네.’

흥미롭게 창밖을 구경 중인 나와는 달리 진무경의 반응은 시큰둥했다.

“소란스럽군. 이럴 바에야 야숙이 훨씬 낫겠어.”

“에이, 어차피 지나가는 길인데 왜 그러십니까.”

혁무진의 넉살 좋은 대답에 진무경의 눈썹이 꿈틀거렸다.

“네놈이 마차만 똑바로 몰았어도 이미 한참 전에 지나쳤다.”

“그전에 이공자님께서 마부만 안 쫓아내셨어도…….”

“뭐?”

“아닙니다. 제가 죽일 놈이죠.”

날카로운 시선에 찔끔한 혁무진이 주절주절 변명을 늘어놓기 시작했다.

“그래도 본가를 대표해서 가는 건데 좋은 곳에서 좋은 거 먹고, 뭐 그래야 하지 않겠습니까? 말들도 쉬게 하고요.”

“무릇 음식이란 허기만 면하면 그만이다. 그리고 우리 중 누가 네게 그렇게 하라고 시키더냐?”

“소가주님이요.”

“……형님께서?”

“예. 수행원들도 없이 가는 거니까 숙식이라도 좋은 곳에서 해결하라고 신신당부하셨습니다.”

내가 저놈 형이었어야 했는데.

성격 더럽고 남의 말은 죽어도 안 듣는 진무경이지만 하나뿐인 형에게는 꼼짝도 못 한다. 머뭇거리던 그가 한숨을 내쉬었다.

“알았으니까 빨리 가기나 해라.”

“옙.”

드디어 1승을 거둔 혁무진이 입가를 씰룩거리며 마차를 몰기 시작했다.



* * *



마차가 멈춘 곳은 4층 높이의 거대한 목조 건물 앞이었다.

봉황객잔. 유려한 필체로 적혀 있는 현판이 인상적이다.

“여기 엄청 비싸 보이는데?”

“대태원진가의 공자님들이 머무르실 곳인데 당연히 비싸야죠. 소가주님께서도 신신당부하셨다니까요, 무조건 최고로!”

“…….”

남의 돈이라고 아주 신났다, 신났어.

고개를 저으며 마차에서 내리자 중학생쯤으로 보이는 점소이가 쪼르르 달려와 허리를 굽혔다.

“어서 옵쇼!”

어린 나이에 서비스 정신이 제법이다. 앞으로 나선 혁무진이 무게감 있는 목소리로 물었다.

“남는 객실이 있느냐?”

“물론입죠. 혹 어떤 방을 원하시는지?”

“가장 큰 곳으로 다오.”

“아, 별채 말씀이십니까요?”

점소이가 우리 일행을 바라봤다. 셋 다 무복 차림이라 그런지 이어지는 말이 조심스럽다.

“죄송하지만 별채는 선불로 절반을 내셔야 합니다.”

“허어, 이런 영악한 놈을 보았나.”

짐짓 얼굴을 굳힌 혁무진이 품에서 묵직한 전낭을 꺼내 들었다. 진위경에게 경비로 받은 돈인 듯싶었다.

“그래, 얼마냐?”

“하루 머무시는데 오십 냥입니다요.”

오십 냥이면 얼마야?

나야 여기서 돈을 사용해 본 적도 없고, 화폐 구조도 모르니 그냥 혁무진에게 맡길 뿐이다.

‘뭐, 알아서 잘하겠지.’

슬쩍 옆을 보니 진무경도 나와 같은 생각을 하고 있는 듯했다.

하긴, 무공 외골수에 부잣집 도련님. 금전 감각과는 도무지 어울리지 않는 배경이긴 하지.

그러나 노동자 계급인 혁무진의 반응은 달랐다.

“뭐? 얼마?”

“오십 냥이요.”

“……철전?”

“예?”

혁무진을 위아래로 훑어본 점소이가 피식 웃었다.

“방 바꿔 드려요?”

“……!”

명백한 비웃음. 입술을 파르르 떨던 혁무진이 이내 호탕한 웃음을 터트렸다.

“으하하! 어린 녀석이 상술이 제법이구나. 바꾸긴 무슨, 어서 별채로 안내해라.”

“그전에 스물다섯 냥은 주셔야 하는데.”

“이놈이 그래도!”

“어이쿠!”

혁무진의 어깃장에 점소이가 움찔 몸을 떨었다.

저 녀석이 우리 사이에서나 괴롭힘 받지, 저래 봬도 일류 무인에 태원진가의 차기 수문각주 후보다.

무공을 모르는 양민, 그것도 겨우 10대에 불과한 어린애는 겁먹을 수밖에 없지.

“바, 바로 안내해 드리겠습니다!”

우리는 바짝 긴장한 점소이를 따라 별채로 이동했다. 가는 길엔 과장 좀 보태서 축구장 크기만 한 정원과 잉어들이 헤엄치는 연못이 보였다.

별채 안은 커다란 방 세 개로 나뉘었고 척 봐도 값나가는 물건들로 장식되어 있었다.

“이야, 방 좋네.”

진무경도 고개를 끄덕였다.

“괜찮군. 이 정도 크기면 수련에도 문제없겠어.”

“…….”

저놈 머릿속은 무공밖에 없나?

내가 별채를 돌아다니며 구경하는 사이 숙박료를 치른 혁무진이 돌아왔다.

“두 분, 식사 안 하십니까?”

“난 됐다. 허기를 참는 것도 일종의 수련이지.”

단호하게 대답한 진무경이 별채를 나서 정원으로 사라졌다.

“조장님은요?”

“내가 저런 미친놈처럼 보이니? 배고파 죽겠다. 빨리 가서 이것저것 다 시켜 먹자.”

순간 녀석의 얼굴이 어두워졌다고 느낀 건 착각일까?



* * *



봉황객잔은 산서성의 명물이다. 그 이유는 총 세 가지로 꼽을 수 있다.

첫째로는 수백의 인원을 수용할 수 있는 크기요, 둘째는 전(前) 황실 숙수가 직접 만드는 요리이며, 마지막 셋째로는 여주인의 미모였다.

그렇다 보니 봉황객잔에는 비싼 가격에도 손님이 끊이질 않았다.

물론 소작농 집안에서 태어난 혁무진은 꿈도 꾸지 못할 곳이었지만.

‘나 같은 놈이 이럴 때 아니면 언제 와 보나.’

반 시진 전만 하더라도 혁무진의 기분은 최고조에 다다라 있었다. 좋은 객실, 맛있는 음식, 그리고 운이 좋은 날에야 볼 수 있다는 여주인의 미모까지.

이 모든 걸 남의 돈으로 즐길 수 있다니!

‘이게 꿈이냐, 생시냐.’

그리고 별채의 하루 숙박료를 듣고 나서 다시 생각했다.

‘이게 꿈이냐, 생시냐.’

같은 말, 다른 느낌.

차라리 꿈이었으면 좋았을 텐데, 정신이 들었을 때는 이미 늦어 버린 뒤였다. 점소이의 비웃음에 홀랑 넘어가 선불 요금까지 냈으니 모든 게 끝장이다.

‘경비로 받은 건 딱 오십 냥이 전부인데.’

은자 오십 냥.

일반적으로 생각했을 때 네 식구의 일 년 생활비가 은자 열 냥이 약간 넘는 걸 감안하면 어마어마하게 큰돈이다.

그러나 봉황객잔의 가격은 일반적인 것과는 수준이 달랐다는 게 문제였다.

‘선불로 스물다섯 냥 줬으니 딱 절반 남았다.’

이마저도 날이 밝으면 없어질 돈이다. 하룻밤 숙박비로 진위경에게 받은 경비를 다 쓰게 생긴 혁무진은 등허리가 축축해졌다.

‘빌어먹을 점소이 놈이 비웃지만 않았어도…….’

후회는 항상 늦는 법.

혁무진은 재빨리 머릿속으로 주판을 튕기기 시작했다.

‘일단 경비는 다 날아갔다. 하지만 혹시 몰라 챙겨 온 비상금이 있으니 어떻게든 해결될지도 몰라.’

은자 다섯 냥. 그가 지금까지 모아 놓은 전 재산이다. 만약의 사태를 대비해 가져온 건데 정말 쓸 줄은 몰랐다.

‘크게 사치만 부리지 않으면 복귀까지 어떻게든 버틸 수 있어.’

그러나 혁무진이 미처 생각하지 못한 부분이 있었다.

바로 진태경의 먹성이었다.

후르르르릅. 꿀꺽. 우걱우걱.

“이야, 입에 쫙쫙 달라붙네.”

“…….”

규화계, 어향육사, 매채구육, 소총반두부, 궁보계정……. 그 외 십여 개의 요리가 줄줄이 탁자 위로 올라올 때마다 진태경의 손이 섬전처럼 움직였다.

“이야, 이거 진짜 맛있다. 육즙이 아주.”

“…….”

“안 먹어? 그럼 남은 것도 내가 먹는다?”

“…….”

“와, 국물이 끝내주네.”

“……많이 드십쇼.”

어느새 혁무진의 볼에는 눈물 한 방울이 또르륵 흐르고 있었다.

‘지금까지 나온 것만 해도 은자 다섯 냥.’

마지막 희망마저 끝장났다. 돌아가는 상황을 보아하니 앞으로 스무 접시는 더 처먹을 기세.

혁무진은 접시로 저 돼지 같은 놈의 머리를 후려갈기고 싶었지만 꾹 참았다. 전 재산에 이어 목숨까지 날리고 싶진 않으니까.

‘옥황상제님, 원시천존님. 제발 저놈을 멈춰 주소서.’

하늘을 원망하던 그때였다.

파창!



* * *



무림에서 가장 힘든 부분이라면 첫째가 생존, 둘째가 음식이다. 어찌 된 건지 하나같이 맵고, 짜고, 기름진 음식들뿐이라 식사 때마다 국물 생각이 간절했다.

그런 의미에서 막 탁자에 오른 이 요리는 각별한 의미가 있다.

‘계용옥미갱(鷄茸玉米羹).’

달걀을 부드럽게 푼, 일종의 옥수수 수프다.

살며시 고개를 숙여 냄새를 맡아 보니 옥수수 특유의 고소한 향이 코끝에 감돌았다.

‘그래, 이거지.’

저절로 웃음이 지어진다. 안 그래도 슬슬 속이 니글거리던 차였다. 계용옥미갱으로 속을 다스린다면 앞으로 열 접시는 더 비울 수 있을 것이다.

‘자, 그럼 이제…….’

기분 좋은 기대감과 함께 뜨끈한 사기그릇을 잡은 그때였다.

파창! 투두두둑!

“……어?”

창졸간에 일어난 일. 탁자 중앙에서 박살 난 술병이 수백 개의 도자기 조각으로 나뉘어 사방으로 비산한다.

거기에 더해 술병 안에 남아 있던 약간의 술까지.

후두두둑.

때아닌 소나기를 고스란히 맞은 나는 할 말을 잃었다.

‘이럴 수가.’

그토록 고대하던 계용옥미갱. 고소하고 부드럽게 내 속을 어루만져 줄 국물은 더 이상 그곳에 없었다.

지금 사기그릇에 담겨 있는 것은 술과 도자기 조각이 들어간 음식물 쓰레기에 불과했다.

맞은편에 앉아 있던 혁무진은 입을 딱 벌렸다.

“오, 옥황상제. 원시천존이시여.”

녀석의 헛소리를 무시하고 술병이 날아온 방향으로 천천히 고개를 돌렸다.

이쪽을 보며 실실 웃고 있는 다섯 놈이 눈에 들어온다.

“어이고, 형장. 미안합니다.”

“손이 미끄러진 걸 누굴 탓해. 다시 시켜 주면 되지.”

“어허, 큰일 날 소리. 저놈 방금까지 먹는 거 못 봤어?”

자기들끼리 킥킥거리는 모습을 가만히 지켜보다가 손을 까딱였다.

처음 내게 사과한 놈. 저놈이 바로 계용옥미앵을 망친 장본인이다.

“뭐, 오라고?”

놈이 피식 웃더니 자리에서 일어나 성큼성큼 다가온다.

땀과 피 냄새가 밴 무복과 왼쪽 허리춤에 찬 곡도(曲刀) 한 자루. 그게 놈이 가진 자신감이었다.

좋아, 이성적으로 대처하자. 나는 침착하게 말문을 열었다.

“옛 성인들께서 말씀하시길, 밥 먹을 땐 개도 안 건드린다고 했다. 정중하게 사과하고 음식 다시 시켜. 계용옥미앵부터.”

“어허, 어린놈이 혀 짧은 것 좀 보게.”

“사과는?”

“얘야, 혀 내밀어라. 뽑아 줄라니까.”

놈이 씩 웃자 시커멓게 썩어들어 간 이빨이 보였다.

끔찍한 구취에 식욕이 씻은 듯이 사라졌다. 아마도 계용옥미앵은 나중에 먹어야 할 듯싶다.

“입 벌려. 주먹 들어간다.”

말과 동시에 놈의 안면에 주먹을 꽂아 넣었다.

콰직!



* * *



봉황객잔이 유명한 이유는 세 가지다.

그러나 사람들, 특히 사내들이 유독 많이 찾는 것은 세 번째 이유 때문이었다.

운 좋은 날에나 만날 수 있다는 미모의 여주인.

그리고 오늘이 바로 그 날이었다.

“소란스럽구나.”

또렷하지만 나른한 여주인의 목소리는 혼잣말이 아니다. 문밖의 인기척이 사라진 것이 그 증거였다.

잠시 후, 문밖에서 조용한 목소리가 들려왔다.

“무인들끼리 싸움이 벌어졌습니다.”

쯧쯧. 작게 혀를 찬 여주인이 입을 열었다.

“죽었느냐?”

“한 명이 다른 여섯을 모두 제압했습니다.”

“어느 곳의 누구라더냐?”

“산서잠룡입니다.”

여주인이 소리 없이 웃었다.

“그거참, 반가운 이름이구나. 간만에 얼굴이나 봐야겠다.”

비스듬히 누워 있던 그녀가 몸을 일으켰다. 창가로 스며든 달빛이 얇은 곰방대를 비췄다.
```

## Final English reading copy

```markdown
# Chapter 104

A city that never sleeps.

That was my first impression of Honju. Even though it was a dark night, the streets lined with countless pavilions were bright with lanterns, and the sound of people laughing and talking never stopped.

*More than I expected.*

It wasn’t quite as lively as a modern city at night, but it was still a well-developed commercial district.

How should I put it? Maybe it had a unique charm born from the culture of this era.

*Oh, that looks pretty cool.*

Unlike me, who was gazing out the window with interest, Jin Mukyung looked unimpressed.

“It’s noisy. We would be better off camping outdoors.”

“Come on, we’re only passing through. Why are you complaining?”

Hyuk Mujin’s cheeky reply made Jin Mukyung’s eyebrow twitch.

“If you had driven the carriage properly, we would have passed through a long time ago.”

“If the Second Young Master hadn’t chased away the coachman in the first place…”

“What?”

“Nothing. I’m the one who deserves to die.”

Stung by the sharp glare, Hyuk Mujin began rambling out excuses.

“Still, we’re representing the family. Shouldn’t we eat something good at a good place? And let the horses rest, too.”

“Food need only satisfy hunger. Besides, who told you to do any of that?”

“The Lesser Family Head.”

“……Brother?”

“Yes. He repeatedly told me that since we were traveling without any attendants, we should at least take care of our meals and lodging somewhere decent.”

*I should’ve been that bastard’s older brother.*

Jin Mukyung had a terrible personality and never listened to anyone, but he was completely helpless in front of his only older brother. After hesitating for a moment, he sighed.

“Fine. Just hurry up and go.”

“Yes, sir.”

Hyuk Mujin had finally won one battle. With the corner of his mouth twitching, he began driving the carriage.



* * *



The carriage stopped in front of a massive wooden building that stood four stories high.

The Phoenix Inn. The signboard, written in elegant calligraphy, was striking.

“This place looks incredibly expensive.”

“Of course it is. This is where the Young Masters of the Jin Family of Taiyuan will be staying. The Lesser Family Head told me repeatedly—he said we had to choose the absolute best!”

“……”

*He’s awfully excited when it’s someone else’s money.*

I shook my head and climbed down from the carriage. A shopkeeper who looked about middle-school age came running over and bowed at the waist.

“Welcome!”

For someone so young, he had quite a bit of service spirit. Hyuk Mujin stepped forward and asked in a weighty voice,

“Do you have any rooms available?”

“Of course, sir. What kind of room would you like?”

“Give us the largest one.”

“Ah, do you mean the private residence?”

The shopkeeper looked over our group. All three of us were dressed in martial artist’s robes, so he chose his next words carefully.

“I’m sorry, but half the fee for the private residence must be paid in advance.”

“Ha! What a shrewd little bastard.”

Hyuk Mujin deliberately hardened his expression and pulled a heavy money pouch from inside his robes. It seemed to be the money Jin Wikyung had given him for expenses.

“Fine. How much?”

“It’s fifty nyang for one day, sir.”

*How much was fifty nyang?*

I had never used money here and didn’t know how the currency worked, so I could only leave it to Hyuk Mujin.

*Well, he’ll handle it somehow.*

I glanced to the side. Jin Mukyung seemed to be thinking the same thing as me.

Then again, he was a martial arts fanatic and the young master of a wealthy family. His background had nothing to do with understanding money.

The reaction of Hyuk Mujin, however, was different.

“What? How much?”

“Fifty nyang, sir.”

“……Iron coins?”

“Excuse me?”

The shopkeeper looked Hyuk Mujin up and down, then let out a quiet laugh.

“Would you like me to change your room?”

“……!”

It was an unmistakable laugh of mockery. Hyuk Mujin’s lips trembled, but soon he burst into hearty laughter.

“Ha ha ha! That’s some impressive business sense for a little brat. Change it? Don’t be ridiculous. Hurry up and show us to the private residence.”

“But you’ll have to give me twenty-five nyang first.”

“You little—!”

“Whoa!”

The shopkeeper flinched at Hyuk Mujin’s show of defiance.

That guy only got bullied when he was with us. Despite appearances, he was a First Rate martial artist and a candidate to become the next Master of the Gatekeeper Pavilion of the Jin Family of Taiyuan.

A commoner who knew nothing about martial arts—and a child barely into his teens at that—could only be frightened.

“I-I’ll show you the way right away!”

We followed the thoroughly tense shopkeeper to the private residence. Along the way, we saw a garden that was, with a little exaggeration, the size of a soccer field, as well as a pond where carp swam.

The private residence was divided into three large rooms and decorated with objects that looked expensive even at a glance.

“Wow, this room is nice.”

Jin Mukyung nodded as well.

“Not bad. At this size, there will be no problem training here.”

“……”

*Is martial arts the only thing in that guy’s head?*

While I was walking around the private residence and looking around, Hyuk Mujin returned after paying for our stay.

“Are you two not going to eat?”

“I’m fine. Enduring hunger is a form of training, too.”

Jin Mukyung answered firmly, then left the private residence and disappeared into the garden.

“What about the Squad Leader?”

“Do I look like that lunatic to you? I’m starving to death. Let’s hurry up and order everything they have.”

*Was it my imagination, or did Hyuk Mujin’s face suddenly darken?*



* * *



The Phoenix Inn was one of Shanxi’s most famous establishments. There were three reasons for that.

First, it was large enough to accommodate hundreds of people. Second, its dishes were prepared by a former imperial-court chef. And third was the beauty of its female proprietor.

As a result, customers never stopped coming to the Phoenix Inn, despite its high prices.

Of course, Hyuk Mujin, who had been born into a family of tenant farmers, had never even dreamed of visiting a place like this.

*If someone like me doesn’t come here at a time like this, when will I ever get the chance?*

Just an hour ago, Hyuk Mujin’s mood had reached its peak. A fine room, delicious food, and even the beauty of the proprietress, whom people said could only be seen on lucky days.

*And I get to enjoy all of this with someone else’s money!*

*Is this a dream or reality?*

Then he heard the price of one night in the private residence and thought about it again.

*Is this a dream or reality?*

The same words. A completely different feeling.

He would have preferred it to be a dream, but by the time he came to his senses, it was already too late. He had fallen completely for the shopkeeper’s mockery and even paid the advance fee. It was all over.

*All I was given for expenses was fifty nyang.*

Fifty silver nyang.

Considering that a family of four generally lived on only a little more than ten silver nyang a year, it was an enormous amount of money.

The problem was that the Phoenix Inn’s prices were on an entirely different level from ordinary prices.

*I gave them twenty-five nyang in advance, so I have exactly half left.*

Even that money would be gone once the sun rose. Hyuk Mujin was about to spend all the expense money Jin Wikyung had given him on a single night’s lodging, and sweat dampened the small of his back.

*If that damned shopkeeper hadn’t laughed at me…*

Regret always comes too late.

Hyuk Mujin quickly began calculating on the abacus in his head.

*The expense money is gone. But I brought some emergency savings just in case, so maybe I can somehow manage.*

Five silver nyang. It was everything he had saved up until now. He had brought it in case something happened, but he had never expected to actually use it.

*If I don’t indulge too much, I should be able to hold out until we return.*

But there was one thing Hyuk Mujin had failed to consider.

Jin Taekyung’s appetite.

Slurp. Gulp. Munch, munch.

“Wow, this really melts in your mouth.”

“……”

Osmanthus chicken, fish-fragrant shredded pork, pork with preserved mustard greens, scallion tofu, Kung Pao chicken… Each time one of those dishes—or one of the more than ten others—arrived at the table, Jin Taekyung’s hand moved like lightning.

“Wow, this is really good. The meat is so juicy.”

“……”

“You’re not eating? Then I’ll eat the rest, too.”

“……”

“Wow, this broth is incredible.”

“……Please, eat as much as you like.”

At some point, a single tear rolled down Hyuk Mujin’s cheek.

*The dishes that have come out so far have already cost five silver nyang.*

His last hope was finished. Judging by the way things were going, that pig would eat another twenty plates.

Hyuk Mujin wanted to smash the pig-like bastard over the head with a plate, but he held himself back. He didn’t want to lose his life after losing his entire fortune.

*Jade Emperor, Primordial Heavenly Venerable. Please, stop that bastard.*

It was just as he was cursing the heavens.

Crash!



* * *



If the most difficult things about living in Murim were ranked, survival would come first and food would come second. For some reason, every dish was spicy, salty, and greasy, leaving me craving soup at every meal.

In that sense, the dish that had just been placed on the table held a special meaning.

*Chicken-and-corn soup.*

It was a kind of corn soup with egg beaten into it until it was silky smooth.

I lowered my head slightly and smelled it. The distinctive savory scent of corn lingered at the tip of my nose.

*Yes, this is it.*

A smile spread across my face on its own. My stomach had already begun to feel greasy. If I settled it with the chicken-and-corn soup, I could probably clear another ten plates.

*All right, then, now…*

Just as I grasped the hot ceramic bowl with pleasant anticipation—

Crash! Clatter, clatter!

“……Huh?”

It happened in an instant. The liquor bottle that had shattered in the middle of the table broke into hundreds of ceramic shards that flew in every direction.

And along with them came the small amount of liquor remaining inside the bottle.

Pitter-patter.

I was drenched by the sudden shower and lost all ability to speak.

*How could this happen?*

The chicken-and-corn soup I had been eagerly awaiting—the warm, savory broth that would gently soothe my stomach—was no longer there.

What now filled the ceramic bowl was nothing more than food waste mixed with liquor and pieces of pottery.

Sitting across from me, Hyuk Mujin stared with his mouth hanging open.

“Oh, Jade Emperor. Primordial Heavenly Venerable.”

I ignored his nonsense and slowly turned my head toward the direction from which the bottle had flown.

Five men were looking this way and snickering.

“Oh, Brother. Sorry about that.”

“Who can you blame when a hand slips? We can just order you another one.”

“Hey, don’t talk crazy. Didn’t you see how much that guy’s been eating?”

I watched them chuckle among themselves, then crooked a finger.

The one who had apologized first—he was the bastard who had ruined my soup.

“What, you want me to come over?”

The man let out a quiet laugh, then stood and strode toward us.

His martial artist’s robes were stained with the smell of sweat and blood, and a curved saber hung at his left hip. That was where his confidence came from.

*All right. Let’s deal with this rationally.*

I calmly opened my mouth.

“The ancient sages said that even a dog shouldn’t be disturbed while it’s eating. Apologize properly and order the food again. Starting with the chicken-and-corn thoup.”

“Well, listen to the little brat lisp.”

“What about the apology?”

“Come on, stick out your tongue. I’ll pull it out for you.”

When he grinned, I saw teeth that had rotted black.

The horrific stench of his breath wiped away my appetite. I supposed I would have to eat the thoup later.

“Open your mouth. My fist is going in.”

At the same time as I spoke, I drove my fist into his face.

Crack!



* * *



There were three reasons the Phoenix Inn was famous.

But the third reason was why people—and men in particular—came here in such great numbers.

The beautiful proprietress, whom one could only meet on a lucky day.

And today was that day.

“It’s noisy.”

The proprietress’s clear yet languid voice was not a soliloquy. The disappearance of the presence outside the door was proof of that.

A moment later, a quiet voice came from beyond the door.

“A fight has broken out between martial artists.”

The proprietress clicked her tongue softly before speaking.

“Did anyone die?”

“One man subdued all six of the others.”

“Who was he, and where was he from?”

“He’s the Sleeping Dragon of Shanxi.”

The proprietress laughed without making a sound.

“What a welcome name. I should go see his face after all this time.”

She had been lying at an angle, but now she sat up. Moonlight filtering through the window illuminated a long-stemmed tobacco pipe.
```
