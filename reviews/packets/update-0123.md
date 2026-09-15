<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0123.txt",
      "sha256": "6c667583e4287e753715790c72f99e27ce94c4cf0b13ddd8092c27c97fd2cca2",
      "bytes": 13370
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f208918ae64edc94cfadb1934057dcea30e061cf679e35492074e554097c2cbf",
      "bytes": 3205
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "af9e46d0a4db6184b6c674d5389435ce2e4b9608a3c043ee90ef7f107c1cc8db",
      "bytes": 20466
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "f172a709d14f6c84fe59a2fe41a345e4bd4333edc13ac7aaa9ff3e7cd1575bde",
      "bytes": 724
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "df77627aa84b7789965bdfe8129de97e6b2e6edcea430dc8804a86ffcbb25f5e",
      "bytes": 1421
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "0c7ec127db8ac0f75cf73abc11796e0a2c2d5c4efdd2199e2504391c0504e936",
      "bytes": 2804
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "aa0523b23326976a2a5c4f45f6879a4d57503840d095f6cdd7fe81bd982e4530",
      "bytes": 3231
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "80c0b7db45c7022fa12596378c7f2a5daa6c3804f97dd284742f7b6f77cd739f",
      "bytes": 1239
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "2fdafe46268503dec3ea1d92aecfed5d8a449c13d88d8388d91e4b300b54edf3",
      "bytes": 1356
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5dea745a2e714cf866b8b5b8934df5a17d2129e099c7ff3164432303d44df785",
      "bytes": 17837
    }
  ],
  "estimated_tokens": 19924
}
-->

# Durable State Update — Chapter 123

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 123. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 123. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 123,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 123,
    "continuity_sources": [123],
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
    "Jin Mukyung survived his fight with Pung Yang and has recovered enough to move independently.",
    "Cheol Mubaek and the other wounded Mount Heng martial artists are recovering after receiving treatment.",
    "Lee Seowol remains the Sect Leader of the Mount Heng Sword Sect and vows to preserve the sect for those who died defending it.",
    "The Lower District Sect sent a relief force with physicians, cooks, and laborers after the battle.",
    "Wolhwa's real name is Eun Sowol, and she is the Lower District Sect's Shanxi Branch Leader with authority over more than thirty Shanxi branches.",
    "Lee Seowol accepted Jin Wikyung's invitation to the Jin Family of Taiyuan's New Year gathering.",
    "Lee Seowol offered the Mount Heng Sword Sect's territorial rights to the Jin Family of Taiyuan as an apology.",
    "Lee Seowol proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist.",
    "Lee Seowol is seventeen years old.",
    "Jin Taekyung has decided to reject Lee Seowol's political marriage proposal because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty with its available medicine.",
    "The Lower District Sect is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued the Mount Heng Sword Sect."
  ],
  "continuity_sources": [
    122
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What is the origin and full long-term effect of the Temporary Strength Pill?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?"
  ],
  "safe_through": 122,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 호신강기 as Body-Protecting Qi.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 뛰어난 금창약 as Superior Wound Medicine and 십년하수오 as Ten-Year He Shouwu.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor and 절정 무공 as Peak martial arts.",
    "Render 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, clank, 산서성 as Shanxi Province, and 총지부장 as Chief Branch Leader."
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
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |

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
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |

## Exact glossary matches

| 진무경    | **Jin Mukyung**    |
| 이천백    | **Lee Cheonbaek**  |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 천무학관   | **Heaven's Gate Temple**         |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 검법     | **sword technique**                              |                                                       |
| 권법     | **fist technique**                               |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 제자     | **Disciple**                                 |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 상태               | **Status**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 122
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 122
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; now able to move independently
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 121
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 121
- **Aliases:** Blood Wolf Sword
- **Role:** Former Sect Leader of the Mount Heng Sword Sect, killed during the Red Wind Band’s assault; father of Lee Seogeun and Lee Seowol
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Deceased father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; former leader of the Mount Heng Sword Sect; longtime close friend and peer of Cheol Mubaek

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 122
- **Aliases:** None
- **Role:** Seventeen-year-old current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady; survived Pung Yang's attack with twenty-four other identified survivors; regards the Mount Heng Sword Sect as effectively destroyed but vows to preserve it for those who died defending it; offered the sect's territorial rights to the Jin Family of Taiyuan and proposed marriage to Jin Taekyung in exchange for three Peak martial arts
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge; has proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 122
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

## Korean source

```text
＃123화



전신에 붕대를 감은 채 누워 있는 중년인.

뭐가 마음에 안 드는지 미간은 잔뜩 찌푸려져 있고, 몸은 한시도 쉬지 않고 꿈지럭거린다.

“끄응.”

앓는 소리를 흘리자 곧장 면박이 날아왔다.

“너무 움직이지 마세요.”

“그게 아니라…….”

“철 숙부, 의원이 했던 말 못 들으셨어요?”

또 시작이군. 항산호 철무백은 천장만 멀거니 바라봤다. 그러자 이소월이 두툼한 솜이불을 그의 가슴까지 덮어 주며 말을 이었다.

“하루라도 빨리 나으셔야죠. 좀이 쑤시는 건 알겠지만 누워 계세요. 잠이라도 더 주무시고.”

“이미 충분히 잤다.”

“고작 한 시진밖에 안 주무셨잖아요.”

“고작이라니. 한 시진이면 충분하지.”

“그러시다가 몸만 더 상해요.”

“삼십 년을 넘게 그리 살았어. 끄떡없다.”

“지금까지는 이렇게 크게 다치신 적이 없었으니까 그렇죠.”

“……끙.”

이소월의 일침에 철무백은 입을 다물었다.

그녀의 말이 맞다. 수라멸권을 익힌 이래 지금처럼 큰 부상을 입은 적은 없었다. 부러진 사지와 심각한 내상. 의원의 말에 의하면 최소 넉 달은 요양해야 할 중상이라고 했다.

“네 아비와 만났을 때도 이 정도는 아니었는데.”

철무백의 푸념에 이소월이 반응했다.

“아버지요?”

“그래, 천백이 그 친구 말이다.”

“두 분 사이에 무슨 일이 있으셨는데요?”

“이야기한 적 없었더냐?”

“그냥 두 분의 마음이 맞아서 친구가 됐다고 알고 있었어요.”

“그랬지. 하지만 처음에는 목숨을 걸고 싸웠단다.”

“싸워요?”

철무백이 빙긋 웃었다.

“무인 두 사람이 만나서 뭘 했겠느냐? 둘 다 젊은 시절이라 호승심도 강했으니 불 보듯 뻔하지.”

철무백은 창밖을 바라봤다. 삼십여 년 전, 저 높이 솟은 산등성이 어딘가에서 두 사람은 처음으로 만났고, 싸웠다.

“날 찾기 위해 석 달 동안 산맥을 이 잡듯 뒤졌다고 했다. 거지 같은 몰골이었지만 기세가 범상치 않았지.”

고수는 고수를 알아보는 법이다. 아무도 찾지 않는 심산유곡에 틀어박혀 홀로 무공을 익힌 철무백과 수많은 전투를 통해 자신만의 무공을 완성한 이천백.

두 절정 고수의 첫 만남이었다.

“나보고 수하가 되라고 하더구나. 산맥 아래에 문파를 세울 테니 함께 초석을 다지자고 했다.”

“아버지답네요. 그래서요?”

“더 무슨 말이 필요했겠느냐? 싸웠지. 그것도 아주 살벌하게.”

이소월이 피식 웃었다.

“그렇군요.”

“어떻게 됐는지 궁금하지 않으냐?”

“들을 필요가 있나요. 철 숙부께서 지금까지 재야에 머물러 계시는 것만 봐도 알 수 있는 사실인데. 서로의 무공에 감복해서 벗이 되었다는 사내들의 낯 뜨거운 얘기 아닌가요?”

“으하하! 맞다! 딱 오백 합 만에 승부가 났…… 윽.”

큰 소리로 웃던 철무백이 갑작스러운 고통에 움찔하자 이소월이 한숨을 내쉬었다.

“저 때문에 상태가 더 안 좋아지시는 것 같은데…… 제가 없는 게 더 낫겠네요.”

“이 녀석. 혼자 늙어 가는 숙부가 가엾지도 않으냐?”

“생각 있으시면 언제든지 말씀하세요. 중매라도 서 드릴 테니.”

“됐다. 다 늙은 마당에 무슨.”

본인 스스로 한 말이지만 입맛이 씁쓸해진다. 철무백은 마음속으로 뇌까렸다.

‘그래, 어느새 이리 늙었구나.’

가족을 잃은 그 날 이후, 정확히 몇 년의 세월이 더 흘렀는지 철무백 자신조차도 알지 못한다.

심후한 내력과 극도로 단련된 신체 덕분에 본래의 나이보다 젊어 보일 뿐, 정신은 오래전부터 늙어 가고 있었다.

‘하나뿐인 벗도 떠나고, 평생 갈고 닦은 무공도 형편없이 꺾였으니, 허허.’

이제야 비로소 인정할 수 있었다. 항산의 호랑이가 이미 늙었다는 사실을. 하지만 철무백에게는 아직 지켜야 할 것이 남아 있다.

“소월아.”

이소월이 따스한 목소리로 대답했다.

“말씀하세요. 숙부.”

“나는 네가 행복해지길 바란다.”

“알아요.”

“아직 늦지 않았다. 사랑하는 사람과 혼인하거라. 태원진가의 도움을 받는다면 산서 땅 어디에서도 안전하고 행복한 가정을 꾸릴 수 있을 것이다.”

“제가 원하는 것은 가정이 아니라 항산검문이에요.”

철무백의 눈빛에 안타까움이 스쳤다. 갓난아이 시절부터 봐 온 이소월이다. 몰락한 문파를 재건하고 부흥시키는 것은 약관도 채 되지 않은 그녀가 감당하기엔 너무 버거운 짐이었다.

“지금의 선택을 후회할 수도 있다.”

“하지만 제가 무슨 선택을 하더라도 숙부님은 절 믿어 주시겠죠.”

“그렇지 않았다면 네게 수라멸권의 비급을 넘기지 않았을 게다.”

이소월이 철무백의 주름진 손을 움켜쥐었다.

그녀 역시 무가의 여식. 눈앞에 있는 이 늙은 무인이 얼마나 큰 결정을 했는지 알고 있었다.

“감사해요, 숙부.”

어느새 촉촉해진 그녀의 목소리에 철무백이 손을 내저었다.

“난 늙었다. 이제 와서 제자를 들이기도 곤란하던 참인데 좋은 기회가 온 게지.”

수라멸권은 일인전승(一人傳承), 비인부전(非人不傳)의 원칙을 따른다. 행동거지가 올곧고 심성이 바른 후인을 찾아 무맥을 이어 가라는 의도다.

그러나 구 대 계승자인 철무백은 그 원칙을 어기고 이소월에게 비급을 넘겼다. 비록 직접 가르침을 받지는 않았지만 사문(師門) 대대로 내려오는 전통을 깨트린 것이다.

그러나 철무백에게도 나름의 생각이 있었다.

‘진천검과 산서잠룡라면 소월이를 지켜 줄 수 있겠지.’

이소월이 정략혼을 마음먹었다면 그 두 사람이 최선이다.

무공에 대한 재능이야 말할 것도 없고, 불의(不義)에 맞서 목숨 걸고 싸울 만한 협기도 지니고 있다.

‘실제 성정은 어떨지 지켜봐야겠지만…….’

잘만 된다면 정략혼의 목적과 일인전승, 비인부전의 전통. 두 가지 모두를 충족시킬 수 있는 길인 것이다.

“그래서 말인데.”

철무백은 은근한 목소리로 말을 이었다.

“둘 중 누구를 택했느냐?”

이소월이 모르는 척 고개를 갸웃했다.

“어머, 뭐가요?”

“시치미 떼지 말고 말해 보아라. 진천검이냐? 아니면 산서잠룡?”

“글쎄요.”

“그놈이 그놈이긴 한데…… 아무래도 진천검이 낫지 않겠느냐?”

“산서잠룡은 마음에 안 드시나 봐요?”

“뭐, 마음에 안 들 것까지야 있겠냐마는…….”

철무백이 눈살을 찌푸렸다. 일 년의 대부분을 산속 깊은 곳에서 머무르는 그조차도 태원진가의 개망나니에 관한 소문은 들어 봤다.

“아무리 개과천선했다 한들 세 살 버릇 여든까지 가는 법이다. 나중에 네 가슴에 대못을 박지 않을까 걱정되는구나.”

“진천검은요?”

철무백의 찌그러졌던 안색이 펴졌다.

“형만 한 아우 없다고 했다. 어제 잠시 이야기를 나눠 봤는데 사람이 참 괜찮더라. 무재가 아주 뛰어나.”

“무공밖에 모르는 사람이라고 들리는데요.”

“떽! 계집질하는 것보다는 훨씬 낫지. 언행부터가 아주 의젓하고 무게감이 있어. 사내란 자고로 그래야지, 암. 그렇고말고.”

흐뭇하게 웃는 철무백이었다.



* * *



반쯤 눈을 뒤집어 깐 진무경이 내 멱살을 잡고 탈탈 털었다.

“당장 혼인해!”

“컥, 컥!”

가뜩이나 코로 찻물이 들어가는 바람에 사레가 들렀는데 쉬지 않고 멱살을 흔들어 대니 정신이 하나도 없다.

“놔, 안 놔?”

“수라멸권! 혈랑검법! 혈랑보법!”

“알았으니까 일단 놔!”

“이 멍청한 놈! 수라멸권이 어떤 무공인 줄 알고!”

“놓고 얘기하자고!”

“일인전승! 비인부전!”

“그만해, 이 미친놈아!”

잠시 후, 간신히 진무경의 손을 떼어 냈을 때는 전각 내부가 폭풍이라도 지나간 것처럼 엉망이 되어 있었다.

“헉, 허억.”

나는 숨을 고르며 주위를 둘러봤다.

탁자는 주저앉았고, 의자는 박살 났으며 산산조각 난 다기(茶器) 파편이 바닥에 굴러다녔다.

그때 차분해진 얼굴로 옷매무새를 가다듬은 진무경이 입을 열었다.

“음, 진정했다.”

“…….”

이거 생각 이상으로 미친놈이었네.

나는 그나마 덜 젖은 소매로 얼굴을 벅벅 문질렀다.

“수라멸권이 무슨 천하제일 무공이야? 왜 그렇게 집착해?”

“천하에서 열 손가락 안에 드는 권법이지. 아니, 이었다.”

“이었다?”

“이백 년 전의 일이니까. 수천, 수만 권의 서적이 있는 천무학관의 서고에도 기록으로만 남아 있는 무공이지. 그런데 항산호 대협이 바로 그 수라멸권의 당대 계승자였다니!”

상상만 해도 설레는지 진무경의 뺨이 붉게 달아오른다.

나는 코에 들어간 찻물을 털어 내며 물었다.

“그래서?”

“뭣이? 그래서라니!”

진무경이 믿을 수 없다는 눈빛으로 나를 바라봤다.

“바로 그 수라멸권이란 말이다! 이미 오래전 무맥이 끊겼다고 알려진 절정 무공!”

“이백 년 전의 천하십대권법이고?”

“바로 그거다!”

“어, 잠깐만 기다려 봐.”

나는 바닥에 굴러다니는 굵직한 나무 막대기를 주워 들었다. 불과 5분 전까지는 탁자 다리라고 불렸던 물건이다.

“이게 뭔지 알아?”

“몽둥이?”

“잘 아네.”

“그게 뭐 어쨌단 말이냐?”

“이게 이천 년 전쯤에는 천하십대병기. 뭐 그런 거 아니었을까?”

내가 하는 말을 못 알아들을 정도로 멍청한 놈이 아니다.

곧 진무경이 눈을 치켜떴다.

“수라멸권을 그따위 것에 비교하다니.”

“그럼 뭐가 다른데?”

“그건…….”

“물론 이런 나무 몽둥이보다는 훨씬 값어치 있는 물건이긴 하지. 하지만 지금도 마찬가지일까?”

과거 인류는 돌로, 몽둥이로 싸웠다. 그러나 청동과 철기가 등장하면서 시대의 흐름에 뒤로 밀려났다.

수라멸권도 크게 다르지 않다.

“물론 지금도 모두가 탐내는 뛰어난 절정 무공이긴 하겠지.”

그걸 몸소 입증한 것이 항산호 철무백이다. 그는 수라멸권으로 산서성에서 이름 높은 절정 고수가 되었다.

“하지만 수라멸권이 지금까지 천하십대권법인 건 아니잖아?”

돌과 몽둥이가 강철로 바뀐 것처럼, 무공도 발전한다.

나야 뭐, 지금 천하십대권법이 뭔지는 모르지만, 진무경의 표정은 내 말이 틀리지 않았음을 증명했다.

“막말로 수라멸권이 그렇게 강한 무공이었으면 풍양에게 질 일도 없었지. 그리고 이게 가장 중요한 건데……”

나는 탁자 다리를 대충 구석에 던지고 쐐기를 박았다.

“난 혼인할 생각 없어.”

“……!”

“당사자가 안 한다는데 뭐 어쩔 거야. 안 그래?”

“그건…… 그렇지.”

진무경이 한숨을 푹푹 내쉬었다. 여기서도 우기면 한 판 붙으려고 했는데, 의외로 순순하게 수긍하는 것 같다.

그래도 수라멸권의 비급이 자꾸 눈앞에 아른거리는지 아련한 눈빛을 하고 있긴 하지만.

‘이 자식도 어지간히 무공 덕후네.’

하긴, 무공을 더 익히고 싶어서 천무학관에 간 녀석이다.

바로 그 천무학관에서도 기록으로만 남아 있는 수백 년 전의 무공을 발견했으니 몸이 달 수밖에.

“후우우…….”

땅이 꺼져라 한숨을 내쉰 진무경이 중얼거렸다.

“아쉽구나, 아쉬워.”

“그렇게까지 아쉬울 것까지야. 인연이 닿으면 다음에 구할 수 있겠지.”

“멍청한 녀석. 절정 무공이 어디 하늘에서 뚝 떨어지는 줄 아느냐?”

“그래? 난 떨어지던데.”

“천하의 무공이 모두 모여 있다는 천무학관에서도 절정 무공들은 철저히 관리…… 뭐라고?”

“난 하늘에서 떨어졌다고.”

나는 품에서 낡은 서책 한 권을 꺼내 들었다. 겉면에 적힌 네 글자는 세월의 풍파로 흐릿했지만, 충분히 읽을 수 있을 만큼 또렷했다.

화염신장(火焰神掌).

호랑이는 죽어서 가죽을 남기고, 조필은 죽어서 초절정 무공을 남겼다.

“화, 화, 화…….”

아마 오늘이 진무경의 일생을 통틀어 가장 놀라운 날일 거다.

눈을 부릅뜨고 나와 비급을 번갈아 보는 녀석에게 씩 웃어 주었다.

“앞으로 형이라고 불러라.”
```

## Final English reading copy

```markdown
# Chapter 123

A middle-aged man lay in bed with bandages wrapped around his entire body.

His brow was deeply furrowed, as if something was bothering him, and his body kept fidgeting without a moment's rest.

“Ugh.”

The moment he let out a groan, a sharp rebuke came flying.

“Please don’t move so much.”

“That’s not it…”

“Uncle Cheol, didn’t you hear what the physician said?”

Here we go again. Cheol Mubaek, the Tiger of Mount Heng, stared blankly at the ceiling. Lee Seowol pulled a thick cotton blanket up to his chest and continued.

“You need to recover as quickly as possible. I know you’re feeling restless, but please stay in bed. At least get some more sleep.”

“I’ve already slept enough.”

“You only slept for two hours.”

“Only? Two hours is plenty.”

“You’ll just make yourself worse.”

“I’ve lived like this for more than thirty years. I’ll be fine.”

“That’s only because you’ve never been this badly injured before.”

“...Urgh.”

Cheol Mubaek fell silent at Seowol’s pointed remark.

She was right. He had never suffered injuries this severe since learning the Shura Annihilating Fist. Broken limbs and serious internal injuries. According to the physician, they were severe enough that he would need at least four months of recuperation.

“I wasn’t this badly hurt even when I met your father.”

Seowol reacted to his complaint.

“My father?”

“Yes. That friend of mine, Cheonbaek.”

“What happened between the two of you?”

“I never told you?”

“I only knew that the two of you became friends because you hit it off.”

“That’s true. But at first, we fought with our lives on the line.”

“You fought?”

Cheol Mubaek smiled faintly.

“What else would two martial artists do when they met? We were both young, and our competitive pride was strong. The answer was obvious.”

Cheol Mubaek looked out the window. More than thirty years ago, somewhere along those towering mountain ridges, the two men had met for the first time—and fought.

“He said he’d searched the mountain range for three months, combing through it inch by inch to find me. He looked like a beggar, but his aura was anything but ordinary.”

Masters recognized masters. Cheol Mubaek had secluded himself in a remote valley that no one visited, training in martial arts alone. Lee Cheonbaek had perfected his own martial arts through countless battles.

It had been the first meeting between two Peak masters.

“He told me to become his subordinate. He said he was going to establish a sect at the foot of the mountains and wanted me to lay its foundation with him.”

“That sounds like Father. So what happened?”

“What else needed to be said? We fought. And we fought viciously.”

Seowol snorted softly.

“I see.”

“Aren’t you curious what happened?”

“Do I need to hear it? I can tell just from the fact that you’ve remained unaffiliated all this time, Uncle Cheol. Isn’t this one of those embarrassing stories men tell about becoming friends after being moved by each other’s martial arts?”

“Ha-ha-ha! That’s right! The fight was decided in exactly five hundred exchanges… ugh.”

Cheol Mubaek had been laughing loudly when a sudden stab of pain made him flinch. Seowol sighed.

“I think I’m making your condition worse by being here… It might be better if I left.”

“Seowol. Don’t you feel sorry for an uncle who’s growing old all alone?”

“If you’re interested, just tell me anytime. I’ll even find someone to set you up with.”

“Forget it. What would I do at my age?”

Although he had said the words himself, they left a bitter taste in his mouth. Cheol Mubaek muttered inwardly.

*Yes. Somehow, I’ve grown this old.*

He did not even know exactly how many years had passed since the day he lost his family.

His deep internal energy and highly trained body made him look younger than his true age, but his mind had been growing old for a long time.

*My one and only friend is gone, and the martial arts I spent my entire life honing have been broken so thoroughly. Heh.*

Only now could he finally admit it. The Tiger of Mount Heng had grown old.

But Cheol Mubaek still had something left to protect.

“Seowol.”

Seowol answered him warmly.

“Yes, Uncle?”

“I want you to be happy.”

“I know.”

“It’s not too late. Marry the person you love. With the Jin Family of Taiyuan’s help, you could build a safe and happy home anywhere in Shanxi.”

“What I want isn’t a family. It’s the Mount Heng Sword Sect.”

A trace of sorrow crossed Cheol Mubaek’s eyes. He had watched Seowol since she was a baby. Rebuilding and reviving a fallen sect was far too heavy a burden for a girl who was not even twenty.

“You may regret the choice you’re making now.”

“But no matter what choice I make, you’ll believe in me, won’t you?”

“If I didn’t, I wouldn’t have given you the martial arts manual for the Shura Annihilating Fist.”

Seowol grasped Cheol Mubaek’s wrinkled hand.

She, too, was the daughter of a martial household. She understood what a momentous decision the old martial artist before her had made.

“Thank you, Uncle.”

At the moisture in her voice, Cheol Mubaek waved a hand.

“I’m old. I was having trouble taking on a Disciple at this point in my life anyway. This was simply a good opportunity.”

The Shura Annihilating Fist followed the principles of a single successor and transmission only to the worthy. Its intent was to find a successor of upright conduct and good character and pass the martial lineage on to them.

Yet Cheol Mubaek, the ninth-generation successor, had broken that principle and handed the martial arts manual to Seowol. Although she had not received direct instruction, he had still broken the tradition passed down through the sect’s generations.

But Cheol Mubaek had his own reasons.

*If she has the Heaven Shaking Sword and the Sleeping Dragon of Shanxi, they’ll be able to protect Seowol.*

If Seowol had decided to enter a political marriage, those two were the best options.

Their talent for martial arts went without saying, and they also possessed the chivalrous spirit to risk their lives standing against injustice.

*Still, I’ll have to watch and see what they’re really like…*

If everything went well, this could satisfy both the purpose of a political marriage and the traditions of a single successor and transmission only to the worthy.

“So, speaking of that…”

Cheol Mubaek continued in a suggestive tone.

“Which one did you choose?”

Seowol tilted her head as if she had no idea what he meant.

“My goodness. Which one?”

“Don’t play dumb. Is it the Heaven Shaking Sword? Or the Sleeping Dragon of Shanxi?”

“I’m not sure.”

“They’re both more or less the same sort, but… Wouldn’t the Heaven Shaking Sword be better?”

“You don’t like the Sleeping Dragon of Shanxi?”

“It’s not that I dislike him…”

Cheol Mubaek frowned. Even he, who spent most of the year deep in the mountains, had heard the rumors about the Jin Family of Taiyuan’s notorious delinquent.

“Even if he has truly reformed, old habits die hard. I’m worried he might break your heart someday.”

“What about the Heaven Shaking Sword?”

Cheol Mubaek’s crumpled expression smoothed out.

“They say a younger brother can’t measure up to his older brother. I spoke with him briefly yesterday, and he seems like a fine person. His talent for martial arts is outstanding.”

“I heard he knows nothing but martial arts.”

“Hey! He’s far better than chasing women. His speech and conduct are both dignified and weighty. That’s how a man ought to be, yes. Absolutely.”

Cheol Mubaek smiled contentedly.

* * *

Jin Mukyung grabbed me by the collar and shook me violently, his eyes half rolled back in his head.

“Marry her right now!”

“Cough, cough!”

Tea had gone up my nose and made me choke, and now Mukyung was shaking me by the collar without pause. I couldn’t think straight.

“Let go! Are you going to let go?”

“The Shura Annihilating Fist! The Blood Wolf Sword Technique! The Blood Wolf Footwork!”

“Fine, but let go first!”

“You stupid bastard! Do you even know what kind of martial art the Shura Annihilating Fist is?”

“Let go and then we’ll talk!”

“A single successor! Only the worthy may inherit it!”

“Enough, you crazy bastard!”

A short while later, by the time I finally pried Mukyung’s hand away, the inside of the pavilion looked as though a storm had passed through it.

“Huff… huff…”

I caught my breath and looked around.

The table had collapsed, the chairs were smashed to pieces, and fragments of broken teaware rolled across the floor.

Mukyung calmly straightened his clothes and spoke.

“Hmm. I’ve calmed down.”

“…”

This guy was even crazier than I’d thought.

I scrubbed my face with the sleeve that was relatively dry.

“Is the Shura Annihilating Fist some kind of greatest martial art in the world? Why are you so obsessed with it?”

“It was one of the ten greatest fist techniques in the world. No—it was.”

“It was?”

“It was two hundred years ago. Even in the library of Heaven’s Gate Temple, which contains thousands upon thousands of books, the only records of this martial art are written accounts. And yet the Great Hero Tiger of Mount Heng was the current successor to the Shura Annihilating Fist!”

His cheeks flushed with excitement at the thought.

I snorted the tea out of my nose and asked, “So?”

“What do you mean, ‘so’?”

Mukyung stared at me as if he couldn’t believe what he was hearing.

“I’m talking about the Shura Annihilating Fist! A Peak martial art whose lineage was believed to have died out long ago!”

“And it was one of the ten greatest fist techniques in the world two hundred years ago?”

“That’s exactly it!”

“Wait a second.”

I picked up a thick wooden stick rolling across the floor. Until five minutes ago, it had been called one of the table legs.

“Do you know what this is?”

“A club?”

“You know your stuff.”

“What does that have to do with anything?”

“Wouldn’t this have been one of the ten greatest weapons in the world around two thousand years ago?”

He wasn’t so stupid that he couldn’t understand what I was saying.

Mukyung’s eyes widened.

“How dare you compare the Shura Annihilating Fist to something like that.”

“Then what’s the difference?”

“That…”

“Of course, it’s far more valuable than a wooden club like this. But is it still the same now?”

In the past, humans fought with stones and clubs. But once bronze and iron appeared, those weapons were pushed aside by the march of the ages.

The Shura Annihilating Fist was no different.

“Of course, it’s still an outstanding Peak martial art that everyone would want.”

Cheol Mubaek himself had proven that. He had become a renowned Peak master in Shanxi Province through the Shura Annihilating Fist.

“But it isn’t still one of the ten greatest fist techniques in the world, is it?”

Just as stone and clubs had been replaced by steel, martial arts advanced as well.

I had no idea what the ten greatest fist techniques in the world were now, but Mukyung’s expression proved that I wasn’t wrong.

“To put it bluntly, if the Shura Annihilating Fist were really that powerful, Pung Yang wouldn’t have defeated him. And this is the most important part…”

I tossed the table leg carelessly into a corner and drove home the final point.

“I have no intention of getting married.”

“...!”

“If the person involved says he won’t do it, what can you do? Right?”

“Well… That’s true.”

Mukyung let out one deep sigh after another. I’d been prepared to fight him if he kept insisting, but he seemed surprisingly willing to accept it.

His wistful gaze still suggested that he couldn’t stop thinking about the martial arts manual for the Shura Annihilating Fist, though.

*This guy is a martial arts nut too.*

Then again, he had gone to Heaven’s Gate Temple because he wanted to learn more martial arts.

And now he had discovered a martial art from several hundred years ago that existed only in the records of that very same temple. Of course he couldn’t contain his excitement.

“Hoo…”

Mukyung let out a sigh deep enough to make the earth cave in and muttered,

“What a shame. What a shame.”

“It’s not that big a deal. If fate brings it around, we can get it another time.”

“You idiot. Do you think Peak martial arts just drop out of the sky?”

“Really? Mine did.”

“Even at Heaven’s Gate Temple, where all the martial arts in the world are gathered, Peak martial arts are strictly controlled… What did you say?”

“I said mine fell out of the sky.”

I pulled an old book from inside my clothes. The four characters written on its cover had been blurred by the ravages of time, but they were still clear enough to read.

**Flame Divine Palm.**

A tiger leaves its hide when it dies, and Jopil left behind Supreme Peak martial arts.

“Flame, Flame, Fla…”

Today was probably the most astonishing day of Jin Mukyung’s entire life.

I grinned at him as he stared wide-eyed, looking back and forth between me and the martial arts manual.

“From now on, call me hyung.”
```
