<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0124.txt",
      "sha256": "6ff03dc62ca26037b414c7c8ef49b4dcabdac59ff4a43612b7c84761173af595",
      "bytes": 12826
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "1d8287624ef38b640e33a9bc6da68ea4889dfa74197825189f90ce443255a2e1",
      "bytes": 4006
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "af9e46d0a4db6184b6c674d5389435ce2e4b9608a3c043ee90ef7f107c1cc8db",
      "bytes": 20466
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "537336e690e288fa4883948770498fc794163c0a42d51d9e5425a292c49e17af",
      "bytes": 5199
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "4bce71038f6327899db886f975ac931dc5dfdbedc5ec129d02e2694ce8a506bd",
      "bytes": 1421
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "596d76df0cdfbf77d70ab9b0f088745c046ce828a23304aa5a05ec765f6a0a4a",
      "bytes": 2893
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "5a807a4571d31032f8c614648ec85603a13b0da2fd3613a5dfc0784da3e6e201",
      "bytes": 1296
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "0ed2c3be8913018e2968cf98020525714f6045b4795bfcc7c1c32008efb6073f",
      "bytes": 1356
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "f6ff116b9427a11dde518246d52050139b646505ba48f53a0910f85a1403a119",
      "bytes": 2374
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "5dea745a2e714cf866b8b5b8934df5a17d2129e099c7ff3164432303d44df785",
      "bytes": 17837
    }
  ],
  "estimated_tokens": 20551
}
-->

# Durable State Update — Chapter 124

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 124. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 124. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 124,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 124,
    "continuity_sources": [124],
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
    "Cheol Mubaek and the other wounded Mount Heng martial artists are recovering; Cheol has broken limbs and serious internal injuries and needs at least four months of recuperation.",
    "Lee Seowol remains the Sect Leader of the Mount Heng Sword Sect and vows to preserve the sect for those who died defending it.",
    "The Lower District Sect sent a relief force with physicians, cooks, and laborers after the battle.",
    "Wolhwa's real name is Eun Sowol, and she is the Lower District Sect's Shanxi Branch Leader with authority over more than thirty Shanxi branches.",
    "Lee Seowol accepted Jin Wikyung's invitation to the Jin Family of Taiyuan's New Year gathering.",
    "Lee Seowol offered the Mount Heng Sword Sect's territorial rights to the Jin Family of Taiyuan as an apology.",
    "Lee Seowol proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist.",
    "Lee Seowol is seventeen years old.",
    "Jin Taekyung has decided to reject Lee Seowol's political marriage proposal because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty with its available medicine.",
    "The Lower District Sect is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued the Mount Heng Sword Sect.",
    "Cheol Mubaek is the ninth-generation successor of the Shura Annihilating Fist and gave its manual to Lee Seowol despite its inheritance traditions.",
    "Cheol Mubaek and Lee Cheonbaek first met more than thirty years ago, fought, and then became close friends.",
    "The Shura Annihilating Fist was an ancient top-ten fist technique whose lineage was believed to have ended and is no longer a current top-ten technique.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm."
  ],
  "continuity_sources": [
    123,
    122
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What is the origin and full long-term effect of the Temporary Strength Pill?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?"
  ],
  "safe_through": 123,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 호신강기 as Body-Protecting Qi.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Render 뛰어난 금창약 as Superior Wound Medicine and 십년하수오 as Ten-Year He Shouwu.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, clank, 산서성 as Shanxi Province, and 총지부장 as Chief Branch Leader.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, and 천하십대권법 as the ten greatest fist techniques in the world."
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

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이소월    | **Lee Seowol**     |
| 조필     | **Jopil**          |
| 월화     | **Wolhwa**         |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 일신     | **One God**         |
| 삼성     | **Three Saints**    |
| 십왕     | **Ten Kings**       |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 열화문    | **Fire Gate Clan**               |
| 남궁세가   | **Nangong Family**               |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 창법     | **spear technique**                              |                                                       |
| 검법     | **sword technique**                              |                                                       |
| 권법     | **fist technique**                               |                                                       |
| 비급     | **martial arts manual**                          | “martial scroll” where object/context warrants        |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 낭인     | **wandering martial artist**                     |                                                       |
| 마교     | **Demonic Cult**                                 |                                                       |
| 지부장    | **Branch Leader**                            |
| 진가창법   | **Jin Family's Spear Technique**       |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 습득               | **Acquired**                   |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 안휘     | **Anhui**              |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 구화산    | **Mount Jiuhua**       |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 본문      | **our sect / this sect**                                        |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소저      | **Young Lady**                                                  |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 122
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; stationed outside Jin Taekyung’s pavilion while Taekyung recovers
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 123
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang, was then incapacitated by five concealed throwing knives, and survived the battle to recover after Taekyung's intervention; now able to move independently
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 123
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan; dead by this chapter, having left behind the Supreme Peak martial art Flame Divine Palm
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 123
- **Aliases:** None
- **Role:** Seventeen-year-old current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady; survived Pung Yang's attack with twenty-four other identified survivors; regards the Mount Heng Sword Sect as effectively destroyed but vows to preserve it for those who died defending it; offered the sect's territorial rights to the Jin Family of Taiyuan and proposed marriage to Jin Taekyung in exchange for three Peak martial arts
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge, to whom he entrusted the Shura Annihilating Fist manual; has proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 123
- **Aliases:** Red Wind Band Leader
- **Role:** Former leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and could temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, seized Taekyung, and was killed by Taekyung after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 122
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃124화



나도 사람인지라 이틀 전 밤 이소월이 내민 세 권의 무공 비급 앞에선 마음이 흔들릴 수밖에 없었다.

자그마치 초절정 무공이다. 진가창법과 진무보법을 대성한 지금, 안 그래도 새로운 무공의 필요성을 느끼고 있던 차에 눈앞에 들이밀어진 달콤한 유혹.

‘이대로는 안 돼.’

풍양과의 싸움은 처절했다. 조필에게서 얻은 [이름 없는 검]이 아니었다면 목숨이 두 개라 해도 살아남지 못했을 것이다.

이젠 더 많은 무공을 익혀서 새로운 경지에 들어야 할 때다.

‘절정 고수.’

혈랑검법과 혈랑보법, 그리고 수라멸권은 이미 검증된 절정 무공이다. 그 높다는 절정의 벽을 허물어트릴 수 있을 만큼 단단한 망치인 것이다. 하지만…….

‘저게 망치면, 이건 포클레인이지.’

나는 손에 들린 낡은 서책을 뿌듯하게 바라봤다.

이 한 권의 무공 비급이 바로 별 미련 없이 이소월의 제안을 거절할 수 있는 이유다.

“화, 화, 화, 화…….”

한참 동안 버퍼링이 걸려 있던 진무경이 마침내 한 단어를 토해 냈다.

“화염신장!”

“오, 아네? 정답.”

200년 전의 천하십대권법도 꿰고 있는 진무경이니 화염신장을 알고 있는 건 어쩜 당연했다. 이건 그보다 훨씬 더 대단한 무공이니까.

‘아이템 확인.’

띠링.



아이템창



[화염신장]

종류 : 무공 비급

등급 : 초절정

제한 : 열양지기의 소유자

설명 : 열화문(熱火門)의 비전절기 중 하나. 강력한 화기를 바탕으로 한 무공이다.

효과 : [화염신장]의 습득





진무경이 믿기지 않는다는 얼굴로 물었다.

“네가 이걸 어떻게…….”

“어떤 고마우신 분이 주고 가셨지.”

“주고 갔다고?”

“응.”

이걸 주고 하늘나라로 훨훨 날아가셨다.

호신강기도 파괴하는 만년한철로 만들어진 [이름 없는 검], 30년의 열양지기를 얻을 수 있는 [열화신단].

마지막으로 초절정 무공인 [화염신장]까지.

나는 아낌없이 주고 떠난 조필을 생각하며 창 너머 푸른 하늘을 바라보았다.

‘잘 지내니.’

그때 진무경이 불쑥 끼어들었다.

“이제 헛소리 그만하고 사실대로 말해라. 열화문(熱火門)의 비전절기가 어떻게 네 손에 있는 거지?”

“말했잖아. 누가 주고 갔다니까.”

“지금 네가 뭘 착각하는 모양인데…….”

진무경이 심각한 얼굴로 말을 이었다.

“농으로 얼버무릴 상황이 아니다.”

“왜?”

“네가 타 문파의 무공을 훔친 도둑놈이 될 수도 있으니까. 자칫하면 본가가 천하 무림의 질타를 받게 된다.”

미처 생각지 못한 문제다.

무공은 곧 문파의 근간이자 역사다. 초절정 무공인 동시에 열화문의 비전절기라는 화염신장이야 말할 것도 없다.

“아, 젠장.”

“다시 한번 물어보마. 화염신장의 비급을 어디서, 어떻게 얻었느냐?”

나는 한숨을 푹 내쉬며 대답했다.

“조필한테서.”

“조필? 내가 알고 있는 일문일살 조필?”

“맞아. 조필을 쓰러트리고 전리품으로 얻은 거지.”

“그놈이 어떻게 화염신장의 비급을 갖고 있었는지 알고 있느냐?”

“글쎄…….”

곰곰이 생각한 끝에 그때 조필이 했던 말을 기억해 낼 수 있었다.

“자기 입으로는 본인이 화염신장의 십구 대 계승자라던데.”

“조필 같은 놈이 어찌…… 잘못 들은 건 아니냐?”

“아냐, 확실해. 거짓말하는 것 같아 보이지도 않았고.”

당시 조필은 선천지기를 끌어 올린 상태였고, 이미 빠르게 죽어 가고 있었다. 죽음을 목전에 둔 사람의 입에서 나오는 말은 대부분 진실에 가깝다.

‘물론 조필이 거짓말을 쳤을 가능성도 염두에 둬야겠지.’

그때 골똘히 생각에 잠겨 있던 진무경이 이해가 안 간다는 얼굴로 입을 열었다.

“화염신장의 계승자라는 놈이 왜 너 같은 놈한테 져?”

“…….”

음, 기분은 더럽지만 일리가 있군.

초절정 무공을 익힌 조필이 낭인 짓을 하고 있다는 것부터가 수상하긴 하다.

‘그러고 보니 검기도 제대로 못 쓰는 놈이었고.’

만나는 놈들마다 검기는 기본이요, 옵션으로 호신강기까지 달고 나오는 요즘이다. 일문일살 조필은 지금까지 내가 상대한 절정 고수 중 가장 약한 축에 속했다.

“화염신장, 이거 생각보다 약한 무공인가?”

“뭐? 화염신장이 약해?”

진무경이 별 미친놈 다 보겠다는 눈빛으로 말했다.

“정신 나간 놈. 화왕(火王)의 독문무공을 약하다고 하는 놈은 천하에 너 하나뿐일 거다.”

“화왕이 누군데.”

“장난칠 기분 아니다.”

“나돈데?”

“그만해라. 재미없으니까.”

“응. 그래서 화왕이 누구냐고.”

이번 침묵은 좀 길었다. 금붕어처럼 입만 벙긋거리던 진무경이 깊은 한숨을 뱉어 냈다.

“네 손, 발가락을 합해 봐라. 모두 몇 개냐?”

“스무 개.”

“그래, 화왕은 천하를 거꾸로 들어서 탈탈 털어도 그 안에 들어가는 고수다.”

“……오우야.”

“일신(一神), 삼성(三星), 십왕(十王). 몰라? 정말 이걸 모른다고?”

이거 아주 못 들어 봤다고 하면 모가지를 비틀어 버릴 기세다.

진무경의 고리눈에 나는 조심스럽게 입을 열었다.

“삼성은 들어 봤는데…….”

“그나마 다행이군.”

이 삼성이 그 삼성이 아니지만 어쨌든.

지금 중요한 건 그게 아니다.

“그럼 내가 화염신장을 갖고 있다는 사실을 화왕이 알게 된다면…….”

“별로 상상하고 싶지 않은 상황이 벌어지겠지.”

젠장, 천하를 통틀어 스무 손가락 안에 든다는 초절정 고수라니. 화왕이 이 사실을 알고 찾아온다면 태원진가 전체가 덤벼도 이길 수 없을 거다.

‘어떻게 얻은 무공인데…….’

익히지도 못하고 넘겨줘야 한다는 사실에 속이 쓰리던 그때였다.

나와 마찬가지로 화염신장의 비급을 안타까운 얼굴로 바라보던 진무경이 한마디를 보탰다.

“화왕이 아직까지 살아 있다면 말이다.”

“뭐?”

“화왕이 마지막으로 모습을 드러낸 것은 사십 년 전이 마지막이다.”

“사십 년 전?”

“처음 무림에 모습을 나타냈을 당시에도 화왕은 이미 노인이었다. 정마대전이 아니었다면 평생 은거기인으로 살았을지도 모르지.”

진무경의 말이 이어졌다.

“남궁세가를 패퇴시키고 안휘성(安徽城)을 점령한 마교의 사기는 하늘을 찔렀다. 수많은 약탈과 살인, 방화가 이뤄졌는데 그 과정에서 구화산(九華山)에 불을 지른 것이 화왕의 심기를 건드렸다더군.”

“그래서?”

“나흘 밤낮 동안 천 명이 죽었고, 구화산 깊숙한 곳에 은거해 있던 노인은 화왕이라는 이름을 얻었다.”

“……천 명?”

“그래. 구화산에서 입은 피해가 너무 컸던 탓에 마교는 얼마 버티지 못하고 안휘성에서 물러나야 했다.”

천 명이란 말이지…….

나는 신중한 고민 끝에 입을 열었다.

“이거, 돌려주자.”

오래 살고 싶다. 내 인생에 단신으로 천 명을 죽였다는 미친 노인네를 만나는 이벤트는 끼워 넣고 싶지 않다.

“당장 출발해야겠네. 안휘성? 아직도 거기 사신대?”

“아무도 모른다. 화왕은 그것으로 분이 안 풀렸는지 일 년 동안 눈에 보이는 마교도들을 전부 박살 내고 다시 은거했으니까.”

“열화문! 열화문에 가면 볼 수 있겠네.”

“열화문은 일인전승(一人傳承)이다. 철 대협과 비슷한 경우지.”

“…….”

돌려주고 싶어도 줄 수가 없네.

그나마 화왕과 가장 가까웠던 인물이라면 조필인데, 이미 죽고 없으니 찾을 방법이 없다.

‘가장 좋은 상황은 화왕이 이미 죽고 없는 건데…….’

사십 년 전 이미 노인이었다고 하니 충분히 가능성이 있다.

반대로 초절정 고수인 만큼 엄청나게 장수하고 있을 수도 있고.

“쓰읍.”

엄청난 보물인지, 아니면 계륵인지. 갈등 어린 눈빛으로 화염신장을 바라보는 내게 진무경이 말했다.

“만약 화왕이 죽었다면…… 네가 바로 열화문의 주인이다.”



* * *



진무경은 빠르게 회복했다. 풍양으로부터 상당한 내상을 입은 탓에 완전히 회복하기까지는 어느 정도 시간이 필요하겠지만, 태원진가로 복귀할 수 있을 만한 기력은 충분했다.

“드디어 돌아가네요.”

혁무진이 감회 어린 얼굴로 중얼거렸다.

“집 나오면 고생이라더니. 앞으로는 절대, 무조건! 본가 밖으로는 나오지 않을 겁니다.”

“……누가 보면 네가 제일 고생한 줄 알겠다, 인마.”

“왜 이러세요? 저도 나름의 고충이 있는 법입니다.”

“너 뒤에 있는 사람한테 똑같이 말해 봐.”

아직도 붕대를 풀지 못한 진무경이 나는 듯이 달려와 혁무진의 뒤통수를 갈겼다.

빡!

“컥!”

“헛소리 그만하고 말이나 몰아.”

“마부가 있는데 왜 제가…….”

혁무진의 말마따나 마부는 따로 있었다. 월화가 따로 붙여 준 하오문 소속의 문도.

그녀는 우리를 배웅하기 위해 먼저 나와 있었다.

“잘 가요. 막상 헤어지려니까 아쉽네?”

“그럼 지금이라도 같이 가실래요?”

나를 향해 눈을 찡긋하는 그녀에게 농담처럼 말을 건넸다. 아직 경계심은 남아 있지만 지난 여정으로 농담 정도는 건넬 수 있는 사이가 됐다.

“어머, 나야 그러고 싶긴 한데…… 이참에 산서 북부를 한번 쭉 돌아볼 생각이라.”

지금까지 항산검문이 철저히 통제하고 있던 산서 북부는 열린 시장이 됐다. 산서성의 총지부장인 월화가 바빠지는 것은 당연한 결과다.

“항산검문과의 일이 잘 풀렸나 보죠?”

“비밀. 명색이 총지부장인데, 제가 본문의 대외비를 외인에게 떠들고 다닐 수는 없죠.”

말은 저렇게 해도 시원시원하게 웃는 모습이 대답을 대신해 주었다.

꼬리 아홉 개가 달려 있어도 이상하지 않은 여인이니 충분히 만족스러운 결과를 얻어 냈을 것이다.

“다음에는 태원진가에서 만나겠네요.”

“아, 혹시?”

“그래도 전(前) 동맹인데, 앞으로도 계속 돈독한 관계를 유지해야 서로 좋지 않겠어요?”

새치름하게 웃은 월화가 치맛자락을 살짝 들어 올렸다.

“그때 꼭 다시 봐요. 그럼 이만.”

그녀가 미리 대기하고 있던 마차에 오르자 곧장 마부가 채찍을 휘둘렀다. 빠르게 멀어져 가는 마차를 하염없이 바라보는 두 쌍의 시선이 있었다.

“쩝. 조금만 더 있다 가시지.”

“음, 으으음.”

혁무진이야 그렇다 치고, 진무경은 도대체 왜?

아쉬움이 듬뿍 묻어 나오는 녀석의 눈빛을 바라보던 내게 문득 떠오르는 생각이 있었다.

‘저 자식, 설마…….’

월화한테 관심이 있나?

세상에, 이럴 수가. 저 무공밖에 모르는 놈이 여자한테 관심을 보이다니.

이 어마어마한 빅뉴스를 혼자만 알고 있을 수는 없다. 나는 개미만 한 목소리로 혁무진에게 바싹 가까이 다가가 아주 작게 속삭였다.

“야, 무진아.”

“아, 깜짝아. 왜요?”

“쉿. 놀라지 말고 들어라. 티 하나도 내지 마. 이건 무덤까지 안고 가야 할 비밀이야.”

혁무진이 바짝 굳은 목소리로 대답했다.

“헙, 네. 말씀하세요.”

“저 인간…… 월화 소저한테 관심 있는 것 같아.”

“…….”

“아무한테도 말하지 마라. 이거 진짜 나만 아는 비밀인데, 너한테만 알려 주는 거야.”

나의 진지한 속삭임에도 혁무진은 썩은 얼굴로 대꾸했다.

“아, 네. 감사합니다. 정말 너무 감사해서 몸 둘 바를 모르겠네요.”

아니, 이 새끼가?

저 싸가지 없는 말투를 어떻게 교정시켜 줘야 할까 고민하던 그때였다.

“은공.”

나는 천천히 돌아섰다. 눈처럼 흰 궁장을 차려입은 이소월이 그곳에 있었다.
```

## Final English reading copy

```markdown
# Chapter 124

I was only human, so I couldn’t help wavering when Lee Seowol presented me with three martial arts manuals two nights ago.

They were Supreme Peak martial arts, no less. Now that I had mastered the Jin Family’s Spear Technique and Jin Family’s Manoeuvre Technique, I had already been feeling the need to learn something new. And then, right in front of me, someone had dangled such a tempting offer.

*This won’t do.*

My fight with Pung Yang had been brutal. If I hadn’t had the Unnamed Sword I’d obtained from Jopil, I wouldn’t have survived even if I’d had two lives.

It was time to learn more martial arts and enter a new realm.

*Peak master.*

The Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist were all proven Peak martial arts. They were sturdy hammers, strong enough to break through that supposedly insurmountable wall of the Peak realm. But…

*If those are hammers, then this is an excavator.*

I gazed proudly at the old book in my hand.

This one martial arts manual was the reason I could reject Lee Seowol’s proposal without much regret.

“Fl, fl, fl, fl…”

After buffering for quite some time, Jin Mukyung finally managed to spit out a single word.

“Flame Divine Palm!”

“Oh, you know it? Correct.”

Jin Mukyung knew even the ten greatest fist techniques in the world from two hundred years ago, so perhaps it was only natural that he knew about the Flame Divine Palm. This martial art was even more incredible than those.

*Check item.*

*Ding.*



> **System**
>
> **Item Window**
>
> **Flame Divine Palm**
>
> **Type:** Martial arts manual  
> **Grade:** Supreme Peak  
> **Restriction:** Owner of Scorching Yang Qi  
> **Description:** One of the secret techniques of the Fire Gate Clan. A martial art based on powerful fire energy.  
> **Effect:** Acquisition of Flame Divine Palm.



Jin Mukyung asked with an expression of utter disbelief.

“How did you get this…?”

“Some generous soul gave it to me before he left.”

“He gave it to you?”

“Yeah.”

He gave it to me and then flew away to heaven.

The Unnamed Sword, made of Ten-Thousand-Year Cold Iron capable of destroying even Body-Protecting Qi. The Blazing Flame Divine Pill, which could grant me thirty years of Scorching Yang Qi.

And finally, the Flame Divine Palm, a Supreme Peak martial art.

Thinking of Jopil, who had given me so much before leaving this world, I gazed at the blue sky beyond the window.

*I hope you’re doing well.*

That was when Jin Mukyung abruptly cut in.

“Stop spouting nonsense and tell me the truth. How did a secret technique of the Fire Gate Clan end up in your hands?”

“I told you. Someone gave it to me before he left.”

“It seems you’re under some kind of misunderstanding…”

Jin Mukyung continued with a serious expression.

“This isn’t a situation you can gloss over with a joke.”

“Why not?”

“Because you could end up branded a thief who stole another sect’s martial arts. If things go badly, the Jin Family could be condemned by the entire Murim.”

That was a problem I hadn’t considered.

Martial arts were the foundation and history of a sect. The Flame Divine Palm was not only a Supreme Peak martial art but also a secret technique of the Fire Gate Clan. That went without saying.

“Damn it.”

“I’ll ask you one more time. Where and how did you acquire the manual for the Flame Divine Palm?”

I let out a deep sigh before answering.

“From Jopil.”

“Jopil? The One Question, One Kill Jopil I know?”

“That’s right. I defeated Jopil and obtained it as spoils.”

“Do you know how that bastard came to possess the Flame Divine Palm manual?”

“Not really…”

After thinking carefully, I remembered what Jopil had said at the time.

“He claimed he was the nineteenth-generation successor of the Flame Divine Palm.”

“How could someone like Jopil be… Are you sure you didn’t hear him wrong?”

“No, I’m sure. He didn’t look like he was lying, either.”

At the time, Jopil had been drawing on his innate qi, and he had already been dying rapidly. Words spoken by someone standing on the brink of death were usually close to the truth.

*Of course, I have to consider the possibility that Jopil was lying.*

Jin Mukyung had been lost in thought. Then he spoke with an expression of confusion.

“If he was a successor of the Flame Divine Palm, how did he lose to someone like you?”

“…”

Well, that pissed me off, but he had a point.

It was suspicious enough that Jopil had been living as a wandering martial artist despite having learned a Supreme Peak martial art.

*Now that I think about it, he couldn’t even use Sword Energy properly.*

These days, every martial artist I met came with Sword Energy as standard and Body-Protecting Qi as an optional extra. One Question, One Kill Jopil had been among the weakest Peak masters I had fought so far.

“Is the Flame Divine Palm weaker than I thought?”

“What? The Flame Divine Palm is weak?”

Jin Mukyung looked at me as if I were the craziest person he had ever seen.

“You lunatic. You’re probably the only person in the world who would call the Fire King’s signature martial art weak.”

“Who’s the Fire King?”

“I’m not in the mood for jokes.”

“Neither am I.”

“Stop it. You’re not funny.”

“Okay. So who’s the Fire King?”

This silence lasted a little longer. Jin Mukyung opened and closed his mouth like a goldfish before letting out a deep sigh.

“Count your fingers and toes. How many are there altogether?”

“Twenty.”

“Right. Even if you turned the entire world upside down and shook it out, the Fire King would still be among the twenty greatest masters in it.”

“…Whoa.”

“One God, Three Saints, Ten Kings. You’ve never heard of them? You really don’t know?”

He looked ready to twist my neck if I said I had never heard of any of them.

Under Jin Mukyung’s ringed eyes, I cautiously opened my mouth.

“I’ve heard of the Three Saints, at least…”

“That’s something.”

I meant Samsung,[^1] not the Three Saints, but whatever.

[^1]: The Korean name “Samsung” is pronounced *Samseong*, the same as the Korean term rendered here as “Three Saints.”

That wasn’t important right now.

“Then if the Fire King finds out that I have the Flame Divine Palm…”

“Something you won’t particularly want to imagine will happen.”

Damn it. A Supreme Peak master ranked among the twenty greatest experts in the entire world. If the Fire King learned about this and came looking for me, the entire Jin Family of Taiyuan could attack him together and still lose.

*After everything it took to obtain this martial art…*

My gut twisted at the thought that I might have to hand it over without even learning it.

At that moment, Jin Mukyung, who had been gazing sorrowfully at the Flame Divine Palm manual just as I was, added one more thing.

“If the Fire King is still alive.”

“What?”

“The last time the Fire King appeared was forty years ago.”

“Forty years ago?”

“When he first appeared in the Murim, the Fire King was already an old man. If not for the Great Faction War, he might have lived his entire life as a secluded eccentric.”

Jin Mukyung continued.

“The Demonic Cult’s morale soared after it defeated the Nangong Family and occupied Anhui Province. They carried out countless acts of looting, murder, and arson, and apparently, setting fire to Mount Jiuhua was what finally provoked the Fire King.”

“And then?”

“A thousand people died over four days and nights, and the old man who had been living in seclusion deep within Mount Jiuhua gained the name Fire King.”

“…A thousand people?”

“Yes. The Demonic Cult suffered such heavy losses at Mount Jiuhua that it could not hold out for long and had to withdraw from Anhui Province.”

A thousand people, huh…

After careful consideration, I opened my mouth.

“Let’s give it back.”

I wanted to live a long life. I didn’t want an event involving some insane old man who had killed a thousand people by himself added to my life.

“We should leave right away. Anhui Province? Do people still say he lives there?”

“No one knows. Perhaps that still hadn’t been enough to quell the Fire King’s anger. He spent an entire year crushing every Demonic Cult member he could find before disappearing into seclusion again.”

“The Fire Gate Clan! We can find him if we go to the Fire Gate Clan.”

“The Fire Gate Clan has a single successor. It’s a situation similar to Great Hero Cheol’s.”

“…”

Even if I wanted to return it, I had no one to give it to.

And the person who had probably been closest to the Fire King was Jopil, but he was already dead. There was no way to find him.

*The best-case scenario would be that the Fire King is already dead…*

He had already been an old man forty years ago, so it was certainly possible.

On the other hand, as a Supreme Peak master, he might have lived an extraordinarily long life.

“Hmm.”

Was this a priceless treasure or a useless burden? As I stared at the Flame Divine Palm with a conflicted expression, Jin Mukyung said,

“If the Fire King is dead… then you’re the master of the Fire Gate Clan now.”

* * *

Jin Mukyung recovered quickly. His Internal Injuries from Pung Yang had been considerable, so it would still take some time for him to recover completely, but he had enough strength to return to the Jin Family of Taiyuan.

“We’re finally going home.”

Hyuk Mujin muttered with deep emotion.

“They say leaving home means hardship. From now on, I will never, ever leave the family grounds again!”

“…Anyone listening to you would think you were the one who suffered the most, you punk.”

“What are you talking about? I have my own hardships, you know.”

“Try saying that to the person behind you.”

Jin Mukyung, who still hadn’t been able to remove his bandages, came flying over and smacked Hyuk Mujin on the back of the head.

*Whack!*

“Urk!”

“Stop spouting nonsense and drive the carriage.”

“There’s a coachman. Why do I have to…?”

Just as Hyuk Mujin said, we had a separate coachman—a member of the Lower District Sect whom Wolhwa had assigned to us.

Wolhwa had come out ahead of time to see us off.

“Goodbye. It’s a shame to part now that the time has come, isn’t it?”

“Then would you like to come with us now?”

I spoke jokingly to her as she winked at me. I was still wary of her, but after traveling together, we were close enough to exchange jokes.

“Oh, I would like that, but… I’m planning to take this opportunity to make a full tour of northern Shanxi.”

Northern Shanxi, which had been under the strict control of the Mount Heng Sword Sect until now, had become an open market. It was only natural that Wolhwa, the Lower District Sect’s Chief Branch Leader in Shanxi Province, would be busy.

“Things must have gone well with the Mount Heng Sword Sect?”

“Secret. I may be the Chief Branch Leader, but I can’t go around telling outsiders the sect’s confidential information.”

Her words said one thing, but her bright, carefree smile was answer enough.

She was the sort of woman who could have nine tails and no one would find it strange, so she had probably obtained a more than satisfactory result.

“We’ll meet again at the Jin Family of Taiyuan next time.”

“Oh, really?”

“We were allies once. Wouldn’t it be better for both of us if we continued to maintain a close relationship?”

Wolhwa gave a coy smile and lifted the hem of her skirt slightly.

“Make sure you come see me again then. Well, I’ll be off.”

As soon as she climbed into the carriage waiting nearby, the coachman cracked his whip. Two pairs of eyes gazed blankly at the carriage as it quickly disappeared into the distance.

“Tsk. She could’ve stayed a little longer.”

“Hmm. Mmm…”

Hyuk Mujin was one thing, but why was Jin Mukyung doing that?

As I watched his wistful gaze, a thought suddenly occurred to me.

*Could that bastard possibly…?*

Was he interested in Wolhwa?

Good heavens. I couldn’t believe it. The man who knew nothing but martial arts was showing an interest in a woman.

I couldn’t keep this earth-shattering news to myself. I moved close to Hyuk Mujin and whispered in a voice as small as an ant.

“Hey, Mujin.”

“Ah! You startled me. What is it?”

“Shh. Listen, but don’t be surprised. Don’t show even the slightest reaction. This is a secret we have to take to our graves.”

Hyuk Mujin answered in a stiff voice.

“Gasp. Yes. Go ahead.”

“I think that guy is interested in Young Lady Wolhwa.”

“…”

“Don’t tell anyone. This is a secret only I know, and I’m telling you alone.”

Despite my serious whisper, Hyuk Mujin replied with a sour expression.

“Oh, yes. Thank you. I’m so grateful I don’t know what to do with myself.”

*Why, this little shit…*

I was wondering how to correct that rude tone when—

“Benefactor.”

I slowly turned around.

Lee Seowol stood there, dressed in a snow-white formal robe.
```
