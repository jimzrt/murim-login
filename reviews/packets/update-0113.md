<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0113.txt",
      "sha256": "f4f4f64c6319fbc7c60c561c9e9fcf5019a6ac323f458107db05daa5b92cea9d",
      "bytes": 12825
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "2c01253d1b5ac603eefc142e96590347fde9e490eb3e1104bb290c91e45fca77",
      "bytes": 2822
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fba5f9a0066f99ae3cb6ef65931aaeecded6defbaad654160c8ba6f1e4dacf70",
      "bytes": 16522
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "f883a0450574246b01d420c3422c15922c3fdd85b828ed25353ceb2135d2d80f",
      "bytes": 724
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "c05684222932d113cf3b9e51eae771384f2398f4eadc6d093824c17a1369c45b",
      "bytes": 5130
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "951a4e9430d51b48f38091b9ca7ac0e63e34bda3488e3d1137cc95bad7083fa2",
      "bytes": 1221
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "d4faabc201182113a1476f07593239569640f07ed6ce23f67406ac5570fde4fd",
      "bytes": 8154
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "44cb11b49c61f2301a07218f2d24cb4483cf73e291f4ae967a5892bce3313b2e",
      "bytes": 3231
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "afe97c24511f7f22f82ae61cfe27894e3aac4d57ea46a67b4c93525bb5083b39",
      "bytes": 749
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "3a745290b611ef9d321ee111e868008f4387122dfb307452e923047fba40cb03",
      "bytes": 684
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "b9a9498513eba506cd197a54f5b335b23b3dd070e394cbcab01745bf4f5648fe",
      "bytes": 2314
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "982cd5b874d0f554868ea591830825c9ff2b47527434c6fdea4fe680879fee38",
      "bytes": 15822
    }
  ],
  "estimated_tokens": 17993
}
-->

# Durable State Update — Chapter 113

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 113. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 113. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 113,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 113,
    "continuity_sources": [113],
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
    "Pung Yang leads the Red Wind Band and commands more than two hundred mounted bandits.",
    "The Red Wind Band has surrounded the Mount Heng Sword Sect without leaving a gap and intends to seize it before sunset.",
    "Pung Yang forbids attacks on commoners to avoid giving the Jin Family of Taiyuan a pretext to intervene.",
    "Pung Yang became a mounted bandit at thirteen after killing a man for dumplings while starving; he was an orphan with exceptional perception and quick thinking.",
    "Pung Yang's first bandit boss was killed by a First Rate master one year after taking him in; Pung Yang later joined another mounted-bandit group under Gwangchil.",
    "Pung Yang reached First Rate by age thirty and rose from squad leader to Red Wind Band Leader three years ago.",
    "The Mount Heng Sword Sect has fewer than one hundred effective defenders after several senior figures fled with their families and followers.",
    "Lee Seowol is the current Sect Leader of the Mount Heng Sword Sect and has prepared ten wagonloads of oil under dried hay throughout the estate.",
    "Lee Seowol intends to delay the battle for one day until Jin Taekyung and Jin Mukyung arrive as reinforcements.",
    "The Red Wind Band's proposed friendship is a coercive choice between total destruction and marriage, with the Mount Heng Sword Sect demanded as the wedding gift.",
    "Cheol Mubaek killed the Red Wind Band envoy with one punch after the envoy delivered the ultimatum.",
    "One hour after the envoy's death, horns began sounding from all directions around the Mount Heng Sword Sect."
  ],
  "continuity_sources": [
    112
  ],
  "open_questions": [
    "What is inside the hard wooden case Pung Yang carries?",
    "What happened three years ago that transformed Pung Yang's position and life?",
    "Whether the Jin reinforcements will arrive before the Mount Heng Sword Sect falls remains unresolved.",
    "Whether Lee Seowol's oil plan will be activated and cause mutual destruction remains unresolved.",
    "What final outcome will follow the battle now beginning around the Mount Heng Sword Sect remains unresolved."
  ],
  "safe_through": 112,
  "temporary_decisions": [
    "Use Peak, early Peak, First Rate, and Third Rate for the established martial-arts ranks.",
    "Use mounted bandits and mounted-bandit groups for 마적 and 마적단; Red Wind Band for 적풍단; and Leader for 단주.",
    "Use Sect Leader for 문주님 and Master of the Gatekeeper Pavilion for 수문각주.",
    "Use rice wine for 탁주, total destruction for 멸문지화, wedding gift for 혼인 예물, and jang for 장.",
    "Retain established renderings for Mount Heng Sword Sect, Jin Family of Taiyuan, Sleeping Dragon of Shanxi, and Heaven Shaking Sword."
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
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |

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
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 체력               | **Stamina**                    |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 공자      | **Young Master**                                                |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 112
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 111
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 112
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 106
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; preparing to consolidate Shanxi Murim under the family's leadership
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 112
- **Aliases:** Blood Wolf Sword
- **Role:** Former Sect Leader of the Mount Heng Sword Sect, killed during the Red Wind Band’s assault; father of Lee Seogeun and Lee Seowol
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Deceased father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; former leader of the Mount Heng Sword Sect; longtime close friend and peer of Cheol Mubaek

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 112
- **Aliases:** None
- **Role:** Current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 112
- **Aliases:** Red Wind Band Leader
- **Role:** Leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 111
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃113화



항산검문으로 사자를 보낸 뒤 반 시진. 풍양은 망설임 없이 명령을 내렸다.

“쳐라.”

속전속결.

시간을 끌수록 그에게는 불리했다. 적풍단이 항산검문을 포위했다는 소문은 빠르게 퍼져 나갈 것이고 외부 세력, 특히 태원진가가 개입한다면 골치 아파진다.

‘어차피 무혈입성은 기대하지도 않았다.’

여인의 몸이라고는 하나 혈랑검 이천백의 핏줄이다.

대화와 손짓으로 길들일 수 없다면 폭력으로 굴복시켜야 한다. 풍양이 지금까지 해 왔던 방식 그대로.

부우우우.

힘찬 뿔피리의 울림이 곳곳에서 울려 퍼졌다. 고원의 마적단들이 사용하는 진격 신호에 항산검문을 에워싼 적풍단의 마적들이 일제히 말의 옆구리를 걷어찼다.

“돌겨어억!”

“한 놈도 남김없이 죽여라!”

두두두두두!

수백 개의 말발굽이 눈 덮인 지면을 짓밟으며 달렸다.

뿔피리 소리는 끊이지 않고 힘차게, 멀리 퍼져 나갔다.



* * *



띠링.



- [운기조식]을 성공적으로 완료했습니다.

- 피로와 체력이 소량 회복됩니다.



시스템 알림음이 들리고 눈을 뜨자마자 주위를 둘러봤다.

“방금 무슨 소리 못 들었어요?”

말에게 건초를 먹이고 있던 월화와 혁무진이 영문을 모르겠다는 얼굴로 묻는다.

“진 공자, 무슨 소리예요?”

“소리야 항상 나죠. 들어 보세요. 말들이 건초 씹는 소리, 바람 소리…….”

“그딴 거 말고, 이 자식아.”

“그럼 뭔데요?”

“부, 부부젤라?”

“부부, 뭐요?”

“스포츠 응원할 때 쓰는…… 됐다. 그런 게 있어.”

나는 설명하는 것을 포기하고 소리가 들려온, 아니 들려왔다고 생각한 방향을 응시했다. 우연의 일치인지 마침 우리가 향하고 있던, 항산검문이 있을 북쪽이다.

‘내가 잘못 들었나?’

월화의 말대로라면 앞으로 세 시진(여섯 시간)은 더 달려야 항산검문에 도착할 수 있다. 무슨 일이 벌어졌다 해도 여기까지 들릴 만한 거리가 아니다.

‘대포 소리라면 모를까.’

때마침 운기조식을 끝마친 진무경도 한마디를 보탰다.

“아무 소리도 안 들렸다.”

“그런데 분명히 뭔가 들은 것 같단 말이지.”

“착각이야.”

“혹시 항산검문에 무슨 일이 난 걸 수도 있잖아.”

“그럴 수도 있지. 하지만 나한테는 아무 소리도 안 들렸다.”

“근데 나는 들은 것 같다니까?”

“그러니까 착각이라는 거다.”

“무슨 근거로?”

“간단하지. 네가 들은 걸 내가 못 들었을 리 없으니까.”

“…….”

이거 상당히 열받는데 맞는 말이라 반박할 수가 없네.

말문이 막힌 나를 보며 진무경이 혀를 찼다.

“눈먼 칼에 죽고 싶지 않다면 심신을 다스리는 것에 집중해라. 전장은 무슨 일이 벌어질지 모르는 곳이니까.”

누가 누굴 가르쳐?

전투 경험으로는 이 중에서 나를 따라갈 사람이 없을 것이다.

워낙 익숙해졌기에 평소와 다름없어 보일 뿐, 전투를 준비하고 참여하는 것에 있어서는 이미 닳고 닳았다.

“적의 숫자가 많으니 공력을 최대한 아끼고 움직임을 최소화해라. 내가 앞장설 테니 뒤따르기만 하면 문제없다.”

그래도 한 핏줄이라고 걱정해 주는 건가?

생각해 보면 지금까지 진무경은 싫어하는 티를 팍팍 내면서도 내게 상당한 도움을 주었다.

수련도 도와주고, 이번에 항산검문도 함께 가 주고, 어린 시절에는 게을러터진 아우를 갱생시키고자 제법 노력도 했다고 들었다.

아무리 진위경의 부탁이 있었다고 해도 정말 나를 싫어했다면 할 수 없는 일들이다.

‘알고 보면 정 많은 놈일지도.’

이런 성격의 사람을 츤데레라고 하나?

새삼 약간 감동이 밀려올 것도 같아 감성적인 눈빛으로 진무경을 바라보는데, 시선이 딱 마주쳤다.

“뭘 봐? 눈 깔아.”

“…….”

“마적 놈들 따위한테 상처 하나라도 입었다가는 내 손에 죽을 줄 알아라.”

“……어, 그래.”

그럼 그렇지. 츤데레는 개뿔. 내가 잠깐 미쳐서 정신 나간 상상을 했구나.

현실을 인정하고 앞서 빼앗은 여분의 말로 안장을 옮기려는데, 어느새 슬쩍 다가온 혁무진이 근심 가득한 얼굴로 입을 열었다.

“이공자님이 저도 죽이는 건 아니겠죠?”

“……난 죽어도 된다는 소리냐?”

“아, 아니 말씀을 왜 그렇게 하세요?”

“넌 반드시 내가 죽이고 죽을 테니까 닥치고 출발 준비나 해.”

뭐라 구시렁거리는 혁무진의 엉덩이를 걷어차 주고 말에 올라탔다.

항산검문까지는 앞으로 세 시진. 이제부터는 정말 일체의 휴식 없이 빡세게 달려야 한다.



제한 시간 : 6:25:19



* * *



항산검문은 하나의 요새 같았다. 높게 쌓아 올린 돌담은 성벽이라 불러도 될 만큼 견고했고 수성(守城)을 위한 각종 방어 시설이 설치되어 있었다.

초대 문주인 이천백의 강경한 의지로 세워진 그것들은 삼십여 년 만에 비로소 제 역할을 발휘했다.

“쏴라!”

쉬쉬쉬쉭!

일제히 쏘아진 수십 발의 화살이 돌진하는 기마를 향해 내리꽂혔다.

그러나 고원에서 가장 흔히 찾아볼 수 있는 병기가 창과 도, 그리고 활이다. 고원의 전투에 익숙한 적풍단의 마적들은 누군가의 명령이 떨어지기도 전에 각자 한 손에 낀 방패를 치켜세웠다.

투둑, 퍼버벅!

낙마한 이는 고작 십여 명.

바짝 마른 나무에 늙은 말의 엉덩이 가죽을 덧대어 만든 방패는 훌륭히 화살들을 막아 냈다.

“크하하핫! 이놈들이 어르신들을 몰라뵙고 감히……!”

적풍단의 조장 하나가 웃음을 터트린 그 순간이었다.

쐐애애액, 퍼걱!

강맹한 기세로 날아온 무언가가 말의 목을 뚫고 조장의 가슴팍에 꽂혔다. 이제 막 일류 초입에 든 그는 믿을 수 없다는 듯 삐죽 튀어나온 화살을 바라보다가 애마와 함께 고꾸라졌다.

뒤따라 달려오던 기마 중 몇 기가 그 때문에 대열이 흐트러져 줄줄이 쓰러진다.

“쇠뇌, 쇠뇌를 조심해라!”

“응사하라!”

쉬쉬쉬쉭!

앞서 항산검문의 공격이 소낙비였다면 적풍단의 화살 세례는 장대비다. 말을 탄 상태에서도 연거푸 시위를 당기는 그들의 화살은 정확하고 빨랐다.

푸푸푸푹!

“크아악!”

“방패 뒤로 몸을 숨겨라! 고개를 내밀지 마!”

그 틈을 타 박차를 가한 마적들은 십여 장 높이의 성벽에 갈고리와 급조한 사다리를 대고 침투를 시도했다.

백병전이 시작된 성벽 위에선 비명과 피가 터져 나왔다.

“크하하! 모두 죽여라!”

“놈들이 올라오지 못하게 막아!”

이소월은 가장 높은 망루에서 이 모든 광경을 지켜보고 있었다. 입술이 파르르 떨리고 얼굴에는 핏기가 사라졌다.

‘이것이 무림.’

죽어 가는 자의 비명, 살고 싶은 자의 몸부림.

마침내 맞닥트린 약육강식의 세계는 그녀가 생각했던 것 이상으로 잔혹하고 두려웠다.

그러나…….

‘물러날 수 없어.’

이미 수많은 이들이 죽었다. 떠날 이들은 떠났고, 남은 이들은 목숨을 걸고 싸우고 있다.

이소월은 이제 그들을 이끌어야 할 문주이며 항산검문과 운명을 함께해야 하는 몸이다.

“문주! 성벽이 위태롭습니다. 지원을 보내야 합니다!”

“놈들이 충차(充車)로 문을 부수고 있습니다!”

“문주! 어서 조치를!”

“문주!”

그 순간, 사방에서 빗발치는 급보를 전해 듣던 이소월이 입을 열었다.

“내가 신호하면 성벽을 향해 화시(火矢)를 한 발, 문을 향해 두 발을 쏘아 올려라. 그리고 철 숙부.”

이소월의 옆을 지키고 있던 철무백이 대답했다.

“뭐든 말하거라.”

“곧 문이 뚫릴 거예요. 잠시 시간을 벌어 주실 수 있나요?”

“나 혼자 말이냐?”

“어려운 부탁을 드려 송구할 따름입니다.”

“일당백(一當百)이라. 언젠가 꼭 해 보고 싶었지.”

“제가 아는 숙부께선 만인적(萬人敵)의 고수십니다. 허나 부디 몸조심하세요.”

“오냐, 내 저런 놈들에게 당할 성싶으냐?”

껄껄 웃은 철무백이 훌쩍 뛰어내렸다. 항산호, 완숙한 절정 고수인 그가 갔으니 풍양이 나서지 않는 한 아무도 문을 넘을 수 없을 것이다.

‘더, 조금만 더.’

치열한 전장을 내려다보던 이소월이 돌연 벼락같은 외침을 토해 냈다.

“지금!”

그녀의 명령을 기다리고 있던 무인 둘이 각각 활시위를 당겼다.

다음 순간, 어느새 어둡게 물든 겨울 하늘 위로 날아오른 불화살이 모두의 머리 위에서 환하게 빛났다.



* * *



유성처럼 떨어지는 불화살은 백 장 너머에 있는 풍양의 눈에도 똑똑히 보였다. 그는 내심 중얼거렸다.

“숨겨 둔 한 수가 있었군.”

짐작이 확신으로 바뀌는 데까지는 그리 오랜 시간이 걸리지 않았다. 잠시 후, 성벽 둘레에서 엄청난 불길이 솟구쳤기 때문이다.

화륵, 화아아악!

“끄아아아악!”

불에 타 죽는 것은 가장 고통스러운 죽음 중 하나다. 성벽 밑에 개미 떼처럼 몰려 있던 적풍단의 마적들이 끔찍한 비명과 함께 몸부림쳤다.

성벽에 걸어 놓은 갈고리의 줄이 끊기고, 목제 사다리가 화염에 휩싸였다.

“쳐라!”

“마적 놈들을 전부 죽여라!”

성벽 밑에서 올라가기를 기다리던 자, 올라가던 자는 불에 타 죽고 이미 올라간 자들은 사방에서 짓쳐 들어오는 병장기에 찔리고 베였다.

“나름 준비를 했다 이거지…….”

덤덤하게 전장을 응시하는 풍양의 시선에 숯검정처럼 곳곳이 까맣게 그을린 채 돌아오는 마적 하나가 들어왔다.

“무슨 일인가?”

“다, 단주님. 피해가 너무 큽니다!”

마적은 그의 앞에 섬과 동시에 넙죽 엎드려 헐떡거리는 목소리로 말을 이었다.

“첫 공격부터 지금까지 족히 일백은 죽은 것 같습니다. 무엇보다 방금 화공(火攻) 때문에 형제들의 사기가…….”

“문은?”

“예?”

“문은 어찌 되었지?”

“뚫긴 했습니다만 항산호 철무백이 홀로 버티고 있어서…….”

“혼자란 말이냐?”

“예. 하지만 워낙 무공이 고강한지라 아무도 나서지 못하고 있습니다.”

“그럼 되었다.”

풍양은 말과 동시에 손을 내밀었다. 무심코 그 손을 맞잡으려던 마적의 신형이 기우뚱 쓰러진다.

어리둥절한 표정으로 굳어 가는 그의 미간에는 비수 한 자루가 깊숙이 박혀 있었다.

“병력은 얼마나 남아 있지?”

풍양의 오른팔 격인 수하에게는 이런 광경이 익숙했다. 시체를 흘끗 바라본 그가 대답했다.

“어림잡아 백오십은 약간 넘고, 이백이 조금 못 됩니다. 우리 측 희생이 더 큰 건 사실입니다.”

“적들은 오죽하겠느냐? 지금 성벽 위에 있는 놈들이 항산검문의 마지막 보루다.”

“저 얼마 안 되는 놈들이 전부란 말씀이십니까?”

“그래.”

“단주님을 못 믿는 건 아닙니다만 방금의 화공처럼 또 다른 함정을…….”

“그걸 노린 게지.”

풍양은 실소를 흘렸다. 누구 머리에서 나온 계략인지는 모르겠지만 제법 머리를 잘 굴렸다.

아마 지금보다 경륜이 부족했다면 풍양 역시 또 다른 함정을 의심하고 병력을 뒤로 물렸을 것이다.

‘시간을 벌기 위해 애쓰는군. 누군가의 지원을 기다리나?’

그렇다면 더욱 망설일 이유가 없다.

중과부적(衆寡不敵). 적풍단이 상당한 피해를 입었다고는 해도 항산검문을 쓸어 버리는 것은 일도 아니다.

거기에 더해…….

“내가 직접 간다.”

“단주님께서 직접 말씀이십니까?”

“그래, 호랑이를 잡아야 하지 않겠느냐?”

너털웃음을 터트린 풍양은 습관적으로 품 안을 더듬었다.

단단한 목곽, 그 안에 호랑이를 단숨에 거꾸러트릴 물건이 들어 있었다.
```

## Final English reading copy

```markdown
# Chapter 113

Half a shichen after sending an envoy to the Mount Heng Sword Sect, Pung Yang gave the order without hesitation.

“Attack.”

A quick, decisive battle.

The longer it dragged on, the worse it would be for him. Word that the Red Wind Band had surrounded the Mount Heng Sword Sect would spread quickly, and if outside forces—especially the Jin Family of Taiyuan—intervened, things would become troublesome.

*I never expected to enter without bloodshed in the first place.*

She might be a woman, but she carried the blood of the Blood Wolf Sword, Lee Cheonbaek.

If words and gestures couldn’t tame her, he would have to subdue her with violence. It was the same method Pung Yang had always used.

Bwooooooong!

The powerful sound of horns rang out from every direction. At the advance signal used by the mounted-bandit groups of the plateau, the mounted bandits surrounding the Mount Heng Sword Sect simultaneously kicked their horses in the ribs.

“Chaaaarge!”

“Kill every last one of them!”

Thundering hooves shook the ground.

Hundreds of horses raced forward, trampling the snow-covered earth.

The horn calls continued without pause, strong and carrying far into the distance.

* * *

Ding!

> **System**
> 
> **Circulate Qi** was successfully completed.
> 
> A small amount of Fatigue and Stamina has been restored.

The moment I opened my eyes at the sound of the System notification, I looked around.

“Did you guys just hear something?”

Wolhwa and Hyuk Mujin, who had been feeding hay to the horses, looked at me in confusion.

“Young Master Jin, what sound?”

“Sounds are always happening. Listen. The horses chewing hay, the wind…”

“Not that crap, you idiot.”

“Then what?”

“A-a vuvuzela?”

“Vuvu… what?”

“The thing people use to cheer at sporting events… Never mind. It’s something.”

I gave up explaining and stared in the direction the sound had come from—or rather, the direction I thought it had come from.

By coincidence, it was the north, where the Mount Heng Sword Sect lay—the very direction we were heading.

*Did I hear it wrong?*

According to Wolhwa, we still had to ride for another three shichen—six hours—before we could reach the Mount Heng Sword Sect. Whatever had happened, it wasn’t something that should have been audible from this distance.

*Unless it was cannon fire.*

Jin Mukyung, who had just finished circulating his qi, added his opinion.

“I didn’t hear anything.”

“But I could have sworn I heard something.”

“You imagined it.”

“Something might have happened at the Mount Heng Sword Sect.”

“That’s possible. But I didn’t hear anything.”

“But I’m telling you, I think I heard something.”

“So I’m telling you that you imagined it.”

“On what grounds?”

“It’s simple. There’s no way I could fail to hear what you heard.”

“…”

That was incredibly irritating, but he was right, so I couldn’t argue.

Seeing me rendered speechless, Jin Mukyung clicked his tongue.

“If you don’t want to die to a stray blade, focus on mastering your mind and body. You never know what might happen on a battlefield.”

*Look who’s lecturing whom.*

When it came to combat experience, no one here could match me.

I only seemed no different from usual because I had grown so accustomed to it. When it came to preparing for and taking part in battle, I was already thoroughly battle-hardened.

“There are a lot of enemies, so conserve your internal energy as much as possible and minimize your movements. I’ll take the lead. Just follow me, and there won’t be a problem.”

*Was he worried about me because we shared the same blood?*

Come to think of it, Mukyung had made his dislike painfully obvious, yet he had still helped me a great deal.

He had helped with my training, agreed to accompany me to the Mount Heng Sword Sect, and, I’d heard, had even made a considerable effort to reform his lazy little brother when they were children.

Even if Jin Wikyung had asked him to, those weren’t things he could have done if he truly hated me.

*Maybe he’s actually a soft-hearted guy.*

Was this what people called a tsundere?

I looked at Jin Mukyung with a sentimental gaze, feeling as though I might actually be moved.

Our eyes met.

“What are you looking at? Lower your eyes.”

“…”

“If you take even a single wound from those mounted-bandit bastards, I’ll kill you myself.”

“…Yeah, sure.”

*That’s more like it. Tsundere, my ass.*

I had briefly lost my mind and imagined something ridiculous.

Accepting reality, I was about to transfer my saddle to one of the spare horses we had taken earlier when Hyuk Mujin approached and spoke with a deeply worried expression.

“Second Young Master, you aren’t going to kill me too, are you?”

“…Are you saying it’s okay if I die?”

“Ah, no! Why are you putting it that way?”

“I’ll kill you before I die, so shut up and prepare to leave.”

I kicked Hyuk Mujin in the rear while he grumbled under his breath, then mounted my horse.

The Mount Heng Sword Sect was still three shichen away.

From this point onward, we had to ride hard without taking a single break.

> **System**
> 
> **Time Limit:** 6:25:19

* * *

The Mount Heng Sword Sect was like a fortress. The stone walls piled high around it were sturdy enough to be called castle walls, and all kinds of defensive facilities had been installed to hold the fortress.

Built more than thirty years ago under the uncompromising will of the founding Sect Leader, Lee Cheonbaek, those defenses were finally serving their intended purpose.

“Fire!”

Whoosh—whoosh—whoosh!

Dozens of arrows launched at once rained down on the charging cavalry.

But the weapons most commonly found on the plateau were spears, swords, and bows. Accustomed to fighting on the plateau, the mounted bandits of the Red Wind Band raised the shields strapped to one arm before anyone even gave the order.

Thud! Thump!

Only a dozen or so men were knocked from their horses.

The shields, made of bone-dry wood faced with hide from an old horse’s rump, did an excellent job of stopping the arrows.

“Ha ha ha! These punks don’t know their elders when they see them, and they dare—!”

That was when it happened.

Fwoosh—crack!

Something came flying with ferocious force. It pierced through a horse’s neck and buried itself in the squad leader’s chest.

He had only just entered the early stages of First Rate. He stared at the arrow protruding from his chest as though he couldn’t believe it, then toppled over together with his prized horse.

Several of the riders behind him lost formation and fell one after another.

“Crossbows! Watch for the crossbows!”

“Return fire!”

Whoosh—whoosh—whoosh!

If the Mount Heng Sword Sect’s attack had been a passing shower, the Red Wind Band’s arrow barrage was a torrential downpour.

Even while mounted, they drew their bowstrings again and again. Their arrows were fast and accurate.

Thwack! Thwack! Thwack!

“Aaargh!”

“Hide behind your shields! Don’t stick your heads out!”

Taking advantage of the opening, the mounted bandits spurred their horses forward and set grappling hooks and makeshift ladders against the walls, which stood more than ten *jang* high. They began attempting to breach the fortress.

A melee erupted atop the walls.

Screams and blood poured forth.

“Ha ha! Kill them all!”

“Stop them from climbing up!”

Lee Seowol watched the entire scene from the highest watchtower. Her lips trembled, and the color had drained from her face.

*So this is the Murim.*

The screams of those dying.

The desperate struggles of those who wanted to live.

The world of the strong preying on the weak that she had finally encountered was more brutal and frightening than she had imagined.

But…

*I can’t retreat.*

Countless people had already died. Those who were going to leave had left, while those who remained were fighting with their lives on the line.

Lee Seowol was now the Sect Leader who had to lead them. She was bound to share her fate with the Mount Heng Sword Sect.

“Sect Leader! The walls are in danger! We need to send reinforcements!”

“They’re breaking down the gate with a battering ram!”

“Sect Leader! You need to take action!”

“Sect Leader!”

As urgent reports rained down from every direction, Lee Seowol opened her mouth.

“When I give the signal, fire one fire arrow toward the walls and two toward the gate. And, Uncle Cheol.”

Cheol Mubaek, who had been standing beside her, answered.

“Tell me what you need.”

“The gate will be breached soon. Can you buy us a little time?”

“By myself?”

“I’m sorry to ask you to do something so difficult.”

“One against a hundred. I’ve always wanted to try that.”

“The uncle I know is a master who can face ten thousand men. But please be careful.”

“All right. Do you think those bastards can get the better of me?”

Cheol Mubaek laughed heartily, then leaped down.

With the Tiger of Mount Heng—a consummate Peak master—there, no one would be able to get through the gate unless Pung Yang himself stepped forward.

*Just a little longer. A little more.*

Lee Seowol watched the fierce battlefield below, then suddenly let out a thunderous shout.

“Now!”

The two martial artists who had been waiting for her command each drew their bowstrings.

The next moment, the fire arrows soared into the darkening winter sky and shone brightly above everyone’s heads.

* * *

The fire arrows falling like meteors were clearly visible even to Pung Yang, who stood more than a hundred *jang* away.

He thought to himself.

*They had a hidden ace.*

It didn’t take long for his suspicion to become certainty.

A moment later, enormous flames erupted around the walls.

Fwoosh! Fwoooosh!

“Aaargh!”

Burning to death was one of the most painful ways to die.

The mounted bandits of the Red Wind Band, massed beneath the walls like a swarm of ants, writhed and screamed horribly.

The ropes attached to the grappling hooks snapped, and the wooden ladders were engulfed in flames.

“Attack!”

“Kill every last one of those mounted-bandit bastards!”

Those waiting below to climb and those still making their way up burned to death. Those who had already reached the top were stabbed and slashed by weapons converging from every direction.

“So they did make some preparations…”

As Pung Yang stared impassively at the battlefield, one of the mounted bandits came back with parts of his body blackened like charcoal.

“What happened?”

“L-Leader. The casualties are too high!”

The moment he reached Pung Yang, the mounted bandit threw himself flat on the ground and continued in a breathless voice.

“From the first assault until now, at least a hundred men must have died. More importantly, after that fire attack, our brothers’ morale is…”

“The gate?”

“Pardon?”

“What happened to the gate?”

“We broke through, but the Tiger of Mount Heng, Cheol Mubaek, is holding it alone…”

“Alone?”

“Yes. His martial arts are so formidable that no one dares step forward.”

“Then it’s settled.”

At the same time, Pung Yang held out his hand.

The mounted bandit instinctively reached to take it, only for his body to list and collapse.

A dagger was buried deep between his brows.

“How many troops do we have left?”

This sort of scene was familiar to the subordinate who served as Pung Yang’s right hand. After glancing at the corpse, he answered.

“By a rough count, somewhere between a little over a hundred and fifty and just under two hundred. It’s true that our losses are greater.”

“Then imagine theirs. The men on those walls are the Mount Heng Sword Sect’s final bulwark.”

“You mean those few men are all they have left?”

“Yes.”

“I’m not doubting you, Leader, but couldn’t there be another trap like that fire attack?”

“That’s what they’re counting on.”

Pung Yang let out a derisive laugh. He didn’t know whose strategy it had been, but they had played it quite cleverly.

*If I had been less experienced, I would have suspected another trap and pulled our forces back.*

*They’re struggling to buy time. Are they waiting for someone’s support?*

If so, there was even less reason to hesitate.

The few couldn’t stand against the many. Even if the Red Wind Band had suffered considerable losses, wiping out the Mount Heng Sword Sect would be easy.

And besides…

“I’m going myself.”

“You’re going yourself, Leader?”

“Yes. We have to catch the tiger, don’t we?”

Pung Yang burst into a hearty laugh and habitually felt inside his robes.

A hard wooden case rested there.

Inside was something that could bring down a tiger in one go.
```
