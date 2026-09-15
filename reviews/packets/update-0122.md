<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0122.txt",
      "sha256": "40d329c1beb2719a49d10749e826b26880f488f980016463f6b7a5a91a218512",
      "bytes": 13172
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "5d934c19c3be5b9870a1df42d0542463cdd2691fde5f9333e85e7208ed4e18d2",
      "bytes": 2573
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "f888cc050332d115b0d37e8382622c02ef64553dcb56726e08e781df07b25c16",
      "bytes": 19991
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "83c30e1d4069c6c70f96feb85a242673c6356bfc49963206aa1a6e7653bca7a4",
      "bytes": 724
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "9c26a3ab9cf3e2ac86338cd9fbed8a6b415554051cde9b7e395fe7b5ea10c090",
      "bytes": 5130
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "7504618882af5623469f0bc5ca75cc00888e48d1ca80abb474fdd6d05490c83b",
      "bytes": 1389
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "6adc3de42c38b62cfbaddc122b016d37a42c6340ada4ff7fd962308afad03947",
      "bytes": 24338
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "2aacfc6b11052008508758702347c2d90b1afc2c1ffcdec1910f214ef397bbdc",
      "bytes": 1239
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "cf891399c267c864b76e174d5f365db37a4a17b237804b76e80bfaa09f8c68e9",
      "bytes": 1356
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "2086405e5a39ed88a497e4ded9e36f89501c55dc0fcb30ea2da97ea4366d4a7b",
      "bytes": 2314
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "438dac3d68138a3e957e3ecfdd0651b831054dacc84a28769b57dc419e6150fa",
      "bytes": 17642
    }
  ],
  "estimated_tokens": 20314
}
-->

# Durable State Update — Chapter 122

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 122. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 122. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 122,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 122,
    "continuity_sources": [122],
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
    "Pung Yang is dead; Jin Taekyung killed him after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest.",
    "Taekyung fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.",
    "Jin Mukyung survived his fight with Pung Yang and is recovering.",
    "Cheol Mubaek and the other wounded Mount Heng martial artists are recovering after receiving treatment.",
    "Lee Seowol remains the Sect Leader of the Mount Heng Sword Sect and vows to preserve the sect for those who died defending it.",
    "The Lower District Sect sent a relief force with physicians, cooks, and laborers after the battle.",
    "Wolhwa's real name is Eun Sowol, and she is the Lower District Sect's Shanxi Branch Leader.",
    "Lee Seowol accepted Jin Wikyung's invitation to the Jin Family of Taiyuan's New Year gathering.",
    "Lee Seowol offered the Mount Heng Sword Sect's territorial rights to the Jin Family of Taiyuan as an apology.",
    "Lee Seowol proposed marriage to Jin Taekyung in exchange for three Peak martial arts.",
    "Lee Seowol is seventeen years old."
  ],
  "continuity_sources": [
    121
  ],
  "open_questions": [
    "Will Jin Taekyung accept Lee Seowol's marriage proposal?",
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What is the origin and full long-term effect of the Temporary Strength Pill?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?"
  ],
  "safe_through": 121,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 호신강기 as Body-Protecting Qi.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 뛰어난 금창약 as Superior Wound Medicine and 십년하수오 as Ten-Year He Shouwu.",
    "Render 완전 회복 as Full Recovery.",
    "Render 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor and 절정 무공 as Peak martial arts."
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
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |

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
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 검법     | **sword technique**                              |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 마적     | **mounted bandits**                              |                                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 문주     | **Sect Leader**                              |
| 지부장    | **Branch Leader**                            |
| 사부     | **Master**                                   |
| 큰형     | **eldest brother**                           |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 일격     | **One Strike**                         |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 공자      | **Young Master**                                                |
| 대사      | **Master** for a senior Buddhist monk                           |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 121
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 121
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 121
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 121
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, who has now proposed marriage to him in exchange for three Peak martial arts

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 121
- **Aliases:** None
- **Role:** Seventeen-year-old current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady; survived Pung Yang's attack with twenty-four other identified survivors; regards the Mount Heng Sword Sect as effectively destroyed but vows to preserve it for those who died defending it; offered the sect's territorial rights to the Jin Family of Taiyuan and proposed marriage to Jin Taekyung in exchange for three Peak martial arts
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge; has proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 121
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 121
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃122화



정보를 전달함에 있어 중요한 것은 두 가지다. 신속과 정확.

그것을 위해 정보를 취급하는 문파인 하오문은 지부마다 촘촘한 정보망을 구성해 두었다.

월화는 그중 산서성에 설치된 삼십여 개 지부에 동원령을 내릴 수 있는 권한을 지니고 있었다.

“일은? 마무리했어?”

그녀의 물음에 멀끔한 인상의 중년인, 하오문 정양지부장이 대답했다.

“시신은 모두 분리해서 옮겨 두었습니다. 항산검문 측 생존자는 더 없었고, 마적 중에 숨이 붙어 있는 놈들이 있더군요.”

“얼마나?”

“정확히 마흔일곱입니다.”

“많이도 살았네. 그중에 몇이나 살릴 수 있어?”

“지금 보유한 약재로는 서른 정도가 한계입니다.”

“모두 다 살릴 필요는 없겠지.”

월화의 한마디에 정양 지부장이 고개를 숙였다.

“조치하겠습니다.”

그것으로 살아남은 마적들의 운명이 결정되었다.

중상을 입었다면 산더미처럼 쌓인 동료들의 곁으로 돌아갈 것이고, 경상을 입었다면 생명을 조금 더 연장시킬 수 있을 것이다.

물론 치료가 끝나는 즉시 광산이나 투기장의 노예로 팔려 가겠지만.

“다음. 혼주지부장?”

“저희 쪽도 문제없습니다.”

혼주지부장은 얼굴에 검상이 가득한 거한이었다. 그는 철사처럼 빳빳한 턱수염을 긁적이며 말을 이었다.

“사실 나설 필요도 없더구먼요. 풍양이 죽고 적풍단이 아작 났다는 걸 알았는지 근처에 얼씬도 안 합디다.”

“당장은 그걸로 충분해. 발 빠르고 입 가벼운 애들로 골라서 소문 퍼트려. 그럼 알아서 내뺄 거야.”

풍양과 그 수하들을 해치웠다지만 아직 인근에는 상당한 숫자의 마적들이 이리처럼 주변을 어슬렁거리고 있었다.

항산검문이라는 손쉬운 먹잇감에 이빨을 박기 위해 호시탐탐 때를 노리는 것이다.

“산서잠룡과 진천검이 풍양을 일격에 때려죽였다. 뭐 이 정도면 놈들도 혼비백산하겠군요.”

“사실과는 좀 다르긴 한데…… 적당히 양념 쳐. 남의 집 싸움에 우리가 피 흘릴 수는 없잖아?”

소문의 진위는 중요하지 않다. 태원진가의 두 형제가 풍양과 적풍단으로부터 항산검문을 구했다는 것만 알려지면 된다.

“어차피 며칠 안에 태원진가가 움직일 거야. 아주 멍청한 놈들이 아니고서야 살고 싶으면 고원으로 돌아가겠지.”

항산검문의 뒤에 태원진가라는 대호(大虎)가 버티고 있다는 사실이야 곧 널리 퍼질 것이다. 산군의 포효 한 번이면 알아서 나가떨어질 놈들 아닌가.

“길어도 닷새야. 그때까지 고생 좀 하자고.”

두 지부장이 고개를 끄덕였다.

“고생이랄 게 있습니까. 총지부장님 명령인데 당연히 따라야죠.”

“전 좋습니다. 옆에 고원이 붙어 있어서 그런가, 탁 트여서 말 달리는 재미도 있고.”

“그럼 다행이고.”

월화가 피식 웃으며 곰방대를 빨아들였다.

“저어, 그런데 말입니다.”

“응?”

휘하 지부장 중 가장 호전적이고 무공 광으로 평가받는 혼주지부장이 눈을 반짝였다.

“여기 부상자들한테 듣기로는 풍양 그놈이 단신으로 항산호와 진천검을 쓰러트렸다던데. 사실입니까?”

“맞아. 나도 직접 보지는 못했지만.”

“허어, 대단하네요.”

“대단하지. 단기간에 그렇게 빨리 강해졌다는 점에서 구린내가 진동하지만.”

절정의 경지는 깨달음의 영역이다. 그때부터는 신체의 단련을 넘어 무리(武理)를 꿰뚫어야 보다 더 높은 경지로 나아갈 수 있는 것이다.

그러나 불과 얼마 전 항산호 철무백을 상대로 패퇴했던 풍양이다. 제아무리 깨달음이 받쳐 준다 해도 짧은 시일 안에 너무 강해졌다.

아직 잠력단의 존재를 모르는 월화는 그 부분을 짚었다.

“뭔가 수를 쓴 게 분명한데…… 자세히 한번 알아봐야겠어.”

눈치 빠른 정양지부장은 묵례를 취했고, 혼주지부장은 뒤통수를 벅벅 긁었다.

“물론 풍양, 그 마적 놈도 대단하지만 제가 말씀드린 건 다른 사람입니다.”

“누구? 아.”

“산서잠룡. 대단하지 않습니까? 본 문에서 파악한 바에 의하면 그의 무공은 아직 일류에 불과한데…… 매번 예상을 벗어나는군요.”

정보는 객관적 사실이 밑바탕 되어야 한다. 하오문도인 그들은 냉정하게 제삼자 입장에서 정보의 쓰임새를 판단하고, 사람과 상황에 적용시킨다.

그런 의미에서 진태경은 골칫덩이였다. 그에 관한 예상은 늘 빗나갔으니까.

“그런데 참 신기한 게, 점점 기대가 된다는 거죠.”

“기대?”

“다음에는 어떤 식으로 우리의 예상을 벗어날까. 뭐 그런 기대 말입니다.”

히죽거리던 혼주지부장은 월화의 냉담한 표정에 웃음을 멈췄다.

“죄송합니다. 제가 입방정을…….”

“잘 아네. 나가서 일 봐.”

두 지부장을 쫓아낸 월화는 다시 곰방대를 물었다.

달싹이는 입술에서 연기와 함께 아주 작은 목소리가 흘러나왔다.

“진태경이라, 진태경.”

문득, 언젠가 사부(師傅)와 나눴던 대화가 생각난다.



‘그런 자들이 있다. 늘 예측을 벗어나는 자, 정보로 판단할 수 없는 자들이.’

‘그럼 어떻게 하죠?’

‘판단하지 말고 그저 지켜보아라. 네가 직접 그에 대한 확신을 내릴 수 있을 때까지.’

‘그렇게까지 했는데도 확신을 내리지 못한다면요?’

‘예측불허. 그런 자가 있다면 언젠가 천하를 움직일 만한 재목이 아니겠느냐?’



‘천하를 움직일 재목…….’

월화는 곰방대의 재를 털고 전각을 빠져나왔다.

어둠이 짙게 내리깔린 밤, 타오르는 횃불을 이정표 삼아 걷던 그녀가 발걸음을 멈춘 곳은 진태경이 머무르는 전각 앞이었다.

“거기서 뭐 해요?”

전각 앞에 처량하게 쭈그려 앉아 있던 혁무진이 월화를 보고 반색했다.

“앗, 오셨습니까?”

“대충 일이 마무리되어 가는 중이라 잠깐 들렀어요. 안에 진 공자 있죠?”

사실 물어볼 필요도 없는 일이었다. 밖으로 환한 불빛이 새어 나오고 있었으니까.

하지만 혁무진은 어두운 얼굴로 고개를 저었다.

“안에 없어요?”

“아뇨, 계시긴 한데. 그…….”

한숨을 푹 내쉰 혁무진이 말을 이었다.

“상태가 별로 좋지 않으셔서요. 아까부터 뜻 모를 소리만 중얼거리고 계세요. 보면 소름이 돋는다니까요.”

“뜻 모를 소리요?”

“네. 혹시 급식이 무슨 뜻인지 아십니까?”

“급식이요?”

월화는 고개를 갸웃했다. 적지 않은 책을 읽었지만 처음 들어 보는 말이다.

“글쎄요. 처음 들어 보는 것 같은데.”

“그렇죠? 전 또 제가 무식한 놈이라 모르는 건가 싶었는데.”

“그래서요?”

“저희 조장님 성격 아시잖아요. 하도 급식, 급식 하시기에 무슨 뜻이냐고 여쭤봤다가 쫓겨났죠.”

처량한 얼굴로 이마를 슬슬 문지르는 걸 보니 곱게 쫓아내진 않은 모양이다.

‘무슨 일이지?’

궁금증을 참지 못한 월화가 문을 두드리려던 그때였다.

문틈 사이로 새어 나오는 누군가의 음산한 목소리.

“급식, 고딩, 철컹, 철컹…….”

순간 소름이 쭉 돋은 월화는 자신도 모르게 뒷걸음질 쳤다.

“바, 방금 들었어요?”

“아까부터 저 상태라니까요.”

그 와중에도 들려오는 의미 불명의 중얼거림에 그녀가 주춤주춤 물러났다.

“다, 다음에 올게요.”

다시 한번 깨달았다.

진태경이라는 인간은 여전히 예측불허라는 사실을.



* * *



이틀이라는 시간이 쏜살같이 흘렀다. 이소월은 그날 밤 이후 다시 찾아오지 않았고, 나도 굳이 전각을 나서지 않았다.

새로 얻은 열양지기를 다루는 데에 대부분의 시간을 보내는 와중에도 불쑥불쑥 그녀가 남긴 마지막 말이 생각났다.



‘혼인은 인륜지대사(人倫之大事)이니 천천히 생각해 보세요.’



당시에는 너무 당황해서 입만 벙긋거렸다. 여자에게 먼저 프러포즈를, 그것도 나보다 한참 어려 보이는 여자애한테 받을 줄이야.

비록 거래라는 단어를 쓸 정도로 삭막한 정략혼 제의였지만 프러포즈는 프러포즈다.

하지만 더 큰 충격이 남아 있었다.

‘열일곱 살이라니. 이거 실화냐.’

고등학교 1학년이면 한창 급식 먹을 나이다.

늦둥이 동생인 하연이보다 두 살이나 어리고, 나와는 무려 열 살 차이인 것이다.

‘역시 무림…….’

중학교 때 결혼하고 고등학생 때 부모 되어도 이상하지 않은 세상이다. 오히려 이 나이 먹도록 결혼 안 한 태원진가 삼 형제가 별종으로 보일 정도다.

아니, 잠깐만.

“뭘 그렇게 보냐?”

내 시선을 눈치챈 진무경이 퉁명스럽게 물었다. 풍양으로부터 상당한 부상을 입었던 그는 이제 스스로 거동이 가능할 정도로 회복되어 있었다.

‘그러고 보니…….’

진무경의 혼인 여부에 대해서는 한 번도 들어 본 적이 없다.

나는 설마 하는 마음에 입을 열었다.

“혹시나 해서 물어보는 건데.”

“뭐.”

“혼인했어?”

푸웁!

내 얼굴에 찻물을 뱉은 진무경이 황급히 외쳤다.

“무, 무슨 헛소리를!”

“아니면 말지. 왜 이렇게 당황해?”

뜻밖의 세수를 당한 나는 소매로 얼굴을 닦으며 질문을 이어 갔다.

“왜 안 했는데?”

잠깐 당황하는가 싶던 진무경이 순순히 대답했다.

“무공 익히기에도 바쁘다. 내게 여인은 사치야.”

“그렇게 말하니까 되게 검소하게 느껴지네.”

“네놈 같은 음탕한 한량과 동급으로 보지 마라. 그건 나에 대한 모욕이야.”

“…….”

음탕하긴 시벌, 27년 동안 모태 솔로로 살았던 나다.

연애를 사치라고 한다면 나는 자린고비 그 자체다. 약간 다른 점이 있다면 자린고비는 굴비를 쳐다보며 밥을 먹었지만 내게는 USB가 있었다는 것 정도지.

“뭐지, 그 표정은? 굉장히 슬퍼 보이는데.”

“지나간 삶에 대한 후회랄까.”

“드디어 사람이 되어 가는군.”

지나간 삶에 대한 해석이 다른 것 같은데…… 그래, 너 좋을 대로 해석해라.

“그런데 갑자기 혼인에 관해서는 왜 물어본 것이냐? 너도 뻔히 아는 사실을.”

“아, 항산검문주가 나랑 혼인하자고 그래서.”

“푸웁!”

“……후, 작작 뱉어라.”

두 번째 찻물을 닦아 내는 사이 평정심을 되찾은 진무경이 입을 열었다.

“항산검문주가?”

“어. 이틀 전에 그러더라고.”

“도대체 왜 너 같은 놈과…… 아, 당연히 정략혼이겠군.”

“…….”

거, 틀린 말은 아닌데 상당히 기분 나쁘네. 이제 나 정도면 무림에서나 현실에서나 일등 신랑감 아닌가?

“그래서, 할 생각이냐?”

“당연히 아니지. 한참 어린 애랑 어떻게 혼인을 해.”

“고작 약관인 놈이 못 하는 말이 없구나.”

몸은 스물이지만 정신은 스물일곱이다, 이놈아.

그리고 이소월의 제의에 대한 내 대답은 이미 정해진 지 오래였다.

사랑하는 사람이 있는데 두 집 살림을 차릴 순 없는 법. 지금 내게는 오직 한 사람뿐이다.

‘송이 씨는 지금 뭘 하고 있을까.’

상상만 해도 행복하다. 흐뭇하게 웃으며 찻잔을 기울이는 나를 진무경이 해괴한 표정으로 바라봤다.

“역겨운 표정이군.”

“아무튼, 여러 가지 이유로 혼인은 거절.”

“잘 생각했다. 적어도 정략혼이라면 우리가 얻는 것이 있어야 하는 법인데, 마음도 없는 상대와 혼인하면서 아무것도 얻지 못한다면 정략혼을 할 이유가 없지.”

무공밖에 모르는 바보인 줄 알았는데, 가끔 보면 제법 날카로운 현실주의자가 된다.

“그리고 무슨 제의를 하더라도 큰형님이 있는 한 어림없다. 널 정략혼으로 엮으실 분은 아니니까.”

“저쪽에서도 꽤 큰 제의를 하긴 했어.”

“흠. 뭘 주겠다더냐?”

진무경이 심드렁한 얼굴로 찻잔을 기울였다.

“혈랑검법, 혈랑보법. 그리고 수라멸권.”

푸웁!

“……아, 시바.”

이번에는 닦을 시간도 없다. 진무경이 내 멱살을 잡고 탈탈 털었다.

“당장 혼인해!”
```

## Final English reading copy

```markdown
# Chapter 122

There were two things that mattered when conveying information: speed and accuracy.

To that end, the Lower District Sect, a sect that dealt in information, had built an extensive information network at every branch.

Wolhwa had the authority to issue mobilization orders to the more than thirty branches established throughout Shanxi Province.

“How’s it going? Are you finished?”

A clean-cut middle-aged man answered her question. He was the Jeongyang Branch Leader of the Lower District Sect.

“We separated and moved all the corpses. There were no more survivors from the Mount Heng Sword Sect, but some of the mounted bandits were still breathing.”

“How many?”

“Exactly forty-seven.”

“That’s quite a lot who survived. How many of them can we save?”

“With the medicine we currently have, thirty at most.”

“We don’t need to save every last one.”

At Wolhwa’s words, the Jeongyang Branch Leader lowered his head.

“I’ll take care of it.”

That decided the surviving mounted bandits’ fates.

Those with serious injuries would rejoin the mountain-high pile of their comrades, while those with minor injuries might live a little longer.

Of course, the moment their treatment was finished, they would be sold as slaves to the mines or fighting pits.

“Next. Honju Branch Leader?”

“No problems on our end, either.”

The Honju Branch Leader was a hulking man whose face was covered in sword scars. He scratched at his stiff, wirelike beard and continued.

“Truth is, we didn’t even need to step in. They must’ve heard Pung Yang was dead and the Red Wind Band had been wrecked, because they didn’t come anywhere near the area.”

“For now, that’s enough. Pick the swiftest and most loose-lipped people you have and spread the rumor. They’ll run away on their own.”

Although Pung Yang and his subordinates had been dealt with, a considerable number of mounted bandits were still prowling around the area like wolves.

They were waiting for an opportunity to sink their teeth into the easy prey that was the Mount Heng Sword Sect.

“The Sleeping Dragon of Shanxi and the Heaven Shaking Sword beat Pung Yang to death with a single blow. If the others hear that, they’ll be scared out of their minds.”

“It’s not exactly true, but… Add enough seasoning. We can’t bleed for someone else’s fight, can we?”

The truth of the rumor was unimportant. All that mattered was that people learned the two brothers of the Jin Family of Taiyuan had rescued the Mount Heng Sword Sect from Pung Yang and the Red Wind Band.

“Besides, the Jin Family of Taiyuan will make a move within a few days. Unless they’re complete idiots, they’ll return to the plateau if they want to live.”

The fact that the great tiger known as the Jin Family of Taiyuan stood behind the Mount Heng Sword Sect would soon spread far and wide. Wouldn’t one roar from the mountain king be enough to send those bandits running?

“Five days at most. Let’s put in some effort until then.”

The two Branch Leaders nodded.

“What effort? It’s the Chief Branch Leader’s order. Of course we have to follow it.”

“I like it. Maybe it’s because the plateau is right next door, but there’s something fun about riding across all this open land.”

“Then that’s a relief.”

Wolhwa gave a short laugh and drew on her long-stemmed tobacco pipe.

“Um, by the way…”

“Yes?”

The Honju Branch Leader, considered the most aggressive and martial-arts-obsessed of her subordinates, had a bright gleam in his eyes.

“I heard from the wounded that bastard Pung Yang took down the Tiger of Mount Heng and the Heaven Shaking Sword all by himself. Is that true?”

“It is. Though I didn’t see it myself.”

“Wow. That’s impressive.”

“It is impressive. The fact that he grew so strong so quickly reeks of something fishy, though.”

The Peak realm was a domain of enlightenment. From that point onward, a martial artist had to see through the principles of martial arts rather than merely train the body in order to advance to a higher realm.

But Pung Yang had been defeated by Cheol Mubaek, the Tiger of Mount Heng, only a short while ago. No matter how much enlightenment supported him, he had become far too strong in far too little time.

Wolhwa, who still knew nothing of the Temporary Strength Pill, focused on that point.

“He definitely used some kind of trick… I’ll have to look into it more closely.”

The quick-witted Jeongyang Branch Leader offered a silent bow, while the Honju Branch Leader vigorously scratched the back of his head.

“Of course, Pung Yang, that mounted-bandit bastard, is impressive too. But I was talking about someone else.”

“Who? Ah.”

“The Sleeping Dragon of Shanxi. Isn’t he incredible? According to what our sect has determined, his martial arts are still only First Rate, but he keeps defying our expectations.”

Information had to be based on objective facts. As members of the Lower District Sect, they coolly judged how information could be used from a third-party perspective, then applied it to people and situations.

In that regard, Jin Taekyung was a headache. Every prediction concerning him had been wrong.

“But the strange thing is, I’m starting to look forward to it more and more.”

“Look forward to what?”

“Wondering how he’ll defy our expectations next time. That kind of anticipation.”

The Honju Branch Leader had been grinning broadly, but he stopped smiling when he saw Wolhwa’s impassive expression.

“I’m sorry. I was running my mouth.”

“At least you know it. Go outside and handle your work.”

After driving the two Branch Leaders out, Wolhwa put her pipe back between her lips.

A tiny voice slipped from her barely moving lips along with the smoke.

“Jin Taekyung. Jin Taekyung.”

She suddenly remembered a conversation she had once shared with her Master.



*There are people like that. People who always defy prediction, people who cannot be judged through information.*

*Then what should I do?*

*Don’t judge them. Just watch them until you can reach your own conclusion about them.*

*What if I still can’t reach a conclusion after going that far?*

*Unpredictable. If there is such a person, wouldn’t they be the sort of talent capable of moving the world someday?*



*A talent capable of moving the world…*

Wolhwa tapped the ash from her pipe and left the pavilion.

Night had fallen thick and dark. Guided by blazing torches that served as landmarks, she walked until she stopped in front of the pavilion where Jin Taekyung was staying.

“What are you doing out here?”

Hyuk Mujin, who had been sitting miserably in a crouch before the pavilion, brightened when he saw Wolhwa.

“Oh, you’re here?”

“I’ve mostly finished dealing with things, so I stopped by for a moment. Young Master Jin is inside, right?”

In truth, there was no need to ask. Bright light was spilling out through the pavilion.

But Hyuk Mujin shook his head with a grim expression.

“He isn’t inside?”

“No, he is. It’s just that…”

Hyuk Mujin let out a deep sigh before continuing.

“His condition isn’t very good. He’s been muttering things that make no sense for a while now. I get goose bumps just looking at him.”

“Things that make no sense?”

“Yes. Do you happen to know what ‘school lunch’ means?”[^1]

“School lunch?”

Wolhwa tilted her head. She had read a considerable number of books, but it was the first time she had ever heard the word used that way.

“I don’t think so. It sounds unfamiliar.”

“Right? I wondered if I was just too ignorant to know.”

“And then?”

“You know what our Squad Leader is like. He kept saying ‘school lunch, school lunch,’ so I asked him what it meant. Then I got kicked out.”

Judging by the way Hyuk Mujin miserably rubbed his forehead, it seemed he had not been politely shown the door.

*What happened?*

Wolhwa was just about to knock when an eerie voice seeped through the gap in the door.

“School lunch, high schooler, clank, clank…”

A chill ran over Wolhwa, and she took a step backward without realizing it.

“D-Did you hear that?”

“He’s been like that for a while.”

Even as the incomprehensible muttering continued, she slowly backed away.

“I-I’ll come another time.”

She realized it once again.

The man named Jin Taekyung was still utterly unpredictable.



* * *



Two days flew by in the blink of an eye. Lee Seowol did not come back after that night, and I didn’t bother leaving the pavilion, either.

Even while spending most of my time learning to control the newly acquired Scorching Yang Qi, her final words kept coming back to me.



*Marriage is one of life’s great human obligations, so take your time thinking it over.*



I had been so flustered at the time that I could only open and close my mouth.

Who would have thought I’d receive a proposal from a woman first—and from a girl who looked so much younger than me, at that?

Although it was a cold political marriage proposal—cold enough that calling it a transaction wasn’t an exaggeration—it was still a proposal.

But there was an even greater shock waiting for me.

*Seventeen years old? Is this for real?*

A first-year high school student was right in the prime school-lunch-eating years.

She was two years younger than my late-born little sister, Hayeon, and a full ten years younger than me.

*That’s the Murim for you…*

Getting married in middle school and becoming a parent in high school wouldn’t even be strange in this world. In fact, the three brothers of the Jin Family of Taiyuan looked like the oddballs for remaining unmarried at our age.

No, wait a second.

“What are you staring at?”

Jin Mukyung noticed my gaze and asked irritably. He had suffered considerable injuries at Pung Yang’s hands, but he had now recovered enough to move around on his own.

*Come to think of it…*

I had never heard whether Jin Mukyung was married.

I opened my mouth, half expecting the worst.

“Just asking in case.”

“What?”

“Are you married?”

Pffft!

Jin Mukyung spat tea into my face and hurriedly shouted.

“What kind of nonsense are you talking about?”

“If you’re not, then you’re not. Why are you so flustered?”

After receiving that unexpected facial wash, I wiped my face with my sleeve and continued asking questions.

“Why aren’t you?”

Jin Mukyung looked flustered for a moment, then answered readily.

“I’m too busy training in martial arts. Women are a luxury to me.”

“You make it sound downright frugal.”

“Don’t lump me in with a lecherous idler like you. That’s an insult to me.”

“…”

Lecherous, my ass. I had spent twenty-seven years as a lifelong single.

If dating was a luxury, then I was the very definition of a miser. The only slight difference was that while Jaringobi ate rice while staring at a strip of dried fish, I had a USB drive.[^2]

“What’s with that expression? You look incredibly sad.”

“Maybe it’s regret over the life I’ve lived.”

“At last, you’re becoming a human being.”

He seemed to have a different interpretation of my past life, but fine. He could interpret it however he wanted.

“But why did you suddenly ask about marriage? It’s something you already know perfectly well.”

“Oh, because the Sect Leader of the Mount Heng Sword Sect asked me to marry her.”

Pffft!

“…For fuck’s sake. Stop spitting.”

While I wiped away the second mouthful of tea, Jin Mukyung regained his composure and spoke.

“The Sect Leader of the Mount Heng Sword Sect?”

“Yeah. She said it two days ago.”

“Why on earth would she marry someone like you… Ah, of course. It must be a political marriage.”

“…”

He wasn’t wrong, but it was still pretty damn irritating. At this point, wasn’t I prime husband material both in the Murim and in the real world?

“So, are you thinking of doing it?”

“Of course not. How could I marry a girl so much younger than me?”

“You’re barely twenty, and you say things like that.”

*My body is twenty, but my mind is twenty-seven, you bastard.*

Besides, I had decided on my answer to Lee Seowol’s proposal a long time ago.

You can’t set up two households when there’s someone you love. There was only one person in my heart right now.

*What could Song-i be doing right now?*

Just imagining it made me happy. I tilted my teacup with a blissful smile, and Jin Mukyung stared at me with a bizarre expression.

“What a disgusting look.”

“Anyway, I’m turning down the marriage for various reasons.”

“You made the right decision. At the very least, a political marriage has to offer us something in return. If you marry someone you have no feelings for and gain nothing from it, there’s no reason to enter into a political marriage.”

I had thought he was a fool who knew nothing but martial arts, but every now and then, he turned into a surprisingly sharp realist.

“And no matter what she offers, it’s out of the question as long as our eldest brother is around. He isn’t the sort of person who’d arrange a political marriage for you.”

“They did make a pretty substantial offer, though.”

“Hm. What did she say they would give you?”

Jin Mukyung tilted his teacup with an uninterested expression.

“The Blood Wolf Sword Technique, the Blood Wolf Footwork, and the Shura Annihilating Fist.”

Pffft!

“…Ah, fuck.”

This time, I didn’t even have time to wipe it away. Jin Mukyung grabbed me by the collar and shook me hard.

“Marry her right now!”

[^1]: “School lunch” is Korean slang for a school-age kid, while “clank, clank” evokes handcuffs or prison bars—the joke is that sexual interest in a high schooler could land someone in jail.
[^2]: Jaringobi is a traditional Korean image of a miser who stares at dried fish while eating rice rather than eat the fish.
```
